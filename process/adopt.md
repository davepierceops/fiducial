---
order: 45
topic: [adopt]
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Adopt

Reconcile the store's current harness context into a repository, including a
repository already using fiducial; use the same procedure for upgrades.
The source of truth and reconciliation ruling are DEC-001630; project
preconditions are in `project-setup`, review separation is [R0462], and gate
classification and authority are [R0534, R0535].

1. **Prepare without changing the target.** Read the target's spec, decisions,
   and `project-setup` preconditions. Record the store SHA and dirty diff, target
   SHA, environment and egress boundary. Extract the single `python` fence below
   to a temporary `adopt.py` (Python 3.11+). Run `python3 adopt.py prepare STORE
   TARGET STAGE`, with absolute paths and a new staging directory outside both
   repositories. This inventories both layouts, including nested `AGENTS.md`
   and `AGENTS.override.md`, stages `--emit claude-code` and `--emit codex`, and
   writes `plan.json` and a proposed `candidate/` tree. Nothing is installed.
2. **Independent contradiction read.** Give a subagent that wrote none of the
   candidate the complete inventory, both staging trees, the candidate diff,
   and relevant target decisions/spec. It reads every inventoried file, including
   nested overrides (which may shadow root instructions), `.codex/config.toml`,
   settings, hooks, rules, agents and skills. Report contradictions by existing
   file/line and staged file/line, their consequence, and proposed disposition;
   do not infer compatibility from a mechanical merge. Its ordinary review
   artifact uses `review-artifact`. Also write `review.json` with `plan_sha256`
   (SHA256 of `plan.json` bytes), `reviewer`, and `findings`: an array of objects
   with unique `id`, `file`, positive integer `line`, `staged_file`, positive
   integer `staged_line`, and `claim`. An empty array explicitly means no
   contradictions found. A planned read that did not run remains a gap [R1617].
3. **Human rulings before append.** Present that report and complete candidate
   diff. For an exact removal/replacement of legacy instructions, prepare a JSON
   array of `{ "path": "CLAUDE.md", "before": "exact old text", "after": "replacement" }`
   edits, then re-run prepare in a new stage with that file as its fourth argument.
   Each `before` must match exactly once. The new plan must receive an independent
   read too. Structural conflicts (an occupied agent or hook name, incompatible
   frontmatter, malformed ownership, edited managed content) require a concrete
   human resolution and a fresh prepare; the helper never guesses. The human
   rules on every contradiction, even one accepted as a risk. Record the actual
   rulings, not an agent's proposed ruling, in `approval.json`: `plan_sha256`,
   `review_sha256` (SHA256 of `review.json` bytes), `human` (name), `go`: `true`,
   `gate` (issue reference, or `routine` when so classified), and `rulings`
   (finding-id to nonempty ruling text). For a consequential adoption, invoke
   `gate` with this package before installation. A file saying `go` records the
   human's response; it cannot supply that response. The first real Illuminait
   run uses this gate, with the report brought to the human before append.
4. **Create/append.** After those rulings, run `python3 adopt.py apply STAGE
   REVIEW_JSON APPROVAL_JSON`. It rechecks the inventory, writes missing files,
   and replaces only owned material. Use `python3 adopt.py labels OWNER/REPO`
   to create missing `human-gate` and the four release-impact labels defined in
   `process/verification-checklists.md`;
   existing label metadata is preserved. Read the labels back. The labels command
   touches GitHub, and is run only within the same authorization as installation.
   No command here commits, pushes, merges, applies infrastructure or destroys it.
5. **Evidence and landing.** The helper saves the inventory, independent read,
   rulings, changed paths, and verification boundary in the target's
   `docs/fiducial-adoption-<timestamp>.md`. Add environment, store/target SHAs,
   dirty source diff, forge-label read-back, project-setup confirmation, and
   actual gate decision to that report. Preserve its timestamp and content when
   a repeat run has no changes; the helper then writes no new report. Inspect the
   complete diff and repeat prepare/apply in a stand-in to establish no diff on
   rerun. Append the adoption ruling to target `decisions/log.md` through
   `decision-log`; remove a superseded `.fiducial/` tree only when the human has
   explicitly approved its removal, recording the removed pin. Open the target's
   own PR; retain a report copy in fiducial `reviews/`. Landing uses `release` and
   the human's merge decision. Keep Claude Code loading **contract-verified**
   until the human opens a fresh session at that target and runs `/context`;
   give him a pasteable command block with the real target path and expected
   output: the repository's `CLAUDE.md` listed as a loaded instruction source.
   Record the observed line when supplied. Codex hook trust is also a live
   boundary; emitted files alone do not prove enforcement.

## Ownership and deterministic create/append

The executable procedure below is part of this skill, not a separately installed
runtime. Tests extract and execute this fence. `.claude/fiducial-ownership.json`
records ownership for both layouts. Markdown uses `<!-- fiducial:begin -->` and
`<!-- fiducial:end -->` as whole lines outside code fences; YAML frontmatter
stays first and is replaced only when owned and unchanged. JSON uses recorded
key/list contributions, never HTML comments: unrelated values and pre-existing
identical entries remain the repository's. Generated TOML agents and executable
hooks use exact file hashes; a collision or later local edit is refused rather
than concatenating invalid configuration or displacing a shebang. An existing
Markdown or JSON file keeps its permissions; a new file takes the generated
ones. Upgrades remove obsolete owned contributions; ambiguous removals need a
human resolution.
Keep the manifest in the adoption PR. Work on an idle branch: checks protect
against changes since review, but installation is not a transaction against a
concurrent editor or a filesystem failure; inspect and revert the adoption diff
if an I/O failure interrupts it.

```python
import copy
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

BEGIN = "<!-- fiducial:begin -->"
END = "<!-- fiducial:end -->"
MANIFEST = ".claude/fiducial-ownership.json"
LAYOUTS = (".claude", ".codex", ".agents")
LABELS = ("human-gate", "blocking", "deferred", "accepted-risk", "not-material")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def safe(root, name):
    parts = pathlib.PurePosixPath(name).parts
    require(parts and not name.startswith("/") and all(p not in ("..", ".git") for p in parts),
            "unsafe path: " + name)
    path = root
    for index, part in enumerate(parts):
        path = path / part
        require(not path.is_symlink(), "symlink: " + str(path))
        require(index == len(parts) - 1 or not path.exists() or path.is_dir(),
                "parent is not a directory: " + str(path))
    require(path.resolve().is_relative_to(root.resolve()), "path escapes target")
    return path


def inventory(root):
    result = {}
    for base, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d != ".git")
        for name in sorted(files + [d for d in dirs if (pathlib.Path(base) / d).is_symlink()]):
            path = pathlib.Path(base) / name
            rel = path.relative_to(root).as_posix()
            if rel.split("/")[0] in LAYOUTS or name in ("CLAUDE.md", "AGENTS.md", "AGENTS.override.md"):
                safe(root, rel)
                require(path.is_file(), "not a regular file: " + rel)
                result[rel] = {"sha256": digest(path.read_bytes()),
                               "mode": path.stat().st_mode & 0o777}
    return result


def frontmatter(text):
    if not re.match(r"^---\r?\n", text):
        return "", text
    match = re.match(r"^---\r?\n.*?\r?\n---\r?\n", text, re.S)
    require(match is not None, "unterminated frontmatter")
    return text[:match.end()], text[match.end():]


def section(text):
    # Ignore examples, including this very skill's embedded marker strings.
    marks, offset, fence = [], 0, None
    for line in text.splitlines(keepends=True):
        bare = line.rstrip("\r\n")
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", bare)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match:
            fence = match[1]
        elif bare in (BEGIN, END):
            marks.append((bare, offset, offset + len(line)))
        offset += len(line)
    require(not fence, "unterminated code fence")
    require(not marks or [m[0] for m in marks] == [BEGIN, END], "ambiguous fiducial markers")
    return (marks[0][1], marks[1][2]) if marks else None


def markdown(current, wanted, old):
    header, body = frontmatter(current)
    bounds = section(body)
    if old:
        require(header == old["header"], "managed frontmatter edited")
        require(bounds and digest(body[bounds[0]:bounds[1]].encode()) == old["section"],
                "managed prose edited or missing")
    else:
        require(not bounds, "untracked fiducial markers")
    if wanted is None:
        body = body[:bounds[0]] + body[bounds[1]:]
        require(not header or not body.strip(), "shared frontmatter retirement needs a ruling")
        return (None if not body.strip() else body), None
    new_header, new_body = frontmatter(wanted)
    owns_header = old["owns_header"] if old else not current
    require(header == new_header or owns_header, "frontmatter collision")
    block = BEGIN + "\n" + new_body.strip("\n") + "\n" + END + "\n"
    require(section(block) == (0, len(block)), "generated prose has conflicting markers or fence")
    if bounds:
        body = body[:bounds[0]] + block + body[bounds[1]:]
    else:
        body += ("\n" if body and not body.endswith("\n") else "") + block
    return new_header + body, {"kind": "markdown", "header": new_header,
                              "owns_header": owns_header, "section": digest(block.encode())}


def json_merge(current, wanted, old):
    data = json.loads(current or "{}")
    require(isinstance(data, dict), "JSON root must be an object")
    before = copy.deepcopy(data)
    for kind, keys, value in (old or {}).get("contributions", []):
        parent = data
        for key in keys[:-1]:
            require(isinstance(parent, dict) and key in parent, "owned JSON path missing")
            parent = parent[key]
        key = keys[-1]
        require(isinstance(parent, dict) and key in parent, "owned JSON value missing")
        if kind == "item":
            require(isinstance(parent[key], list) and parent[key].count(value) == 1,
                    "owned JSON list contribution edited")
            parent[key].remove(value)
        else:
            require(parent[key] == value, "owned JSON scalar edited")
            del parent[key]
    contributions = []
    def add(target, source, keys):
        require(isinstance(source, dict), "generated JSON root must be an object")
        for key, value in source.items():
            path = keys + [key]
            if isinstance(value, dict):
                target.setdefault(key, {})
                require(isinstance(target[key], dict), "JSON object collision: " + str(path))
                add(target[key], value, path)
            elif isinstance(value, list):
                target.setdefault(key, [])
                require(isinstance(target[key], list), "JSON list collision: " + str(path))
                for item in value:
                    if item not in target[key]:
                        target[key].append(item)
                        contributions.append(["item", path, item])
            elif key in target:
                require(target[key] == value, "JSON scalar collision: " + str(path))
            else:
                target[key] = value
                contributions.append(["value", path, value])
    if wanted is not None:
        add(data, json.loads(wanted), [])
    text = current if before == data and current else encoded(data).decode()
    state = {"kind": "json", "contributions": contributions} if wanted is not None else None
    return text, state


def build_plan(target, staged, edits=()):
    snapshot = inventory(target)
    manifest_path = safe(target, MANIFEST)
    prior = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"version": 1, "files": {}}
    require(prior.get("version") == 1, "unknown ownership version")
    desired = {}
    for tree in staged:
        for name in inventory(tree):
            require(name != MANIFEST and name not in desired, "duplicate/reserved staged path: " + name)
            path = safe(tree, name)
            desired[name] = (path.read_bytes().decode("utf-8"), path.stat().st_mode & 0o777)
    require("CLAUDE.md" in desired and "AGENTS.md" in desired, "stage both harnesses")
    edited = {}
    for edit in edits:
        name = edit["path"]
        require(name in snapshot and name != MANIFEST, "edit is outside inventoried context")
        text = edited.get(name, safe(target, name).read_bytes().decode("utf-8"))
        require(edit["before"] and text.count(edit["before"]) == 1, "edit must match exactly once: " + name)
        edited[name] = text.replace(edit["before"], edit["after"], 1)
    writes, owned, conflicts = {}, {}, []
    names = set(desired) | set(prior["files"]) | set(edited)
    for name in sorted(names):
        try:
            path = safe(target, name)
            current = path.read_bytes().decode("utf-8") if path.exists() else ""
            mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
            text = edited.get(name, current)
            old = prior["files"].get(name)
            wanted, new_mode = desired.get(name, (None, mode))
            if path.exists() and name.endswith((".md", ".json")):
                new_mode = mode
            if wanted is None and not old:
                result, state = text, None
            elif name.endswith(".md"):
                result, state = markdown(text, wanted, old)
            elif name.endswith(".json"):
                result, state = json_merge(text, wanted, old)
            else:
                # TOML and scripts remain valid, whole-file objects with hash ownership.
                require((old and old["kind"] == "file" and digest(text.encode()) == old["sha256"]
                         and mode == old["mode"]) or (not old and not path.exists()),
                        "occupied or modified structured file")
                result = wanted
                state = ({"kind": "file", "sha256": digest(wanted.encode()), "mode": new_mode}
                         if wanted is not None else None)
            if state:
                owned[name] = state
            if result != current or (result is not None and mode != new_mode):
                writes[name] = {"text": result, "mode": new_mode}
        except (ValueError, OSError, KeyError, TypeError) as exc:
            conflicts.append({"file": name, "reason": str(exc)})
    manifest = encoded({"version": 1, "files": owned}).decode()
    if not manifest_path.exists() or manifest_path.read_text() != manifest:
        writes[MANIFEST] = {"text": manifest,
                          "mode": manifest_path.stat().st_mode & 0o777 if manifest_path.exists() else 0o644}
    return {"target": str(target.resolve()), "inventory": snapshot, "writes": writes,
            "conflicts": conflicts, "edits": list(edits)}


def prepare(store, target, stage, edits=()):
    require(not stage.exists(), "use a fresh staging directory")
    require(not stage.resolve().is_relative_to(target.resolve()) and
            not stage.resolve().is_relative_to(store.resolve()), "stage outside both repositories")
    stage.mkdir(parents=True)
    trees = []
    for harness in ("claude-code", "codex"):
        tree = stage / harness
        subprocess.run([str(store / "bin/bundle"), "--emit", harness, "--out", str(tree)],
                       cwd=store, check=True)
        trees.append(tree)
    plan = build_plan(target, trees, edits)
    plan["timestamp"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (stage / "plan.json").write_bytes(encoded(plan))
    for name, item in plan["writes"].items():
        if item["text"] is not None:
            path = safe(stage / "candidate", name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(item["text"].encode("utf-8"))
            path.chmod(item["mode"])
    return plan


def apply(stage, review_path, approval_path):
    plan_bytes = (stage / "plan.json").read_bytes()
    plan = json.loads(plan_bytes)
    review_bytes = review_path.read_bytes()
    review, approval = json.loads(review_bytes), json.loads(approval_path.read_bytes())
    require(not plan["conflicts"], "resolve structural conflicts and prepare again")
    require(review["plan_sha256"] == approval["plan_sha256"] == digest(plan_bytes), "stale review/approval")
    require(approval["review_sha256"] == digest(review_bytes), "review changed after ruling")
    require(review["reviewer"] and approval["human"] and approval["gate"] and approval["go"] is True,
            "independent read and explicit human go required")
    ids = []
    for finding in review["findings"]:
        require(all(finding.get(k) for k in ("id", "file", "staged_file", "claim")) and
                type(finding.get("line")) is int and finding["line"] > 0 and
                type(finding.get("staged_line")) is int and finding["staged_line"] > 0,
                "contradiction needs file/line citations in both trees")
        ids.append(finding["id"])
    require(len(ids) == len(set(ids)) and set(ids) == set(approval["rulings"]) and
            all(isinstance(v, str) and v.strip() for v in approval["rulings"].values()),
            "human ruling required for every contradiction")
    target = pathlib.Path(plan["target"])
    require(inventory(target) == plan["inventory"], "target changed since review; prepare again")
    # Validate every destination before the first write, including the report.
    report_name = "docs/fiducial-adoption-" + plan["timestamp"] + ".md"
    report_path = safe(target, report_name)
    require(not plan["writes"] or not report_path.exists(), "report timestamp already used")
    if not plan["writes"]:
        return []
    for name, item in [*plan["writes"].items(), (report_name, {"text": ""})]:
        path = safe(target, name)
        require(not path.is_dir(), name + " is a directory")
        if path.exists() and item["text"] is not None:
            require(os.access(path, os.W_OK), "no write permission on " + name)
            continue
        anchor = path.parent
        while not anchor.exists():
            anchor = anchor.parent
        require(anchor.is_dir() and os.access(anchor, os.W_OK | os.X_OK),
                "no write and search permission on " + str(anchor.relative_to(target) or ".") + " for " + name)
    report = ("# Fiducial adoption\n\nEvidence class: contract-verified. Claude Code /context and Codex hook trust: "
              "not live-verified by this procedure.\n\nChanged paths:\n\n" +
              "\n".join("- `" + n + "`" for n in sorted(plan["writes"])) +
              "\n\n## Inventory\n\n```json\n" + encoded(plan["inventory"]).decode() +
              "```\n\n## Independent contradiction read\n\n```json\n" + review_bytes.decode() +
              "\n```\n\n## Human rulings\n\n```json\n" + encoded(approval).decode() +
              "```\n\n## Exact legacy edits\n\n```json\n" + encoded(plan["edits"]).decode() + "```\n")
    for name, item in plan["writes"].items():
        path = safe(target, name)
        if item["text"] is None:
            path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(item["text"].encode("utf-8"))
            path.chmod(item["mode"])
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    return sorted(plan["writes"])


