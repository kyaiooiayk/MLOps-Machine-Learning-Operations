# Creating a basic app
***

## Goal
- We are going to a machine model called `GuassianNB`.
- The dataset used is the iris dataset which is available striaght fom sklearn so we avoid having to download on disk some data.
***

## Create the model
- Create a file called `ML_model.py` and fit the data.
- Please note that our goal is to simple get something off the ground, hence we are not following the normal must-do checks like data splitting etc, overfitting checks etc ...
```
# Imports
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# Loading Iris Dataset
iris = load_iris()

# Getting features and targets from the dataset
X = iris.data
Y = iris.target

# Fitting our Model on the dataset
clf = GaussianNB()
clf.fit(X,Y)
```
***

## Create a request & response and bodies
- The data sent from the client side to the API is called a **request body**. The data sent from API to the client is called a response body. 
- To define our request body we’ll use BaseModel, in pydantic module, and define the format of the data we’ll send to the API. 
- To define our request body, we’ll create a class that inherits BaseModel and define the features as the attributes of that class along with their type hints.
- What pydantic does is that it defines these type hints during runtime and generates an error when data is invalid.
```
from pydantic import BaseModel

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
```

## Creating and end point
- A model endpoint is a simple way to create inferences.
- The endpoint willl predict the class and return it as a response.
```
@app.post('/predict')
def predict(data : request_body):
    test_data = [[
            data.sepal_length, 
            data.sepal_width, 
            data.petal_length, 
            data.petal_width
    ]]
    class_idx = clf.predict(test_data)[0]
    return { 'class' : iris.target_names[class_idx]}
```
***

## Firying your app
- Run your app with: `uvicorn basic-app:app --reload`
- `basic-app` refers to the name of the the `*.py` file
- `app` refers to the FastAPI instantiation name.
- `–reload` tells to restart the server every time we reload.
- Copy and past this address in yor browser: `http://127.0.0.1:8000/`
***

## Interactive API app calls
- FastAPI comes with Interactive API docs which can access by adding `/docs` in your path as in: `http://127.0.0.1:8000/docs`. 
- Here you’ll get a webpage where you can test the endpoints of your API by seeing the output.
*** 


## Troubleshooting
- If you get an erro like this: `OSError: [Errno 48] Address already in use` then follow this [link](https://ishaileshmishra.medium.com/the-python-flask-problem-socket-error-errno-48-address-already-in-use-4d074847587e) to resolve it. Essentially this appens, when you fire the app for the first time, you kill the python thread and relaunching it again.
- Option #1:
   - Try to locate the PID of the process with: `ps -fA | grep python`
   - Then kill the PID with: `kill PID`
   - If the one above does not work try: `kill -s KILL <pid>` or `kill -9 <pid>`
- Option #2:
   - Locate the PID with: `lsof -i:8050`
   -  Then shut the process with: `kill PID`
***

## Refereces
- [Deploying ML Models as API using FastAPI](https://www.geeksforgeeks.org/deploying-ml-models-as-api-using-fastapi/?ref=rp)
- [What is a model endpoint?](https://medium.com/@starpebble/what-is-a-model-endpoint-101cd264d96f)
***
