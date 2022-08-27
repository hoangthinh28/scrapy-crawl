pipeline {
    agent any
    stages {
        stage("Clone stage") {
            steps{
                withDockerRegistry(credentialsId: 'dockerHub', url: 'https://index.docker.io/v1/'){
                    sh label : '', script: 'docker build -t thinh28042001/mycrawler:latest .'
                }
            }
        }
    }
}