def labels(repo, run=subprocess.run):
    require(re.fullmatch(r"[\w.-]+/[\w.-]+", repo), "expected OWNER/REPO")
    def names():
        return set(run(["gh", "api", "--paginate", "repos/" + repo + "/labels", "--jq", ".[].name"],
                       check=True, text=True, capture_output=True).stdout.splitlines())
    existing = names()
    for name in LABELS:
        if name not in existing:
            run(["gh", "api", "--method", "POST", "repos/" + repo + "/labels",
                 "-f", "name=" + name, "-f", "color=6e7781"], check=True, text=True, capture_output=True)
    require(set(LABELS) <= names(), "label read-back incomplete")


if __name__ == "__main__":
    try:
        command, *args = sys.argv[1:]
        if command == "prepare" and len(args) in (3, 4):
            edits = json.loads(pathlib.Path(args[3]).read_text()) if len(args) == 4 else []
            plan = prepare(*(pathlib.Path(a).resolve() for a in args[:3]), edits=edits)
            print(json.dumps({"conflicts": plan["conflicts"], "changed_paths": sorted(plan["writes"])}))
        elif command == "apply" and len(args) == 3:
            print(json.dumps(apply(*(pathlib.Path(a).resolve() for a in args))))
        elif command == "labels" and len(args) == 1:
            labels(args[0])
        else:
            raise ValueError("usage: prepare STORE TARGET STAGE [EDITS_JSON] | apply STAGE REVIEW_JSON APPROVAL_JSON | labels OWNER/REPO")
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print("adopt: " + str(exc), file=sys.stderr)
        sys.exit(2)
```

Provenance: DEC-001100 (supersedes DEC-000910), DEC-001280; SPEC.md §§3.1, 6, 7;
subtraction plan §5; retained judgment cited above and R0030, R0196, R0462, R1617.
