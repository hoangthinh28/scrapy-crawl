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
                    pip install Scrapy
                    python crawl.py
                """
            }
        }
    }
}
