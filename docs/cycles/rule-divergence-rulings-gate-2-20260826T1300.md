You are an execution session for davepierceops/fiducial, acting as the Context Quality Reviewer. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE ASSIGNMENT. Create and use only this tree:
~~~
cd /Users/dave/code/fiducial && git fetch origin rule-divergence-rulings-cycle-2 && git worktree add --no-track -b rule-divergence-rulings-gate-2 "$TMPDIR/rule-divergence-rulings-gate-2" origin/rule-divergence-rulings-cycle-2 && cd "$TMPDIR/rule-divergence-rulings-gate-2"
~~~
Write this entire block, verbatim, to docs/cycles/rule-divergence-rulings-gate-2-20260826T1300.md. Commit with message "docs/cycles: land rule-divergence-rulings gate-2 directive". Push with `git push origin rule-divergence-rulings-gate-2`. Verify with `git ls-remote origin rule-divergence-rulings-gate-2`. Report "landed <path> as <sha>" using the SHA read back from git. Keychain noise ("failed to store: 100001") is not an error; the git exit code is.

REVIEWED REF: 3e064f6e4175684633b79498ead44361b1d41fb9 (branch rule-divergence-rulings-cycle-2). Prior cycle: reviews/rule-divergence-rulings-cycle-1.md @ 1d67b6b. Cycle-2 directive: docs/cycles/cycle-2-directive-rule-divergence-rulings.md @ c778d6b. Base: d1086a56f9c4214fe120560afb865af8b79353bd (main).
STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/rule-divergence-rulings-cycle-2` is not 3e064f6.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

LOAD YOUR ROLE: run `bin/bundle --audience context-quality-reviewer > "$TMPDIR/cqr-bundle.md"` and read it in full before reviewing.

TASK — cycle-2 re-gate of the same reconciliation. Confirm every cycle-1 finding is resolved per the cycle-2 directive's decisions, and that the fixes introduced nothing new. Scope is `git diff d1086a5..3e064f6 -- docs/global-context context-sets policies roles skills LEXICON.md operating-model.md CLAUDE.md` — ten governed documents. Apply all twelve rubric criteria to the edited text; apply criterion 12 to the corpus for any rule the cycle-2 edits touched. A finding you raised in cycle 1 that is now resolved is confirmed in the header, not re-listed.

specs/directive-tooling.md is also in the diff (N4: a quoted line updated). It is outside your gate — the Spec Reviewer gates specs. Inspect the diff, report in `Not inspected:` that the spec's agreement is not yours to gate, and in prose state in one line whether the diff is confined to the quotation.

OUTPUT — write reviews/rule-divergence-rulings-cycle-2.md in the review-artifact schema. `Reviewed:` cites the ten document paths @ 3e064f6. `Prior cycle:` names the cycle-1 artifact. If clean, the artifact is the header and nothing else, Verdict ready.

COMMIT AND PUSH: commit with message "reviews: rule-divergence-rulings cycle 2 gate at 3e064f6". Push with `git push origin rule-divergence-rulings-gate-2`. Verify with `git ls-remote origin rule-divergence-rulings-gate-2`.

DO NOT: edit any governed file; edit the register, clusters, or prior review files; flip status; open a pull request; merge; delete branches or worktrees.

REPORT, in this order:
1. Directive path and landed SHA.
2. Review artifact path and commit SHA.
3. The artifact's header block, verbatim.
4. Any findings, one line each: id, document, claim.
5. The one-line spec diff statement.
Label every claim in the report observed, inferred, told, or unknown.
