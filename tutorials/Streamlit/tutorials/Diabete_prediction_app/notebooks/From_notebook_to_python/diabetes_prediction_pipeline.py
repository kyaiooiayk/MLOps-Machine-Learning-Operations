#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Import-modules" data-toc-modified-id="Import-modules-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Import modules</a></span></li><li><span><a href="#Import-dataset" data-toc-modified-id="Import-dataset-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Import dataset</a></span></li><li><span><a href="#Data-Preprocessing" data-toc-modified-id="Data-Preprocessing-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Data Preprocessing</a></span></li><li><span><a href="#Modelling" data-toc-modified-id="Modelling-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Modelling</a></span></li><li><span><a href="#Inference" data-toc-modified-id="Inference-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Inference</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# **What?** Diabate prediction
# 
# </font>
# </div>

# # Import modules

# In[1]:


import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load


# # Import dataset

# In[2]:


data = pd.read_csv('../data/datasets_228_482_diabetes.csv')


# In[3]:


data.Outcome.value_counts()


# In[4]:


eda_profiling = ProfileReport(data)


# In[5]:


eda_profiling


# In[6]:


data.head()


# # Data Preprocessing

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - There are considerable zeros.
# - To fix this we use imputation by median.
# - We also scale the inputs to maintain the range and significance between numeric variables.
# - We could probably do more, but for the sake of this demo, we'll it as it stands.
# 
# <br></font>
# </div>

# In[7]:


data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)


# In[8]:


def impute_median(data, var):   
    temp = data[data[var].notnull()]
    temp = temp[[var, 'Outcome']].groupby(['Outcome'])[[var]].median()
    data.loc[(data['Outcome'] == 0 ) & (data[var].isnull()), var] = temp.loc[0 ,var]
    data.loc[(data['Outcome'] == 1 ) & (data[var].isnull()), var] = temp.loc[1 ,var]
    return data


# In[9]:


data = impute_median(data, 'Glucose')
data = impute_median(data, 'BloodPressure')
data = impute_median(data, 'SkinThickness')
data = impute_median(data, 'Insulin')
data = impute_median(data, 'BMI')


# In[10]:


data.head()


# In[11]:


y = data['Outcome']
x = data.drop('Outcome', axis = 1)
columns = x.columns

scaler = StandardScaler()
scaler = scaler.fit(x)
X = scaler.transform(x)
features = pd.DataFrame(X, columns = columns)


# In[12]:


dump(scaler, '../models/scaler.joblib')


# In[13]:


features.head()


# # Modelling

# In[14]:


x_train, x_test, y_train, y_test = train_test_split(features, y, test_size = 0.2, random_state = 42)


# In[15]:


model = RandomForestClassifier(n_estimators=300, bootstrap = True, max_features = 'sqrt')
model.fit(x_train, y_train)
y_pred = model.predict(x_test)


# In[16]:


print(classification_report(y_test, y_pred))


# In[17]:


dump(model, '../models/model.joblib')


# # Inference

# In[18]:


pregnancies = 2
glucose = 13
bloodpressure = 30
skinthickness = 4
insulin = 5
bmi = 5
dpf = 0.55
age = 34
feat_cols = features.columns

row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]


# In[19]:


scaler = load('../models/scaler.joblib')


# In[20]:


model = load('../models/model.joblib')


# In[21]:


feat_cols


# In[22]:


df = pd.DataFrame([row], columns = feat_cols)
X = scaler.transform(df)
features = pd.DataFrame(X, columns = feat_cols)


# In[23]:


if (model.predict(features)==0):
    print("This is a healthy person!")
else: 
    print("This person has high chances of having diabetics!")


# # References

# <div class="alert alert-block alert-warning">
# <font color=black>
# 
# - [Link to article](https://pub.towardsai.net/how-i-build-machine-learning-apps-in-hours-a1b1eaa642ed) 
# - [Link to code](https://github.com/arunnthevapalan/diabetes-prediction-app)
# 
# </font>
# </div>

# In[ ]:




