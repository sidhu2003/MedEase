pipeline {
    agent any
    tools {
        terraform 'terraform'
    }
    stages {
        stage ('Terraform Init') {
            steps {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "terraform init"
                    }
            }
        }
        stage ('Terraform Plan') {
            steps {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "terraform plan"
                    }
            }
        }
        stage ('Terraform Apply & Deploy Docker Image on Webserver') {
            steps {
                    withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
                        sh "terraform apply -auto-approve"
                    }
            }
        }
    }
}
