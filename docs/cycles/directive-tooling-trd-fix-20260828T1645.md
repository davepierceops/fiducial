You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Carry out cycle 2: apply the triaged cycle-1 Spec Reviewer findings to specs/directive-tooling-trd.md on branch directive-tooling-trd.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-trd-fix-20260828T1645.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: cycle-2 fixes for directive-tooling TRD", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-trd-fix", created by: git worktree add "$TMPDIR/fiducial-dt-trd-fix" directive-tooling-trd
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-trd, stop and report. Do not touch the main tree.

BASE VERIFICATION before any edit: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Both origin/directive-tooling-trd and local directive-tooling-trd must be at fcd7377aeb9f201dcec3fe9e03eeae60b2e00d4a. If either has moved, stop and report.

READ before editing, whole, from the worktree: reviews/directive-tooling-trd-cycle-1.md and specs/directive-tooling-trd.md, plus specs/directive-tooling.md where a finding cites it. The review artifact's per-finding Fix fields are the edit instructions.

DISPOSITIONS — one entry per finding:
- F-1 accept: apply Fix as stated (correct M2's mechanism to one that decides "this commit touches this path" — verify the corrected invocation by running it in the worktree against a known touching and a known non-touching case before writing it into the document).
- F-2 accept: apply Fix as stated (resolve the invariants document's committed content against the repository that holds it; state the home-vs-root relationship the resolution assumes and what the test fixture must therefore provide).
- F-3 accept: apply Fix as stated (the disposition prompt region enters the emission tables; region counts and the §3.3 closure sentence updated to match).
- F-4 accept: apply Fix as stated (give M1, M4, M5, M6, M7 each a match rule that does not require wording only the invariants document states, or where a delegation is genuinely needed, disclose it per-element as G6 licenses for M3's label — not as a blanket extension).
- F-5 accept: apply Fix as stated (one destination for the general-mode skeleton, chosen so PRD §7's correct-by-construction mitigation for M8 holds).
- F-6 accept: apply Fix as stated (cycle-mode region table enumerates its regions one-to-one so AC-DT-05 and AC-DT-18 are decidable over it).
- F-7 accept, direction ruled by Dave 2026-08-28: keep the narrow match, disclose it. Add the disclosure in the M3/exclusive-assignment section on the fence-exclusion pattern: the match rule (git worktree add plus a quoted or backticked path token) is this document's own narrowing of the governed "a named directory plus the command creating it"; it narrows what the lint matches rather than adding an enforced requirement; a well-formed disposition phrased outside it is a false stop, accepted per PRD §7's cheap direction. Cross-reference the PRD §7 accepted-risk item it instantiates.
- F-8 accept: apply Fix as stated (AC-DT-02's scan scoped to the generator's source, per the agreed criterion and §8's own restatement).
- F-9 accept: apply Fix as stated (reconcile --date's YYYY-MM-DD grain with the hhmmss claim — state what actually determines the time component, or drop the determinism claim to what --date can carry).
- The five non-blocking observations: no edits this cycle; they ride to convergence per the ruled process. Do not touch them even where a blocking fix passes nearby, except where a blocking fix's edit makes one of them true or false — in that case update the affected line and say so in the report.

Frontmatter stays exactly: status: draft, last-reviewed: null, audience: [human]. The four removal categories still bind: no provenance tags, no changelog prose, no closed questions, no per-citation SHAs.

SCOPE: edit only specs/directive-tooling-trd.md. The only other file this session creates is the directive file above. No other file, no ref creation or deletion, no merge, no PR.

AFTER EDITS: run bin/check-frontmatter --all from the worktree; it must exit 0. Commit the TRD edits alone with message "directive-tooling TRD: cycle-2 fixes per reviews/directive-tooling-trd-cycle-1.md". Push.

CLEANUP — after the report is composed and both pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-trd-fix" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref fcd7377aeb9f201dcec3fe9e03eeae60b2e00d4a: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; fix commit SHA; per-finding list of edits with section locations, including the F-1 verification-by-running result; any observation line a blocking fix changed; check-frontmatter exit code; anything observed that this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
