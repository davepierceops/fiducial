Write this directive verbatim to docs/cycles/directive-tooling-gate-2-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This is a review-only gate of specs/directive-tooling.md @ commit 0eafc3066434f7a91cc78fc80556576c8fd0e09a on branch directive-tooling-spec (the spec's blob at that commit is bcd8e3ef…). Stop conditions pin to 0eafc3066434f7a91cc78fc80556576c8fd0e09a. Fetch origin as your first git act.

YOUR ROLE, and the reason this session exists: Spec Reviewer only. Twelve cycles have run — eleven authored and gated by the same session per cycle, one prior independent gate (cycle 8) whose three blockers all reproduced and were fixed. This is the second independent read, after four further self-gated cycles. You author nothing, fix nothing, and edit no file other than creating this directive file and your review artifact. A defect you find is a finding, never an edit.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-gate2" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-gate2 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before reviewing: specs/directive-tooling.md at the pinned commit; roles/spec-reviewer-agent.md, skills/review-artifact.md, docs/global-context/core.md, skills/directive-authoring.md at origin/main; docs/packages/package-a-spec.md; bin/cycle-open and bin/tests/test_cycle_open.py; docs/research/gh-write-friction-20260823T184149Z.md; reviews/directive-tooling-cycle-12.md (for its open N1, the unnamed third case in M3's fallback, which you must independently confirm, dismiss, or sharpen); reviews/directive-tooling-cycle-8.md (the prior independent gate, for what reproduced); the intervening review artifacts and directive files on this branch as decision record.

TASK — as Spec Reviewer per roles/spec-reviewer-agent.md, run a full gate review of the spec at the pinned commit: all required PRD sections, internal consistency, traceability, AC testability, risk tolerance, open questions, plus consistency against the governed files in the companion list. Verify by running where running is cheap; keep every probe inside your assigned worktree or read-only. Address cycle 12's N1 explicitly, as your own finding or a dismissal with grounds. Produce reviews/directive-tooling-cycle-13.md per skills/review-artifact.md, verdict first, findings in the required schema. Your verdict is your own; the twelve prior artifacts are record, not precedent that binds it.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-13.md — and modify nothing. Directive file first, review artifact after the review completes. Run bin/check-frontmatter --all before the final push and report its exit status.

STOP CONDITIONS. Anything you cannot execute as written → stop and surface; no reinterpretation. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not modify specs/directive-tooling.md or any other existing file; do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; frontmatter check exit status; the verdict line; findings by severity, one line each; your explicit disposition of cycle 12's N1. Label every claim observed / inferred / told / unknown.
