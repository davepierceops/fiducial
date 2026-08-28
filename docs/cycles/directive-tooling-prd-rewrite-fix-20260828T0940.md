You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Carry out cycle 22: apply the triaged cycle-21 Spec Reviewer findings to specs/directive-tooling.md on branch directive-tooling-prd-rewrite.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-prd-rewrite-fix-20260828T0940.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: cycle-22 fixes for directive-tooling PRD rewrite", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-prd-fix", created by: git worktree add "$TMPDIR/fiducial-dt-prd-fix" directive-tooling-prd-rewrite
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-prd-rewrite, stop and report. Do not touch the main tree.

BASE VERIFICATION before any edit: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Both origin/directive-tooling-prd-rewrite and local directive-tooling-prd-rewrite must be at 80e5337582b4a4581f38bc97f87a06a00a29b746. If either has moved, stop and report.

READ before editing, whole, from the worktree: reviews/directive-tooling-cycle-21.md and specs/directive-tooling.md. The review artifact's per-finding Fix fields are the edit instructions; this directive carries dispositions, not restated wording.

DISPOSITIONS — one entry per finding:
- B1 accept: apply Fix as stated (restore four "Not accepted" members to §7 with the write bound as AC-DT-12 states it, remote-write clause kept beside it).
- B2 accept: apply Fix as stated (restore residual shape (a) with its G6 ground, accepted items (b)(c)(d), and the closing Escalation statement).
- B3 accept: apply Fix as stated (restore the no-retrofit disposition in one sentence at §4; §5's third outcome points at it).
- B4 accept: apply Fix as stated (restore the M8 fixture set to eight, compact form; keep the absolute-path addition; include the no-slug-character-boundary clause).
- N1 accept: apply Fix as stated (one clause: own wrongly-fenced statement is a badly formatted statement, not a mention; false positive follows from the fence exclusion).
- N2 accept: apply Fix as stated (name the population: the 90 markdown files in docs/cycles/ the research document measured, not "the directive corpus").
- N3 accept: apply Fix as stated (one clause at M3's row or AC-DT-13: the fence exclusion is this document's own, no governed file states it, it narrows what the lint matches).
- N4 accept: apply Fix as stated (restore §6 preamble in two or three sentences: derived from §4; fixture-repository substrate, testable offline; AC-DT-15 and AC-DT-16 the two exceptions).
- N5 accept: apply Fix as stated (second outcome's baseline clause; third outcome's zero-by-construction bound sentence).
- O1 no edit: the finding's observation is confirmed correct — audience did narrow from [all-roles, human] to [human] — and Dave ruled the narrowing deliberate and kept, 2026-08-28 decision session. Frontmatter stays exactly: status: draft, last-reviewed: null, audience: [human].
- O2 accept: restore the precedent's address at G10: specs/bin-land.md §4 G6. Path and section only — no SHA.
- O3 accept in part: restore the one-clause resolution mechanism (a conflict is resolved by a dictated disposition stating which of the two moved and why). Do not restore the quote-AC-CO-criteria-whole obligation.
- O4 accept: one clause at Q9: the three gated criteria read on AC-DT-16's model until Q9 resolves. Touch neither criterion.

REGISTER CONSTRAINT binding every restoration: the four removal categories from the rewrite still bind — no provenance tags, no cycle-by-cycle changelog prose, no closed questions, no per-citation SHAs. Restore substance in the compact register of the 511-line rewrite; a restoration that reintroduces any of the four categories is a defect. Restate; do not paste prior text wholesale.

SCOPE: edit only specs/directive-tooling.md. The only other file this session creates is the directive file above. No other file, no ref creation or deletion, no merge.

AFTER EDITS: run bin/check-frontmatter --all from the worktree; it must exit 0. Commit the spec edits alone with message "directive-tooling PRD: cycle-22 fixes per reviews/directive-tooling-cycle-21.md". Push.

STOP CONDITIONS, pinned to reviewed ref 80e5337582b4a4581f38bc97f87a06a00a29b746: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; fix commit SHA; per-finding list of edits with section locations; check-frontmatter exit code; anything observed that this directive did not anticipate. Label every claim observed, inferred, told, or unknown.
