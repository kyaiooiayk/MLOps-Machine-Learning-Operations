# MLOps (Machine Learning Operations)
How to create, deploy and manage your ML projects. But what do we mean when we talk about model deployment? Training a ML model using a method of your choice. Writing a service using FastAPI for exposing the model through a service endpoint. Packaging the service into a Docker container. Deploying the Docker container to (AWS) Kubernetes Cluster to scale up the service.

![image](https://user-images.githubusercontent.com/89139139/148684996-107b35e5-7136-4842-a132-119db6ee48ce.png)
***

### Data Engineering
- Apache Nifi
- Spark
- Argo workflow
- Azue databricks
- Hadoop 
- Apache Spark
***

### Pipelines
- [[Apache Airflow](https://airflow.apache.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Airflow)]
- **Kubeflow Pipelines** is an orchestration subsystem built on Kubernetes.
- [MLeap](https://github.com/combust/mleap) It allows data scientists and engineers to deploy machine learning pipelines from Spark and Scikit-learn to a portable format and execution engine. MLeap is a common serialization format and execution engine for machine learning pipelines. 
***

### Model serialisation
- [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Model_Serialiation)
***
### Model lifecycle
- MLFlow
- Kubeflow
- Tensorflow Serving
- AWS SageMaker
- GCP (Google Cloud Platform)
***
### Dashboard
- Bokeh
- Plotly
***
## Deployment options
You essentially have two options:
 - If our application requires **low latency**, then we should deploy the model as a real- time API to provide super-fast predictions on single prediction requests over HTTPS, for example. We can deploy, scale, and compare our model prediction servers with SageMaker Endpoints using the REST API protocol with HTTPS and JSON.
 - For **less-latency-sensitive** applications that require high throughput, we should deploy our model as a batch job to perform batch predictions on large amounts of data in S3, for example. We will use SageMaker Batch Transform to perform the batch predic‐ tions along with a data store like Amazon RDS or DynamoDB to productionize the predictions,
***
### DevOps
- [ Git | [Notes](https://github.com/kyaiooiayk/Git-Cheatsheet)]
- [[Jenkins](https://www.jenkins.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Jenkins)]
- Maven : it is used to create deployment package.
- [[Docker](https://www.docker.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Docker)]
- [Kubernets | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Kubernetes)]
***
### Application Framework/Model Deployment
- Django
- [[Flask](https://flask.palletsprojects.com/en/2.1.x/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Flask)]
- [[Node.js]() | [Notes]()]
- [[Express.js]() | [Notes]()]
- [ [React](https://reactjs.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/React)]
- Nginx
- Redis
- [[FastAPI](https://fastapi.tiangolo.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/FastAPI)]
- [Heroku | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Heroku/Quora_insincere_questions_classification)]
- [Streamlit | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Streamlit)]
***
### Cloud computing
Cloud computing is a name which refers to cluster machines on the cloud. AWS, seems to be the most popular. Maybe if one has to choose one while trying to learn something about it, one would look  at the one allowing more free computing hrs.
- [[AWS (Amazon Web Services)](https://aws.amazon.com/?nc2=h_lg) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS)]
- Microsoft Azure
- GCP (Google Cloud Platform)
***
### Edge computing
- Edge computing referes to computation done on edge devices, meaning consumer devices. Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data.
***
### Relational Database
RDB (relational database) is a database that stores data into tables with rows and columns.
***
### Relational database at scale
How to turn SQL-like into a map-reduce job that can run on a distributed file system. This is essentiallu what we mean by relational database at scale.
- [Hive | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Hive.md)] (twice as popular as Pig and developed by Facebook). Hive provides SQL type querying language for the ETL purpose on top of Hadoop file system. 
- Pig (less popular than Hive)
***

### Data warehouse tools
A **data warehouse*** stores data in files or folders in a hierarchical manner whereas a **data lake** uses a flat architecture. Every bit of data in the lake has a unique ID and is tagged with sets of extended metadata tags. When you need information, the data lake can be queried for relevant data, and that smaller set of data can be accessed to get the data you need. The ability to append your own metadata enables you to make it very easy to search your data.
- MongoDB
- CosmosDB
- Looker
- Stitch
- DBT
- Snowflake
- Amazon redshift
- Azure synapse
- Google big query
***
###  Management 
It is an unified analytics platform.
- Databricks 
- AWS google
- MS has its own alternative
***
### Streaming
- Apache Kafka
- Apache Spark
- Google Dataflow
***
## APIs & Microservices
- **APIs vs Microservices: How They Work Together?** Microservices function as the “building‐blocks” of the application by performing various services, while “RESTful APIs” function as the “glue” that integrates the microservices into an application.
- **Why were microservices created?** Suppose that you have an application with tightly coupled components comprising of databases, servers, the user interface, business logic, and so on. This type of architecture can be considered a monolithic application, but if a single component fails, other components fail, and possibly the entire application fails. In a microservices approach, application components are loosely coupled, thus if a single component fails, the other components continue to work. 
- **HTTP vs. REST APIs** APIs can be categorised into various types based on application designs and other constraints, such as Web API, HTTP API, REST API, and many more.
  - REST API is a Software Architectural Style that is used to guide the creation and design of the architecture of the World Wide Web. In other words, REST APIs establish a set of guidelines for how a distributed system’s architecture should function. REST APIs add no new capability to HTTP APIs. REST APIs are ideal for creating scalable general-purpose applications. 
  - On the other hand, HTTP API is an application that communicates between two systems using the Hypertext Transfer Protocol. HTTP APIs make endpoints available as API gateways, allowing HTTP queries to connect to a server. The majority of HTTP APIs are on the verge of becoming completely RESTful.
***
- **When an API can be called REST API?** The requirements are:
   - Client-Server: A server oversees the application’s data and state in REST applications. The server connects with a client, which is responsible for handling user interactions. The two components are separated by a clear separation of responsibilities. As a result, you’ll be able to update and upgrade them in separate tracks.
   - Stateless: Client state is not maintained by servers; instead, clients handle their own application state. All of the information needed to process the client’s requests are contained in the requests to the server.
   - Cacheable: Servers must indicate whether or not their responses are cacheable. To boost performance, systems and clients might cache replies when it is convenient. They also get rid of non-cacheable data, so no client has to deal with stale data.
   - Uniform Interface: REST’s most well-known characteristics are that the emphasis on a uniform interface between components is the primary aspect that distinguishes the REST architectural style from other network-based approaches. Data is provided as resources through REST services, which have a consistent namespace.
   - Layered System: The system’s components can’t look beyond their own layer. This limited scope makes it simple to add load-balancers and proxies to increase authentication security and performance
***
## Version control system (VCS)
- Version control system (VCS) also known as revision control or source control, records and manages changes to files and folders. [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/VCS.md)
- [[Hydra](https://hydra.cc/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/Hydra)]
- [[DVC](https://dvc.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/DVC)]
***
## References
- [A Full End-to-End Deployment of a Machine Learning Algorithm into a Live Production Environment](https://www.kdnuggets.com/2021/12/deployment-machine-learning-algorithm-live-production-environment.html)
- [Guide to evaluating MLOps platforms *by thoughtworks*](https://www.thoughtworks.com/content/dam/thoughtworks/documents/whitepaper/tw_whitepaper_guide_to_evaluating_mlops_platforms_2021.pdf)
- [MLOps Is a Mess But That's to be Expected](https://www.mihaileric.com/posts/mlops-is-a-mess/)
- [VCS](https://deploybot.com/blog/version-control-systems-and-continuous-deployment-tools-a-perfect-fit)
- [ML Experiment Tracking: What It Is, Why It Matters, and How to Implement It](https://neptune.ai/blog/ml-experiment-tracking)
- [HTTP vs. REST APIs](https://hevodata.com/learn/http-api-vs-rest-api/)
- [Awesome production machine learning](https://github.com/EthicalML/awesome-production-machine-learning#model-and-data-versioning)
- [MLOps Is a Mess But That’s to be Expected](https://www.kdnuggets.com/2022/03/mlops-mess-expected.html)
- [MLOps Principles](https://ml-ops.org/content/mlops-principles)
