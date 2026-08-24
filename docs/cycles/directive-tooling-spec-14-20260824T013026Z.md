Write this directive verbatim to docs/cycles/directive-tooling-spec-14-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

ROLES. This session fills two roles in sequence: spec author for Task 1 (drafting-agent work over a spec document, per the operating model's authorship rules), then Spec Reviewer per roles/spec-reviewer-agent.md for Task 2. State the active role in your report where each task's output is described. No other role is in scope.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-13.md @ cbf012dd31922761a8a89098b7c8d469feee95f8 — the second independent gate. Stop conditions pin to cbf012dd31922761a8a89098b7c8d469feee95f8. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c14" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c14 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-13.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main; docs/packages/package-a-spec.md §8.2 (AC-CO-12, for N3's defect class).

TASK 1 — as spec author, revise specs/directive-tooling.md per these dispositions of the cycle-13 findings. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: single predicate, locatability. M3's search extent keys on exactly one test: a conforming G11 manifest locates the disposition author region → M3 searches that region; in every other case — manifest absent, malformed, or conforming but not locating that region — M3 searches the whole file. State the predicate once, in M3's own text, and make every other site (the §4 block at :676 and :725, :747, J3, G3, AC-DT-03, AC-DT-06, AC-DT-10's coverage statement, the Reliability NFR) speak from it: M3 is total by construction, so AC-DT-10's non-reach to M3 is a derived consequence stated as such, not a declaration, and the Reliability NFR conflict dissolves. The degraded-or-non-locating-manifest whole-file case may false-positive on generator-sourced text; state that this is the §7 paste residual already accepted, not a new one. Replace the fallback ground the cycle-13 gate showed falsified (:729) with the ground above.

N1 — accept, disposition: one definition. AC-DT-02's structural exclusion is exactly the enumerated rule: a line is excluded when it consists solely of whitespace and characters from the set - = ~ ` # * _ | > +. Delete the second definition and the equivalence claim; re-derive the criterion's prose examples (including the table-rule line) from the single rule and correct any that fail it.

N2 — accept. State the lint's manifest contract as the input-contract clause of M3's predicate: the lint attempts to locate the disposition author region via conforming G11 markers; any input where that attempt fails is the whole-file case. Marker syntax remains deferred to the TRD; state that the contract is syntax-independent — it consumes whatever conforming form the TRD fixes.

N3 — accept. State how the lint resolves its path argument: the argument is resolved to a repository-relative path from the repository root before M8's patterns apply, and an argument outside the repository is a refused invocation with a stated non-zero exit; cite AC-CO-12's shipped-bug record as the motivating precedent. Add the corresponding fixture to AC-DT-06.

O1–O5 — no action; O5's record stands.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-14.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. A third independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-14.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 14 verdict line; findings by severity; anything stopped or surfaced; the active role stated per task. Label every claim observed / inferred / told / unknown.
