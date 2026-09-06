"""The rule-store package behind `bin/bundle`.

`store.py` is the storage boundary (DEC-000410): the one module allowed to
name `rules/` or `process/`, walk a directory, parse frontmatter, or open a
file. `query.py`, `terms.py`, `keys.py`, `near.py` and `render.py` are the
processing modules, working over `Row` objects handed to them in memory.

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
"""
