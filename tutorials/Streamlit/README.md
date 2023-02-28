# Streamlit
***

## Introduction
- If you’re a data scientist or a machine learning engineer, you are probably reasonably confident in your ability to build models to solve real-world business problems. But how good are you at front-end web development? 
- Can you build a visually appealing web application to showcase your models? Chances are, you may be a Python specialist, but not a front-end Javascript expert. This is where streamlit can help.
***

## Why streamlit?
- To build a web app you’d typically use such Python web frameworks as Django and Flask. But the steep learning curve and the big time investment for implementing these apps present a major hurdle. 
- **Streamlit** makes the app creation process as simple as writing Python scripts! 
- In short streamlit is a Python library you can use to build **interactive data-driven web apps**.

![image](https://user-images.githubusercontent.com/89139139/150639628-56770fb2-18cb-4a8f-9cf4-5e4b567a9a0b.png)
***

## Types of model deployment
Model deployment is the endpoint of a data science workflow. Models can be deployed as:
  - Jupyter notebooks which are commonly used for prototyping the data science workflow and they can be:
    - Uploaded to GitHub
    - Shared as a link via Google Colab
    - Shared via Binder
  - API: Models can also be deployed as a REST API using tools such as FastAPI. This approach **does not have** a frontend for displaying it graphically for ease of use.
  - Web apps. The traditional approach is to wrap the API via the use of web frameworks such as Django and Flask. A much simpler approach is to use a low-code solution such as **Streamlit** to create a web app.
***

## Four Streamlit design principles
- Embrace Python scripting. Build and grow Streamlit apps line by line.
- Treat widgets as variables. Widgets are input elements that let users interact with Streamlit apps. They’re presented as basic input text boxes, checkboxes, slider bars, etc.
- Reuse data and computation. Historically, data and computations had been cached with the @st.cache decorator. This saves computational time for app changes. It can be hundreds of times if you actively revise the app!
- Deploy instantly. Easily and instantly deploy apps with Streamlit Cloud.
***

## Installation
- Via pip as: `pip install streamlit`
***

## Bird-eye view on how to build an  app
- Create a Python script file: `app.py`. Inside this file, you can import the Streamlit library via `import streamlit as st` and use any of the available Streamlit functions
- Once the app has been coded, launching it is as easy as running `streamlit run app.py`.
***

## Available tutorials
- [k-means app](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Streamlit/tutorials/K-means_app)
- [Diabete prediction app](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Streamlit/tutorials/Diabete_prediction_app)
****

## References
- [How to master streamlit for data science](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/)
- [Build a Data-Annotation Pipeline with Less than Fifty Lines of Code with Streamlit](https://towardsdatascience.com/build-a-data-annotation-pipeline-with-less-than-fifty-lines-of-code-with-streamlit-e72a3a84e259)
- [Streamlit Guide: How to Build Machine Learning Applications](https://neptune.ai/blog/streamlit-guide-machine-learning)
- [How to buil an app leveraging the pandas profiling tool](https://github.com/dataprofessor/eda-app)
***
