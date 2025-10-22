import pytest
from isac_app.matlab_runner import MatlabSession, MatlabNotAvailable

def test_matlab_session_imports_or_raises(monkeypatch):
    with monkeypatch.context() as m:
        m.setitem(__import__("sys").modules, "matlab", None)
        with pytest.raises(MatlabNotAvailable):
            MatlabSession(start=False)
