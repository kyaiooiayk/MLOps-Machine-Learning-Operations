#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Intoduction on Pandera
# 
# </font>
# </div>

# # Import modules
# <hr style = "border:2px solid black" ></hr>

# In[1]:


# pip install pandera 
# pip inarLL ipytest
import pandas as pd
import pandera as pa
from pandera import Column, Check
from pandera.typing import Series
import ipytest
import numpy as np


# # What is Pandera
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - In a data science project, it is not only important to test your functions, but it is also important to test your data to make sure they work as you expected.
# - One option is Great Expectations but for a small data science project, this can be an overkill.
# - An alternative is a simple Python library for validating a pandas DataFrame called: `pandera`.
# 
# </font>
# </div>

# # Dummy dataset creation
# <hr style = "border:2px solid black" ></hr>

# In[2]:


fruits = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Aldi", "Walmart", "Walmart", "Aldi"],
        "price": [2, 1, 3, 4],
    }
)

fruits


# # Simple checks
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Scenario: your manager told you that there can only be certain fruits and stores in the dataset, and the price must be less than 4.
# - To make sure your data follow these conditions, checking your data manually can cost too much time, especially when your data is big. Is there a way that you can automate this process?
# - That is when Pandera comes in handy. Specifically, we:
#     - Create multiple tests for the entire dataset using `DataFrameSchema`
#     - Create multiple tests for each column using `Column`
#     - Specify the type of test using `Check`
# - Since not all values in the column price are less than 4, the test fails.
# 
# </font>
# </div>

# In[3]:


available_fruits = ["apple", "banana", "orange"]
nearby_stores = ["Aldi", "Walmart"]


# In[4]:



schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(str, Check.isin(nearby_stores)),
        "price": Column(int, Check.less_than(4)),
    }
)
schema.validate(fruits)


# <div class="alert alert-info">
# <font color=black>
# 
# - If we use `5` instead of `4` then the test will pass.
# 
# </font>
# </div>

# In[5]:


schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(str, Check.isin(nearby_stores)),
        "price": Column(int, Check.less_than(5)),
    }
)
schema.validate(fruits)


# <div class="alert alert-info">
# <font color=black>
# 
# - We can also create custom checks using lambda. 
# - In the code below, we are going to check if the sum of the column price is less than 20.
# 
# </font>
# </div>

# In[6]:


schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(str, Check.isin(nearby_stores)),
        "price": Column(
            int, [Check.less_than(5), Check(lambda price: sum(price) < 20)]
        ),
    }
)
schema.validate(fruits)


# # Schema Model

# <div class="alert alert-info">
# <font color=black>
# 
# - When our tests are complicated, using dataclass can make our tests look much cleaner than using a dictionary. 
# - Luckily, Pandera also allows us to create tests using a dataclass instead of a dictionary.
# 
# </font>
# </div>

# In[7]:


class Schema(pa.SchemaModel):
    name: Series[str] = pa.Field(isin=available_fruits)
    store: Series[str] = pa.Field(isin=nearby_stores)
    price: Series[int] = pa.Field(le=5)

    @pa.check("price")
    def price_sum_lt_20(cls, price: Series[int]) -> Series[bool]:
        return sum(price) < 20


Schema.validate(fruits)


# # Validation Decorator 

# ## Check Input

# In[8]:




ipytest.autoconfig()


# In[9]:


fruits = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Aldi", "Walmart", "Walmart", "Aldi"],
        "price": [2, 1, 3, 4],
    }
)

schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(str, Check.isin(nearby_stores)),
        "price": Column(int, Check.less_than(5)),
    }
)


def get_total_price(fruits: pd.DataFrame, schema: pa.DataFrameSchema):
    validated = schema.validate(fruits)
    return validated["price"].sum()


get_total_price(fruits, schema)


# In[10]:


get_ipython().run_cell_magic('ipytest', '-qq', 'def test_get_total_price():\n    fruits = pd.DataFrame({\'name\': [\'apple\', \'banana\'], \'store\': [\'Aldi\', \'Walmart\'], \'price\': [1, 2]})\n    \n    schema = pa.DataFrameSchema(\n        {\n            "name": Column(str, Check.isin(available_fruits)),\n            "store": Column(str, Check.isin(nearby_stores)),\n            "price": Column(int, Check.less_than(5)),\n        }\n    )\n    assert get_total_price(fruits, schema) == 3')


# In[ ]:


from pandera import check_input, check_output, check_io

fruits = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Aldi", "Walmart", "Walmart", "Aldi"],
        "price": ["2", "1", "3", "4"],
    }
)


