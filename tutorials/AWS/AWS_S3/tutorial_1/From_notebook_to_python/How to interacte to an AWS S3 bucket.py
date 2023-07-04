#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-AWS-S3-and-boto3" data-toc-modified-id="What-is-AWS-S3-and-boto3-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is AWS S3 and boto3</a></span></li><li><span><a href="#Import-modules" data-toc-modified-id="Import-modules-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Import modules</a></span></li><li><span><a href="#Create-a-bucket-via-AWS-console" data-toc-modified-id="Create-a-bucket-via-AWS-console-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Create a bucket via AWS console</a></span></li><li><span><a href="#Conncet-to-the-S3-bucket" data-toc-modified-id="Conncet-to-the-S3-bucket-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conncet to the S3 bucket</a></span></li><li><span><a href="#Inspect-what-buckets-are-available" data-toc-modified-id="Inspect-what-buckets-are-available-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Inspect what buckets are available</a></span></li><li><span><a href="#Create-a-syntetic-dataframe" data-toc-modified-id="Create-a-syntetic-dataframe-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Create a syntetic dataframe</a></span></li><li><span><a href="#Upload-files-to-S3-bucket" data-toc-modified-id="Upload-files-to-S3-bucket-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Upload files to S3 bucket</a></span><ul class="toc-item"><li><span><a href="#Update-large-files" data-toc-modified-id="Update-large-files-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Update large files</a></span></li></ul></li><li><span><a href="#Retrieve-file-from-S3-bucket" data-toc-modified-id="Retrieve-file-from-S3-bucket-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Retrieve file from S3 bucket</a></span></li><li><span><a href="#Download-from-S3-and-dump-locally" data-toc-modified-id="Download-from-S3-and-dump-locally-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Download from S3 and dump locally</a></span></li><li><span><a href="#References" data-toc-modified-id="References-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to interacte to an AWS S3 bucket
# 
# </font>
# </div>

# # What is AWS S3 and boto3
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - S3 stands for Simple Storage Service. Amazon S3 is a key-value, object-based storage service.
# - `boto3` is nothing more than a python library used to interact (create/upload/download and more) with an AWS S3 bucket.
# 
# </font>
# </div>

# # Import modules
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - To install `boto3` and `s3fs` simply use:
#     - `pip install boto3`
#     - `pip install s3fs`
# 
# </font>
# </div>

# In[1]:


import boto3
import pandas as pd
import s3fs
import os


# # Create a bucket via AWS console
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - You can create a bucket in two ways:
#     - Log into your AWS console and created a S3 bucket from there. This is what you are supposed to this in this tutorial.
#     - Crate a bucket via boto3. This is not done here. Please see this other [notebook](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/AWS/AWS_Lambda/Tutorial_%231/tutorial_1_files/Step_2_Deploying%20k-NN%20model%20on%20AWS.ipynb) to know how to do it.
# - Information such as `aws_access_key_id` and `aws_secret_access_key` can be obtained from the Identity and Access Management (IAM) in your AWS console. If you have done it before, you probably have saved this information locally in a .csv file
#     
# </font>
# </div>

# # Conncet to the S3 bucket
# <hr style = "border:2px solid black" ></hr>

# In[2]:


s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)


# <div class="alert alert-info">
# <font color=black>
# 
# - Alternatively, you can add your variable to your urrent environment once which then simplify your s3 conncetion via boto3.
# - Please keep in mind that both `aws_access_key_id` and `aws_secret_access_key` should not shared! They are here reported just to remind you how the look like. The use associated to them no longer exists.
# 
# </font>
# </div>

# In[3]:


os.environ["AWS_DEFAULT_REGION"] = 'eu-west-2'
os.environ["AWS_ACCESS_KEY_ID"] = ''
os.environ["AWS_SECRET_ACCESS_KEY"] = ''

s3 = boto3.resource(
    service_name='s3'
)


# # Inspect what buckets are available
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - The bucket showns in the print out below are those that are available to a specific user whose `aws_access_key_id` and `aws_secrete_access_key` have been provided.
#     
# </font>
# </div>

# In[4]:


# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


# # Create a syntetic dataframe
# <hr style = "border:2px solid black" ></hr>

# In[5]:


# Make dataframes
foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})

# Save locally to csv
foo.to_csv('foo.csv')
bar.to_csv('bar.csv')


# In[6]:


foo.head()


# In[7]:


bar.head()


# In[8]:


# Check the file were dumped
get_ipython().system('ls ')


# # Upload files to S3 bucket
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - `aws-s3-26` is our bucket.
# - `foo.csv` and `bar.csv` are the files we want to upload to the S3 bucket.
# 
# </font>
# </div>

# In[9]:


s3.Bucket('aws-s3-26').upload_file(Filename='foo.csv', Key='foo.csv')
s3.Bucket('aws-s3-26').upload_file(Filename='bar.csv', Key='bar.csv')


# In[10]:


# Verifying tfhe files were successfully uploaded
for obj in s3.Bucket('aws-s3-26').objects.all():
    print(obj)


# ## Update large files

# In[ ]:


from boto3.s3.transfer import TrasnferConfig
boto3.client("s3").uploadfile(Bucket="bucket_name", 
                              Key="path_ouput", 
                              Filename="path_input", 
                              Config=TransferConfig(5*(1024**3)),
                              ExtraArgs={"ACL": "bucket-owner-full-control"})


# # Retrieve file from S3 bucket
# <hr style = "border:2px solid black" ></hr>

# In[11]:


obj = s3.Bucket('aws-s3-26').Object('foo.csv').get()
foo = pd.read_csv(obj['Body'], index_col=0)


# In[12]:


obj = s3.Bucket('aws-s3-26').Object('bar.csv').get()
bar = pd.read_csv(obj['Body'], index_col=0)


# In[13]:


foo.head()


# In[14]:


bar.head()


# # Download from S3 and dump locally
# <hr style = "border:2px solid black" ></hr>

# In[15]:


s3.Bucket('aws-s3-26').download_file(Key='foo.csv', Filename='foo1.csv')
s3.Bucket('aws-s3-26').download_file(Key='bar.csv', Filename='bar1.csv')


# In[16]:


pd.read_csv('foo1.csv', index_col=0)


# In[17]:


pd.read_csv('bar1.csv', index_col=0)


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [YouTube video | Tutorial 1- Cloud Computing-AWS-Introduction To S3(Simple Storage Services)](https://www.youtube.com/watch?v=G3adspFQ59I)
# - [YouTube video | Tutorial 3- Deployment Of ML Models In AWS EC2 Instance](https://www.youtube.com/watch?v=JKlOlDFwsao)
# - [GitHub code](https://github.com/krishnaik06/AWS/blob/main/boto3%20read%20S3.ipynb)
# 
# </font>
# </div>

# In[ ]:




