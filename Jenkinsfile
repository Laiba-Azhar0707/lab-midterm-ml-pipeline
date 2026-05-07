pipeline {
    agent any
    
    stages {
        stage('Pull from GitHub') {
            steps {
                sh 'cd /home/ubuntu/lab-midterm-ml-pipeline && git fetch origin main && git reset --hard origin/main'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -q -r /home/ubuntu/lab-midterm-ml-pipeline/requirements.txt --break-system-packages'
            }
        }
        stage('Train Model') {
            steps {
                sh 'cd /home/ubuntu/lab-midterm-ml-pipeline && python3 train.py'
            }
        }
        stage('Build Docker') {
            steps {
                sh 'cd /home/ubuntu/lab-midterm-ml-pipeline && docker build -t ml-pipeline-api:latest .'
            }
        }
        stage('Deploy') {
            steps {
               sh 'docker stop ml-api 2>/dev/null || true && docker rm ml-api 2>/dev/null || true && docker run -d -p 8000:8000 --restart unless-stopped --name ml-api ml-pipeline-api:latest && sleep 5 && curl http://localhost:8000/metrics'
            }
        }
    }
}
