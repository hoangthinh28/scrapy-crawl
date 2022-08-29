pipeline {
    agent any

    stages {
        stage('install') { 
            steps {
                sh "sudo apt install python3"
                sh "python --version"
            }
        }
    }
}
