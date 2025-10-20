from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import os
import json
from typing import Any, Dict

@dataclass(frozen=True)
class AppConfig:
    threshold: float = 0.8
    matlab_script: str = "run_pipeline"
    workdir: str = "."

def _from_env(env: Dict[str, str]) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if "ISAC_THRESHOLD" in env:
        data["threshold"] = float(env["ISAC_THRESHOLD"])
    if "ISAC_MATLAB_SCRIPT" in env:
        data["matlab_script"] = env["ISAC_MATLAB_SCRIPT"]
    if "ISAC_WORKDIR" in env:
        data["workdir"] = env["ISAC_WORKDIR"]
    return data

def load_config(path: str | Path | None = None, env: Dict[str, str] | None = None) -> AppConfig:
    env = os.environ if env is None else env
    base = AppConfig()
    file_data: Dict[str, Any] = {}
    if path:
        p = Path(path)
        if p.exists():
            file_data = json.loads(p.read_text())
    merged = {**base.__dict__, **file_data, **_from_env(env)}
    return AppConfig(**merged)  # type: ignore[arg-type]
