#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** Build k-NN model applied to MNIST
# 
# </font>
# </div>

# # Import modules
# <hr style = "border:2px solid black" ></hr>

# In[1]:


from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import joblib


# # Read-in dataset
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - For this classification project, we will be using the MNIST data set that contain 70,000 images of handwritten digits. In this data set, each row represents an image and each column a pixel from a 28 by 28 pixel image. The MNIST dataset is widely used to train classifiers and can be fetched using the helper function sklearn.datasets.fetch_openml.
# 
# - The code below will download the data, and sample 20,000 rows from the original dataset. I will be reducing the number of rows in the dataset to decrease model size and to reduce build time for this project. The code below will also plot the first image in the data set which we can see is the number eight.
#   
# </font>
# </div>

# In[2]:


# Load data
mnist = fetch_openml("mnist_784", version=1)

# Randomly sample 20000 rows from the original dataset
mnist_data = (
    mnist
    .data
    .sample(n=20000, random_state=42, axis=0, replace=False)
)

# Slice target by the same row sampling
target = (
    mnist
    .target
    .loc[mnist_data.index].astype('uint8')
)


# In[3]:


# Reshape values to be 28x28
some_digit_image = (
    mnist_data
    .iloc[0]
    .values
    .reshape(28, 28)
    .astype('float32')
)
plt.imshow(some_digit_image, cmap="binary")
plt.axis("off")


# # Training a k-NN Classifier
# <hr style = "border:2px solid black" ></hr>

# In[4]:


def train_knn_model(features: np.array, target: np.array):
    """
    Function to train KNN Classifier and show scores
    """
    # Train KNN Classifier
    knnclf = KNeighborsClassifier(weights='distance', n_neighbors=4)
    knnclf.fit(features, target)
    scores = cross_val_score(
        knnclf, features, target, scoring='accuracy', cv=10
    )
    print(f'Cross Validation Scores: {scores}')
    print(f'Average accuracy: {np.mean(scores)}')
    return knnclf, scores


# In[5]:


# Split data to training and test set
train_features, test_features, train_target, test_target = train_test_split(
    mnist_data, target, test_size=0.2, random_state=42
)
knnclf, scores = train_knn_model(train_features, train_target)


# <div class="alert alert-info">
# <font color=black>
# 
# - The model achieves a decent average accuracy of 96% from cross validation. 
# - Let's evaluate the model's performance on the test_features data set and plot a confusion matrix with the show_cm function as shown below.
#     
# </font>
# </div>

# In[6]:


def show_cm(y_true, y_pred, labels):
    """
    Display Confusion matrix and show accuracy scores
    """
    conf_mat = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=conf_mat, display_labels=labels)
    score = accuracy_score(y_true, y_pred)
    print(f'Accuracy: {score}')
    disp.plot()


# In[15]:


# Make predictions
#print(test_features)
test_target_pred = knnclf.predict(test_features)
# Show confusion matrix
show_cm(test_target, test_target_pred, range(10))


# <div class="alert alert-info">
# <font color=black>
# 
# - Base on the accuracy on the test data set, we can see that our model fits the data. We get very similar prediction accuracy when comparing accuracies between the training and testing set. 
# 
# - Furthermore, a confusion matrix, like above, is very effective in helping visualise the gaps in the model's performance. It will help us understand the kind of errors that the classifier is making.
# 
# - The matrix indicates that there were 16 instances where the number 4 was misidentified for the number 9, and 12 instances where the number 8 was misidentified for the number 5. 
# 
# - Looking at the images below, it is possible to see why some of these errors may occur as the number 4 and 9 do share some similar features. Likewise for the number 8 and 5.
#     
# </font>
# </div>

# In[8]:


def show_digits(pixel_vals):

    some_digit_image = (
        pixel_vals
        .values
        .reshape(28, 28)
        .astype('float32')
    )
    plt.imshow(some_digit_image, cmap="binary")
    plt.axis("off")


# In[9]:


fours = train_features[train_target == 4]
nines = train_features[train_target == 9]
eights = train_features[train_target == 8]
fives = train_features[train_target == 5]

plt.figure(figsize=(8, 8))
plt.subplot(221)
show_digits(fours.iloc[0])
plt.subplot(222)
show_digits(nines.iloc[0])
plt.subplot(223)
show_digits(eights.iloc[1])
plt.subplot(224)
show_digits(fives.iloc[1])


# This insight is not going to affect model deployment on AWS but will help guide strategies to further improve the model. 
# For now, we will save the model locally to be containerised as part of the lambda function using Docker.

# # Model serialisation
# <hr style = "border:2px solid black" ></hr>

# In[10]:


joblib.dump(knnclf, 'app/knnclf.joblib')


# In[11]:


get_ipython().system('mkdir validation')


# In[12]:


joblib.dump(test_features, 'validation/test_features.joblib')


# In[13]:


get_ipython().system('ls app')


# In[14]:


get_ipython().system('ls validation')


# # Check file loading from joblib
# <hr style = "border:2px solid black" ></hr>

# In[16]:


test_target_pred = knnclf.predict(joblib.load('validation/test_features.joblib'))
# Show confusion matrix
show_cm(test_target, test_target_pred, range(10))


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Blog post](https://towardsdatascience.com/serverless-deployment-of-machine-learning-models-on-aws-lambda-5bd1ca9b5c42)
# - [Github code](https://github.com/lloydhamilton/aws_lambda_no_authoriser)
# 
# </font>
# </div>
