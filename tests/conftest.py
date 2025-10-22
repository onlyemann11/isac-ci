import pytest
from isac_app.config import AppConfig

class FakeMatlab:
    def __init__(self):
        self.calls = []
    def run(self, func, *args, **kwargs):
        self.calls.append((func, args, kwargs))
        return args[0] if args else None

@pytest.fixture
def cfg():
    return AppConfig(threshold=0.5, matlab_script="run_pipeline", workdir=".")

@pytest.fixture
def fake_matlab():
    return FakeMatlab()
