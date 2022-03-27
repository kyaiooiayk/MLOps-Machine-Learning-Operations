# How to use Docker
In this tutorial we will:
    - Train a model
    - Serialise the model
    - Create an app with Flask
    - Create a Docker image for our app
    
The main goal of the tutorial is to see how a Docker image is built. The ML model is not tuned and it effectively serves as a dummy model.


## Step-by-step tutorial
- **Step #1** Train the model by running the `Model_training_and_serialisation.ipynb` notebook
- **Step #2** Run: `python flask_api.py` and past this address on your browser `http://192.168.1.15:8000/`
- **Step #3** Copy and past this address on the browser `http://192.168.1.15:8000/predict?variance=2&skewness=2&curtosis=2&entropy=1`. Look at the structure of the URL. Fisrt of all there is an `?` soon after the `predict` and then the syntax `variance=2` means that we'd like to send a request for where `variance` is assigned value 2.
- **Step #3** Copy and past this address on the browser `http://192.168.1.15:8000/predict_file?file_name=TestFile.csv` which will then returns the predicted class for the instances listed in the .csv file.
Creation of a front end
- **Step #4** Write a Docker file. This is called `Dockerfile`. Build with: `docker built -t money_api .` which essentially create a Docker image called `money_api` locally, meaning for where you ae running the command line.
- **Step #5** Load the Docker image as: `docker run -p 8000:8000 money_api` and it will give you a message like this `Running on http://172.17.0.2:8000/ (Press CTRL+C to quit)`. Now if you copy and paste this it will not work. What you have to do is paste this instead `http://localhost:8000/`. If you are on a MacOS PC and you have installed Docker, click on `OPEN IN BROWSER` one the Docker image shown.

## Troubleshooting
- If you get an erro like this: `OSError: [Errno 48] Address already in use` then follow this [link](https://ishaileshmishra.medium.com/the-python-flask-problem-socket-error-errno-48-address-already-in-use-4d074847587e) to resolve it. Essentially this appens, when you are the app for the first time, you kill the python thread and while relaunching it again.
- Option #1:
   - Try to locate the PID of the process with: `ps -fA | grep python`
   - Then kill the PID with: `kill PID`
   - If the one above does not work try: `kill -s KILL <pid>` or `kill -9 <pid>`
- Option #2:
   - Locate the PID with: `lsof -i:8050`
   -  Then shut the process with: `kill PID`

## References
- [YouTube video tutorial](https://www.youtube.com/watch?v=ipFUANeStYE)
- [GitHub code](https://github.com/krishnaik06/Dockers)
- [Dataset Link](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)
