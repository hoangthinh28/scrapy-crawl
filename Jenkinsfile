pipeline {
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'thinh28042001/mycrawler:latest'
                    image 'python:latest'
                }
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