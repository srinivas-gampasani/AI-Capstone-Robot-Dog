Overview
This project uses Docker to run a containerized application. Use the provided scripts to build the Docker image and start the container.

Prerequisites
Docker: Make sure Docker is installed and running on your system.
X Server:
Windows: Install VcXsrv(https://sourceforge.net/projects/vcxsrv/).
macOS: Install XQuartz(https://www.xquartz.org/).

Building the Docker Image
Run the docker_build.sh script to build the Docker image: { ./docker_build.sh }
Starting the Docker Container
Use the start_docker_instance.py script to start the Docker container: {python start_docker_instance.py}

Configuring the X Server
For Windows (VcXsrv):
1.Install VcXsrv.
2.While configuring Select Multiple windows,Start no client, and tick all the boxes.
For macOS (XQuartz):
1.Install XQuartz.
2.Open XQuartz and go to Preferences > Security. Check "Allow connections from network clients."
3.Restart XQuartz and configure the DISPLAY environment variable in your Docker container.
