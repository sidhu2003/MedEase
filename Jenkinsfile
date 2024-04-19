pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Building the medease application on Docker'
                sh 'docker-compose up --build -d'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying the medease application on Docker'
                sh 'docker-compose up -d'
            }
        }
    }
}