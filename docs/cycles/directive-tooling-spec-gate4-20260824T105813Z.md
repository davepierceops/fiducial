Write this directive verbatim to docs/cycles/directive-tooling-spec-gate4-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act, and report the SHA read back from git via ls-remote.

ROLES. This session fills one role: Spec Reviewer per roles/spec-reviewer-agent.md, independent — this session authored nothing under review. Review only: no edits to specs/directive-tooling.md or any governed file. This session creates exactly two files — this directive file and the review artifact — and modifies nothing.

REVIEWED REF. specs/directive-tooling.md @ 255eb65b95705551b1463ddf6a05be275c4323f8 (blob 62a9d3b1) on branch directive-tooling-spec. Stop conditions pin to 255eb65, not the branch head after this directive's own commit lands. Fetch origin as your first git act. Do not rebase or merge anything.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-gate4" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-gate4 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before reviewing: reviews/directive-tooling-cycle-18.md @ c5090995; reviews/directive-tooling-cycle-19.md @ 616e382b; docs/cycles/directive-tooling-spec-19-20260824T061718Z.md @ c05efadd; docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md @ 5ea201e6 (the origin of the N2-scoping and N1-fix dispositions Dave ruled); skills/directive-authoring.md at origin/main (last-reviewed reviews/expedited-log.md @ 7853525aedf831bcc07da3264c3af7a91825b048).

TASK — confirmation-scoped independent gate. This is NOT a fresh full-depth read; eighteen authoring cycles and three independent gates precede it, and Dave has bound the scope. Confirm exactly three things, each by running where the artifacts permit:

1. Cycle-18 B1 is resolved as ruled: the cycle mode emits the labelled disposition statement as an extension of the emitted structure, AC-CO-1 through AC-CO-12 untouched, G3's invariant uniform in both modes, the ruling recorded with its ground.
2. The cycle-19 findings are resolved as ruled: N1 — M3's Derived-from quotation runs to the end of the governed bullet, matched against skills/directive-authoring.md at origin/main by running, and "quoted whole" is true as written; N2 — the reading is scoped to carried wording, the fenced-only shape restored to §7's residual set as an accepted false positive, and the two consequential-update sites the fix session disclosed (M3's contract and qualification cells; AC-DT-13's cycle-19 sentence) are consistent with that scoping — Dave has endorsed those edits.
3. No new contradiction between the document and the governed text it cites, over the text the cycle-19 and cycle-19-fix revisions touched. Re-run the citation sweep over quotations those revisions introduced or changed, by running against the cited sources. Do not re-derive findings the prior gates already dispositioned; do not re-open dispositioned conflicts.

Residual non-blocking findings from prior cycles ride to the TRD stage by Dave's standing ruling and are not re-litigated here. A finding outside the three confirmations above is out of scope unless it is a new blocking contradiction, in which case file it.

ARTIFACT. Produce reviews/directive-tooling-cycle-20.md per skills/review-artifact.md, verdict first. State the confirmation scope in the Scope line and state independence in the Reviewer line. Expected verdicts: ready or ready-with-findings if the three confirmations hold; changes-required only on a failed confirmation or a new blocking contradiction.

LANDING. Directive file first, review artifact after the review. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. A confirmation you cannot run as written → stop and surface. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree. Do not edit specs/directive-tooling.md under any circumstance.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the verdict line; each of the three confirmations stated pass/fail with its evidence class; findings by severity if any; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
