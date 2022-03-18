# AWS Amazon Web Server

## Other Concepts
- **What is a client-server model?** In computing, a client can be a web browser or desktop application that a person interacts with to make requests to computer servers. A server can be services such as Amazon Elastic Compute Cloud (Amazon EC2), a type of virtual server.
- **What is cloud computing?** Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing.
- **Elasticity** With cloud computing, you don’t have to over-provision resources up front to handle peak levels of business activity in the future. Instead, you provision the amount of resources that you actually need. You can scale these resources up or down to instantly grow and shrink capacity as your business needs change.
- **Types of cloud computing**: There are 3 types of them: Infrastructure or Platform or Software as a Service. Alternatively: Iaas, PaaS and SaaS. These are arranged from more to less flexibility.
- **Multitenancy**: the idea of sharing underlying hardware between virtual machines.

## Quick references
- **Elastic Inference** allows you to attach low-cost GPU-powered acceleration to Amazon EC2 and Sagemaker instances or Amazon ECS tasks, to reduce the cost of running deep learning inference by up to 75%. Amazon Elastic Inference supports TensorFlow, Apache MXNet, PyTorch and ONNX models.
- **S3 bucket** stand for Simple Storage Service (S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics
- **SageMaker** is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly. It provides the tools to build, train and deploy machine learning (ML) models for predictive analytics applications. The platform automates the tedious work of building a production-ready artificial intelligence (AI) pipeline. *Why would you use it?* AWS SageMaker provides more elegant ways to train, test and deploy models with tools like Inference pipelines, Batch transform, multi model endpoints, A/B testing with production variants, Hyper-parameter tuning, Auto scaling etc.

- **EC2 (Amazon's Elastic Compute Cloud) instance** is a virtual server for running applications on the Amazon Web Services (AWS) infrastructure. It provides secure, resizable compute capacity in the cloud. 

- **Amazon EC2 Auto Scaling** enables you to automatically add or remove Amazon EC2 instances in response to changing application demand. By automatically scaling your instances in and out as needed, you are able to maintain a greater sense of application availability. Two approaches are available: 
  - Dynamic scaling responds to changing demand. 
  - Predictive scaling automatically schedules instances based on predicted demand.

- **Amazon EC2 instance types**: 
  - General purpose instances: balances compute, memory, and networking resources
  - Compute optimized instances: compute-intensive tasks. Offers high-performance processors
  - Memory optimized instances: memory-intensive task. Ideal for high-performance databases.
  - Accelerated computing instances: GPUs? 
  - Storage optimized instances: suitable for data warehousing applications

- **Elastic Load Balancing** Elastic Load Balancing is the AWS service that automatically distributes incoming application traffic across multiple resources, such as Amazon EC2 instances. This means that as you add or remove Amazon EC2 instances in response to the amount of incoming traffic, these requests route to the load balancer first. Then, the requests spread across multiple resources that will handle them. Although Elastic Load Balancing and Amazon EC2 Auto Scaling are separate services, they work together to help ensure that applications running in Amazon EC2 can provide high performance and availability. 

- **Amazon EC2 pricing**
  - On-Demand
  - Amazon EC2 Savings Plans
  - Reserved Instances
  - Spot Instances: ideal for workloads that can withstand interruptions. Compute costs by up to 90% over On-Demand costs.  AWS can reclaim the resorces anytime with a 2 minutes warning.
  - Dedicated Hosts: resources is not shared with anyone else.
 
- **Lambda** is a serverless compute service that lets your code without provisioning or managing servers. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic.
- **API Gateway** is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the “front door” for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications.
- **Boto3** is the name of the Python SDK(Software Development Kit) for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts. The same is true with APIs and SDKs. By definition, an SDK is a kit that includes instructions that allow developers to create systems and develop applications. APIs, on the other hand, are purpose-built for an express use — to allow communication between applications.
- **Amazon SageMaker Python SDK** SageMaker Python SDK provides several high-level abstractions for working with Amazon SageMaker.
- **API vs. SDK** An API is simply an interface that allows software to interact with other software. If an API is a set of building blocks that allow for the creation of something, an SDK is a full-fledged workshop, facilitating creation far outside the scopes of what an API would allow. By definition, an SDK is a kit that includes instructions that allow developers to create systems and develop applications. APIs, on the other hand, are purpose-built for an express use — to allow communication between applications.

## 4 ways to train and deploy ML models in SageMaker
  - Training and deploying inside SageMaker , both using SageMaker’s own built-in algorithm containers (pls note these are AWS managed containers).
  - Training our model locally/outside SageMaker and then use SageMaker’s built-in algorithm container to just deploy the locally trained model (Bring Your Own Model type ).
  - Use SageMaker’s (AWS managed) built-in algorithms containers, but customize the training as per needs with our own scripts ( Bring Your Own Model type).
  - Train our model in whatever method / or our own algorithms as we want locally in our container (built and managed by us ) and then bring that container to SageMaker and deploy it for usage (BYOC: Bring Your Own Container).

## Resources
- [Build, train, and deploy a machine learning model with Amazon SageMaker](https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/)
- [Free Machine Learning Services on AWS](https://aws.amazon.com/free/machine-learning/?trk=a422f088-0a19-452b-80fd-deab1be2be30&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Machine%20Learning|Solution|GB|EN|Text&s_kwcid=AL!4422!3!474715178818!p!!g!!%2Bamazon%20%2Bweb%20%2Bservices%20%2Bmachine%20%2Blearning&ef_id=CjwKCAiAprGRBhBgEiwANJEY7BPfUexY9PSb8WzXUXRu25P9guBimJefMIOSkehzdo5wVx09Zm41DxoCZwMQAvD_BwE:G:s&s_kwcid=AL!4422!3!474715178818!p!!g!!%2Bamazon%20%2Bweb%20%2Bservices%20%2Bmachine%20%2Blearning)
- [5 Different Ways to Deploy your Machine Learning Model with AWS](https://towardsdatascience.com/5-different-ways-to-deploy-your-machine-learning-model-with-aws-bd676ab5f8d4)
- [Deploy A Locally Trained ML Model In Cloud Using AWS SageMaker](https://medium.com/geekculture/84af8989d065)
- [Python, Boto3, and AWS S3: Demystified](https://realpython.com/python-boto3-aws-s3/)
- [SageMaker Example Notebooks](https://github.com/aws/amazon-sagemaker-examples)
- [16 videos on Amazon SageMaker Technical Deep Dive Series](https://www.youtube.com/playlist?list=PLhr1KZpdzukcOr_6j_zmSrvYnLUtgqsZz)
- [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
