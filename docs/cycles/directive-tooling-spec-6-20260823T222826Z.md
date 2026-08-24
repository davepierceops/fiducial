Write this directive verbatim to docs/cycles/directive-tooling-spec-6-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-5.md @ 545903d8f906889a3c98ae11756e7bd6320470e6. Stop conditions pin to 545903d8f906889a3c98ae11756e7bd6320470e6. Fetch origin as your first git act. origin/main has moved (merge commit e01d9e00914694f47abc313e787a14f3dc5b9f8b landed the third skills/directive-authoring.md amendment); do not rebase or merge main into the spec branch — read the amended skill at origin/main, work on the spec branch as it stands.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c6" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c6 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-5.md and the five prior directive files on this branch; specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (agreed, last-reviewed reviews/expedited-log.md @ 6179221a013e8006e573d6a35a4dca75dd966ccb — its Naming section now requires date and time components both present); docs/packages/package-a-spec.md §3.6 AC-CO-1; bin/cycle-open and bin/tests/test_cycle_open.py.

TASK 1 — revise specs/directive-tooling.md per these dispositions. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: scope M8's claim. M8 asserts form-set membership only — the filename matches one of the three licensed patterns — and asserts nothing about mode-appropriateness, which no filename check can decide. Mode-appropriateness is guaranteed by the generator by construction and stated as such in §4; the residual (a hand-written general-mode directive named <slug>-directive.md passes M8) is stated explicitly as an accepted minor defect class, with the generator's adoption as the mitigation. Restate AC-DT-06's claim scope accordingly.

B2 — accept, and the prerequisite is discharged: skills/directive-authoring.md at origin/main now states the timestamp form requires date and time components both present (content commit 6179221a013e8006e573d6a35a4dca75dd966ccb). Re-anchor M8's time-component rule on that governed sentence; restore AC-DT-13's "as written" claim and §7's Not-accepted item to true; remove any carve-out or stricter-than-source framing.

N1 — accept. Define the slug character class as the lint's own stated contract in M8 (lowercase alphanumerics and hyphens, no leading or trailing hyphen), noted as the lint's normalization of a class AC-CO-1 leaves unstated — the lint's contract, not a claim about cycle-open's behavior; the recount criterion cites it.

N2 — accept. AC-DT-17's fixtures (and AC-DT-09's, same property) are restated as synthetic cases embedded in the offline fixture repo, constructed to the same shape as the historical instances they replace; the historical files are cited as provenance in prose, not as test inputs. §6's offline-testability preamble becomes true as written.

O4 — accept as a baseline restatement: §5's third signal re-baselines against the three-pattern check (1 non-conforming of 97) with provenance, or is narrowed to the signal the recount still supports; state which.

O1, O2, O3 — no action in this cycle. O1 is disposed at the process level: the next gate after this cycle runs as an independent review-only session, recorded here for the audit trail.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-6.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-6.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 6 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
