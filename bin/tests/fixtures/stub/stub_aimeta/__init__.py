"""Relocation package for the throwaway `bin/land` stub's two submodules.

Not stub content — see `land.py` and `report.py` in this package, and
`repo.py`, for the actual throwaway logic and the relocation shim
respectively. This file exists only so `land.py`'s `from . import report,
repo` continues to resolve after the move out of `bin/aimeta/`.
"""
