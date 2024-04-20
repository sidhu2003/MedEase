pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-jenkins')['AWS_ACCESS_KEY_ID']
        AWS_SECRET_ACCESS_KEY = credentials('aws-jenkins')['AWS_SECRET_ACCESS_KEY']
        AWS_DEFAULT_REGION = 'us-east-1'
        registryUrl = 'programmer175/django-app'
        registryCredential = 'programmer175'
    }

    stages {
        stage ('Build Docker Image') {
            steps {
                script {
                   dockerImage = docker.build registryUrl + ":$BUILD_NUMBER"
                }
            }
            
        }
        stage ('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
