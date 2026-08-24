Write this directive verbatim to docs/cycles/directive-tooling-spec-19-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

ROLES. This session fills two roles in sequence: spec author for Task 1, then Spec Reviewer per roles/spec-reviewer-agent.md for Task 2. State the active role in your report where each task's output is described. No other role is in scope.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-18.md @ its branch head commit (read it from origin/directive-tooling-spec at your first fetch and report it; the reviewed spec commit is de0cc683). Stop conditions pin to the branch head you report. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c19" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c19 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-18.md (the governing findings); specs/directive-tooling.md at branch head; skills/directive-authoring.md at origin/main (last-reviewed reviews/expedited-log.md @ 7853525aedf831bcc07da3264c3af7a91825b048); docs/packages/package-a-spec.md AC-CO-1 through AC-CO-12; bin/cycle-open.

TASK 1 — as spec author, revise specs/directive-tooling.md per these dispositions of the cycle-18 findings. This directive is the origin of the dictated dispositions, including a Core rule 9 resolution Dave has ruled; the spec cites it by path and SHA.

B1 — accept, disposition: the cycle mode emits the labelled statement too. Dave's ruling, resolving the surfaced contradiction between skills/directive-authoring.md (every directive states its disposition, exactly one labelled statement) and the preserved cycle-open skeleton (no disposition region): reviewer-gated cycle directives demonstrably use working trees, so the requirement reaches them, and the cycle-mode skeleton gains the labelled disposition statement over an empty content slot exactly as the general mode's does. G3's invariant holds uniformly in both modes. State this as an extension of the emitted structure, with the preserved AC-CO criteria untouched — they constrain what the skeleton must contain, not what may be added. Verify that reading against AC-CO-1 through AC-CO-12 before writing: if any criterion forbids additions to the skeleton, stop and surface rather than absorbing a second contradiction. Record the ruling and its ground where the conflict was filed.

N1 — accept, disposition: resolved by reading, no amendment. A fenced copy of a labelled statement is a mention, not a statement — the same statement/mention distinction the governed rule itself draws ("mechanically distinguishable from incidental mention") and the carry-as-pointer rule's framing of quoted wording. State the reading where M3's count is grounded: "exactly one per directive" and "M3 counts unfenced statements" agree because only an unfenced instance is a statement. Restore §7's residual-set claims to true as written under that reading.

N2 — accept, disposition: no action, recorded. The Q9-gated amber set is the descope's design, not a defect; record it as such where the finding was filed.

O1–O6 — no action.

Consistency: run the corpus recount and Core rule 13 sweep as the document's own rules require, labelling consequential updates at their sites.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-19.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. Gate against the descoped scope stated in §4: a mechanism routed to the TRD by a §8 question is not a PRD finding. A confirmation-scoped independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-19.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 19 verdict line; findings by severity; anything stopped or surfaced; the active role stated per task. Label every claim observed / inferred / told / unknown.
