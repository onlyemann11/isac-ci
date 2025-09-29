pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args '-u 0'
    }
  }
  options { ansiColor('xterm'); timestamps() }

  stages {
    stage('Checkout') { steps { checkout scm } }

    stage('Install / Build') {
      steps { sh 'bash ci/scripts/build.sh' }
    }

    stage('Unit Tests') {
      steps { sh 'bash ci/scripts/test.sh' }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/unit-tests.xml'
          archiveArtifacts artifacts: 'reports/coverage.xml, reports/coverage_html/**', onlyIfSuccessful: false
        }
      }
    }

    stage('Integration Tests (non-blocking for now)') {
      steps {
        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
          sh 'bash ci/scripts/integration.sh'
        }
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/integration-tests.xml'
        }
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/**/*.xml', fingerprint: true, onlyIfSuccessful: false
    }
    success  { echo '✅ CI passed' }
    unstable { echo '🟨 CI unstable (integration or quality gates)' }
    failure  { echo '❌ CI failed' }
  }
}
