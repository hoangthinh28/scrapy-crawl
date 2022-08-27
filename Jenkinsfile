pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'pip3 install -r requirements.txt' 
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
