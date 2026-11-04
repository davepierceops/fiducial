"""Shared plumbing for the `bin/hooks/*` scripts (the plan, §3a).

Every script is a Claude Code hook: it reads one JSON object on stdin —
`hook_event_name`, `tool_name`, `tool_input` (`file_path`, `content`,
`old_string`, `new_string`, `command`, ...), `tool_response` after the tool
ran, and `cwd` — and answers with its exit status. `0` lets the call
through; `2` blocks it (`PreToolUse`) or reports the failure to the model
(`PostToolUse`), with the reason on stderr. Any other failure of the script
itself is also exit 2 with a reason, never a silent pass.

The emitter copies this directory whole into `.claude/hooks/`, so a script
imports this module from its own directory and nothing else outside the
standard library.
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys

EXIT_PASS = 0
EXIT_BLOCK = 2


def read_input():
    """The hook's JSON input, or `{}` on empty stdin."""
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except ValueError as exc:
        block("hook input is not JSON: %s" % exc)


def block(reason):
    print(reason, file=sys.stderr)
    sys.exit(EXIT_BLOCK)


def passthrough(message=None):
    if message:
        print(message)
    sys.exit(EXIT_PASS)


def git(root, *args):
    proc = subprocess.run(
        ["git", *args], cwd=str(root), capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def cwd_of(data):
    return pathlib.Path(data.get("cwd") or os.getcwd())


def repo_root(start):
    """The git toplevel containing `start`, or `None`."""
    start = pathlib.Path(start)
    probe = start if start.is_dir() else start.parent
    while not probe.exists() and probe != probe.parent:
        probe = probe.parent
    code, out, _ = git(probe, "rev-parse", "--show-toplevel")
    if code != 0:
        return None
    return pathlib.Path(out.strip())


def target_file(data):
    """`(root, relpath)` for the file a tool call names, or `(None, None)`
    when the call names no file. `relpath` is POSIX, relative to the git
    toplevel; a file outside any repository gives `(None, path)`."""
    file_path = (data.get("tool_input") or {}).get("file_path")
    if not file_path:
        return None, None
    path = pathlib.Path(file_path)
    if not path.is_absolute():
        path = cwd_of(data) / path
    root = repo_root(path)
    if root is None:
        return None, path.as_posix()
    try:
        rel = path.resolve().relative_to(root.resolve())
    except ValueError:
        return None, path.as_posix()
    return root, rel.as_posix()


def tracked_at_head(root, relpath):
    code, _, _ = git(root, "cat-file", "-e", "HEAD:%s" % relpath)
    return code == 0


DEFAULT_BRANCH_REFS = ("origin/main", "main")


def on_default_branch(root, relpath):
    """Whether `relpath` exists on the default branch (`origin/main` or
    `main`, whichever exist; either holding it counts). With neither ref
    present, falls back to being tracked at HEAD."""
    refs = [ref for ref in DEFAULT_BRANCH_REFS
            if git(root, "rev-parse", "--verify", "-q", ref + "^{commit}")[0] == 0]
    if not refs:
        return tracked_at_head(root, relpath)
    return any(git(root, "cat-file", "-e", "%s:%s" % (ref, relpath))[0] == 0 for ref in refs)


def current_branch(root):
    code, out, _ = git(root, "rev-parse", "--abbrev-ref", "HEAD")
    return out.strip() if code == 0 else ""


def under(relpath, *dirs):
    return any(relpath == d.rstrip("/") or relpath.startswith(d) for d in dirs)
