Reviewer gate over branch retire-bundle-methodology. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE. Create the tree with `git worktree add --no-track "$TMPDIR/retire-bundle-methodology-gate" -b retire-bundle-methodology-gate origin/retire-bundle-methodology` from the main clone and work only there. If the add fails for any reason, stop and report; do not retry with different flags.
Write this entire block, verbatim, to docs/cycles/retire-bundle-methodology-gate-20260827T0135.md. Commit with message "docs/cycles: land retire-bundle-methodology-gate directive". Push with `git push origin retire-bundle-methodology-gate`. Verify with `git ls-remote origin retire-bundle-methodology-gate`. Report "landed <path> as <sha>" using the SHA read back from git.

ROLE: Reviewer Agent (roles/reviewer-agent.md), execution session. You gate; you do not edit the reviewed change.

REVIEWED REF: 999675b7f8770210a70b6a0b33de9bc770d379e3 (retire-bundle-methodology head). Baseline: 0ee38821648ece6def9c1cbba84ca7f089b3d881 (main). Governing decision: decisions/log.md DEC-000210. Execution directive: docs/cycles/retire-bundle-methodology-20260827T0120.md @ c695d881.

STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/retire-bundle-methodology` is not 999675b before you begin.
- Any tree mutation you did not intend, including your own.
- Any push fails.

SCOPE: the diff 0ee3882..999675b. Confirm: exactly three files removed and nothing else changed; the removal is what DEC-000210 orders and no more; no surviving file under bin/ imports, invokes, or depends on the removed files (bin/tests/test_bundle_audience.py mentions the old tool in comments only — confirm that reading); bin/tests/run at 999675b passes with failures=0, verified by running, output captured to "$TMPDIR/gate-tests.txt"; bin/check-frontmatter --all exits 0; `bin/bundle --audience chief-of-staff | wc -l` is 3217 at both refs.

ARTIFACT: write reviews/retire-bundle-methodology-cycle-1.md per skills/review-artifact.md. Reviewed: the three removed paths @ 999675b. Baseline: 0ee3882. Prior cycle: none. Evidence lines say verified by running or inferred by reading. Verdict is ready, ready-with-findings, or changes-required.

COMMIT AND PUSH: one commit, message "reviews: retire-bundle-methodology cycle 1 — <verdict>". Push with `git push origin retire-bundle-methodology-gate`. Verify with `git ls-remote origin retire-bundle-methodology-gate`.

DO NOT: edit any file other than the review artifact and this directive; open a pull request; merge; delete branches or worktrees.

REPORT:
1. Directive path and landed SHA.
2. Artifact path and commit SHA.
3. The artifact header, verbatim.
4. Each finding in one line: id, severity, location, claim.
Label every claim observed, inferred, told, or unknown.
