# MLOps (Machine Learning Operations)
How to create, deploy and manage your ML projects. This [Ref](https://neptune.ai/blog/ml-experiment-tracking) offers a nice visualisation of what MLOps encompasses.

![image](https://user-images.githubusercontent.com/89139139/148684996-107b35e5-7136-4842-a132-119db6ee48ce.png)

- **Model deployment** Training a machine learning model using a method of your choice [XGBoost, LightGBM.] Writing a service using FastAPI for exposing the model through a service endpoint. Packaging the service into a Docker container. Deploying the Docker container to (AWS) Kubernetes Cluster to scale up the service.

### Data Engineering
- Apache Nifi
- Apache Airflow
- Spark
- DVC
- Argo workflow
- Azue databricks
- Hadoop 
- Apache Spark

### Model serialisation
- [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Model_Serialiation)

### Model lifecycle
- MLFlow
- Kubeflow
- Tensorflow Serving
- AWS SageMaker
- GCP (Google Cloud Platform)

### DevOps
- Git
- [Jenkins](https://www.jenkins.io/): Jenkins is an open source continuous integration/continuous delivery and deployment (CI/CD) automation software DevOps tool written in the Java programming language. It is used to implement CI/CD workflows, called pipelines.
- [Docker | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Docker)]
- [Kubernets | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Kubernetes)]

### Application Framework/Model Deployment
- Django
- [Flask | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Flask)]
- Nodejs
- Expressjs
- React
- Nginx
- Redis
- [Heroku | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Heroku/Quora_insincere_questions_classification)]
- [Streamlit | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Streamlit)]

### Cloud computing
Cloud computing is a name which refers to cluster machines on the cloud. AWS, seems to be the most popular. Maybe if one has to choose, one would look  at the one allowing more free computing hrs.
- [AWS (Amazon Web Server)| [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS)]
- Microsoft Azure
- GCP (Google Cloud Platform)

### Edge computing
- Edge computing referes to computation done on edge devices, meaning consumer devices. Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data.

### Relational Database
RDB (relational database) is a database that stores data into tables with rows and columns.

### Relational database at scale
How to turn SQL-like into a map-reduce job that can run on a distributed file system. This is essentiallu what we mean by relational database at scale.
- [Hive | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Hive.md)] (twice as popular as Pig and developed by Facebook). Hive provides SQL type querying language for the ETL purpose on top of Hadoop file system. 
- Pig (less popular than Hive)

### Non relational database
 - MongoDB
 - CosmosDB

### Data warehouse tools
- Looker
- Stitch
- DBT
- Snowflake
- Amazon redshift
- Azure synapse
- Google big query

###  Management 
It is an unified analytics platform.
- Databricks 
- AWS google
- MS has its own alternative

### Streaming
- Apache Kafka
- Apache Spark
- Google Dataflow

## APIs & Microservices
- **APIs vs Microservices: How They Work Together?** Microservices function as the “building‐blocks” of the application by performing various services, while “RESTful APIs” function as the “glue” that integrates the microservices into an application.

## Version control system (VCS)
- Version control system (VCS) also known as revision control or source control, records and manages changes to files and folders. [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/VCS.md)


## Links to useful resources
- [A Full End-to-End Deployment of a Machine Learning Algorithm into a Live Production Environment](https://www.kdnuggets.com/2021/12/deployment-machine-learning-algorithm-live-production-environment.html)
- [Guide to evaluating MLOps platforms *by thoughtworks*](https://www.thoughtworks.com/content/dam/thoughtworks/documents/whitepaper/tw_whitepaper_guide_to_evaluating_mlops_platforms_2021.pdf)
- [2022 | MLOps Is a Mess But That's to be Expected](https://www.mihaileric.com/posts/mlops-is-a-mess/)
- [VCS](https://deploybot.com/blog/version-control-systems-and-continuous-deployment-tools-a-perfect-fit)
