# Converging model — Context Quality Reviewer branch gate Directive

Date: 2026-09-02
Documents in scope:
- policies/document-metadata-policy.md @ 4129a453b59dd32dedcb5afc6b9512602fd49128
- operating-model.md @ 03ece2f57758cfee74b76cc760adda2f19627631
- roles/test-designer-agent.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
- skills/spec-review-cycle.md @ 58790b3e14aab0c47ea48c4a577e2d7517d07dc6
- skills/review-artifact.md @ 96a18367a5d316ecc29032e5692bda60b314eede
- LEXICON.md @ f93dcf7ad29034b76dfa43d40615071f67d75411
- context-sets/spec-and-change-discipline.md @ dd86a8a99349324a02bb87c8ab373f937de8f7c3

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/converging-model-gate-directive.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

```text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
```

Both admitted forms, worked:

```text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-converging-model-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-converging-model-gate" -b converging-model-gate origin/main

## Decisions

No findings precede this gate; nothing is disposed here. This directive
opens the review of a branch, not a re-gate.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored nothing
under review (the Editor revision was a different session; this directive's
author drafted neither the documents nor the revision). Full-depth review of
the seven documents in scope at their named revisions, against
docs/global-context/review-rubric.md and LEXICON.md conformance, as one
review over one range:

Baseline: 2c9c5842a96c523529523f986d6a111508d15898 (main before the branch)
Reviewed: 3a511a1e6353428948a923a751423ac47c7f8a8b (main at the merge)

The reviewed range is git diff 2c9c5842a96c523529523f986d6a111508d15898..3a511a1e6353428948a923a751423ac47c7f8a8b
over the seven documents; read each document whole at the reviewed ref, and
the range diff for what changed. Three questions the review answers, in
addition to the rubric:
1. Are the eight ruled changes recorded in
   docs/cycles/converging-model-editor-directive.md (CM-0 through CM-7)
   faithfully realized, and do the seven documents now state one consistent
   model — one status name, one entry rule, one exit rule, one three-valued
   build-gating rule — with no two of them disagreeing? Intent was binding,
   wording the Editor's; a wording choice is not a finding unless it breaks a
   rubric criterion, the lexicon, or a ruled intent.
2. Do the three Editor judgment calls disclosed in the execution report hold
   against the rubric and DEC-000360: the metadata policy's per-task
   confirmation exception removed rather than kept; "Specs agreed" now
   closing change-flow step 4; the exit gate run by the role that gated the
   document (Spec Reviewer for specs)?
3. Does any live governing text outside the seven — every file
   bin/check-frontmatter --all reports in scope — still state the old
   two-status order (test plan after specs agreed; build-gating with a
   per-task exception)? Verify by grep over the in-scope set at the reviewed
   ref; a hit is a finding naming the file.

LOOP START (told — the decision session's statement, Dave's to override):
the agreement bar for this cycle is a verdict of ready or ready-with-findings
with zero blocking findings across the branch; cadence is this one gate over
the branch, then a fix directive if warranted, then one confirmation-scoped
re-gate over the fix, then seven flips by bin/flip-agreed, one invocation
per document.

ARTIFACT. Produce reviews/converging-model-cycle-1.md per
skills/review-artifact.md at its reviewed revision — the artifact stem names
the branch; the header carries Baseline: and Reviewed: as above and lists all
seven documents with their SHAs; verdict first. Before writing it, confirm
the path is absent at the base ref (git cat-file -e 3a511a1e6353428948a923a751423ac47c7f8a8b:reviews/converging-model-cycle-1.md
must fail); if it exists, stop and report. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only: no edits to any governed file.

## Deferred / out of scope

- Findings triage, any fix directive, the re-gate, and the seven flips — the
  decision session's next steps after this report.
- The bin/ package enforcing `converging` — a separate package; not reviewed
  here. That STATUSES in bin/aimeta/frontmatter.py lacks the value is known
  and is not a finding.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin converging-model-gate — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
3a511a1e6353428948a923a751423ac47c7f8a8b. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ 4129a453b59dd32dedcb5afc6b9512602fd49128
- operating-model.md @ 03ece2f57758cfee74b76cc760adda2f19627631
- roles/test-designer-agent.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
- skills/spec-review-cycle.md @ 58790b3e14aab0c47ea48c4a577e2d7517d07dc6
- skills/review-artifact.md @ 96a18367a5d316ecc29032e5692bda60b314eede
- LEXICON.md @ f93dcf7ad29034b76dfa43d40615071f67d75411
- context-sets/spec-and-change-discipline.md @ dd86a8a99349324a02bb87c8ab373f937de8f7c3
- docs/cycles/converging-model-editor-directive.md @ 0c84d626d35686d04a039cf2c6fd122ccc6e460f
- decisions/log.md @ 15b1a874c6fdb1cbbebe89ce149ab81409a3acd5
- reviews/spec-review-cycle-cycle-11.md @ d66a89333f85682f69f7424e60fd91d51cbc30f7
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d

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
   "$TMPDIR/fiducial-converging-model-gate-frontmatter.log", exit status
   reported.
2. The artifact's header carries Baseline and Reviewed as stated above and
   names all seven documents at their SHAs; its verdict line is first. State
   both, labelled observed.
3. The grep for question 3, output captured to
   "$TMPDIR/fiducial-converging-model-gate-grep.log"; state the hit count.

STOP CONDITIONS

Pinned to the reviewed ref 3a511a1e6353428948a923a751423ac47c7f8a8b. Cannot execute as written: stop
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

    Converging model — Context Quality Reviewer branch gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
