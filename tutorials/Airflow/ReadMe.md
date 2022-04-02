# Apache Airflow
***

## Intoduction
- What is it? Apache Airflow is a workflow automation and scheduling system that can be used to author and manage data pipelines. Airflow uses workflows made of directed acyclic graphs (DAGs) of tasks.
- What are DAGs? DAGs are collections of all the tasks you want to run, written in python
- Is Airflow an ETL tool? Apache Airflow for Python-Based Workflows. ... Airflow isn't an ETL tool per se. But it manages, structures, and organizes ETL pipelines using something called Directed Acyclic Graphs (DAGs)
- Is Airflow Apache free? Airflow is free and open source, licensed under Apache License 2.0.
***

## An example of DAG
- Let's imagine that a given DAG consists of three tasks, like: 
  - T1 - preparing data to make a report 
  - T2 - making the report 
  - T3 - sending an email notification that the report is ready 
- You can organize the whole process by defining the rule that T1 runs first and T2 cannot start before the T1 is done. Now, you can also decide that T2 will be restarted 3 times (or more if you wish) if it fails. In case everything goes according to plan, and a report is created, you can schedule an email notification (T3) just after T2 is finished.
***

## Weakness
- No versioning of your data pipelines. ... 
- Not intuitive for new users. ... 
- Configuration overload right from the start + hard to use locally. ... 
- Setting up Airflow architecture for production is NOT easy. ... 
- Lack of data sharing between tasks encourages not-atomic tasks. ... 
- Scheduler as a bottleneck.
***

## References
- https://www.techtimes.com/articles/256141/20210120/what-is-apache-airflow-and-why-should-you-use-it-in-your-company.htm 
