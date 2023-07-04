#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#With-pydantic" data-toc-modified-id="With-pydantic-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>With pydantic</a></span></li><li><span><a href="#How-pydantic-fails" data-toc-modified-id="How-pydantic-fails-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>How pydantic fails</a></span></li><li><span><a href="#Field-and-some-weird-behaviour-with-&quot;_&quot;" data-toc-modified-id="Field-and-some-weird-behaviour-with-&quot;_&quot;-5"><span class="toc-item-num">5&nbsp;&nbsp;</span><code>Field</code> and some weird behaviour with "_"</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Pydantic introduction
# 
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[37]:


from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import Field


# # With pydantic
# <hr style="border:2px solid black"> </hr>

# In[21]:


class User(BaseModel):
    item_id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


# In[22]:


external_data = {
    'item_id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}


# In[23]:


user = User(**external_data)


# In[25]:


user.dict()


# # How pydantic fails
# <hr style="border:2px solid black"> </hr>

# In[26]:


external_data = {
    'item_id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, 'not number'],
}


# In[27]:


user = User(**external_data)


# In[28]:


try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())


# # `Field` and some weird behaviour with "_"
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - pay attention if your variable start with an `_` as in `_id`
# - Surprisingly (or at least surprising to me), Pydantic hides fields that start with an underscore (regardless of how you try to access them).
# - To be able to use those variables you need to use an alias with `Field`
# 
# </font>
# </div>

# In[29]:


class User(BaseModel):
    _id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


# In[32]:


external_data = {
    '_id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, 3],
}


# In[33]:


user = User(**external_data)


# In[35]:


# where is _id?
user.dict()


# In[102]:


class Item(BaseModel):
    _id: str
    is_available: bool  # 1


# In[103]:


item1 = Item(_id='test-item-id', is_available=True) 


# In[104]:


# where is _id?
item1.dict()


# In[108]:


class Item(BaseModel):
    item_id: str = Field(alias="_id")
    is_available: bool  # 1


# In[109]:


item1 = Item(_id='test-item-id', is_available=True) 


# In[110]:


# where is _id?
item1.dict()


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Pydantic official documentation](https://docs.pydantic.dev/latest/)
# - [Cool things you can do with Pydantic](https://medium.com/swlh/cool-things-you-can-do-with-pydantic-fc1c948fbde0)
# 
# </font>
# </div>

# In[ ]:




