"""The rendered bundle document (AC-RS-6, AC-RS-14, AC-RS-15).

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
"""

from __future__ import annotations

TITLE = "# fiducial-bundle"


def _heading(row):
    return row.path if row.kind == "process" else row.id


def _manifest_line(row):
    return "  - %s (%s)" % (_heading(row), row.blob)


def render(rows, definitions, *, repo, head, generated):
    """The header, the selected rows in order, and the definitions last.

    No `## Human` content anywhere: only `row.body` is ever emitted.
    """
    rows = list(rows)
    definitions = list(definitions)

    lines = [
        TITLE,
        "- Repo: %s" % repo,
        "- HEAD: %s" % head,
        "- Generated: %s" % generated,
        "- Rows:",
    ]
    lines.extend(_manifest_line(row) for row in rows)
    if definitions:
        lines.append("- Definitions:")
        lines.extend(_manifest_line(row) for row in definitions)

    body = []
    for row in rows:
        body.append("## %s" % _heading(row))
        body.append("")
        body.append(row.body)
        body.append("")
    if definitions:
        body.append("## Definitions")
        body.append("")
        for definition in definitions:
            terms = definition.keys.get("term") or []
            first_term = terms[0] if terms else definition.id
            body.append("**%s** — %s" % (first_term, definition.body))
            body.append("")

    text = "\n".join(lines) + "\n" + "\n".join(body)
    return text.rstrip("\n") + "\n"
