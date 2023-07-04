#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
# 
# **What?** Quick introduction to Plotly
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


# # Code requirements

# In[4]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-p plotly')


# # Simple example - plotting a line

# In[7]:


fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
print(fig)
fig.show()


# # Deployment in DASH

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Dash is the best way to build analytical apps in Python using Plotly figures.
# - To deploy this script via DASH
# - run: **Quick_introduction_to_Plotly_deployment_via_dash**
# 
# <br></font>
# </div>

# In[1]:


get_ipython().system('ls')


# # References

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - https://plotly.com/python/figure-structure/
# 
# <br></font>
# </div>

# In[ ]:




