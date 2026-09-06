#!/usr/bin/env python3
"""Skeptic probes over the rule-store bundle tool.

Companion to `reviews/bundle-tool-skeptic-20260906T150000Z.md`, which states
what each probe found and what follows from it. Run it from the repository
root:

    python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py

Stdlib only, no arguments, no writes outside a temporary directory it makes and
removes. Every git repository it needs it builds itself with real `git`, for the
reason `bin/tests/helpers.py` gives: a blob SHA and a `HEAD`-against-
`origin/main` comparison are git objects and cannot be mocked into existence.

The probes answer, in order, the six questions the review directive
`docs/cycles/bundle-tool-review-20260906T150000Z.md` names:

  (a) the red-gate     — did the five sampled tests fail on their own assertion?
  (b) the boundary     — is AC-RS-4 enforced, or defeated by a rename?
  (c) the sync refusal — what does `--where` do ahead, behind, and dirty?
  (d) definitions      — a term inside a longer word; a phrase across a wrap.
  (e) the header       — is the blob HEAD's, or the working tree's?
  (f) the untouched    — no frontmatter, a quoted comma, `### Human`, a
                         rule/process id collision.
  (g) the pre-existing — what the AC-X-* cross-cutting scans still cover once
                         `bin/bundle` is the rule-store command.

Each probe prints its observations and appends one PASS/FAIL/NOTE line to the
summary printed last. FAIL means the probe demonstrated the defect the review
reports; it is not a failure of this script.
"""

from __future__ import annotations

import ast
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
BIN = REPO / "bin"
PACKAGE = BIN / "rulestore"
RED_LOG = BIN / "tests" / "red-run-rulestore.log"

sys.path.insert(0, str(BIN))

from rulestore import query, render, terms  # noqa: E402
from rulestore.store import (  # noqa: E402
    FileRowSource,
    Row,
    RowShapeError,
    normalize_fields,
)

SUMMARY = []


def note(tag, verdict, text):
    SUMMARY.append("%s %-4s %s" % (tag, verdict, text))


def head(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def git(cwd, *args, check=True):
    env = dict(os.environ)
    env.update(
        GIT_CONFIG_GLOBAL=os.devnull,
        GIT_CONFIG_SYSTEM=os.devnull,
        GIT_AUTHOR_NAME="Probe",
        GIT_AUTHOR_EMAIL="probe@example.invalid",
        GIT_COMMITTER_NAME="Probe",
        GIT_COMMITTER_EMAIL="probe@example.invalid",
        GIT_TERMINAL_PROMPT="0",
    )
    proc = subprocess.run(
        ["git", *args], cwd=str(cwd), env=env, capture_output=True, text=True
    )
    if check and proc.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), proc.stderr))
    return proc


def bundle(cwd, *args):
    """`bin/bundle` as a subprocess, as a user would run it."""
    env = dict(os.environ)
    env.update(HOME=str(cwd), GIT_TERMINAL_PROMPT="0")
    proc = subprocess.run(
        [sys.executable, str(BIN / "bundle"), *args],
        cwd=str(cwd), env=env, capture_output=True, text=True, timeout=120,
    )
    return proc.returncode, proc.stdout, proc.stderr


def row(row_id, body, *, kind="rule", path=None, blob="0" * 40, **keys):
    return Row(
        id=row_id, body=body, human=None, keys=keys, order=None, kind=kind,
        path=path if path is not None else "rules/%s.md" % row_id, blob=blob,
    )


def write(root, relpath, text):
    dest = pathlib.Path(root) / relpath
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    return dest


# ---------------------------------------------------------------- the store

STORE = {
    "rules/R0001.md": (
        "---\nid: R0001\norder: 10\ntopic: [core]\nrole: [writer]\n"
        "session: [decision]\ncorpus: [writing]\nverb: require\nterm: null\n---\n\n"
        "Open one tranche per delta, and close it at the end.\n\n"
        "## Human\n\nDEC-000170: the branch is the state.\n"
    ),
    "rules/R0100.md": (
        "---\nid: R0100\norder: 20\ntopic: [lexicon]\nverb: define\n"
        "term: [tranche, tranches]\n---\n\n"
        "A tranche is one concurrent workstream of build work.\n"
    ),
    "process/change-flow.md": (
        "---\norder: 30\nrole: [writer]\nsession: [decision]\ncorpus: [writing]\n"
        "---\n\n# Change flow\n\nEvery pull request gets an agentic code review.\n"
    ),
}


def make_store_repo(parent, files=None):
    """`(origin, clone)` — a bare origin and a clone level with it."""
    origin = parent / "origin.git"
    git(parent, "init", "--bare", "-q", "-b", "main", str(origin))
    seed = parent / "seed"
    seed.mkdir()
    git(seed, "init", "-q", "-b", "main")
    git(seed, "config", "commit.gpgsign", "false")
    for relpath, text in (STORE if files is None else files).items():
        write(seed, relpath, text)
    git(seed, "add", "-A")
    git(seed, "commit", "-q", "-m", "store: the probe rows")
    git(seed, "remote", "add", "origin", str(origin))
    git(seed, "push", "-q", "origin", "main")
    clone = parent / "clone"
    git(parent, "clone", "-q", str(origin), str(clone))
    git(clone, "config", "user.email", "probe@example.invalid")
    git(clone, "config", "user.name", "Probe")
    git(clone, "config", "commit.gpgsign", "false")
    return origin, clone


# ------------------------------------------------------------------ probe a


#: Five tests sampled across the four new files and four different modules.
SAMPLED = [
    "test_ac_rs_2_result_is_ordered_by_order_then_topic_then_id",
    "test_ac_rs_13_a_definition_is_never_added_twice",
    "test_ac_rs_14_the_human_form_is_carried_on_the_row_and_never_rendered",
    "test_ac_rs_4_no_processing_module_names_a_storage_path",
    "test_ac_rs_6_a_query_writes_exactly_one_file_under_the_ruled_name",
]


def probe_a():
    head("(a) THE RED-GATE — did the sampled tests fail on their own assertion?")
    if not RED_LOG.is_file():
        note("(a)", "NOTE", "red log absent; not run")
        return
    text = RED_LOG.read_text(encoding="utf-8", errors="replace")
    blocks = re.split(r"^={70}$", text, flags=re.M)
    clean = True
    for name in SAMPLED:
        block = next((b for b in blocks if re.search(r"^FAIL: %s " % re.escape(name), b, re.M)), None)
        if block is None:
            print("  %-70s NOT FOUND in the red log" % name)
            clean = False
            continue
        last_frame = re.findall(r'^  File "([^"]+)", line (\d+), in (\S+)', block, re.M)
        error = re.search(r"^(\w+Error): (.*)$", block, re.M)
        kind = error.group(1) if error else "(no error line)"
        origin = last_frame[-1][0].rsplit("/", 1)[-1] if last_frame else "(no frame)"
        ok = kind == "AssertionError" and origin.startswith(("test_", "helpers"))
        clean = clean and ok
        print("  %s" % name)
        print("      error: %-16s raised in: %-28s -> %s"
              % (kind, origin, "own assertion" if ok else "SCAFFOLDING"))
        if error:
            print("      claim: %s" % error.group(2).strip()[:100])
    total_fail = len(re.findall(r"^FAIL: ", text, flags=re.M))
    total_err = len(re.findall(r"^ERROR: ", text, flags=re.M))
    total_assert = len(re.findall(r"^AssertionError", text, flags=re.M))
    print()
    print("  whole log: FAIL=%d ERROR=%d AssertionError=%d" % (total_fail, total_err, total_assert))
    note("(a)", "PASS" if clean and total_err == 0 else "FAIL",
         "5/5 sampled tests failed on their own assertion; log has %d FAIL, %d ERROR"
         % (total_fail, total_err))


# ------------------------------------------------------------------ probe b

#: A processing module that reaches the filesystem while passing every one of
#: the eight checks in `bin/tests/test_rulestore_boundary.py`. It never writes
#: the literals the scan looks for and never uses a `from ... import` the scan
#: inspects.
EVASION = '''"""A processing module that quietly reads the store."""

import rulestore.store

ROOT_NAMES = ("rul" "es/", "proc" "ess/")


def leak(root):
    """Everything AC-RS-4 says a processing module must never be able to do."""
    return rulestore.store.FileRowSource(root).rows()
'''


def _boundary_checks(source, name="query.py"):
    """The eight checks `test_rulestore_boundary.py` makes, over one source."""
    forbidden = {"os", "pathlib", "glob", "io", "subprocess"}
    storage_paths = ("rules/", "process/")
    allowed_store_names = {"Row", "RowSource"}
    tree = ast.parse(source, filename=name)
    imports = set()
    from_store = set()
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                imports.add(node.module.split(".")[0])
            module = node.module or ""
            if (node.level == 0 and module in ("rulestore.store", "store")) or (
                node.level > 0 and module == "store"
            ):
                from_store.update(alias.name for alias in node.names)
        elif isinstance(node, ast.Call):
            func = node.func
            called = getattr(func, "id", None) or getattr(func, "attr", None)
            if called in ("open", "read_text", "read_bytes", "rglob", "glob",
                          "iterdir", "walk", "listdir"):
                calls.append(called)
    return {
        "imports a filesystem module": sorted(imports & forbidden),
        "names a storage path": [p for p in storage_paths if p in source],
        "takes more than Row/RowSource from store": sorted(from_store - allowed_store_names),
        "calls a file-opening name": calls,
        "imports outside stdlib+rulestore": sorted(
            n for n in imports if n not in set(sys.stdlib_module_names) | {"rulestore"}
        ),
    }


def probe_b():
    head("(b) THE STORAGE BOUNDARY — is AC-RS-4 enforced, or only string-scanned?")
    print("  The candidate processing module under scan:")
    for line in EVASION.strip().splitlines():
        print("      | %s" % line)
    print()
    results = _boundary_checks(EVASION)
    for check, offenders in results.items():
        print("      %-42s -> %s" % (check, offenders or "clean"))
    caught = any(results.values())
    print()
    print("  every boundary check passes on this module: %s" % (not caught))
    print("  and yet it reads the store: leak(root) -> FileRowSource(root).rows()")
    print()
    print("  A rename also defeats the literal scan. `STORAGE_PATHS` is the pair")
    print("  ('rules/', 'process/'); rename either root and the scan asserts nothing,")
    print("  and `test_ac_rs_4_store_is_the_only_module_that_names_a_storage_path`")
    print("  fails on store.py rather than catching a processing module.")
    note("(b)", "FAIL" if not caught else "PASS",
         "AC-RS-4 is defeated by `import rulestore.store` + a split string literal")


# ------------------------------------------------------------------ probe c

def probe_c():
    head("(c) THE SYNC REFUSAL — --where against ahead, behind, and dirty")
    parent = pathlib.Path(tempfile.mkdtemp(prefix="probe-sync-"))
    try:
        results = {}

        # level and clean — the control
        _origin, clone = make_store_repo(parent / "level" if False else parent)
        out = parent / "out"
        out.mkdir()
        code, stdout, stderr = bundle(clone, "--where", "role=writer", "--out", str(out))
        results["level and clean"] = (code, stderr.strip() or stdout.strip())

        # equal but dirty
        (clone / "rules/R0001.md").write_text(
            (clone / "rules/R0001.md").read_text() + "\nAn uncommitted line.\n",
            encoding="utf-8",
        )
        code, stdout, stderr = bundle(clone, "--where", "role=writer", "--out", str(out))
        results["equal but dirty"] = (code, stderr.strip() or stdout.strip())
        git(clone, "checkout", "--", "rules/R0001.md")

        # one commit ahead of origin/main
        write(clone, "rules/R0002.md",
              "---\nid: R0002\norder: 40\ntopic: [core]\nrole: [writer]\n"
              "verb: require\nterm: null\n---\n\nA later rule.\n")
        git(clone, "add", "-A")
        git(clone, "commit", "-q", "-m", "store: a later rule")
        code, stdout, stderr = bundle(clone, "--where", "role=writer", "--out", str(out))
        results["one commit ahead"] = (code, stderr.strip() or stdout.strip())

        # one commit behind origin/main
        git(clone, "push", "-q", "origin", "main")
        git(clone, "reset", "--hard", "-q", "HEAD~1")
        code, stdout, stderr = bundle(clone, "--where", "role=writer", "--out", str(out))
        results["one commit behind"] = (code, stderr.strip() or stdout.strip())

        for state, (code, message) in results.items():
            print("      %-18s exit %-2s  %s" % (state, code, message))
        wrote = sorted(p.name for p in out.iterdir())
        print()
        print("      files written across all four states: %s" % (wrote or "none"))

        refused = all(results[s][0] == 2 for s in
                      ("equal but dirty", "one commit ahead", "one commit behind"))
        allowed = results["level and clean"][0] == 0
        note("(c)", "PASS" if refused and allowed else "FAIL",
             "ahead/behind/dirty all refuse exit 2 with one line; level+clean writes one file")
    finally:
        shutil.rmtree(parent, ignore_errors=True)


