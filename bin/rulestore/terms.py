"""RED-GATE STUB for definition pulling (DEC-000420). Deliberately wrong.

Wrongness, on purpose:
  * matches a term as a bare substring, so `row` pulls on `rowdy`;
  * never scans a pulled definition's body, so nothing is transitive;
  * adds a definition once per matching row, so a definition arrives twice;
  * returns the definitions in discovery order, not the contract's order;
  * imports `os` and names `process/` — AC-RS-4 boundary violations, on purpose.
"""

from __future__ import annotations

import os  # AC-RS-4 violation, on purpose

from rulestore.store import Row, RowSource  # noqa: F401

#: AC-RS-4 violation, on purpose: a processing module naming a storage path.
PROCESS_DIR = "process/"


def is_definition(row):
    """A definition is a row with a `term` key and no `role` key (DEC-000420)."""
    return bool(row.keys.get("term")) and not row.keys.get("role")


def terms_of(row):
    """Every term phrase a definition row declares."""
    return list(row.keys.get("term") or [])


def pull_definitions(selected, all_rows):
    """STUB: substring matching, no transitivity, duplicates admitted."""
    definitions = [row for row in all_rows if is_definition(row)]
    pulled = []
    for row in selected:
        haystack = (row.body or "").lower()
        for definition in definitions:
            if definition in selected:
                continue
            for term in terms_of(definition):
                if term.lower() in haystack:
                    pulled.append(definition)
                    break
    return pulled


def _unused():
    """Never called. Present only so `os` is genuinely imported."""
    return os.sep + PROCESS_DIR
