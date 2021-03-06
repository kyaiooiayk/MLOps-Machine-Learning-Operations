# Tutorial #1 
![](https://img.shields.io/badge/-Docker-blue?style=plastic&logo=Docker) ![](https://img.shields.io/badge/-AWS-orange?style=plastic&logo=Amazon-AWS)

How to deploy a ML model on AWS Lambda.
<hr>

## Introduction
How to deploy a ML model on AWS as a lambda function which is the AWS serverless offering. First a AWS CLI is set up locally. Next, we will train a k-NN classifier which is then deploy via a Docker container.

## Setting up your workspace
- Sign up for a [AWS free tier account](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).
- Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Setup [AWS CLI](https://medium.com/@lloyd.hamilton/setting-up-aws-cli-credentials-65d0a5fc0c4e)
- Install [AWS Serverless Application Model (SAM) CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Install [Docker](https://docs.docker.com/get-docker/)

## Step-by-step guide
  - **Step #1**: It is assumed a ML is trained. The only extra step which is required out of what is normally done when building a ML model is to save the model locally as a binary file. This is done with the `joblib` library. the notebook which implements this step is called `Step_1_Build k-NN model applied to MNIST.ipynb`.
  
  - **Step #2** See my [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Docker) on how to Dockerise your ML. The file is called `Dockerfile`.
  
  - **Step #3** Let’s initialise a S3 bucket with the code below. The bucket contains some data will be feeding the ML model with to make some inferences. To do so, we will be interacting with AWS using the AWS Python SDK boto3. This package contains all the dependencies we require to integrate Python projects with AWS. This step is implemented in the notebookd called `Step_2_Deploying k-NN model on AWS.ipynb`.

  - **Step #4** We now have to write a function to upload to the S3 bucket the file object for inference. The bucket variable defines the destination S3 bucket and the key variable will define the file path in the bucket. The bucket and key variables will form part of the data payload in the POST HTTP request to our lambda function. This step is implemented in the notebookd called `Step_2_Deploying k-NN model on AWS.ipynb`.

  - **Step #5** We can check if the objects have been uploaded with the helper function which lists all objects in the bucket. This step is implemented in the notebookd called `Step_2_Deploying k-NN model on AWS.ipynb`.

  - **Step #6** Deploying and Testing AWS Lambda Functions with SAM. AWS SAM is an open source framework used to build serverless applications. It streamlines the build and deploy a serverless architecture by unifying all the tools all within a YAML configuration file. There is another packaged called [serverless](https://www.serverless.com/) which works with AWS, Azure and Google. Amazon provides an [official guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html) on how to configure a AWS SAM yaml file. Here is what goes into `template_no_auth.yaml`. As the name suggests it does not include resources that performs server side authentication of API requests. Therefore, deployment of our lambda function at its current state will allow anyone with the URL to make a request to your function. There are 6 important points store in the `.yaml` file.
    - [AWSTemplateFormatVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-formats.html) where you specified the latest template available.
    - [Transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html) which identifies an AWS CloudFormation template file as an AWS SAM template file and is a requirement for SAM template files.
    - [Globals](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy-globals.html) variables to be used by specific resources can be defined here. Function timeout and the memory size is set to 50 and 5000 MB respectively. When the specified timeout is reached, the function will stop execution.
    - [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) sets the default staging value to dev. You can define parameter values which can be referenced in the yaml file.
    - [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html) is used to declare the specific AWS resources we require for our application: API gateway and lambda function.
    - In the outputs section we declared a set of outputs to return after deploying the application with SAM. In this case the output returns the URL of the API endpoint to invoke the lambda function.

  - **Step #7** The `lambda_predict.py` in `tutorial_1_files/app` implements 4 steps:
    - Load the model
    - Download the test_features data set referenced by the bucket and key variable
    - Perform a prediction on the downloaded data set
    - Return JSON object of the predictions as a numpy array
  
  - **Step #8** The Dockerfile located at `tutorial_1_files/Dockerfile` details the instructions required to containerised our lambda function as a docker image. I will be using Python 3.9 and installing the python dependencies using poetry. Key thing to note, the entry point for the docker image is set to the lamba_handler function which is declared in the lambda_predict.py file. This entry point defines the function to be executed during an event trigger, an event such as a HTTP POST request. Any code outside of the lambda_handler function that is within the same script will be executed when the container image is initialised. 

  - **Step #9** AWS SAM provide functionality to build and locally test applications before deployment. This will allow you to see the output on a browser on a URL like this `http://127.0.0.1:3000/predict`.

  - **Step #10** Deploying on AWS Lambda. As easy as it was to deploy locally, SAM will also handle all the heavy lifting to deploy on AWS Lambda.

## References
- [Serverless Deployment of Machine Learning Models on AWS Lambda](https://towardsdatascience.com/serverless-deployment-of-machine-learning-models-on-aws-lambda-5bd1ca9b5c42)
