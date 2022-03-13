# VCS (Version Control System)

## CI vs. CD
- **Continuous Integration (CI)**: The code is built and tested on a regular basis, i.e. daily, several times per day, or – even better – with every commit. It is the practice of merging all developers' working copies to a shared mainline several times a day.
- **Continuous Delivery (CD)**: This is the next step, and its goal is to always have code available that can be released at any point. CD uses some automation (building and testing) but requires *human intervention* in the end when it comes to releasing to a productive environment. It is an approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time and, when releasing the software, without doing so manually.
- **Continuous Deployment (CD)**: All code changes are automatically built, tested, and released. It's similar to continuous delivery but also brings the new version to the production environment *without human intervention*.
- All three methods rely on a version control system – there is no way around it.

## GitHub vs. GitLab
- GIT stands for Global Information Tracker
- The most significant difference between the GitHub and Git Lab is that while GitHub is a collaboration platform that helps review and manage codes remotely, GitLab is majorly focused on DevOps and CI/CD.
- GitHub is more popular amongst the developers as it holds millions of repositories, but recently GitLab has been gaining popularity, as the company continues to add new features to make it more competitive and user-friendly.

## Semantic versioning of package
- Let's say we donwload a python package named `ML_Mine` version `0.19.2`. What do those numbers really mean?
  - `0.19.2` The first number in this chain is called the **major** version. when there's backwards incompatible changes, i.e. changes that break the old API are released. Usually, when major versions are released.
  - `(0.19.2)` The second number is called the **minor** version. When backwards compatible changes. Functionality is added (or speed improvements) that does not break any existing functionality, at least the public API that end- users would use
  - `(0.19.2)` The third number is called the **patch** version. backwards compatible bug fixes

## MLOps vs. DevOps
- Traditional software development often relies on DevOps, which involves Continuous Integration (CI), Continuous Delivery (CD), and Continuous Testing (CT) to reduce development time while continuously delivering new releases and maintaining quality.
- MLOps embraces DevOps’ continuous integration and continuous delivery, but replaces the *continuous testing* phase with *continuous training*. This continuous training of new models, which includes redeployment of those new models and all of the technical efforts that go along with it, aims to address three notable aspects of ML projects:
  - The need for explainability especially for auditing purposes.
  - Model decay, possibily due to data drifting.
  - The continuous development and enhancements to the model driven by business requirements. 
- **Continuous training** is a new property, unique to ML systems, that's concerned with automatically retraining and serving the models.
- There is another one called **Continuous Monitoring (CM)** which entitles to catching errors in production system, and monitoring production inference data and model performance metrics tied to business outcomes.

## 3 levels of MLOps processes
- **MLOps level 0: Manual process**: Many teams have data scientists and ML researchers who can build state-of-the-art models, but their process for building and deploying ML models is entirely manual. This is considered the basic level of maturity, or level 0. Deployment refers to the prediction service where concern is only with deploying the trained model as a prediction service (microservice with a REST API). MLOps level 0 is common in many businesses that are beginning to apply ML to their use cases. *Challenges*: this manual, data-scientist-driven process might be sufficient when models are rarely changed or trained. In practice, models often break when they are deployed in the real world.

- **MLOps level 1: ML pipeline automation**: The goal is to perform continuous training of the model by automating the ML pipeline; this lets you achieve continuous delivery of model prediction service. To automate the process of using new data to retrain models in production, you need to introduce automated data and model validation steps to the pipeline, as well as pipeline triggers and metadata management. In level 0, you deploy a trained model as a prediction service to production. For level 1, you deploy a whole training pipeline, which automatically and recurrently runs to serve the trained model as the prediction service. *Challenges*: If you manage many ML pipelines in production, you need a CI/CD setup to automate the build, test, and deployment of ML pipelines.
 
- **MLOps level 2: CI/CD pipeline automation**: For a rapid and reliable update of the pipelines in production, you need a robust automated CI/CD system. This automated CI/CD system lets your data scientists rapidly explore new ideas around feature engineering, model architecture, and hyperparameters. They can implement these ideas and automatically build, test, and deploy the new pipeline components to the target environment.

## References
- [DS is software](https://nbviewer.org/github/ethen8181/machine-learning/blob/master/data_science_is_software/notebooks/data_science_is_software.ipynb)
- [Implementing MLOps on an Edge Device](https://www.kdnuggets.com/2020/08/implementing-mlops-edge-device.html)
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#mlops_level_2_cicd_pipeline_automation)
