"""THROWAWAY TEST STUB — NOT AN IMPLEMENTATION. DELETE AND REWRITE WHOLESALE.

=============================================================================
 THIS FILE IS A TEST FIXTURE WRITTEN BY THE TEST DESIGNER, NOT PRODUCTION CODE.
 It exists so `bin/tests/test_land.py` fails on bad logic rather than on a
 missing module. It is DELIBERATELY WRONG and is not a partial implementation.
 The Coder replaces this whole file with the real `land.py` of
 `specs/bin-land-trd.md` §3.2 and §3.7.
=============================================================================

How it is deliberately wrong:

- **Nine of the eleven steps of §3.2 are absent.** It does not fetch, does not
  read the remote, does not stage, does not commit, does not push, and does
  not verify. It establishes no fact, and hands `report.py` a `facts` dict
  that stub also ignores.
- **It performs step 6's ref rewrite with no divergence guard in front of it,
  and with the base taken from local HEAD rather than from the remote.** That
  is the destructive class `specs/bin-land.md` §7 puts under "Not accepted"
  and TRD §3.3 warns about by name: run without step 5's guard, `checkout -B`
  orphans whatever unpushed commits `<branch>` carried. It is here **on
  purpose**, so that AC-LAND-T03's "the prior tip is still reachable" and "no
  ref moved" assertions fail on real behaviour instead of passing for free
  against a stub that does nothing.

    ***Do not carry any line of this file forward.*** A guarded version of
    this function is not the fix; the fix is deleting the file.
"""

from __future__ import annotations

from . import report, repo


def land(branch, message, paths, cwd):
    """Signature-shaped after TRD §3.7 and performing no landing whatsoever."""
    del message  # a real implementation is where this is used
    if branch:
        # DELIBERATE DESTRUCTIVE DEFECT — see the module docstring. No guard,
        # no remote read, no base from origin.
        repo.run(["checkout", "-B", branch], cwd=cwd)
    return report.Report.build(branch, {"paths": list(paths or [])}, None)
