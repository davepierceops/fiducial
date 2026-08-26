Cycle-2 re-gate for the agreeing-clusters branch. You are the Context Quality Reviewer. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: SOLE TREE. Continue in "$TMPDIR/agreeing-clusters-gate" on branch agreeing-clusters-gate; create no other tree. Run `git fetch origin agreeing-clusters` first so ade5dad is present.
Write this entire block, verbatim, to docs/cycles/agreeing-clusters-gate-2-20260826T2230.md. Commit with message "docs/cycles: land agreeing-clusters gate-2 directive". Push with `git push origin agreeing-clusters-gate`. Verify with `git ls-remote origin agreeing-clusters-gate`. Report "landed <path> as <sha>" using the SHA read back from git.

REVIEWED REF: ade5dadee543e746bede1ac66244743810a2e1d5 (branch agreeing-clusters). Prior cycle: reviews/agreeing-clusters-cycle-1.md @ 2acf0415. Cycle-2 directive: docs/cycles/cycle-2-directive-agreeing-clusters.md @ 19acddaa. Base: 3d13b4c (main).
STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/agreeing-clusters` is not ade5dad.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

TASK — cycle-2 re-gate. Confirm F1, F2, F3 are resolved per the cycle-2 directive's decisions and that the three fixes introduced nothing new. Scope is `git diff 050ad4b..ade5dad -- roles skills policies` — three files, one of which (skills/review-artifact.md) is newly in-review and joins the reconciliation. Apply all twelve rubric criteria to the edited text; apply criterion 12 for each added sentence against the corpus. A cycle-1 finding now resolved is confirmed in the header, not re-listed.

OUTPUT — write reviews/agreeing-clusters-cycle-2.md in the review-artifact schema. `Reviewed:` cites the 26 in-review document paths @ ade5dad. `Prior cycle:` names the cycle-1 artifact. If clean, the artifact is the header and nothing else, Verdict ready.

COMMIT AND PUSH: commit with message "reviews: agreeing-clusters cycle 2 re-gate at ade5dad". Push with `git push origin agreeing-clusters-gate`. Verify with `git ls-remote origin agreeing-clusters-gate`.

DO NOT: edit any governed file; edit the register, clusters, directive, or prior review files; flip status; open a pull request; merge; delete branches or worktrees.

REPORT, in this order:
1. Directive path and landed SHA.
2. Review artifact path and commit SHA.
3. The artifact's header block, verbatim.
4. Any findings, one line each.
Label every claim observed, inferred, told, or unknown.
