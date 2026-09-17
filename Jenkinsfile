pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT', 
            choices: ['dev', 'staging', 'prod'], 
            description: 'Select the deployment environment'
        )
    }

    stages {
        stage('Show Parameter') {
            steps {
                echo "Selected environment: ${params.ENVIRONMENT}"
            }
        }
        stage('Build for Environment') {
            steps {
                echo "Building the application for the ${params.ENVIRONMENT} environment..."
            }
        }
    }
}