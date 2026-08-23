Write this directive verbatim to docs/cycles/directive-tooling-spec-3-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-2.md @ e19100198e13135a93e0e044767722890929b8b0. Stop conditions pin to e19100198e13135a93e0e044767722890929b8b0. Fetch origin as your first git act. Note origin/main has moved past the spec branch's base (merge commit 820d071edeaf6a36284235c888b043298fe44377 landed the amended skills/directive-authoring.md); do not rebase or merge main into the spec branch — read the amended skill at origin/main, work on the spec branch as it stands.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c3" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c3 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-2.md and both prior directive files on this branch; specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (agreed, last-reviewed reviews/expedited-log.md @ 48ad7fd1e827a7c92660fd2cd9ebc5871c1dbc21 — the mandatory working-tree-disposition rule this cycle depends on); docs/packages/package-a-spec.md §3.6 and bin/tests/test_cycle_open.py; decisions/log.md entries DEC-000150, DEC-000160, DEC-000180 at origin/main.

TASK 1 — revise specs/directive-tooling.md per these dispositions. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: two forms, mode-determined. The generator's cycle mode emits docs/cycles/cycle-<N>-directive.md per package-a-spec AC-CO-1; every other mode emits <descriptor>-<timestamp>.md per Core rule 14. M8 becomes a two-pattern check accepting exactly these two forms. Core rule 14 already yields to a stated convention, so both governed sources stay licensed and neither is amended. The 37 historical non-conforming files are not retrofitted; the lint governs directives written after adoption.

B2 — accept. The migration section names docs/packages/package-a-spec.md §3.6 and AC-CO-1 through AC-CO-12 as the governing contract for the skeleton being moved, states that the generalize disposition preserves that contract intact under the cycle mode, and names bin/tests/test_cycle_open.py as the test surface that must stay green through migration.

N1 — accept, and the prerequisite is discharged: skills/directive-authoring.md at origin/main now states the mandatory working-tree-disposition rule as agreed governed text. Remove the prerequisite framing from §1, §4 G6, the M3 row, §7, and AC-DT-13; cite the amended skill by path and content-commit SHA 48ad7fd1e827a7c92660fd2cd9ebc5871c1dbc21; write the AC-DT-06 test the prerequisite blocked; close the Q4 sequencing item.

N2 — accept. G11's manifest locates each sourced section's extent, not only its source, so §5's first signal is computable; state the mechanism.

N3 — accept, disposition: supersession by new entry. The spec states, as an implementation-landing requirement, that a new decision-log entry supersedes the cycle-open obligation-bearing references in DEC-000150 and DEC-000180 — whole-entry supersession per the log's append-only rule. No log edit in this cycle.

O1 — dispose: the cycle-1 O1 question (governed home for the mandatory rule) is resolved by the expedited amendment above; record that disposition where the spec carries the question.

O2, O4 — no action. O3 — no action in this cycle; the stale AC-CO-3 pointer is outside this blast radius and is tracked by the decision session.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-3.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-3.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 3 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
