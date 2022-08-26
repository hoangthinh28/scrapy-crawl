pipeline {
    agent none

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }

            steps {
                sh "python --version"
                sh "pip3 install --no-cache-dir -r requirements.txt"
                sh "python crawl.py"
            }
        }
        stage('Test') {
            steps {
                sh "scrapy crawl posts -o posts.json"
            }
        }
    }
}