pipeline {
    agent {
        docker {
            image "python:3.8-alpine"
        }
    }

    stages {
        stage('Build') { 
            steps {
                sh """
                    docker --version
                    python --version
                """
            }
        }
    }
}
