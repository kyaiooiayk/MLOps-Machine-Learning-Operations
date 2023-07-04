#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sagemaker

# Get a SageMaker-compatible role used by this Notebook Instance.
role = sagemaker.get_execution_role()

# get a SageMaker session object, that can be
# used to manage the interaction with the SageMaker API.
sagemaker_session = sagemaker.Session()

# create a training job to train a KMeans model using
# Amazon SageMaker's own implementation of the k-means algorithm
#
# set hyperparameter k = 3
from sagemaker import KMeans

input_location = 's3://awsml-sagemaker-source/iris-train.csv'
output_location = 's3://awsml-sagemaker-results'

kmeans_estimator = KMeans(role=role,
                train_instance_count=1,
                train_instance_type='ml.m4.xlarge',
                output_path=output_location,
                k=3)


# In[2]:


import boto3
import io
import pandas as pd
import numpy as np

# load training and validation dataset from Amazon S3
s3_client = boto3.client('s3')
s3_bucket_name='awsml-sagemaker-source'

response = s3_client.get_object(Bucket='awsml-sagemaker-source', Key='iris_train.csv')
response_body = response["Body"].read()
df_iris_train = pd.read_csv(io.BytesIO(response_body), header=0, delimiter=",", low_memory=False)

response = s3_client.get_object(Bucket='awsml-sagemaker-source', Key='iris_test.csv')
response_body = response["Body"].read()
df_iris_test = pd.read_csv(io.BytesIO(response_body), header=0, index_col=False, delimiter=",", low_memory=False)

# Convert target variables 'species' from strings into integers.
from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
labelEncoder.fit(df_iris_train['species'])
labelEncoder.fit(df_iris_test['species'])
df_iris_train['species'] = labelEncoder.transform(df_iris_train['species'])
df_iris_test['species'] = labelEncoder.transform(df_iris_test['species'])

# separate training and validation dataset into separate features and target datasets
# assuming that the first column of the iris_train.csv and iris_test.csv files
# contains the target attribute.
#
# since training a k-means classifier does not require labelled training data,
# you will not make use of df_iris_target_train

df_iris_features_train= df_iris_train.iloc[:,1:]
df_iris_target_train = df_iris_train.iloc[:,0]

df_iris_features_test= df_iris_test.iloc[:,1:]
df_iris_target_test = df_iris_test.iloc[:,0]

# create a training job.
train_data = df_iris_features_train.values.astype('float32')
record_set = kmeans_estimator.record_set(train_data)
kmeans_estimator.fit(record_set)


# In[3]:


# deploy the model to a prediction instance
# and create a prediction endpoint.
predictor = kmeans_estimator.deploy(initial_instance_count=1, instance_type="ml.m4.xlarge")


# In[4]:


test_data = df_iris_features_test.values.astype('float32')

predictions = predictor.predict(test_data)
print (predictions)


# In[5]:


# terminate the prediction instance and associated
# HTTPS endpoint.
kmeans_estimator.delete_endpoint()


# In[ ]:




