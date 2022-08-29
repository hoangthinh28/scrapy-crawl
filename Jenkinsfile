pipeline {
    agent {
        docker {
            image "thinh28042001/mycrawler:latest"
        }
    }

    stages {
        stage('Build') { 
            steps {
                sh """
                    python --version
                    python crawl.py
                """
            }
        }
    }
}
