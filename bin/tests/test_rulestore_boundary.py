"""AC-RS-4: the storage boundary (DEC-000410), as a static check on the source.

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT" and AC-RS-4, landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
DEC-000410 (`decisions/log.md @ a00deba150c0736f77562ec80d858c3986cd7f11`):
"filesystem traversal, filename conventions, frontmatter parsing, and file I/O
stay inside the storage layer".

The boundary is only real if it is checkable without running anything, so this
module reads the package's own source and asserts on it. `bin/tests/
test_rulestore.py` carries the other half of AC-RS-4 — every processing test
there builds its rows in memory and touches no file.

`store.py` is the storage layer. `query.py`, `terms.py`, `keys.py`, `near.py`
and `render.py` are the processing modules; `__init__.py` is the package
docstring and nothing else, and is held to the processing modules' rules.
"""

from __future__ import annotations

import ast
import pathlib
import unittest

from tests.helpers import BIN_DIR

PACKAGE_DIR = BIN_DIR / "rulestore"

#: The modules AC-RS-4 names as processing modules, plus the package marker.
PROCESSING_MODULES = ("query.py", "terms.py", "keys.py", "near.py", "render.py",
                      "__init__.py")
STORAGE_MODULE = "store.py"

#: Imports that can only serve filesystem traversal or subprocess work.
FORBIDDEN_IMPORTS = {"os", "pathlib", "glob", "io", "subprocess"}

#: The two storage paths only `store.py` may name.
STORAGE_PATHS = ("rules/", "process/")

#: The only two names a processing module may take from the storage module.
ALLOWED_STORE_NAMES = {"Row", "RowSource"}


def source_of(name):
    return (PACKAGE_DIR / name).read_text(encoding="utf-8")


def top_level_imports(name):
    """Every top-level module name `name` imports, `import x` and `from x`."""
    tree = ast.parse(source_of(name), filename=name)
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                found.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                found.add(node.module.split(".")[0])
    return found


def names_imported_from_store(name):
    """Every name `name` imports out of the storage module, either spelling."""
    tree = ast.parse(source_of(name), filename=name)
    found = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom):
            continue
        module = node.module or ""
        is_store = (
            (node.level == 0 and module in ("rulestore.store", "store"))
            or (node.level > 0 and module == "store")
        )
        if is_store:
            found.update(alias.name for alias in node.names)
    return found


class TestStorageBoundary(unittest.TestCase):
    """AC-RS-4: only `store.py` knows the rows came from files."""

    def test_ac_rs_4_the_package_holds_exactly_the_contracted_modules(self):
        """AC-RS-4: the check is meaningful only over the whole package."""
        present = sorted(p.name for p in PACKAGE_DIR.glob("*.py"))
        self.assertEqual(present, sorted((STORAGE_MODULE,) + PROCESSING_MODULES))

    def test_ac_rs_4_no_processing_module_imports_a_filesystem_module(self):
        """AC-RS-4: os, pathlib, glob, io and subprocess belong to the storage layer."""
        offenders = []
        for name in PROCESSING_MODULES:
            for imported in sorted(top_level_imports(name) & FORBIDDEN_IMPORTS):
                offenders.append("%s imports %s" % (name, imported))
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_ac_rs_4_no_processing_module_names_a_storage_path(self):
        """AC-RS-4: only `store.py` names `rules/` or `process/`."""
        offenders = []
        for name in PROCESSING_MODULES:
            text = source_of(name)
            for needle in STORAGE_PATHS:
                if needle in text:
                    offenders.append("%s contains %r" % (name, needle))
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_ac_rs_4_store_is_the_only_module_that_names_a_storage_path(self):
        """AC-RS-4: the boundary has a storage side, and it is `store.py` alone."""
        naming = sorted(
            p.name
            for p in PACKAGE_DIR.glob("*.py")
            if any(needle in p.read_text(encoding="utf-8") for needle in STORAGE_PATHS)
        )
        self.assertEqual(naming, [STORAGE_MODULE])

    def test_ac_rs_4_store_is_the_only_module_that_reaches_the_filesystem(self):
        """AC-RS-4: `store.py` is where directory reads and file opens live."""
        reaching = sorted(
            p.name
            for p in PACKAGE_DIR.glob("*.py")
            if top_level_imports(p.name) & FORBIDDEN_IMPORTS
        )
        self.assertEqual(reaching, [STORAGE_MODULE])

    def test_ac_rs_4_processing_modules_take_only_row_and_rowsource_from_store(self):
        """AC-RS-4: "import nothing from store.py but the Row type and RowSource"."""
        offenders = []
        for name in PROCESSING_MODULES:
            extra = names_imported_from_store(name) - ALLOWED_STORE_NAMES
            for taken in sorted(extra):
                offenders.append("%s imports %s from store" % (name, taken))
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_ac_rs_4_no_processing_module_opens_a_file(self):
        """AC-RS-4: file I/O stays inside the storage layer, however it is spelled."""
        offenders = []
        for name in PROCESSING_MODULES:
            tree = ast.parse(source_of(name), filename=name)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    func = node.func
                    called = getattr(func, "id", None) or getattr(func, "attr", None)
                    if called in ("open", "read_text", "read_bytes", "rglob", "glob",
                                  "iterdir", "walk", "listdir"):
                        offenders.append("%s calls %s()" % (name, called))
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_ac_rs_4_every_module_parses_and_is_stdlib_only(self):
        """AC-RS-4: the scan means nothing unless every module actually parses."""
        import sys

        allowed = set(sys.stdlib_module_names) | {"rulestore"}
        offenders = []
        for path in sorted(PACKAGE_DIR.glob("*.py")):
            for imported in sorted(top_level_imports(path.name)):
                if imported not in allowed:
                    offenders.append("%s imports %s" % (path.name, imported))
        self.assertEqual(offenders, [], "\n".join(offenders))


if __name__ == "__main__":
    unittest.main()
