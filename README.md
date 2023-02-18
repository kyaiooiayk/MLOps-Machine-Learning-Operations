# MLOps (Machine Learning Operations)
How to create, deploy and manage your ML projects. But what do we mean when we talk about model deployment? Training a ML model using a method of your choice. Writing a service using FastAPI for exposing the model through a service endpoint. Packaging the service into a Docker container. Deploying the Docker container to (AWS) Kubernetes Cluster to scale up the service.

![image](https://user-images.githubusercontent.com/89139139/148684996-107b35e5-7136-4842-a132-119db6ee48ce.png)
***

## XaaS and the likes
**as a Service** is a licensing model which allows access to services on a subscription basis using external servers.
<details>
<summary>Expand ⬇️</summary>
<br>

- **IaaS** (Infrastructure as a Service) - base hardware and operating system. It is a method to create virtualized computing environments and rapidly scale infrastructure to meet specific organizational needs.
- **PaaS** (Platform as a Service) - infrastructure, development tools (Node.JS, Java Git)
- **SaaS** (Software as a Service) - infrastructure, operating system, and ready-to-use end-user applications. SaaS has many business applications, including file sharing, email, calendars, customer retention management, and human resources. SaaS  has at least have lower up-front costs) since users pay for SaaS as they go instead of purchasing multiple software licenses for multiple computers. Drawbacks to the adoption of SaaS center around data security, speed of delivery, and lack of control. Examples: (Amazon Web Server, Google Cloud Computing, Microsoft Azure and Oracle) are also SaaS, meaning they are much more than this.
- PaaS (platform as a Service) - 
- **IaaC** (Infrastructure as a Code) is the process of managing and provisioning computer data centers through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools. It is a tool for provisioning and managing infrastructure and configurations for those resources. Examples: [Terraform](https://www.terraform.io/) | [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) | [Ansible](https://www.ansible.com/) | [Chef](https://docs.chef.io/) | [Pulumi](https://www.pulumi.com/)
- **BPaaS** (Business Process as a Service) - SaaS + business process (Accounting, Auditing) : Examples: PayPal
- **MLaaS** (Machine Learning as a Service) - SaaS + ML specific applications. Examples: [Amazon Sagemaker](https://aws.amazon.com/sagemaker/?nc=sn&loc=0&refid=811736de-a95f-4b18-b2e9-a2bad5c010f3) | [Microsoft Azure Machine Learning Studio](https://studio.azureml.net/) | [IBM Watson Machine Learning](https://www.ibm.com/cloud/watson-studio?mhsrc=ibmsearch_a&mhq=watson%20studio)
</details>

***

## Data Engineering - Pipelines
Workflow orchestration is a set of tools for scheduling and monitoring work that you want to complete. Ex: Scheduling ML models training. The purpose of workflow orchestration is to reduce mistakes and gently fail.
<details>
<summary>Expand ⬇️</summary>
<br>

- Apache Nifi
- Argo workflow
- [Databricks](https://www.databricks.com/) develops a web-based platform for working with Spark, that provides automated cluster management and IPython-style notebooks. | [Databricks vs. Azure databricks](https://www.websitebuilderinsider.com/is-azure-databricks-same-as-databricks/)
- [Azure databricks](https://azure.microsoft.com/en-us/products/databricks/) is a fast, easy, and collaborative Apache Spark-based big data analytics service designed for data science and data engineering.
- [[Apache Airflow](https://airflow.apache.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Airflow)] Apache is a very mature and popular option initially developed to orchestrate data engineering and extract-transform-load (ETL) pipelines for analytics workloads. Airflow has expanded into the machine-learning space as a viable pipeline orchestrator. 
- [[Terraform](https://www.terraform.io/) | Notes | [Ref#1](https://www.jeremyjordan.me/terraform/) | [Ref#2](https://developer.hashicorp.com/terraform/intro)] is an infrastructure-as-code tool which provides a mechanism for declaratively defining your infrastructure via a set of configuration files. When you first started working with cloud services, you probably just created whatever resources you needed directly in the AWS/GCP/Azure console. However, as the size of your organization or the number of projects grow, this becomes difficult to manage at scale. The core Terraform workflow consists of three stages:
  - **Write**: You define resources, which may be across multiple cloud providers and services. For example, you might create a configuration to deploy an application on virtual machines in a Virtual Private Cloud (VPC) network with security groups and a load balancer.
  - **Plan**: Terraform creates an execution plan describing the infrastructure it will create, update, or destroy based on the existing infrastructure and your configuration.
  - **Apply**: On approval, Terraform performs the proposed operations in the correct order, respecting any resource dependencies. For example, if you update the properties of a VPC and change the number of virtual machines in that VPC, Terraform will recreate the VPC before scaling the virtual machines.
- [Apache Beam](https://beam.apache.org/) is an open source tool for defining and executing data-processing jobs. Apache Beam can be used to describe batch processes, streaming operations, and data pipelines. In fact, TFX relies on Apache Beam and uses it under the hood for a variety of components (e.g., TensorFlow Transform or TensorFlow Data Validation). You can run the same data pipeline on Apache Spark or Google Cloud Dataflow without a single change in the pipeline description. Also, Apache Beam was not just developed to describe batch processes but to support streaming operations seamlessly.  
- **[Kubeflow](https://www.kubeflow.org/) Pipelines** is an orchestration subsystem built on Kubernetes that includes an orchestration subsystem called Kubeflow Pipelines. 
- [[MLeap](https://github.com/combust/mleap) | Notes] It allows data scientists and engineers to deploy machine learning pipelines from Spark and Scikit-learn to a portable format and execution engine. MLeap is a common serialisation format and execution engine for machine learning pipelines. 
- [[Prefect](https://www.prefect.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Prefect)] is an open-source data flow automation platform that aims to decrease negative engineering and simplify workflow orchestration when compared to existing products like Airflow.
- Kubeflow
- [[Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/TensorFlowServing.md)]
- AWS SageMaker - Amazon SageMaker is a cloud machine-learning platform that was launched in November 2017. SageMaker enables developers to create, train, and deploy machine-learning models in the cloud. SageMaker also enables developers to deploy ML models on embedded systems and edge-devices.
- Google Vertex AI - diret competitor of AWS SageMaker
- [Tensor Flow Extended (TFX)](https://www.tensorflow.org/tfx) is an open source collection of Python libraries used within a pipeline orchestrator such as Kubeflow Pipelines, Apache Airflow, and MLflow.
- [Apache PyArrow](https://arrow.apache.org/docs/python/index.html) is a cross-language development platform for in-memory data. It specifies a standardized language-independent columnar memory format for flat and hierarchical data, organized for efficient analytic operations (store, process and move data fast) on modern hardware. It facilitates communication between many components, for example, reading a parquet file with Python (pandas) and transforming to a Spark dataframe, Falcon Data Visualization or Cassandra without worrying about conversion. It does this by takeing advantage of a columnar buffer to reduce IO and accelerate analytical processing performance. [Ref](https://towardsdatascience.com/a-gentle-introduction-to-apache-arrow-with-apache-spark-and-pandas-bb19ffe0ddae)
</details>

***

## Data validation
<details>
<summary>Expand ⬇️</summary>
<br>

- [[Pandera](https://pandera.readthedocs.io/en/stable/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Data_validation/Pandera)]
- [[Great Expectations](https://greatexpectations.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Data_validation/Great_expectations)]
</details>

***

## Experiment Tracking
Experiment tracking allows us to manage all the experiments along with their components, such as parameters, metrics, and more. It makes easier to track the evolution of your model as learn more and more about the problem.
<details>
<summary>Expand ⬇️</summary>
<br>

- [MLFlow](https://mlflow.org/) is an open source project that offers experiment tracking and multiframe‐work support including Apache Spark, but limited workflow support. If you need a lightweight, simple way to track experiments and run simple workflows, this may be a good choice.
- [Comet ML](https://www.comet.com/site/) 
- [Neptune](https://neptune.ai/)
- [Weights and Biases](https://wandb.ai/site)
- [TensorBoard](https://www.tensorflow.org/tensorboard)
</details>

***
 

## Model serialisation
<details>
<summary>Expand ⬇️</summary>
<br>

- Serialisation is the process of translating a data structure or object state into a format that can be stored or transmitted and reconstructed later. 
- Common formats: hdf5, json, pickle, joblib, dill, ONNX
- [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Model_Serialisation)
</details>

***

## Dashboard
<details>
<summary>Expand ⬇️</summary>
<br>

- Bokeh
- Plotly
</details>

***

## Deployment options
<details>
<summary>Expand ⬇️</summary>
<br>

You essentially have two options:
 - If our application requires **low latency**, then we should deploy the model as a real-time API to provide super-fast predictions on single prediction requests over HTTPS.
 - For **less-latency-sensitive** applications that require high throughput, we should deploy our model as a batch job to perform batch predictions on large amounts of data.
</details>

***

## DevOps
DevOps is a role that integrates the job scope of software developers and operations teams to automate workflows.
<details>
<summary>Expand ⬇️</summary>
<br>

- Maven : it is used to create deployment package.
- [[Docker](https://www.docker.com/) | [Notes](https://github.com/kyaiooiayk/Docker-Notes)]
- [[Kubernets](https://kubernetes.io/) | [Notes](https://github.com/kyaiooiayk/Kubernetes-Notes)]
- [Packaging | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Packaging)]
- [Apache Jmeter](https://jmeter.apache.org/)
- [ Git | [Notes](https://github.com/kyaiooiayk/Git-Cheatsheet)]
</details>

***

## CI/CD
In modern software development teams, continuous integration (CI) and continuous deployment (CD) are standard practices.  CI is about how the project should be built and tested in various runtimes, automatically and continuously. CD is needed so that every new bit of code that passes automated testing can be released into production with no extra effort. 
<details>
<summary>Expand ⬇️</summary>
<br>

- [[GitHub Actions](https://github.com/features/actions) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/GitHub_Actions.md)]
- [[Jenkins](https://www.jenkins.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Jenkins)]
- [CI/CD tools comparison](https://neptune.ai/blog/continuous-integration-continuous-deployment-tools-for-machine-learning)
</details>

***

## Application Framework/Model Deployment
<details>
<summary>Expand ⬇️</summary>
<br>

- Django
- [[Flask](https://flask.palletsprojects.com/en/2.1.x/) | [Notes](https://github.com/kyaiooiayk/Flask-Notes)]
- [[Node.js]() | Notes]
- [[Express.js]() | Notes]
- [[React](https://reactjs.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/React)]
- Redis
- [[FastAPI](https://fastapi.tiangolo.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/FastAPI)]
- [[Streamlit](https://streamlit.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Streamlit)]
- [[Electron](https://www.electronjs.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Electron.md)]
- [[Dash](https://plotly.com/building-machine-learning-web-apps-in-python/)]
- [[Gradio](https://github.com/gradio-app/gradio)]
</details>

***

## Public server deployment
<details>
<summary>Expand ⬇️</summary>
<br>

- [[Heroku](https://www.heroku.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Heroku)] - allows access directly to your GitHub account
- [[PythonAnywhere](https://www.pythonanywhere.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/pythonanywhere)] - does not allow access directly to your GitHub account
- [[Netlify](https://www.netlify.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Netlify.md)] - allows access directly to your GitHub account
</details>

***

## Cloud computing
<details>
<summary>Expand ⬇️</summary>
<br>

- Cloud computing is a name which refers to cluster machines on the cloud. 
- **Bare-metal** cloud is a public cloud service where the customer rents dedicated hardware resources from a remote service provider, without (hence bare) any installed operating systems or virtualization infrastructure.
- [[AWS (Amazon Web Services)](https://aws.amazon.com/?nc2=h_lg) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS)]
- [[Microsoft Azure](https://azure.microsoft.com/en-gb/) | Notes]
- [[GCP (Google Cloud Platform)](https://cloud.google.com/) | Notes]
</details>

***

## Edge computing
<details>
<summary>Expand ⬇️</summary>
<br>

- Edge computing referes to computation done on edge devices, meaning consumer devices. Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data.
- [TensorFlow Lite | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/TensorFLowLite.md)]
</details>

***

## Relational Database
RDB (relational database) is a database that stores data into tables with rows and columns. To be able to process SQL queries on huge volumes of data that is stored in Hadoop cluster, specialised tools are needed.
<details>
<summary>Expand ⬇️</summary>
<br>

- [MySQL](https://www.mysql.com/) is the world's most popular open source database.
- [PostgreSQL](https://www.postgresql.org/) is the world's most advanced open source database.
- [MariaDB](https://mariadb.org/) is an enhanced, drop-in replacement for MySQL.
- [Amazon RDS](https://aws.amazon.com/rds/) makes it easy to set up, operate, and scale a relational database in the cloud.
</details>

***

## Non-relational Database
Nonrelational “NoSQL” databases or also "not only SQL" represent data in tables, instead data is stored as key value pairs, wide-columns or graphs. The need for NoSQL databases is especially prevalent when you have a real-time system. NoSQL databases perform and scale best when your schema is designed to model the application’s access patterns, the frequency with which those patterns are called, and the velocity of access. The goal should be to precompute the answers to these access patterns, and only rarely ask questions of the data (ad hoc querying). This is true whether the data is key/value, wide column, or JSON document store. 

<details>
<summary>Expand ⬇️</summary>
<br>

- Document:
  - [MongoDB](https://www.mongodb.com/) is an open-source, document database designed for ease of development and scaling. It is classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. 
  - [Elastic](https://www.elastic.co/) search & analyze data in real time.
- Wide column:
  - [Apache Cassandra](https://cassandra.apache.org/_/index.html) is the right choice when you need scalability and high availability without compromising performance.
  - [Apache HBase](https://hbase.apache.org/) is the Hadoop database, a distributed, scalable, big data store.
  - [Google Bigtable](https://cloud.google.com/bigtable) is a fully managed wide-column and key-value NoSQL database service for large analytical and operational workloads
- Graph
  - [Neo4j](https://neo4j.com/) is the world’s leading graph database.
- Key-value
  - [Redis](https://redis.io/) is an open source, BSD licensed, advanced key-value cache and store.
  - [Google Bigtable](https://cloud.google.com/bigtable) is a fully managed wide-column and key-value NoSQL database service for large analytical and operational workloads
   - [AWS DynamoDB](https://aws.amazon.com/dynamodb/) is a fast and flexible NoSQL database service for all applications that need consistent, single-digit millisecond latency at any scale.
</details>

***

## Data warehouse tools
**Databases** are typically structured with a defined schema. Items are organized as a set of tables with columns and rows. Columns include attributes and rows indicate an object or entity. Database is typically designed to be transactional and they are not designed to perform data analytics. 

**Data warehouse** exists on top of several databases and used for business intelligence. Data warehouse consumes data from all these databases and creates a layer optimized to perform data analytics. 

**Data lake** uses a flat architecture. Every bit of data in the lake has a unique ID and is tagged with sets of extended metadata tags. A data lake is a centralized repository for structured and unstructured data storage.  Data lakes could be used to store raw data *as is* (this is the bid differentiator) without any structure (schema).  There is no need to perform any ETL or transformation jobs on it.  You can store many types of data such images, text, files, videos. 
<details>
<summary>Expand ⬇️</summary>
<br>
 
- [Snowflake](https://www.snowflake.com/en/) - offers a cloud-based data storage and analytics service, generally termed "data-as-a-service".
- [Presto](https://prestodb.io/) is an open source SQL query engine that's fast, reliable, and efficient at scale. Use Presto to run interactive/ad hoc queries at sub-second performance for your high volume apps.
- [Amazon Redshift](https://aws.amazon.com/redshift/) uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale.
- [Azure Synapse](https://azure.microsoft.com/en-us/products/synapse-analytics/) is a limitless analytics service that brings together data integration, enterprise data warehousing, and big data analytics. It gives you the freedom to query data on your terms, using either serverless or dedicated options—at scale
- [Google bigquery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=emea-gb-all-en-dr-bkws-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_253506573802-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Data%20Analytics%20~%20BigQuery%23v7-KWID_43700053283817151-kwd-63326440124-userloc_9045312&utm_term=KW_google%20bigquery-NET_g-PLAC_&gclid=Cj0KCQiAiJSeBhCCARIsAHnAzT9ZSudPHNYsr7-5adSmRpuTJFpoQjr1_MfOWqoObOa8cA-6KXYMlzgaApS5EALw_wcB&gclsrc=aw.ds) is a fully managed, serverless data warehouse that enables scalable analysis over petabytes of data. It is a Platform as a Service
- [[Apache Hive](https://hive.apache.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Hive.md)] (twice as popular as Pig and developed by Facebook). Hive provides SQL type querying language for the ETL purpose on top of Hadoop file system. 
- [Apache Impala](https://impala.apache.org/docs/build/html/topics/impala_langref.html)
</details>

***

## Object storage
<details>
<summary>Expand ⬇️</summary>
<br>

- [AWS S3](https://aws.amazon.com/s3/)
- Azure Blob Storage
- Google Cloud Storage
</details>

***

## Data processing
Hybrid means they are able to process data in batches or continuous streaming. Batch data processing is generally done by analytical data warehouse applications.
<details>
<summary>Expand ⬇️</summary>
<br>

- Batch
  - [Apache Pig](https://pig.apache.org/) is a high-level platform for creating programs that run on Apache Hadoop. The language for this platform is called Pig Latin. Pig can execute its Hadoop jobs in MapReduce, Apache Tez, or Apache Spark. Less popular than Hive.
  - [Apache Arrow](https://arrow.apache.org/) is a language-agnostic software framework for developing data analytics applications that process columnar data. It contains a standardized column-oriented memory format that is able to represent flat and hierarchical data for efficient analytic operations on modern CPU and GPU hardware
- Hybrid
  - [[Apache Spark](https://spark.apache.org/) | [Notes](https://github.com/kyaiooiayk/pySpark-Notes)]
  - Apache Beam
  - Apache Flink
  - Apache NiFi
- Streaming
  - [Apache Kafka](https://kafka.apache.org/) is a distributed event store and stream-processing platform. It is an open-source system developed by the Apache Software Foundation written in Java and Scala. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. 
  - Google Dataflow
</details>

***

## Schedulers
<details>
<summary>Expand ⬇️</summary>
<br>

- [5 ways to schedule Jupyter Notebook](https://mljar.com/blog/schedule-jupyter-notebook/)
</details>

***

## RESTful APIs & Microservices
<details>
<summary>Expand ⬇️</summary>
<br>

- **Microservices** function as the “building‐blocks” of the application by performing various services.
- **RESTful APIs** function as the “glue” that integrates the microservices into an application.
- [NOTES](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/RESTful%20APIs%20%26%20Microservices)
</details>

***

## Version control system (VCS)
<details>
<summary>Expand ⬇️</summary>
<br>

- Version control system (VCS) also known as revision control or source control, records and manages changes to files and folders. [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/VCS/VCS.md)
- [[Hydra](https://hydra.cc/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/Hydra)]
- [[DVC](https://dvc.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/DVC)]
</details>

***

## Servers
<details>
<summary>Expand ⬇️</summary>
<br>

- [[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)] stands for Web Server Gateway Interface and is an application server that aims to provide a full stack for developing and deploying web applications and services. It is named after the Web Server Gateway Interface, which was the first plugin supported by the project.
- [[Nginx](https://www.nginx.com/)] is a web server that can also be used as a reverse proxy (which provides a more robust connection handling), load balancer, mail proxy and HTTP cache.
</details>

***

## References
- [Guide to evaluating MLOps platforms *by thoughtworks*](https://www.thoughtworks.com/content/dam/thoughtworks/documents/whitepaper/tw_whitepaper_guide_to_evaluating_mlops_platforms_2021.pdf)
- [MLOps Is a Mess But That's to be Expected](https://www.mihaileric.com/posts/mlops-is-a-mess/)
- [VCS](https://deploybot.com/blog/version-control-systems-and-continuous-deployment-tools-a-perfect-fit)
- [ML Experiment Tracking: What It Is, Why It Matters, and How to Implement It](https://neptune.ai/blog/ml-experiment-tracking)
- [HTTP vs. REST APIs](https://hevodata.com/learn/http-api-vs-rest-api/)
- [Awesome production machine learning](https://github.com/EthicalML/awesome-production-machine-learning#model-and-data-versioning)
- [MLOps Is a Mess But That’s to be Expected](https://www.kdnuggets.com/2022/03/mlops-mess-expected.html)
- [MLOps Principles](https://ml-ops.org/content/mlops-principles)
- [What is an MLOps Engineer?](https://www.kdnuggets.com/2022/03/mlops-engineer.html)
- [Google Rules of Machine Learning: Best Practices for ML Engineering](https://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf)
- [Top 10 MLOps Tools to Optimize & Manage Machine Learning Lifecycle](https://www.kdnuggets.com/2022/10/top-10-mlops-tools-optimize-manage-machine-learning-lifecycle.html)
- [The MLOps Blog run by neptune.ai](https://neptune.ai/blog)
- [Awesome production machine learning](https://github.com/EthicalML/awesome-production-machine-learning/blob/master/README.md)
- [Best End-to-End MLOps Platforms comparison](https://neptune.ai/blog/end-to-end-mlops-platforms)
***
