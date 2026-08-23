Write this directive verbatim to docs/cycles/directive-tooling-spec-2-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md @ bd09720a on branch directive-tooling-spec, per reviews/directive-tooling-cycle-1.md @ cfb2501454454ba620d8a5fe0602633864944ace. Stop conditions pin to cfb2501454454ba620d8a5fe0602633864944ace. Fetch origin as your first git act.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c2" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c2 (a local working branch; the remote branch is checked-out state you cannot claim). Push via git push origin HEAD:directive-tooling-spec.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973, extended by cycle 1's observations:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Push without -u; upstream tracking cannot be set from a $TMPDIR worktree.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-1.md and docs/cycles/directive-tooling-spec-20260823T194242Z.md on this branch; specs/directive-tooling.md @ bd09720a; decisions/log.md entries DEC-000110, DEC-000160, DEC-000180 at origin/main; bin/cycle-open source; skills/directive-authoring.md, docs/global-context/core.md, docs/global-context/decision-layer.md at origin/main.

TASK 1 — revise specs/directive-tooling.md per these dispositions. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: generalize. bin/cycle-open becomes a mode of bin/directive: one generator, one home for invariant text. The spec states this relationship explicitly, licenses that implementation and no other, states the migration scope (cycle-open's skeleton emission moves; nothing else claimed at PRD level), and removes the assertion that no generator exists.

B2 — accept, disposition: mandatory always. Every directive states its working-tree disposition explicitly: either an exclusive assignment (named directory plus the command creating it) or a literal sole-tree declaration. The lint checks presence of exactly one of the two, unconditionally, in every directive. M3 is no longer conditional; close Q3 and Q7 accordingly; rewrite AC-DT-06 as an unconditional presence check; §3 J3's must-prevent claim now rests on a mechanically checkable element and stays.

B3 — accept. Cite DEC-000110, DEC-000160, DEC-000180 where they govern; close or narrow Q5 against what the log already answers; every governing decision cited by ID.

N1 — accept. The skeleton carries the claim-label requirement as an instruction to the executor, not text asserting labels the generator cannot hold; restate AC-DT-11 accordingly.

N2 — accept. Q1 (where invariant text lives) remains open, resolved-by Dave at the TRD stage; restate AC-DT-02 so it is decidable independent of Q1, or pin it explicitly as unwritable until Q1 resolves and say which.

N3 — accept. Name the attribution mechanism for §5's first signal or drop the signal; relabel the inference carried as observed.

O2 — no edit to specs/bin-land.md, which stays forbidden; add one sequencing note in the spec that the naming disposition's durable record lands with bin-land cycle 3.

O3, O4 — no action.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-2.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-2.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 2 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
