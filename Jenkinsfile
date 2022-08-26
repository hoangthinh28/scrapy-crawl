pipeline {
    agent { filename 'Dockerfile' }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh "python crawl.py"
            }
        }
    }
}