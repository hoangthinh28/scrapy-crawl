pipeline {
    agent any
    stages {
        stage('Build') { 
            agent {
                docker {
                    image "python:3"
                }
            }
            steps {
                sh "pip3 install -r requirements.txt"
            }
        }

        stage("Test"){
            steps {
                sh "python crawl.py"
            }
        }
    }
}