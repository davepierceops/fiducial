"""No live file names a removed tool (subtraction plan section 6, DEC-001160, DEC-001200).

For each removed tool name, every hit across `bin/`, `process/`, `rules/`, `README.md`,
`specs/` and `.claude/` must be under `docs/history/` or `decisions/log.md`
(neither is in the scanned set, so the check is: no hit at all, this file
excepted). README.md is rewritten in package 6b; until then its hits are
reported, not failed, via `README_PENDING`.

Run alone: `python3 -m unittest discover -s bin/tests -t bin -p test_removed_tools.py`
or `python3 bin/tests/test_removed_tools.py` to print every hit.
"""

from __future__ import annotations

import pathlib
import re
import unittest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SELF = pathlib.Path(__file__).resolve()

#: The removed names. "directive" is matched only as the command, never as the
#: ordinary word the corpus still uses.
PATTERNS = {
    "directive": re.compile(r"bin/directive\b|(?<![\w-])directive --descriptor"),
    "check-directive": re.compile(r"check-directive"),
    "cycle-open": re.compile(r"cycle-open"),
    "aimeta": re.compile(r"aimeta"),
    "bin/land": re.compile(r"bin/land\b"),
}
SCANNED = ["bin", "process", "rules", "README.md", "specs", ".claude"]
#: Package 6b rewrites README.md; its hits are listed, not failed.
README_PENDING = True


def hits():
    found = []
    for entry in SCANNED:
        root = REPO_ROOT / entry
        files = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file()) if root.exists() else []
        for path in files:
            if path.resolve() == SELF or "__pycache__" in path.parts:
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (UnicodeDecodeError, OSError):
                continue
            for number, line in enumerate(lines, 1):
                for name, pattern in PATTERNS.items():
                    if pattern.search(line):
                        found.append((name, path.relative_to(REPO_ROOT).as_posix(), number, line.strip()))
    return found


class TestRemovedToolNames(unittest.TestCase):
    def test_no_live_file_names_a_removed_tool(self):
        offenders = [h for h in hits()
                     if not (README_PENDING and h[1] == "README.md")]
        self.assertEqual(
            offenders, [],
            "\n".join("%s: %s:%d: %s" % h for h in offenders),
        )


if __name__ == "__main__":
    for hit in hits():
        print("%s: %s:%d: %s" % hit)
    unittest.main(argv=["x"], exit=False)
