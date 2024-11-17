# Deployed MLops sentinment analysis project 

# Step 1 : Deploying application on AWS

Deployed the application on the Aws on ec2 instance on ubuntu OS

# Step 2 : installed the docker tools 
sudo apt update -y 
sudo apt install docker.io
sudo chown ubuntu /var/run/docker.sock

#check the dockerfile is perfectly running or not 
use command : docker ps 

# Step 3 : Docker Env
To create a Dockerfile for this Streamlit application, you’ll need to set up a Docker environment, install all required libraries, and expose the appropriate port.

# Step 4 : requirements.txt
In the  project folder, created a requirements.txt file listing the necessary packages. Based on code

# Step 5 : Build and Run the Docker Container
Once you have the Dockerfile and requirements.txt in place, you can build and run the Docker container.

Build the Docker Image:
docker build -t sentiment-analysis-app .

Run the Docker Container:
docker run -p 8501:8501 sentiment-analysis-app
