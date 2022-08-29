pipeline {
    agent {
        docker {
            image "node:16.3.0-alpine"
        }
    }

    stages {
        stage('Build') { 
            steps {
                sh """
                    npm --version
                """
            }
        }
    }
}
