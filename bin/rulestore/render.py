"""The rendered bundle document (DEC-000630, DEC-000640).

Contract: `docs/cycles/bundle-tool-followup-20260907T170000Z.md`, item 5 —
overrides `docs/cycles/bundle-tool-tests-20260906T110000Z.md`'s header and
body form (the ordering contract, AC-RS-14 and AC-RS-15, stand).
"""

from __future__ import annotations


def _heading(row):
    """A row's label: its path for a process document, its id for a rule.

    Kept for `--near`'s printed label (item 7, Q6); `render` no longer
    heads a row with it.
    """
    return row.path if row.kind == "process" else row.id


def render(rows, definitions, *, repo, head, generated):
    """One header line, the selected rows as body text, then definitions.

    No `## Human` content anywhere: only `row.body` is ever emitted.
    """
    rows = list(rows)
    definitions = list(definitions)

    lines = ["<!-- fiducial %s @ %s %s -->" % (repo, head, generated), ""]

    for row in rows:
        lines.append(row.body)
        lines.append("")
    if definitions:
        lines.append("## Definitions")
        lines.append("")
        for definition in definitions:
            terms = definition.keys.get("term") or []
            first_term = terms[0] if terms else definition.id
            lines.append("**%s** — %s" % (first_term, definition.body))
            lines.append("")

    text = "\n".join(lines)
    return text.rstrip("\n") + "\n"
