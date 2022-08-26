pipeline {
    agent none
    stages {
        stage('Build') { 
            steps {
                sh "python --version"
                sh "docker build -t mycrawler ."
                sh "docker compose up"
            }
        }
        stage('Test') {
            steps {
                sh "scrapy crawl posts -o posts.json"
            }
        }
    }
}