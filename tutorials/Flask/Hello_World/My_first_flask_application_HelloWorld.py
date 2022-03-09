"""
My first code with Flask
The code just prints "hello world!" in a web page
Reference code: https://www.fullstackpython.com/flask.html

Step #1: run this code as: python helloWorld.py
Step #2: copy and past in the webbroser this http://127.0.0.1:5000/
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()