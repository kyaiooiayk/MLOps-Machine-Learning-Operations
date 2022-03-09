"""
Two lines require explanation:
from flask_cors import CORS
CORS(app)

This is meant to get rid of the annoying CORS error we always get
when we’re making an API request to a different domain. At this 
current stage (before deployment), React is running on port 3000 
and Flask on port 5000. Hence, when React is making a request to 
Flask backend, this CORS error pops up.
"""


# Import modules
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
#from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler

"""
The static_url_path can be used to specify a different path 
for the static files on the web and it defaults to the name 
of the static_folder folder. 
"""
app = Flask(__name__, static_url_path = '', static_folder = 'frontend/build')
#CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')
