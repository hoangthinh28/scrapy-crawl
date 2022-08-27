pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'pip install -r requirements.txt' 
            }
        }
        stage('Test') { 
            steps {
                sh 'python crawl.py' 
            }
        }

        stage('Deploy-To-Staging') { 
            steps {
                sh 'echo "Deploying to staging "'
            }
        }

    }
}