# ------------------------------------------------------------------ probe d

def probe_d():
    head("(d) DEFINITIONS BY TERM — a longer word, and a phrase across a wrap")
    d_row = row("R0900", "A row is one obligation.", term=["row"])
    cases = [
        ("term inside a longer word", "A rowdy meeting settles nothing.", []),
        ("term as a plural (rows)", "Two rows disagree.", []),
        ("term after a hyphen", "A row-by-row read.", ["R0900"]),
        ("term as itself", "One row per obligation.", ["R0900"]),
    ]
    for label, body, expected in cases:
        selected = [row("R0100", body)]
        got = [r.id for r in terms.pull_definitions(selected, selected + [d_row])]
        print("      %-28s %-34r -> %s %s"
              % (label, body, got or "[]", "" if got == expected else "(UNEXPECTED)"))

    print()
    phrase = row("R0902", "A spec delta is an open change.", term=["spec delta"])
    wrapped = [
        ("one line", "While a spec delta is open, edit freely."),
        ("wrapped at the space", "While a spec\ndelta is open, edit freely."),
        ("two spaces", "While a spec  delta is open, edit freely."),
    ]
    for label, body in wrapped:
        selected = [row("R0101", body)]
        got = [r.id for r in terms.pull_definitions(selected, selected + [phrase])]
        print("      %-22s -> %s" % (label, got or "[] NOT PULLED"))

    print()
    print("  The same question asked of the real store:")
    rows = FileRowSource(REPO).rows()
    definitions = [r for r in rows if terms.is_definition(r)]
    missed = []
    for r in rows:
        body = r.body or ""
        flat = re.sub(r"\s+", " ", body)
        for d in definitions:
            if d.id == r.id:
                continue
            for term in d.keys.get("term") or []:
                if " " not in term:
                    continue
                as_written = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(term), re.I)
                unwrapped = re.compile(
                    r"(?<!\w)%s(?!\w)" % re.escape(re.sub(r"\s+", " ", term)), re.I
                )
                if unwrapped.search(flat) and not as_written.search(body):
                    missed.append((r.id, d.id, term))
    print("      rows: %d   definitions: %d   multi-word terms: %d"
          % (len(rows), len(definitions),
             sum(1 for d in definitions for t in d.keys["term"] if " " in t)))
    print("      real rows whose phrase-term use is missed because the body wraps: %d"
          % len(missed))
    for r_id, d_id, term in missed:
        print("          row %-16s misses definition %-8s on term %r" % (r_id, d_id, term))
    note("(d)", "FAIL" if missed else "PASS",
         "whole-word matching is right; a phrase across a line break is missed "
         "(%d real rows lose a definition)" % len(missed))


# ------------------------------------------------------------------ probe e

def probe_e():
    head("(e) THE HEADER — is every blob HEAD's blob, or the working tree's?")
    parent = pathlib.Path(tempfile.mkdtemp(prefix="probe-blob-"))
    try:
        _origin, clone = make_store_repo(parent)
        committed = git(clone, "rev-parse", "HEAD:rules/R0001.md").stdout.strip()
        before = FileRowSource(clone).rows()
        r_before = next(r for r in before if r.path == "rules/R0001.md")

        (clone / "rules/R0001.md").write_text(
            (clone / "rules/R0001.md").read_text().replace(
                "Open one tranche per delta, and close it at the end.",
                "AN UNCOMMITTED EDIT.",
            ),
            encoding="utf-8",
        )
        worktree_blob = git(clone, "hash-object", "rules/R0001.md").stdout.strip()
        after = FileRowSource(clone).rows()
        r_after = next(r for r in after if r.path == "rules/R0001.md")

        print("      blob at HEAD                     %s" % committed)
        print("      blob of the working-tree file    %s" % worktree_blob)
        print("      row.blob before the edit         %s" % r_before.blob)
        print("      row.blob after the edit          %s" % r_after.blob)
        print("      row.body after the edit          %r" % r_after.body)
        print()
        blob_is_head = r_after.blob == committed
        body_is_worktree = "UNCOMMITTED" in (r_after.body or "")
        print("      blob follows HEAD:        %s" % blob_is_head)
        print("      body follows working tree: %s" % body_is_worktree)
        print()
        print("      So the header's blob and the rendered body can name different")
        print("      content. --where refuses a dirty rules/ or process/ tree, which")
        print("      closes the gap for the written bundle; nothing closes it for a")
        print("      caller of FileRowSource, and the dirty check is a `git status`")
        print("      pathspec, so a .gitignore'd file under rules/ is invisible to it.")
        note("(e)", "NOTE" if blob_is_head and body_is_worktree else "PASS",
             "blob is HEAD's, body is the working tree's; only the --where "
             "refusal keeps them consistent")
    finally:
        shutil.rmtree(parent, ignore_errors=True)


