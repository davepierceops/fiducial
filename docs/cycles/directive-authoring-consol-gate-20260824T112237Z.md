Write this directive verbatim to docs/cycles/directive-authoring-consol-gate-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act, and report the SHA read back from git via ls-remote.

ROLES. This session fills one role: Spec Reviewer per roles/spec-reviewer-agent.md, independent — this session authored nothing under review. Review only: no edits to skills/directive-authoring.md or any governed file. This session creates exactly two files — this directive file and the review artifact — and modifies nothing.

REVIEWED REF. skills/directive-authoring.md at origin/main, head 06e5d110cd71711231ce8257db0a31f6a1d12ed4 at dispatch — read the file at the main head you fetch and report both that head and the last commit touching the path. The document is status: agreed, last-reviewed reviews/expedited-log.md @ 7853525aedf831bcc07da3264c3af7a91825b048, reached through five same-day expedited amendments on 2026-08-23/24. This gate is the consolidation review those amendments accumulated toward. Stop conditions pin to 06e5d110. Fetch origin as your first git act.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and other worktrees, and at least one executor is running concurrently. From the clone root: git worktree add "$TMPDIR/fiducial-da-consol-gate" origin/main — then do all work in that directory and nowhere else. In it: git checkout -b directive-authoring-consolidation (local working branch). Push via git push origin HEAD:directive-authoring-consolidation, without -u; the first push creates the remote branch.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read before reviewing: skills/directive-authoring.md at origin/main (the document under review); reviews/expedited-log.md at origin/main (the five amendment entries and their SHAs — reconstruct each amendment by diffing its content commit against its parent); skills/spec-review-cycle.md; skills/command-blocks.md; skills/directive-dispatch.md; LEXICON.md; docs/global-context/core.md; docs/global-context/decision-layer.md; policies/document-metadata-policy.md; specs/directive-tooling.md at origin/main (a DOWNSTREAM CITER — now agreed, it quotes this document's first bullet whole in M3's Derived-from cell, anchors its count on the fifth amendment's sentence, and cites content commit 7853525a; reviews/directive-tooling-cycle-20.md verified those quotations by running).

TASK — wholesale consolidation review. Five expedited amendments landed same-day, each individually under the ten-line cap, none seen together by any reviewer. Review the document as one whole:

1. Coherence of the accumulated text: do the five amendments read as one rule set, or do they carry seams — redundancy, ordering that buries a requirement, a sentence whose referent moved when a later amendment landed.
2. Internal consistency: every requirement stated once, no self-contradiction, the naming section consistent with the body, Core rule 13 holding within the file.
3. Cross-document consistency: against every companion above — in particular whether directive-dispatch's "Writing the directive file" section and this document state the same requirements without drift, and whether anything here contradicts LEXICON, core, decision-layer, or spec-review-cycle.
4. Fitness as governing text: the document is read before every directive is authored; flag anything ambiguous enough that two careful authors would emit differently — the fix-cycle role-line omission class.
5. Downstream citation exposure: for every fix you propose, state whether it moves text specs/directive-tooling.md quotes or anchors on, and name the spec site that would go stale. A fix that moves quoted text is not thereby wrong — but its full cost must be on the record before Dave rules.

Do not review the expedited path's legitimacy — that is policy, dispositioned elsewhere. Do not propose restructuring for taste; findings require a stated consequence per skills/review-artifact.md.

ARTIFACT. Produce reviews/directive-authoring-cycle-3.md per skills/review-artifact.md, verdict first, independence stated in the Reviewer line, the five amendment SHAs listed in Scope. Findings one entry each, evidence verified by running wherever the repo permits.

LANDING. Directive file first, review artifact after the review. Run bin/check-frontmatter --all and bin/tests/run before the final push and report exit statuses; the AC-BN-10 pair failing in bin/tests/run is pre-existing and accepted.

STOP CONDITIONS. Anything you cannot review as directed → stop and surface. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the main clone's checked-out state, any other branch, or any other worktree. Do not edit skills/directive-authoring.md under any circumstance.

REPORT, triageable by the decision session: head SHA of directive-authoring-consolidation read back via ls-remote; per-file landed confirmation with blob match; gate exit statuses; the verdict line; findings by severity with one-line claims; the downstream-exposure statement for each proposed fix; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
