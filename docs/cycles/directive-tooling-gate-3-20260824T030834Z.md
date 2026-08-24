Write this directive verbatim to docs/cycles/directive-tooling-gate-3-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

ROLES. This session fills one role: Spec Reviewer per roles/spec-reviewer-agent.md. You author nothing, fix nothing, and edit no file other than creating this directive file and your review artifact. A defect you find is a finding, never an edit.

REVIEWED REF. This is a review-only gate of specs/directive-tooling.md @ commit 0b1c90c651a90b4a635d9fac711a4872ab353dba on branch directive-tooling-spec (the spec's blob at that commit is ca04e153…). Stop conditions pin to 0b1c90c651a90b4a635d9fac711a4872ab353dba. Fetch origin as your first git act.

CONTEXT. Fifteen cycles have run: thirteen authored-and-gated by one session per cycle, two prior independent gates (cycle 8, cycle 13), each of which found blocking defects the preceding self-gates passed. The cycle-15 self-gate returned ready-with-findings with three open non-blockings. This is the third independent read, intended as the last gate before Dave's agreement if it comes back clean or minor.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-gate3" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-gate3 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before reviewing: specs/directive-tooling.md at the pinned commit; roles/spec-reviewer-agent.md, skills/review-artifact.md, docs/global-context/core.md, docs/global-context/decision-layer.md, skills/directive-authoring.md at origin/main (note its four same-day amendments; last-reviewed reviews/expedited-log.md @ b4a0fa581ba5c64ac5a0e5374b5604e979a73653); docs/packages/package-a-spec.md; bin/cycle-open and bin/tests/test_cycle_open.py; docs/research/gh-write-friction-20260823T184149Z.md; reviews/directive-tooling-cycle-15.md (for its open N1, N2, N3, which you must independently confirm, dismiss, or sharpen — N1's quotation residual in particular against the skill's carry-as-pointer rule); reviews/directive-tooling-cycle-8.md and reviews/directive-tooling-cycle-13.md (the prior independent gates); the intervening artifacts and directive files on this branch as decision record.

TASK — as Spec Reviewer, run a full gate review of the spec at the pinned commit: all required PRD sections, internal consistency, traceability, AC testability, risk tolerance, open questions, plus consistency against the governed files in the companion list — including whether M3's labelled-statement contract is consistent with the amended skill, and whether §7's residual set (including the new false-negative item) is honestly and completely stated for Dave's signature. Verify by running where running is cheap; keep every probe inside your assigned worktree or read-only. Address cycle 15's N1, N2, and N3 explicitly, each as your own finding or a dismissal with grounds. Produce reviews/directive-tooling-cycle-16.md per skills/review-artifact.md, verdict first, findings in the required schema. Your verdict is your own; the fifteen prior artifacts are record, not precedent that binds it.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-16.md — and modify nothing. Directive file first, review artifact after the review completes. Run bin/check-frontmatter --all before the final push and report its exit status.

STOP CONDITIONS. Anything you cannot execute as written → stop and surface; no reinterpretation. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not modify specs/directive-tooling.md or any other existing file; do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; frontmatter check exit status; the verdict line; findings by severity, one line each; your explicit dispositions of cycle 15's N1, N2, N3. Label every claim observed / inferred / told / unknown.
