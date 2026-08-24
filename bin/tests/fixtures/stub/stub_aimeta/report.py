r"""THROWAWAY TEST STUB — NOT AN IMPLEMENTATION. DELETE AND REWRITE WHOLESALE.

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
- It **never emits `detail.stage`**, so no failure report says where the
  sequence stopped.
- It emits `detail.git_status` **as a string, on every path**, where §5.2
  closes that value at a JSON number and §5.3 establishes the key on no
  success path at all. Both halves are wrong on purpose: it is the one value
  domain this stub violates, so the red-gate shows the domain assertions can
  fail rather than only that they run.
- Its `exit_code` is derived from *how many paths were named*, which is not a
  rule anywhere in the TRD, so `verification` and the exit status disagree
  whenever no path was named (AC-LAND-T02).
- It serializes with **`ensure_ascii=False`**, so a non-ASCII character in a
  value is written out as raw UTF-8 bytes where §5.2 requires a `\uXXXX`
  escape and a stdout that is pure ASCII on every path. This one is here for a
  reason worth stating in full: `json.dumps` **defaults** to
  `ensure_ascii=True`, so a stub that simply called it would already satisfy
  the escape rule, and `test_land.py`'s escape assertions would pass against a
  stub that implements nothing. A passing assertion is not a red-gate. The
  argument is written in explicitly, and written in *wrong*, so that
  `TestT01NonAsciiValuesAreEscaped`'s three cases fail on behaviour — this
  stub emitting the raw character — rather than on scaffolding.

Its serialization is otherwise §5.2's — two-space indent, sorted keys, one
trailing newline — on purpose: the format assertions must pass so that the
behavioural assertions are what fail. `ensure_ascii` is the single knob turned
the wrong way, and nothing else about the format is.
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
                # DELIBERATE DEFECT: a string, and on every path (§5.2, §5.3).
                "git_status": {"value": "128", "class": "observed"},
                "local_head": {"value": FAKE_SHA, "class": "observed"},
                "prior_branch": {"value": "main", "class": "observed"},
                "remote_head": {"value": FAKE_SHA, "class": "observed"},
            },
        }

    def to_json(self):
        r"""§5.2's format but for `ensure_ascii` — see the module docstring.

        DELIBERATE DEFECT: `ensure_ascii=False`. §5.2 requires a non-ASCII
        character in any value to be written as a `\uXXXX` escape, so that
        stdout is pure ASCII on every path whatever a value carries (the
        decision that retired OQ-11). `json.dumps` gives that for free by
        default, which is exactly why the default is not used here: the
        assertion has to be able to fail. Indent, key order and the single
        trailing newline stay §5.2's.
        """
        return (
            json.dumps(self.as_dict(), indent=2, sort_keys=True, ensure_ascii=False)
            + "\n"
        )

    def exit_code(self):
        """DELIBERATELY WRONG: a rule that appears nowhere in the TRD."""
        return 0 if self.paths else 4
