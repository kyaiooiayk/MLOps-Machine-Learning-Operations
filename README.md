# MLOps (Machine Learning Operations)
How to create, deploy and manage your ML projects. But what do we mean when we talk about model deployment? Training a ML model using a method of your choice. Writing a service using FastAPI for exposing the model through a service endpoint. Packaging the service into a Docker container. Deploying the Docker container to (AWS) Kubernetes Cluster to scale up the service.

![image](https://user-images.githubusercontent.com/89139139/148684996-107b35e5-7136-4842-a132-119db6ee48ce.png)
***

## Big data
- Hadoop
- [[Apache Spark](https://spark.apache.org/) | [Notes](https://github.com/kyaiooiayk/pySpark-Notes)]
***

## Data Engineering - Pipelines
- Apache Nifi
- Argo workflow
- [Azure databricks](https://azure.microsoft.com/en-us/products/databricks/) is a fast, easy, and collaborative Apache Spark-based big data analytics service designed for data science and data engineering.
- [[Apache Airflow](https://airflow.apache.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Airflow)] Apache is a very mature and popular option initially developed to orchestrate data engineering and extract-transform-load (ETL) pipelines for analytics workloads. Airflow has expanded into the machine-learning space as a viable pipeline orchestrator. 
- [Apache Beam](https://beam.apache.org/) is an open source tool for defining and executing data-processing jobs. Apache Beam can be used to describe batch processes, streaming operations, and data pipelines. In fact, TFX relies on Apache Beam and uses it under the hood for a variety of components (e.g., TensorFlow Transform or TensorFlow Data Validation). You can run the same data pipeline on Apache Spark or Google Cloud Dataflow without a single change in the pipeline description. Also, Apache Beam was not just developed to describe batch processes but to support streaming operations seamlessly.  
- **[Kubeflow](https://www.kubeflow.org/) Pipelines** is an orchestration subsystem built on Kubernetes that includes an orchestration subsystem called Kubeflow Pipelines. 
- [[MLeap](https://github.com/combust/mleap) | Notes] It allows data scientists and engineers to deploy machine learning pipelines from Spark and Scikit-learn to a portable format and execution engine. MLeap is a common serialisation format and execution engine for machine learning pipelines. 
- [[Prefect](https://www.prefect.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Prefect)]
- MLFlow is an open source project that offers experiment tracking and multiframe‐work support including Apache Spark, but limited workflow support. If you need a lightweight, simple way to track experiments and run simple workflows, this may be a good choice.
- Kubeflow
- [[Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/TensorFlowServing.md)]
- AWS SageMaker - Amazon SageMaker is a cloud machine-learning platform that was launched in November 2017. SageMaker enables developers to create, train, and deploy machine-learning models in the cloud. SageMaker also enables developers to deploy ML models on embedded systems and edge-devices.
- Google Vertex AI - diret competitor of AWS SageMaker
- [Tensor Flow Extended (TFX)](https://www.tensorflow.org/tfx) is an open source collection of Python libraries used within a pipeline orchestrator such as Kubeflow Pipelines, Apache Airflow, and MLflow.
***

## Data validation
- [[Pandera](https://pandera.readthedocs.io/en/stable/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Data_validation/Pandera)]
- [[Great Expectations](https://greatexpectations.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Data_validation/Great_expectations)]
***

## Model serialisation
- Serialisation is the process of translating a data structure or object state into a format that can be stored or transmitted and reconstructed later. 
- Common formats: hdf5, json, pickle, joblib, dill, ONNX
- [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Model_Serialisation)
***

## Dashboard
- Bokeh
- Plotly
***

## Deployment options
You essentially have two options:
 - If our application requires **low latency**, then we should deploy the model as a real- time API to provide super-fast predictions on single prediction requests over HTTPS, for example. We can deploy, scale, and compare our model prediction servers with SageMaker Endpoints using the REST API protocol with HTTPS and JSON.
 - For **less-latency-sensitive** applications that require high throughput, we should deploy our model as a batch job to perform batch predictions on large amounts of data in S3, for example. We will use SageMaker Batch Transform to perform the batch predictions along with a data store like Amazon RDS or DynamoDB to productionize the predictions,
***

## DevOps
DevOps is a role that integrates the job scope of software developers and operations teams to automate workflows.

- Maven : it is used to create deployment package.
- [[Docker](https://www.docker.com/) | [Notes](https://github.com/kyaiooiayk/Docker-Notes)]
- [[Kubernets](https://kubernetes.io/) | [Notes](https://github.com/kyaiooiayk/Kubernetes-Notes)]
- [Packaging | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Packaging)]
- [[Apache Jmeter](https://jmeter.apache.org/) |[Notes](https://github.com/ethen8181/machine-learning/tree/master/model_deployment/fastapi_kubernetes)]
- [ Git | [Notes](https://github.com/kyaiooiayk/Git-Cheatsheet)]
***

## CI/CD
In modern software development teams, continuous integration (CI) and continuous deployment (CD) are standard practices.  CI is about how the project should be built and tested in various runtimes, automatically and continuously. CD is needed so that every new bit of code that passes automated testing can be released into production with no extra effort. 
- [[GitHub Actions](https://github.com/features/actions) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/GitHub_Actions.md)]
- [[Jenkins](https://www.jenkins.io/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Jenkins)]
- [CI/CD tools comparison](https://neptune.ai/blog/continuous-integration-continuous-deployment-tools-for-machine-learning)
***

## Application Framework/Model Deployment
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
***

## Public server deployment
- [[Heroku](https://www.heroku.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/Heroku)] - allows access directly to your GitHub account
- [[PythonAnywhere](https://www.pythonanywhere.com/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/pythonanywhere)] - does not allow access directly to your GitHub account
- [[Netlify](https://www.netlify.com/) | [Notes]] - allows access directly to your GitHub account
***

## Cloud computing
- Cloud computing is a name which refers to cluster machines on the cloud. 
- **Bare-metal** cloud is a public cloud service where the customer rents dedicated hardware resources from a remote service provider, without (hence bare) any installed operating systems or virtualization infrastructure.
- [[AWS (Amazon Web Services)](https://aws.amazon.com/?nc2=h_lg) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/AWS)]
- [[Microsoft Azure](https://azure.microsoft.com/en-gb/) | Notes]
- [[GCP (Google Cloud Platform)](https://cloud.google.com/) | Notes]
***

## Edge computing
- Edge computing referes to computation done on edge devices, meaning consumer devices. Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data.
- [TensorFlow Lite | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/TensorFLowLite.md)]
***

## Relational Database
- RDB (relational database) is a database that stores data into tables with rows and columns.
- How to turn SQL-like into a map-reduce job that can run on a distributed file system. This is essentially what we mean by relational database at scale.
- [Hive | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/Hive.md)] (twice as popular as Pig and developed by Facebook). Hive provides SQL type querying language for the ETL purpose on top of Hadoop file system. 
- Pig (less popular than Hive)
***

## Data warehouse tools
**Databases** are typically structured with a defined schema. Items are organized as a set of tables with columns and rows. Columns include attributes and rows indicate an object or entity. Database is typically designed to be transactional and they are not designed to perform data analytics. 

**Data warehouse** exists on top of several databases and used for business intelligence. Data warehouse consumes data from all these databases and creates a layer optimized to perform data analytics. 

**Data lake** uses a flat architecture. Every bit of data in the lake has a unique ID and is tagged with sets of extended metadata tags. A data lake is a centralized repository for structured and unstructured data storage.  Data lakes could be used to store raw data as is without any structure (schema).  There is no need to perform any ETL or transformation jobs on it.  You can store many types of data such images, text, files, videos. 
- MongoDB

- CosmosDB
- Looker
- Stitch
- DBT
- [Snowflake](https://www.snowflake.com/en/) - offers a cloud-based data storage and analytics service, generally termed "data-as-a-service".
- Amazon redshift
- Azure synapse
- [Google bigquery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=emea-gb-all-en-dr-bkws-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_253506573802-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Data%20Analytics%20~%20BigQuery%23v7-KWID_43700053283817151-kwd-63326440124-userloc_9045312&utm_term=KW_google%20bigquery-NET_g-PLAC_&gclid=Cj0KCQiAiJSeBhCCARIsAHnAzT9ZSudPHNYsr7-5adSmRpuTJFpoQjr1_MfOWqoObOa8cA-6KXYMlzgaApS5EALw_wcB&gclsrc=aw.ds) is a fully managed, serverless data warehouse that enables scalable analysis over petabytes of data. It is a Platform as a Service
***

## Streaming
- Apache Kafka
- Google Dataflow
***

## Schedulers
- [5 ways to schedule Jupyter Notebook](https://mljar.com/blog/schedule-jupyter-notebook/)
***

## RESTful APIs & Microservices
- **Microservices** function as the “building‐blocks” of the application by performing various services.
- **RESTful APIs** function as the “glue” that integrates the microservices into an application.
- [NOTES](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/RESTful%20APIs%20%26%20Microservices)
***

## Version control system (VCS)
- Version control system (VCS) also known as revision control or source control, records and manages changes to files and folders. [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/blob/master/tutorials/VCS/VCS.md)
- [[Hydra](https://hydra.cc/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/Hydra)]
- [[DVC](https://dvc.org/) | [Notes](https://github.com/kyaiooiayk/MLOps-Machine-Learning-Operations/tree/master/tutorials/VCS/DVC)]
***

## Servers
- [[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)] is an application server that aims to provide a full stack for developing and deploying web applications and services. It is named after the Web Server Gateway Interface, which was the first plugin supported by the project.
- [[Nginx](https://www.nginx.com/)] is a web server that can also be used as a reverse proxy (which provides a more robust connection handling), load balancer, mail proxy and HTTP cache.
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
