#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Build, Train, Deploy Machine Learning Model In AWS SageMaker.
# 
# </font>
# </div>

# # Import modules
# <hr style = "border:2px solid black" ></hr>

# In[10]:


import sagemaker
import boto3
from sagemaker.amazon.amazon_estimator import get_image_uri 
from sagemaker.session import s3_input, Session
import numpy as np
import pandas as pd
import urllib
import os
from sagemaker.predictor import csv_serializer


# # Create S3 bucket
# <hr style = "border:2px solid black" ></hr>

# In[11]:


bucket_name = 'bankapplication' # <--- CHANGE THIS VARIABLE TO A UNIQUE NAME FOR YOUR BUCKET
my_region = boto3.session.Session().region_name # set the region of the instance
print(my_region)


# In[12]:


s3 = boto3.resource('s3')
try:
    if my_region == 'us-east-1':
        s3.create_bucket(Bucket=bucket_name)
    print('S3 bucket created successfully')
except Exception as e:
    print('S3 error: ', e)


# # Map train and rest data in S3
# <hr style = "border:2px solid black" ></hr>

# In[13]:


# set an output path where the trained model will be saved
prefix = 'xgboost-as-a-built-in-algo'
output_path = 's3://{}/{}/output'.format(bucket_name, prefix)
print(output_path)


# # Downloading The Dataset And Storing in S3
# <hr style = "border:2px solid black" ></hr>

# In[14]:


try:
    urllib.request.urlretrieve(
        "https://d1.awsstatic.com/tmt/build-train-deploy-machine-learning-model-sagemaker/bank_clean.27f01fbbdf43271788427f3682996ae29ceca05d.csv", "bank_clean.csv")
    print('Success: downloaded bank_clean.csv.')
except Exception as e:
    print('Data load error: ', e)

try:
    model_data = pd.read_csv('./bank_clean.csv', index_col=0)
    print('Success: Data loaded into dataframe.')
except Exception as e:
    print('Data load error: ', e)


# # Train Test split
# <hr style = "border:2px solid black" ></hr>

# In[7]:


train_data, test_data = np.split(model_data.sample(
    frac=1, random_state=1729), [int(0.7 * len(model_data))])
print(train_data.shape, test_data.shape)


# # Saving Train And Test Into Buckets
# <hr style = "border:2px solid black" ></hr>

# In[15]:


# We start with Train Data

pd.concat([train_data['y_yes'], train_data.drop(['y_no', 'y_yes'],
                                                axis=1)],
          axis=1).to_csv('train.csv', index=False, header=False)
boto3.Session().resource('s3').Bucket(bucket_name).Object(
    os.path.join(prefix, 'train/train.csv')).upload_file('train.csv')
s3_input_train = sagemaker.s3_input(
    s3_data='s3://{}/{}/train'.format(bucket_name, prefix), content_type='csv')


# In[16]:


# Test Data Into Buckets
pd.concat([test_data['y_yes'], test_data.drop(['y_no', 'y_yes'], axis=1)], axis=1).to_csv('test.csv', index=False, header=False)
boto3.Session().resource('s3').Bucket(bucket_name).Object(os.path.join(prefix, 'test/test.csv')).upload_file('test.csv')
s3_input_test = sagemaker.s3_input(s3_data='s3://{}/{}/test'.format(bucket_name, prefix), content_type='csv')


# # Modelling
# <hr style = "border:2px solid black" ></hr>

# In[18]:


# Building Models Xgboot- Inbuilt Algorithm
# this line automatically looks for the XGBoost image URI and builds an XGBoost container.
# specify the repo_version depending on your preference.
container = get_image_uri(boto3.Session().region_name,
                          'xgboost',
                          repo_version='1.0-1')


# In[25]:


# initialize hyperparameters
hyperparameters = {
    "max_depth": "5",
    "eta": "0.2",
    "gamma": "4",
    "min_child_weight": "6",
    "subsample": "0.7",
    "objective": "binary:logistic",
    "num_round": 50
}


# In[26]:


# construct a SageMaker estimator that calls the xgboost-container
estimator = sagemaker.estimator.Estimator(image_name=container,
                                          hyperparameters=hyperparameters,
                                          role=sagemaker.get_execution_role(),
                                          train_instance_count=1,
                                          train_instance_type='ml.m5.2xlarge',
                                          train_volume_size=5,  # 5 GB
                                          output_path=output_path,
                                          train_use_spot_instances=True,
                                          train_max_run=300,
                                          train_max_wait=600)


# In[27]:


estimator.fit({'train': s3_input_train, 'validation': s3_input_test})


# # Deploy Machine Learning Model As Endpoints
# <hr style = "border:2px solid black" ></hr>

# In[28]:


xgb_predictor = estimator.deploy(
    initial_instance_count=1, instance_type='ml.m4.xlarge')


# # Prediction of the Test Data
# <hr style = "border:2px solid black" ></hr>

# In[29]:


test_data_array = test_data.drop(
    ['y_no', 'y_yes'], axis=1).values  # load the data into an array
xgb_predictor.content_type = 'text/csv'  # set the data type for an inference
xgb_predictor.serializer = csv_serializer  # set the serializer type
predictions = xgb_predictor.predict(
    test_data_array).decode('utf-8')  # predict!
# and turn the prediction into an array
predictions_array = np.fromstring(predictions[1:], sep=',')
print(predictions_array.shape)


# In[30]:


predictions_array


# - The results are not great, but our goal was just to run the model.
# - The results are not great becasue probably the dataset is imbalanced.

# In[31]:


cm = pd.crosstab(index=test_data['y_yes'], columns=np.round(predictions_array), rownames=['Observed'], colnames=['Predicted'])
tn = cm.iloc[0,0]; fn = cm.iloc[1,0]; tp = cm.iloc[1,1]; fp = cm.iloc[0,1]; p = (tp+tn)/(tp+tn+fp+fn)*100
print("\n{0:<20}{1:<4.1f}%\n".format("Overall Classification Rate: ", p))
print("{0:<15}{1:<15}{2:>8}".format("Predicted", "No Purchase", "Purchase"))
print("Observed")
print("{0:<15}{1:<2.0f}% ({2:<}){3:>6.0f}% ({4:<})".format("No Purchase", tn/(tn+fn)*100,tn, fp/(tp+fp)*100, fp))
print("{0:<16}{1:<1.0f}% ({2:<}){3:>7.0f}% ({4:<}) \n".format("Purchase", fn/(tn+fn)*100,fn, tp/(tp+fp)*100, tp))


# # Deleting The Endpoints
# <hr style = "border:2px solid black" ></hr>

# In[32]:


sagemaker.Session().delete_endpoint(xgb_predictor.endpoint)
bucket_to_delete = boto3.resource('s3').Bucket(bucket_name)
bucket_to_delete.objects.all().delete()


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [YouTube tutorial #1](https://www.youtube.com/watch?v=G3adspFQ59I)
# - [YouTube tutorial #2](https://www.youtube.com/watch?v=HuDzjNTgS2A)
# - [YouTube tutorial #3](https://www.youtube.com/watch?v=4D8mTJue9BE)
# - [YouTube tutorial #4](https://www.youtube.com/watch?v=WIZeMBxtvgM)
# - [YouTube tutorial #5](https://www.youtube.com/watch?v=zOjAdtaA3k8)
# - [YouTube tutorial #6](https://www.youtube.com/watch?v=_z220tK9u0U)
# - [YouTube tutorial #7](https://www.youtube.com/watch?v=XSsnPtHRZ6A)
# - [GutHub code](https://github.com/krishnaik06/AWS-SageMaker/blob/master/Untitled2.ipynb)
# 
# </font>
# </div>
