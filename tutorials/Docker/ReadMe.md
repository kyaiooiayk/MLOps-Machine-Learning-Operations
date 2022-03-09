# Docker

## Brief intro on Docker
- Docker is a tool designed to create, deploy, and run applications by using containers. The applications you build, if shipped with a docker image, become reproducible anywhere. 
- It is open-source and essentially a container file format. It automates the deployment of applications as portable, self-sufficient containers that can run in the cloud or on-premises.
- A container is a standardized software unit, in simple terms — nothing but a packaged bundle of application code and required libraries and other dependencies.
- A **Docker Image** is an executable software package that includes everything needed to run an application and becomes a Container at runtime.

## Docker (Docker Swarm!) vs. Kubernets
- **Docker** is meant to be run on a single node.
- While it’s common to compare Kubernetes with Docker, a more apt comparison is Kubernetes vs **Docker Swarm**. Docker Swarm is Docker’s orchestration technology that focuses on clustering for Docker containers – tightly integrated into the Docker ecosystem and using its own API.
- **Kubernetes** (also known as k8s) is meant to run across a cluster environment. It is more extensive than Docker and is meant to coordinate clusters of nodes at scale in production in an efficient manner. While Docker provides an open standard for packaging and distributing containerised apps, the potential complexities can add up fast. How do you coordinate and schedule several containers? How do all of the different containers in your app talk to each other? How do you scale several container instances? This is where Kubernetes can help. It contains all the parts and glue to form a resilient and reliable way of running services, including things like load balancers, resource quotas, scaling policies, traffic management, sharing secrets, and more.
- **Can you use them together?** Although they are fundamentally different technologies, they work well together when building, delivering and scaling containerised apps.

## Docker vs. Virtual Environment
- You could argue that virtual environment approaches such as conda and virtualenv address these issues. They do, but only partially.
- Several non-Python dependencies are not managed by these solutions.
- Due to the complexity of a typical machine learning stack, a large part of framework dependencies, such as hardware libraries, are outside the scope of virtual environments. 
- Conclusion? Containers can fully encapsulate not just your training code, but the entire dependency stack down to the hardware libraries.

## Sharing your container
- You have two options:
  - **Container image**: This is the easiest option. This allows every collaborator or a cluster management service, such as Kubernetes, to pull a container image, instantiate it, and execute training immediately.
  - **Dockerfile**: This is a lightweight option. Dockerfiles contain instructions on what dependencies to download, build, and compile to create a container image. Dockerfiles can be versioned along with your training code. You can automate the process of creating container images from Dockerfiles by using continuous integration services, such as AWS CodeBuild.

## Step-by-step guide to create a Docker image
- Step #1: Save all the packages in the file with: `pip freeze > requirements.txt`. It’s a good practice to list the exact version of the library rather than `><`, but this does not seem to have stuck among practioners. The file looks like something like this:
```
joblib==0.16.0
numpy==1.19.1
pandas==1.1.0
pandas-profiling==2.8.0 ▪ scikit-learn==0.23.2
streamlit==0.64.0
```
- Step #2: Write a Dockerfile file named `Dockerfile` that can be used to build the required virtual environment for our app to run on. Every Dockerfile has to start with a `FROM`. What follows FROM must be an already existing image (either locally on your machine or from the DockerHub repository). Since our environment is based on Python, we use python:3.7 as our base image and eventually create a new image using this Dockerfile. Streamlit runs on a default port of 8501. So for the app to run, it is important to expose that particular port. We use the EXPOSE command for that. WORKDIR sets the working directory for the application. The rest of the commands will be executed from this path. Here COPY command copies all of the files from your Docker client’s current directory to the working directory of the image. RUN command ensures that the libraries we defined in the requirements.txt are installed appropriately. CMD specifies what command to run within the container as it starts. Hence, streamlit run app.py ensures that the Streamlit app runs as soon as the container has spun up.
```
FROM python:3.7
EXPOSE 8501
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD streamlit run app.py
```
- Step #3: Build it and create an image. The idea is this image we create is the reproducible environment irrelevant to the underlying system. (The dot at the end signifies the path for the Dockerfile, which is the current directory.): `docker build --tag app:1.0 .`

- Step #4: Run command runs the specified container on the host machine. `--publish 8501:8501` lets the port 8501 of the container to be mapped to the port 8501 of the host machine, while -it is needed for running interactive processes (like shell/terminal): `docker run --publish 8501:8501 -it app:1.0` What do I do with it? You can share the built images on DockerHub or deploy them on the cloud, and so on.

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


## References
- [How to Dockerize Any Machine Learning Application](https://towardsdatascience.com/how-to-dockerize-any-machine-learning-application-f78db654c601)
- [Why use Docker containers for machine learning development?](https://aws.amazon.com/blogs/opensource/why-use-docker-containers-for-machine-learning-development/)
