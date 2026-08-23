Write this directive verbatim to docs/cycles/directive-tooling-spec-9-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. This cycle revises specs/directive-tooling.md on branch directive-tooling-spec, per reviews/directive-tooling-cycle-8.md @ e8bf561c52c5bf4dbf213af11242734903d33edd — the independent gate. Stop conditions pin to e8bf561c52c5bf4dbf213af11242734903d33edd. Fetch origin as your first git act. Do not rebase or merge main into the spec branch.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling-c9" origin/directive-tooling-spec — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec-c9 (local working branch). Push via git push origin HEAD:directive-tooling-spec, without -u.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before revising: reviews/directive-tooling-cycle-8.md (the governing findings) and reviews/directive-tooling-cycle-7.md; specs/directive-tooling.md at branch head; docs/packages/package-a-spec.md §3.6 and §8.2 at its current last-touching commit; docs/research/gh-write-friction-20260823T184149Z.md §3.2; skills/directive-authoring.md at origin/main; bin/cycle-open.

TASK 1 — revise specs/directive-tooling.md per these dispositions of the cycle-8 findings. This directive is the origin of the dictated dispositions; the spec cites it by path and SHA.

B1 — accept. Re-anchor the preserved-contract citation: AC-CO-1 through AC-CO-11 at §3.6 and AC-CO-12 at §8.2, each cited at a SHA where the cited text exists — read package-a-spec.md's history and pin the correct commit(s); never carry the stale 434e5921 anchor forward for text it does not contain. State that §8.2 amends none of AC-CO-1..11, with the cycle-8 verification as provenance.

B2 — accept, disposition: licenses, read through the destination clause. "What the contract can emit" means what AC-CO-1 licenses, and AC-CO-1's own statement that output lands at docs/cycles/<name>-directive.md is the boundary: pattern 3 matches a single-component basename, no path separators, because a separator-bearing name produces a path outside the destination the contract states. The boundary derives from cited governed text, not an invented class — cite AC-CO-1's destination clause and G6 together as the ground. Both cycle-8 probe cases (sub/nested, ../escaped) are stated as outside the licensed set and appear as failing fixtures in AC-DT-06. State explicitly that implementation behavior beyond the licensed set is not pattern 3's referent.

B3 — accept. §5's third outcome re-baselines on the instance unit: the source's figure is one contradiction (the eight-versus-one), cited to the research §3.2; the signal becomes zero new contradiction instances in post-adoption directives, with the first recount expected to read 0-against-0 and stated as meaningful only over time. Remove the nine-file baseline.

N1 — accept. AC-DT-02 gains the threshold that makes it decidable: the reproduced line must be a non-blank line of invariant text, and the criterion states the match is exact after whitespace normalization. State it as the criterion's own contract.

N2 — accept. Correct §1 to the source's figure (91 markdown files, 90 excluding that cycle's own) and reconcile with §4's recount (99 files, 3 non-directives) by stating each count's scope where it appears; no figure appears without its scope.

O5 — accept. G2 and G5 each gain at least one acceptance criterion, derived from the goal text as stated; if either goal is not testable at PRD level, narrow the goal or state the criterion at the level the PRD carries and mark the remainder for the TRD stage.

O1–O4 — no action; O2's stale pointer remains tracked by the decision session.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, re-gate the revised spec, producing reviews/directive-tooling-cycle-9.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the revision. An independent gate follows this cycle; your artifact is its input, not its substitute.

LANDING. Create exactly two files — this directive file and reviews/directive-tooling-cycle-9.md — and modify exactly one: specs/directive-tooling.md. Nothing else. Directive file first, spec and review artifact after the re-gate. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Any disposition you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree.

REPORT, triageable by the decision session: head SHA of directive-tooling-spec read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the cycle 9 verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
