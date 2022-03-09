#---------CREATE APP WITH STREAMLIT-------
What? Web-based app of a model built on the pima-Indian dataset.
#---------------------
Technology to prouced the web ap. Steamlit
#---------------------
Link to the data: https://www.kaggle.com/uciml/pima-indians-diabetes-database)
#---------------------
Pre-requisites which can be written by:
pip install pipreqs which install only the model used in your directory (not
all your packages as it happens with pip freeze -> requirements.txt)
pipreqs .
    pandas==1.2.4
    joblib==0.17.0
    streamlit==0.87.0
    Pillow==8.3.1
    Installation with pip:
#---------------------
How to launch the app
streamlit run app.py
#---------------------


#---------CREATE A CONTAINER WITH DOCKER-------
Create a docker file called Docker
    FROM python:3.7
    EXPOSE 8501
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD streamlit run app.py
#---------------------
Building an image
The idea is this image we create is the reproducible environment irrelevant to the underlying system.
docker build --tag app:1.0 .
#---------------------
Run the image
docker run --publish 8051:8051 -it app:1.0
#---------------------