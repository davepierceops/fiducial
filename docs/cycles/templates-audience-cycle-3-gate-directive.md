# PRD and TRD templates audience cycle 3 — Spec Reviewer gate Directive

Date: 2026-09-04
Documents in scope:
- specs/prd-template.md @ 6d05d0156511527bb00e27e1e905e6cbbdebe695
- specs/trd-template.md @ 473c1c81b004db9c981e48c516d9961fc8454e26

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/templates-audience-cycle-3-gate-directive.md, commit it alone with a
message naming the gate it opens, push with git push origin templates-audience-cycle-3-gate (no -u), verify by git ls-remote origin templates-audience-cycle-3-gate, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-templates-audience-cycle-3-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-templates-audience-cycle-3-gate" -b templates-audience-cycle-3-gate origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch templates-audience-cycle-3-gate, if a branch of that name already exists locally or on origin (git ls-remote origin templates-audience-cycle-3-gate returns a ref), or if "$TMPDIR/fiducial-templates-audience-cycle-3-gate" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

No findings precede this gate; nothing is disposed here. This directive opens
the review, not a re-gate.

ROLE AND TASK. This session fills one role: Spec Reviewer Agent per
roles/spec-reviewer-agent.md, independent — this session authored nothing
under review (the Editor revision was a different session; this directive's
author drafted neither template nor the revision). Two documents, two gates,
two artifacts — one document, one cycle, one verdict each, per
skills/spec-review-cycle.md; nothing in one artifact depends on the other.
Full-depth review of each template at its revision:

- specs/prd-template.md @ 6d05d0156511527bb00e27e1e905e6cbbdebe695
- specs/trd-template.md @ 473c1c81b004db9c981e48c516d9961fc8454e26

against docs/global-context/review-rubric.md and LEXICON.md conformance, and
against the template's own purpose as a skeleton a project copies. The one
change recorded in docs/cycles/templates-audience-cycle-3-directive.md (TA3-1
for the PRD template, TA3-2 for the TRD template) was dictated wording:
`audience: [human]` in the skeleton frontmatter block; confirm each is
realized exactly and that nothing else in the body moved (the Editor reports
three changed lines per file; verify against the diff from each document's
cycle-2 reviewed revision, the parent of its content commit). Cross-check in
scope: the skeleton value against AC-BS-5 of specs/bundle-system.md and
against the top-level audience of every file under specs/ at the base ref —
every spec is [human]; record agreement or disagreement. A finding against
the templates' pre-existing text is in scope — this is full-depth — but the
ruled value itself is not open: AC-BS-5 and Dave's 2026-08-28 ruling
(OPEN-ITEMS.md, entry "PRD and TRD templates carry the wrong audience —
directed fix") settle it. Finding ids take this cycle's prefix: PT3-n for the
PRD template, TT3-n for the TRD template.

LOOP START (told — the decision session's statement, Dave's to override): the
agreement bar for each document is a verdict of ready or ready-with-findings
with zero blocking findings; cadence is one full-depth gate (this directive),
then a fix directive if findings warrant one, then one confirmation-scoped
re-gate over the fix, then one flip per document citing its artifact at its
reviewed SHA.

ARTIFACTS. Produce reviews/prd-template-cycle-3.md and
reviews/trd-template-cycle-3.md per skills/review-artifact.md, each verdict
first, its Reviewed: line naming its document at the SHA above in full, and
stating in its own scope that it reviewed that document at that SHA. Before
writing either, confirm both paths are absent at the base ref (git cat-file -e
aba461a2d8839af546318448e123be485f973411:reviews/prd-template-cycle-3.md and the same for
reviews/trd-template-cycle-3.md must both fail); if either exists, stop and
report. This session creates exactly three files — this directive file and
the two review artifacts — and modifies nothing. Review only: no edits to
either template or any governed file. Commit the two artifacts in one commit
after the directive's own.

## Deferred / out of scope

- Findings triage, any resulting fix directive, the re-gates, and the two
  agreement flips — the decision session's next steps after this report;
  tracked by the cycle.
- specs/bundle-system.md §5 wording residues — folded by Dave's ruling
  (2026-09-03) into that PRD's next substantive opening; not this gate's.
- The templates' top-level frontmatter audience values — unchanged and
  correct; a finding against them is out of scope.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin templates-audience-cycle-3-gate — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files. A compound command after a cd has been
  rejected whole and silently by the sandbox's ~/.ssh deny rule (told — an
  executor's report); use absolute paths and one git command per invocation,
  and confirm each commit landed with git log before proceeding.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-templates-audience-cycle-3-gate" (no --force). If it fails, report the
  failure; do not retry. Your report's final line states whether the worktree
  was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
aba461a2d8839af546318448e123be485f973411. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- specs/prd-template.md @ 6d05d0156511527bb00e27e1e905e6cbbdebe695
- specs/trd-template.md @ 473c1c81b004db9c981e48c516d9961fc8454e26
- docs/cycles/templates-audience-cycle-3-directive.md @ 045ef2480189a304b58863c29efed76b66e50018 — the Editor directive; TA3-1 and TA3-2.
- roles/spec-reviewer-agent.md @ e4110f0cc3e47a245a51289b9aa00639ccf05fdb
- skills/spec-review-cycle.md @ 0911b06042f62aabb5de9d5fa49547e93b1eeed8
- skills/review-artifact.md @ 5d593a742b6726861b7f57a6d93cc31851b2408b
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41
- specs/bundle-system.md @ 4d6373a6d73e44023fdc86961e1d49a36eb0b342 — AC-BS-5 and the file's own frontmatter.
- reviews/prd-template-cycle-2.md and reviews/trd-template-cycle-2.md at the base ref — the prior verdicts, for continuity.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Named verification, before the final push:

1. bin/check-frontmatter --all, output captured to
   "$TMPDIR/fiducial-templates-audience-cycle-3-gate-frontmatter.log", exit status reported (expected 0).
2. git diff --stat aba461a2d8839af546318448e123be485f973411..HEAD in the worktree: exactly three added files —
   this directive and the two review artifacts; state it, labelled observed.
3. Each artifact's Reviewed: line names its document at its SHA above
   character-for-character; state both, labelled observed.
4. git diff --stat 6d05d0156511527bb00e27e1e905e6cbbdebe695~1..6d05d0156511527bb00e27e1e905e6cbbdebe695 and 473c1c81b004db9c981e48c516d9961fc8454e26~1..473c1c81b004db9c981e48c516d9961fc8454e26: one file each, three
   lines changed each; state both, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref aba461a2d8839af546318448e123be485f973411. Cannot execute as written: stop
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

    PRD and TRD templates audience cycle 3 — Spec Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    Decisions — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Deferred / out of scope — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Execution notes — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
