# Imports
from fastapi import FastAPI
import uvicorn

# Instaniate your FastAPI instance
app = FastAPI()

# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to kyaiooiayk!'}

# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name : str):
    # Defining a function that takes only string as input and output the following message.
    return {'message': f'Welcome to kyaiooiayk! Provided input:, {name}'}