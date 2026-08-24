Write this directive verbatim to docs/cycles/directive-authoring-exactly-one-<timestamp>.md — generate the timestamp yourself, ISO 8601 basic format, UTC — then commit and push it as your first act per the landing sequence below, and report the SHA read back from git.

ROLES. This session fills one role: executor of an expedited-path document revision. No authoring judgment is in scope; the wording is dictated.

REVIEWED REF. Stop conditions pin to origin/main HEAD as of your first fetch; report that SHA. Fetch origin as your first git act.

WORKING TREE — exclusive assignment. Other sessions hold the main clone and several worktrees. From the clone root: git worktree add "$TMPDIR/fiducial-da-exactly-one" origin/main — then do all work in that directory and nowhere else. In it: git checkout -b directive-authoring-exactly-one. Push without -u; upstream tracking cannot be set from a $TMPDIR worktree.

SANDBOX CONSTRAINTS — carry as told; provenance docs/cycles/pass2-held-fix-20260823T180753Z.md @ commit b9444973:
- Worktrees go under $TMPDIR; sibling paths of the clone are sandbox-denied.
- Never invoke gh, for anything. Its errors are not evidence about credentials; reason from first principles.
- "fatal: failed to store: 100001" on stderr is keychain noise; git's exit status is correct; verify pushes by git ls-remote, never by absence of errors.
- Sequential standalone git invocations, never a shell loop.
- Never merge. Merges happen from the decision session over its repository connector.

TASK — an expedited-path revision of skills/directive-authoring.md per policies/document-metadata-policy.md. Read both at origin/main before editing. This directive is the origin of the dictated wording below.

Content commit — exactly one commit touching exactly one tracked path, skills/directive-authoring.md. In the working-tree disposition bullet, replace the phrase "The disposition is stated as its own labelled statement, mechanically distinguishable" with, verbatim:

The disposition is stated as its own labelled statement, exactly one per
directive, mechanically distinguishable

The rest of the sentence and every other line stays untouched; re-wrap only the affected bullet to the file's existing column convention, preserving the word sequence exactly. The same commit flips frontmatter to status: in-review and last-reviewed: null, per the policy's revision-lifecycle rule. The body diff must stay at or under ten changed lines; if the replacement as dictated exceeds that, stop and surface — do not compress beyond what the substitution itself requires. Push, verify by ls-remote, report the commit SHA and the full diff.

HOLD. Stop after reporting. Dave reads the diff. Proceed only on a message stating he agrees the diff as-is — relayed or direct. Any finding instead → stop; the expedited path has escalated to a full cycle and this directive ends.

ON AGREEMENT — two further commits, in order, per the policy's expedited sequence:
1. Append one line to reviews/expedited-log.md naming skills/directive-authoring.md, the content-commit SHA, the local date, and what changed (exactly one labelled disposition statement per directive). Its own commit.
2. A frontmatter-only status-transition commit on skills/directive-authoring.md: status: agreed, last-reviewed: reviews/expedited-log.md @ <content-commit SHA> — the same SHA the log entry names, character-for-character. Nothing but the frontmatter transition in this commit.
Push, verify by ls-remote, report both SHAs.

STOP CONDITIONS. Anything you cannot execute as written → stop and surface; no reinterpretation. Concurrent tree mutation in your worktree → stop and surface. A push you cannot verify by ls-remote → stop and surface; never retry a write. Run bin/check-frontmatter --all after the flip commit and report its exit status. Do not touch any other file, branch, or worktree; do not merge.

REPORT at each stage, triageable by the decision session: branch head via ls-remote; commit SHAs; the content diff in full at the hold; frontmatter check exit status after the flip. Label every claim observed / inferred / told / unknown.
