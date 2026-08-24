"""THROWAWAY TEST STUB — NOT AN IMPLEMENTATION. DELETE AND REWRITE WHOLESALE.

=============================================================================
 THIS FILE IS A TEST FIXTURE WRITTEN BY THE TEST DESIGNER, NOT PRODUCTION CODE.
 It exists for exactly one purpose: to make `bin/tests/test_land.py` execute
 and fail on *bad logic* rather than on an ImportError. It is DELIBERATELY
 WRONG. It is not a partial implementation and must never be extended into
 one. The Coder replaces this whole file with the real `report.py` of
 `specs/bin-land-trd.md` §3.7 and §5.
=============================================================================

How it is deliberately wrong, stated so nobody mistakes a defect for a bug:

- It emits a **canned success-shaped report on every path**, whatever
  happened. `prior_head` is always the literal `created`, `verification` is
  always `complete`, every named file always `match: true`, and every SHA is
  the constant `deadbeef...`.
- It **never emits `detail.stage` or `detail.git_status`**, so no failure
  report says where the sequence stopped.
- Its `exit_code` is derived from *how many paths were named*, which is not a
  rule anywhere in the TRD, so `verification` and the exit status disagree
  whenever no path was named (AC-LAND-T02).

Its serialization *is* §5.2's — two-space indent, sorted keys, one trailing
newline — on purpose: the format assertions must pass so that the behavioural
assertions are what fail.
"""

from __future__ import annotations

import json

#: Deliberately not a real SHA of anything. 40 hex characters so the value
#: domain of §5.2 is satisfied while the value is a lie.
FAKE_SHA = "deadbeef" * 5


class Report:
    """A canned report. Not the `Report` of TRD §3.7."""

    def __init__(self, branch, paths):
        self.branch = branch
        self.paths = list(paths)

    @classmethod
    def build(cls, branch, facts, stop=None):
        """Signature-shaped after §3.7 and ignoring both `facts` and `stop`."""
        return cls(branch, (facts or {}).get("paths", []))

    def as_dict(self):
        return {
            "branch": {"value": self.branch, "class": "observed"},
            "head": {"value": FAKE_SHA, "class": "observed"},
            "prior_head": {"value": "created", "class": "observed"},
            "files": [
                {"path": path, "match": True, "class": "observed"}
                for path in self.paths
            ],
            "verification": {"value": "complete", "class": "observed"},
            "detail": {
                "base": {"value": FAKE_SHA, "class": "observed"},
                "local_head": {"value": FAKE_SHA, "class": "observed"},
                "prior_branch": {"value": "main", "class": "observed"},
                "remote_head": {"value": FAKE_SHA, "class": "observed"},
            },
        }

    def to_json(self):
        """§5.2's format, correctly — the one thing this stub gets right."""
        return json.dumps(self.as_dict(), indent=2, sort_keys=True) + "\n"

    def exit_code(self):
        """DELIBERATELY WRONG: a rule that appears nowhere in the TRD."""
        return 0 if self.paths else 4
