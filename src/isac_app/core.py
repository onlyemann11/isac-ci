from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Any
from .config import AppConfig

class MatlabLike(Protocol):
    def run(self, func: str, *args: Any, **kwargs: Any) -> Any: ...

@dataclass
class IsacEngine:
    cfg: AppConfig
    matlab: MatlabLike | None = None

    def compute(self, x: float) -> float:
        return x * self.cfg.threshold

    def run_matlab_step(self, *args: Any, **kwargs: Any) -> Any:
        if self.matlab is None:
            raise RuntimeError("MATLAB session not attached")
        return self.matlab.run(self.cfg.matlab_script, *args, **kwargs)
