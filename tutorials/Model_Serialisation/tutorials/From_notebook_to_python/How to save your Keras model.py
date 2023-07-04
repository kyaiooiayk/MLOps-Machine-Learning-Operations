#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#How-to-save-your-Keras-model" data-toc-modified-id="How-to-save-your-Keras-model-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>How to save your Keras model</a></span></li><li><span><a href="#Import-modules" data-toc-modified-id="Import-modules-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Import modules</a></span></li><li><span><a href="#HDF5-&amp;-JASON-format" data-toc-modified-id="HDF5-&amp;-JASON-format-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>HDF5 &amp; JASON format</a></span></li><li><span><a href="#YAML-format" data-toc-modified-id="YAML-format-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>YAML format</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to save your Keras model
# 
# </font>
# </div>

# # How to save your Keras model
# <hr style = "border:2px solid black" ></hr>

# 
# <div class="alert alert-info">
# <font color=black>
# 
# - Keras separates the concerns of saving your model architecture and saving your model weights. Model weights are saved to HDF5 format. 
# 
# - This is a  grid format that is ideal for storing multi-dimensional arrays of numbers.
# 
# - The model structure can be described and saved (and loaded) using two  different formats: JSON and YAML.
#     
# - Saving and loading your model weights to HDF5 formatted files.
# 
# </font>
# </div>

# # Import modules
# <hr style = "border:2px solid black" ></hr>

# In[20]:


from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.models import model_from_yaml
import numpy
import os


# # HDF5 & JASON format
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The Hierarchical Data Format or HDF5 for short is a flexible data storage format and is convenient for storing large arrays of real values, as we  have in the weights of neural networks.
# 
# - JSON is a simple file format for describing data hierarchically. 
# 
# </font>
# </div>

# In[4]:


# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load pima indians dataset
dataset = numpy.loadtxt("../DATASETS/pima-indians-diabetes.csv", delimiter=",")

# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

# create model
model = Sequential()
model.add(Dense(12, input_dim = 8, kernel_initializer = "uniform" , activation = "relu" ))
model.add(Dense(8, kernel_initializer = "uniform" , activation = "relu" ))
model.add(Dense(1, kernel_initializer = "uniform" , activation = "sigmoid" ))    


# Compile model
model.compile(loss= "binary_crossentropy" , optimizer= "adam" , metrics=["accuracy"])

# Fit the model
model.fit(X, Y, epochs=150, batch_size=10, verbose=0)

# evaluate the model
scores = model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# In[7]:


# serialize model to JSON
model_json = model.to_json()
with open("../OUTPUT/model.json", "w") as json_file:
    json_file.write(model_json)

# serialize weights to HDF5
model.save_weights("../OUTPUT/model.h5")
print("Saved model to disk")


# In[11]:


# later...
# load json and create model

json_file = open("../OUTPUT/model.json" ,  "r" )
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")   

# evaluate loaded model on test data
loaded_model.compile(loss= "binary_crossentropy" , optimizer= "rmsprop" , metrics=["accuracy"])
score = loaded_model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))


# # YAML format
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - This example is much the same as the above JSON example, except the YAML format is used for the model specification. 
# 
# - The model is described using YAML, saved to file model.yaml and later loaded into a new model via the model from yaml() function. 
# 
# - Weights are handled in the same way as above in HDF5 format as model.h5.
# 
# </font>
# </div>

# In[17]:


# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("../DATASETS/pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

# create model
model = Sequential()
model.add(Dense(12, input_dim = 8, kernel_initializer = "uniform" , activation = "relu" ))
model.add(Dense(8, kernel_initializer = "uniform" , activation = "relu" ))
model.add(Dense(1, kernel_initializer = "uniform" , activation = "sigmoid" ))    

# Compile model
model.compile(loss= "binary_crossentropy" , optimizer= "adam" , metrics=[ "accuracy" ])

# Fit the model
model.fit(X, Y, epochs =150, batch_size=10, verbose=0)

# evaluate the model
scores = model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# serialize model to YAML
model_yaml = model.to_yaml()
with open("model.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)

# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")


# In[21]:


# later...
# load YAML and create model
yaml_file = open( "model.yaml" ,  "r" )
loaded_model_yaml = yaml_file.read()
yaml_file.close()

loaded_model = model_from_yaml(loaded_model_yaml)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss= "binary_crossentropy" , optimizer= "rmsprop" , metrics=[ "accuracy" ])
score = loaded_model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))


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




