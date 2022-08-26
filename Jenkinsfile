pipeline {
    
    agent any

    stages {
        stage('Build') {
            steps {
                sh "python --version"
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