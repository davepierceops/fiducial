You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Amend the consolidation revision on branch directive-authoring-consolidation with two region-text edits to skills/directive-invariants.md, ruled after the revision landed. You do not flip status, do not run bin/flip-agreed, do not edit any review artifact, and do not edit skills/directive-authoring.md, bin/, specs/, docs/global-context/, policies/, or roles/. No other session holds the branch or worktree named below; the worktree the prior revision used was removed and must not be recreated.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-b-20260831T172000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation amendment b (Report and Base verification regions)", push with git push origin directive-authoring-consolidation (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-consol-b", created on the existing branch by: git worktree add "$TMPDIR/fiducial-da-consol-b" directive-authoring-consolidation
This reuses the existing local branch: no -b and no --no-track (git rejects --no-track without -b; the form above was dry-run against a local branch at 759344c before dispatch). An earlier text of this amendment, never landed, carried the rejected flag; this file supersedes it. Before creating it, run git fetch origin directive-authoring-consolidation, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation, or if "$TMPDIR/fiducial-da-consol-b" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin directive-authoring-consolidation. Judge the fetch by the refs it reports, not by credential-helper noise on stderr. The local branch directive-authoring-consolidation and origin/directive-authoring-consolidation must both be exactly 759344c315d26ab1fe7336f9f0d13de0fe46af38; if either is anything else, stop and report. In the worktree, git rev-parse HEAD:skills/directive-invariants.md must be the blob the content commit 759344c landed — confirm with git diff --quiet 759344c315d26ab1fe7336f9f0d13de0fe46af38 -- skills/directive-invariants.md (exit 0); if it differs, stop and report.

COMPANION, read whole from the worktree before writing: docs/cycles/directive-authoring-consolidation-20260831T150000Z.md @ 9cb11060498171782ccf378e3320d6829eeb0e07 — the revision this amends; its editing constraints on skills/directive-invariants.md bind this directive unchanged, except that the two region bodies named below now change. Also read skills/directive-invariants.md whole.

EDITS, in order, to skills/directive-invariants.md. Anchors are exact strings in the file at 759344c; if an anchor is not found exactly once, stop and report.

E1. In the section headed "## Report format", insert one bullet directly after the bullet "- what was verified, how, and where the run log is" and before the bullet "- anything observed this directive did not anticipate":

- every count reported, with the environment it was observed in — clone, worktree, or sandbox

The marker line REPORT and every other bullet are unchanged; the worktree-removal bullet remains last.

E2. In the section headed "## Base verification", replace the sentence "Judge the fetch by the refs it reports, not by a credential helper's noise on stderr." — which the file wraps across two lines at 759344c, so match it as a sentence, not as one line — with: Judge every remote operation — fetch, push, ls-remote — by the refs it reports, not by a credential helper's noise on stderr. Reflow the paragraph at the document's 79-character width; the marker line BASE VERIFICATION, the {{reviewed_ref}} placeholder, and the two sentences around it are unchanged in wording.

EDITING CONSTRAINTS: no ## section is added, removed, renamed, or reordered; no region section's first body line changes; no fenced block is added, removed, or reordered; no other region body changes; the preamble and the four lint sections are untouched. After the edits the shipped unfenced_labelled_statements check (in bin/tests/test_directive.py) returns no hit over the file. Frontmatter untouched: status stays in-review, last-reviewed stays null.

SCOPE, one commit after the directive-file commit: skills/directive-invariants.md only. Commit message: "directive-invariants: Report region counts carry their environment; Base verification judges every remote operation by refs (consolidation amendment b)". Push with git push origin directive-authoring-consolidation.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-consol-b-run.log": bin/tests/run for the whole suite; per-file runs with python3 -m unittest discover -s bin/tests -t bin -p <file> for test_directive.py, test_directive_trd.py, and test_check_directive.py; bin/check-frontmatter --all (state exit code and count); the shipped unfenced_labelled_statements check over skills/directive-invariants.md (expected: no hits); grep -c "^- " over the Report format section's body (expected: 6); git diff --stat of the content commit (expected: exactly one file).
Expected state, and a stop if it differs: whole suite OK with zero failures and zero errors, 7 skipped; test_directive.py 43/43; test_directive_trd.py 16 passed + 6 skipped; test_check_directive.py 84/84; check-frontmatter exit 0, 61 files / 14 globs. Any red is a stop: report it with the assertion text; do not adjust a test and do not adjust the document to satisfy it.

GH: never invoke gh. Push the branch; the pull request already open on it updates in place.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-consol-b" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 759344c315d26ab1fe7336f9f0d13de0fe46af38. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any anchor not found exactly once, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the content commit SHA, and the branch it is on
- the run-log path
- per edit E1 and E2, the changed passage verbatim as landed with its line numbers
- suite counts, whole and per the three files, each with the environment it was observed in
- check-frontmatter exit code and count
- the unfenced-label result and the bullet count
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
