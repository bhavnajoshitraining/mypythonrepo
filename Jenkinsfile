pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                // Show where Python is (for debugging). This will fail if python is missing.
                bat 'python --version || (echo PYTHON_NOT_FOUND & exit /b 1)'
                bat 'where python || echo "where python returned non-zero"'
            }
        }

        stage('Create venv & Install deps') {
            steps {
                // Create venv in workspace to keep isolation
                bat """
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                if exist requirements.txt (
                  pip install -r requirements.txt
                ) else (
                  pip install pytest
                )
                """
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest and write junit xml
                bat """
                call venv\\Scripts\\activate
                pytest --junitxml=test-report.xml
                """
            }
        }
    }

    post {
        always {
            // allowEmptyResults true avoids failing Jenkins when no xml found on first run
            junit testResults: 'test-report.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'test-report.xml', allowEmptyArchive: true
        }
        success {
            echo 'All stages succeeded.'
        }
        failure {
            echo 'Build failed — check console output and test results.'
        }
    }
}
