pipeline {
    agent any
    stages {
        stage("Clone stage") {
            steps{
                withDockerRegistry(credentialsId: 'docker', url: 'https://index.docker.io/v1/'){
                    sh label : '', script: 'docker build -t mycrawler .'
                }
            }
        }
    }
}