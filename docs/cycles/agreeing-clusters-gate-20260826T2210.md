You are an execution session for davepierceops/fiducial, acting as the Context Quality Reviewer. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE ASSIGNMENT. Create and use only this tree:
~~~
git fetch origin agreeing-clusters && git worktree add --no-track -b agreeing-clusters-gate "$TMPDIR/agreeing-clusters-gate" origin/agreeing-clusters && cd "$TMPDIR/agreeing-clusters-gate"
~~~
Write this entire block, verbatim, to docs/cycles/agreeing-clusters-gate-20260826T2210.md. Commit with message "docs/cycles: land agreeing-clusters gate directive". Push with `git push origin agreeing-clusters-gate`. Verify with `git ls-remote origin agreeing-clusters-gate`. Report "landed <path> as <sha>" using the SHA read back from git. Keychain noise ("failed to store: 100001") is not an error; the git exit code is.

REVIEWED REF: 050ad4baaf23b22085d5ed01141fd660b6e62235 (branch agreeing-clusters). Base: 3d13b4ca907f4cd7472768b3cdf4ec99e2fcb789 (main). Decision record: docs/cycles/agreeing-clusters-collapse-20260826T2120.md @ 3dc7e796 and docs/cycles/agreeing-clusters-collapse-2-20260826T2200.md @ 716171bb. Prior cycle: none.
STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/agreeing-clusters` is not 050ad4b.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

LOAD YOUR ROLE: run `bin/bundle --audience context-quality-reviewer > "$TMPDIR/cqr-bundle.md"` and read it in full before reviewing.

TASK — cycle-1 gate over one reconciliation: the deletion of duplicated rules across the corpus, each rule kept once in a stated home. Scope is `git diff 3d13b4c..050ad4b -- docs/global-context context-sets policies roles skills boundaries LEXICON.md operating-model.md` — 25 governed documents, all now in-review. Apply all twelve rubric criteria to the edited text. For criterion 12 the specific test is: for every rule a diff hunk deletes, confirm the home file states it, and states it the same way; a deleted rule with no surviving statement is a blocking defect. Also confirm, per the two directives' bundle invariant, that every deleted statement's file has an `audience:` covered by its home's, except the three clusters (C049–C051) Dave ruled cut regardless. Read the two directives for the rulings; a deletion they authorize is not a finding for being a deletion.

OUTPUT — write reviews/agreeing-clusters-cycle-1.md in the review-artifact schema. `Reviewed:` cites the 25 document paths @ 050ad4b. If clean, the artifact is the header and nothing else, Verdict ready.

COMMIT AND PUSH: commit with message "reviews: agreeing-clusters cycle 1 gate at 050ad4b". Push with `git push origin agreeing-clusters-gate`. Verify with `git ls-remote origin agreeing-clusters-gate`.

DO NOT: edit any governed file; edit the register, clusters, or directive files; flip status; open a pull request; merge; delete branches or worktrees.

REPORT, in this order:
1. Directive path and landed SHA.
2. Review artifact path and commit SHA.
3. The artifact's header block, verbatim.
4. Any findings, one line each: id, document, claim.
Label every claim in the report observed, inferred, told, or unknown.
