# Jenkins
***

## Introduction
- Jenkins is an open source continuous integration/continuous delivery and deployment (CI/CD) automation software DevOps tool written in the Java programming language. It is used to implement CI/CD workflows. 
- It is also used to create deployment package. Jenkins provides mechanisms to restart any failed components and keep the pipeline running. Human intervention is often required, however. Jenkins supports manual, human-in-the-loop feedback as well.
- It’s important to understand that Jenkins is not the same as CloudBees. CloudBees is the company that primarily maintains Jenkins.
- The four products used by the Jenkins community are:
  - **Jenkins Open Source** natively supports application building, artifact packaging, application testing, and pull requests. Extending the native functionality of Jenkins to support Continuous Delivery is done through plugins.
  - **Jenkins X** is meant to make running a pipeline out of the box with Kubernetes easier. Jenkins X natively integrates Jenkins CI/CD server, Kubernetes, Helm, and other tools to offer a prescriptive CI/CD pipeline with best practices built-in, such as using GitOps to manage environments. It deploys Jenkins into Kubernetes containers to get around the complexities of installing and integrating Jenkins. However, it is a complex pairing of many tools including the fragile Jenkins server.
  - **CloudBees Core** is a distinct product built on top of open source Jenkins and is a paid tool. CloudBees CI has two components: the Client Master and the Operations Center. The Client Master is a Jenkins master, whose main function is to coordinate the building of projects such as Pipelines. When a CloudBees CI installation consists of two or more Client Masters, it is usually a good idea to install an Operations Center instance to manage these Client Masters.
  - **CloudBees Jenkins Distribution** is free software that provides developers with a Jenkins environment built on the most recent supported Jenkins release. The distribution comes with a recommended catalog of tested plugins available through the CloudBees Assurance Program.
***

## Jenkins vs. Git
- Developers describe Git as "Fast, scalable, distributed revision control system". Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. On the other hand, Jenkins is detailed as "An extendable open source continuous integration server". In a nutshell Jenkins CI is the leading open-source continuous integration server. Built with Java, it provides over 300 plugins to support building and testing virtually any project.
- Git and Jenkins are primarily classified as "Version Control System" and "Continuous Integration" tools respectively.
- "Distributed version control system", "Efficient branching and merging" and "Fast" are the key factors why developers consider Git; whereas "Hosted internally", "Free open source" and "Great to build, deploy or launch anything async" are the primary reasons why Jenkins is favored.
***

## GitHub Actions vs. Jenkins
- Since GitHub Actions is a fully managed service by GitHub, you don’t need to know how to scale and operate the infrastructure to run it, whereas with Jenkins you have to manage it.
- If you already use Github, never used Jenkins before and you are about to lean about CI/CD then GitHub Actions seems to be a natural choice.
***

## References
- [GitLab Differentiators](https://about.gitlab.com/devops-tools/jenkins-vs-gitlab/gitlab-differentiators/)
- [Git vs Jenkins](https://stackshare.io/stackups/git-vs-jenkins)
- [Github Actions or Jenkins?](https://blog.bitsrc.io/github-actions-or-jenkins-making-the-right-choice-for-you-9ac774684c8)
***
