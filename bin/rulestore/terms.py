"""Definition pulling by term (AC-RS-13, DEC-000420).

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
"""

from __future__ import annotations

import re

from rulestore.query import sort_key


def is_definition(row):
    """A definition is a row with a `term` key and no `role` key."""
    return bool(row.keys.get("term")) and not row.keys.get("role")


def _term_pattern(term):
    return re.compile(r"(?<!\w)%s(?!\w)" % re.escape(term), re.IGNORECASE)


def pull_definitions(selected, all_rows):
    """Definitions pulled into `selected`, transitively, in `select`'s order."""
    definitions = [row for row in all_rows if is_definition(row)]
    already = {row.id for row in selected}
    pulled = {}
    frontier = list(selected)
    while frontier:
        next_frontier = []
        for row in frontier:
            haystack = row.body or ""
            for definition in definitions:
                if definition.id in already or definition.id in pulled:
                    continue
                for term in definition.keys.get("term") or []:
                    if _term_pattern(term).search(haystack):
                        pulled[definition.id] = definition
                        next_frontier.append(definition)
                        break
        frontier = next_frontier
    return sorted(pulled.values(), key=sort_key)
