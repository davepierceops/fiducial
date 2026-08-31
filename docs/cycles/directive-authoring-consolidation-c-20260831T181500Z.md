You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Amend the consolidation branch (rev c) with the four accepted findings of the consolidation gate: reviews/directive-authoring-cycle-4.md F-1 and F-2, and reviews/directive-invariants-cycle-5.md F-1 and F-2, each fix carrying the reviewer's wording. You do not flip status, do not run bin/flip-agreed, do not edit any review artifact, and do not edit bin/, specs/, docs/global-context/, policies/, or roles/. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-c-20260831T181500Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation amendment c (gate findings)", push with git push origin directive-authoring-consolidation (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-consol-c", created on the existing branch by: git worktree add "$TMPDIR/fiducial-da-consol-c" directive-authoring-consolidation
This reuses the existing local branch: no -b and no --no-track. Before creating it, run git fetch origin directive-authoring-consolidation, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation, or if "$TMPDIR/fiducial-da-consol-c" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin directive-authoring-consolidation. Judge every remote operation — fetch, push, ls-remote — by the refs it reports, not by credential-helper noise on stderr. The local branch directive-authoring-consolidation and origin/directive-authoring-consolidation must both be exactly c1983fe7a9c5b46c59b4e8f9e8b925408188419f; if either is anything else, stop and report. In the worktree, git rev-parse HEAD:skills/directive-authoring.md must be 43538c1bbc782f19b53e884bd46e08b67db5713b and HEAD:skills/directive-invariants.md must be f6ca0a6482a60d967e3bc647a3c04adeaec19179; if either differs, stop and report.

COMPANIONS, read whole from the worktree before writing: docs/cycles/directive-authoring-consolidation-20260831T150000Z.md @ 9cb11060498171782ccf378e3320d6829eeb0e07 and docs/cycles/directive-authoring-consolidation-b-20260831T172000Z.md @ b2b8bfa — their editing constraints bind this directive unchanged except where an edit below names the passage it changes; reviews/directive-authoring-cycle-4.md and reviews/directive-invariants-cycle-5.md, both at cd6c8347f7f4b3475c5bfeddf74aee47324e4bc7 via git show, for the findings these edits resolve. Also read both documents under edit, whole.

EDITS. Anchors are sentences in the file at c1983fe, the files wrap prose at 79 characters, so match every anchor as a sentence across line breaks, never as one line. If an anchor is not found exactly once, stop and report.

E1 (cycle-4 F-1), in skills/directive-authoring.md, first bullet: replace the words " and nowhere else" with ", which is their one definition", so the sentence reads: "the label's fixed form, the canonical sole-tree sentence, and a worked example of each form are stated in the Directive Invariants document, which is their one definition." Reflow the bullet at 79 characters.

E2 (cycle-4 F-2), in skills/directive-authoring.md, second bullet: replace "no other unfenced line" with "no other eligible line", so the bullet reads: "**The disposition label leads the disposition statement and no other eligible line.**"

E3 (byte-equality with E1), in skills/directive-invariants.md, the first fence of the section headed "## Working-tree disposition prompt": apply E1's replacement to the fence body — the same words, the same resulting sentence — and reflow the fence body at 79 characters. Fence markers, the framing sentence, and the second fence are unchanged. Confirm by the flow method (whitespace runs collapsed to one space, lines joined, the bullet's leading "- " stripped): fence body and the skill's first bullet are equal at 669 bytes each.

E4 (cycle-5 F-1), in skills/directive-invariants.md, the section headed "## Stop conditions": append one sentence to the end of the region's paragraph, directly after "do not retry with different flags, and do not delete or create any ref to recover.": A remote operation whose refs report success is not a failed command. Reflow at 79 characters; the marker line STOP CONDITIONS and the {{reviewed_ref}} placeholder are unchanged.

E5 (cycle-5 F-2), in skills/directive-invariants.md, the section headed "## Report format": replace the whole bullet "- every count reported, with the environment it was observed in — clone, worktree, or sandbox" (wrapped across two lines) with: - every count reported, with the tree it was observed in — the clone's main tree, or the worktree the directive assigns; a sandboxed run says so
Wrapped at 79 characters; position unchanged; the worktree-removal bullet remains last.

EDITING CONSTRAINTS: no ## section is added, removed, renamed, or reordered in either file; no region section's first body line changes except as E4 and E5 state; no fenced block is added, removed, or reordered; no other passage changes. After the edits the shipped unfenced_labelled_statements check (in bin/tests/test_directive.py) returns no hit over either file, and the bare label token does not appear in skills/directive-authoring.md. Frontmatter untouched: both files stay in-review, last-reviewed null.

SCOPE, one commit after the directive-file commit: skills/directive-authoring.md and skills/directive-invariants.md only. Commit message: "directive-authoring + directive-invariants: consolidation amendment c — gate findings (cycle-4 F-1/F-2, cycle-5 F-1/F-2)". Push with git push origin directive-authoring-consolidation.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-consol-c-run.log": bin/tests/run for the whole suite; per-file runs with python3 -m unittest discover -s bin/tests -t bin -p <file> for test_directive.py, test_directive_trd.py, and test_check_directive.py; bin/check-frontmatter --all (state exit code and count); the shipped unfenced_labelled_statements check over both files (expected: no hits); the E3 flow comparison (expected: 669 and 669, equal); grep -c "^- " over the Report format section's body (expected: 6); git diff --stat of the content commit (expected: exactly two files).
Expected state, and a stop if it differs: whole suite OK with zero failures and zero errors, 7 skipped; test_directive.py 43/43; test_directive_trd.py 16 passed + 6 skipped; test_check_directive.py 84/84; check-frontmatter exit 0, 61 files / 14 globs. Any red is a stop: report it with the assertion text; do not adjust a test and do not adjust either document to satisfy it.

GH: never invoke gh. Push the branch; pull requests #263 and #264 are the decision session's concern.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-consol-c" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref c1983fe7a9c5b46c59b4e8f9e8b925408188419f. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any anchor not found exactly once, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the content commit SHA, and the branch it is on
- the run-log path
- per edit E1 to E5, the changed passage verbatim as landed with its line numbers
- suite counts, whole and per the three files, each with the tree it was observed in; a sandboxed run says so
- check-frontmatter exit code and count
- the unfenced-label results, the E3 flow result, and the bullet count
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
