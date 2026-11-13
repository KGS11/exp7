
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python Application'
                bat 'python -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Executing automated unit tests'
                bat 'python -m unittest app'
            }
        }

        stage('Run appliaction') {
            steps {
               bat 'python app.py'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
