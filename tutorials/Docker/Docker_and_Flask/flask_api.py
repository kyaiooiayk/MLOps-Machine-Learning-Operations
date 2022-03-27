"""
Reference: https://github.com/krishnaik06/Dockers
"""

# Import modules
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
#import flasgger
#from flasgger import Swagger

app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# This works as a root page, meaning this is the first thing our app will show
@app.route('/')
def welcome():
    return("Welcome All!")

@app.route('/predict', methods=["Get"])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
    In this case we are going to predict a single
    class
    """
    print("******")
    print("Request received:", request)
    print("Request received with args:", request.args)
    print("******")
    
    variance=float(request.args.get("variance"))
    skewness=float(request.args.get("skewness"))
    curtosis=float(request.args.get("curtosis"))
    entropy=float(request.args.get("entropy"))
    prediction=classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return ("The answer is: " + str(prediction))
    
@app.route('/predict_file', methods=["Get"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    In this case we are going to provide
    a .csv file
    """
    
    print("******")
    print("Request received:", request)
    print("Request received with args:", request.args)
    print("Request ag value:", request.args.get("file_name"))
    print("******")
    
    df_test=pd.read_csv(request.args.get("file_name"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000)
    
    