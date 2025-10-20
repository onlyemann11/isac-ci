from isac_app.core import IsacEngine

def test_compute_uses_threshold(cfg):
    eng = IsacEngine(cfg)
    assert eng.compute(10.0) == 5.0

def test_matlab_call_is_delegated(cfg, fake_matlab):
    eng = IsacEngine(cfg, matlab=fake_matlab)
    out = eng.run_matlab_step(42)
    assert out == 42
    assert fake_matlab.calls[0][0] == "run_pipeline"
