# Flask microframework

## What is it?
- Flask is a web application framework written in Python. It has multiple modules that make it easier for a web developer to write applications without having to worry about the details like protocol management, thread management, etc.
- Flask microframework is an easy-to-use microframework that can be used to build RESTful microservices, it is a very popular framework, and it is well documented.
- Essentially, Flask is used to create the web app.
- One of the most popular types of APIs for building microservices applications is known as “RESTful API” or “REST API.” REST API is a popular standard among developers because it uses HTTP commands, which most developers are familiar with.
- **ATTENTION**: The Flask server is not powerful enough to support production loads. Instead, you should use gunicorn and nginx for proper deployment.

## Flask vs. Django
- Flask is considered more Pythonic than the Django web framework because in common situations the equivalent Flask web application is more explicit.
- Flask is also easy to get started with as a beginner because there is little boilerplate code for getting a simple app up and running.

## Tools stack
- `Flask` is used for the back-end
- `React` is used for the front-end
- `Heroku` is used for the public server deployment

## How to run
- Step #1: run this code as: python `my_app_name.py1
- Step #2: copy and past in the browser this `http://127.0.0.1:5000/`

## Troubleshooting
- If you get an erro like this: `OSError: [Errno 48] Address already in use` then follow this [link](https://ishaileshmishra.medium.com/the-python-flask-problem-socket-error-errno-48-address-already-in-use-4d074847587e) to resolve it. Essentially this appens, when you are the app for the first time, you kill the python thread and while relaunching it again.
- Option #1:
   - Try to locate the PID of the process with: `ps -fA | grep python`
   - Then kill the PID with: `kill PID`
   - If the one above does not work try: `kill -s KILL <pid>` or `kill -9 <pid>`
- Option #2:
   - Locate the PID with: `lsof -i:8050`
   -  Then shut the process with: `kill PID`

## Resources
- [list of resources](https://www.fullstackpython.com/flask.html)
- [article + code](https://towardsdatascience.com/model-deployment-using-flask-c5dcbb6499c9)
- [article + code + flask + rect](https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9)
 
