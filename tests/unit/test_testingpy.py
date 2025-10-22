import logging
import pytest
from TestingPy import generate_messages, run

def test_generate_messages_basic():
    assert generate_messages("Alice", 3) == ["Hello, Alice!"] * 3

def test_generate_messages_invalid_repeat():
    with pytest.raises(ValueError):
        generate_messages("Bob", 0)

def test_run_logs_messages(caplog):
    caplog.set_level(logging.INFO)
    logger = logging.getLogger("ArcSynerCom.test")
    run("Alice", 2, logger=logger)
    msgs = [rec.getMessage() for rec in caplog.records if rec.name == "ArcSynerCom.test"]
    assert "(1) Hello, Alice!" in msgs[0]
    assert "(2) Hello, Alice!" in msgs[1]
