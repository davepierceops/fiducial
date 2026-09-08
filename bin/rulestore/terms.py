"""Definition pulling by term (AC-RS-13, DEC-000420).

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`; `is_definition`
amended by `docs/cycles/bundle-tool-followup-20260907T170000Z.md` item 7 (Q4)
to match DEC-000420's wording exactly.
"""

from __future__ import annotations

import re

#: `None` order sorts after every integer, however large (F3: the definitions
#: band's order is pinned here, independent of `query.sort_key`).
_NO_ORDER = float("inf")


def is_definition(row):
    """A definition is a row with a `term` key and none of `role`, `session`,
    or `corpus` (DEC-000420's wording — bundle-tool-quality-20260906T150000Z.md
    Q4)."""
    return bool(row.keys.get("term")) and not any(
        row.keys.get(key) for key in ("role", "session", "corpus")
    )


def _term_pattern(term):
    words = r"\s+".join(re.escape(word) for word in term.split())
    return re.compile(r"(?<!\w)%s(?!\w)" % words, re.IGNORECASE)


def pull_definitions(selected, all_rows):
    """Definitions pulled into `selected`, transitively, sorted by `(order,
    id)`, `None` order last — the definitions band's own key, independent of
    the rows/process bands' sequence-based `sort_key` (F3, DEC-000640)."""
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
    return sorted(
        pulled.values(),
        key=lambda r: (r.order if r.order is not None else _NO_ORDER, r.id),
    )
