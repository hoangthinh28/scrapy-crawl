pipeline {
    agent {
        docker {
            image "python:3.10.0-alpine"
        }
    }

    stages {
        stage('Build') { 
            steps {
                sh """
                    python --version
                    pip3 install --no-cache-dir -r requirements.txt
                    python crawl.py
                """
            }
        }
    }
}
