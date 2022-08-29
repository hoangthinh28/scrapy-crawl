pipeline {
    agent {
        docker {
            image "nodejs:18"
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
