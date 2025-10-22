# Ensure the project root (the directory containing TestingPy.py) is importable.
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]  # ~/ArcSynerCom
root_str = str(ROOT)
if root_str not in sys.path:
    sys.path.insert(0, root_str)
