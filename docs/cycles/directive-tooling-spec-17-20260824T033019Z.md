Write this directive verbatim to docs/cycles/directive-tooling-spec-17-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

ROLES. This session fills two roles in sequence: spec author for Task 1, then Spec Reviewer per roles/spec-reviewer-agent.md for Task 2. State the active role in your report where each task's output is described. No other role is in scope.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-16.md @ 91ea85115ebcabc0dfc241ee08a2721412783ff3 — the third independent gate. Stop conditions pin to 91ea85115ebcabc0dfc241ee08a2721412783ff3. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c17" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c17 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-16.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (last-reviewed reviews/expedited-log.md @ b4a0fa581ba5c64ac5a0e5374b5604e979a73653 — the labelled-statement rule and the carry-as-pointer rule with its origin exception).

TASK 1 — as spec author, revise specs/directive-tooling.md per these dispositions of the cycle-16 findings. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept. The generated skeleton carries the labelled disposition statement itself: the TRD-fixed label emitted by the generator, content slot empty, so a faithful author sees the exact form M3 matches and fills content only. Restate AC-DT-03 from "author region present and blank" to "labelled statement present with empty content slot, author fills the content"; reconcile AC-DT-06 fixture (v) to the same wording so the two criteria agree; state at J1/J2 that the ordinary generated path passes the lint by construction once the content is filled.

N1 — accept, disposition: fence-scoped exactly-one. M3 counts labelled disposition statements outside fenced code blocks only, and requires exactly one; text inside fences is outside M3's match. Ground, stated: dictated and quoted wording travels in fences under the carry-as-pointer rule's origin exception, so a directive originating other directives' labelled statements carries them fenced and passes, while the motivating incident — no labelled statement at all — still fails. The fence exclusion is M3's only markdown sensitivity, stated at PRD level as such; finer markdown-awareness is a TRD concern. Restate §7's residual accordingly: the accepted false positive becomes a labelled statement quoted outside a fence, and the false-negative item (a labelled statement whose content is false) stands. AC-DT-06 gains a fixture: a directive with one unfenced labelled statement plus fenced labelled statements passes.

N2 — accept. §8 gains the question tracking the label-form deferral: the TRD fixes the label's lexical form; until then M3's fixtures state shape, not literal text; resolved-by the TRD stage.

N3 — accept. Recast §1's motivating-incident paragraph in past tense as the incident's record, with the governed requirement cited at its current form rather than restated narrower.

N4 — accept. Extend the conflict-disposition clause to cover generator/lint conflicts generally, not only conflicts with preserved AC-CO criteria — one clause, stating such conflicts surface as spec defects at review.

O6 — accept. §1's gate record names cycle 13's gate directive alongside cycle 8's, by path.

O1–O5 — no action.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-17.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. A confirmation-scoped independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-17.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 17 verdict line; findings by severity; anything stopped or surfaced; the active role stated per task. Label every claim observed / inferred / told / unknown.
