You are an execution session for davepierceops/fiducial. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE ASSIGNMENT. Create and use only this tree:
~~~
cd /Users/dave/code/fiducial && git fetch origin main && git worktree add --no-track -b rule-divergence-rulings "$TMPDIR/rule-divergence-rulings" origin/main && cd "$TMPDIR/rule-divergence-rulings"
~~~
Write this entire block, verbatim, to docs/cycles/rule-divergence-rulings-20260825T1900.md. Commit with message "docs/cycles: land rule-divergence-rulings directive". Push with `git push origin rule-divergence-rulings`. Verify with `git ls-remote origin rule-divergence-rulings`. Report "landed <path> as <sha>" using the SHA read back from git. Keychain noise ("failed to store: 100001") is not an error; the git exit code is.

REVIEWED REF: d1086a56f9c4214fe120560afb865af8b79353bd (main). Governed files are unchanged since f9a7a5e8b4c695e8aa52549e180dae277da94a28; the cluster analysis at docs/rule-register/rule-clusters-20260825T1600.md and the register at docs/rule-register/rule-register-20260825T1435.md were produced against that ref.
STOP CONDITIONS — stop and report, do not recover:
- `git diff --stat f9a7a5e -- docs/global-context context-sets policies roles skills LEXICON.md operating-model.md` is non-empty.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

TASK — apply eight rulings by Dave (2026-08-25, decision session) on the divergent clusters C001–C008 in the clusters file. Read the clusters file and the register rows each cluster cites before editing; the row's `file`, `line`, and `source` locate the text. Edit the minimum text that makes every row in the cluster agree with the ruling. Do not touch any row outside these eight clusters. Do not flip any `status:`. Do not edit the register or clusters files.

RULINGS — one entry per cluster; this directive is the decision record.

C001 (disagreement handling): the source-of-truth policy wins for its case only. General rule stays as Core states it: surface and continue. Core rule 9 gains one stated exception: a conflict between a canonical document and an artifact derived from it stops the session and waits for Dave. The policy's text stays; reword only if it claims to be the general rule.

C002 (release-impact labels): add `not-material` to the mock-checklist enumeration in context-sets/testing-and-verification.md so it lists LEXICON's four labels. Keep it enumerated; do not replace with a pointer.

C003 (red-gate strength): the behavioural red wins everywhere. Every statement of the red-gate — operating-model.md, roles/test-designer-agent.md, and any other row in the cluster — requires that the tests demonstrably fail on wrong logic, not only on a missing import. Use the wording context-sets/spec-and-change-discipline.md already carries as the source; carry it as a pointer where the rubric permits, inline where the reader is an execution session that will not hold that file.

C004 (when a retro runs): the skill wins. docs/global-context/decision-layer.md rule 12 gains the exclusion: a reviewer-gated cycle conversation runs no retro unless directed; its cycle directive is its decision record. The skill's text stays.

C005 (directive parts): amend docs/global-context/review-rubric.md criterion 8 to check all three parts — route, model, and the execution block — matching Core's Directive definition.

C006 (meaning of blocking): the Skeptic role wins. LEXICON.md's definition of `blocking` narrows to: a gap the governing policies prohibit releasing with. A gap awaiting Dave's judgment is not blocking by that fact alone; it reaches him through the release package. Adjust any other row in the cluster that repeats the wider definition.

C007 (propagating a changed fact): split by session kind. Core rule 13 is reworded: an execution session carrying a directive updates every place that states the changed fact, within the files the directive permits, and names any place outside them; a decision session names every place and edits none. The source-of-truth policy's "flag derived artifacts" text is reconciled to say the same thing for its case.

C008 (clean pass format): wording only. Core rule 10's clean-pass sentence becomes: a clean pass says so in one line, or in the artifact header where a review artifact is required. The review-artifact schema stays.

PROVENANCE: every ruling above is *told* — Dave decided it in chat; this directive is where it lands. The cluster claims are *inferred* by the Pass 2 session; confirm each divergence against `source` before editing, and if a cluster's divergence does not hold on reading, stop on that cluster, leave it unedited, and report it.

VERIFY before committing: run `bin/check-frontmatter --all`; must be green. For each of the eight clusters, re-read every cited row's location and confirm the texts now agree with the ruling. Report per cluster: files edited, lines changed (from `git diff --stat`), agree/still-diverges.

COMMIT AND PUSH: one commit per cluster, message "C00n: <ruling in ≤10 words>", in order C001–C008. Push with `git push origin rule-divergence-rulings`. Verify with `git ls-remote origin rule-divergence-rulings`.

DO NOT: edit files outside the eight clusters' cited files plus the directive; flip status; open a pull request; merge; delete branches or worktrees; edit the register or clusters files.

REPORT, in this order:
1. Directive path and landed SHA.
2. Eight commit SHAs, one per cluster, with `git diff --stat` per commit.
3. Per-cluster verification line.
4. Any cluster left unedited and why.
5. `bin/check-frontmatter --all` result.
6. Any place a ruling forced you to touch text outside the cluster's cited rows, with file and line.
Label every claim in the report observed, inferred, told, or unknown.
