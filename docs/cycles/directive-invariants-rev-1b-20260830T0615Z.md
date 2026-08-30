You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Revise skills/directive-invariants.md per the cycle-1 decisions below. You do not flip status, do not edit the review artifact, and do not edit bin/, specs/, docs/global-context/, policies/, or roles/. This directive supersedes docs/cycles/directive-invariants-rev-1-20260830T0600Z.md, which was never written; its base-verification guard was too broad.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-invariants-rev-1b-20260830T0615Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-invariants cycle 1 revision (reissue, narrowed guard)", push with git push origin directive-invariants-rev-1 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-di-rev-1", created by: git worktree add --no-track "$TMPDIR/fiducial-di-rev-1" -b directive-invariants-rev-1 origin/main
Before creating it, run git worktree list; if any existing worktree holds branch directive-invariants-rev-1, or if "$TMPDIR/fiducial-di-rev-1" already exists, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin and git fetch origin directive-invariants-gate. Judge the fetch by the refs it reports, not by credential-helper noise on stderr. origin/main must contain 7c233c1506dc6111194b5fe603f2fd2f967d4998. If origin/main is beyond it, proceed only if no commit past it touches any of: skills/directive-invariants.md, skills/directive-authoring.md, specs/directive-tooling-trd.md, bin/aimeta/, bin/directive, bin/check-directive, bin/cycle-open, bin/tests/test_directive.py, bin/tests/test_directive_trd.py, bin/tests/test_check_directive.py, bin/tests/test_cycle_open.py, bin/tests/test_cross_cutting.py; otherwise stop and report. Other paths under bin/ do not trip the guard. origin/directive-invariants-gate must contain bc2577fa70a346efd67fe7e68e9d0e8898cca0fc.

READ before writing, whole: the review artifact via git show bc2577fa70a346efd67fe7e68e9d0e8898cca0fc:reviews/directive-invariants-cycle-1.md; and from the worktree: skills/directive-invariants.md (the document under revision); skills/directive-authoring.md; specs/directive-tooling-trd.md §3.3, §3.4, §3.5, §3.6; docs/global-context/review-rubric.md; bin/aimeta/invariants.py (to confirm what the parser reads: section names, first-body-line markers, and the fences the lint sections carry — you change none of those).

EDITING CONSTRAINTS, binding over every decision below. No ## section is added, removed, renamed, or reordered. The first non-blank line of every section's body is unchanged. In the seventeen region sections, the body text is unchanged except where a decision below names an edit; every region body remains what is emitted into skeletons. No fenced block's content changes except where a decision names it. The disposition label literal WORKING-TREE DISPOSITION: continues to appear only inside fenced blocks — never in prose, never in this directive's own text landing in that file. All prose additions go in the preamble (above ## Heading (general)) or in the unfenced prose of the four lint sections (## Disposition label, ## Marker syntax, ## Preamble markers, ## Match phrases). State rules; cite no file by path and no document by section number — where the TRD states a rule you need, state the rule here in this file's own words. Frontmatter untouched: status stays draft.

DECISIONS (Dave, 2026-08-30, at triage of reviews/directive-invariants-cycle-1.md):

### F-1 — accept
Finding: match rule's "exactly that literal" takes the colon-bearing fence as antecedent; code and the TRD match the bare token.
Resolution: In ## Disposition label, keep the fenced emitted literal WORKING-TREE DISPOSITION: as is. Restate the match rule so the token is named in prose without the colon — the leading content, after stripping, is exactly the label token WORKING-TREE DISPOSITION with no trailing colon counted as part of it, followed by a colon anywhere later on the same line. Write the bare token in backticks in prose, not in a fence, so the fence-only property holds (the bare token without colon is not the label literal; confirm by reading that invariants.py's label_literal() reads the fence and nothing else).

### F-2 — accept
Finding: the closed placeholder set is sourced to TRD tables that do not fix the three cycle-heading placeholders.
Resolution: Replace the sentence citing "the TRD's §3.3 tables" with a statement of the closed set in the preamble, per region: Heading (general): title. Heading (cycle): heading, date, scope_list. Route and model: route, model. First act: directive_path. Base verification: reviewed_ref. Companions: companion_list. Stop conditions: reviewed_ref. Source manifest: manifest. Every other region: none. An unrecognised placeholder remains a refusal. Verify the list against the actual {{…}} tokens in each region body before committing; any difference is a stop, not a silent correction. The TRD cycle-table column is a rider tracked in the decision session — not yours.

### F-3 — accept
Finding: bin/ paths named; "eligible line" and "after stripping" undefined.
Resolution: Replace the sentence naming bin/aimeta/invariants.py, bin/directive and bin/check-directive with the property it was cited for: the label, the marker syntax and every region's text have exactly one definition, and that definition is this file; the generator and the lint both read it here. Then, in ## Disposition label's prose, state what makes a line eligible and what stripping removes, in enough words to apply the match rule by hand, taking the substance from the TRD's masking rules without citing them: an eligible line is one outside fenced code blocks and outside HTML comments; stripping removes leading whitespace and leading Markdown list or blockquote markers (state exactly the set the TRD names — read it and carry the set, not a paraphrase of it).

