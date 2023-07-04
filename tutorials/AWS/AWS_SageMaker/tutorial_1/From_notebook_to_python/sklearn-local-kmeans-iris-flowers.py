#!/usr/bin/env python
# coding: utf-8

# In[23]:


import boto3
import sagemaker
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

# separate training anf validation dataset into separate features and target variables
# assume that the first column in each dataset is the target variable.
df_iris_features_train = df_iris_train.iloc[:,1:]
df_iris_target_train = df_iris_train.iloc[:,0]

df_iris_features_test= df_iris_test.iloc[:,1:]
df_iris_target_test = df_iris_test.iloc[:,0]

# create a KMeans multi-class classifier.
from sklearn.cluster import KMeans

kmeans_model = KMeans(n_clusters=3)
kmeans_model.fit(df_iris_features_train, df_iris_target_train.values.ravel())

# use the  model to create predictions on the test set
kmeans_predictions = kmeans_model.predict(df_iris_features_test)

# compute confusion matrix
from sklearn.metrics import confusion_matrix
cm_kmeans = confusion_matrix(df_iris_target_test.values.ravel(), kmeans_predictions)


# In[24]:


# print predicted classes
print (kmeans_predictions)


# In[25]:


# print expected classes
print (df_iris_target_test.values.ravel())


# In[26]:


# print confusion matrix
print(cm_kmeans)

