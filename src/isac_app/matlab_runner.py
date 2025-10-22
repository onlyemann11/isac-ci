from __future__ import annotations
from typing import Any

class MatlabNotAvailable(ImportError):
    pass

class MatlabSession:
    def __init__(self, start: bool = True):
        try:
            import matlab.engine  # type: ignore
        except Exception as e:
            raise MatlabNotAvailable(
                "MATLAB Engine for Python not available. Install it from your MATLAB distribution."
            ) from e
        self._eng = None
        self._eng_mod = matlab.engine
        if start:
            self._eng = self._eng_mod.start_matlab()

    def run(self, func_name: str, *args: Any, **kwargs: Any) -> Any:
        if self._eng is None:
            self._eng = self._eng_mod.start_matlab()
        func = getattr(self._eng, func_name)
        return func(*args, nargout=kwargs.pop("nargout", 1), **kwargs)

    def close(self) -> None:
        if self._eng is not None:
            self._eng.quit()
            self._eng = None
