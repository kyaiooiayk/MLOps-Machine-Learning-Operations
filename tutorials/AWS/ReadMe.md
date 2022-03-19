# AWS Amazon Web Server

## Other Concepts
- **What is a client-server model?** In computing, a client can be a web browser or desktop application that a person interacts with to make requests to computer servers. A server can be services such as Amazon Elastic Compute Cloud (Amazon EC2), a type of virtual server.

- **What is cloud computing?** Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing.

- **Elasticity** With cloud computing, you don’t have to over-provision resources up front to handle peak levels of business activity in the future. Instead, you provision the amount of resources that you actually need. You can scale these resources up or down to instantly grow and shrink capacity as your business needs change.

- **Types of cloud computing**: There are 3 types of them: Infrastructure or Platform or Software as a Service. Alternatively: Iaas, PaaS and SaaS. These are arranged from more to less flexibility.

- **Multitenancy**: the idea of sharing underlying hardware between virtual machines.

- **Serverless** means that your code runs on servers, but you do not need to provision or manage these servers. With serverless computing, you can focus more on innovating new products and features instead of maintaining servers. The opposite of this way of working is the EC2 (i.e. virtual server) instance that lets you run virtual servers in the cloud. If you have applications that you want to run in Amazon EC2, you must do the following:
  - Provision instances (virtual servers).
  - Upload your code.
  - Continue to manage the instances while your application is running.

- **Shared responsibility model** is the idea that both customer and AWS is responsible for keeping resources secure. AWS is responsible for some parts of your environment and you (the customer) are responsible for other parts. The shared responsibility model divides into customer responsibilities (commonly referred to as “security in the cloud”) and AWS responsibilities (commonly referred to as “security of the cloud”).

- **Caching** is applied to improve application performance. The cache is a piece of memory that has much faster read/write time (around an order of magnitude faster).


## Quick references
- **Elastic Inference** allows you to attach low-cost GPU-powered acceleration to Amazon EC2 and Sagemaker instances or Amazon ECS tasks, to reduce the cost of running deep learning inference by up to 75%. Amazon Elastic Inference supports TensorFlow, Apache MXNet, PyTorch and ONNX models.

- **S3 bucket** stand for Simple Storage Service (S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. There are 6 types:
  - S3 Standard
  - S3 Standard-Infrequent Access (S3 Standard-IA)
  - S3 One Zone-Infrequent Access (S3 One Zone-IA)
  - S3 Intelligent-Tiering
  - S3 Glacier
  - S3 Glacier Deep Archive 

- **SageMaker** is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly. It provides the tools to build, train and deploy machine learning (ML) models for predictive analytics applications. The platform automates the tedious work of building a production-ready artificial intelligence (AI) pipeline. *Why would you use it?* AWS SageMaker provides more elegant ways to train, test and deploy models with tools like Inference pipelines, Batch transform, multi model endpoints, A/B testing with production variants, Hyper-parameter tuning, Auto scaling etc.

- **EC2 (Amazon's Elastic Compute Cloud) instance** is a virtual server for running applications on the Amazon Web Services (AWS) infrastructure. It provides secure, resizable compute capacity in the cloud. 

- **Amazon EC2 Auto Scaling** enables you to automatically add or remove Amazon EC2 instances in response to changing application demand. By automatically scaling your instances in and out as needed, you are able to maintain a greater sense of application availability. Two approaches are available: 
  - Dynamic scaling responds to changing demand. 
  - Predictive scaling automatically schedules instances based on predicted demand.

- **Amazon EC2 instance types**: 
  - General purpose instances: balances compute, memory, and networking resources
  - Compute optimized instances: compute-intensive tasks. Offers high-performance processors. Used for a batch processing workload.
  - Memory optimized instances: memory-intensive task. Ideal for high-performance databases.
  - Accelerated computing instances: GPUs? 
  - Storage optimized instances: suitable for data warehousing applications

- **Elastic Load Balancing** Elastic Load Balancing is the AWS service that automatically distributes incoming application traffic across multiple resources, such as Amazon EC2 instances. This means that as you add or remove Amazon EC2 instances in response to the amount of incoming traffic, these requests route to the load balancer first. Then, the requests spread across multiple resources that will handle them. Although Elastic Load Balancing and Amazon EC2 Auto Scaling are separate services, they work together to help ensure that applications running in Amazon EC2 can provide high performance and availability.  An example of Elastic Load Balancing Ensuring that no single Amazon EC2 instance has to carry the full workload on its own.

- **Amazon EC2 pricing**
  - On-Demand
  - Amazon EC2 Savings Plans
  - Reserved Instances
  - Spot Instances: ideal for workloads that can withstand interruptions. Compute costs by up to 90% over On-Demand costs.  AWS can reclaim the resorces anytime with a 2 minutes warning.
  - Dedicated Hosts: resources is not shared with anyone else.
 
- **Lambda** is a serverless compute service that lets your code without provisioning or managing servers. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic. This is how AWS Lambda works:
  - You upload your code to Lambda. 
  - You set your code to trigger from an event source, such as AWS services, mobile applications, or HTTP endpoints.
  -  Lambda runs your code only when triggered. The trigger part is key to understand how they work.
  - You pay only for the compute time that you use. In the previous example of resizing images, you would pay only for the compute time that you use when uploading new images. Uploading the images triggers Lambda to run code for the image resizing function.

- **API Gateway** is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the “front door” for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications.

- **Boto3** is the name of the Python SDK(Software Development Kit) for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts. The same is true with APIs and SDKs. By definition, an SDK is a kit that includes instructions that allow developers to create systems and develop applications. APIs, on the other hand, are purpose-built for an express use — to allow communication between applications.

- **Amazon SageMaker Python SDK** SageMaker Python SDK provides several high-level abstractions for working with Amazon SageMaker.- **API vs. SDK** An API is simply an interface that allows software to interact with other software. If an API is a set of building blocks that allow for the creation of something, an SDK is a full-fledged workshop, facilitating creation far outside the scopes of what an API would allow. By definition, an SDK is a kit that includes instructions that allow developers to create systems and develop applications. APIs, on the other hand, are purpose-built for an express use — to allow communication between applications.

- **Amazon Simple Notification Service (Amazon SNS) & Amazon Simple Queue Service (Amazon SQS)** Suppose that you have an application with tightly coupled components comprising of databases, servers, the user interface, business logic, and so on. This type of architecture can be considered a monolithic application, but if a single component fails, other components fail, and possibly the entire application fails. In a microservices approach, application components are loosely coupled, thus if a single component fails, the other components continue to work. Two services facilitate application integration: Amazon Simple Notification Service (Amazon SNS) and Amazon Simple Queue Service (Amazon SQS).
  - Amazon SNS is a publish/subscribe service. Using Amazon SNS topics, a publisher publishes messages to subscribers. Subscribers can be web servers, email addresses, AWS Lambda functions, or several other options.
  - Amazon SQS is a message queuing service. Using Amazon SQS, you can send, store, and receive messages between software components, without losing messages or requiring other services to be available. In Amazon SQS, an application sends messages into a queue. A user or service retrieves a message from the queue, processes it, and then deletes it from the queue.
 
- **Amazon Elastic Container Service (Amazon ECS)** is a highly scalable, high-performance container management system that enables you to run and scale containerized applications on AWS. Amazon ECS supports Docker containers.

- **Amazon Elastic Kubernetes Service (Amazon EKS)** is a fully managed service that you can use to run Kubernetes on AWS. Kubernetes is open-source software that enables you to deploy and manage containerized applications at scale.

- **AWS Fargate** AWS Fargate is a serverless compute engine for containers. It works with both Amazon ECS and Amazon EKS. When using AWS Fargate, you do not need to provision or manage servers. AWS Fargate manages your server infrastructure for you.

- **AWS Elastic Beanstalk** With AWS Elastic Beanstalk, you provide code and configuration settings, and Elastic Beanstalk deploys the resources necessary to perform the following tasks:
  - Adjust capacity
  - Load balancing
  - Automatic scaling
  - Application health monitoring

- **AWS CloudFormation** With AWS CloudFormation, you can treat your infrastructure as code. This means that you can build an environment by writing lines of code instead of using the AWS Management Console to individually provision resources.

- **Amazon CloudFront** is best described as a global content delivery service. Edge location are site that Amazon CloudFront use to cache copies of content for faster delivery to users at any location.

- **Amazon Outpost** it is used to extend AWS infrastructure and services to your on-premises data center.

- **Amazon Route 53** is a DNS web service which gives developers and businesses a reliable way to route end users to internet applications hosted in AWS. DNS can be thought as being the phone book of the internet. DNS resolution is the process of translating a domain name to an IP address. 

- **Instance store** is a store that provides temporary block-level storage for an Amazon EC2 instance. An instance store is disk storage that is physically attached to the host computer for an EC2 instance, and therefore has the same lifespan as the instance. When the instance is terminated, you lose any data in the instance store. Thus, instance stores for use cases that involve temporary data that you do not need in the long term.

- **Amazon Elastic Block Store (Amazon EBS)** is a service that provides block-level storage volumes that you can use with Amazon EC2 instances. If you stop or terminate an Amazon EC2 instance, all the data on the attached EBS volume remains available. Because EBS volumes are for data that needs to persist, it’s important to back up the data. You can take incremental backups of EBS volumes by creating Amazon EBS snapshots. It stores data in a *single* availability zone.

- **Amazon Elastic File System (Amazon EFS)** is a scalable file system used with AWS Cloud services and on-premises resources. As you add and remove files, Amazon EFS grows and shrinks automatically. It can scale on demand to petabytes without disrupting applications. It stores data in a *multiple* availability zone.

- **Amazon DynamoDB** is a key-value database service, thus NoSQL. It delivers single-digit millisecond performance at any scale. Nonrelational databases are sometimes referred to as “NoSQL databases” because they use structures other than rows and columns to organize data. One type of structural approach for nonrelational databases is key-value pairs. With key-value pairs, data is organized into items (keys), and items have attributes (values). You can think of attributes as being different features of your data. It is serveless which means you do not have to provision, patch and manage servers.

- **Amazon Redshift** is a data warehousing service that you can use for big data analytics. It offers the ability to collect data from many sources and helps you to understand relationships and trends across your data.

- **AWS Database Migration Service (AWS DMS)** enables you to migrate relational databases, nonrelational databases, and other types of data stores. With AWS DMS, you move data between a source database and a target database. The source and target databases can be of the same type or different types. During the migration, your source database remains operational, reducing downtime for any applications that rely on the database. For example, suppose that you have a MySQL database that is stored on premises in an Amazon EC2 instance or in Amazon RDS. Consider the MySQL database to be your source database. Using AWS DMS, you could migrate your data to a target database, such as an Amazon Aurora database.

- The **AWS Well-Architected Framework** helps you understand how to design and operate reliable, secure, efficient, and cost-effective systems in the AWS Cloud. It provides a way for you to consistently measure your architecture against best practices and design principles and identify areas for improvement.

## Ways to interact with AWS services
  - Via the **AWS Management Console** which is a web-based interface for accessing and managing AWS services.
  - Via the **AWS Command Line Interface (AWS CLI)** To save time when making API requests, you can use the AWS CLI. AWS CLI enables you to control multiple AWS services directly from the command line within one tool. AWS CLI is available for users on Windows, macOS, and Linux. 
  - Via **Software Development Kits (SDKs)** Another option for accessing and managing AWS services is the software development kits (SDKs). SDKs make it easier for you to use AWS services through an API designed for your programming language or platform. SDKs enable you to use AWS services with your existing applications or create entirely new applications that will run on AWS.

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
- [Find the hands-on tutorials for your AWS needs](https://aws.amazon.com/getting-started/hands-on/?awsf.getting-started-category=category%23compute&awsf.getting-started-content-type=content-type%23hands-on&getting-started-all.sort-by=item.additionalFields.sortOrder&getting-started-all.sort-order=asc&awsf.getting-started-level=*all)
