"""Shared fixtures and helpers for the Package A test suite.

Design constraints (see `docs/packages/package-a-spec.md` §5):

- **No mocked git.** Every git interaction in this suite runs against a real
  repository created with `git init` in a throwaway temp directory.
- **Isolated environment.** Subprocesses never inherit the developer's
  `AI_METHODOLOGY_HOME`, global git config, or global hooks.
- **Stdlib only.**

This module is test scaffolding, not production code: it is the one place in
`bin/` that is allowed to know where the methodology repo lives, and AC-X-1's
absolute-path scan deliberately excludes `bin/tests/`.
"""

from __future__ import annotations

import atexit
import os
import pathlib
import re
import shutil
import subprocess
import tempfile

# bin/tests/helpers.py -> bin/tests -> bin -> <repo root>. Derived, never
# hardcoded, so the suite moves with the repo.
TESTS_DIR = pathlib.Path(__file__).resolve().parent
BIN_DIR = TESTS_DIR.parent
REPO_ROOT = BIN_DIR.parent

POLICY_RELPATH = "policies/document-metadata-policy.md"
DISPOSITION_RELPATH = "reviews/frontmatter-disposition.md"

CLI_NAMES = [
    "check-frontmatter",
    "flip-agreed",
    "cycle-open",
    "bundle",
    "migrate-frontmatter",
    "install-hooks",
    "directive",
    "check-directive",
]

#: Minimal argv that gets each CLI past argparse, for tests that only care
#: about environmental preconditions (e.g. AC-X-4, "run outside a repo").
CLI_MINIMAL_ARGS = {
    "check-frontmatter": ["--all"],
    "flip-agreed": ["policies/x.md", "--review", "reviews/r.md @ abc1234"],
    "cycle-open": ["--cycle", "1"],
    "bundle": ["base"],
    "migrate-frontmatter": ["--plan"],
    "install-hooks": [],
    "directive": ["--descriptor", "x", "--title", "T"],
    "check-directive": ["docs/cycles/x-20260828T170000.md"],
}

REAL_POLICY_TEXT = (REPO_ROOT / POLICY_RELPATH).read_text()

DEFAULT_ROLE_SLUGS = (
    "coder-agent",
    "test-designer-agent",
    "reviewer-agent",
    "architect-agent",
)

_SESSION_HOME = None


# ---------------------------------------------------------------- temp dirs


def _session_home():
    """A process-wide throwaway `$HOME`, so global git config cannot leak in."""
    global _SESSION_HOME
    if _SESSION_HOME is None:
        _SESSION_HOME = tempfile.mkdtemp(prefix="aimeta-session-home-")
        atexit.register(shutil.rmtree, _SESSION_HOME, ignore_errors=True)
    return _SESSION_HOME


def temp_dir(case, prefix="aimeta-"):
    """Create a temp directory and register its removal with `case`."""
    path = pathlib.Path(tempfile.mkdtemp(prefix=prefix))
    case.addCleanup(shutil.rmtree, str(path), ignore_errors=True)
    return path


# ---------------------------------------------------------------- environment


def base_env(methodology_home=None, home=None, **overrides):
    """A subprocess environment scrubbed of anything that could skew results.

    Drops every inherited `GIT_*` var and `AI_METHODOLOGY_HOME`; pins `HOME`
    to a throwaway dir; disables system and global git config so the
    developer's `core.hooksPath` or identity cannot influence a test.
    """
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.pop("AI_METHODOLOGY_HOME", None)
    env["HOME"] = str(home or _session_home())
    env["GIT_CONFIG_NOSYSTEM"] = "1"
    env["GIT_CONFIG_GLOBAL"] = os.devnull
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["LC_ALL"] = "C"
    if methodology_home is not None:
        env["AI_METHODOLOGY_HOME"] = str(methodology_home)
    for key, value in overrides.items():
        if value is None:
            env.pop(key, None)
        else:
            env[key] = str(value)
    return env


# ---------------------------------------------------------------- git plumbing


