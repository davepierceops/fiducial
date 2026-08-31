You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Amend the consolidation branch (rev d) with the two accepted findings of the confirmation gate: reviews/directive-authoring-cycle-5.md F-1 and reviews/directive-invariants-cycle-6.md F-1, each fix carrying the reviewer's wording. You do not flip status, do not run bin/flip-agreed, do not edit any review artifact, and do not edit bin/, specs/, docs/global-context/, policies/, or roles/. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-d-20260831T190000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation amendment d (confirmation-gate findings)", push with git push origin directive-authoring-consolidation (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-consol-d", created on the existing branch by: git worktree add "$TMPDIR/fiducial-da-consol-d" directive-authoring-consolidation
This reuses the existing local branch: no -b and no --no-track. Before creating it, run git fetch origin directive-authoring-consolidation, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation, or if "$TMPDIR/fiducial-da-consol-d" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin directive-authoring-consolidation. Judge every remote operation — fetch, push, ls-remote — by the refs it reports and its exit status, not by credential-helper noise on stderr; an operation that exits 0 and reports no refs is not a failure. The local branch directive-authoring-consolidation and origin/directive-authoring-consolidation must both be exactly efaad5f6a4db5c6005b81f2af9f1bd53a1063872; if either is anything else, stop and report. In the worktree, git rev-parse HEAD:skills/directive-authoring.md must be ceb6a0dc5c34efa682d35f732169f5d5e119d5dc and HEAD:skills/directive-invariants.md must be bb54dcb55d3db29c4d4629698218be0810101f5a; if either differs, stop and report.

COMPANIONS, read whole from the worktree before writing: docs/cycles/directive-authoring-consolidation-c-20260831T181500Z.md @ 68af089d66fcbadb43aa59d6c18292464149a948 — its editing constraints bind this directive unchanged except where an edit below names the passage it changes; reviews/directive-authoring-cycle-5.md and reviews/directive-invariants-cycle-6.md, both at 7e055d7393d96deabd5c50c6ca01e52047e306e4 via git show, for the findings these edits resolve. Also read both documents under edit, whole.

EDITS. Anchors are sentences in the file at efaad5f, the files wrap prose at 79 characters, so match every anchor as a sentence across line breaks, never as one line. If an anchor is not found exactly once, stop and report.

E1 (cycle-5 F-1), in skills/directive-authoring.md, second bullet: replace the whole bullet "**The disposition label leads the disposition statement and no other eligible line.**" with: **The disposition label leads the disposition statement and no other eligible line, eligibility as the Directive Invariants document defines it.**
Reflow at 79 characters. The first bullet is untouched; the fence in the other document is untouched — this bullet is not the one the fence quotes.

E2 (cycle-6 F-1), in skills/directive-invariants.md, the section headed "## Stop conditions": replace the sentence "A remote operation whose refs report success is not a failed command." with: A remote operation that exits successfully is not a failed command, whatever a credential helper writes to stderr.
Reflow the paragraph at 79 characters; the marker line STOP CONDITIONS and the {{reviewed_ref}} placeholder are unchanged. The Base verification region is untouched.

EDITING CONSTRAINTS: no ## section is added, removed, renamed, or reordered in either file; no region section's first body line changes; no fenced block is added, removed, or reordered; no other passage changes. After the edits the shipped unfenced_labelled_statements check (in bin/tests/test_directive.py) returns no hit over either file, and the bare label token does not appear in skills/directive-authoring.md. The disposition-prompt fence and the skill's first bullet remain byte-equal after flowing, at 669 bytes each — neither edit touches either copy; verify, do not re-derive. Frontmatter untouched: both files stay in-review, last-reviewed null.

SCOPE, one commit after the directive-file commit: skills/directive-authoring.md and skills/directive-invariants.md only. Commit message: "directive-authoring + directive-invariants: consolidation amendment d — confirmation-gate findings (cycle-5 F-1, cycle-6 F-1)". Push with git push origin directive-authoring-consolidation.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-consol-d-run.log": bin/tests/run for the whole suite; per-file runs with python3 -m unittest discover -s bin/tests -t bin -p <file> for test_directive.py, test_directive_trd.py, and test_check_directive.py; bin/check-frontmatter --all (state exit code and count); the shipped unfenced_labelled_statements check over both files (expected: no hits); the fence-bullet flow comparison (expected: 669 and 669, equal); git diff --stat of the content commit (expected: exactly two files).
Expected state, and a stop if it differs: whole suite OK with zero failures and zero errors, 7 skipped; test_directive.py 43/43; test_directive_trd.py 16 passed + 6 skipped; test_check_directive.py 84/84; check-frontmatter exit 0, 61 files / 14 globs. Any red is a stop: report it with the assertion text; do not adjust a test and do not adjust either document to satisfy it.

GH: never invoke gh. Push the branch; pull requests are the decision session's concern.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-consol-d" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref efaad5f6a4db5c6005b81f2af9f1bd53a1063872. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any anchor not found exactly once, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the content commit SHA, and the branch it is on
- the run-log path
- per edit E1 and E2, the changed passage verbatim as landed with its line numbers
- suite counts, whole and per the three files, each with the tree it was observed in; a sandboxed run says so
- check-frontmatter exit code and count
- the unfenced-label results, the flow result, and anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
