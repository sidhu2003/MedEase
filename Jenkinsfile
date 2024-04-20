pipeline {
    agent any

    environment {
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
                    docker.withRegistry(registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