def git(repo, *args, env=None, check=False, timeout=60):
    """Run git in `repo`. Returns `(returncode, stdout, stderr)`."""
    proc = subprocess.run(
        ["git", *[str(a) for a in args]],
        cwd=str(repo),
        env=env or base_env(),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if check and proc.returncode != 0:
        raise AssertionError(
            "git %s failed in %s: %s" % (" ".join(map(str, args)), repo, proc.stderr)
        )
    return proc.returncode, proc.stdout, proc.stderr


def make_repo(case, name="proj", parent=None, env=None):
    """A real, empty git repo on branch `main`, with a local identity.

    `parent` lets a test control the repo's *sibling* directory layout, which
    AC-RP-2's `<parent>/ai` fallback needs.
    """
    parent = pathlib.Path(parent) if parent is not None else temp_dir(case, "aimeta-work-")
    root = parent / name
    root.mkdir(parents=True, exist_ok=True)
    env = env or base_env()
    git(root, "init", "-q", "-b", "main", env=env, check=True)
    git(root, "config", "user.email", "tests@example.invalid", env=env, check=True)
    git(root, "config", "user.name", "AI Methodology Tests", env=env, check=True)
    git(root, "config", "commit.gpgsign", "false", env=env, check=True)
    return root


def write(repo, relpath, text):
    """Write `text` to `repo/relpath`, creating parent directories."""
    path = pathlib.Path(repo) / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def read(repo, relpath):
    """Read `repo/relpath` as text."""
    return (pathlib.Path(repo) / relpath).read_text()


def write_bytes(repo, relpath, data):
    """Write raw bytes — for fixtures that must not be valid UTF-8 (AC-CF-14)."""
    path = pathlib.Path(repo) / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def read_bytes(repo, relpath):
    """Read `repo/relpath` as raw bytes."""
    return (pathlib.Path(repo) / relpath).read_bytes()


def git_bytes(repo, *args, env=None, timeout=60):
    """Run git and return raw stdout bytes, for blob content that may not decode."""
    proc = subprocess.run(
        ["git", *[str(a) for a in args]],
        cwd=str(repo),
        env=env or base_env(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )
    return proc.returncode, proc.stdout, proc.stderr.decode("utf-8", "replace")


def blob_bytes(repo, spec, env=None):
    """`git cat-file blob <spec>` as bytes — e.g. `":policies/x.md"` for the index."""
    rc, out, err = git_bytes(repo, "cat-file", "blob", spec, env=env)
    if rc != 0:
        raise AssertionError("git cat-file blob %s failed: %s" % (spec, err))
    return out


def stage(repo, *paths, env=None):
    """`git add` the given paths (or everything when none are given)."""
    env = env or base_env()
    args = ["add", "--"] + list(paths) if paths else ["add", "-A"]
    git(repo, *args, env=env, check=True)


def commit(repo, message, *paths, env=None):
    """Stage `paths` (or everything) and commit. Returns the full SHA."""
    env = env or base_env()
    stage(repo, *paths, env=env)
    git(repo, "commit", "-q", "--no-verify", "-m", message, env=env, check=True)
    return git(repo, "rev-parse", "HEAD", env=env, check=True)[1].strip()


def head_sha(repo, env=None):
    return git(repo, "rev-parse", "HEAD", env=env or base_env(), check=True)[1].strip()


def show(repo, rev_and_path, env=None):
    """`git show <rev>:<path>` — e.g. `show(r, ":policies/x.md")` for the index."""
    rc, out, err = git(repo, "show", rev_and_path, env=env or base_env())
    if rc != 0:
        raise AssertionError("git show %s failed: %s" % (rev_and_path, err))
    return out


def commit_paths(repo, rev="HEAD", env=None):
    """Sorted list of paths touched by a commit."""
    rc, out, err = git(
        repo,
        "show",
        "--pretty=format:",
        "--name-only",
        rev,
        env=env or base_env(),
        check=True,
    )
    return sorted(p for p in out.splitlines() if p.strip())


def commit_count(repo, env=None):
    rc, out, _ = git(repo, "rev-list", "--count", "HEAD", env=env or base_env())
    return int(out.strip()) if rc == 0 else 0


def porcelain(repo, env=None):
    return git(repo, "status", "--porcelain", env=env or base_env(), check=True)[1]


# ---------------------------------------------------------------- methodology home


def make_home(case, policy_text=None, roles=DEFAULT_ROLE_SLUGS, parent=None, name="ai",
              git_init=True):
    """A temp methodology home: a policy, roles, a `bin/` symlink, and a history.

    `bin/` is a **symlink to the real `bin/`**, so the scripts exercised are
    the ones under test, while `policies/document-metadata-policy.md` is a
    copy this test can vary (AC-CF-13).

    TRD §4.1 and §3.9's migration make the home a git repository with
    `skills/directive-invariants.md` committed in it: §3.2 resolves that
    document's revision in the home, so the substrate must give it one.
    `git_init=False` withholds both, for FM-G1's no-committed-body refusal.
    """
    parent = pathlib.Path(parent) if parent is not None else temp_dir(case, "aimeta-home-")
    home = parent / name
    home.mkdir(parents=True, exist_ok=True)
    write(home, POLICY_RELPATH, REAL_POLICY_TEXT if policy_text is None else policy_text)
    for slug in roles:
        write(home, "roles/%s.md" % slug, role_doc(slug))
    link = home / "bin"
    if not link.exists():
        link.symlink_to(BIN_DIR, target_is_directory=True)
    if git_init:
        env = base_env()
        git(home, "init", "-q", "-b", "main", env=env, check=True)
        git(home, "config", "user.email", "tests@example.invalid", env=env, check=True)
        git(home, "config", "user.name", "AI Methodology Tests", env=env, check=True)
        git(home, "config", "commit.gpgsign", "false", env=env, check=True)
        write(home, ".gitignore", "bin\n")
        invariants_doc(home, env=env, message="home: invariants and policy")
    return home


def policy_without(marker_glob, policy_text=None):
    """The real policy text with one in-scope bullet removed (AC-CF-13)."""
    text = REAL_POLICY_TEXT if policy_text is None else policy_text
    return "\n".join(
        line for line in text.splitlines() if line.strip() != "- `%s`" % marker_glob
    ) + "\n"


# ---------------------------------------------------------------- CLI invocation


def run_cli(name, *args, cwd, env=None, methodology_home=None, timeout=90, script_dir=None):
    """Invoke `bin/<name>` as a subprocess through its own shebang.

    CLI behaviour is tested across the process boundary because exit codes are
    part of the contract (spec §2.4).
    """
    script = pathlib.Path(script_dir or BIN_DIR) / name
    proc = subprocess.run(
        [str(script), *[str(a) for a in args]],
        cwd=str(cwd),
        env=env if env is not None else base_env(methodology_home=methodology_home),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return proc.returncode, proc.stdout, proc.stderr


# ---------------------------------------------------------------- assertions


BRACKET_CODE_RE = re.compile(r"\[([a-z][a-z0-9-]*)\]")


def bracket_codes(text):
    """Every bracketed `[code]` in a diagnostic stream.

    Tests assert on codes, never on English wording, so that rewording a
    message does not break the suite.
    """
    return BRACKET_CODE_RE.findall(text or "")


def codes(findings):
    """Codes of a `list[Finding]`, in order."""
    return [f.code for f in findings]


def code_set(findings):
    return set(codes(findings))


def no_traceback(*streams):
    return not any("Traceback (most recent call last)" in (s or "") for s in streams)


DOCUMENTED_EXIT_CODES = (0, 1, 2, 3, 4)


def ascii_env(methodology_home=None, **overrides):
    """An environment whose *default* text encoding is ASCII, not UTF-8.

    A hook spawned by a GUI git client inherits no login shell and can easily
    run under `LC_ALL=C`. Python's PEP 538 locale coercion and PEP 540 UTF-8
    mode both paper over that, so both are disabled here — otherwise the
    platform default never actually becomes ASCII and AC-X-7 cannot fail.
    """
    return base_env(
        methodology_home=methodology_home,
        LC_ALL="C",
        LANG="C",
        PYTHONCOERCECLOCALE="0",
        PYTHONUTF8="0",
        **overrides
    )


def fake_path_dir(case, tools=("git", "dirname"), prefix="aimeta-path-"):
    """A directory of symlinks to exactly `tools` — a deliberately sparse PATH.

    Used by AC-IH-9 to remove `python3` from PATH while leaving the utilities
    the shim itself needs.
    """
    path = temp_dir(case, prefix)
    for tool in tools:
        located = shutil.which(tool)
        if located is None:  # pragma: no cover - environment sanity
            raise AssertionError("cannot build a fake PATH without %s" % tool)
        (path / tool).symlink_to(located)
    return path


def filesystem_is_case_insensitive(path):
    """True when `path`'s filesystem folds case (macOS default, not Linux)."""
    probe = pathlib.Path(path) / "CaseProbe.tmp"
    probe.write_text("probe")
    try:
        return (pathlib.Path(path) / "caseprobe.tmp").exists()
    finally:
        probe.unlink()


def snapshot_tree(root, skip=()):
    """`{relpath: (size, mtime_ns, sha-ish content)}` for a directory tree."""
    root = pathlib.Path(root)
    skip = [pathlib.Path(s).resolve() for s in skip]
    out = {}
    for path in sorted(root.rglob("*")):
        try:
            resolved = path.resolve()
        except OSError:
            continue
        if any(resolved == s or s in resolved.parents for s in skip):
            continue
        if path.is_symlink() or not path.is_file():
            continue
        st = path.stat()
        out[str(path.relative_to(root))] = (st.st_size, st.st_mtime_ns)
    return out


# ---------------------------------------------------------------- doc fixtures


def frontmatter_block(**fields):
    lines = ["---"]
    for key, value in fields.items():
        key = key.replace("_", "-")
        if value is None:
            lines.append("%s: null" % key)
        elif isinstance(value, (list, tuple)):
            lines.append("%s: [%s]" % (key, ", ".join(str(v) for v in value)))
        else:
            lines.append("%s: %s" % (key, value))
    lines.append("---")
    return "\n".join(lines) + "\n"


DEFAULT_BODY = "\n# Sample Document\n\nOriginal body text.\n"
REVIEW_POINTER = "reviews/sample-review.md @ abc1234"


def agreed_doc(body=DEFAULT_BODY, review=REVIEW_POINTER, audience=("all-roles",)):
    """A fully valid `agreed` document (AC-FM-16's shape)."""
    return (
        frontmatter_block(
            status="agreed",
            last_reviewed=review,
            audience=list(audience),
            superseded_by=None,
        )
        + body
    )


def draft_doc(body=DEFAULT_BODY, audience=("all-roles",)):
    return (
        frontmatter_block(
            status="draft",
            last_reviewed=None,
            audience=list(audience),
            superseded_by=None,
        )
        + body
    )


def in_review_doc(body=DEFAULT_BODY, audience=("all-roles",)):
    return (
        frontmatter_block(
            status="in-review",
            last_reviewed=None,
            audience=list(audience),
            superseded_by=None,
        )
        + body
    )


def converging_doc(body=DEFAULT_BODY, audience=("all-roles",)):
    """AC-CV-*: a `converging` document — no `last-reviewed` (DEC-000360)."""
    return (
        frontmatter_block(
            status="converging",
            last_reviewed=None,
            audience=list(audience),
            superseded_by=None,
        )
        + body
    )


def legacy_doc(title="Legacy Document", status_word="stable", body_extra=""):
    """A pre-frontmatter document carrying a body `Status:` line."""
    return "# %s\n\nStatus: %s\n\nSome legacy prose.\n%s" % (title, status_word, body_extra)


def context_set_doc(name, depends_on=(), body=None, status_word=None):
    """A context set carrying composition frontmatter and no lifecycle fields."""
    head = frontmatter_block(
        context_set=name,
        purpose="Purpose of %s." % name,
        include_when="When %s applies." % name,
        depends_on=list(depends_on),
    )
    if body is None:
        body = "\n# Context Set: %s\n\nProse.\n" % name
    if status_word:
        body = "\n# Context Set: %s\n\nStatus: %s\n\nProse.\n" % (name, status_word)
    return head + body


def role_doc(slug):
    return agreed_doc(body="\n# Role: %s\n\nRole prose.\n" % slug)


def disposition_doc(paths):
    lines = ["# Frontmatter grandfather disposition", ""]
    lines += ["- `%s` — agreed before policy adoption" % p for p in paths]
    return "\n".join(lines) + "\n"


def plan_block(path, action="migrate", **fields):
    """One `migrate-frontmatter --plan` block (spec §3.8 format)."""
    lines = ["## `%s`" % path, "- action: %s" % action]
    for key, value in fields.items():
        lines.append("- %s: %s" % (key.replace("_", "-"), value))
    return "\n".join(lines) + "\n"


# ================================================================ directive tooling
#
# Fixture substrate for `bin/directive` and `bin/check-directive`, per
# `specs/directive-tooling-trd.md` §4.1. Everything below is **additive**: no
# existing helper's behaviour changes, so the pre-existing suite is untouched.
#
# Two deviations from §4.1 were deliberate at test-authorship time and are
# closed by the implementation landing (§3.9 steps 1-2):
#
#   * `make_home` IS now a git repository with the invariants document
#     committed in it, per §4.1. It was not at test-authorship time, because
#     making it so before a tool read the home would have reddened the existing
#     suite. `make_home_repo` survives as a thin alias.
#   * `directive` IS now in `CLI_NAMES` / `CLI_MINIMAL_ARGS`, so AC-X-1..X-7
#     cover it. `check-directive` is still absent: its binary does not exist
#     yet, and adding the name would redden those seven against nothing.
#     `test_directive_trd.py` carries the red test asserting that remaining
#     integration point.

#: Where the two binaries are looked up. Overridden by `$DIRECTIVE_TOOLING_BIN`
#: for the red-gate run against the deliberately-wrong stubs in
#: `bin/tests/stubs/`. Test-only; no production code reads it.
DT_BIN_ENV_VAR = "DIRECTIVE_TOOLING_BIN"

INVARIANTS_RELPATH = "skills/directive-invariants.md"
AUTHORING_RELPATH = "skills/directive-authoring.md"

#: TRD §3.4's Q9 decision. The fixture substrate sources it from one place so
#: that a test can vary it and prove the single-source property.
DISPOSITION_LABEL = "WORKING-TREE DISPOSITION"

#: TRD §3.4's sole-tree branch: a literal the invariants document fixes.
SOLE_TREE_SENTENCE = "This session works in the sole tree at the clone root."

DT_STUB_DIR = TESTS_DIR / "stubs"


def dt_bin_dir():
    """Directory the two directive-tooling binaries are invoked from."""
    override = os.environ.get(DT_BIN_ENV_VAR)
    return pathlib.Path(override) if override else BIN_DIR


def using_stub_binaries():
    """True when the red-gate run has pointed us at `bin/tests/stubs/`."""
    return dt_bin_dir().resolve() != BIN_DIR.resolve()


def run_dt(name, *args, cwd, env=None, methodology_home=None, timeout=90):
    """`run_cli` for the two directive-tooling binaries, honouring `dt_bin_dir()`."""
    return run_cli(
        name,
        *args,
        cwd=cwd,
        env=env,
        methodology_home=methodology_home,
        timeout=timeout,
        script_dir=dt_bin_dir(),
    )


# ------------------------------------------------------- the invariants document
#
# TRD §3.2 decides *that* the invariants document holds one section per region,
# "each addressed by its heading", and §3.3 fixes the marker syntax and the
# region tables. It fixes no schema for the document itself: no heading level,
# no statement of whether a region's marker line is part of the committed
# section body or emitted by the generator, and no section name for the M1 and
# M4-M7 match phrases §3.6 says `invariants.py` compiles from it.
#
# This fixture therefore *is* the schema the tests assert against:
#
#   * sections are `## <name>` ATX headings; a section's body runs to the next
#     `## ` heading;
#   * a region section's body **begins with that region's marker line**, so the
#     generator copies it verbatim and composes no prose of its own (§3.2
#     condition 1) while AC-DT-02 still forbids the marker from being a literal
#     in the generator's source;
#   * `## Disposition label`, `## Marker syntax`, `## Preamble markers` and
#     `## Match phrases` carry the lint's compiled strings inside fenced blocks.
#
# The label literal appears **only inside fenced blocks** (§3.2 condition 2).

_SECTION_ORDER = (
    "Heading (general)",
    "Heading (cycle)",
    "Route and model",
    "First act",
    "Working-tree disposition prompt",
    "Base verification",
    "Companions",
    "Task",
    "Sandbox constraints",
    "Verification steps",
    "Stop conditions",
    "Report format",
    "Claim labels",
    "Decisions",
    "Deferred",
    "Execution notes",
    "Source manifest",
    "Disposition label",
    "Marker syntax",
    "Preamble markers",
    "Match phrases",
)

_FENCE = "```"


def invariants_sections():
    """The fixture invariants document, section name -> body (no heading line)."""
    prompt_examples = "\n".join(
        [
            _FENCE + "text",
            "%s (exclusive assignment): this session works only in a worktree" % DISPOSITION_LABEL,
            'at "wt/<name>", created by: git worktree add "wt/<name>" main',
            "",
            "%s: %s" % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE),
            _FENCE,
        ]
    )
    label_block = "\n".join(
        [
            _FENCE + "text",
            "%s:" % DISPOSITION_LABEL,
            _FENCE,
        ]
    )
    sole_tree_block = "\n".join([_FENCE + "text", SOLE_TREE_SENTENCE, _FENCE])
    return {
        "Heading (general)": "# {{title}}\n",
        "Heading (cycle)": (
            "# {{heading}}\n"
            "\n"
            "Date: {{date}}\n"
            "\n"
            "Documents in scope:\n"
            "\n"
            "{{scope_list}}\n"
        ),
        "Route and model": "ROUTE AND MODEL\n\nRoute: {{route}}\nModel: {{model}}\n",
        "First act": (
            "FIRST ACT\n"
            "\n"
            "Write this directive verbatim to {{directive_path}}, commit it alone,\n"
            "push, and report the SHA.\n"
        ),
        "Working-tree disposition prompt": (
            "DISPOSITION PROMPT\n"
            "\n"
            "A working-tree disposition is required. Two forms are admitted: an\n"
            "exclusive assignment — a named directory plus the command creating it —\n"
            "or an explicit sole-tree declaration. A prohibition is not a\n"
            "disposition. The disposition is stated as its own labelled statement,\n"
            "exactly one per directive, mechanically distinguishable from incidental\n"
            "mention of trees or commands elsewhere in the file.\n"
            "\n"
            "Worked examples of the two admitted forms:\n"
            "\n" + prompt_examples + "\n"
        ),
        "Base verification": (
            "BASE VERIFICATION\n"
            "\n"
            "Before anything else, confirm the base is at the reviewed ref\n"
            "{{reviewed_ref}}. If it has moved, stop and report.\n"
        ),
        "Companions": "COMPANIONS\n\n{{companion_list}}\n",
        "Task": "TASK\n",
        "Sandbox constraints": (
            "SANDBOX\n"
            "\n"
            "Commands run in a sandbox. Use the scratchpad directory for temporary\n"
            "files; a denied write is reported, never worked around.\n"
        ),
        "Verification steps": (
            "VERIFICATION\n"
            "\n"
            "Run the test suite and the frontmatter check from the working tree, and\n"
            "state both results.\n"
        ),
        "Stop conditions": (
            "STOP CONDITIONS\n"
            "\n"
            "Pinned to the reviewed ref {{reviewed_ref}}. Cannot execute as written:\n"
            "stop and surface. Concurrent tree mutation: stop and surface.\n"
        ),
        "Report format": (
            "REPORT\n"
            "\n"
            "- the directive file's commit SHA\n"
            "- what was verified, and how\n"
            "- anything observed this directive did not anticipate\n"
        ),
        "Claim labels": (
            "CLAIM LABELS\n"
            "\n"
            "Label every claim observed, inferred, told, or unknown.\n"
        ),
        "Decisions": (
            "## Decisions\n"
            "\n"
            "<!--\n"
            "Finding:\n"
            "Resolution:\n"
            "Dictated wording:\n"
            "-->\n"
        ),
        "Deferred": "## Deferred / out of scope\n",
        "Execution notes": "## Execution notes\n",
        "Source manifest": (
            "SOURCE MANIFEST\n"
            "\n"
            "One entry per emitted region, in emission order: the marker that begins\n"
            "the region, and either the committed path it was read from or an\n"
            "author-region marking.\n"
            "\n"
            "{{manifest}}\n"
        ),
        "Disposition label": (
            "The label literal the generator emits, at column 0:\n"
            "\n" + label_block + "\n"
            "\n"
            "Match rule: an eligible line whose leading content, after stripping, is\n"
            "exactly that literal, followed by a colon anywhere later on the same\n"
            "line. Case-sensitive; no hyphen variants; no case folding.\n"
            "\n"
            "Statement extent: the label line plus every following line up to the\n"
            "first blank line.\n"
            "\n"
            "Exclusive-assignment form: the extent contains a `git worktree add`\n"
            "invocation and a quoted or backticked path-shaped token.\n"
            "\n"
            "Canonical sole-tree sentence:\n"
            "\n" + sole_tree_block + "\n"
        ),
        "Marker syntax": (
            "A marker is a line at column 0 that is either an ATX heading (one to\n"
            "six `#` characters, a space, then text; the token is the text after the\n"
            "run) or an all-caps run of three or more characters drawn from `A`-`Z`,\n"
            "`0`-`9`, `-`, and single interior spaces, terminated by any character\n"
            "outside that set or by end of line (the token is the run). Nothing else\n"
            "is a marker.\n"
        ),
        "Preamble markers": (
            "Markers admitted before the first-act statement (M5):\n"
            "\n" + _FENCE + "text\n"
            "<document heading>\n"
            "ROUTE AND MODEL\n"
            + _FENCE + "\n"
        ),
        "Match phrases": (
            "The phrases the lint compiles, one fenced block per element.\n"
            "\n"
            "M1:\n"
            "\n" + _FENCE + "text\nreviewed ref\n" + _FENCE + "\n"
            "\n"
            "M4:\n"
            "\n" + _FENCE + "text\ncannot execute as written\nconcurrent tree mutation\n"
            + _FENCE + "\n"
            "\n"
            "M5:\n"
            "\n" + _FENCE + "text\nwrite\ncommit\npush\nreport the SHA\n" + _FENCE + "\n"
            "\n"
            "M6:\n"
            "\n" + _FENCE + "text\nreport\n" + _FENCE + "\n"
            "\n"
            "M7:\n"
            "\n" + _FENCE + "text\nobserved\ninferred\ntold\nunknown\n" + _FENCE + "\n"
        ),
    }


def invariants_text(overrides=None, drop=()):
    """Render the fixture invariants document.

    `overrides` replaces a section's body outright — AC-DT-01 changes one
    section's committed text this way. `drop` removes sections, for FM-G2.
    """
    sections = invariants_sections()
    sections.update(overrides or {})
    parts = ["# Directive Invariants\n"]
    for name in _SECTION_ORDER:
        if name in drop:
            continue
        parts.append("\n## %s\n\n%s" % (name, sections[name]))
    return "".join(parts)


def invariants_doc(home, overrides=None, drop=(), env=None, commit_it=True,
                   message="invariants"):
    """Install `skills/directive-invariants.md` into `home` and commit it there.

    §3.2 resolves the document's revision in the **methodology home**, so the
    fixture must give the home a history (F-2's resolution). Returns the
    commit SHA, or None when `commit_it` is False.
    """
    env = env or base_env()
    write(home, INVARIANTS_RELPATH, invariants_text(overrides, drop))
    if not commit_it:
        return None
    return commit(home, message, env=env)


def make_home_repo(case, git_init=True, **kwargs):
    """A thin alias for `make_home`, kept so existing imports stand.

    TRD §4.1 said this fold lands at migration step 1/2, and it has: there is
    one substrate helper again, and this name is the migration's step rather
    than a second one.
    """
    return make_home(case, git_init=git_init, **kwargs)


# ------------------------------------------------------------ fixture directives
#
# One well-formed base carrying every element M1-M8, built as an ordered list of
# (block key, text) pairs so `omit=` removes exactly one element's text
# (TRD §4.1). Two elements cannot be built by subtraction and are built by
# corruption instead, which is filed as a finding:
#
#   * M2 — a directive with no companion citation passes M2 vacuously, so the
#     failing fixture replaces a citation rather than removing one;
#   * M8 — the element is a property of the filename, not of the text.

DT_DEFAULT_NAME = "docs/cycles/fixture-well-formed-20260828T170000.md"
DT_COMPANION_A = "docs/companion-a.md"
DT_COMPANION_B = "docs/companion-b.md"

#: The label line the base fixture carries: §3.4's parenthetical tolerance.
DT_DISPOSITION_STATEMENT = (
    '%s (exclusive assignment): this session works only in a worktree at\n'
    '"wt/fixture", created by: git worktree add "wt/fixture" main\n'
) % DISPOSITION_LABEL

DT_SOLE_TREE_STATEMENT = "%s: %s\n" % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE)


def _dt_blocks(reviewed_ref, companion_path, companion_sha, title, directive_path):
    """The base directive's regions, in order, as (key, text) pairs."""
    return [
        ("heading", "# %s\n" % title),
        ("route", "ROUTE AND MODEL\n\nRoute: fresh\nModel: Opus 5\n"),
        (
            "first-act",
            "FIRST ACT\n"
            "\n"
            "Write this directive verbatim to %s, commit it alone, push, and\n"
            "report the SHA.\n" % directive_path,
        ),
        (
            "disposition-prompt",
            "DISPOSITION PROMPT\n"
            "\n"
            "A working-tree disposition is required. Two forms are admitted: an\n"
            "exclusive assignment — a named directory plus the command creating it —\n"
            "or an explicit sole-tree declaration. A prohibition is not a\n"
            "disposition. The disposition is stated as its own labelled statement,\n"
            "exactly one per directive.\n",
        ),
        ("disposition", DT_DISPOSITION_STATEMENT),
        (
            "base-verification",
            "BASE VERIFICATION\n"
            "\n"
            "Confirm the base is at the reviewed ref %s before anything else.\n"
            % reviewed_ref,
        ),
        (
            "companions",
            "COMPANIONS\n\n- %s @ %s\n" % (companion_path, companion_sha),
        ),
        ("task", "TASK\n\nDo the fixture work described by the dispatching session.\n"),
        (
            "sandbox",
            "SANDBOX\n"
            "\n"
            "Commands run in a sandbox. Use the scratchpad directory for temporary\n"
            "files.\n",
        ),
        (
            "verification",
            "VERIFICATION\n\nRun the suite and the frontmatter check, and state both\nresults.\n",
        ),
        (
            "stop-conditions",
            "STOP CONDITIONS\n"
            "\n"
            "Pinned to the reviewed ref %s. Cannot execute as written: stop and\n"
            "surface. Concurrent tree mutation: stop and surface.\n" % reviewed_ref,
        ),
        (
            "report",
            "REPORT\n"
            "\n"
            "- the directive file's commit SHA\n"
            "- what was verified, and how\n"
            "- anything observed this directive did not anticipate\n",
        ),
        (
            "claim-labels",
            "CLAIM LABELS\n\nLabel every claim observed, inferred, told, or unknown.\n",
        ),
    ]


#: Which base block each element's text lives in, for `omit=`.
DT_ELEMENT_BLOCKS = {
    "M1": ("base-verification", "stop-conditions"),
    "M3": ("disposition",),
    "M4": ("stop-conditions",),
    "M5": ("first-act",),
    "M6": ("report",),
    "M7": ("claim-labels",),
}

#: M1 and M4 share the `stop-conditions` block, so removing one must leave the
#: other's text standing. These are the reduced forms.
DT_REDUCED_BLOCKS = {
    "M1": {
        "base-verification": "BASE VERIFICATION\n\nConfirm the base before anything\nelse.\n",
        "stop-conditions": (
            "STOP CONDITIONS\n"
            "\n"
            "Cannot execute as written: stop and surface. Concurrent tree mutation:\n"
            "stop and surface.\n"
        ),
    },
    "M4": {
        "stop-conditions": "STOP CONDITIONS\n\nPinned to the reviewed ref %s.\n",
    },
}


def directive_body(
    *,
    reviewed_ref,
    companion_path=DT_COMPANION_A,
    companion_sha=None,
    title="Fixture Directive — well formed",
    directive_path=DT_DEFAULT_NAME,
    omit=None,
    replace=None,
    extra=None,
):
    """The text of a fixture directive.

    `omit` names one of M1, M3-M7 and removes exactly that element's text.
    `replace` maps a block key to replacement text. `extra` is appended.
    """
    blocks = _dt_blocks(reviewed_ref, companion_path, companion_sha, title, directive_path)
    reduced = dict(DT_REDUCED_BLOCKS.get(omit, {}))
    if omit == "M4":
        reduced["stop-conditions"] = reduced["stop-conditions"] % reviewed_ref
    drop = set()
    if omit in DT_ELEMENT_BLOCKS and omit not in DT_REDUCED_BLOCKS:
        drop = set(DT_ELEMENT_BLOCKS[omit])
    out = []
    for key, text in blocks:
        if key in drop:
            continue
        if key in reduced:
            text = reduced[key]
        if replace and key in replace:
            if replace[key] is None:
                continue
            text = replace[key]
        out.append(text)
    body = "\n".join(out)
    if extra:
        body += "\n" + extra
    return body


def directive_fixture(
    repo,
    *,
    reviewed_ref,
    omit=None,
    name=None,
    companion_path=DT_COMPANION_A,
    companion_sha=None,
    replace=None,
    extra=None,
    text=None,
    title="Fixture Directive — well formed",
):
    """Write a fixture directive into `repo` and return its repo-relative path.

    `omit="M8"` is a name change, not a text change: M8 is a property of the
    resolved path. `omit="M2"` corrupts the citation rather than removing it,
    because a directive carrying no citation passes M2 vacuously.
    """
    relpath = name or DT_DEFAULT_NAME
    if omit == "M8":
        relpath = name or "docs/cycles/fixture-no-timestamp.md"
        omit = None
    if omit == "M2":
        omit = None
    if text is None:
        text = directive_body(
            reviewed_ref=reviewed_ref,
            companion_path=companion_path,
            companion_sha=companion_sha,
            title=title,
            directive_path=relpath,
            omit=omit,
            replace=replace,
            extra=extra,
        )
    write(repo, relpath, text)
    return relpath


# ------------------------------------------------------------------ M3 shape set
#
# AC-DT-06's shapes (i)-(vii) plus the two-statement and neither/both cases,
# instantiable now that §3.4 fixes the label. Each varies only the disposition
# region of the well-formed base, so a non-zero exit is attributable to M3.

DT_M3_SHAPES = (
    "i-exclusive",
    "i-sole-tree",
    "ii-unlabelled-prohibition",
    "iii-plus-unlabelled-instance",
    "iv-slot-filled",
    "v-slot-blank",
    "vi-unfenced-plus-fenced",
    "vii-only-fenced",
    "two-unfenced",
    "neither-form",
    "both-forms",
)

#: Shapes AC-DT-06 fixes as passing M3.
DT_M3_PASSING = frozenset(
    {"i-exclusive", "i-sole-tree", "iii-plus-unlabelled-instance",
     "iv-slot-filled", "vi-unfenced-plus-fenced"}
)


def _dt_m3_disposition(shape):
    """`(disposition block text, extra text appended after the base)`."""
    fenced = "\n".join(
        [
            _FENCE + "text",
            "%s (exclusive assignment): a carried disposition from another" % DISPOSITION_LABEL,
            'directive, quoted under the origin exception: git worktree add "wt/other" main',
            _FENCE,
            "",
        ]
    )
    if shape == "i-exclusive":
        return DT_DISPOSITION_STATEMENT, None
    if shape == "i-sole-tree":
        return DT_SOLE_TREE_STATEMENT, None
    if shape == "ii-unlabelled-prohibition":
        return (
            "Do not create a worktree and do not share a tree with another\n"
            "session.\n"
        ), None
    if shape == "iii-plus-unlabelled-instance":
        return DT_DISPOSITION_STATEMENT, (
            "CLEANUP\n"
            "\n"
            'Afterwards remove the tree at "wt/fixture" created by\n'
            'git worktree add "wt/fixture" main.\n'
        )
    if shape == "iv-slot-filled":
        return (
            "%s (exclusive assignment): this session works only in a worktree at\n"
            '"wt/slot", created by: git worktree add "wt/slot" main\n' % DISPOSITION_LABEL
        ), None
    if shape == "v-slot-blank":
        return "%s:\n" % DISPOSITION_LABEL, None
    if shape == "vi-unfenced-plus-fenced":
        return DT_DISPOSITION_STATEMENT, fenced
    if shape == "vii-only-fenced":
        return "The disposition is carried below, wrongly fenced.\n", fenced
    if shape == "two-unfenced":
        return DT_DISPOSITION_STATEMENT, DT_SOLE_TREE_STATEMENT
    if shape == "neither-form":
        return (
            "%s: this session works wherever the operator finds convenient.\n"
            % DISPOSITION_LABEL
        ), None
    if shape == "both-forms":
        return (
            "%s (exclusive assignment): this session works only in a worktree at\n"
            '"wt/both", created by: git worktree add "wt/both" main. %s\n'
            % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE)
        ), None
    raise AssertionError("unknown M3 shape: %r" % shape)


