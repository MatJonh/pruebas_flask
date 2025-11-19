pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}/flask_app/Scripts/activate"
        DOCKER_IMAGE = "flask-ci-tasks"
        APP_PORT = "5000"
        // Configura tu correo o token de Slack/Teams según prefieras
        EMAIL = "mateo51804084@gmail.com"
    }

    triggers {
        // Dispara automáticamente con el webhook de GitHub
        githubPush()
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo "Activando entorno virtual y instalando dependencias..."
                sh """
                . ${VENV_PATH} && pip install --upgrade pip
                . ${VENV_PATH} && pip install -r requirements.txt
                """
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                echo "Ejecutando pruebas unitarias con pytest..."
                sh ". ${VENV_PATH} && pytest -v"
            }
        }

        stage('Construir Docker') {
            steps {
                echo "Construyendo imagen Docker..."
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Desplegar Docker') {
            steps {
                echo "Deteniendo contenedor previo (si existe) y desplegando..."
                sh """
                docker stop ${DOCKER_IMAGE} || true
                docker rm ${DOCKER_IMAGE} || true
                docker run -d -p ${APP_PORT}:5000 --name ${DOCKER_IMAGE} ${DOCKER_IMAGE}
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline completado correctamente ✅"
            mail to: "${EMAIL}",
                 subject: "Pipeline Exitoso: ${JOB_NAME} #${BUILD_NUMBER}",
                 body: "El pipeline se completó correctamente.\nRevisa Jenkins para más detalles."
        }
        failure {
            echo "Hubo errores durante la ejecución ❌"
            mail to: "${EMAIL}",
                 subject: "Pipeline Fallido: ${JOB_NAME} #${BUILD_NUMBER}",
                 body: "El pipeline ha fallado.\nRevisa Jenkins para más detalles."
        }
    }
}
