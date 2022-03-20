# FastAPI

## Introduction
What if you want to integrate your machine learning model into a larger software solution instead of a simple standalone web application (in this case streamlit would suffice)? What if you are working alongside a software engineer who is building a large application and needs to access your model through a REST API? This exactly where FastAPI comes into play.

## What is FastAPI?
FastAPI is a Python web framework that makes it easy for developers to build fast (high-performance), production-ready REST APIs. If you’re a data scientist who works mostly with Python, FastAPI is an excellent tool for deploying your models as REST APIs. FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data, and automatically auto-generate OpenAPI documents. It fully supports asynchronous programming and can run with Uvicorn and Gunicorn. FastAPI is lighter weight than Django, offers similar features (along with API style) to Flask but was built with async in mind. 

## What is Uvicorn and gunicorn?
Gunicorn is a mature, fully featured server and process manager. Uvicorn includes a Gunicorn worker class allowing you to run ASGI applications, with all of Uvicorn's performance benefits, while also giving you Gunicorn's fully-featured process management.

## References
- [FastAPI wiki](https://en.wikipedia.org/wiki/FastAPI)
- [FastAPI official website](https://fastapi.tiangolo.com/)


