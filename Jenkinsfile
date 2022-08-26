pipeline {
    agent {
        docker { dockerfile true }
    } 

    stages {
        stage('Build') { 
            steps {
                sh "python --version"
            }
        }
    }
}