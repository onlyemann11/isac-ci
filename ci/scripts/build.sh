#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip
test -f requirements.txt && pip install -r requirements.txt
