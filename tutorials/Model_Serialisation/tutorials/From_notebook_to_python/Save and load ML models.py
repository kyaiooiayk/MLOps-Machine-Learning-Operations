#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#References" data-toc-modified-id="References-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Save and load ML models
# 
# </font>
# </div>

# In[1]:


"""
Two methods are shown:
[1] pickle file
[2] joblib library

Pickle is the standard way of serializing objects in Python. You can use 
the pickle1 operation to serialize your machine learning algorithms and 
save the serialized format to a file.

The Joblib library is part of the SciPy ecosystem and provides utilities for 
pipelining Python jobs. It provides utilities for saving and loading Python 
objects that make use of NumPy data structures, efficiently
"""


# In[2]:


# Import python modules
from pickle import dump
from pickle import load
from pandas import read_csv
from IPython.display import Markdown, display
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[4]:


myPrint("Importing dataset")
filename = './datasetCollections/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
dataframe = read_csv(filename, names = names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
num_folds = 10
print("Input size: ", X.shape)
print("Labels size: ", Y.shape)


# In[5]:


myPrint("Create the ML model")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=7)
# Fit the model on 33%
model = LogisticRegression(max_iter = 250) 
model.fit(X_train, Y_train)
print("Model score: ", model.score(X_test, Y_test))


# In[16]:


myPrint("USING pickle")
print("Save the model to disk")
outputPath = './output/finalized_model.pkl' 
dump(model, open(outputPath, 'wb'))
print("File save at: " + outputPath)
print("load the model from disk")
loaded_model = load(open(outputPath, 'rb')) 
result = loaded_model.score(X_test, Y_test) 
print("Model score: ", result)


# In[19]:


myPrint("USING joblib")
from joblib import dump, load

# save the model to disk
outputPathJoblib = './output/finalized_model.joblib' 
print("Save the model to disk")
dump(model, outputPathJoblib)
print("File save at: " + outputPathJoblib)

# load the model from disk
print("load the model from disk")
loaded_model = load(outputPathJoblib)
result = loaded_model.score(X_test, Y_test)
print("Model score: ", result)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
# 
# </font>
# </div>

# In[ ]:




