pipeline {
    agent {
        docker {
            image "python:3.10.0-alpine3.15"
        }
    }

    stages {
        stage('Build') { 
            steps {
                sh """
                    python --version
                    python crawl.py
                """
            }
        }
    }
}
