"""
What? Creation of web-based app using streamlit
"""

# Import modules
import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# STEP #0 - App description 
st.title('Diabetes Prediction App')
st.write('The model was trained on the Pima-Indian diabate dataset')
image = Image.open('data/diabetes_image.jpg')
st.image(image, use_column_width=True)
st.write('Please fill in the details of the person under consideration in the left sidebar and click on the button below!')

# STEP #1 - Optimise the app 
#Cache repetitive runs that do not change between runs
#It helps speed up the app by caching repetitive functions that don’t change between runs.

@st.cache(allow_output_mutation = True)
def load(scaler_path, model_path):
    sc = joblib.load(scaler_path)
    model = joblib.load(model_path)
    return sc , model

# STEP #2 - Understand how the app communicates with the user
def inference(row, scaler, model, feat_cols):
    df = pd.DataFrame([row], columns = feat_cols)
    X = scaler.transform(df)
    features = pd.DataFrame(X, columns = feat_cols)
    if (model.predict(features)==0):
        return "This is a healthy person!"
    else: return "This person has high chances of having diabetics!"

# STEP #3 - User inputs
age =           st.sidebar.number_input("Age in Years", 1, 150, 25, 1)
pregnancies =   st.sidebar.number_input("Number of Pregnancies", 0, 20, 0, 1)
glucose =       st.sidebar.slider("Glucose Level", 0, 200, 25, 1)
skinthickness = st.sidebar.slider("Skin Thickness", 0, 99, 20, 1)
bloodpressure = st.sidebar.slider('Blood Pressure', 0, 122, 69, 1)
insulin =       st.sidebar.slider("Insulin", 0, 846, 79, 1)
bmi =           st.sidebar.slider("BMI", 0.0, 67.1, 31.4, 0.1)
dpf =           st.sidebar.slider("Diabetics Pedigree Function", 0.000, 2.420, 0.471, 0.001)

row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]

# STEP #4 - Run the pipeline & displpay output
if (st.button('Find Health Status')):
    feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    sc, model = load('models/scaler.joblib', 'models/model.joblib')
    result = inference(row, sc, model, feat_cols)
    st.write(result)
