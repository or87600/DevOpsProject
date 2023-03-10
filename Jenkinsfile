pipeline {
    agent any
    options {
        buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
    }
    stages {
        // stage # 1 GitHub checkout and set pollSCM - every 30min
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git url: 'https://github.com/or87600/DevOpsProject'
            }
        }
        stage('pip install') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'pip install --ignore-installed pymysql requests selenium flask pypika psutil'
                    } else {
                        sh 'pip install --ignore-installed pymysql requests selenium flask pypika psutil'
                    }
                }
            }
        }
        stage('Run rest_app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python rest_app.py'
                    } else {
                        sh 'nohup python rest_app.py'
                    }
                }
            }
        }
        stage('Run web_app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python web_app.py'
                    } else {
                        sh 'nohup python web_app.py'
                    }
                }
            }
        }
        stage('Run backend_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python backend_testing.py'
                    } else {
                        sh 'python backend_testing.py'
                    }
                }
            }
        }
        stage('Run frontend_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python frontend_testing.py'
                    } else {
                        sh 'python frontend_testing.py'
                    }
                }
            }
        }
        stage('Run combined_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python combined_testing.py'
                    } else {
                        sh 'python combined_testing.py'
                    }
                }
            }
        }
        stage('Run clean_environment') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python clean_environment.py'
                    } else {
                        sh 'python clean_environment.py'
                    }
                }
            }
        }
    }
    post{
        failure {
            emailext to: "or87600@gmail.com",
            subject: "jenkins build:${currentBuild.currentResult}: ${env.JOB_NAME}",
            body: "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nMore Info can be found here: ${env.BUILD_URL}",
            attachLog: true
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}