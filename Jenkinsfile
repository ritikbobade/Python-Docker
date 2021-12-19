pipeline {
    agent any
    //The above line tells to use any agent for the following pipline code written below
    stages {
        //There are many stages in a piepline the above line states below written code are the stages of the pipeline
        stage('Checkout'){
            // As this project is a Github project so we have to checkout (stage) it in order jenkins can fetch the repository, above line of code do the same
            steps {
                //The above line of code tells the steps to be executed in this particular stage
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '*******', url: 'https://github.com/ritikbobade/Python-Docker']]])
                //This line of code give the credentials for the github in order jenkins can checkout from the git.
                echo 'Checkout Complete'
                //Last we print a message telling the checkout is complete
            }
        }
        
        stage('Build'){
            // This stage is the builing stage in which the program will be build.
            steps{
                //The above line of code tells the steps to be executed in build stage
                git credentialsId: '******', url: 'https://github.com/ritikbobade/Python-Docker'
                // The above line of code connect to github with authentication credentials for build purpose
                sh '''#!/bin/bash
                python3 print.py'''
                //Line of code to execute a shell script to build our python program.
                echo 'Build Complete'
                //Last we print a message telling the Build is complete
            }
        }
        
        stage('Deploy'){
            // This stage is the deployement stage in which the program will be Deployed.
            steps{
                //The above line of code tells the steps to be executed in Deployement stage
                git credentialsId: '****', url: 'https://github.com/ritikbobade/Python-Docker'
                // The above line of code connect to github with authentication credentials for deployement purpose
                sh '''#!/bin/bash
                docker build -t dockerpython .'''
                // As we are deploying our program on docker container the above shell script buil the dockerfile we have created.
                sh '''#!/bin/bash
                    docker run -p 5000:5000 dockerpython'''
                //After succefully build of our docker image we will now run it by the above script.
                echo 'Deploy succesful'
                // This print the message that the Deployement was succesful
                
                    
            }
        }
    }
}
