pipeline {
    agent {
        docker {
            image "thinh28042001/mycrawler:2.0"
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
