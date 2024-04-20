pipeline {
    agent any
    stages {
        stage('Terraform Init') {
            steps {
                script {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "terraform init"
                    }
                }
            }
        }
        stage('Terraform Plan') {
            steps {
                script {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "terraform plan"
                    }
                }
            }
        }
        stage('Terraform Apply & Deploy Docker Image on Webserver') {
            steps {
                script {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "terraform apply -auto-approve"
                    }
                }
            }
        }
    }
}
