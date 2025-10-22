"""isac_app — expandable core with MATLAB seam."""

from .config import AppConfig, load_config
from .core import IsacEngine
from .matlab_runner import MatlabSession, MatlabNotAvailable

__all__ = ["AppConfig", "load_config", "IsacEngine", "MatlabSession", "MatlabNotAvailable"]
__version__ = "0.1.0"
