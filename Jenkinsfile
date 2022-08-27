pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                sh "install python3-pip"
            }
        }

        stage("Test"){
            steps {
                sh "python crawl.py"
            }
        }
    }
}