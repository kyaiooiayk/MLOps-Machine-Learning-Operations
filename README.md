# MLOps (Machine Learning Operations)
How to create, deploy and manage your ML projects. This [Ref](https://neptune.ai/blog/ml-experiment-tracking) offers a nice visualisation of what MLOps encompasses.

![image](https://user-images.githubusercontent.com/89139139/148684996-107b35e5-7136-4842-a132-119db6ee48ce.png)


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
- Edge computing referres to computation done on edge devices, meaning consumer devices.

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
- Version control system (VCS) also known as revision control or source control, records and manages changes to files and folders.
- It is important to make the distinction between the following 3 concepts:
   - **Continuous Integration (CI)**: The code is built and tested on a regular basis, i.e. daily, several times per day, or – even better – with every commit.
   - **Continuous Delivery (CD)**: This is the next step, and its goal is to always have code available that can be released at any point. CD uses some automation (building and testing) but requires human intervention in the end when it comes to releasing to a productive environment.
   - **Continuous Deployment (CD)**: All code changes are automatically built, tested, and released. It's similar to continuous delivery but also brings the new version to the production environment without human intervention.
   - All three methods rely on a version control system – there is no way around it.

- GIT stands for Global Information Tracker
 - The most significant difference between the GitHub and Git Lab is that while GitHub is a collaboration platform that helps review and manage codes remotely, GitLab is majorly focused on DevOps and CI/CD.
 - GitHub is more popular amongst the developers as it holds millions of repositories, but recently GitLab has been gaining popularity, as the company continues to add new features to make it more competitive and user-friendly

## Links to useful resources
- [A Full End-to-End Deployment of a Machine Learning Algorithm into a Live Production Environment](https://www.kdnuggets.com/2021/12/deployment-machine-learning-algorithm-live-production-environment.html)
- [Guide to evaluating MLOps platforms *by thoughtworks*](https://www.thoughtworks.com/content/dam/thoughtworks/documents/whitepaper/tw_whitepaper_guide_to_evaluating_mlops_platforms_2021.pdf)
- [2022 | MLOps Is a Mess But That's to be Expected](https://www.mihaileric.com/posts/mlops-is-a-mess/)
- [VCS](https://deploybot.com/blog/version-control-systems-and-continuous-deployment-tools-a-perfect-fit)
