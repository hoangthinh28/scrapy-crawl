pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                sh """
                    python crawl.py
                """
            }
        }
    }
}
