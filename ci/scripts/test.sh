#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports/coverage_html
pytest -q tests/unit \
  --junitxml=reports/unit-tests.xml \
  --cov=src --cov-report=xml:reports/coverage.xml \
  --cov-report=html:reports/coverage_html
