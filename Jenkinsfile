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
                    python --version
                    pip3 install -r requirements.txt
                    python crawl.py
                """
            }
        }
    }
}
