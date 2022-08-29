pipeline {
    agent any

    stages {
        stage('Install') { 
            steps {
                sh "sudo apt update"
                sh "sudo apt install build-essential zlib1g-dev \
                    libncurses5-dev libgdbm-dev libnss3-dev \
                    libssl-dev libreadline-dev libffi-dev curl"
                sh "curl -O https://www.python.org/ftp/python/3.10.6/Python-3.10.6.tar.xz"
                sh "tar -xf Python-3.10.6.tar.xz"
                sh "cd Python-3.10.6 && ./configure && sudo make altinstall || sudo make install"
                sh "python3 --version"
            }
        }
    }
}
