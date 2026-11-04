"""The `claude-code` target: `CLAUDE.md` and `.claude/` (SPEC.md §7; the plan,
§3a). The worked example of the interface in this package's docstring.

What it emits, from what:

- `CLAUDE.md` — the standing context: the judgment rows of the query
  `role=chief-of-staff session=decision`, in bundle order, plus the
  principle prose of the `enforce: hook|deny` rows in that selection (the
  mechanism is in `settings.json`; the principle is what the model reads —
  DEC-001220), then the definitions those rows use. No row carrying
  `paths:` (those go to `.claude/rules/`), no `enforce: agent|skill` row
  (fields and skills), no process document (skills). Over `CLAUDE_MD_LIMIT`
  lines the target refuses and reports the count.
- `.claude/rules/<topic>.md` — one file per first topic of the rows carrying
  `paths:`, with `paths:` the union of their patterns, body the rows.
- `.claude/agents/<role>.md` — one per role the tier map gives a tier
  (`tiers["roles"]`): `description` from the role's `field: description`
  rows (R1056's Human note rides with it, DEC-001270), `model` from the
  role's tier through the harness column, `tools` read-only for a reviewer
  or skeptic role and writing for the rest (`READ_ONLY_MARKERS`), `skills`
  the skills the role's `enforce: skill` rows name and the emission
  provides, `hooks` the role's `scope: agent` hook rows, and the body the
  role's rows rendered as a bundle renders them, definitions last.
- `.claude/skills/<stem>/SKILL.md` — one per process document except
  `project-setup` and `named-queries`; `name` the stem, `description` the document's first
  sentence, `disable-model-invocation: true` for `gate`; the body is the
  document.
- `.claude/settings.json` — `permissions.deny` from the `enforce: deny`
  blocks (in row order, duplicates dropped) and `hooks` from the repo-level
  `enforce: hook` blocks, grouped by event then matcher.
- `.claude/hooks/<name>` — every script under `bin/hooks/`, marked
  executable; every block command is rewritten from `bin/hooks/<name>` to
  `.claude/hooks/<name>`.

Two consistency checks run before anything is returned: every hook a block
names is a script the emission carries (a refusal otherwise), and every
skill a row names that no document provides is a note, not a refusal, since
the documents land after this emitter (the plan, §4).
"""

from __future__ import annotations

import json
import re

from rulestore import query, render, terms

from . import EmitError, Emission, Target, blocks

HARNESS = "claude-code"
CLAUDE_MD_QUERY = {"role": "chief-of-staff", "session": "decision"}
CLAUDE_MD_LIMIT = 200
HOOKS_DIR = ".claude/hooks"
BLOCK_HOOK_PREFIX = "bin/hooks/"

#: A role whose slug carries one of these reads and reports; it does not edit.
READ_ONLY_MARKERS = ("reviewer", "skeptic")
READ_ONLY_TOOLS = ["Read", "Grep", "Glob"]
WRITING_TOOLS = ["Read", "Grep", "Glob", "Edit", "Write", "Bash"]

#: Process documents that are not skills: `project-setup` (the plan, §3a)
#: and `named-queries`, which is this tool's own input, not a procedure.
NOT_A_SKILL = ("project-setup", "named-queries")
#: Skills the model may not invoke on its own (DEC-001280: the gate).
NO_MODEL_INVOCATION = ("gate",)

_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s")
_HEADING_RE = re.compile(r"^#{1,6}\s+")


# ------------------------------------------------------------- classification


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

    def emitted_command(self):
        return HOOKS_DIR + "/" + self.command[len(BLOCK_HOOK_PREFIX):]

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


def render_rows(rows, all_rows, enforced):
    """Rows as a bundle body: text per row, blank-line separated, definitions
    last under `## Definitions` — `rulestore.render`'s form without its
    header line."""
    lines = []
    for row in rows:
        text = text_of(row, enforced)
        if text:
            lines.append(text)
            lines.append("")
    definitions = terms.pull_definitions(rows, all_rows)
    if definitions:
        lines.append("## Definitions")
        lines.append("")
        for definition in definitions:
            names = definition.keys.get("term") or []
            lines.append("**%s** — %s" % (names[0] if names else definition.id, definition.body))
            lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n" if lines else ""


