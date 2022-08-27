pipeline {
    agent {
        docker {
            image "python:2-alpine"
        }
    }
    
    options{
        skipStagesAfterUnstable()
    }

    stages {
        stage('Build') { 
            steps {
                sh 'python --version' 
            }
        }
    }
}
