# Rule extraction — Pass 3, whole agent-facing corpus at fd54448

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/rule-extraction-pass3-20260904T210000Z.md, commit it alone with a
message naming the pass it opens, push with git push origin rule-extraction-pass3 (no -u), verify by git ls-remote origin rule-extraction-pass3, and report the
SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

~~~text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
~~~

Both admitted forms, worked:

~~~text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
~~~

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-rule-extraction-pass3", created by: git worktree add --no-track "$TMPDIR/fiducial-rule-extraction-pass3" -b rule-extraction-pass3 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch rule-extraction-pass3, if a branch of that name already exists locally or on origin (git ls-remote origin rule-extraction-pass3 returns a ref), or if "$TMPDIR/fiducial-rule-extraction-pass3" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
fd5444870b40d4fd93cc63d833d6d40358246fba. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/rule-register/rule-register-20260825T1435.md @ 6d2744bef0cb4344d85081eeb41d84b77fb75652 — the Pass 1 register; read its header and first forty rows only, for the column shape. It is stale (pinned to f9a7a5e8) and is not an input to this pass.
- The 54 files listed under TASK, all read from the base ref fd5444870b40d4fd93cc63d833d6d40358246fba, whole. These are the corpus.

TASK

Pass 3 of the corpus deduplication, first half: extract every rule in the agent-facing governed corpus at the base ref into one register. Extraction only — no merging, no judgment about duplicates, no edit to any governed file. The second half (clustering and the row count) is a separate directive that consumes this register; do not attempt it here.

This session does the work itself: no sub-sessions, no subagents, no fan-out.

IN SCOPE — exactly these 54 files, the in-scope set of the document-metadata policy minus the 8 files whose audience is human alone. Read each from the worktree at the base ref, in this order, whole:

    1. LEXICON.md
    2. boundaries/human-review-boundary.md
    3. context-sets/production-grade-software.md
    4. context-sets/spec-and-change-discipline.md
    5. context-sets/testing-and-verification.md
    6. docs/global-context/core.md
    7. docs/global-context/decision-layer.md
    8. docs/global-context/review-rubric.md
    9. engagements/assistant.md
    10. engagements/cartographer.md
    11. engagements/sre-critic.md
    12. engagements/sre/README.md
    13. engagements/sre/baseline-measurement.md
    14. engagements/sre/engagement-change-package.md
    15. engagements/sre/implementer.md
    16. engagements/sre/override-log-policy.md
    17. engagements/sre/speed-audit.md
    18. engagements/sre/system-discovery.md
    19. engagements/working-with-dave.md
    20. operating-model.md
    21. policies/commit-and-change-control-policy.md
    22. policies/decision-log-policy.md
    23. policies/document-metadata-policy.md
    24. policies/project-setup-requirements.md
    25. policies/release-readiness-policy.md
    26. policies/remote-write-verification-policy.md
    27. policies/source-of-truth-policy.md
    28. policies/verification-boundary-policy.md
    29. public-prose-criteria.md
    30. roles/architect-agent.md
    31. roles/chief-of-staff.md
    32. roles/coder-agent.md
    33. roles/context-quality-reviewer.md
    34. roles/copy-editor.md
    35. roles/critic.md
    36. roles/release-manager-agent.md
    37. roles/reviewer-agent.md
    38. roles/skeptic-risk-agent.md
    39. roles/spec-reviewer-agent.md
    40. roles/test-designer-agent.md
    41. roles/writer.md
    42. skills/boundary-audit.md
    43. skills/command-blocks.md
    44. skills/conversation-retro.md
    45. skills/directive-authoring.md
    46. skills/directive-invariants.md
    47. skills/evidence-review.md
    48. skills/outline.md
    49. skills/review-artifact.md
    50. skills/spec-review-cycle.md
    51. skills/test-plan-review.md
    52. specs/prd-template.md
    53. specs/trd-template.md
    54. voice.md

