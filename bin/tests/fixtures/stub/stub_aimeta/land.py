"""THROWAWAY TEST STUB — NOT AN IMPLEMENTATION. DELETE AND REWRITE WHOLESALE.

=============================================================================
 THIS FILE IS A TEST FIXTURE WRITTEN BY THE TEST DESIGNER, NOT PRODUCTION CODE.
 It exists so `bin/tests/test_land.py` fails on bad logic rather than on a
 missing module. It is DELIBERATELY WRONG and is not a partial implementation.
 The Coder replaces this whole file with the real `land.py` of
 `specs/bin-land-trd.md` §3.2 and §3.7.
=============================================================================

How it is deliberately wrong:

- **Almost every step of §3.2 is absent.** It does not fetch, does not
  read the remote, does not resolve or confirm a base, does not guard, does
  not commit, does not push, and does not verify. It establishes no fact, and
  hands `report.py` a `facts` dict that stub also ignores.
- **It writes the index before deciding anything.** `git add -A` runs first,
  with no guard and no base in front of it, which is step 7 happening before
  steps 3 through 6. It is here **on purpose**, so that AC-LAND-T03's "stops
  before anything is staged" fails on real behaviour — a tool that staged and
  then refused — rather than passing because a stub that does nothing left the
  index alone.
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
        # DELIBERATE DEFECT — see the module docstring. The index is written
        # before anything has been resolved, guarded, or based.
        repo.run(["add", "-A"], cwd=cwd)
        # DELIBERATE DESTRUCTIVE DEFECT — see the module docstring. No guard,
        # no remote read, no base from origin.
        repo.run(["checkout", "-B", branch], cwd=cwd)
    return report.Report.build(branch, {"paths": list(paths or [])}, None)
