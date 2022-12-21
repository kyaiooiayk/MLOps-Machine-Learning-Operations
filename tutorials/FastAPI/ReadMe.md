# FastAPI
***

## Introduction
- What if you want to integrate your machine learning model into a larger software solution instead of a simple standalone web application?
- What if you are working alongside a software engineer who is building a large application and needs to access your model through a REST API? This exactly where FastAPI comes into play.
***

## What is FastAPI?
- FastAPI is a Python web framework that makes it easy for developers to build fast (high-performance), production-ready REST APIs. If you’re a data scientist who works mostly with Python, FastAPI is an excellent tool for deploying your models as REST APIs. 
- FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data, and automatically auto-generate OpenAPI documents. 
- It fully supports asynchronous programming and can run with Uvicorn and Gunicorn. 

## FastAPI vs. Django vs. Flask
- Django is usually used for large scale application and takes quite a bit time to set up that.
- Flask is usually your go-to for quickly deploying your model on a web app. 
- FastAPI is lighter weight than Django, offers similar features (along with API style) to Flask but was built with async in mind. 
- FastAPI is way faster than Flask, not just that it’s also one of the fastest python modules out there.
- Unlike Flask, FastAPI provides an easier implementation for Data Validation to define the specific data type of the data you send.
- Automatic Docs to call and test your API(Swagger UI and Redoc).
- FastAPI comes with built-in support for Asyncio, GraphQL and Websockets.
***

## What is uvicorn and gunicorn?
- Gunicorn is a mature, fully featured server and process manager. 
- Uvicorn includes a Gunicorn worker class allowing you to run ASGI applications, with all of Uvicorn's performance benefits, while also giving you Gunicorn's fully-featured process management.
***

## Installation
- Install can be done with: `pip install fastapi uvicorn`
***

## References
- [FastAPI wiki](https://en.wikipedia.org/wiki/FastAPI)
- [FastAPI official website](https://fastapi.tiangolo.com/)
- [Deploying ML Models as API using FastAPI](https://www.geeksforgeeks.org/deploying-ml-models-as-api-using-fastapi/?ref=rp)
***

