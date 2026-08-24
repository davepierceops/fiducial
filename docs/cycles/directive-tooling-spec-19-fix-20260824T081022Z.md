Write this directive verbatim to docs/cycles/directive-tooling-spec-19-fix-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act, and report the SHA read back from git via ls-remote.

ROLES. This session fills one role: spec author. No re-gate runs in this session; a confirmation-scoped independent gate follows and pins the commit this session lands.

REVIEWED REF. This session revises specs/directive-tooling.md on branch directive-tooling-spec, executing two dispositions Dave ruled against reviews/directive-tooling-cycle-19.md @ 616e382b8ab2fd8c4d23ee0b8821e6a419a63c81 (branch head at dispatch; reviewed spec commit a304212c, blob dc9a55d3). Stop conditions pin to 616e382b. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c19f" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c19f (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-19.md @ 616e382b (findings N1 and N2, whose dispositions follow); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (last-reviewed reviews/expedited-log.md @ 7853525aedf831bcc07da3264c3af7a91825b048).

TASK — as spec author, execute two dispositions. This directive is the origin of both dictated dispositions; the spec cites it by path and SHA.

Cycle-19 N2 — disposition (b), Dave's ruling: the reading scopes to carried wording. A fenced copy of another directive's statement is a mention; an author's own fenced statement is a statement they formatted badly. State that scoping where the reading is stated in §4. Consequence, followed through: the fenced-only shape returns to §7's residual set as an accepted false positive; revise §7's cycle-19 paragraph and §4's "One consequence of the reading reaches §7" accordingly. AC-DT-06 fixture (vii) is untouched — its verdict is non-zero under both scopings, per the cycle-19 artifact. The N1-closure of cycle 18 is unaffected: the duplicate shape is carriage under either scoping, per the cycle-19 artifact.

Cycle-19 N1 — fix (a), Dave's ruling: extend M3's Derived-from quotation to the end of the governed bullet, restoring its fourth sentence, matched against skills/directive-authoring.md at origin/main by running — never from memory. "Quoted whole at its current form" then stands true as written; change no other cell of the row.

Consistency: run the corpus recount and Core rule 13 sweep as the document's own rules require, labelling consequential updates at their sites; this directive file raises the corpus count by one.

LANDING. Create exactly one file — this directive file — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. A disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the sites each disposition reached; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
