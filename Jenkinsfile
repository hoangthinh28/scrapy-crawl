pipeline {
    agent {
        docker {image 'thinh28042001/mycrawler'}
    } 
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