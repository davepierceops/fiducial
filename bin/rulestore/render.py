"""The rendered bundle document (DEC-000630, DEC-000640).

Contract: `docs/cycles/bundle-tool-followup-20260907T170000Z.md`, item 5 —
overrides `docs/cycles/bundle-tool-tests-20260906T110000Z.md`'s header and
body form (the ordering contract, AC-RS-14 and AC-RS-15, stand).
"""

from __future__ import annotations

from rulestore.emit import blocks


def _heading(row):
    """A row's label: its path for a process document, its id for a rule.

    Kept for `--near`'s printed label (item 7, Q6); `render` no longer
    heads a row with it.
    """
    return row.path if row.kind == "process" else row.id


def row_text(row):
    """What a bundle prints for a row: its body — except an `enforce:` row,
    whose fenced block is the harness's mechanism (a hook's yaml, deny
    patterns, a field name), not text a reader acts on. Such a row prints its
    prose, the principle the mechanism enforces; a block-only row prints
    nothing. A bundle carries no `## Human` content, for any row (#399).
    """
    if (row.keys or {}).get("enforce"):
        block, prose = blocks.split_block(row.body or "")
        if block is not None:
            return prose
    return row.body


def render(rows, definitions, *, repo, head, generated):
    """One header line, the selected rows as body text, then definitions.

    `## Human` content never reaches the output; only `row_text` is emitted.
    """
    rows = list(rows)
    definitions = list(definitions)

    lines = ["<!-- fiducial %s @ %s %s -->" % (repo, head, generated), ""]

    for row in rows:
        text = row_text(row)
        if not text:
            continue
        lines.append(text)
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
