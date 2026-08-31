You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Revise skills/directive-invariants.md per the cycle-2 decisions below. You do not flip status, do not edit any review artifact, and do not edit bin/, specs/, docs/global-context/, policies/, or roles/. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-invariants-rev-2-20260830T0730Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-invariants cycle 2 revision", push with git push origin directive-invariants-rev-2 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-di-rev-2", created by: git worktree add --no-track "$TMPDIR/fiducial-di-rev-2" -b directive-invariants-rev-2 origin/directive-invariants-rev-1
Before creating it, run git fetch origin directive-invariants-rev-1, then git worktree list; if any existing worktree holds branch directive-invariants-rev-2, or if "$TMPDIR/fiducial-di-rev-2" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin, git fetch origin directive-invariants-rev-1, git fetch origin directive-invariants-gate-2. Judge each fetch by the refs it reports, not by credential-helper noise on stderr. origin/directive-invariants-rev-1 must be exactly 875bfb2ab714a7011ffe45850f3709ec61ec5ca6; if it is anything else, stop and report. origin/directive-invariants-gate-2 must contain e27792c5495ad6ecd7ae7c6ffe9b63c1bafe58a7.

READ before writing, whole: the cycle-2 artifact via git show e27792c5495ad6ecd7ae7c6ffe9b63c1bafe58a7:reviews/directive-invariants-cycle-2.md; and from the worktree: skills/directive-invariants.md (the document under revision, at 875bfb2); specs/directive-tooling-trd.md §3.2, §3.4, §3.5; bin/aimeta/invariants.py (to confirm which fences the parser reads — you add, remove, or reorder none).

EDITING CONSTRAINTS, binding over every decision below; each decision has been read against them and none contradicts. No ## section is added, removed, renamed, or reordered. No region section's first body line changes. No fenced block is added, removed, or reordered anywhere in the file. Region bodies are unchanged except the one fence F-1 names. Prose in the preamble (above ## Heading (general)) and in the four lint sections may change only where a decision names it. The literal WORKING-TREE DISPOSITION: continues to appear only inside fenced blocks. Frontmatter untouched: status stays draft. State rules; cite no file by path and no document by section number.

DECISIONS (Dave, 2026-08-30, at triage of reviews/directive-invariants-cycle-2.md):

### F-1 — accept
Finding: the worked exclusive-assignment example declares "wt/<name>" and creates "wt/<n>".
Resolution: In ## Working-tree disposition prompt's second fence, change the command's path token so both tokens read "wt/<name>": the line becomes  worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b  with <branch> origin/main continuing on the next line as landed. Nothing else in the fence changes.

### F-2 — accept
Finding: the preamble's fence-only sentence names "the disposition label" without saying whether it means the emitted literal or the bare token; the bare token appears in backticked prose.
Resolution: Rewrite the preamble sentence at line 40 to bound the emitted literal: The label literal the generator emits, `WORKING-TREE DISPOSITION:`, appears in this document **only inside fenced blocks**; the bare token may appear in prose. Keep it as its own paragraph.

### F-3 — accept
Finding: the sole-tree form's membership test is not stated.
Resolution: In ## Disposition label, immediately after the canonical sole-tree sentence's fence, add one sentence: Sole-tree form: the extent contains that sentence literally, reproduced exactly — capitalisation and full stop included; a paraphrase carries no admitted form. No fence is added.

### F-4 — accept
Finding: "line endings are normalised" states neither which endings nor to what.
Resolution: In ## Disposition label's eligibility paragraph, replace "Line endings are normalised before masking" with: Line endings are normalised before masking — `\r\n` and `\r` become `\n`. Rest of the sentence unchanged.

### F-5 — accept
Finding: the placeholder escape is not stated.
Resolution: Extend the preamble's syntax sentence at line 24 to: Placeholders are written `{{name}}`; `{{{{` is a literal `{{`. The set is closed and fixed per region: — keeping the list that follows unchanged.

### O-1, O-2, O-3 — no action (O-2 and O-3 are tracked in the decision session).

SCOPE, one commit: skills/directive-invariants.md only. Commit message: "directive-invariants: cycle 2 revision (F-1..F-5)". Push with git push origin directive-invariants-rev-2.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-di-rev-2-run.log": bin/tests/run for the whole suite; bin/check-frontmatter --all (state exit code and count); a self-check that the string WORKING-TREE DISPOSITION: occurs in skills/directive-invariants.md only on lines inside fenced blocks (state the command and line numbers); and a self-check that the second fence of ## Working-tree disposition prompt contains "wt/<name>" exactly twice and "wt/<n>" not at all.
Expected state, and a stop if it differs: whole suite OK with zero failures and zero errors, 7 skipped; test_cross_cutting.py 17/17; test_cycle_open.py 62/62; test_directive.py 43/43; test_directive_trd.py 16 passed + 6 skipped; test_check_directive.py 84/84; check-frontmatter exit 0, 61 files / 14 globs. Any red is a stop: report it with the assertion text; do not adjust a test and do not adjust the document to satisfy it.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-invariants-rev-2 shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-di-rev-2" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 875bfb2ab714a7011ffe45850f3709ec61ec5ca6: on any failed command, any precondition not met, any decision above you cannot carry out inside the editing constraints, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; content commit SHA; branch name; run-log path; per decision, one line stating what changed and the line numbers; the five changed passages verbatim as landed; suite counts whole and per the five files; check-frontmatter exit code and count; both self-check results; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
