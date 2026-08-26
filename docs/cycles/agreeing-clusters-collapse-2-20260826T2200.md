Second directive for the agreeing-clusters branch. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: SOLE TREE. Continue in "$TMPDIR/agreeing-clusters" on branch agreeing-clusters; create no other tree.
Write this entire block, verbatim, to docs/cycles/agreeing-clusters-collapse-2-20260826T2200.md. Commit with message "docs/cycles: land agreeing-clusters-collapse-2 directive". Push with `git push origin agreeing-clusters`. Verify with `git ls-remote origin agreeing-clusters`. Report "landed <path> as <sha>" using the SHA read back from git.

REVIEWED REF: 9e1adadff5bbe366b92d8734895d7a86b93499b9 (agreeing-clusters head). Your report of 2026-08-26 against docs/cycles/agreeing-clusters-collapse-20260826T2120.md @ 3dc7e796 is the input; this block records Dave's rulings on its items 3–5 and the residual duplicate.
STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/agreeing-clusters` is not 9e1adad before your first content commit.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

RULINGS (all *told* — Dave decided in chat; this directive is the record):

R1 — Unsure homes accepted as you proposed. Collapse: C022 → policies/project-setup-requirements.md; C029 → skills/review-artifact.md; C034 → policies/commit-and-change-control-policy.md; C047 → policies/verification-boundary-policy.md; C053 → policies/source-of-truth-policy.md. The bundle invariant from the first directive still applies to each; leave and report any that fail it.

R2 — Bundle-invariant clusters. C049, C050, C051: cut anyway. No role other than the Chief of Staff needs its procedure; operating-model.md's Chief of Staff subsection under Responsibilities becomes one sentence stating that the role assesses state and proposes the next step, operating as a decision session — nothing more. The full text stays in roles/chief-of-staff.md. C030 and C039: leave as they are; accepted duplicates.

R3 — The 35 divergent-on-reading clusters: accepted as not-duplicates; no edit. Dave will rule separately on the subset that are real divergences.

R4 — The five C003 red-gate inlines: leave all five.

R5 — policies/release-readiness-policy.md line 18 (routine changes flow to release on evidence; consequential needs an explicit go): collapse into the C013 home, policies/commit-and-change-control-policy.md, under the invariant.

The first directive's rules on minimum edits, folding detail into the home rather than appending, hook-made status flips being expected, and no hand flips all still bind.

VERIFY: `bin/check-frontmatter --all` green. For each collapsed cluster and R5, re-read the home and confirm the rule stands there once and nowhere else in the rows you removed. Record `bin/bundle --audience chief-of-staff | wc -l` after.

COMMIT AND PUSH: one commit per edited file, message "dedup-2: <file> — <clusters or R-number>", homes first. Push with `git push origin agreeing-clusters`. Verify with `git ls-remote origin agreeing-clusters`.

DO NOT: touch any cluster not named in R1, R2, R5; open a pull request; merge; delete branches or worktrees; edit the register or clusters files; flip status by hand.

REPORT:
1. Directive path and landed SHA.
2. Commit SHAs in order with `git diff --stat`.
3. Per-cluster line for R1, R2 (C049–C051), R5: collapsed | left-for-invariant, with the home.
4. `bin/check-frontmatter --all` result; the full in-review list now on the branch.
5. CoS bundle line count after.
Label every claim observed, inferred, told, or unknown.
