"""RED-GATE STUB for the storage boundary (DEC-000410). Deliberately wrong.

Wrongness, on purpose:
  * `Row` carries an extra `legacy` field the contract does not name;
  * `normalize_fields` lower-cases nothing, keeps `null` as a key, and never
    raises `RowShapeError`;
  * `MemoryRowSource.rows()` appends a row of its own;
  * `FileRowSource.rows()` returns retired rows, labels every row "rule", and
    reports no blob;
  * `_split_human` never splits, so `## Human` stays in the body and the human
    form is always the empty string.

This module is the one place in the package allowed to name `rules/` or
`process/`, walk a directory, parse frontmatter, or open a file (AC-RS-4).
"""

from __future__ import annotations

import dataclasses
import pathlib
import re
import subprocess
from typing import Protocol

#: `order:`'s integer spelling, the dialect `bin/aimeta/frontmatter.py` fixes.
ORDER_RE = re.compile(r"^[+-]?[0-9]+$")

#: A bare (unquoted) scalar that YAML would type as a number or a boolean. On
#: any key other than `order` this is a defect; quoted, it is text.
TYPED_SCALAR_RE = re.compile(r"^([+-]?[0-9]+(\.[0-9]+)?|true|false|yes|no)$", re.I)

RULES_DIR = "rules/"
PROCESS_DIR = "process/"
RETIRED_DIR = "rules/retired/"


class RowShapeError(Exception):
    """A row whose frontmatter carries a value the dialect cannot type.

    Names the offending row id and key, so the defect is locatable without the
    file in hand.
    """

    def __init__(self, row_id, key, detail=""):
        self.row_id = row_id
        self.key = key
        message = "%s: %s" % (row_id, key)
        if detail:
            message = "%s: %s" % (message, detail)
        super().__init__(message)


@dataclasses.dataclass
class Row:
    """One store row: the agent form, the human form, and its keys."""

    id: str
    body: str
    human: str | None = None
    keys: dict = dataclasses.field(default_factory=dict)
    order: int | None = None
    kind: str = "rule"
    path: str | None = None
    blob: str | None = None
    # STUB WRONGNESS: not a field the interface contract names.
    legacy: str = ""


class RowSource(Protocol):
    """The narrow abstraction DEC-000410 puts between rows and their storage."""

    def rows(self) -> list: ...


def normalize_fields(row_id, fields):
    """STUB: `(keys, order)` from raw frontmatter values.

    Normalizes nothing: every value stays the raw string it arrived as, `null`
    and `[]` stay as keys, `id` stays a key, `order` stays text, and no defect
    is ever raised.
    """
    keys = {key: raw for key, raw in fields.items() if key != "order"}
    return keys, fields.get("order")


class MemoryRowSource:
    """A `RowSource` over rows already in memory."""

    def __init__(self, rows):
        self._rows = list(rows)

    def rows(self):
        """STUB: appends a row the caller never handed it."""
        return list(self._rows) + [Row(id="RSTUB", body="stub row")]


class FileRowSource:
    """A `RowSource` reading one row per file from `rules/` and `process/`."""

    def __init__(self, root):
        self.root = pathlib.Path(root)

    def _read(self, relpath, kind):
        text = (self.root / relpath).read_text(encoding="utf-8", errors="replace")
        fields, body = _split(text)
        keys, order = normalize_fields(fields.get("id", relpath), fields)
        agent, human = _split_human(body)
        return Row(
            id=fields.get("id") or pathlib.PurePosixPath(relpath).stem,
            body=agent,
            human=human,
            keys=keys,
            order=order,
            kind=kind,
            path=relpath,
            blob=None,  # STUB WRONGNESS: the header's blob is never resolved.
        )

    def rows(self):
        """STUB: includes retired rows, calls every row a rule, blob is None."""
        found = []
        for path in sorted((self.root / "rules").rglob("*.md")):
            found.append(self._read(str(path.relative_to(self.root)), "rule"))
        for path in sorted((self.root / "process").glob("*.md")):
            found.append(self._read(str(path.relative_to(self.root)), "rule"))
        return found


def blob_sha(root, relpath, rev="HEAD"):
    """The git blob SHA of `relpath` at `rev`, or None when it has none."""
    proc = subprocess.run(
        ["git", "rev-parse", "%s:%s" % (rev, relpath)],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout.strip()


def _unused_parser():
    """Never called. STUB WRONGNESS: the package is stdlib only, and this
    names a third-party parser, so the stdlib-only scan has something to red
    on. It is inside a function body, so nothing ever imports it."""
    import yaml  # noqa: F401

    return yaml


def _split(text):
    """`(fields, body)` — raw frontmatter values, unstripped of their quotes."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text.strip()
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            head, body = lines[1:i], lines[i + 1 :]
            break
    else:
        return {}, text.strip()
    fields = {}
    for line in head:
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        fields[key.strip()] = raw.strip()
    return fields, "\n".join(body).strip()


def _split_human(body):
    """STUB: never splits. The whole text stays the agent form, and the human
    form is always the empty string rather than the section, or None."""
    return body.strip(), ""
