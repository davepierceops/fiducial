Write this directive verbatim to docs/cycles/directive-tooling-spec-11-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-10.md @ 6a1b18a560c41ff0f133a82e40940c18aac8b3f1. Stop conditions pin to 6a1b18a560c41ff0f133a82e40940c18aac8b3f1. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c11" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c11 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-10.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main.

TASK 1 — revise specs/directive-tooling.md per these dispositions of the cycle-10 findings. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: scope M3 to the author region. M3's search for the stated disposition runs over the author region of the working-tree slot as the manifest locates it, not the whole file; the sourced prompt region naming both admitted forms is outside M3's search by that scoping. State the scope in M3's own text; AC-DT-06 gains two fixtures — a correctly-filled directive (prompt region present, author region carrying one form: passes) and an unfilled one (prompt region present, author region empty: fails, the motivating incident's mechanical catch). State the scoping wherever M3's behavior is described so no site implies a whole-file search.

N1 — accept, disposition: delimit by enumeration. AC-DT-02's excluded structural class is a stated character set, not a named category: a line consisting solely of whitespace and characters from the set - = ~ ` # * _ | > + is excluded. State the set as the criterion's own contract, note it is the criterion's test-selection rule rather than a rule imposed on any governed file, and keep --- as the demonstrating exclusion.

N2 — accept. Reconcile §2 to the two freehand regions §3, §4, and §6 now state: the decision session authors the task-specific middle and the author region of the working-tree slot; §2's one-region phrasing is corrected everywhere it appears.

O2 — the cycle-9 subsumption premise failing re-derivation is already handled by the seven-fixture state; confirm the fixture list and relation text are consistent with it and make no further change.

O1, O3, O4 — no action.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-11.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. An independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-11.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 11 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
