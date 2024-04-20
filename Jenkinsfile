pipeline {
    agent any

    environment {
        registryUrl = 'programmer175/django-app'
        registryCredential = 'programmer175'
        dockerImage = ''
        AWS_API_KEY = credentials('jenkins-aws')
    }

    tools {
        terraform 'terraform'
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
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage ('Deploy with Terraform') {
            steps {
                withCredentials([(credentialsId: 'jenkins-aws', variable: 'AWS_API_KEY')]){
                    sh 'cd terraform && terraform init && terraform apply -auto-approve'
                }       
            }
        }
    }
}
