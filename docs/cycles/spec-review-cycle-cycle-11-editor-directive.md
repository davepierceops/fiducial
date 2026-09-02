# Spec-review-cycle skill cycle 11 — Editor revision Directive

Date: 2026-09-02
Documents in scope:
- skills/spec-review-cycle.md @ 9d5456cb8010ed8efddf9500af8dd2771c38f5e3

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/spec-review-cycle-cycle-11-editor-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-spec-review-cycle-11", created by: git worktree add --no-track "$TMPDIR/fiducial-spec-review-cycle-11" -b spec-review-cycle-11 origin/main

## Decisions

This is an Editor revision opening the cycle, not a findings disposition: no
review artifact precedes it. Each entry below is a ruled change (told — Dave's
rulings, recorded in OPEN-ITEMS.md @ f56ec0a85ad8e797c682f5655af637edd96d95c0,
"Topic walk 2026-08-31 — rulings" item 3, "Retrospective session 2026-08-31 —
follow-ups" item 6, and the entry "Convergence process — canonization owed";
and in retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203,
topics T09 and T20). Intent is binding; wording is the Editor's — no wording is
dictated. The document is on the expedited path's ineligible list; a full
Context Quality Reviewer gate follows this revision in a later directive.

### SR-1 — accept
Finding: a re-gate has been used to take new decisions, which puts a ruling in
a review artifact where no cycle directive records it.
Resolution: state that a re-gate disposes the findings of the cycle it closes
and takes no new decisions; a new decision opens its own cycle at step 1.
Dictated wording: none.

### SR-2 — accept
Finding: the agreement bar and the gate cadence are decided ad hoc per cycle,
and a gate scoped to confirmation of named resolutions exists in practice
(conversation-retro cycle 4, bundle-system cycle 2) but not in the skill.
Resolution: require that the agreement bar (what verdict satisfies the flip —
ready or ready-with-findings, per the document metadata policy) and the gate
cadence are stated at loop start; and admit the confirmation-scoped re-gate as
a named form — a re-gate whose scope is confirmation that named resolutions
landed, stated as such in its directive and its artifact.
Dictated wording: none.

### SR-3 — accept
Finding: findings below the reviewed document's stage (a PRD gate raising TRD
questions, a spec gate raising implementation questions) are filed as
blockers against the document under review.
Resolution: state that such findings route to the next stage's question list
and are not filed as blocking findings against the reviewed document.
Dictated wording: none.

### SR-4 — accept
Finding: when a reviewer names a defect class and lists its instances, the
instances have been triaged one by one before the class was ruled on.
Resolution: state that a named defect class is triaged before its instances —
one ruling on the class, then the instances dispose under it.
Dictated wording: none.

### SR-5 — accept
Finding: the convergence process — spec and tests revised together, findings
flowing both ways, joint flip — ran ad hoc for the directive-tooling TRD
(reviews/directive-tooling-trd-cycle-1.md through cycle-3.md; the
docs/cycles/directive-tooling-trd-* chain) and is written nowhere.
Resolution: write the convergence shape into this skill as its own section:
the spec stays open while the Test Designer writes tests against it; neither
is final until they cohere; findings flow both ways; the decision session is
the mediating agent between the two execution sessions; dispositions are
intent — the executor verifies against the counterparty's artifact and
discloses any deviation; when they cohere, both flip agreed together. If the
Editor judges a sibling skill the better home, stop and report — this
directive's scope is one document.
Dictated wording: none.

## Deferred / out of scope

- The Context Quality Reviewer gate over this revision — a later directive
  from the decision session; tracked by the cycle itself.
- The orchestrator question the topic walk closed into this cycle (ruling 9)
  — closed by SR-5's mediating-agent statement; nothing further is owed.
- Every other cycle the 2026-08-31 rulings opened — tracked in OPEN-ITEMS.md,
  "Topic walk 2026-08-31 — rulings".

## Execution notes

- Edit skills/spec-review-cycle.md only. The content edit flips
  status: in-review and last-reviewed: null in the same commit, per the
  document metadata policy's revision lifecycle.
- Leave the document conformant to docs/global-context/review-rubric.md and to
  LEXICON.md (the touch rule); the Context Quality Reviewer gates the result
  in a later directive.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin spec-review-cycle-11 — no -u; the sandbox refuses
  the .git/config write. Process substitution (<(...)) is refused by the
  sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
1d100e1ba7b2d941f0615e0b974075c89fa70681. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/spec-review-cycle.md @ 9d5456cb8010ed8efddf9500af8dd2771c38f5e3
- OPEN-ITEMS.md @ f56ec0a85ad8e797c682f5655af637edd96d95c0
- retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203
- reviews/directive-tooling-trd-cycle-1.md @ fcd7377aeb9f201dcec3fe9e03eeae60b2e00d4a
- reviews/directive-tooling-trd-cycle-2.md @ d6ed0c7dcf58a2dcaeb98b45dceab859c9cc931a
- reviews/directive-tooling-trd-cycle-3.md @ 667346159973d99a5c9955b6129c97e36d0d7b5c
- docs/cycles/conversation-retro-cycle-4-regate-directive.md @ c0c20b68296e7db03d45f5101559c1d91241945b
- context-sets/spec-and-change-discipline.md @ cac23b8c9e6f3335e930acb7ceb024bd4959c8a9
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- policies/document-metadata-policy.md @ 1d6213baf82bd2a9eeb4c10e9dc9b8fb78025390
- LEXICON.md @ 17960bb7570e1a0abe6ca0492e35f95a15d627cf

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
   "$TMPDIR/fiducial-spec-review-cycle-11-frontmatter.log", exit status
   reported.
2. Read the revised document once against each of the five Decisions entries
   and state, per entry, where its change landed (section or line), labelled
   observed.

STOP CONDITIONS

Pinned to the reviewed ref 1d100e1ba7b2d941f0615e0b974075c89fa70681. Cannot execute as written: stop
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

    Spec-review-cycle skill cycle 11 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