### F-4 — reject, recorded
Finding: ## Stop conditions restates Core rules 11 and 15.
Resolution: No action. The region is emitted skeleton text that the lint's M4 element matches on; it is by-value quotation of the same class as the disposition prompt's governed rule, not a bundle rule stated twice. Recorded for audit.

### F-5 — reject, recorded
Finding: ## Claim labels restates Core rule 6.
Resolution: No action, same ground as F-4 (M7). Recorded for audit.

### F-6 — accept
Finding: preamble carries rationale.
Resolution: Cut the three clauses the finding locates ("so the label, the marker syntax…" — replaced under F-3; "so the generator copies the marker rather than composing it"; and the sentence beginning "That is the one property of this one file…"). State the rules they were justifying, bare: the label appears in this document only inside fenced blocks; a region section's body opens with that region's marker line.

### F-7 — accept as modify
Finding: the parse-schema paragraph addresses the maintainer, not the reading agent.
Resolution: Keep the schema; restate it as an instruction to whoever edits this file, opening with a sentence to that effect, and retaining the rule that the first non-blank line of a body is always body.

### F-8 — accept
Finding: no session-kind statement.
Resolution: Add to the preamble, as its own sentence: This document is read by the generator a decision session runs; its region bodies are emitted into directives that execution sessions carry out, and are not standing instructions to the reader of this file.

### F-9 — accept
Finding: exclusive-assignment test carries no disclosure that it is a match bound.
Resolution: In ## Disposition label's prose, immediately after the exclusive-assignment form test, add one sentence: this test bounds what the lint matches and adds no requirement on how a disposition is written; a disposition in another form is a lint miss, not a violation.

### F-10 — accept
Finding: nothing says the model value is a tier.
Resolution: In the preamble's placeholder list (F-2), annotate: model — a tier (frontier, solid general-purpose, cheap), never a model name; route — fresh or existing session. No change to the region body.

### F-11 — accept
Finding: five match-phrase blocks for eight elements, absence unexplained.
Resolution: In ## Match phrases, change the opening line to say one fenced block per element that compiles a phrase, and add a line stating that M2 and M8 match no phrase and M3's strings are those of ## Disposition label, so none of the three carries a block here.

### F-12 — accept
Finding: <document heading> in the preamble-markers fence is not a literal and nothing marks it.
Resolution: Leave the fence unchanged. Add one prose sentence in ## Preamble markers: the first entry stands for whatever heading line the mode emits and is not matched as a literal; the second is matched as a literal.

### O-1 — accept as modify
Finding: worked example git worktree add "wt/<n>" main fails when main is checked out in the primary tree.
Resolution: In ## Working-tree disposition prompt's second fence, change the exclusive-assignment worked example's command to: git worktree add --no-track "wt/<n>" -b <branch> origin/main — the path token stays quoted; nothing else in either fence changes. This is emitted text; the test suite is the check.

### O-2 — no action
### O-3 — no action (the byte-equality test gap is tracked separately)

SCOPE, one commit: skills/directive-invariants.md only. Commit message: "directive-invariants: cycle 1 revision (F-1, F-2, F-3, F-6..F-12, O-1)". Push with git push origin directive-invariants-rev-1.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-di-rev-1-run.log": bin/tests/run for the whole suite; bin/check-frontmatter --all (state exit code and count); and a self-check that the string WORKING-TREE DISPOSITION: occurs in skills/directive-invariants.md only on lines inside fenced blocks (state the command and the line numbers found).
Expected state, and a stop if it differs: test_cross_cutting.py 17/17; test_cycle_open.py 62/62; test_directive.py 43/43; test_directive_trd.py green except its 6 skips; test_check_directive.py 84/84; the only reds in the suite, if any, the three pre-existing cases outside directive tooling (test_scope sc1 and sc3, test_check_frontmatter cf13); check-frontmatter exit 0, 61 files / 14 globs. Any other red is a stop: report it with the assertion text, do not adjust a test and do not adjust the document to satisfy it.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-invariants-rev-1 shows your commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-di-rev-1" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 7c233c1506dc6111194b5fe603f2fd2f967d4998: on any failed command, any precondition not met, any decision above you cannot carry out inside the editing constraints, any placeholder-list mismatch under F-2, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; content commit SHA; branch name; run-log path; per decision, one line stating what changed and where (line numbers); the full new preamble verbatim; pass/fail/skip counts for the whole suite and for each of the five files named above; the named red cases with the one-line reason each; check-frontmatter exit code and count; the label self-check result; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