OUT OF SCOPE: everything else, including the 8 human-only files (specs/bin-land.md, specs/bin-land-trd.md, specs/bundle-system.md, specs/directive-tooling.md, specs/directive-tooling-trd.md, vendors/README.md, vendors/claude-code/environment-config.md, voice-template.md), reviews/, retros/, docs/cycles/, docs/rule-register/ except for the file this pass writes, bin/.

WHAT A RULE IS: one sentence or clause that binds an agent or a human to do, not do, or do-under-condition something. Definitions in LEXICON.md and in any file's vocabulary section count (verb: define). A frontmatter field does not count. Rationale, examples, worked illustrations, and context do not count, but a rule stated inside an example counts once. When a sentence carries two obligations, emit two rows. When unsure whether something is a rule, emit it with binds set to unsure.

OUTPUT — write docs/rule-register/rule-register-20260904T210000Z.md with this exact shape:

~~~text
# Rule register — Pass 3 extraction

Derived artifact. Source: davepierceops/fiducial @ fd5444870b40d4fd93cc63d833d6d40358246fba. Extraction only; no deduplication performed. Supersedes docs/rule-register/rule-register-20260825T1435.md.

Files read: 54. Rows: <M>.

| id | file | line | binds | verb | rule | condition | source |
|---|---|---|---|---|---|---|---|
| R0001 | LEXICON.md | 12 | all | define | ... | — | "..." |
~~~

Column rules:
- id: R + four digits, sequential in the file order above, then line order.
- file: repo-relative path.
- line: line number of the source sentence in that file at the base ref.
- binds: one of all, decision, execution, dave, human, a role slug taken from the file's own frontmatter audience or its heading (chief-of-staff, coder-agent, writer, sre-critic, ...), or unsure.
- verb: one of require, forbid, define, escalate, stop.
- rule: the obligation restated in plain words, present tense, no file names, no rationale. No length cap; write the shortest restatement that loses nothing an agent would act on. (The Pass 1 "twelve words" was a column width, not a rule; it does not apply.)
- condition: the triggering condition in plain words, or —.
- source: the verbatim sentence, in double quotes, pipes escaped as \|.

Write the register incrementally: append each file's rows as soon as that file is done, so a session that ends early leaves a partial register on disk. Do not skip a file because it looks rule-free; a file with no rules gets no rows and still counts in "Files read".

VERIFY before committing: (1) choose 15 rows by a stated rule (every 60th id from R0001), and for each confirm by grep that the source string is present verbatim at the stated file and line at the base ref; report id and pass/fail for each; (2) confirm the Rows count in the header equals the number of table rows (a command, its output stated); (3) confirm every id is unique and sequential with no gaps (a command, its output stated).

COMMIT: the register alone, message "docs/rule-register: Pass 3 extraction at fd54448". Run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-rule-extraction-pass3-fm.log" and state its exit status (expected 0; docs/rule-register/ is out of its scope). Never bypass the pre-commit hook.

Push with git push origin rule-extraction-pass3 (no -u) and verify by git ls-remote origin rule-extraction-pass3: the tip must be the register commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-rule-extraction-pass3" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

REPORT ADDITIONS, after the standard report items: files read and rows, one line; rows with binds=unsure; per-file row counts, one line each, 54 lines; the three verification results; anything you could not extract, with file and line, and why.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

STOP CONDITIONS

Pinned to the reviewed ref fd5444870b40d4fd93cc63d833d6d40358246fba. Cannot execute as written: stop
and report. Concurrent tree mutation: stop and report. On any failed command,
any precondition not met, or any tree mutation you did not intend, including
your own — stop and report; do not retry with different flags, and do not
delete or create any ref to recover. A remote operation that exits successfully
is not a failed command, whatever a credential helper writes to stderr.

REPORT

- the directive file's commit SHA
- every commit SHA this session landed, in order, and the branch they are on
- what was verified, how, and where the run log is
- every count reported, with the tree it was observed in — the clone's main
  tree, or the worktree the directive assigns; a sandboxed run says so
- anything observed this directive did not anticipate
- the worktree-removal status — or, under the sole-tree form, that no worktree
  existed

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    Rule extraction — Pass 3, whole agent-facing corpus at fd54448 — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    TASK — author region
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
