"""
What? Deploy a model via flask in a public server (heroku)

What is interesting is that the code is first deployed in
1) local machine
2) public server

References
[article] https://towardsdatascience.com/model-deployment-using-flask-c5dcbb6499c9
[video] https://www.youtube.com/watch?v=mrExsjcvF4o
"""

# Import modules
import pandas as pd
import joblib
import flask
import re
import nltk
import numpy as np
from flask import Flask, jsonify, request
from sklearn import linear_model
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
 

# Problem statement    
"""
Kaggle Quora Insincere Questions Classification challenge.
Here an insincere question is where someone ask a question that looks like a statement
rather than to look for helpful answers.
"""


# Download and load the model
nltk.download('wordnet')
nltk.download('punkt')

clf = joblib.load('quora_model.pkl')
count_vect = joblib.load('quora_vectorizer.pkl')


# Preprocesing of the user inputted question
"""
1) converting all to lower case
2) tokenisation
3_ word lemamntisation
"""
def pre_processing(text):
    lemmatizer = WordNetLemmatizer()
    text = text.lower()
    text = re.sub('[0-9]+','num',text)
    word_list = nltk.word_tokenize(text)
    word_list =  [lemmatizer.lemmatize(item) for item in word_list]
    return ' '.join(word_list)



# How is flask calling the html file
"""
The first line @app.route (‘/index’) is a decorator, in simple words it just maps the the method defined below it to the URL mentioned inside the decorator, i.e whenever user visits that URL ‘/’ (the complete address would have an ip address and a port number as well, something like http://127.0.0.1:5000/), index() method would be called automatically, and the index() method returns our main HTML page called index.html (in our case index.html provides a text box to the user where he could enter his question)

The flask.render_template() looks for the this index.html file in the templates folder that we created in our main directory and dynamically generates/renders a HTML page for the end user, I will explain the dynamic part in a bit
"""
app = Flask(__name__)
@app.route('/')
def index():
    return flask.render_template('index.html')


"""
@app.route (‘/predict’) maps the predict() method with the /predict URL , this predict() method as the name suggests takes the input given by the user, does all the preprocessing, generates the final feature vector, runs the model on it and gets the final prediction.
"""
@app.route('/predict', methods=['POST'])
def predict():
    to_predict_list = request.form.to_dict()
    review_text = pre_processing(to_predict_list['review_text'])
    
    pred = clf.predict(count_vect.transform([review_text]))
    prob = clf.predict_proba(count_vect.transform([review_text]))
    #pr =  1
    if prob[0][0]>=0.5:
        prediction = "Positive"
        #pr = prob[0][0]
    else:
        prediction = "Negative"
        #pr = prob[0][0]

    # sanity check to filter out non questions. 
    if not re.search("(?i)(what|which|who|where|why|when|how|whose|\?)",to_predict_list['review_text']):
        prediction = "Negative"
        #prob = prob*0           
    
    return flask.render_template('predict.html', prediction = prediction, prob =np.round(prob[0][0],3)*100)


if __name__ == '__main__':
    #clf = joblib.load('quora_model.pkl')
    #count_vect = joblib.load('quora_vectorizer.pkl')
    app.run(debug=True)
    #app.run(host='localhost', port=8081)
