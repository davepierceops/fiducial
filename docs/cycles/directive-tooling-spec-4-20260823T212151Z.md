Write this directive verbatim to docs/cycles/directive-tooling-spec-4-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-3.md @ 83e6eed6da82eedd0f137bff99e39758e6a0a830. Stop conditions pin to 83e6eed6da82eedd0f137bff99e39758e6a0a830. Fetch origin as your first git act. origin/main has moved (merge commit 073ca7471923f1f52819ea748bc9988a76f86262 landed the second skills/directive-authoring.md amendment); do not rebase or merge main into the spec branch — read the amended skill at origin/main, work on the spec branch as it stands.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c4" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c4 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-3.md and the three prior directive files on this branch; specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (agreed, last-reviewed reviews/expedited-log.md @ 83b60511f4cc6e0346b08e4e111a7c17a14bc0d9 — its Naming section now licenses both filename forms); docs/packages/package-a-spec.md §3.6; bin/tests/test_cycle_open.py.

TASK 1 — revise specs/directive-tooling.md per these dispositions. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: mode-scoped refusal. The cycle mode preserves its inherited contract's refusals (AC-CO-1, -2, -5, -6, -12) intact; the general mode refuses no directive — the lint gates downstream. G4 and AC-DT-04 are restated as claims about the general mode only, and the spec states the scoping explicitly so the two modes' claims cannot be read globally again. AC-DT-15's stay-green requirement on bin/tests/test_cycle_open.py is unaffected and stays.

B2 — accept. Align §6 to §4's Security NFR, which already states the reconcilable version: AC-DT-12 is restated so the mutation prohibition binds the general mode and the lint, while the cycle mode's contract-required writes (directive file, bundle, per AC-CO-1/-7) are licensed as the preserved contract states them.

N1 — accept. M2's check enforces what its Derived-from cites, or the Derived-from narrows to what the check enforces — state which and make the two consistent; the spec's own citations must pass the stated check.

N2 — accept, and the prerequisite is discharged: skills/directive-authoring.md at origin/main now licenses both forms in its Naming section (content commit 83b60511f4cc6e0346b08e4e111a7c17a14bc0d9). Re-anchor M8's second form on that sentence; remove any scheduling language for an amendment that has now landed.

N3 — accept, disposition: extend the implementation-landing requirement so the same landing that supersedes the decision-log references also updates the OPEN-ITEMS.md Track-guard reference to bin/cycle-open. A tracker edit, not a log edit; no edit in this cycle.

O3 — accept as a wording fix: state which party AC-DT-16 binds (the decision session at implementation landing) so the criterion is not read as an implementer obligation.

O1, O2, O4 — no action. The dual count (37 single-pattern / 29 two-pattern) stays as recorded with provenance; the stale AC-CO-3 pointer remains tracked by the decision session; build-gating and the pre-existing red pair carry unchanged.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-4.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-4.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 4 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
