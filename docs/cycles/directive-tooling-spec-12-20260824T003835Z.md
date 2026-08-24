Write this directive verbatim to docs/cycles/directive-tooling-spec-12-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-11.md @ 3749d8a94e0be0ad8e7ddc6b8fa9525b6026534a. Stop conditions pin to 3749d8a94e0be0ad8e7ddc6b8fa9525b6026534a. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c12" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c12 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-11.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main.

TASK 1 — revise specs/directive-tooling.md per these dispositions of the cycle-11 findings. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: whole-file fallback. M3 runs region-scoped where a G11 manifest exists and whole-file where none does. Ground, stated in the spec: a manifest-less directive carries no generator-written prompt region, so a whole-file search cannot false-positive on sourced text naming both forms. AC-DT-06's hand-written fixtures are decidable under the fallback and keep their dictated exits; AC-DT-10's undecidability rule no longer reaches M3, and the two criteria agree. State the fallback in M3's own text and at every site that describes M3's scope, so no site implies the manifest is required.

N1 — accept. Correct "the three failing fixtures" to the actual enumeration — four of seven fail — naming the date-with-no-time fixture in it.

N2 — accept. Repair the two stale deictics in §4's recount paragraph to name cycle 9 explicitly.

O4 — accept, resolved under B1's disposition: state in §7 what residual the fallback leaves — a hand-written directive that pastes the generated prompt text without a manifest is searched whole-file and may false-positive on the pasted forms — as an accepted minor residual with the generator's adoption as mitigation; if on execution you determine the fallback leaves no residual, state that instead, with the ground.

O1, O2, O3 — no action.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-12.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. The independent gate follows this cycle regardless of your verdict; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-12.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 12 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
