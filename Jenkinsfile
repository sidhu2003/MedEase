pipeline {
    agent any
    stages {
        stage ('Terraform Init') {
            steps {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "cd terraform && terraform init"
                    }
            }
        }
        stage ('Terraform Plan') {
            steps {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "cd terraform && terraform plan"
                    }
            }
        }
        stage ('Terraform Apply & Deploy Docker Image on Webserver') {
            steps {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "cd terraform && terraform apply -auto-approve"
                    }
            }
        }
    }
}
