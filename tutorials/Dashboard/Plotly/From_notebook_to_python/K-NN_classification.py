#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
# 
# **What?** K-NN classification
# 
# <br></font>
# </div>

# # What is plotly?

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - The plotly Python package exists to create, manipulate and render graphical figures (i.e. charts, plots, maps and diagrams) represented by data structures also referred to as figures. 
# - The rendering process uses the Plotly.js JavaScript library under the hood although Python developers using this module very rarely need to interact with the Javascript library directly, if ever.
# - Figures can be represented in Python either as dicts or as instances of the plotly.graph_objects.Figure class.
# - Figures are are serialized as text in **JavaScript Object Notation (JSON)** before being passed to Plotly.js.
# 
# <br></font>
# </div>

# # Import modules

# In[9]:


import plotly
import dash
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# # Code requirements

# In[8]:


get_ipython().run_line_magic('load_ext', 'watermark')
import plotly,dash,numpy,sklearn
get_ipython().run_line_magic('watermark', '-p plotly,dash,numpy,sklearn')


# # Simple example - classification via k-NN

# In[10]:


mesh_size = .02
margin = 0.25

# Load and split data
X, y = make_moons(noise=0.3, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y.astype(str), test_size=0.25, random_state=0)

# Create a mesh grid on which we will run our model
x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# Create classifier, run predictions on grid
clf = KNeighborsClassifier(15, weights='uniform')
clf.fit(X, y)
Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

trace_specs = [
    [X_train, y_train, '0', 'Train', 'square'],
    [X_train, y_train, '1', 'Train', 'circle'],
    [X_test, y_test, '0', 'Test', 'square-dot'],
    [X_test, y_test, '1', 'Test', 'circle-dot']
]

fig = go.Figure(data=[
    go.Scatter(
        x=X[y==label, 0], y=X[y==label, 1],
        name=f'{split} Split, Label {label}',
        mode='markers', marker_symbol=marker
    )
    for X, y, label, split, marker in trace_specs
])
fig.update_traces(
    marker_size=12, marker_line_width=1.5,
    marker_color="lightyellow"
)

fig.add_trace(
    go.Contour(
        x=xrange,
        y=yrange,
        z=Z,
        showscale=False,
        colorscale='RdBu',
        opacity=0.4,
        name='Score',
        hoverinfo='skip'
    )
)
fig.show()


# # Deployment in DASH

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Dash is the best way to build analytical apps in Python using Plotly figures.
# - To deploy this script via DASH
# - run: **K-NN_classification_deployment_via_Dash.py**
# 
# <br></font>
# </div>

# In[12]:


get_ipython().system('ls')


# # References

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - https://plotly.com/python/knn-classification/
# 
# <br></font>
# </div>

# In[ ]:




