"""Codex target (SPEC.md §7; subtraction plan §3b).

Standalone agent TOMLs and project hooks follow the Codex 0.162 interface
verified for this package; see https://learn.chatgpt.com/docs/hooks and
https://learn.chatgpt.com/docs/agent-configuration/subagents. Project hooks
require trust in the adopting repository. Repository hook payloads include
agent_type: the generated dispatcher uses it to scope agent lane guards. Shell
writes and reads outside the named deny patterns remain judgment obligations,
just as the source rows' Human notes say.

The generated adapter translates canonical apply_patch commands into per-file
Write payloads for the unchanged bin/hooks scripts. Bash already carries a
command. Successful hook stdout becomes additionalContext: Codex ignores plain
stdout for tool hooks. No target reads the filesystem; the adapter does so
only when the adopting harness runs it.
"""

from __future__ import annotations

import json
import shlex

from rulestore import query

from . import EmitError, Emission, Target
from .common import (
    NO_MODEL_INVOCATION, definition_ids, first_sentence, read_enforced,
    render_rows, skill_documents, standing_selection, topic_stem,
)

HARNESS = "codex"
AGENTS_MD_LIMIT = 32 * 1024
HOOKS_DIR = ".codex/hooks"
ADAPTER = "codex-hook"
HOOK_COMMAND = 'python3 "$(git rev-parse --show-toplevel)/.codex/hooks/codex-hook"'
SCOPED_GUARD = ("Lane guard is enforced for supported Codex apply_patch calls by "
                "repository hooks scoped to this agent type.")

# Kept in this module so a target remains one module under the target interface.
# This helper is emitted alongside, never substituted for, the original scripts.
HOOK_ADAPTER = r'''#!/usr/bin/env python3
"""Translate Codex tool-hook inputs for fiducial's unchanged hook scripts."""
import fnmatch
import json
import os
import pathlib
import re
import subprocess
import sys


def refuse(reason):
    print("codex-hook: " + reason, file=sys.stderr)
    raise SystemExit(2)


def patch_files(data):
    """Yield synthetic Writes for every path, including both sides of moves.

    Only the decision-log guard needs proposed content. Other pre hooks need
    paths, and post hooks inspect the file after the tool has run. Avoid
    reconstructing old content from a post-tool filesystem.
    """
    raw = data.get("tool_input") or {}
    patch = raw.get("command") if isinstance(raw, dict) else raw
    if not isinstance(patch, str):
        refuse("apply_patch carries no command")
    lines = patch.strip().splitlines()
    if not lines or lines[0] != "*** Begin Patch" or lines[-1] != "*** End Patch":
        refuse("unrecognized apply_patch envelope")
    i = 1
    while i < len(lines) - 1:
        header = re.fullmatch(r"\*\*\* (Add|Update|Delete) File: (.+)", lines[i])
        if not header:
            refuse("unrecognized apply_patch file header")
        kind, name = header.groups()
        i += 1
        move = None
        if i < len(lines) and lines[i].startswith("*** Move to: "):
            move = lines[i][len("*** Move to: "):]
            i += 1
        start = i
        while i < len(lines) and not lines[i].startswith(("*** Add File: ", "*** Update File: ",
                                                        "*** Delete File: ", "*** End Patch")):
            i += 1
        chunks = lines[start:i]
        path = pathlib.Path(name)
        if not path.is_absolute():
            path = pathlib.Path(data.get("cwd") or os.getcwd()) / path
        content = ""
        # Reconstruct just the governed log, before the patch is applied. Full
        # content lets the existing Write guard decide append-only semantics.
        if (kind == "Update" and data.get("hook_event_name") != "PostToolUse"
                and path.as_posix().endswith("/decisions/log.md")):
            old = path.read_text(encoding="utf-8") if path.exists() else ""
            current = old.splitlines()
            cursor, output = 0, []
            pos = 0
            while pos < len(chunks):
                if chunks[pos].startswith("@@"):
                    pos += 1
                    continue
                before, after = [], []
                while pos < len(chunks) and not chunks[pos].startswith("@@"):
                    line = chunks[pos]
                    pos += 1
                    if line == "*** End of File":
                        continue
                    if not line or line[0] not in " +-":
                        refuse("unrecognized apply_patch hunk")
                    if line[0] in " -":
                        before.append(line[1:])
                    if line[0] in " +":
                        after.append(line[1:])
                matches = [n for n in range(cursor, len(current) + 1)
                           if current[n:n + len(before)] == before]
                if len(matches) != 1:
                    refuse("decision-log patch context is absent or ambiguous")
                at = matches[0]
                output.extend(current[cursor:at])
                output.extend(after)
                cursor = at + len(before)
            output.extend(current[cursor:])
            content = "\n".join(output) + ("\n" if output else "")
        elif kind == "Add":
            if any(not line.startswith("+") for line in chunks):
                refuse("unrecognized apply_patch added content")
            content = "\n".join(line[1:] for line in chunks) + ("\n" if chunks else "")
        yield dict(data, tool_name="Write", tool_input={"file_path": str(path), "content": content})
        if move:
            destination = pathlib.Path(move)
            if not destination.is_absolute():
                destination = pathlib.Path(data.get("cwd") or os.getcwd()) / destination
            # Moving the log removes it, even if its old bytes move intact.
            if name.endswith("decisions/log.md"):
                yield dict(data, tool_name="Write", tool_input={"file_path": str(path), "content": ""})
            yield dict(data, tool_name="Write", tool_input={"file_path": str(destination), "content": content})


def path_match(name, pattern):
    """Credential path globs: ** spans zero or more path components."""
    names, patterns = name.split("/"), pattern.split("/")
    def match(parts, globs):
        if not globs:
            return not parts
        if globs[0] == "**":
            return any(match(parts[n:], globs[1:]) for n in range(len(parts) + 1))
        return bool(parts and fnmatch.fnmatchcase(parts[0], globs[0])
                    and match(parts[1:], globs[1:]))
    return match(names, patterns)


def deny(data, patterns):
    tool = data.get("tool_name", "")
    args = data.get("tool_input") or {}
    if not isinstance(args, dict):
        return
    command = args.get("command", args.get("cmd", ""))
    if isinstance(command, list):
        command = " ".join(command)
    for pattern in patterns:
        match = re.fullmatch(r"(Read|Bash)\((.*)\)", pattern)
        if not match:
            refuse("unsupported deny pattern " + repr(pattern))
        kind, glob = match.groups()
        if kind == "Bash" and tool in ("Bash", "exec_command", "shell", "shell_command"):
            if fnmatch.fnmatchcase(command, glob):
                refuse("denied by " + pattern)
        elif kind == "Read" and tool in ("Read", "read_file"):
            name = args.get("file_path", args.get("path", ""))
            if not name:
                continue
            path = pathlib.Path(name).expanduser()
            if not path.is_absolute():
                path = pathlib.Path(data.get("cwd") or os.getcwd()) / path
            if glob.startswith("~/"):
                candidate = str(path.resolve())
                glob = str(pathlib.Path.home().resolve()) + "/" + glob[2:]
            else:
                candidate = os.path.relpath(path, data.get("cwd") or os.getcwd())
                glob = glob.removeprefix("./")
            if path_match(candidate, glob):
                refuse("denied by " + pattern)


def main():
    data = json.load(sys.stdin)
    if not isinstance(data, dict):
        refuse("hook input is not an object")
    if sys.argv[1] == "deny":
        deny(data, json.loads(sys.argv[2]))
        return
    roles = json.loads(sys.argv[2])
    if roles and data.get("agent_type") not in roles:
        return
    script = pathlib.Path(__file__).resolve().parent / sys.argv[3]
    if data.get("tool_name") == "apply_patch":
        payloads = list(patch_files(data))
    else:
        payloads = [data]
    messages = []
    for payload in payloads:
        proc = subprocess.run([sys.executable, str(script), *sys.argv[4:]],
                              input=json.dumps(payload), text=True, capture_output=True)
        if proc.returncode:
            refuse(proc.stderr.strip() or "hook script failed: " + script.name)
        if proc.stdout.strip():
            messages.append(proc.stdout.strip())
    if messages:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": data.get("hook_event_name", "PostToolUse"),
            "additionalContext": "\n".join(messages)}}))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError, IndexError) as exc:
        refuse(str(exc))
'''


def _scalar(value):
    # JSON double-quoted strings are also TOML and YAML double-quoted strings.
    return json.dumps(value, ensure_ascii=False)


def _skill(stem, doc):
    lines = ["---", "name: " + _scalar(stem),
             "description: " + _scalar(first_sentence(doc.body) or stem)]
    if stem in NO_MODEL_INVOCATION:
        lines.append("disable-model-invocation: true")
    return "\n".join(lines + ["---", "", doc.body.strip(), ""])


class CodexTarget(Target):
    name = HARNESS
    takes_query = "none"

    def emit(self, inputs):
        rows = list(inputs.rows)
        rules = sorted((row for row in rows if row.kind == "rule"),
                       key=lambda row: query.sort_key(row, inputs.sequences))
        enforced = read_enforced(rules)
        column = (inputs.tiers.get("harnesses") or {}).get(HARNESS)
        if not column:
            raise EmitError("refused: tiers.json has no 'codex' column")
        role_tiers = inputs.tiers.get("roles") or {}
        documents = skill_documents(sorted((row for row in rows if row.kind == "process"),
                                           key=lambda row: query.sort_key(row, inputs.sequences)))
        stems = [stem for stem in inputs.sequences[1] if stem in dict(documents)]
        standing, spill = [], {}
        for row in standing_selection(rules, inputs.sequences):
            topics = row.keys.get("topic") or []
            stem = topic_stem(topics[0], stems) if topics else None
            if stem is None:
                standing.append(row)
            else:
                spill.setdefault(stem, []).append(row)
        body = render_rows(standing, rows, enforced)
        text = "<!-- fiducial %s @ %s -->\n\n%s" % (inputs.repo, inputs.head, body)
        count = len(text.encode("utf-8"))
        if count > AGENTS_MD_LIMIT:
            raise EmitError("refused: AGENTS.md is %d bytes, over the %d-byte limit"
                            % (count, AGENTS_MD_LIMIT))
        emission = Emission(files={"AGENTS.md": text})
        files = emission.files
        standing_ids = {row.id for row in standing}
        definitions = definition_ids(standing, rows)
        skill_names = {stem for stem, _ in documents}
        for stem, doc in documents:
            text = _skill(stem, doc)
            if stem in spill:
                text += "\n## Rules\n\n" + render_rows(
                    spill[stem], rows, enforced, skip_definitions=definitions,
                    definitions_heading="### Definitions")
            files[".agents/skills/%s/SKILL.md" % stem] = text

        hooks = {}
        for item in enforced.values():
            if item.kind == "hook":
                if not item.event or not item.matcher or not item.command:
                    raise EmitError("refused: %s's hook block lacks event, matcher or command"
                                    % item.row.id)
                if item.hook_name not in inputs.hooks:
                    raise EmitError("refused: %s's block invokes %s, which bin/hooks/ does not provide"
                                    % (item.row.id, item.command))
                if item.agent_scoped and not item.roles:
                    raise EmitError("refused: %s has agent scope but no role" % item.row.id)
                roles = item.roles if item.agent_scoped else []
                try:
                    invocation = shlex.join(shlex.split(item.hook_invocation))
                except ValueError as exc:
                    raise EmitError("refused: %s has an invalid hook command: %s" % (item.row.id, exc))
                command = HOOK_COMMAND + " script " + shlex.quote(json.dumps(roles)) + " " + invocation
                matcher = item.matcher  # Codex aliases Edit|Write to apply_patch.
            elif item.kind == "deny":
                for pattern in item.deny:
                    if not (pattern.startswith(("Read(", "Bash(")) and pattern.endswith(")")):
                        raise EmitError("refused: %s has unsupported deny pattern %r"
                                        % (item.row.id, pattern))
                command = HOOK_COMMAND + " deny " + shlex.quote(json.dumps(item.deny))
                matcher = ".*"
            elif item.kind == "skill":
                for skill in item.skills:
                    if skill not in skill_names:
                        emission.notes.append("%s names skill %r; no process document provides it yet"
                                              % (item.row.id, skill))
                continue
            else:
                continue
            event = item.event if item.kind == "hook" else "PreToolUse"
            entries = hooks.setdefault(event, [])
            entry = next((entry for entry in entries if entry["matcher"] == matcher), None)
            if entry is None:
                entry = {"matcher": matcher, "hooks": []}
                entries.append(entry)
            entry["hooks"].append({"type": "command", "command": command})
        files[".codex/hooks.json"] = json.dumps({"hooks": hooks}, indent=2) + "\n"
        if ADAPTER in inputs.hooks:
            raise EmitError("refused: bin/hooks/%s collides with the Codex adapter" % ADAPTER)
        for name, script in sorted(inputs.hooks.items()):
            files[HOOKS_DIR + "/" + name] = script
            emission.executable.add(HOOKS_DIR + "/" + name)
        files[HOOKS_DIR + "/" + ADAPTER] = HOOK_ADAPTER
        emission.executable.add(HOOKS_DIR + "/" + ADAPTER)

        for role, tier in sorted(role_tiers.items()):
            own = query.select(rules, {"role": role}, inputs.sequences)
            descriptions, skills, lane = [], [], []
            for row in own:
                item = enforced.get(row.id)
                if item is None:
                    continue
                if item.kind == "agent" and item.field == "description":
                    descriptions.append(item.prose + (" " + row.human.strip() if row.human else ""))
                elif item.kind == "skill":
                    for skill in item.skills:
                        if skill in skill_names and skill not in skills:
                            skills.append(skill)
                elif item.kind == "hook" and item.agent_scoped:
                    lane.append("Scoped lane guard (%s): %s/%s" %
                                (row.id, HOOKS_DIR, item.hook_invocation))
            specific = [row for row in own if row.id not in standing_ids and not row.keys.get("paths")]
            instructions = ""
            if lane:
                instructions += SCOPED_GUARD + "\n\n" + "\n".join(lane) + "\n\n"
            instructions += render_rows(specific, rows, enforced, skip_definitions=definitions)
            for row in own:
                if row.keys.get("paths"):
                    instructions += "\n## Rules for paths matching %s\n\n%s" % (
                        ", ".join(row.keys["paths"]),
                        render_rows([row], rows, enforced, skip_definitions=definitions))
            if skills:
                instructions += "\nAvailable procedures: " + ", ".join(
                    "$%s (.agents/skills/%s/SKILL.md)" % (skill, skill) for skill in skills) + ".\n"
            fields = [("name", role), ("description", " ".join(descriptions) or "Fiducial's %s role." % role),
                      ("model", column[tier]), ("developer_instructions", instructions)]
            files[".codex/agents/%s.toml" % role] = "\n".join(
                key + " = " + _scalar(value) for key, value in fields) + "\n"
        return emission
