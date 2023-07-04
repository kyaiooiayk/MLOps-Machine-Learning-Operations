#!/usr/bin/env python
# coding: utf-8

# # load datasets

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import os

# Iris dataset
dataset_file = './datasets/iris_dataset/Kaggle/iris.csv'
df_iris = pd.read_csv(dataset_file)
df_iris_target = df_iris.loc[:,['species']]
df_iris_features = df_iris.drop(['species'], axis=1)


# # creating a training and validation set

# In[5]:



# using Scikit-Learn's train_test_split function.
from sklearn.model_selection import train_test_split

iris_split = train_test_split(df_iris_features, df_iris_target, 
                              test_size=0.25, random_state=17)
df_iris_features_train = iris_split[0]
df_iris_features_test = iris_split[1]
df_iris_target_train = iris_split[2]
df_iris_target_test = iris_split[3]


# In[6]:


# concatenate the features and target and 
# save training and test datasets into seperate files.
#
# Amazon Sagemaker requires that the first column of the CSV file is the target value.
df_iris_train = pd.concat([df_iris_target_train, df_iris_features_train], axis=1)
df_iris_test = pd.concat([df_iris_target_test, df_iris_features_test], axis=1)

df_iris_train.to_csv('./datasets/iris_dataset/Kaggle/iris_train.csv', index=False, header=True)
df_iris_test.to_csv('./datasets/iris_dataset/Kaggle/iris_test.csv', index=False, header=True)


# In[ ]:




