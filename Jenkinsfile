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
        stage('Deploy with Terraform') {
            environment {
                AWS_ACCESS_KEY_ID = credentials('jenkins-aws').AWS_ACCESS_KEY_ID
                AWS_SECRET_ACCESS_KEY = credentials('jenkins-aws').AWS_SECRET_ACCESS_KEY
            }
            steps {
                sh 'cd terraform && terraform init && terraform apply -auto-approve'
            }
        }
    }
    }
}