@check_input(schema)
def get_total_price(fruits: pd.DataFrame):
    return fruits.price.sum()


get_total_price(fruits)


# In[11]:


get_ipython().run_cell_magic('ipytest', '-qq', "def test_get_total_price():\n    fruits = pd.DataFrame({'name': ['apple', 'banana'], 'store': ['Aldi', 'Walmart'], 'price': [1, 2]})\n    assert get_total_price(fruits) == 3")


# ## Check Output

# In[12]:


fruits_nearby = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Aldi", "Walmart", "Walmart", "Aldi"],
        "price": [2, 1, 3, 4],
    }
)

fruits_faraway = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Whole Foods", "Whole Foods", "Schnucks", "Schnucks"],
        "price": [3, 2, 4, 5],
    }
)

out_schema = pa.DataFrameSchema(
    {"store": Column(str, Check.isin(["Aldi", "Walmart", "Whole Foods", "Schnucks"]))}
)


@check_output(out_schema)
def combine_fruits(fruits_nearby: pd.DataFrame, fruits_faraway: pd.DataFrame):
    fruits = pd.concat([fruits_nearby, fruits_faraway])
    return fruits


combine_fruits(fruits_nearby, fruits_faraway)


# ## Check Both

# In[13]:


in_schema = pa.DataFrameSchema({"store": Column(str)})

out_schema = pa.DataFrameSchema(
    {"store": Column(str, Check.isin(["Aldi", "Walmart", "Whole Foods", "Schnucks"]))}
)


@check_io(fruits_nearby=in_schema, fruits_faraway=in_schema, out=out_schema)
def combine_fruits(fruits_nearby: pd.DataFrame, fruits_faraway: pd.DataFrame):
    fruits = pd.concat([fruits_nearby, fruits_faraway])
    return fruits


combine_fruits(fruits_nearby, fruits_faraway)


# # Other Arguments for Column Validation

# ## Deal with Null Values

# In[14]:


fruits = fruits = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Aldi", "Walmart", "Walmart", np.nan],
        "price": [2, 1, 3, 4],
    }
)

fruits


# In[15]:


schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(str, Check.isin(nearby_stores)),
        "price": Column(int, Check.less_than(5)),
    }
)
schema.validate(fruits)


# In[16]:


schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(str, Check.isin(nearby_stores), nullable=True),
        "price": Column(int, Check.less_than(5)),
    }
)
schema.validate(fruits)


# ## Deal with Duplicates

# In[17]:


schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store": Column(
            str, Check.isin(nearby_stores), nullable=True, allow_duplicates=False
        ),
        "price": Column(int, Check.less_than(5)),
    }
)
schema.validate(fruits)


# ## Convert Data Types

# In[18]:


fruits = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store": ["Aldi", "Walmart", "Walmart", "Aldi"],
        "price": [2, 1, 3, 4],
    }
)

schema = pa.DataFrameSchema({"price": Column(str, coerce=True)})
validated = schema.validate(fruits)
validated.dtypes


# ## Patern Matching

# In[19]:


favorite_stores = ["Aldi", "Walmart", "Whole Foods", "Schnucks"]

fruits = pd.DataFrame(
    {
        "name": ["apple", "banana", "apple", "orange"],
        "store_nearby": ["Aldi", "Walmart", "Walmart", "Aldi"],
        "store_far": ["Whole Foods", "Schnucks", "Whole Foods", "Schnucks"],
    }
)

schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.isin(available_fruits)),
        "store_+": Column(str, Check.isin(favorite_stores), regex=True),
    }
)
schema.validate(fruits)


# # Export and Load From a YAML file

# <div class="alert alert-info">
# <font color=black>
# 
# - Using a YAML file is a neat way to show your tests to colleagues who don’t know Python. 
# - We can keep a record of all validations in a YAML file using 
# 
# </font>
# </div>

# ## Export

# In[20]:


yaml_schema = schema.to_yaml()
print(yaml_schema)


# In[23]:


from pathlib import Path

f = Path("schema.yml")
f.touch()
f.write_text(yaml_schema)


# ## Load

# In[24]:


with f.open() as file:
    yaml_schema = file.read()


# In[25]:


schema = pa.io.from_yaml(yaml_schema)
schema


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Blog article](https://towardsdatascience.com/validate-your-pandas-dataframe-with-pandera-2995910e564)
# - [GitHub code](https://github.com/khuyentran1401/Data-science/tree/master/data_science_tools/pandera_example)
# 
# </font>
# </div>
