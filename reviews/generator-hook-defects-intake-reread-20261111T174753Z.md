# Review: intake/generator-hook-defects — reread-amendment

Verdict: ready-with-findings
Reviewed: process/adopt.md @ 9baea5a
Baseline: process/adopt.md @ b11df95
Reviewer: context-quality-reviewer (subagent; wrote none of the candidate)
Date: 2026-11-11
Scope: `git diff b11df95 9baea5a -- process/` (step 4 reworded, boundary sentence reduced); fence preflight re-read at 9baea5a; boundary sentence compared with 76a6c14.
Cross-checked: process/adopt.md at 76a6c14 (the later diff against 76a6c14 shows no hunk at the boundary sentence, so it is back to base wording); prior read findings F1-F3.
Not inspected: fence unchanged since b11df95 (not re-compiled or re-emitted); running the preflight as a non-root uid; emitted skills and bundle.
Findings: 0 blocking, 1 non-blocking

Resolution of prior findings:
- F1 resolved: the false "does not see read-only filesystems, ACLs or immutable flags" clause is removed.
- F2 resolved: step 4 now limits ownership to "an existing file it would write", matching fence line 375 inside `path.exists() and item["text"] is not None`. Delete and create are routed to the parent or ancestor check (fence lines 376-381), matching "planned write, delete or create".
- F3 resolved: the list now appears once, in step 4 only.

## N1 — non-blocking
Claim: Line 57 is 103 characters, against 76-80 for the surrounding lines, and "permission bits" is narrower than the check, which is `os.access` and so also reflects read-only mounts.
Classification: suggestion
Location: process/adopt.md:54-57; fence lines 374, 380
Evidence: Measured line lengths. The `os.access` behaviour on read-only mounts was run in the earlier read.
Consequence: Style drift (reflow) only; "permission bits" leaves the read-only case unstated, though nothing false is asserted.
Fix: Reflow line 57; optionally say "write permission".
