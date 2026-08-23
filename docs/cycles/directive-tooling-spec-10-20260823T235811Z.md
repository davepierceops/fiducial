Write this directive verbatim to docs/cycles/directive-tooling-spec-10-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-9.md @ 714d2c94a688257e424ff4f9aff9906fe7fdeb74. Stop conditions pin to 714d2c94a688257e424ff4f9aff9906fe7fdeb74. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c10" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c10 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-9.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main; docs/global-context/core.md and docs/global-context/decision-layer.md at origin/main.

TASK 1 — revise specs/directive-tooling.md per these dispositions of the cycle-9 findings. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: split the slot. The working-tree disposition region divides into two: a sourced prompt region — invariant, read from committed text, carrying the requirement that a disposition be stated and the two legal forms per skills/directive-authoring.md — and an author region carrying the actual assignment or sole-tree declaration. Each region carries exactly one classification in G11's manifest; G1 lists the prompt region among invariant sections, G3/J1/AC-DT-03 have the author fill the author region only; §5's first measurement and AC-DT-05's partition become well-defined over the split. State the split wherever the slot is named so no site retains the dual classification.

N1 — accept. AC-DT-02's reproduced line must be non-blank and must not consist solely of structural delimiters or punctuation (state the rule as the criterion's own contract, with --- named as the demonstrating exclusion); exact match after whitespace normalization stands.

N2 — accept. State the <SLUG>-is-one-path-component reading as an explicit step in the B2 ground — AC-CO-1's destination clause locates the output at docs/cycles/<SLUG>-directive.md, a single directory level, so <SLUG> denotes one path component — then the sub/nested and ../escaped conclusions follow from it; keep both fixtures.

O2 — accept. Drop the subsumed fixture; state which fixture subsumes it.

O5 — accept. Add the provenance line at G2 recording the cycle-9 narrowing and its directive.

O1, O3, O4 — no action.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-10.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. An independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-10.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 10 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
