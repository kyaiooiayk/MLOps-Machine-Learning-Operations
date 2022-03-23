# AWS SageMaker

## Introduction
- It is a fully managed web service that provides the ability to explore data, engineer features, and train machine learning models on AWS cloud infrastructure using Python code.
- It provides implementations of a number of cloud-optimized versions of machine learning algorithms such as XGBoost, factorization machines, and PCA.
- It provides the ability to create your own algorithms based on popular frameworks such as Scikit-learn, Google TensorFlow, and Apache MXNet.
- It provides a convenient high-level, object-oriented interface for Python developers.
- A SageMaker notebook instances are EC2 instances in your account that come preconfigured with a Jupyter Notebook server, and a number of common Python libraries.
- Training jobs create dedicated compute instances in the AWS cloud that contain model- building code, load your training data from Amazon S3, execute the model-building code on your training data, and save the trained model to Amazon S3.
- When the training job is complete, the compute instances that were provisioned to support the training process will automatically be terminated.
- Deploying a model into production involves creating one or more compute instances, deploying your model onto these instances, and providing an API that can be used to make predictions using the deployed model.
- Prediction instances are not automatically terminated.
- An endpoint configuration ties together information on the location of a trained machine
learning model, type of compute instances, and an auto-scaling policy.
- A prediction endpoint is an HTTPS REST API endpoint that can be used to get single predictions from a deployed model. The HTTP endpoint is secured using AWS Signature V4 authentication.
- If you need to make predictions on an entire dataset, you can create use Amazon SageMaker Batch Transform to create a batch prediction job from a trained model

## 4 ways to train and deploy ML models in SageMaker
  - Training and deploying inside SageMaker , both using SageMaker’s own built-in algorithm containers (pls note these are AWS managed containers).
  - Training our model locally/outside SageMaker and then use SageMaker’s built-in algorithm container to just deploy the locally trained model (Bring Your Own Model type ).
  - Use SageMaker’s (AWS managed) built-in algorithms containers, but customize the training as per needs with our own scripts ( Bring Your Own Model type).
  - Train our model in whatever method and then bring your container to SageMaker and deploy it for usage (BYOC: Bring Your Own Container).

## References
- [GitHub repository for notebooks](https://github.com/asmtechnology/awsmlbook-chapter16)
- Mishra, Abhishek. Machine Learning in the AWS Cloud: Add Intelligence to Applications with Amazon SageMaker and Amazon Rekognition. John Wiley & Sons, 2019.
