#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-wrong-with-the-Pickle-files?" data-toc-modified-id="What-is-wrong-with-the-Pickle-files?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is wrong with the Pickle files?</a></span></li><li><span><a href="#ONNX" data-toc-modified-id="ONNX-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>ONNX</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Dumping-the-model-with-pickle" data-toc-modified-id="Dumping-the-model-with-pickle-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Dumping the model with <code>pickle</code></a></span></li><li><span><a href="#Dumping-the-model-with-ONNX" data-toc-modified-id="Dumping-the-model-with-ONNX-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Dumping the model with ONNX</a></span></li><li><span><a href="#Folder-clean-up" data-toc-modified-id="Folder-clean-up-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Folder clean-up</a></span></li><li><span><a href="#References" data-toc-modified-id="References-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Model serialisation with dill
# 
# </font>
# </div>

# # What is wrong with the Pickle files?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - So the first thing I will say is that there is nothing inherently wrong with pickling your models. 
# 
# - When you pickle a model you are serializing a python object so it can be stored in a file. When you load the python object from the pickle file it will assume all the packages and functions it calls are the same. What this means is that your exported model is strongly coupled to the environment it was exported in. If you try to load your model with something like a different sklearn version, your pickle can fail to load.
# 
# - Additionally, if all you want to do is make predictions with the model (for example when creating an inference endpoint) you will still need **to download the entire sklearn package**, which is overkill.
# 
# </font>
# </div>

# # ONNX
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In contrast when you export a model to ONNX you are converting it to a set of operations that can be executed directly by the framework. 
#     
# - When you load the model there will be no assumptions on other functions or packages, it will simply execute the operations and generate your results. 
#     
# - What this means is that your model is no longer strongly coupled to your specific python environment. In fact it’s no longer coupled with Python at all, because ONNX models are portable to many different languages 
#     
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
import pickle

from skl2onnx import convert_sklearn
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from skl2onnx import get_latest_tested_opset_version
from onnxmltools.utils import save_model

import onnxruntime as ort
import numpy as np


# # Dumping the model with `pickle`
# <hr style = "border:2px solid black" ></hr>

# In[2]:


X, y = make_hastie_10_2(random_state=0)
X_train, X_test = X[:2000], X[2000:]
y_train, y_test = y[:2000], y[2000:]

clf = GradientBoostingClassifier(
    n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)

clf = clf.fit(X_train, y_train)


# In[3]:


with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)
    
with open("model.pkl","rb") as f:
    pkl_clf = pickle.load(f)

preds = pkl_clf.predict(X_train)


# # Dumping the model with ONNX
# <hr style = "border:2px solid black" ></hr>

# In[4]:


target_opset = get_latest_tested_opset_version()
n_features = X_train.shape[1]
onnx_clf = convert_sklearn(
    clf,
    "gbdt_model",
    initial_types=[("input", FloatTensorType([None, n_features]))],
    target_opset={"": target_opset, "ai.onnx.ml": 1}
)
save_model(onnx_clf, "model.onnx")


# In[5]:


sess = ort.InferenceSession("model.onnx")
preds, _ = sess.run(
    None, {"input": X_train.astype(np.float32)}
)


# # Folder clean-up
# <hr style = "border:2px solid black" ></hr>

# In[6]:


get_ipython().system('rm model.pkl')
get_ipython().system(' rm model.onnx')


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://medium.com/@liamwr17/stop-pickling-your-ml-models-use-onnx-instead-983cd4561e3a
# - [ONNX](https://onnx.ai/)
# 
# </font>
# </div>

# In[ ]:




