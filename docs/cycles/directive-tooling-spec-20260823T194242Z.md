Write this directive verbatim to docs/cycles/directive-tooling-spec-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

REVIEWED REF. All stop conditions pin to origin/main @ 38b2c61f0f57ebdf4fedfd66c9f276b533294e57. Fetch origin as your first git act; read every companion document at that ref.

WORKING TREE — exclusive assignment, as executed. Two other sessions hold the main clone and ../fiducial-pass2. From the clone root: git worktree add "$TMPDIR/fiducial-directive-tooling" origin/main — then do all work in that directory and nowhere else. In it: git checkout -b directive-tooling-spec. All three files this directive creates land on that branch.

The assignment as first issued named the sibling path ../fiducial-directive-tooling. That path could not be created, so Dave reassigned the tree to $TMPDIR in the decision session; everything else in this directive is unchanged. The reason, with this session's probes as provenance (all observed): git worktree add ../fiducial-directive-tooling origin/main returned "fatal: could not create leading directories of '../fiducial-directive-tooling/.git': Operation not permitted", exit 128; a bare mkdir of the same sibling path returned "Operation not permitted" while /Users/dave/code is drwxr-xr-x dave:staff, so the denial is the sandbox's write allowlist and not a filesystem permission; mkdir probes under $TMPDIR and inside the clone root both succeeded, and both probes were removed. The failed worktree add left no entry in .git/worktrees and the main clone stayed clean on bin-land-spec-2.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ 9f5f4c9d8ce06d1c5489bf3b5a3248b5386fe650:
- Branch via git checkout origin/main then git checkout -b <branch> (the worktree add above already detaches at origin/main; the -b step follows it).
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

COMPANIONS — read all before authoring, at the reviewed ref: docs/global-context/core.md, LEXICON.md, skills/directive-authoring.md, policies/document-metadata-policy.md, specs/prd-template.md, roles/spec-reviewer-agent.md, skills/review-artifact.md, specs/bin-land.md, reviews/bin-land-cycle-1.md, docs/research/gh-write-friction-20260823T184149Z.md. The last three are the precedent: this session repeats the bin-land cycle 1 shape.

TASK 1 — author specs/directive-tooling.md, a PRD per specs/prd-template.md. Frontmatter: status: draft, last-reviewed: null, audience: [all-roles, human]. Label every assertion observed / inferred / told / unknown. This directive is the origin of the dictated content below; the spec cites this file by path and SHA and does not restate the content as if derived elsewhere.

Dictated problem statement: directives are the only ungated load-bearing artifact class in this methodology — specs get the Spec Reviewer, governed documents get the Context Quality Reviewer, code gets the red-gate; directives ship freehand from a decision session to an executor. Freehand composition has an irreducible error rate that worsens with accumulated context; a decision session late in a long conversation is a degraded author. The countermeasure is structural, not exhortative: shrink the freehand surface, gate the remainder.

Dictated motivating incident, which the spec must state and must prevent recurring: a parallel directive stated a working-tree prohibition instead of an assignment; skills/directive-authoring.md requires an assignment — a named directory plus the command creating it (e.g. git worktree add ../fiducial-pass2 origin/main). The executor stopped correctly; the omission class is the target.

Dictated tool 1 — bin/directive: emits a directive skeleton whose invariant text — sandbox constraints, stop conditions, a working-tree assignment slot, verification steps, report format, claim labels — is read from committed repo text at generation time, never hardcoded in the tool; the decision session authors only the task-specific middle.

Dictated tool 2 — bin/check-directive: a lint the executor runs as part of its existing first act (write directive file, commit, push); a directive missing required elements produces a nonzero exit, and the executor stops and surfaces before any work.

Dictated naming disposition (Dave, this session; this directive is the committed origin until the bin-land cycle 3 directive lands the durable record): binary names are not methodology vocabulary; no LEXICON entry is created for a binary name.

Dictated requirement: the lint's required-element set is derived from committed governed text — docs/global-context/core.md's Vocabulary, docs/global-context/decision-layer.md rule 14, skills/directive-authoring.md — never invented in the tool. The spec must distinguish mechanically checkable elements from judgment-only rules and keep the latter out of the lint's claims.

Open questions the spec must carry as open, resolved-by named per question: (a) where the invariant text lives and how the generator resolves it; (b) lint sequencing relative to commit and push — whether a failing directive still lands for the audit trail; (c) how the lint distinguishes a parallel directive (worktree assignment required) from a sole-tree one; (d) whether these tools change the text of skills/directive-authoring.md or sit beneath it.

TASK 2 — same session, switch roles: as Spec Reviewer per roles/spec-reviewer-agent.md, run the gate review of the spec you authored, producing reviews/directive-tooling-cycle-1.md per skills/review-artifact.md, verdict first. Do not soften findings because you authored the document; the bin-land precedent shows the shape.

LANDING. Create exactly three files — the directive file, specs/directive-tooling.md, reviews/directive-tooling-cycle-1.md — and modify nothing else. Commit and push the directive file first, the spec and review artifact after the review completes. Run bin/check-frontmatter --all and bin/tests/run before the final push and report their exit statuses.

STOP CONDITIONS. Any dictated content you cannot execute as written → stop and surface; no reinterpretation, no silent partial execution. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Do not touch the bin-land-spec-2 branch or ../fiducial-pass2.

REPORT, triageable by the decision session: branch; head SHA read back via ls-remote; the three files with per-file landed confirmation; frontmatter and test exit statuses; the review verdict line; findings by severity; anything stopped or surfaced. Label every claim observed / inferred / told / unknown.
