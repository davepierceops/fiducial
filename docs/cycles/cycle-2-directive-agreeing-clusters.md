Cycle-2 directive for the agreeing-clusters branch. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: SOLE TREE. Continue in "$TMPDIR/agreeing-clusters" on branch agreeing-clusters; create no other tree.
Write this entire block, verbatim, to docs/cycles/cycle-2-directive-agreeing-clusters.md. Commit with message "docs/cycles: land agreeing-clusters cycle-2 directive". Push with `git push origin agreeing-clusters`. Verify with `git ls-remote origin agreeing-clusters`. Report "landed <path> as <sha>" using the SHA read back from git.

REVIEWED REF: 050ad4baaf23b22085d5ed01141fd660b6e62235 (agreeing-clusters head). Gate: reviews/agreeing-clusters-cycle-1.md @ 2acf0415 on branch agreeing-clusters-gate — fetch it with `git fetch origin agreeing-clusters-gate` and read it from that ref; do not merge it. Base: 3d13b4c (main).
STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/agreeing-clusters` is not 050ad4b before your first content commit.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

DECISIONS — one per finding; all *told* (Dave, decision session, 2026-08-26). This directive is the record.

F1 (blocking) — accepted. roles/context-quality-reviewer.md: restore one sentence in the Scope rule stating that documents under specs/ — PRD, TRD, and acceptance criteria — are gated by the Spec Reviewer, not this role. One sentence; do not restore the prior paragraph.

F2 (non-blocking) — accepted, modified. Do not restore the three deleted lines. Instead, skills/review-artifact.md gains one sentence stating the requirement itself: every review procedure emits exactly one artifact in this shape per cycle. Place it in the "What this schema governs" section beside the sentence saying the schema governs the artifact.

F3 (observation) — accepted, modified. policies/project-setup-requirements.md: delete section 4 entirely — the heading "### 4. A recorded grandfather disposition list, or none" and the sentence beneath it. Sections 1–3 stand; renumber nothing. The obligation lives in the metadata policy's grandfather clause.

Hook-made status flips are expected; flip nothing by hand.

VERIFY: `bin/check-frontmatter --all` green. Re-read each of the three edits in place. Confirm no other statement of the F1 or F2 sentence exists in the corpus (grep), so neither reintroduces a duplicate.

COMMIT AND PUSH: one commit per file, message "cycle-2 F<n>: <fix in ≤8 words>", in order F1, F2, F3. Push with `git push origin agreeing-clusters`. Verify with `git ls-remote origin agreeing-clusters`.

DO NOT: edit any other governed file; edit the register, clusters, review, or prior directive files; flip status by hand; open a pull request; merge; delete branches or worktrees.

REPORT:
1. Directive path and landed SHA.
2. Three commit SHAs with `git diff --stat`.
3. Branch head SHA, read back from git.
4. `bin/check-frontmatter --all` result.
Label every claim observed, inferred, told, or unknown.
