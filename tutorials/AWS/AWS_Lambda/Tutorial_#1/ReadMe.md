# Tutorial #1 
![GitHub](https://img.shields.io/github/license/lloydhamilton/aws_lambda_no_authoriser?logo=GitHub&style=plastic) ![GitHub Repo stars](https://img.shields.io/github/stars/lloydhamilton/aws_lambda_no_authoriser?logo=GitHub&style=plastic) ![](https://img.shields.io/badge/-Docker-blue?style=plastic&logo=Docker) ![](https://img.shields.io/badge/-AWS-orange?style=plastic&logo=Amazon-AWS)

How to deploy a ML model on AWS Lambda.

## Introduction
How to deploy a ML model on AWS as a lambda function which is the AWS serverless offering. First a AWS CLI is set up locally. Next, we will train a K-nearest neighbour classifier which is then deploy via a Docker container.

## Setting up your workspace
- Sign up to the [AWS free tier account](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).
- Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Setup [AWS CLI](https://medium.com/@lloyd.hamilton/setting-up-aws-cli-credentials-65d0a5fc0c4e)
- Install [AWS Serverless Application Model (SAM) CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Install [Docker](https://docs.docker.com/get-docker/)

## Step-by-step guide
This main aim is the following: lay down the steps required to deploy a simple ML model as a Lambda function on AWS. Serverless deployment of ML models — 1) Test data is uploaded to a S3 bucket. 2) To initiate the lambda function, a POST HTTP request is sent through the Amazon API Gateway. 3) Initialisation of the lambda function executes code that downloads the data from the S3 bucket and performs predictions. 4) A HTTP response is returned to client with the predictions as a data payload. (Image by author)
![image](https://user-images.githubusercontent.com/89139139/159281026-10f4b7d9-76f2-404a-a82e-79acce068cd3.png)

  - **Step #1**: It assumed a ML was trained. The only extra step which is required here is to save the model locally. 
  ```
  import joblib
  joblib.dump(my_ML_object, 'my_ML_name.joblib')
  ```
  - **Step #2** See my [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Docker) on how to Dockerise your ML. Since what goes inside a Docker file depends on the ML application, only a representative example (taken from [here](https://docs.docker.com/compose/gettingstarted/)) is here reported:
 ```
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
 ```
  - **Step #3** Let’s initialise a S3 bucket with the code below. The bucket contains some data will be feeding the ML model with to make some inferences. To do so, we will be interacting with AWS using the AWS Python SDK boto3. This package contains all the dependencies we require to integrate Python projects with AWS. 
```
import boto3

def create_bucket(region:str, my_bucket_name:str) -> dict:

    s3 = boto3.client('s3')
    response = s3.create_bucket(
        Bucket=my_bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint':region
        }
    )
    return response

region = 'eu-west-2'
bucket_name = 'lh-lambda-buckets-2022'
create_bucket(region, bucket_name)
```
  - **Step #4** We now have to write a function to upload to the S3 bucket the file object for inference. The bucket variable defines the destination S3 bucket and the key variable will define the file path in the bucket. The bucket and key variables will form part of the data payload in the POST HTTP request to our lambda function.
```
from io import BytesIO
import joblib
import boto3

def UploadToS3(data, bucket:str, key:str):

    with BytesIO() as f:
        joblib.dump(data, f)
        f.seek(0)
        (
            boto3
            .client('s3')
            .upload_fileobj(Bucket=bucket, Key=key, Fileobj=f)
        )

bucket_name = 'lh-lambda-buckets-202222'
key =  'validation/test_features.joblib'
UploadToS3(test_features, bucket_name, key)
```

  - **Step #5** We can check if the objects have been uploaded with the helper function which lists all objects in the bucket.
```
import boto3

def listS3Objects(bucket:str) -> list:

     # Connect to s3 resource
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)

    # List all object keys in s3 bucket
    obj_list = [object_summary.key for object_summary in my_bucket.objects.all()]
    return obj_list

listS3Objects('lh-lambda-buckets-2022')
```
  - **Step #6** Deploying and Testing AWS Lambda Functions with SAM. AWS SAM is an open source framework used to build serverless applications. It streamlines the build and deploy a serverless architecture by unifying all the tools all within a YAML configuration file. There is another packaged called [serverless](https://www.serverless.com/) which works with AWS, Azure and Google. Amazon provides an [official guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html) on how to configure a AWS SAM yaml file. Here is what goes into `template_no_auth.yaml`. As the name suggests it does not include resources that performs server side authentication of API requests. Therefore, deployment of our lambda function at its current state will allow anyone with the URL to make a request to your function.
    - [AWSTemplateFormatVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html) where you specified the latest template available.
    - [Transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html) which identifies an AWS CloudFormation template file as an AWS SAM template file and is a requirement for SAM template files.
    - [Globals](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy-globals.html) variables to be used by specific resources can be defined here. Function timeout and the memory size is set to 50 and 5000 MB respectively. When the specified timeout is reached, the function will stop execution.
    - [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) sets the default staging value to dev. You can define parameter values which can be referenced in the yaml file.
    - [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html) is used to declare the specific AWS resources we require for our application: API gateway and lambda function.
    - In the outputs section we declared a set of outputs to return after deploying the application with SAM. In this case the output returns the URL of the API endpoint to invoke the lambda function.
```
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Globals:
  Function:
    Timeout: 50
    MemorySize: 5000
  Api:
    OpenApiVersion: 3.0.1
Parameters:
  Stage:
    Type: String
    Default: dev
Resources:
  # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
  LambdaAPI:
    Type: AWS::Serverless::Api
    Properties:
      StageName: !Ref Stage
  # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
  PredictFunction:
    Type: AWS::Serverless::Function
    Properties:
      PackageType: Image
      Architectures:
        - x86_64
      Events:
        Predict:
          Type: Api
          Properties:
            RestApiId: !Ref LambdaAPI
            Path: /predict
            Method: POST
      Policies:
        - AmazonS3FullAccess
    Metadata:
      Dockerfile: Dockerfile
      DockerContext: ./
      DockerTag: python3.9-v1
Outputs:
  LambdaApi:
    Description: "API Gateway endpoint URL for Dev stage for Predict Lambda function"
    Value: !Sub "https://${LambdaAPI}.execute-api.${AWS::Region}.amazonaws.com/${Stage}/predict"
```
  - **Step #7** The `lambda_predict.py` file contains steps that perform the following steps:
    - Load the model
    - Download the test_features data set referenced by the bucket and key variable
    - Perform a prediction on the downloaded data set
    - Return JSON object of the predictions as a numpy array
```
from io import BytesIO
import json
import boto3
import joblib
import logging

# Define logger class
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Helper function to download object from S3 Bucket
def DownloadFromS3(bucket:str, key:str):
    s3 = boto3.client('s3')
    with BytesIO() as f:
        s3.download_fileobj(Bucket=bucket, Key=key, Fileobj=f)
        f.seek(0)
        test_features  = joblib.load(f)
    return test_features

# Load model into memory
logger.info('Loading model from file...')
knnclf = joblib.load('knnclf.joblib')
logger.info('Model Loaded from file...')

def lambda_handler(event, context):

    # Read JSON data packet
    data = json.loads(event['body'])
    bucket = data['bucket']
    key = data['key']

    # Load test data from S3
    logger.info(f'Loading data from {bucket}/{key}')
    test_features = DownloadFromS3(bucket, key)
    logger.info(f'Loaded {type(key)} from S3...')

    #  Perform predictions and return predictions as JSON.
    logger.info(f'Performing predictions...')
    predictions = knnclf.predict(test_features)
    response = json.dumps(predictions.tolist())

    return {
        'statusCode': 200,
        'headers':{
            'Content-type':'application/json'
        },
        'body': response
    }
```
  - **Step #8** The Dockerfile details the instructions required to containerised our lambda function as a docker image. I will be using Python 3.9 and installing the python dependencies using poetry. Key thing to note, the entry point for the docker image is set to the lamba_handler function which is declared in the lambda_predict.py file. This entry point defines the function to be executed during an event trigger, an event such as a HTTP POST request. Any code outside of the lambda_handler function that is within the same script will be executed when the container image is initialised. 
```
# Install python
FROM public.ecr.aws/lambda/python:3.9

# Install poetry
RUN pip install "poetry==1.1.11"

# Install dependencies, exclude dev dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy required files
COPY app ./

# Set entry point
CMD ["lambda_predict.lambda_handler"]
```
  - **Step #9** AWS SAM provide functionality to build and locally test applications before deployment. After making sure your docker is running:
    - Build the application in SAM: `sam build -t template_no_auth.yaml`
    - Locally deploy the dockerised lambda function: `sam local start-api`
    - On your local web browser type (your URL may differ): `http://127.0.0.1:3000/predict` 
```
import requests
import json
import numpy as np

bucket_name = 'lh-lambda-buckets-202222'
key =  'validation/test_features.joblib'

data = {
    'bucket':bucket_name,
    'key':key,
}

headers = {
    'Content-type': "application/json"
}

# Main code for post HTTP request
url = "http://127.0.0.1:3000/predict"
response = requests.request("POST", url, headers=headers, data=json.dumps(data))

# Show confusion matrix and display accuracy
lambda_predictions = np.array(response.json())
show_cm(test_target, lambda_predictions, range(10))
```
  - **Step #10** Deploying on AWS Lambda. As easy as it was to deploy locally, SAM will also handle all the heavy lifting to deploy on AWS Lambda.
    - Build the application in SAM: `sam build -t template_no_auth.yaml`
    - Deploy the application: `sam deploy --guided` Follow the prompts that guides you through the deployment configurations. Most of the settings I used were the default value with a few exceptions.
```
Stack Name [sam-app]: predict-no-auth
AWS Region [eu-west-2]:
Parameter Stage [dev]: 
Confirm changes before deploy [y/N]: 
Allow SAM CLI IAM role creation [Y/n]: 
Disable rollback [y/N]: y
PredictFunction may not have authorization defined, Is this okay? [y/N]: y
Save arguments to configuration file [Y/n]: 
SAM configuration file [samconfig.toml]: 
SAM configuration environment [default]:
Create managed ECR repositories for all functions? [Y/n]:
```

## References
- [Serverless Deployment of Machine Learning Models on AWS Lambda](https://towardsdatascience.com/serverless-deployment-of-machine-learning-models-on-aws-lambda-5bd1ca9b5c42)
