# docker_python_flask

 ##Jenkins Pipeline to Build a Python Program and Deploy it on a Docker Container##
This Jenkins pipeline is an end-to-end pipeline for deploying a python application on a docker container. This pipeline is created on the development environment of Red hat Enterprise Linux 8 (RHEL 8) and python 3.
This Pipeline will be fetching the project code from SCM in our case we will be using GitHub.
We have created the Jenkins file which will run the pipeline which comes under the functionality provided by Jenkins .i.e., Pipeline as a Code.
Jenkins’s file:
The first line of code declares that it is a pipeline code by keyword "pipeline". Then we have to specify the agent for the stages to be executed in the pipeline. Agents can be docker, maven, etc. For our pipeline we will be declaring the agent as "any" because we do not have such a use case to build our project on a remote server, in that case, we may have used docker.
Next comes the stages of the pipeline we have three stages in the out pipeline
1.Checkout Stage- As we are using SCM as GitHub we need to check out it for Jenkins could fetch all the code files. So, in the steps, we will add the checkout steps along with the authentication details.
2.Build Stage-  In this stage, we will build our python program to be deployed in the next stage. To build it in steps we will first add the git authentication details incorrect syntax so that Jenkins can access the code from the GitHub.
In the next step, we will execute a shell script that will run the python command to run out python command. 
3. Deployment Stage -  In this stage, we will deploy our python program on the docker container. As our python program is built using the Flask framework so the end result of deployment will be shown in the web browser.
So, for deployment on docker, we have created a docker file and it will be used for launching a new docker container.
In steps first, we will again authenticate It with git in correct syntax and after that, we will run a script that runs docker command "docker build -t dockerpython” which will build our docker file with specification written in the docker file.
In the next step, we will run again run a shell script that will run the docker command " docker run -p 5000:5000 dockerpython” which will run the desired docker container with port 5000 exposed to the public. Now our program is successfully deployed and can be accessed by running the docker IP.

##How to run a job in Jenkins## –
Job is the task or set of tasks that you want Jenkins to be performed.
There can be many types of jobs in Jenkins like freestyle, pipeline, maven, etc.
The mainly used job in Jenkins is freestyle and pipeline.
We will first see how to run a freestyle job.
Step 1- We first need to select a new item and give a name to our job and select the type of project from the options i.e. Freestyle Project.
Step 2 – After that on the next page, we will see a wide variety of options to configure your project. like General,  Source Code Management, Build Triggers, Build Environment, Build, Post-build actions.
Step 3- In General Section, we can add the Description of our project/job.
Step 4- Source Code Management checks out code from version control hosts, which implies that if your code is hosted on GitHub or any other repositories, you have to add the repository details. Jenkins will clone the repository. To use the git option we need to install the git plugin from the manage Jenkins section.
Step 5- Under Source Code Management(SCM) tab,
Select Git as a repository source and enter your Git Repository URL.
In case you have your repository created locally, it is permissible to use a local repository.
Suppose the GitHub repository you are using is private. In that case, Jenkins will validate the login credentials with GitHub, and upon successful validation, it will then pull the source code from your GitHub repository.
Step 6-Go to the Build section and click on the Add build step.
Under the build section,
Click on the “Add build step.”
Then, “Execute Windows batch command” and add the commands you want to execute during the build process. E.g., Java compiles batch commands.
Step 7-When you have entered all the data,
Click Apply.
Save the project.
Step 8-On the left-hand side panel, click the Build Now button to build the source code.



