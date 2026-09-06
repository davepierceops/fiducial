"""RED-GATE STUB for selection. Deliberately wrong.

Wrongness, on purpose:
  * `parse_where` accepts a token with no `=`, an empty key and an empty value;
  * `select` treats a missing key as a match;
  * `select` returns its result reversed, ignoring order / topic / id;
  * the module imports `os` and `pathlib`, imports `FileRowSource` from the
    storage module, and names `rules/` — three AC-RS-4 boundary violations, so
    `test_rulestore_boundary.py` reds on an assertion rather than on nothing.
"""

from __future__ import annotations

import os  # AC-RS-4 violation, on purpose
import pathlib  # AC-RS-4 violation, on purpose

from rulestore.store import FileRowSource, Row, RowSource  # noqa: F401

#: AC-RS-4 violation, on purpose: a processing module naming a storage path.
STORE_DIR = "rules/"


class QueryError(Exception):
    """A `--where` token that is not a `k=v` pair with both halves non-empty."""


def parse_where(args):
    """STUB: never raises; a token with no `=` becomes a key with no value."""
    where = {}
    for token in args:
        key, _, value = token.partition("=")
        where[key.strip()] = value.strip()
    return where


def sort_key(row):
    """STUB: the contract's order/topic/id key, never applied by `select`."""
    order = row.order if row.order is not None else 10**9
    topic = (row.keys.get("topic") or [""])[0]
    return (order, topic, row.id)


def select(rows, where):
    """STUB: a missing key matches, and the result comes back reversed."""
    hits = []
    for row in rows:
        matched = True
        for key, value in where.items():
            values = row.keys.get(key)
            if values is not None and value not in values:
                matched = False
        if matched:
            hits.append(row)
    return list(reversed(hits))


def _unused(root):
    """Never called. Present only so `os`/`pathlib` are genuinely imported."""
    return os.path.join(str(pathlib.Path(root)), STORE_DIR)
