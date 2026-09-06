"""RED-GATE STUB for the computed key census (AC-RS-3). Deliberately wrong.

Wrongness, on purpose:
  * `id` and `order` are counted, which the contract excludes;
  * every value's count is fixed at 1, whatever the store holds;
  * imports `os` and names `rules/` — AC-RS-4 boundary violations, on purpose.
"""

from __future__ import annotations

import os  # AC-RS-4 violation, on purpose

from rulestore.store import Row, RowSource  # noqa: F401

#: AC-RS-4 violation, on purpose: a processing module naming a storage path.
STORE_DIR = "rules/"


def keys_in_use(rows):
    """STUB: counts `id` and `order` too, and every count is 1."""
    census = {}
    for row in rows:
        for key, values in (row.keys or {}).items():
            for value in values:
                census.setdefault(key, {})[value] = 1
        census.setdefault("id", {})[row.id] = 1
        if row.order is not None:
            census.setdefault("order", {})[str(row.order)] = 1
    return census


def _unused():
    """Never called. Present only so `os` is genuinely imported."""
    return os.sep + STORE_DIR
