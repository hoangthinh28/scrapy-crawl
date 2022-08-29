pipeline {
    agent {
        docker {
            image "thinh28042001/mycrawler:1.0"
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