# ------------------------------------------------------------------ probe f

def probe_f():
    head("(f) WHAT THE TESTS NEVER TOUCH")

    print("  f1 — a rules/ file with no frontmatter")
    parent = pathlib.Path(tempfile.mkdtemp(prefix="probe-f1-"))
    try:
        files = dict(STORE)
        files["rules/R0777.md"] = "Just prose, and no frontmatter at all.\n"
        _origin, clone = make_store_repo(parent, files=files)
        rows = FileRowSource(clone).rows()
        orphan = next(r for r in rows if r.path == "rules/R0777.md")
        print("      returned: id=%r keys=%r order=%r" % (orphan.id, orphan.keys, orphan.order))
        print("      -> accepted silently; the id falls back to the path stem, and the")
        print("         row is unselectable by any key while still counting as a row.")
        f1_defect = orphan.keys == {} and orphan.id == "R0777"
    finally:
        shutil.rmtree(parent, ignore_errors=True)

    print()
    print("  f2 — a value containing a comma inside quotes")
    got, _order = normalize_fields("R0002", {"topic": '["a, b", c]'})
    print("      topic: [\"a, b\", c]  ->  %r" % got)
    scalar, _order = normalize_fields("R0003", {"note": '"one, two"'})
    print("      note: \"one, two\"     ->  %r" % scalar)
    f2_defect = got.get("topic") != ["a, b", "c"]
    print("      -> the bracket branch splits on every comma before quotes come off,")
    print("         so the quoted value is torn in two and both halves keep a quote.")

    print()
    print("  f3 — a `## Human` heading at a different level")
    parent = pathlib.Path(tempfile.mkdtemp(prefix="probe-f3-"))
    try:
        files = dict(STORE)
        files["rules/R0778.md"] = (
            "---\nid: R0778\norder: 60\ntopic: [core]\nrole: [writer]\n"
            "verb: require\nterm: null\n---\n\nThe obligation.\n\n"
            "### Human\n\nDEC-000999: the rationale nobody should see.\n"
        )
        _origin, clone = make_store_repo(parent, files=files)
        rows = FileRowSource(clone).rows()
        mis = next(r for r in rows if r.path == "rules/R0778.md")
        print("      human: %r" % mis.human)
        print("      body:  %r" % mis.body)
        text = render.render([mis], [], repo="probe", head="0" * 40, generated="20260906T150000Z")
        leaked = "DEC-000999" in text
        print("      the rationale reaches the rendered bundle: %s" % leaked)
        print("      -> AC-RS-14 holds only for the exact string '## Human'; one wrong")
        print("         heading level publishes the human form to an agent.")
        f3_defect = leaked
    finally:
        shutil.rmtree(parent, ignore_errors=True)

    print()
    print("  f4 — an id collision between a rule and a process stem")
    parent = pathlib.Path(tempfile.mkdtemp(prefix="probe-f4-"))
    try:
        files = dict(STORE)
        files["process/R0001.md"] = (
            "---\norder: 15\nrole: [writer]\nsession: [decision]\ncorpus: [writing]\n"
            "---\n\n# A process document whose stem collides with a rule id.\n"
        )
        _origin, clone = make_store_repo(parent, files=files)
        rows = FileRowSource(clone).rows()
        colliding = [r for r in rows if r.id == "R0001"]
        print("      rows sharing id 'R0001': %s"
              % [(r.kind, r.path) for r in colliding])
        selected = query.select(rows, {"role": "writer"})
        print("      both selected: %s" % [(r.kind, r.id) for r in selected])
        # the dedupe that keys on id
        definition = row("R0100", "A tranche is one workstream.", term=["tranche"])
        pulled = terms.pull_definitions(selected, rows)
        print("      pull_definitions dedupes on row.id; selected ids seen as: %s"
              % sorted({r.id for r in selected}))
        collide_defect = len(colliding) > 1 and len({r.id for r in selected}) < len(selected)
        print("      -> `pull_definitions` builds `already = {row.id for row in selected}`,")
        print("         so a definition whose id equals a colliding process stem is")
        print("         suppressed, and `--near` prints an ambiguous first column.")
        f4_defect = collide_defect
    finally:
        shutil.rmtree(parent, ignore_errors=True)

    defects = [name for name, bad in
               (("no-frontmatter accepted", f1_defect),
                ("quoted comma torn", f2_defect),
                ("### Human leaks", f3_defect),
                ("id collision unguarded", f4_defect)) if bad]
    note("(f)", "FAIL" if defects else "PASS",
         "untested cases that misbehave: %s" % (", ".join(defects) or "none"))


