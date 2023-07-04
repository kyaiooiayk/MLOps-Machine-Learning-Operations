#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-model-persistance?" data-toc-modified-id="What-is-model-persistance?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is model persistance?</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Load-dataset-and-fit-a-dummy-model" data-toc-modified-id="Load-dataset-and-fit-a-dummy-model-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Load dataset and fit a dummy model</a></span></li><li><span><a href="#pickle" data-toc-modified-id="pickle-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>pickle</code></a></span></li><li><span><a href="#joblib" data-toc-modified-id="joblib-6"><span class="toc-item-num">6&nbsp;&nbsp;</span><code>joblib</code></a></span></li><li><span><a href="#skops" data-toc-modified-id="skops-7"><span class="toc-item-num">7&nbsp;&nbsp;</span><code>skops</code></a></span></li><li><span><a href="#Clean-up" data-toc-modified-id="Clean-up-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Clean-up</a></span></li><li><span><a href="#Conclusions" data-toc-modified-id="Conclusions-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Conclusions</a></span></li><li><span><a href="#References" data-toc-modified-id="References-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Model serialisation with pickle, joblib, skops
# 
# </font>
# </div>

# # What is model persistance?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - After training a scikit-learn model, it is desirable to have a way to persist the model for future use without having to retrain. 
# - The following sections give you some hints on how to persist a scikit-learn model.
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from sklearn import svm
from sklearn import datasets
import pickle
from joblib import dump, load
import skops.io as sio


# # Load dataset and fit a dummy model
# <hr style = "border:2px solid black" ></hr>

# In[2]:


clf = svm.SVC()
X, y = datasets.load_iris(return_X_y=True)
clf.fit(X, y)


# # `pickle`
# <hr style = "border:2px solid black" ></hr>

# In[3]:


s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print("prediction", clf2.predict(X[0:1]))
print("target: ", y[0])


# # `joblib`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# 
# - In the specific case of scikit-learn, it may be better to use joblib’s replacement of pickle (dump & load), which is more efficient on objects that carry large numpy arrays internally as is often the case for fitted scikit-learn estimators, but can only pickle to the disk and not to a string.
# 
# </font>
# </div>

# In[4]:


dump(clf, './filename.joblib')


# In[5]:


get_ipython().system('ls *.joblib')


# In[6]:


clf3 = load('filename.joblib') 


# In[7]:


print("prediction", clf3.predict(X[0:1]))
print("target: ", y[0])


# # `skops`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `skops` provides a more secure format via the skops.io module. 
# - It avoids using pickle and only loads files which have types and references to functions which are trusted either by default or by the user. 
# 
# </font>
# </div>

# In[8]:


obj = sio.dumps(clf)


# In[11]:


unknown_types = sio.get_untrusted_types(obj)
clf = sio.loads(obj, trusted=unknown_types)


# In[12]:


clf = sio.loads(obj, trusted=True)


# In[13]:


print("prediction", clf.predict(X[0:1]))
print("target: ", y[0])


# # Clean-up
# <hr style = "border:2px solid black" ></hr>

# In[ ]:


get_ipython().system('rm *.jobliv')


# In[ ]:


get_ipython().system('ls *.joblib')


# # Conclusions
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-danger">
# <font color=black>
# 
# - `pickle` (and `joblib` by extension), has some issues regarding maintainability and security. Because of this,
#     - Never unpickle untru sted data as it could lead to malicious code being executed upon loading.
#     - While models saved using one version of scikit-learn might load in other versions, this is entirely unsupported and inadvisable. It should also be kept in mind that operations performed on such data could give different and unexpected results.
# 
# </font>
# </div>

# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Model persistance in scikit-learn](https://scikit-learn.org/stable/model_persistence.html)
# 
# </font>
# </div>

# In[ ]:




