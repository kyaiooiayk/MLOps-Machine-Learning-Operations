#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sagemaker

# Get a SageMaker-compatible role used by this Notebook Instance.
role = sagemaker.get_execution_role()

# get a SageMaker session object, that can be
# used to manage the interaction with the SageMaker API.
sagemaker_session = sagemaker.Session()

# train a Scikit-Learn KMeans classifier on a dedicated instance
# send hyperparameter n_clusters = 3.
from sagemaker.sklearn.estimator import SKLearn

sklearn = SKLearn(entry_point='sklearn-kmeans-training-script.py', 
                  train_instance_type='ml.m4.xlarge', 
                  role=role, 
                  sagemaker_session=sagemaker_session, 
                  hyperparameters={'n_clusters': 3},
                  output_path='s3://awsml-sagemaker-results/')
 
sklearn.fit({'train': 's3://awsml-sagemaker-source/'})


# In[4]:


# create a prediction instance
predictor = sklearn.deploy(initial_instance_count=1, instance_type="ml.m4.xlarge")


# In[5]:


# load iris_test.csv from Amazon S3 and split the features 
# and target variables into separate dataframes.
import boto3
import sagemaker
import io

import pandas as pd
import numpy as np

# load training and validation dataset from Amazon S3
s3_client = boto3.client('s3')
s3_bucket_name='awsml-sagemaker-source'

response = s3_client.get_object(Bucket='awsml-sagemaker-source', Key='iris_test.csv')
response_body = response["Body"].read()
df_iris_test = pd.read_csv(io.BytesIO(response_body), header=0, index_col=False, delimiter=",", low_memory=False)

# Convert target variables 'species' from strings into integers.
from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
labelEncoder.fit(df_iris_test['species'])
df_iris_test['species'] = labelEncoder.transform(df_iris_test['species'])

# separate training anf validation dataset into separate features and target variables
# assume that the first column in each dataset is the target variable.
df_iris_features_test= df_iris_test.iloc[:,1:]
df_iris_target_test = df_iris_test.iloc[:,0]

# use the prediction instance to create predictions.
predictions = predictor.predict(df_iris_features_test.values)
print (predictions)


# In[6]:


sklearn.delete_endpoint()


# In[ ]:




