import subprocess
import sys
import pathlib
import re
import pytest

@pytest.mark.integration
def test_cli_repeats_and_logs():
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    cmd = [sys.executable, str(repo_root / "TestingPy.py"), "Alice", "--repeat", "3"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    output = (result.stdout or "") + (result.stderr or "")
    lines = [ln for ln in output.strip().splitlines() if ln]
    assert len(lines) >= 3
    assert re.search(r"INFO: \(\d\) Hello, Alice!", lines[0])
