pipeline {
    
    agent any

    stages {
        stage('Build') {
             agent {
                docker {image 'python:3'}
            }
            steps {
                sh "python --version"
                sh "docker build -t mycrawler ."
                sh "docker compose up"
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