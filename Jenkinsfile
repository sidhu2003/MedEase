pipeline {
    agent any

    environment {
        registryUrl = 'programmer175/django-app'
        registryCredential = 'programmer175'
        dockerImage = ''
        AWS_DEFAULT_REGION = 'us-east-1'
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
                     sh 'cd terraform && terraform init && terraform apply -auto-approve'
                    
            }
        }
    }
}
