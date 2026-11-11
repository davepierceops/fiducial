"""What every harness target shares (the plan, §3a): the standing selection,
the reading of `enforce:` rows, what a row prints, how a process document
becomes a skill, and which topics a skill absorbs. Nothing here names a
harness, a directory layout or a model. `claude_code.py` is the worked
example of a target built on it; `codex.py` (package 3b) imports from here
rather than copying.
"""

from __future__ import annotations

import re

from rulestore import query, terms

from . import EmitError, blocks

#: The standing selection: the rows every session of the chief of staff
#: loads (`CLAUDE.md`, `AGENTS.md`).
STANDING_QUERY = {"role": "chief-of-staff", "session": "decision"}
BLOCK_HOOK_PREFIX = "bin/hooks/"

#: Process documents that are not skills: `project-setup` (the plan, §3a)
#: and `named-queries`, which is this tool's own input, not a procedure.
NOT_A_SKILL = ("project-setup", "named-queries")
#: Skills the model may not invoke on its own (DEC-001280: the gate).
NO_MODEL_INVOCATION = ("gate",)

_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s")
_HEADING_RE = re.compile(r"^#{1,6}\s+")


def enforce_of(row):
    values = (row.keys or {}).get("enforce") or []
    return values[0] if values else None


class Enforced:
    """One `enforce:` row read: its kind, its block fields, its prose."""

    def __init__(self, row):
        self.row = row
        self.kind = enforce_of(row)
        fields, prose = blocks.parse(row.body)
        if fields is None:
            raise EmitError(
                "refused: %s carries enforce: %s and no fenced block" % (row.id, self.kind)
            )
        self.fields = fields
        self.prose = prose

    @property
    def roles(self):
        return self.row.keys.get("role") or []

    # hook rows
    @property
    def event(self):
        return self.fields.get("event")

    @property
    def matcher(self):
        return self.fields.get("matcher")

    @property
    def command(self):
        return self.fields.get("command")

    @property
    def agent_scoped(self):
        return self.fields.get("scope") == "agent"

    @property
    def hook_name(self):
        command = self.command or ""
        if not command.startswith(BLOCK_HOOK_PREFIX):
            raise EmitError("refused: %s's hook command does not invoke %s<name>: %r"
                            % (self.row.id, BLOCK_HOOK_PREFIX, command))
        return command[len(BLOCK_HOOK_PREFIX):].split()[0]

    @property
    def hook_invocation(self):
        """The command with `bin/hooks/` stripped: `<name> [args]`."""
        return (self.command or "")[len(BLOCK_HOOK_PREFIX):]

    # deny rows
    @property
    def deny(self):
        return blocks.as_list(self.fields.get("deny"))

    # agent rows
    @property
    def field(self):
        return self.fields.get("field")

    # skill rows
    @property
    def skills(self):
        return blocks.as_list(self.fields.get("skill"))


def read_enforced(rows):
    """`{id: Enforced}` over every `enforce:` rule, refusing a blockless one."""
    found = {}
    for row in rows:
        if row.kind == "rule" and enforce_of(row):
            found[row.id] = Enforced(row)
    return found


def standing_selection(rules, sequences):
    """The rows of `STANDING_QUERY` in bundle order, minus any row carrying
    `paths:` (those are scoped, not standing)."""
    return [row for row in query.select(rules, STANDING_QUERY, sequences)
            if not row.keys.get("paths")]


def text_of(row, enforced):
    """What a harness text file prints for a row: a judgment row's body; an
    `enforce: hook|deny` row's principle prose (nothing for a block-only
    row); nothing for an `enforce: agent|skill` row."""
    item = enforced.get(row.id)
    if item is None:
        return row.body
    if item.kind in ("hook", "deny"):
        return item.prose
    return ""


def render_rows(rows, all_rows, enforced, *, skip_definitions=(),
                definitions_heading="## Definitions", definition_sources=None):
    """Rows as a bundle body: text per row, blank-line separated, definitions
    last under `definitions_heading` — `rulestore.render`'s form without its
    header line. A definition whose id is in `skip_definitions` is left out
    (it is printed elsewhere the reader also loads). `definition_sources` lets
    a skill include definitions used by its process body as well as its rules."""
    lines = []
    for row in rows:
        text = text_of(row, enforced)
        if text:
            lines.append(text)
            lines.append("")
    sources = rows if definition_sources is None else definition_sources
    definitions = [d for d in terms.pull_definitions(sources, all_rows)
                   if d.id not in skip_definitions]
    if definitions:
        lines.append(definitions_heading)
        lines.append("")
        for definition in definitions:
            names = definition.keys.get("term") or []
            lines.append("**%s** — %s" % (names[0] if names else definition.id, definition.body))
            lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n" if lines else ""


def definition_ids(rows, all_rows):
    return {d.id for d in terms.pull_definitions(rows, all_rows)}


def first_sentence(body):
    """The first sentence of a document's prose, headings skipped."""
    paragraph = []
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped or _HEADING_RE.match(stripped):
            if paragraph:
                break
            continue
        paragraph.append(stripped)
    text = " ".join(paragraph)
    if not text:
        return ""
    return _SENTENCE_END_RE.split(text, 1)[0].strip()


def document_stem(doc):
    stem = (doc.path or doc.id).rsplit("/", 1)[-1]
    return stem[:-3] if stem.endswith(".md") else stem


def skill_documents(processes):
    """`[(stem, doc)]` for each process document emitted as a skill."""
    return [(document_stem(doc), doc) for doc in processes
            if document_stem(doc) not in NOT_A_SKILL]


def topic_stem(topic, stems):
    """The skill stem whose document governs `topic`: the stem itself or the
    longest stem the topic extends with `-` (`decision-log-policy` belongs to
    `decision-log`); `None` for a topic with no document. `stems` are the
    document stems `named-queries.md` lists."""
    best = None
    for stem in stems:
        if topic == stem or topic.startswith(stem + "-"):
            if best is None or len(stem) > len(best):
                best = stem
    return best


_PROCESS_REF_RE = re.compile(r"(`?)(?<![\w/])process/([\w-]+)\.md(?![\w/])(`?)")


def rewrite_process_references(doc, stems, form):
    """`doc.body` with each `process/<stem>.md` reference replaced by
    `form % stem`, backticks around it consumed. A reference whose stem is not
    in `stems` raises EmitError naming the document and the reference."""
    def replace(match):
        stem = match.group(2)
        if stem not in stems:
            raise EmitError("refused: %s refers to %s, which is not emitted as a skill"
                            % (doc.path or doc.id, "process/%s.md" % stem))
        quoted = match.group(1) and match.group(3)
        return form % {"stem": stem} + ("" if quoted else match.group(1) + match.group(3))
    return _PROCESS_REF_RE.sub(replace, doc.body)
