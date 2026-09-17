pipeline {
    agent any

    environment {
        APP_NAME = 'Student Management System'
        REPORT_NAME = 'report.txt'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Cloning repository from GitHub..."
                git branch: 'main', url: 'https://github.com/mairalsanika/Jenkins-Project-2.git'
            }
        }

        stage('Initialize Environment') {
            steps {
                echo "=================================================="
                echo "Starting CI/CD Execution for: ${env.APP_NAME}"
                echo "Target Workspace: ${env.WORKSPACE}"
                echo "=================================================="
            }
        }

        stage('Verify Runtime Dependencies') {
            steps {
                echo "Checking Python installation and environment..."
                bat 'python --version'
            }
        }

        stage('Execute Python Application') {
            steps {
                echo "Executing app.py to generate execution metrics..."
                bat 'python app.py'
            }
        }

        stage('Verify Output Artifact') {
            steps {
                script {
                    if (fileExists("${env.REPORT_NAME}")) {
                        echo "SUCCESS: Found generated artifact '${env.REPORT_NAME}'."
                    } else {
                        error "FAILURE: Required artifact '${env.REPORT_NAME}' was not created!"
                    }
                }
            }
        }

        stage('Archive Build Artifacts') {
            steps {
                echo "Archiving '${env.REPORT_NAME}' to Jenkins UI..."
                archiveArtifacts artifacts: "${env.REPORT_NAME}", fingerprint: true, allowEmptyArchive: false
            }
        }
    }

    post {
        always {
            echo "Pipeline execution finished."
        }
        success {
            echo "Build finished successfully. Report has been archived."
        }
        failure {
            echo "Build failed. Check the console output above for detailed errors."
        }
    }
}