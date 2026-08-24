Write this directive verbatim to docs/cycles/directive-tooling-spec-18-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

ROLES. This session fills two roles in sequence: spec author for Task 1, then Spec Reviewer per roles/spec-reviewer-agent.md for Task 2. State the active role in your report where each task's output is described. No other role is in scope.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-17.md @ 1e818febf60b71558fc3fd0964f4a55d783e3bc9. Stop conditions pin to 1e818febf60b71558fc3fd0964f4a55d783e3bc9. Fetch origin as your first git act. origin/main has moved (merge commit b5fc675c644036b66f0813c4af80a596a19dacec landed the fifth skills/directive-authoring.md amendment); do not rebase or merge main into the spec branch — read the amended skill at origin/main, work on the spec branch as it stands.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c18" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c18 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-17.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (agreed, last-reviewed reviews/expedited-log.md @ 7853525aedf831bcc07da3264c3af7a91825b048 — the labelled-statement rule now reads "exactly one per directive").

TASK 1 — as spec author, revise specs/directive-tooling.md per these dispositions, which combine the cycle-17 findings with a deliberate descope. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

DESCOPE, governing everything below: the PRD carries goals, journeys, risk posture, and criteria decidable at PRD level; generator/lint interaction mechanics at the granularity of label lexical form, fence semantics beyond the stated exclusion property, and prompt-content bounds are TRD-stage decisions. Where a cycle-17 finding is about such a mechanism, its disposition is a PRD-level invariant plus a §8 question routing the mechanism to the TRD — not a mechanism stated in the PRD.

B1 — accept via the descope. State as a generator invariant, at G-level: the generated skeleton contains exactly one unfenced labelled disposition statement — the one the generator emits over the empty content slot — whatever sourced text the skeleton carries; the passes-by-construction property at J1/J2 rests on this invariant. How sourced prompt text avoids introducing a second unfenced instance (fencing of examples, prompt-content bounds, or another mechanism) is a TRD decision; add or extend the §8 question routing it there. Remove any PRD text that states the mechanism.

N1 — accept, closed by governed text: the exactly-one count is now stated by skills/directive-authoring.md (content commit 7853525aedf831bcc07da3264c3af7a91825b048); re-anchor M3's count on that sentence, cited by path and SHA; restore §7's and AC-DT-13's every-element-governed claims to true as written, removing the four-stood-one-stands disclosure.

N2 — accept via the descope: the single-source requirement for the label form is folded into the §8 label-form question (Q9), stated as a property the TRD's resolution must satisfy — generator and lint source the label from one committed definition.

N3 — accept. AC-DT-06 gains the fenced-only fixture as a shape: a directive whose only labelled statements are fenced fails M3 (zero unfenced statements); stated at the shape level consistent with Q9's literal-text deferral.

O1–O5 — no action.

Consistency: run the corpus recount and Core rule 13 sweep as the document's own rules require, labelling consequential updates at their sites.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-18.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. Gate against the descoped scope: a mechanism correctly routed to the TRD by a §8 question is not a PRD finding. A confirmation-scoped independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-18.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 18 verdict line; findings by severity; anything stopped or surfaced; the active role stated per task. Label every claim observed / inferred / told / unknown.
