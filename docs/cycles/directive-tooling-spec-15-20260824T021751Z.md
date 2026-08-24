Write this directive verbatim to docs/cycles/directive-tooling-spec-15-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

ROLES. This session fills two roles in sequence: spec author for Task 1, then Spec Reviewer per roles/spec-reviewer-agent.md for Task 2. State the active role in your report where each task's output is described. No other role is in scope.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-14.md @ 23f91c8efadfb3a8b9d68abe04907e44cd35d32c. Stop conditions pin to 23f91c8efadfb3a8b9d68abe04907e44cd35d32c. Fetch origin as your first git act. origin/main has moved (merge commit 7bbb3a71ee7d5ebc542fbade75829a531685d296 landed the fourth skills/directive-authoring.md amendment); do not rebase or merge main into the spec branch — read the amended skill at origin/main, work on the spec branch as it stands.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c15" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c15 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-14.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (agreed, last-reviewed reviews/expedited-log.md @ b4a0fa581ba5c64ac5a0e5374b5604e979a73653 — the disposition is now its own labelled statement, mechanically distinguishable, label form a tooling concern).

TASK 1 — as spec author, revise specs/directive-tooling.md per these dispositions of the cycle-14 findings. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept, disposition: anchor on the labelled statement. The governed rule now states the disposition is its own labelled statement, mechanically distinguishable from incidental mention (cite the skill at content commit b4a0fa581ba5c64ac5a0e5374b5604e979a73653). M3's check becomes: exactly one labelled disposition statement is present, carrying one of the two admitted forms; zero labelled statements fails — including the prohibition-only hand-written case, the motivating incident, which now fails mechanically whatever else the file mentions; incidental text instantiating a form without the label is outside M3's match by the governed rule itself. The label's fixed lexical form is stated as a TRD decision, with M3's PRD-level contract being label-presence and form-membership. Consequence, executed in full: the locatability predicate, the region scoping, and the whole-file fallback for M3 are retired — remove that apparatus from M3's row, the §4 block, J3, G3, AC-DT-03, AC-DT-06, AC-DT-10's coverage statement, and the Reliability NFR site, restating each from the labelled-statement check; the cycle-14 N3 vacuity question is recorded as dissolved with the predicate it questioned. AC-DT-06's M3 fixtures are restated over the labelled statement: labelled-and-well-formed passes; unlabelled prohibition-only fails; labelled statement plus incidental worktree mention elsewhere passes. G11's manifest remains for the measurement apparatus (§5, AC-DT-05) only; state that M3 no longer consumes it.

N1 — accept, resolved within B1: the predicate N1 wanted referenced once is retired; verify no site restates a retired test and that every M3 site references the labelled-statement check rather than restating it in full.

N2 — accept. Restate §7's characterization honestly: the accepted-residual enumeration changed in extension across cycles 12–14 and changes again under B1 — state the current residual set plainly (what M3 still cannot catch, if anything: a labelled statement whose content is false, e.g. naming a tree the session does not use, remains uncheckable and is the accepted residual), without the "restated, not widened" framing.

N3 — accept, resolved within B1: the third enumerated shape is retired with the predicate; record the dissolution where the question was raised.

O1–O4 — no action.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-15.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. A third independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-15.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 15 verdict line; findings by severity; anything stopped or surfaced; the active role stated per task. Label every claim observed / inferred / told / unknown.