# ------------------------------------------------------------------ probe g

def probe_g():
    head("(g) THE PRE-EXISTING CROSS-CUTTING SCANS — what still covers bin/bundle?")

    print("  g1 — the argv AC-X-4/6/7 run `bundle` with")
    helpers = (BIN / "tests" / "helpers.py").read_text(encoding="utf-8")
    argv = re.search(r'"bundle": (\[[^\]]*\])', helpers)
    print("      helpers.CLI_MINIMAL_ARGS['bundle'] = %s" % (argv.group(1) if argv else "?"))
    print("      (its comment: \"Minimal argv that gets each CLI past argparse\")")
    outside = pathlib.Path(tempfile.mkdtemp(prefix="probe-outside-"))
    try:
        code, out, err = bundle(outside, "base")
        print("      `bundle base` outside a repo -> exit %s, %r"
              % (code, (err.strip().splitlines() or [""])[-1]))
        print("      -> it dies AT argparse, never reaching the repo, file or encoding")
        print("         work AC-X-4, AC-X-6 and AC-X-7 exist to exercise.")

        print()
        print("  g2 — what those ACs would have caught with a live argv")
        for args in (("--keys",), ("--near", "anything")):
            code, out, err = bundle(outside, *args)
            print("      `bundle %-16s` outside a repo -> exit %s, stdout %r, stderr %r"
                  % (" ".join(args), code, out.strip(), err.strip()))
        print("      -> AC-X-4 requires exit 2 or 3 outside a repository. Both modes")
        print("         exit 0 in silence: `_repo_root()` falls back to the cwd and")
        print("         `FileRowSource` finds no rules/ directory there.")
        acx4_violated = bundle(outside, "--keys")[0] == 0
    finally:
        shutil.rmtree(outside, ignore_errors=True)

    print()
    print("  g3 — which files the AC-X-1/2/7 static scans read")
    scanned = sorted(p.name for p in BIN.iterdir() if p.is_file() and not p.name.startswith("."))
    scanned += sorted("aimeta/%s" % p.name for p in (BIN / "aimeta").glob("*.py"))
    package = sorted("rulestore/%s" % p.name for p in PACKAGE.glob("*.py"))
    print("      production_files() covers %d files under bin/ and bin/aimeta/" % len(scanned))
    print("      bin/rulestore/ files it covers: %s"
          % ([n for n in package if n in scanned] or "none"))
    print("      -> the new package is outside every AC-X static scan, and bin/bundle")
    print("         reaches it through importlib, so the module graph AC-X-2 reads")
    print("         no longer includes the code that does the work.")

    note("(g)", "FAIL" if acx4_violated else "PASS",
         "AC-X-4 is violated by --keys/--near (exit 0 outside a repo) and hidden "
         "by a stale argv; bin/rulestore/ is outside every AC-X scan")


def main():
    print("Skeptic probes — bundle-tool-review-20260906T150000Z")
    print("repository: %s" % REPO)
    probe_a()
    probe_b()
    probe_c()
    probe_d()
    probe_e()
    probe_f()
    probe_g()
    print()
    print("SUMMARY (FAIL = the probe demonstrated the defect the review reports)")
    for line in SUMMARY:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
