pipeline {
    agent {
        docker {image 'thinh28042001/mycrawler'}
    } 
    stages {
        stage('Build') { 
            steps {
                sh """
                    python --version
                    docker build -t mycrawler .
                    docker compose up
                """ 
            }
        }
    }
}