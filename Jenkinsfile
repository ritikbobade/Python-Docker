pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '6761344f-84ef-4b25-b35c-e48d02445e17', url: 'https://github.com/ritikbobade/Python-Docker']]])
                echo 'Check out Complete'
            }
        }
        
        stage('Build'){
            steps{
                git credentialsId: '9d16d0f0-4c06-4cb0-b6ca-02fc02bdefcc', url: 'https://github.com/ritikbobade/Python-Docker'
                sh '''#!/bin/bash
                python3 print.py'''
                echo 'Build Complete'
            }
        }
        
        stage('Deploy'){
            steps{
                git credentialsId: '9d16d0f0-4c06-4cb0-b6ca-02fc02bdefcc', url: 'https://github.com/ritikbobade/Python-Docker'
                sh '''#!/bin/bash
                docker build -t dockerpython .'''
                sh '''#!/bin/bash
                    docker run -p 5000:5000 dockerpython'''
                echo 'Deploy succesful'
                
                    
            }
        }
    }
}