# ------------------------------------------------------------------ frontmatter


_PLAIN_SCALAR_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _./*'(),;!?-]*$")


def _yaml_scalar(text):
    """A frontmatter scalar: plain where YAML reads it back unchanged, else a
    JSON string, which YAML reads as a double-quoted scalar."""
    if (_PLAIN_SCALAR_RE.match(text) and ": " not in text and " #" not in text
            and not text.endswith(":") and text.lower() not in ("true", "false", "yes", "no", "null")):
        return text
    return json.dumps(text, ensure_ascii=False)


def _yaml_list(items):
    return "[" + ", ".join(_yaml_scalar(item) for item in items) + "]"


def frontmatter(fields):
    """`---` block from an ordered list of `(key, value)`; a value is a
    string, a list of strings, or a `hooks` mapping rendered as YAML."""
    lines = ["---"]
    for key, value in fields:
        if isinstance(value, list):
            lines.append("%s: %s" % (key, _yaml_list(value)))
        elif isinstance(value, dict):
            lines.append("%s:" % key)
            lines.extend(_yaml_hooks(value))
        elif isinstance(value, bool):
            lines.append("%s: %s" % (key, "true" if value else "false"))
        else:
            lines.append("%s: %s" % (key, _yaml_scalar(value)))
    lines.append("---")
    return "\n".join(lines) + "\n"


def _yaml_hooks(hooks):
    """`{event: [{matcher, hooks: [{type, command}]}]}` as indented YAML."""
    lines = []
    for event, entries in hooks.items():
        lines.append("  %s:" % event)
        for entry in entries:
            lines.append("    - matcher: %s" % json.dumps(entry["matcher"]))
            lines.append("      hooks:")
            for hook in entry["hooks"]:
                lines.append("        - type: %s" % hook["type"])
                lines.append("          command: %s" % json.dumps(hook["command"]))
    return lines


def group_hooks(items):
    """`{event: [{matcher, hooks: [...]}]}` from hook rows, grouped by event
    then matcher, in row order."""
    grouped = {}
    for item in items:
        if not item.event or not item.matcher or not item.command:
            raise EmitError("refused: %s's hook block lacks event, matcher or command"
                            % item.row.id)
        entries = grouped.setdefault(item.event, [])
        for entry in entries:
            if entry["matcher"] == item.matcher:
                break
        else:
            entry = {"matcher": item.matcher, "hooks": []}
            entries.append(entry)
        entry["hooks"].append({"type": "command", "command": item.emitted_command()})
    return grouped


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


def tools_for(role):
    if any(marker in role for marker in READ_ONLY_MARKERS):
        return list(READ_ONLY_TOOLS)
    return list(WRITING_TOOLS)


# ---------------------------------------------------------------------- target


class ClaudeCodeTarget(Target):
    name = HARNESS
    takes_query = "none"

    def emit(self, inputs):
        rows = list(inputs.rows)
        rules = [row for row in rows if row.kind == "rule"]
        processes = [row for row in rows if row.kind == "process"]
        enforced = read_enforced(rules)
        column = (inputs.tiers.get("harnesses") or {}).get(HARNESS)
        if not column:
            raise EmitError("refused: tiers.json has no %r column" % HARNESS)
        role_tiers = inputs.tiers.get("roles") or {}

        emission = Emission()
        files = emission.files

        # --- skills, first: agents and the consistency check name them
        skill_names = set()
        for doc in processes:
            stem = (doc.path or doc.id).rsplit("/", 1)[-1]
            stem = stem[:-3] if stem.endswith(".md") else stem
            if stem in NOT_A_SKILL:
                continue
            fields = [("name", stem), ("description", first_sentence(doc.body) or stem)]
            if stem in NO_MODEL_INVOCATION:
                fields.append(("disable-model-invocation", True))
            files[".claude/skills/%s/SKILL.md" % stem] = (
                frontmatter(fields) + "\n" + doc.body.strip() + "\n"
            )
            skill_names.add(stem)

        # --- hook scripts
        for name, text in sorted(inputs.hooks.items()):
            files["%s/%s" % (HOOKS_DIR, name)] = text
            emission.executable.add("%s/%s" % (HOOKS_DIR, name))

        # --- CLAUDE.md
        standing = [
            row for row in query.select(rules, CLAUDE_MD_QUERY, inputs.sequences)
            if not row.keys.get("paths")
        ]
        body = render_rows(standing, rows, enforced)
        claude_md = "<!-- fiducial %s @ %s -->\n\n%s" % (inputs.repo, inputs.head, body)
        count = claude_md.count("\n")
        if count > CLAUDE_MD_LIMIT:
            raise EmitError("refused: CLAUDE.md would be %d lines, over the %d-line limit"
                            % (count, CLAUDE_MD_LIMIT))
        files["CLAUDE.md"] = claude_md

        # --- .claude/rules/<topic>.md
        scoped = {}
        for row in sorted(rules, key=lambda r: query.sort_key(r, inputs.sequences)):
            if row.keys.get("paths"):
                topic = (row.keys.get("topic") or ["untopiced"])[0]
                scoped.setdefault(topic, []).append(row)
        for topic, topic_rows in scoped.items():
            paths = []
            for row in topic_rows:
                for pattern in row.keys["paths"]:
                    if pattern not in paths:
                        paths.append(pattern)
            files[".claude/rules/%s.md" % topic] = (
                frontmatter([("paths", paths)]) + "\n"
                + render_rows(topic_rows, rows, enforced)
            )

        # --- .claude/agents/<role>.md
        roles_seen = set()
        for row in rules:
            roles_seen.update(row.keys.get("role") or [])
        for role in sorted(roles_seen):
            tier = role_tiers.get(role)
            if tier is None:
                continue
            own = [row for row in query.select(rules, {"role": role}, inputs.sequences)
                   if not row.keys.get("paths")]
            descriptions, skills, agent_hooks = [], [], []
            for row in own:
                item = enforced.get(row.id)
                if item is None:
                    continue
                if item.kind == "agent" and item.field == "description":
                    text = item.prose
                    if row.human:
                        text = "%s %s" % (text, row.human.strip())
                    descriptions.append(text)
                elif item.kind == "skill":
                    for skill in item.skills:
                        if skill not in skills:
                            skills.append(skill)
                elif item.kind == "hook" and item.agent_scoped:
                    agent_hooks.append(item)
            description = " ".join(descriptions) or "Fiducial's %s role." % role
            fields = [
                ("name", role),
                ("description", description),
                ("model", column[tier]),
                ("tools", tools_for(role)),
            ]
            provided = [skill for skill in skills if skill in skill_names]
            for skill in skills:
                if skill not in skill_names:
                    emission.notes.append(
                        "%s names skill %r; no process document provides it yet"
                        % (role, skill))
            if provided:
                fields.append(("skills", provided))
            if agent_hooks:
                fields.append(("hooks", group_hooks(agent_hooks)))
            files[".claude/agents/%s.md" % role] = (
                frontmatter(fields) + "\n" + render_rows(own, rows, enforced)
            )

        # --- settings.json
        deny = []
        repo_hooks = []
        for item in enforced.values():
            if item.kind == "deny":
                for pattern in item.deny:
                    if pattern not in deny:
                        deny.append(pattern)
            elif item.kind == "hook" and not item.agent_scoped:
                repo_hooks.append(item)
        repo_hooks.sort(key=lambda item: query.sort_key(item.row, inputs.sequences))
        settings = {"permissions": {"deny": deny}, "hooks": group_hooks(repo_hooks)}
        files[".claude/settings.json"] = json.dumps(settings, indent=2) + "\n"

        # --- consistency: every hook a block names is a script we carry
        for item in enforced.values():
            if item.kind == "hook":
                script = "%s/%s" % (HOOKS_DIR, item.hook_name)
                if script not in files:
                    raise EmitError("refused: %s's block invokes %s, which bin/hooks/ does not provide"
                                    % (item.row.id, item.command))
        return emission
