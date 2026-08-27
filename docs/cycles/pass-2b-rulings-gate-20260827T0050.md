Context Quality Reviewer gate over branch pass-2b-rulings. Reissued after the worktree-add failure; supersedes the previous block. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE. The local branch pass-2b-rulings-gate already exists at 7b7fb8d. Create the tree with `git worktree add "$TMPDIR/pass-2b-rulings-gate" pass-2b-rulings-gate` from the main clone and work only there. Confirm `git rev-parse HEAD` in the new tree is 7b7fb8d before anything else. If the add fails for any reason, stop and report; do not retry with different flags.
Write this entire block, verbatim, to docs/cycles/pass-2b-rulings-gate-20260827T0050.md. Commit with message "docs/cycles: land pass-2b-rulings-gate directive". Push with `git push origin pass-2b-rulings-gate`. Verify with `git ls-remote origin pass-2b-rulings-gate`. Report "landed <path> as <sha>" using the SHA read back from git.

ROLE: Context Quality Reviewer, execution session. You gate; you do not edit the reviewed documents.

REVIEWED REF: 7b7fb8d86964d4023ff074f83670b184dba1613a (pass-2b-rulings head). Baseline: a3acb75ef47d4eaa8295bfe2524a967742df8f85 (main). Decision record: docs/cycles/pass-2b-rulings-20260827T0025.md @ 94c01bf7 — read it first; it states each ruling and its reason.

STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/pass-2b-rulings` is not 7b7fb8d before you begin.
- Any tree mutation you did not intend, including your own.
- Any push fails.

SCOPE: the diff a3acb75..7b7fb8d over the three governed documents — skills/spec-review-cycle.md, roles/chief-of-staff.md, operating-model.md. Review each changed passage in the context of its whole file against every criterion of docs/global-context/review-rubric.md. Confirm each edit does what its ruling says and nothing more.

CROSS-CHECK, at minimum, and name what you checked:
- C014: policies/document-metadata-policy.md — that the deleted sentence's check is stated there and nothing in the skill now contradicts it.
- C015: LEXICON.md "Claimed" and context-sets/spec-and-change-discipline.md "Concurrency" — that the new bullet describes both accurately.
- C018: LEXICON.md evidence classes and policies/verification-boundary-policy.md — that the new bullet agrees with both.

ARTIFACT: write reviews/pass-2b-rulings-cycle-1.md per skills/review-artifact.md. This is a multi-document review; the stem names the branch. Reviewed: lists the three documents at 7b7fb8d. Baseline: a3acb75. Prior cycle: none. Findings cite path and line. Verdict is ready, ready-with-findings, or changes-required.

COMMIT AND PUSH: one commit, message "reviews: pass-2b-rulings cycle 1 — <verdict>". Push with `git push origin pass-2b-rulings-gate`. Verify with `git ls-remote origin pass-2b-rulings-gate`.

DO NOT: edit any file other than the review artifact and this directive; flip status; open a pull request; merge; delete branches or worktrees.

REPORT:
1. Directive path and landed SHA.
2. Artifact path and commit SHA.
3. The artifact header, verbatim.
4. Each finding in one line: id, severity, path:line, claim.
Label every claim observed, inferred, told, or unknown.
