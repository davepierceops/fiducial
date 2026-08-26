You are an execution session for davepierceops/fiducial. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE ASSIGNMENT. Create and use only this tree:
~~~
cd /Users/dave/code/fiducial && git fetch origin main && git worktree add --no-track -b agreeing-clusters "$TMPDIR/agreeing-clusters" origin/main && cd "$TMPDIR/agreeing-clusters"
~~~
Write this entire block, verbatim, to docs/cycles/agreeing-clusters-collapse-20260826T2120.md. Commit with message "docs/cycles: land agreeing-clusters-collapse directive". Push with `git push origin agreeing-clusters`. Verify with `git ls-remote origin agreeing-clusters`. Report "landed <path> as <sha>" using the SHA read back from git. Keychain noise ("failed to store: 100001") is not an error; the git exit code is.

REVIEWED REF: 3d13b4ca907f4cd7472768b3cdf4ec99e2fcb789 (main). The clusters file docs/rule-register/rule-clusters-20260825T1600.md and the register docs/rule-register/rule-register-20260825T1435.md were produced against f9a7a5e; PR #211 (82c0c61) has since edited files those artifacts cite, so a row's `line` is advisory and its `source` text is what locates it. Where a row's `source` text no longer exists verbatim, find its reworded successor; if none exists, treat the row as already collapsed and report it.
STOP CONDITIONS — stop and report, do not recover:
- `git diff --stat 3d13b4c -- docs/global-context context-sets policies roles skills boundaries LEXICON.md operating-model.md` is non-empty at any point before your own first content commit.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

TASK — collapse the 69 agreeing clusters C009–C077 in the clusters file into their proposed homes. For each cluster: keep the rule stated once, in the file the cluster names as `Proposed home`, and delete every other row's statement of it. Where the home file's existing text already states the rule, delete the other rows and change nothing in the home. Where the home does not yet state it in full (a row elsewhere carries a detail the home lacks), fold that detail into the home's existing sentence; do not append a new rule. Edit the minimum text; never rewrite surrounding prose. Do not touch any row outside the 69 clusters. Do not edit the register or clusters files.

BUNDLE INVARIANT — read before deleting anything. Bundle membership is the `audience:` frontmatter; a row deleted from file A survives only in bundles that carry the home B. Before deleting a row from A, confirm every audience value on A is covered by B's audience, where `all-roles` covers every value, `all-decision-roles` covers every role whose role document carries `session: decision`, and `human` covers only `human`. If B does not cover A, leave A's row unedited and report the cluster under item 5. This applies equally to the five inlined statements of the behavioural red-gate landed under PR #211's C003 ruling: collapse an inline only where the home covers its file's audience.

UNSURE HOMES — any cluster whose `Proposed home` is `unsure` (at least C022, C029, C034, C047, C053): do not edit. For each, report the candidate home you would choose and the one-line reason, for Dave's ruling.

INTRA-FILE CLUSTERS (C056 onward): the home is the same file; keep the fuller statement, delete the other rows' restatements.

STATUS: the pre-commit hook flips every edited agreed document to in-review with last-reviewed null. Those flips are expected; do not flip any status by hand and do not run bin/flip-agreed.

PROVENANCE: the cluster claims are *inferred* by the Pass 2 session. Before collapsing a cluster, read every cited row at its source and confirm the rows state the same rule; if any row in the cluster differs materially from the others on reading, stop on that cluster, leave it unedited, and report it as divergent-on-reading.

VERIFY before opening no PR: run `bin/check-frontmatter --all`; must be green apart from the standing `WARN README.md: [unmatched-glob]`. Run `bin/bundle --audience chief-of-staff | wc -l` and record the line count before and after. For each collapsed cluster, re-read the home's location and confirm the rule is stated there once and nowhere else in its cited rows.

COMMIT AND PUSH: one commit per edited file, message "dedup: <file> — collapse C0nn, C0nn, …", homes committed before the files that lose rows to them. Push with `git push origin agreeing-clusters`. Verify with `git ls-remote origin agreeing-clusters`.

DO NOT: edit files outside the clusters' cited files plus the directive; flip status by hand; open a pull request; merge; delete branches or worktrees; edit the register or clusters files.

REPORT, in this order:
1. Directive path and landed SHA.
2. Commit SHAs in order, each with `git diff --stat`.
3. Per-cluster line: collapsed | left-for-invariant | left-unsure | divergent-on-reading | already-collapsed, with the home file.
4. Unsure clusters: candidate home and reason, one line each.
5. Clusters left for the bundle invariant: the uncovered audience value and which file carries it.
6. `bin/check-frontmatter --all` result; documents now in-review, listed.
7. CoS bundle line count before and after.
Label every claim in the report observed, inferred, told, or unknown.
