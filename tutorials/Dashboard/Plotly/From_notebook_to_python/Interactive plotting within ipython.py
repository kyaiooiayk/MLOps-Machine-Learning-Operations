#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
# 
# **What?** Interactive plotting within ipython
# 
# <br></font>
# </div>

# # Import modules

# In[1]:


import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor
import glob
from ipywidgets import interact, widgets
import plotly.graph_objs as go
from plotly.offline import iplot, plot, init_notebook_mode
init_notebook_mode(connected=True)
import plotly_express as px
import cufflinks as cf
#cf.go_offline(connected=True)


# # Check packages version

# In[2]:


import numpy,pandas,plotly
get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-p numpy,pandas,plotly')


# # Dataset

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - The energy data is measured every 15 minutes and includes 3 weather variables related to energy consumption: temperature, irradiance, and relative humidity. 
# - This is the data from the DrivenData Energy Forecasting competition.
# - I've cleaned up the datasets and extracted 8 features that allow us to predict the energy consumption fairly accurately.
# - Dataset refrence: https://www.drivendata.org/competitions/51/electricity-prediction-machine-learning/
# 
# <br></font>
# </div>

# In[3]:


files = glob.glob('../../DATASETS/*_energy_data.csv')
files


# In[4]:


data = pd.read_csv(files[2], parse_dates = ['timestamp'], index_col = 'timestamp').sort_index()
data.head()
data = data.rename(columns={"energy": "actual"})


# In[5]:


data.head(5)


# # Interactive plotting

# In[6]:


# Create a subset of data for plotting
data_to_plot = data.loc["2015"].copy()


def plot_timescale(timescale, selection, theme):
    """
    Plot the energy consumption on different timescales (day, week, month).
    
    :param timescale: the timescale to use
    :param selection: the numeric value of the timescale selection (for example the 15th day
    of the year or the 1st week of the year)
    :param theme: aesthetics of plot
    """
    # Subset based on timescale and selection
    subset = data_to_plot.loc[
        getattr(data_to_plot.index, timescale) == selection, "actual"
    ].copy()

    if subset.empty:
        print("Choose another selection")
        return
    
    # Make an interactive plot
    fig = subset.iplot(
            title=f"Energy for {selection} {timescale.title()}", theme=theme, asFigure=True
    )
    fig['layout']['height'] = 500
    fig['layout']['width'] = 1400
    iplot(fig)
    


_ = interact(
    plot_timescale,
    timescale=widgets.RadioButtons(
        options=["dayofyear", "week", "month"], value="dayofyear"
    ),
    # Selection 
    selection=widgets.IntSlider(value=16, min=0, max=365),
    theme=widgets.Select(options=cf.themes.THEMES.keys(), value='ggplot')
)


# # References

# <div class="alert alert-block alert-warning">
# <font color=black><br>
# 
# - https://towardsdatascience.com/how-to-generate-prediction-intervals-with-scikit-learn-and-python-ab3899f992ed<br>
# - https://nbviewer.jupyter.org/github/WillKoehrsen/Data-Analysis/blob/master/prediction-intervals/prediction_intervals.ipynb<br>
# 
# <br></font>
# </div>

# In[ ]:




