# Basic ML Model deployment using Flask
Tutorial for Deploying a Basic ML model using flask
***

## Steps #1 - Install package locally
- Create a clean new virtual environment:
- `pip install joblib`
- `pip install Flask`
- `pip install numpy`
- `pip install pandas`
- `pip install scikit_learn`
- `pip install gunicorn`
***

## Step #2 - Create a requirement.txt
- Create a file called `requirements.txt` with the following content:
```
joblib==0.13.2
Flask==1.0.3
numpy==1.17.2
pandas==0.25.1
scikit_learn==0.21.3
gunicorn==19.9.0
```
- New user will just have to create a virtual environment and then run `pip install requirements.txt `
***

## Step #3 - Buid & save model 
- All the step to create this simple model are inside this python file: `model.py`
- Run the model with: `python model.py` which will output a `model.pkl` file

## Step #4 - Run the Flask app locally
- Execute flask app: `python app.py` which will automatically run on port 5000
- Open in web browser `http://localhost:5000/` and try the app

## Step #5 - Sign up tp  pythonanywhere
- Sign-up [here](https://www.pythonanywhere.com/pricing/) and choose the beginner plan which is totally free.
- A limited account with one web app at `<your-username>.pythonanywhere.com`, restricted outbound Internet access from your apps, low CPU/bandwidth, no IPython/Jupyter notebook support.
***

## Step #6 - setup a virtual environment
- Under the`Start a new console` tab clock on `bash`
- Make virtual environment: `mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv`
- Install required dependencies: `pip install scikit_learn flask joblib`. Alternatively, load the `requirements.txt`.
- Go under the `Files` tab and take note of where this newly created mesh is located: `/home/<your_user_name>/.virtualenvs/my-virtualenv`
***

## Step #7 - Configure the Web host
- Under `Web` tab click on `Add a new web app`
- Because the account is on its "Beginner" tier, our app URL will have our login name in it: `your_user_name.pythonanywhere.com`
- Click on manual configuration.
- Select the same python version used when the virtual environment was created.
- Under `Code`, on `WSGI configuration file`, click on `/var/www/<your_user_name>_pythonanywhere_com_wsgi.py`
- Delete the following code:
```
HELLO_WORLD = """<html>
<head>
...
...
</p>
</body>
</html>"""


def application(environ, start_response):
    if environ.get('PATH_INFO') == '/':
    ....
    ....
    yield content.encode('utf8')
```
- Uncomment the following and modify the `path` along with the name of the app:
```
import sys

path = '/home/kyaiooiayk/
if path not in sys.path:
    sys.path.append(path)

from app import app as application  # noqa
```
- Navigate to the `Virutalenv` and past there the path of your virtual environment.
***

## Step #8 - Configure the file
***
- Under the `File` tab click on `Upload a file`
- Upload the `app.py`
- Upload the `model.pkl`
- Create a new folder called `templates` under the file `tab` and then `Directories` tab. 
- Upload `index.html` located in your `templates` local folder.
- Now go back under the `Web` tab and click the hyperlink under the `Reload` tab.
- Click on the `<your_userna,e>.pythonanywhere.com` hyperlink and you should be able to see the html file you uploaded above.
***

## Step #9 - Try up on the publish host
- Navigate to `<your_user_name>.pythonanywhere.com` and try out the app.
- Mine is can be access [here](http://kyaiooiayk.pythonanywhere.com/)
***

## References
- [Salary regressor article](https://medium.com/@kaustuv.kunal/how-to-deploy-and-host-machine-learning-model-de8cfe4de9c5)
- [Salary regressor GitHub](https://github.com/kaustuvkunal/BasicMLModelFlaskDeploy)
- [Salary regressor YouTube](https://www.youtube.com/watch?v=6tvJJ9-yojk&feature=youtu.be)
***



