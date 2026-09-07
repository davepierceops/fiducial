"""The storage boundary (DEC-000410).

This module is the one place in the package allowed to name `rules/` or
`process/`, walk a directory, parse frontmatter, or open a file (AC-RS-4).
Everything else works over `Row` objects handed to it in memory.

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
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
TYPED_SCALAR_RE = re.compile(r"^([+-]?[0-9]+(\.[0-9]+)?|true|false|yes|no)$", re.IGNORECASE)

#: Any ATX heading whose text is "Human", whatever its level (S2,
#: bundle-tool-skeptic-20260906T150000Z.md) — a mis-levelled `### Human` must
#: not publish the rationale it introduces.
HUMAN_MARKER_RE = re.compile(r"^#{1,6}\s+Human\s*$")


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
    """One store row: the agent form, the human form, and its keys.

    `blob` is the git blob at `HEAD`; `body` (and `human`) come from the
    working tree's file (S5, bundle-tool-skeptic-20260906T150000Z.md). The
    two can name different content for any caller that skips the sync check
    `bin/bundle --where` runs before it reads; a bundle's render no longer
    emits `blob` at all (item 5), so nothing downstream sees them disagree.
    """

    id: str
    body: str
    human: str | None = None
    keys: dict = dataclasses.field(default_factory=dict)
    order: int | None = None
    kind: str = "rule"
    path: str | None = None
    blob: str | None = None


class RowSource(Protocol):
    """The narrow abstraction DEC-000410 puts between rows and their storage."""

    def rows(self) -> list: ...


def _strip_quotes(raw):
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ("'", '"'):
        return raw[1:-1]
    return raw


def _split_list_items(inner):
    """Split a bracket list's inner text on commas outside quotes (S4):
    `["a, b", c]`'s comma stays inside its item instead of tearing it in two.
    """
    items = []
    current = []
    quote = None
    for char in inner:
        if quote:
            current.append(char)
            if char == quote:
                quote = None
        elif char in ("'", '"'):
            quote = char
            current.append(char)
        elif char == ",":
            items.append("".join(current))
            current = []
        else:
            current.append(char)
    items.append("".join(current))
    return items


def normalize_fields(row_id, fields):
    """`(keys, order)` from raw frontmatter values.

    Takes the **raw** value text as it stands after `key: `, quotes included:
    whether "a quoted number on another key is text" is only decidable before
    the quotes come off.
    """
    keys = {}
    order = None
    for key, raw in fields.items():
        if key == "id":
            continue
        text = raw.strip() if isinstance(raw, str) else raw
        if key == "order":
            if not isinstance(text, str) or not ORDER_RE.match(text):
                raise RowShapeError(row_id, key, "not an integer: %r" % (raw,))
            order = int(text)
            continue
        if text is None or text == "null":
            continue
        if text.startswith("[") and text.endswith("]"):
            inner = text[1:-1].strip()
            if not inner:
                continue
            values = []
            for part in _split_list_items(inner):
                part = part.strip()
                unquoted_part = _strip_quotes(part)
                if unquoted_part == part and TYPED_SCALAR_RE.match(part):
                    raise RowShapeError(
                        row_id, key, "typed value on a text key: %r" % (raw,)
                    )
                values.append(unquoted_part.strip().lower())
            keys[key] = values
            continue
        unquoted = _strip_quotes(text)
        if unquoted == text and TYPED_SCALAR_RE.match(text):
            raise RowShapeError(row_id, key, "typed value on a text key: %r" % (raw,))
        keys[key] = [unquoted.strip().lower()]
    return keys, order


def _parse_frontmatter(text):
    """`(fields, body)` — raw frontmatter values, unstripped of their quotes."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    close = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            close = index
            break
    if close is None:
        return {}, text
    fields = {}
    for line in lines[1:close]:
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        fields[key.strip()] = raw.strip()
    return fields, "\n".join(lines[close + 1 :])


def _split_human(body):
    """`(agent_form, human_form)` — everything above/below the Human heading."""
    lines = body.split("\n")
    for index, line in enumerate(lines):
        if HUMAN_MARKER_RE.match(line.strip()):
            agent = "\n".join(lines[:index]).strip()
            human = "\n".join(lines[index + 1 :]).strip()
            return agent, (human or None)
    return body.strip(), None


class MemoryRowSource:
    """A `RowSource` over rows already in memory. The identity over its rows."""

    def __init__(self, rows):
        self._rows = list(rows)

    def rows(self):
        return list(self._rows)

    def named_queries_text(self):
        return ""


class FileRowSource:
    """A `RowSource` reading one row per file from `rules/` and `process/`."""

    def __init__(self, root):
        self.root = pathlib.Path(root)

    def named_queries_text(self):
        """`process/named-queries.md`'s text under the root, or `""` if absent."""
        path = self.root / "process" / "named-queries.md"
        if not path.is_file():
            return ""
        return path.read_text(encoding="utf-8", errors="replace")

    def _blob(self, relpath):
        proc = subprocess.run(
            ["git", "rev-parse", "HEAD:%s" % relpath],
            cwd=str(self.root),
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            return None
        return proc.stdout.strip()

    def _row(self, path, kind):
        relpath = path.relative_to(self.root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        fields, body = _parse_frontmatter(text)
        if kind == "rule" and not fields:
            raise RowShapeError(relpath, "frontmatter", "no frontmatter block")
        row_id = fields.get("id") or path.stem
        keys, order = normalize_fields(row_id, fields)
        agent, human = _split_human(body)
        return Row(
            id=row_id,
            body=agent,
            human=human,
            keys=keys,
            order=order,
            kind=kind,
            path=relpath,
            blob=self._blob(relpath),
        )

    def rows(self):
        """Every `rules/*.md` (kind "rule") and `process/*.md` (kind "process").

        `rules/retired/` is a subdirectory; a non-recursive glob over
        `rules/*.md` never descends into it. Raises `RowShapeError` on an id
        shared across the two roots (S4): a duplicate is a defect, not a
        second row.
        """
        found = []
        seen = {}
        rules_dir = self.root / "rules"
        if rules_dir.is_dir():
            for path in sorted(rules_dir.glob("*.md")):
                found.append(self._row(path, "rule"))
        process_dir = self.root / "process"
        if process_dir.is_dir():
            for path in sorted(process_dir.glob("*.md")):
                found.append(self._row(path, "process"))
        for row in found:
            if row.id in seen:
                raise RowShapeError(
                    row.id, "id", "duplicate of %s at %s" % (row.id, seen[row.id])
                )
            seen[row.id] = row.path
        return found
