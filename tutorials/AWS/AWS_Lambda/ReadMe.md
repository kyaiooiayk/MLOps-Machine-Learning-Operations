# AWS Lambda
***

## What is a serverless lambda?
- AWS Lambda is the only Amazon compute option that remains free after one year. It’s also arguably the best option for a service that will scale smoothly to handle thousands, millions, or billions of requests. Choosing Lambda from the beginning sets your application up for success in the future. Pay attention that this is AWS services in the free tier come with a limit, usually enforced each month. Some of these seem impossibly large like AWS Lambda’s grant of one million function calls. A million can come pretty soon if you’re not careful, so make sure you actually monitor this.
- Lambda is a serverless compute service that lets your code without provisioning or managing servers. “Serverless” doesn’t mean there is no server, it just means that you don’t care about the underlying infrastructure for your code and you only pay for what you use. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic. This is how AWS Lambda works:
  - You upload your code to Lambda.
  - You set your code to trigger from an event source, such as AWS services, mobile applications, or HTTP endpoints.
  - Lambda runs your code only when triggered. The trigger part is key to understand how they work.
  - You pay only for the compute time that you use. In the previous example of resizing images, you would pay only for the compute time that you use when uploading new images. Uploading the images triggers Lambda to run code for the image resizing function.

**In conclusion**, since developers do not need to manage infrastructure, serverless implementation of code has the benefit of increasing productivity as developers can spend more time writing code. 
***

## Common use cases
- **Serverless back end**: Using a combination of API Gateway and AWS Lambda, you can build a complete, highly scalable RESTful API to support an external application.
- **Triggers**: You can use AWS Lambda to run code in response to changes in Amazon S3 buckets and Amazon DynamoDB tables. The code could perform a variety of tasks such as enforcing data integrity checks, firing emails, writing to queues, and interacting with other AWS services such as Amazon Machine Learning and AWS Rekognition, to name a few.
- **Maintenance**: You can use AWS Lambda to run code in response to scheduled events. Such code could perform essential maintenance and cleanup of content in databases.
- **Streams**: You can configure AWS Lambda code to run in response to new data arriving on Kinesis streams. Amazon Kinesis streams allow you to build applications that process streaming data from several sources such as social media streams, financial transactions, and IOT hardware.
***

## Cold start
- It is important to understand the concept of cold start and how this impacts latency performance while deploying on a serverless lambda.
- The first two steps of setting up the environment and the code are frequently referred to as a “cold start”. You are not charged for the time it takes for Lambda to prepare the function but it does add latency to the overall invocation duration.
- After the execution completes, the execution environment is frozen. To improve resource management and performance, the Lambda service retains the execution environment for a non-deterministic period of time. During this time, if another request arrives for the same function, the service may reuse the environment. This second request typically finishes more quickly, since the execution environment already exists and it’s not necessary to download the code and run the initialization code. This is called a “warm start”.
![image](https://user-images.githubusercontent.com/89139139/159456806-794382c7-4801-4121-bb7c-6df25976fe22.png)
***

## Lambda application vs. function
- A **lambda function** is a piece of code (managed by AWS) that is executed whenever it is triggered by an event from an event source. To create an AWS Lambda function, you first create a deployment package that contains the code you want to execute along with any dependencies. 
- A **lambda application** is a cloud application that includes one ore more Lambda functions, as well as potentially other types of services.
***

## Programming paradigm
- Every Lambda function has 5 common structures: handlers, events, context, logging, and exceptions.
- The **handler** is the entry point in your Lambda function. It is a method that AWS Lambda calls to start execution of your function. The handler method can subsequently invoke other methods in the code that make up the Lambda function. A handler can return a value or if the lambda function was invoked synchronously, the caller will receive the return value serialized as a JSON object.
```
# General structure
def lambda_handler(event, context): 
  return a_value

# Example of returning a jason file
def lambda_handler(event, context):  
  return {
  'balance': '1250' ,
  'name': 'Mr. John Woods' }
```
- The **event** is the first parameter of the handler method. Events are generated by event sources. An event source is an AWS service or custom application that publishes an event.  This is a [complete list](http://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html) of AWS services that can act as event sources. It is a standard JSON dictionary with the following general syntax:
```
{
"key3": "value3", 
"key2": "value2", 
"key1": "value1"
}
```
- **Context** is the second parameter of a handler method and you can obtain from the context object:
  - The number of seconds remaining before Lambda terminates the function.
  - The CloudWatch log group stream associated with the function.
  - The AWS request ID that was returned to the client when the function was invoked. This ID can be used for follow-up inquiries with AWS support.
  - The name of the mobile app, and the device invoking the function, if the function is invoked using the AWS Mobile SDK.
- **Logging** Any logging statements in your Lambda function are written out to CloudWatch logs. 
```
print()
logging.Logger.info()
logging.Logger.error()
```
- **Exceptions** Your function can create an exception to notify AWS Lambda that an error had occurred while executing the function code.
```
def lambda_handler(event, context):
  raise AnException('Something went wrong!')
```
***

## What are the disadvantages?
- Response latency: Since the code is not running readily and will only run once it is called, there will be latency till the code is up and running (loading a model in case of ML).
- Not useful for long running processes: Serverless providers charge for the amount of time code is running, it may cost more to run an application with long-running processes in a serverless infrastructure compared to a traditional one.
- Difficult to debug: Debugging is difficult since the developer cannot have the access(ssh) to the machine where the code is running.
***

## References
- [Is the AWS Free Tier really free?](https://www.lastweekinaws.com/blog/is-the-aws-free-tier-really-free/)
- [Serverless Deployment of Machine Learning Models on AWS Lambda](https://towardsdatascience.com/serverless-deployment-of-machine-learning-models-on-aws-lambda-5bd1ca9b5c42)
- [Cold start and lambda](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)
- [Serverless NLP Inference via HTTP API on AWS](https://towardsdatascience.com/serverless-nlp-inference-via-http-api-on-aws-e27ea41d122b)
- [Serverless NLP Inference on Amazon SageMaker with Transformer Models from Hugging Face](https://towardsdatascience.com/serverless-nlp-inference-on-amazon-sagemaker-with-transformer-models-from-hugging-face-4843609a7451)
- [MLOps Basics [Week 8]: Serverless Deployment - AWS Lambda](https://www.ravirajag.dev/blog/mlops-serverless)
***
