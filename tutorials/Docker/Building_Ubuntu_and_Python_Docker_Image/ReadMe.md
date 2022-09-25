# Building an Ubuntu and Python Docker Image
*This section illustrates the building of a Docker image based on the latest version of Ubuntu. *
***

## Description of the files needed
To this end, two scripts are needed:
  - One is a bash script named `install.sh` that does all the work on the Linux level. \
  - The other is a Docker file  nammed `Dockerfile` which controls the building procedure for the image itself.
***

## Installation procedure
- Make sure thath the `Dockerfile` and `install.sh` are in the same folder 
- Make sure that `Docker` is installed.
- Run the following command `docker build -t <your_docker_image_name:tag>` to build the Docker image. What comes after `:`is a tage you want to assign to your contatiner.
- Make sure the image is now listed with: `docker images`.
- Run the Docker container with `docker run <your_docker_image_name:tag>`.
- The `docker ps` command will still show the running container.
- You can detach from a container by typing `Ctrl-P +Ctrl-Q`.
- Attaching to a Docker container is accomplished with the command `docker attach $CONTAINER_ID` (notice that a few letters of the $CONTAINER_ID are enough).
- The `exit` command stops the Docker container. It can be removed with `docker rm $CONTAINER_ID`.- 
- The Docker image can be removed via `docker rmi` if not needed any longer as this my take a considerable amount of space.


## Refeneces
- [Source Code](https://github.com/yhilpisch/py4fi2nd/tree/master/code/ch02/Docker)
- Hilpisch, Yves. Python for finance: mastering data-driven finance. O'Reilly Media, 2018.
