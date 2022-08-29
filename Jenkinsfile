pipeline {
    agent any

    stages {
        stage('Build') { 
            steps {
                sh """
                    cd crawldata
                    python crawl.py
                """
            }
        }
    }
}
