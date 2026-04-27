pipeline {
    agent any

    environment {
        DOCKER_HUB = "yashjha113/gym-app"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/yashjha9/gym-devops-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('SonarQube Scan') {
            steps {
                sh 'sonar-scanner'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB:v1 .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'Yashjha113', passwordVariable: 'Yashjha@113')]) {
                    sh 'docker login -u $USER -p $PASS'
                    sh 'docker push $DOCKER_HUB:v1'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
