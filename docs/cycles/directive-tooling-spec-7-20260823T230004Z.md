Write this directive verbatim to docs/cycles/directive-tooling-spec-7-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-6.md @ d8f8d7a6a8c7d47761383d32dfcd3cd6161f6bb8. Stop conditions pin to d8f8d7a6a8c7d47761383d32dfcd3cd6161f6bb8. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c7" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c7 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-6.md and the six prior directive files on this branch; specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main; docs/packages/package-a-spec.md §3.6 AC-CO-1; bin/cycle-open.

TASK 1 — revise specs/directive-tooling.md per these dispositions. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: drop the slug character class. M8's slug pattern accepts any filename of the form <slug>-directive.md that the preserved contract can emit; no character-class constraint, because no governed file states one and the spec's own G6 forbids the lint enforcing an unstated rule — cite G6 as the ground. The looseness this admits is covered by the mode-appropriateness residual §7 already accepts. AC-DT-13's "as written" claim and §7's Not-accepted item return to true; the AC-DT-06 fixture set follows the pattern as restated; the recount is unchanged (state so, with the cycle-6 verification as provenance).

B2 — accept. Add the mode-appropriateness residual to AC-DT-08's unchecked set, so a lint built to §6 discloses the bound §7 accepts; one clause, worded to match §7's statement of the residual.

N1 — accept, resolved by B1: the fixture set reflects M8 as restated, with no class-boundary cases.

N2 — accept, disposition: drop the term. Remove "concurrently-live" and narrow the third outcome to what the recount reproduces without it; the spec states the narrowing.

O1–O4 — no action. The independent gate after this cycle stands as recorded in the cycle 6 directive.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-7.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-7.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 7 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
