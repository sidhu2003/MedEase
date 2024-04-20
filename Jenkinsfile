pipeline {
    agent any
    stages {
         stage ('Terraform Init'){
            steps {
            withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
            sh "terraform init"
          }
            }
       }
         stage ('Terraform Plan'){
            steps {
            withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
            sh "terraform plan" 
            }
         }
      }
         stage ('Terraform Apply & Deploy Docker Image on Webserver'){
            withAWS(credentials: 'aws-jenkins', region: 'us-east-1') {
            steps {
            sh "terraform apply -auto-approve"
        }
            }
      }
    }
  }