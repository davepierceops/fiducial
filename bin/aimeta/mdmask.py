"""Which lines of a directive a line-anchored match may consider.

TRD §3.5. One pure text function plus its stripping rule: no git, no
filesystem, and no import from this repository. §3.1 isolates it here because
it is the part of the design most likely to need revision once a corpus of
post-adoption directives exists, and a revision confined to a module that
builds no repository is a revision one file's tests can exercise.

This is a line scanner, not a markdown parser: nothing here builds a document
tree, and the technical non-goals forbid one.
"""

from __future__ import annotations

import re

_FENCE_OPEN = re.compile(r"^(`{3,}|~{3,})")
_LIST_MARKER = re.compile(r"^(?:[-*+]|\d+[.)]) ")
_HEADING_RUN = re.compile(r"^#{1,6} ")
_EMPHASIS_RUN = re.compile(r"^(?:\*\*|__)")

_COMMENT_OPEN = "<!--"
_COMMENT_CLOSE = "-->"


def normalize_endings(text):
    """`\\r\\n` and `\\r` become `\\n`; the match is byte-exact thereafter."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _indent_of(line):
    body = line.lstrip(" ")
    return len(line) - len(body), body


def eligible(text):
    """`(lines, indices)` — the lines, and which of them a match may consider.

    Masked: fenced code blocks and their fence lines (an unclosed fence masks
    to end of file), blockquote lines, and HTML comments from the line opening
    one to the line closing it. Indented code blocks are **not** masked: four
    spaces is how this corpus writes continuation lines inside list items.
    """
    lines = normalize_endings(text).split("\n")
    indices = []
    fence_char = None
    fence_length = 0
    commented = False
    for index, line in enumerate(lines):
        indent, body = _indent_of(line)
        if commented:
            if _COMMENT_CLOSE in line:
                commented = False
            continue
        if fence_char is not None:
            if indent <= 3 and _closes(body, fence_char, fence_length):
                fence_char = None
            continue
        if _COMMENT_OPEN in line:
            if _COMMENT_CLOSE not in line.split(_COMMENT_OPEN, 1)[1]:
                commented = True
            continue
        opening = _FENCE_OPEN.match(body)
        if opening is not None and indent <= 3:
            fence_char = opening.group(1)[0]
            fence_length = len(opening.group(1))
            continue
        if body.startswith(">"):
            continue
        indices.append(index)
    return lines, indices


def _closes(body, char, length):
    """A closing fence: a run of at least the opening length, nothing after it."""
    run = _FENCE_OPEN.match(body)
    if run is None or run.group(1)[0] != char or len(run.group(1)) < length:
        return False
    return body[len(run.group(1)):].strip() == ""


def leading_content(line):
    """What an eligible line leads with, once decoration is stripped.

    Applied once each, in order: up to three leading spaces; one list marker
    and the space after it; an ATX heading run and its space; one leading `**`
    or `__`. The corpus writes labels bare, bulleted, and bolded, and refusing
    the bulleted form would fail authors on a distinction no governed file
    draws.
    """
    text = re.sub(r"^ {0,3}", "", line, count=1)
    text = _LIST_MARKER.sub("", text, count=1)
    text = _HEADING_RUN.sub("", text, count=1)
    text = _EMPHASIS_RUN.sub("", text, count=1)
    return text
