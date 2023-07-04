#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Load-dataset" data-toc-modified-id="Load-dataset-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Load dataset</a></span></li><li><span><a href="#Create-pipeline" data-toc-modified-id="Create-pipeline-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Create pipeline</a></span></li><li><span><a href="#Fit-pipeline" data-toc-modified-id="Fit-pipeline-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Fit pipeline</a></span></li><li><span><a href="#Serialise-model" data-toc-modified-id="Serialise-model-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Serialise model</a></span></li><li><span><a href="#Deserialise-model" data-toc-modified-id="Deserialise-model-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Deserialise model</a></span></li><li><span><a href="#Clean-up" data-toc-modified-id="Clean-up-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Clean-up</a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Model serialisation with dill
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[13]:


import pickle
import inspect
import dill
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer


# # Load dataset
# <hr style = "border:2px solid black" ></hr>

# In[3]:


data = load_iris()
X = data["data"]
y = data["target"]


# In[4]:


# Split into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y)


# # Create pipeline
# <hr style = "border:2px solid black" ></hr>

# In[5]:


#  Create a function for use with the FunctionTransformer
# Transform function that relies on imported package
def scale(X_input):
    """Scale the input matrix."""
    import os
    scale_factor = os.getenv("SCALE_FACTOR", 2)
    return X_input * scale_factor


# In[6]:


# Create a simple toy model that transforms the dataset
# and uses a random forest
model = Pipeline(
    [
        ("transform", FunctionTransformer(scale)),
        ("forest", RandomForestClassifier())
    ]
)


# # Fit pipeline
# <hr style = "border:2px solid black" ></hr>

# In[7]:


# Train the model
model.fit(X_train, y_train)


# # Serialise model
# <hr style = "border:2px solid black" ></hr>

# In[8]:


# Serialize the model using dill.
with open("model.dill", "wb") as f:
    dill.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)


# In[9]:


get_ipython().system('ls *.dill')


# # Deserialise model
# <hr style = "border:2px solid black" ></hr>

# In[10]:


with open("model.dill", "rb") as f:
    model = dill.load(f)


# In[11]:


print(model)


# In[14]:


print(inspect.getsource(model.steps[0][1].func))


# In[15]:


# Make some predictions
predictions = model.predict(X_test)


# In[16]:


predictions


# # Clean-up
# <hr style = "border:2px solid black" ></hr>

# In[17]:


get_ipython().system('ls')


# In[18]:


get_ipython().system('rm *.dill')


# In[19]:


get_ipython().system('ls')


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://flynn.gg/blog/machine-learning-model-serialization/
# 
# </font>
# </div>

# In[ ]:




