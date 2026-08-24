Write this directive verbatim to docs/cycles/directive-tooling-spec-5-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-4.md @ bf6b311bfeb7aa2b5f5a0927570643ad25e8250d. Stop conditions pin to bf6b311bfeb7aa2b5f5a0927570643ad25e8250d. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c5" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c5 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-4.md and the four prior directive files on this branch; specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main; docs/packages/package-a-spec.md §3.6 AC-CO-1; bin/cycle-open and bin/tests/test_cycle_open.py.

TASK 1 — revise specs/directive-tooling.md per these dispositions. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: license the slug form. M8 becomes a three-pattern check: <descriptor>-<timestamp>.md per skills/directive-authoring.md's Naming sentence, and cycle-<n>-directive.md and <slug>-directive.md per package-a-spec AC-CO-1, which is the "stated convention" that sentence defers to. The two cycle-mode patterns anchor on AC-CO-1 directly, cited by path and SHA. AC-DT-06's fixture set gains a passing <slug>-directive.md case and loses the failing one. State explicitly that any further filename branch discovered in the preserved contract is a defect to surface, not a pattern to absorb — see N3 below.

N1 — accept, disposition: a date-only YYYYMMDD is not an ISO 8601 basic timestamp for M8's purposes; the full <date>T<time> form is required. AC-DT-06 gains a failing fixture for the date-only case. The historical file metadata-scope-fix-20260823.md is not retrofitted (the lint governs directives written after adoption, as already stated); restate the historical count against the three-pattern check with this rule applied and record the provenance of the recount.

N2 — accept. Pin the M2 narrowing with a criterion in §6 so the section read alone cannot support the strict check; the criterion states what M2 enforces and the fixture the spec's own citations satisfy.

N3 — accept. Rewrite the mode-scoping precedence clause so a goal-vs-contract conflict is surfaced as a spec defect at review, never resolved silently in either direction; note that this cycle's B1 is the demonstrating instance.

O2 — the cycle-4 B2 extension (rewriting the contradicting Security-NFR sentence) is confirmed and absorbed; no further action.

O1, O3, O4 — no action.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-5.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-5.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 5 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
