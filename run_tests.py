#!/usr/bin/env python3
"""Convenience launcher for local tests."""
import sys
try:
    import pytest
except Exception:
    print("pytest is required. Try: pip install -r requirements.txt", file=sys.stderr)
    raise SystemExit(1)
raise SystemExit(pytest.main(["-q", "--maxfail=1"]))
