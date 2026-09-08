"""Named queries and their render sequence (DEC-000640, DEC-000650).

Pure over text: nothing here reads a file or names a storage path. A method
of the storage layer's file-backed row source is the one caller that reads
the document this module parses; this module works over whatever text it is
given, and a missing heading or block is an empty result, not an error.

Contract: `docs/cycles/bundle-tool-followup-20260907T170000Z.md`, item 3.
"""

from __future__ import annotations

import re

_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
_FENCE_RE = re.compile(r"^(`{3,}|~{3,})")


def _section(text, heading):
    """Lines between the `## <heading>` line and the next `## ` line, if any."""
    found = []
    in_section = False
    for line in text.splitlines():
        match = _HEADING_RE.match(line)
        if match:
            if in_section:
                break
            in_section = match.group(1).strip() == heading
            continue
        if in_section:
            found.append(line)
    return found


def _fenced_blocks(lines):
    """Every fenced code block's lines, in order, as a list of line-lists."""
    blocks = []
    current = None
    for line in lines:
        if _FENCE_RE.match(line):
            if current is None:
                current = []
            else:
                blocks.append(current)
                current = None
            continue
        if current is not None:
            current.append(line)
    return blocks


def sequences(text):
    """`(topic_positions, process_positions)` from the two `## Sequence` blocks.

    `topic_positions` is a list of lists of names, one inner list per line of
    the first block. `process_positions` is a list of stems, one per line of
    the second block.
    """
    blocks = _fenced_blocks(_section(text, "Sequence"))
    topic_block = blocks[0] if len(blocks) >= 1 else []
    process_block = blocks[1] if len(blocks) >= 2 else []
    topic_positions = [line.split() for line in topic_block if line.strip()]
    process_positions = [line.strip() for line in process_block if line.strip()]
    return topic_positions, process_positions


def bundles(text):
    """`[(name, query_tokens), ...]` from the `## The list` block.

    One entry per non-blank line: the first field is the name, the remaining
    fields are `k=v` query tokens.
    """
    blocks = _fenced_blocks(_section(text, "The list"))
    if not blocks:
        return []
    entries = []
    for line in blocks[0]:
        fields = line.split()
        if not fields:
            continue
        entries.append((fields[0], fields[1:]))
    return entries
