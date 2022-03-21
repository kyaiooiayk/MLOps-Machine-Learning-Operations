# AWS Lambda

## What is a serverless lambda?
AWS Lambda is the only Amazon compute option that remains free after one year. It’s also arguably the best option for a service that will scale smoothly to handle thousands, millions, or billions of requests. Choosing Lambda from the beginning sets your application up for success in the future. Pay attention that this is AWS services in the free tier come with a limit, usually enforced each month. Some of these seem impossibly large like AWS Lambda’s grant of one million function calls. A million can come pretty soon if you’re not careful, so make sure you actually monitor this.

Lambda is a serverless compute service that lets your code without provisioning or managing servers. “Serverless” doesn’t mean there is no server, it just means that you don’t care about the underlying infrastructure for your code and you only pay for what you use. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic. This is how AWS Lambda works:

  - You upload your code to Lambda.
  - You set your code to trigger from an event source, such as AWS services, mobile applications, or HTTP endpoints.
  - Lambda runs your code only when triggered. The trigger part is key to understand how they work.
  - You pay only for the compute time that you use. In the previous example of resizing images, you would pay only for the compute time that you use when uploading new images. Uploading the images triggers Lambda to run code for the image resizing function.

**In conclusion**, since developers do not need to manage infrastructure, serverless implementation of code has the benefit of increasing productivity as developers can spend more time writing code. 

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

## References
- [Is the AWS Free Tier really free?](https://www.lastweekinaws.com/blog/is-the-aws-free-tier-really-free/)
- [Serverless Deployment of Machine Learning Models on AWS Lambda](https://towardsdatascience.com/serverless-deployment-of-machine-learning-models-on-aws-lambda-5bd1ca9b5c42)
