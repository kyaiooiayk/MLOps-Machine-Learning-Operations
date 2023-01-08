# How to create an app with streamlit
*Web-based app of a model built on the pima-Indian dataset*
***

## Pre-requisites
- Run `pip install pipreqs` which install only the model used in your directory (not all your packages as it happens with `pip freeze -> requirements.txt`). This will create a file called `pipreqs` containing:
```
pandas==1.2.4
joblib==0.17.0
streamlit==0.87.0
Pillow==8.3.1
```
***

## Run the app
- How to launch the app: `streamlit run app.py`
***

## Create an image with Docker
- Create a docker file called dockerfile:
```
FROM python:3.7
EXPOSE 8501
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD streamlit run app.py
```
***

## Build the  image
- The idea is this image we create is the reproducible environment irrelevant to the underlying system.
- Build the image with: `docker build --tag app:1.0`
- Run the image: `docker run --publish 8051:8051 -it app:1.0`
***

## References
- [Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
- [Link to article](https://pub.towardsai.net/how-i-build-machine-learning-apps-in-hours-a1b1eaa642ed) 
- [Link to code](https://github.com/arunnthevapalan/diabetes-prediction-app)
***