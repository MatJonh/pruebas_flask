pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub')
        IMAGE_NAME = "mateojuan/flask_api"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: 'https://github.com/MatJonh/pruebas_flask'
                    // url: 'https://github.com/TU_USUARIO/TU_REPO.git'
            }
        }

        stage('Install Python dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -q
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh '''
                echo "$DOCKERHUB_PSW" | docker login -u "$DOCKERHUB_USR" --password-stdin
                '''
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                docker push ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Aquí puedes conectar con Railway, Render o servidor propio"
            }
        }
    }
}
