"""Relocation shim, not stub content.

`land.py`'s `from . import report, repo` expects a sibling `repo` module.
`repo.py` is real production code shared with the other `bin/` tools and
stays at `bin/aimeta/repo.py` — it is not part of the throwaway stub and must
not be duplicated. This module re-exports it unchanged; the relocated `land`
executable puts the real `bin/` directory on `sys.path` before this import
runs, so `aimeta.repo` here is the exact same module object the rest of the
tooling uses.
"""

from aimeta.repo import *  # noqa: F401,F403
from aimeta.repo import run  # noqa: F401
