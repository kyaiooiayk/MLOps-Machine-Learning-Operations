# Note on streamlit

## Why streamlit?
To build a web app you’d typically use such Python web frameworks as Django and Flask. But the steep learning curve and the big time investment for implementing these apps present a major hurdle. **Streamlit** makes the app creation process as simple as writing Python scripts! In short streamlit is a Python library you can use to build interactive data-driven web apps.

![image](https://user-images.githubusercontent.com/89139139/150639628-56770fb2-18cb-4a8f-9cf4-5e4b567a9a0b.png)


## Types of model deployment
Model deployment is the endpoint of a data science workflow. Models can be deployed as:

- Jupyter notebooks
- API
- Web apps

**Jupyter notebooks**. Jupyter notebooks are commonly used for prototyping the data science workflow and they can be:

- Uploaded to GitHub
- Shared as a link via Google Colab
- Shared via Binder

**API**. Models can also be deployed as a REST API using tools such as FastAPI. This approach does not have a frontend for displaying it graphically for ease of use.

**Web apps**. This brings us to deploying machine learning models as web applications. The traditional approach is to wrap the API via the use of web frameworks such as Django and Flask. A much simpler approach is to use a low-code solution such as **Streamlit** to create a web app.

## Four Streamlit design principles
- Embrace Python scripting. Build and grow Streamlit apps line by line.
- Treat widgets as variables. Widgets are input elements that let users interact with Streamlit apps. They’re presented as basic input text boxes, checkboxes, slider bars, etc.
- Reuse data and computation. Historically, data and computations had been cached with the @st.cache decorator. This saves computational time for app changes. It can be hundreds of times if you actively revise the app! In 0.89.0 release Streamlit launched two new primitives (st.experimental_memo and st.experimental_singleton) to afford a significant speed improvement to that of @st.cache.
- Deploy instantly. Easily and instantly deploy apps with Streamlit Cloud.

## Installation
- Via pip as: `pip install streamlit`

## My first app
- Create a Python script file: `app.py`. Inside this file, you can import the Streamlit library via `import streamlit as st` and use any of the available Streamlit functions
- Once the app has been coded, launching it is as easy as running `streamlit run app.py`.
- A nice example on how to buil an app leveraging the pandas profiling tool can be found [here](https://github.com/dataprofessor/eda-app)

## References
- https://blog.streamlit.io/how-to-master-streamlit-for-data-science/
