pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                sh """
                    ls
                    python crawl.py
                """
            }
        }
    }
}
