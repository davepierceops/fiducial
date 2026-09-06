"""RED-GATE STUB for the rendered bundle (AC-RS-6/14/15). Deliberately wrong.

Wrongness, on purpose:
  * every row's `## Human` section is rendered, which G4 forbids outright;
  * definitions are rendered first, not last, and without their `**term** — `
    lead;
  * the header omits `- Rows:` and abbreviates HEAD to seven characters;
  * a process document is rendered under its id, not its path;
  * imports `os` and names `rules/` — AC-RS-4 boundary violations, on purpose.
"""

from __future__ import annotations

import os  # AC-RS-4 violation, on purpose

from rulestore.store import Row, RowSource  # noqa: F401

#: AC-RS-4 violation, on purpose: a processing module naming a storage path.
STORE_DIR = "rules/"

TITLE = "# fiducial-bundle"


def render(rows, definitions, *, repo, head, generated):
    """STUB: Human text included, definitions first, header fields missing."""
    lines = [
        TITLE,
        "",
        "- Repo: %s" % repo,
        "- HEAD: %s" % head[:7],
        "- Generated: %s" % generated,
        "",
    ]
    for row in list(definitions) + list(rows):
        lines.append("## %s" % row.id)
        lines.append("")
        lines.append(row.body)
        if row.human:
            lines.append("")
            lines.append("## Human")
            lines.append("")
            lines.append(row.human)
        lines.append("")
    return "\n".join(lines) + "\n"


def _unused():
    """Never called. Present only so `os` is genuinely imported."""
    return os.sep + STORE_DIR
