from isac_app.config import load_config, AppConfig

def test_defaults():
    cfg = load_config(None, env={})
    assert isinstance(cfg, AppConfig)
    assert 0 < cfg.threshold <= 1.0
