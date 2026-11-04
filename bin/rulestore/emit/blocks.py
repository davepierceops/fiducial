"""The fenced block an `enforce:` row carries (SPEC.md §7; the plan, §1b).

A block is the last fenced ```yaml``` code block of a row's body, in the
small dialect the rows use and nothing wider:

    key: value              a scalar
    key: [a, b]             a list, on one line
    key:                    a list, one `- item` per following line
      - item
    # a comment             ignored, wherever it stands

`parse(body)` returns `(fields, prose)`: `fields` is `{key: value}` with a
list where the row wrote one and a string otherwise; `prose` is the body with
the block removed and surrounding blank lines trimmed — the principle the
mechanism enforces, or `""` for a block-only row. A row with `enforce:` and
no block is a defect the emitter refuses (SPEC.md §7).
"""

from __future__ import annotations

import re

_FENCE_OPEN_RE = re.compile(r"^(`{3,}|~{3,})\s*(\w+)?\s*$")
_ITEM_RE = re.compile(r"^\s+-\s+(.*)$")


def _strip_comment(line):
    """The line before an unquoted `#` that starts a comment."""
    out = []
    quote = None
    for index, char in enumerate(line):
        if quote:
            out.append(char)
            if char == quote:
                quote = None
        elif char in ("'", '"'):
            quote = char
            out.append(char)
        elif char == "#" and (index == 0 or line[index - 1].isspace()):
            break
        else:
            out.append(char)
    return "".join(out).rstrip()


def _scalar(text):
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ("'", '"'):
        return text[1:-1]
    return text


def _list(inner):
    return [_scalar(part) for part in inner.split(",") if part.strip()]


def split_block(body):
    """`(block_lines, prose)` for the last fenced block, or `(None, body)`."""
    lines = body.split("\n")
    opens = [i for i, line in enumerate(lines) if _FENCE_OPEN_RE.match(line.strip())]
    # fences come in pairs; the last pair is the block
    if len(opens) < 2:
        return None, body.strip()
    close = opens[-1]
    start = opens[-2]
    prose = "\n".join(lines[:start] + lines[close + 1:]).strip()
    return lines[start + 1:close], prose


def parse_lines(block_lines):
    fields = {}
    current_list = None
    for raw in block_lines:
        line = _strip_comment(raw)
        if not line.strip():
            continue
        item = _ITEM_RE.match(line)
        if item and current_list is not None:
            fields[current_list].append(_scalar(item.group(1)))
            continue
        if ":" not in line:
            raise ValueError("not a key: value line: %r" % raw)
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if not value:
            fields[key] = []
            current_list = key
            continue
        current_list = None
        if value.startswith("[") and value.endswith("]"):
            fields[key] = _list(value[1:-1])
        else:
            fields[key] = _scalar(value)
    return fields


def parse(body):
    """`(fields, prose)`; `fields` is `None` when the body has no block."""
    block_lines, prose = split_block(body or "")
    if block_lines is None:
        return None, prose
    return parse_lines(block_lines), prose


def as_list(value):
    """A block value as a list: a scalar becomes a one-item list."""
    if value is None:
        return []
    if isinstance(value, list):
        return list(value)
    return [value]
