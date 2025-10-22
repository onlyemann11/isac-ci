from __future__ import annotations
import argparse
from .config import load_config
from .core import IsacEngine
from .matlab_runner import MatlabSession, MatlabNotAvailable

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser("isac")
    p.add_argument("--config", type=str, default=None, help="path to config.json")
    p.add_argument("--x", type=float, default=1.0, help="input for compute()")
    p.add_argument("--with-matlab", action="store_true", help="attempt MATLAB call")
    args = p.parse_args(argv)

    cfg = load_config(args.config)
    engine = IsacEngine(cfg)

    y = engine.compute(args.x)
    print(f"compute({args.x}) => {y}")

    if args.with_matlab:
        try:
            m = MatlabSession(start=True)
            engine.matlab = m
            out = engine.run_matlab_step(y)
            print(f"MATLAB {cfg.matlab_script}({y}) => {out}")
            m.close()
        except MatlabNotAvailable as e:
            print(str(e))
            return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
