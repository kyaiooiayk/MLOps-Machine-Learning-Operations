# Prefect
***

## What is it?
- It is a open-source tool designed for modern ML-driven workflow orchestration. 
- It has a set of tools for scheduling and monitoring work that you want to complete. Ex: Scheduling ML models training. The purpose of workflow orchestration is to reduce mistakes and gently fail. 
- It aims to decrease negative engineering and simplify workflow orchestration when compared to existing products like Airflow.
***

## Prefect vs. Apache Airflow
- Prefect is new to the ML workflow space and lacks a few integrations. This is where Apache Airflow features are several steps ahead of Prefect. 
- **However**, being developed almost a decade ago, Airflow is not perfect for modern data environments that manage dynamic workflows.
***

## How does it work?
- First, let’s understand tasks and flow in prefect:
  - A **flow** is the basis of all Prefect workflows. A flow is a Python function decorated with a `@flow` decorator.
  - A **task** is a Python function decorated with a `@task` decorator. Tasks represent distinct pieces of work executed within a flow.
***

## References
- [Create Robust Data Pipelines with Prefect, Docker, and GitHub](https://towardsdatascience.com/create-robust-data-pipelines-with-prefect-docker-and-github-12b231ca6ed2)
- [ML Workflow Orchestration](https://medium.com/@haythemtellili/ml-workflow-orchestration-ddc8165c26c0)
***
