You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Revise skills/directive-invariants.md per the cycle-3 decisions below. You do not flip status, do not edit any review artifact, and do not edit bin/, specs/, docs/global-context/, policies/, or roles/. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-invariants-rev-3-20260830T0900Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-invariants cycle 3 revision", push with git push origin directive-invariants-rev-3 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-di-rev-3", created by: git worktree add --no-track "$TMPDIR/fiducial-di-rev-3" -b directive-invariants-rev-3 origin/directive-invariants-rev-2
Before creating it, run git fetch origin directive-invariants-rev-2, then git worktree list; if any existing worktree holds branch directive-invariants-rev-3, or if "$TMPDIR/fiducial-di-rev-3" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin, git fetch origin directive-invariants-rev-2, git fetch origin directive-invariants-gate-3. Judge each fetch by the refs it reports, not by credential-helper noise on stderr. origin/directive-invariants-rev-2 must be exactly fd35ed20f55689c28cf7714379097537b6d4accd; if it is anything else, stop and report. origin/directive-invariants-gate-3 must contain 065815e0d077dd401d2a5e9d4b14b71d37fcb393.

READ before writing, whole: the cycle-3 artifact via git show 065815e0d077dd401d2a5e9d4b14b71d37fcb393:reviews/directive-invariants-cycle-3.md; and from the worktree: skills/directive-invariants.md (the document under revision, at fd35ed2); specs/directive-tooling-trd.md §3.2, §3.4, §3.5; bin/aimeta/invariants.py and bin/aimeta/mdmask.py (to confirm which fences the parser reads and what unfenced_labelled_statements tests — you add, remove, or reorder no fence).

EDITING CONSTRAINTS, binding over every decision below; each decision has been read against them and none contradicts. No ## section is added, removed, renamed, or reordered. No region section's first body line changes. No fenced block is added, removed, or reordered anywhere. Region bodies are unchanged except the two places named: the second fence of ## Working-tree disposition prompt (O-1) and the last bullet of ## Report format (F-2). Preamble prose changes only where F-1 and O-2 name it. The four lint sections are untouched. The colon-terminated label literal continues to appear only inside fenced blocks, and no unfenced eligible line of the file satisfies the match rule after stripping — including the sentences you add. Frontmatter untouched: status stays draft. State rules; cite no file by path and no document by section number.

DECISIONS (Dave, 2026-08-30, at triage of reviews/directive-invariants-cycle-3.md):

### F-1 — accept
Finding: the preamble's fence-only sentence bounds containment of the emitted literal; the property the tooling tests is the match rule over unfenced eligible lines, which the sentence under-bounds.
Resolution: Replace the paragraph at lines 40–42 with: Outside fenced blocks, no eligible line of this document satisfies the match rule the Disposition label section states — after stripping, no unfenced line leads with the bare label token and carries a colon later on the same line. The emitted, colon-terminated literal — the form the first fence of that section carries — appears only inside fenced blocks; the bare token may appear in prose where it does not lead the line. Keep it as its own paragraph. Confirm by running the shipped unfenced-labelled-statements check that the file, including this paragraph, returns no hit.

### F-2 — accept
Finding: ## Report format's "the worktree-removal status" is emitted unconditionally, including into sole-tree directives with no worktree.
Resolution: Change that bullet, and only that bullet, to: - the worktree-removal status — or, under the sole-tree form, that no worktree existed. Marker line REPORT and every other bullet unchanged.

### O-2 — accept
Finding: fence order in the Disposition label section is load-bearing and the editor's format rules do not say so.
Resolution: Append one sentence to the format-rules paragraph at lines 18–22: In the Disposition label section the fences are positional — the first carries the emitted literal and the last carries the canonical sole-tree sentence — so no fence is added, removed, or reordered there.

### O-1 (the undefined <branch>) — accept as modify
Finding: <branch> is undefined in the worked exclusive-assignment example.
Resolution: In the second fence of ## Working-tree disposition prompt, change -b <branch> to -b <name> so the example's one placeholder names both the path and the branch: the command reads git worktree add --no-track "wt/<name>" -b <name> origin/main. Nothing else in the fence changes; "wt/<name>" still occurs exactly twice.

### F-1's sibling observations and everything else in the artifact — no action.

SCOPE, one commit: skills/directive-invariants.md only. Commit message: "directive-invariants: cycle 3 revision (F-1, F-2, O-1, O-2)". Push with git push origin directive-invariants-rev-3.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-di-rev-3-run.log": bin/tests/run for the whole suite; bin/check-frontmatter --all (state exit code and count); the shipped unfenced-labelled-statements check over skills/directive-invariants.md (state the call and the result, expected: no hits); a grep for the colon-terminated literal with each hit classified fenced or unfenced by the shipped masker (expected: all fenced); and a count over the second fence of ## Working-tree disposition prompt: "wt/<name>" exactly twice, "<branch>" zero times.
Expected state, and a stop if it differs: whole suite OK with zero failures and zero errors, 7 skipped; test_cross_cutting.py 17/17; test_cycle_open.py 62/62; test_directive.py 43/43; test_directive_trd.py 16 passed + 6 skipped; test_check_directive.py 84/84; check-frontmatter exit 0, 61 files / 14 globs. Any red is a stop: report it with the assertion text; do not adjust a test and do not adjust the document to satisfy it.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-invariants-rev-3 shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-di-rev-3" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref fd35ed20f55689c28cf7714379097537b6d4accd: on any failed command, any precondition not met, any decision above you cannot carry out inside the editing constraints, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; content commit SHA; branch name; run-log path; per decision, one line stating what changed and the line numbers; the four changed passages verbatim as landed; suite counts whole and per the five files; check-frontmatter exit code and count; the three self-check results; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
