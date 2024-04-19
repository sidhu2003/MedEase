pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Building the medease application on Docker'
                sh 'docker-compose -f docker-compose-production.yml build -d'
            } 
        }
        stage('Deploy'){
            steps{
                echo 'Deploying the medease application on Docker'
                sh 'docker-compose -f docker-compose-production.yml up -d'
            }
        }
    }
}