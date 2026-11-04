"""The `claude-code` target: `CLAUDE.md` and `.claude/` (SPEC.md §7; the plan,
§3a). The worked example of the interface in this package's docstring.

What it emits, from what:

- `CLAUDE.md` — the standing context: the judgment rows of the query
  `role=chief-of-staff session=decision`, in bundle order, plus the
  principle prose of the `enforce: hook|deny` rows in that selection (the
  mechanism is in `settings.json`; the principle is what the model reads —
  DEC-001220), then the definitions those rows use. No row carrying
  `paths:` (those go to `.claude/rules/`), no `enforce: agent|skill` row
  (fields and skills), no process document (skills). A row whose first topic
  names an emitted skill (`common.topic_stem`: the topic is, or extends with
  `-`, a stem `named-queries.md` lists) spills: it is omitted here and
  appended to that `SKILL.md` under `## Rules`. Over `CLAUDE_MD_LIMIT` lines
  the target warns with the count on stderr and still emits; the limit is
  guidance.
- `.claude/rules/<topic>.md` — one file per first topic of the rows carrying
  `paths:`, with `paths:` the union of their patterns, body the rows.
- `.claude/agents/<role>.md` — one per role the tier map gives a tier
  (`tiers["roles"]`): `description` from the role's `field: description`
  rows (R1056's Human note rides with it, DEC-001270), `model` from the
  role's tier through the harness column, `tools` the same list for every
  agent (a role's lane is a `scope: agent` hook row, not a tool list), `skills`
  the skills the role's `enforce: skill` rows name and the emission
  provides, `hooks` the role's `scope: agent` hook rows, and the body the
  role's rows rendered as a bundle renders them, definitions last, minus the
  rows (and definitions) `CLAUDE.md` already carries, which the agent also loads.
- `.claude/skills/<stem>/SKILL.md` — one per process document except
  `project-setup` and `named-queries`; `name` the stem, `description` the document's first
  sentence, `disable-model-invocation: true` for `gate`; the body is the
  document.
- `.claude/settings.json` — `permissions.deny` from the `enforce: deny`
  blocks (in row order, duplicates dropped) and `hooks` from the repo-level
  `enforce: hook` blocks, grouped by event then matcher.
- `.claude/hooks/<name>` — every script under `bin/hooks/`, marked
  executable; every block command is rewritten from `bin/hooks/<name>` to
  `"$CLAUDE_PROJECT_DIR"/.claude/hooks/<name>`, so a session started in a
  subdirectory still finds it.

What a row prints, the standing selection and the skill rules live in
`common.py`, which every harness target shares.

Two consistency checks run before anything is returned: every hook a block
names is a script the emission carries (a refusal otherwise), and every
skill a row names that no document provides is a note, not a refusal, since
the documents land after this emitter (the plan, §4).
"""

from __future__ import annotations

import json
import re

from rulestore import query

from . import EmitError, Emission, Target
from .common import (
    NO_MODEL_INVOCATION,
    definition_ids,
    first_sentence,
    read_enforced,
    render_rows,
    skill_documents,
    standing_selection,
    topic_stem,
)

HARNESS = "claude-code"
#: `CLAUDE.md` over this many lines is a warning with the count, not a
#: refusal: the limit is guidance (the human's ruling, 2026-11-04).
CLAUDE_MD_LIMIT = 200
HOOKS_DIR = ".claude/hooks"
#: How a hook command reaches its script: from the project root the harness
#: names, not the session's working directory.
HOOK_COMMAND_DIR = '"$CLAUDE_PROJECT_DIR"/' + HOOKS_DIR
TOOLS = ["Read", "Grep", "Glob", "Edit", "Write", "Bash"]


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
        entry["hooks"].append({"type": "command",
                               "command": HOOK_COMMAND_DIR + "/" + item.hook_invocation})
    return grouped


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

        # --- the standing selection, and which of its rows spill into skills
        standing = standing_selection(rules, inputs.sequences)
        documents = skill_documents(processes)
        stems = [stem for stem in inputs.sequences[1] if stem in dict(documents)]
        spill = {}
        in_claude_md = []
        for row in standing:
            topics = row.keys.get("topic") or []
            stem = topic_stem(topics[0], stems) if topics else None
            if stem is None:
                in_claude_md.append(row)
            else:
                spill.setdefault(stem, []).append(row)

        # --- CLAUDE.md
        body = render_rows(in_claude_md, rows, enforced)
        claude_md = "<!-- fiducial %s @ %s -->\n\n%s" % (inputs.repo, inputs.head, body)
        count = claude_md.count("\n")
        if count > CLAUDE_MD_LIMIT:
            emission.notes.append(
                "warning: CLAUDE.md is %d lines, over the %d-line guidance; emitted anyway"
                % (count, CLAUDE_MD_LIMIT))
        files["CLAUDE.md"] = claude_md
        claude_md_rows = {row.id for row in in_claude_md}
        claude_md_definitions = definition_ids(in_claude_md, rows)

        # --- skills: agents and the consistency check name them
        skill_names = set()
        for stem, doc in documents:
            fields = [("name", stem), ("description", first_sentence(doc.body) or stem)]
            if stem in NO_MODEL_INVOCATION:
                fields.append(("disable-model-invocation", True))
            text = frontmatter(fields) + "\n" + doc.body.strip() + "\n"
            if stem in spill:
                text += "\n## Rules\n\n" + render_rows(
                    spill[stem], rows, enforced, skip_definitions=claude_md_definitions,
                    definitions_heading="### Definitions")
            files[".claude/skills/%s/SKILL.md" % stem] = text
            skill_names.add(stem)

        # --- hook scripts
        for name, text in sorted(inputs.hooks.items()):
            files["%s/%s" % (HOOKS_DIR, name)] = text
            emission.executable.add("%s/%s" % (HOOKS_DIR, name))

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
                ("tools", list(TOOLS)),
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
            # the agent also loads CLAUDE.md: its body carries only what that lacks
            specific = [row for row in own if row.id not in claude_md_rows]
            files[".claude/agents/%s.md" % role] = (
                frontmatter(fields) + "\n"
                + render_rows(specific, rows, enforced, skip_definitions=claude_md_definitions)
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
