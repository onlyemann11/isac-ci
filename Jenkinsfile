pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      // run as root so pip can install; add your own hardening as needed
      args '-u 0'
    }
  }

  options {
    timestamps()
    ansiColor('xterm')
    disableConcurrentBuilds()
  }

  environment {
    // simple, workspace-local pip cache to speed up repeated builds
    PIP_CACHE_DIR = "${WORKSPACE}/.pip-cache"
    REPORTS_DIR   = "${WORKSPACE}/reports"
  }

  stages {
    stage('Prepare workspace') {
      steps {
        sh '''
          set -euxo pipefail
          mkdir -p "$REPORTS_DIR" "$PIP_CACHE_DIR" "$REPORTS_DIR/coverage_html"
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install --cache-dir "$PIP_CACHE_DIR" -r requirements.txt; fi
          pip install --cache-dir "$PIP_CACHE_DIR" pytest pytest-cov
        '''
      }
    }

    stage('Run unit tests') {
      steps {
        sh '''
          set -euxo pipefail
          pytest -q \
            --junitxml="$REPORTS_DIR/unit-tests.xml" \
            --cov=. --cov-report=xml:"$REPORTS_DIR/coverage.xml" \
            --cov-report=html:"$REPORTS_DIR/coverage_html"
        '''
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/unit-tests.xml'
          // archive even on failure so you can inspect results
          archiveArtifacts artifacts: 'reports/**/*', fingerprint: true, onlyIfSuccessful: false
        }
      }
    }

    stage('Integration tests') {
      when { expression { return fileExists('integration_test.sh') } }
      steps {
        // If integration tests fail, mark build UNSTABLE (not SUCCESS),
        // so you still keep artifacts and see the signal.
        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
          sh '''
            set -euxo pipefail
            chmod +x ./integration_test.sh
            ./integration_test.sh
          '''
        }
      }
      post {
        always {
          // Use a distinct report name if your script outputs JUnit XML
          // Adjust the path if your script writes elsewhere.
          junit allowEmptyResults: true, testResults: 'reports/junit.xml'
          archiveArtifacts artifacts: 'reports/**/*', fingerprint: true, onlyIfSuccessful: false
        }
      }
    }
  }

  post {
    always {
      // final sweep (in case a stage returned early)
      junit allowEmptyResults: true, testResults: 'reports/**/*.xml'
      archiveArtifacts artifacts: 'reports/**/*', fingerprint: true, onlyIfSuccessful: false
    }
  }
}
