#!/usr/bin/env bash
set -eo pipefail
# bring up any services here (docker compose, etc) before running tests.
pytest -q tests/integration --junitxml=reports/integration-tests.xml
