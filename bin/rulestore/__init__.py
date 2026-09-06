"""RED-GATE STUB package for the rule-store bundle tool. Deliberately wrong.

`bin/rulestore/` is the package `docs/cycles/bundle-tool-tests-20260906T110000Z.md`
specifies: `store.py` (the storage boundary, DEC-000410), and the processing
modules `query.py`, `terms.py`, `keys.py`, `near.py`, `render.py`.

Every module here has the interface contract's public names with the contract's
signatures, and every one of them returns a **deliberately wrong value**, so
that `bin/tests/test_rulestore*.py` and `bin/tests/test_bundle_cli.py` go red on
an `AssertionError` rather than on an `ImportError` or an `AttributeError`. Each
module's docstring names its wrongness. Nothing here is a head start on the
implementation: no module decides anything the acceptance criteria ask for.

The Coder replaces this package. See `bin/tests/stubs/README.md` for the same
arrangement applied to `bin/directive` and `bin/check-directive`.
"""
