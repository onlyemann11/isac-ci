import pytest
from isac_app.config import AppConfig
from isac_app.core import IsacEngine
from isac_app.matlab_runner import MatlabSession, MatlabNotAvailable

pytestmark = pytest.mark.matlab

def test_end_to_end_with_matlab_if_available():
    cfg = AppConfig(threshold=0.9, matlab_script="run_pipeline")
    try:
        m = MatlabSession(start=True)
    except MatlabNotAvailable:
        pytest.skip("MATLAB Engine not installed; skipping integration test.")
    eng = IsacEngine(cfg, matlab=m)
    y = eng.compute(2.0)
    out = eng.run_matlab_step(y)
    assert out is not None
    m.close()
