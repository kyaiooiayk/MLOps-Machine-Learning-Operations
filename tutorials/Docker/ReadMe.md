# Docker

## Brief intro on Docker
- Docker is a tool designed to create, deploy, and run applications by using containers. The applications you build, if shipped with a docker image, become reproducible anywhere. 
- It is open-source and essentially a container file format. It automates the deployment of applications as portable, self-sufficient containers that can run in the cloud or on-premises.
- A container is a standardized software unit, in simple terms — nothing but a packaged bundle of application code and required libraries and other dependencies.
- A **Docker Image** is an executable software package that includes everything needed to run an application and becomes a Container at runtime.

## Docker (Docker Swarm!) vs. Kubernets
- **Docker** is meant to be run on a single node.
- While it’s common to compare Kubernetes with Docker, a more apt comparison is Kubernetes vs **Docker Swarm**. Docker Swarm is Docker’s orchestration technology that focuses on clustering for Docker containers – tightly integrated into the Docker ecosystem and using its own API.
- **Kubernetes** (also known as k8s) is meant to run across a cluster environment. It is more extensive than Docker and is meant to coordinate clusters of nodes at scale in production in an efficient manner. While Docker provides an open standard for packaging and distributing containerised apps, the potential complexities can add up fast. How do you coordinate and schedule several containers? How do all of the different containers in your app talk to each other? How do you scale several container instances? This is where Kubernetes can help.
- **Can you use them together?** Although they are fundamentally different technologies, they work well together when building, delivering and scaling containerised apps.

## List of commands
- **Create a container**: `docker run CONTAINER --network NETWORK`
- **Start a stopped container**: `docker start CONTAINER NAME`
- **Stop a running container**: `docker stop`
- **List all running containers**: `docker ps`
- **List all containers including stopped ones**: do`cker ps -a`
- **Inspect the container configuration. For instance network settings and so on**: `docker inspect CONTAINER`
- **List all available virtual networks**: `docker network ls`
- **Create a new network**: `docker network create NETWORK --driver bridge`
- **Connect a running container to a network**: `docker network connect NETWORK CONTAINER`
- **Disconnect a running container from a network**: `docker network disconnect NETWORK CONTAINER`
- **Remove a network**: `docker network rm NETWOR`


References
- [How to Dockerize Any Machine Learning Application](https://towardsdatascience.com/how-to-dockerize-any-machine-learning-application-f78db654c601)