def disposition_fixture(repo, shape, *, reviewed_ref, companion_sha=None, name=None):
    """One of AC-DT-06's M3 shapes, written into `repo`."""
    block, extra = _dt_m3_disposition(shape)
    relpath = name or ("docs/cycles/fixture-m3-%s-20260828T170000.md" % shape)
    return directive_fixture(
        repo,
        reviewed_ref=reviewed_ref,
        companion_sha=companion_sha,
        name=relpath,
        replace={"disposition": block},
        extra=extra,
        title="Fixture Directive — M3 %s" % shape,
    )


# ------------------------------------------------------------- citation fixtures
#
# AC-DT-09's four synthetic citations and AC-DT-17's two passing forms, all on
# real objects in the fixture repository. The touching commit is the repository's
# **root** commit, so the pair exercises F-1's `diff-tree --root` semantics: a
# root commit compared against nothing reports touching no path.


def citation_fixtures(repo, env=None):
    """Build real objects for M2 and return the SHAs each fixture cites.

    Keys:
      `touching`      — the root commit, which introduced `DT_COMPANION_A`
      `non_touching`  — a later commit touching `DT_COMPANION_B` only
      `blob`          — `DT_COMPANION_A`'s blob hash
      `tag`           — an annotated tag object pointing at `touching`
      `abbreviated`   — an 8-character prefix of `touching` (AC-DT-17 (a))
      `not_last`      — a content commit that is not the last touching the path
      `last`          — the last commit touching `DT_COMPANION_A`
      `unresolvable`  — a well-formed SHA that names no object
    """
    env = env or base_env()
    write(repo, DT_COMPANION_A, "# Companion A\n\nv1\n")
    touching = commit(repo, "companion a", env=env)
    write(repo, DT_COMPANION_B, "# Companion B\n\nv1\n")
    non_touching = commit(repo, "companion b", env=env)
    blob = git(repo, "rev-parse", "%s:%s" % (touching, DT_COMPANION_A), env=env, check=True)[1].strip()
    git(repo, "tag", "-a", "fixture-tag", "-m", "annotated", touching, env=env, check=True)
    tag = git(repo, "rev-parse", "fixture-tag", env=env, check=True)[1].strip()
    write(repo, DT_COMPANION_A, "# Companion A\n\nv2\n")
    last = commit(repo, "companion a v2", env=env)
    return {
        "touching": touching,
        "non_touching": non_touching,
        "blob": blob,
        "tag": tag,
        "abbreviated": touching[:8],
        "not_last": touching,
        "last": last,
        "unresolvable": "0" * 40,
    }


# ---------------------------------------------------------------- M8 name fixtures
#
# AC-DT-06's nine: five passing, four failing. `subdir_relative` and `absolute`
# name the same file as `timestamped`, invoked differently — M8 matches on the
# resolved repository-relative path (AC-DT-19).

DT_M8_PASSING_NAMES = {
    "timestamped": "docs/cycles/fixture-desc-20260828T170000.md",
    "cycle": "docs/cycles/cycle-7-directive.md",
    "slug": "docs/cycles/some slug+odd-directive.md",
}

DT_M8_FAILING_NAMES = {
    "date-only": "docs/cycles/fixture-desc-20260828.md",
    "neither": "docs/cycles/fixture-plain-name.md",
    "nested": "docs/cycles/sub/nested-directive.md",
    "escaped": "docs/escaped-directive.md",
}
