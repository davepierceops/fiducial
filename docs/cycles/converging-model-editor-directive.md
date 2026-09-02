# Converging model — branch-scoped Editor revision Directive

Date: 2026-09-02
Documents in scope:
- policies/document-metadata-policy.md @ 1d6213baf82bd2a9eeb4c10e9dc9b8fb78025390
- operating-model.md @ b206f517d96d59c321917479d49f29b1c1d55798
- roles/test-designer-agent.md @ 0959c1379a3a597b7fdcdc9b53b04aca91cd3480
- skills/spec-review-cycle.md @ 7600590f900fd195eeb0763e87f36bbf4ec1f092
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- LEXICON.md @ 17960bb7570e1a0abe6ca0492e35f95a15d627cf
- context-sets/spec-and-change-discipline.md @ cac23b8c9e6f3335e930acb7ceb024bd4959c8a9

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/converging-model-editor-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-converging-model", created by: git worktree add --no-track "$TMPDIR/fiducial-converging-model" -b converging-model origin/main

## Decisions

This is a branch-scoped Editor revision: one branch carries the edits to
every document in scope, and one Context Quality Reviewer gate over the
branch follows in a later directive — the multi-document gate practised at
PRs #211, #215, #218, #221. It disposes the six non-blocking findings and one
observation of reviews/spec-review-cycle-cycle-11.md (N-1..N-6, O-1) and
carries the ruling that reshaped N-1 (told — Dave, 2026-09-02, this cycle's
triage in the decision session): convergence is the standard change flow, not
an exception, and the state has a name. Intent is binding; wording is the
Editor's except where "Dictated wording" says otherwise.

### CM-0 — the ruling this revision encodes
Finding: the Convergence section landed at cycle 11 contradicts three agreed
texts (N-1) — the metadata policy's build-gating rule, the operating model's
change-flow order, and the Test Designer role — and the reviewer asked which
file yields.
Resolution: the three texts yield; the Convergence section is rewritten to the
converging model below and nothing in it is conditioned on an exception.
The model:
- A fourth agreed-route status, `converging`, between `in-review` and
  `agreed`. A document enters it after its first reviewer gate has run
  (any verdict), on Dave's say, by a frontmatter-only status-transition
  commit — the same shape as the agreement flip, and exempt from the
  edit-flips-in-review rule the same way.
- While `converging`, the spec is edited freely and the Test Designer writes
  tests against it; a content edit to a `converging` document leaves its
  status and `last-reviewed` unchanged (nothing is agreed yet, so there is
  nothing to reset). Findings flow both ways through the decision session.
- Entry point and exit point are read from git, not maintained: the entry
  SHA is the transition commit that set `converging`; the exit SHA is the
  reviewed SHA the exit gate cites. The exit gate directive states both —
  Baseline: <entry sha>, Reviewed: <exit sha> — and reviews the diff between
  them together with the tests; the review artifact carries both lines.
  Dave reads that diff before the flip.
- Exit is one ruling by Dave: the spec flips `agreed` (frontmatter-only
  commit, as today); the tests' acceptance as red-gate evidence is recorded in
  the exit gate's review artifact, not in the flip commit; implementation
  begins only after both.
- The build-gating rule becomes three-valued: `draft` / `in-review` — nothing
  is built or tested against it; `converging` — tests yes, implementation no;
  `agreed` — build.
Dictated wording: none, except the status value `converging` and the
directive-header labels `Baseline:` and `Reviewed:`.

### CM-1 — policies/document-metadata-policy.md — accept
Finding: the status enum and the build-gating rule (Agent behavior, "Do not
build against a draft or in-review spec") do not admit the model.
Resolution: add `converging` to the `status:` enum with a one-line meaning;
state its entry transition (after the first gate, Dave's, frontmatter-only,
exempt from the edit-flips rule as the other transitions are) and that
content edits to a `converging` document do not change status or
`last-reviewed`; restate the build-gating rule three-valued per CM-0. Note
that `status: converging` requires no `last-reviewed` (it is not agreed).
State in one sentence that enforcement of the new value lands as a `bin/`
change before any document enters it.
Dictated wording: none beyond CM-0's.

### CM-2 — operating-model.md — accept
Finding: change-flow steps 1–4 order the test plan after specs agreed, which
the model reverses.
Resolution: reorder and reword the change flow so that after the first spec
gate the spec enters `converging`, the test plan is written and confirmed red
against it, spec and tests converge, and one ruling agrees the spec and
accepts the tests; implementation (step 5) follows both. Conform the
Definition of done and the change-package list where they assume the old
order. Do not touch the two riders queued for this document in OPEN-ITEMS.md
(spike step; mutation-as-coverage) — they are not in scope.
Dictated wording: none.

### CM-3 — roles/test-designer-agent.md — accept
Finding: the role derives tests from acceptance criteria only and is silent on
working against a `converging` spec.
Resolution: state that during convergence the Test Designer works against the
`converging` spec and its acceptance criteria, files spec findings through the
decision session where a test cannot be derived, verifies each disposition
against the spec and discloses deviation, and hands the red-gate result to the
exit gate as its evidence.
Dictated wording: none.

### CM-4 — skills/spec-review-cycle.md — accept (disposes N-1..N-6, O-1)
Finding: the Convergence section and the re-gate forms carry the cycle-11
findings.
Resolution: rewrite the Convergence section to CM-0's model, using
`converging` and never "open" for the state (O-1); state the unit and record
of the joint flip per CM-0 (N-3); add `test-designer-agent` to the audience
(N-2); route below-stage findings to the loose-end tracker, which
context-sets/spec-and-change-discipline.md already names for this, and say
"change package" where the text says "implementation package" (N-4); state
the confirmation-scoped read as the named resolutions plus the revision's
diff against the governed text it cites, and state in Procedure step 7 that
the executor discloses any deviation from a disposition (N-5); state that the
agreement bar and gate cadence are Dave's, recorded in the cycle's opening
directive (N-6). Add the exit-gate range statement (Baseline/Reviewed) to the
directive format this skill describes.
Dictated wording: none beyond CM-0's.

### CM-5 — skills/review-artifact.md — accept
Finding: the artifact header names one revision; a range review has two
(cycle-5 schema feedback item 4, tracked in OPEN-ITEMS.md).
Resolution: add an optional `Baseline: <path> @ <sha>` header line, stated as
required when the artifact reviews a range — an exit gate or a reconciliation.
Dictated wording: `Baseline:`.

### CM-6 — LEXICON.md — accept
Finding: the model introduces a term the lexicon lacks, and "open" now
collides with "open spec delta".
Resolution: define **Converging** under Spec state — the status and the
interval, entry and exit as CM-0 states — and add one sentence
distinguishing it from an open spec delta (a delta is a branch interval on an
agreed spec; converging is a status interval before first agreement). Apply
the touch rule to any other edited file.
Dictated wording: none.

### CM-7 — context-sets/spec-and-change-discipline.md — accept
Finding: "The red-gate" and "Open spec delta" sections do not mention the
converging interval, and the loose-end tracker sentence now receives
below-stage findings by name.
Resolution: one cross-reference sentence in "The red-gate" stating that the
red-gate runs during convergence and its result is the exit gate's evidence;
one sentence distinguishing convergence from the open spec delta, mirroring
CM-6. No other change.
Dictated wording: none.

### CM-8 — decisions/log.md — accept
Finding: the ruling is unlogged (Decision Layer: a decision is logged in the
session that makes it).
Resolution: append the entry below as its own commit on the branch, after the
document commits, touching decisions/log.md only.
Dictated wording, verbatim:

```text
## DEC-000360 — Convergence is the standard change flow; `converging` is a status
Date: 2026-09-02
Decision: Spec and tests converge before agreement, as the standard change
flow, not an exception. A fourth agreed-route status, `converging`, sits
between `in-review` and `agreed`: entered after the first reviewer gate on
Dave's say by a frontmatter-only transition; while converging the spec is
edited freely and the Test Designer writes tests against it, and content
edits change neither status nor `last-reviewed`; exited by one exit gate
over the diff from the entry transition commit to the reviewed SHA plus the
tests, Dave's read of that diff, and one ruling that flips the spec agreed
and records the tests' acceptance in the exit artifact. Building against a
document is three-valued: draft/in-review nothing; converging tests only;
agreed implementation. Enforcement of the value lands as a bin/ package
before the first document enters it.
Context: Owner decision (Dave), 2026-09-02, triaging
reviews/spec-review-cycle-cycle-11.md N-1, which found the cycle-11
Convergence section contradicting the metadata policy, the operating model,
and the Test Designer role. Dave refused an exception-shaped fix: the rules
say convergence is how it is done, and the three texts yield. Landed by
docs/cycles/converging-model-editor-directive.md as one branch-scoped cycle.
```

## Deferred / out of scope

- The Context Quality Reviewer gate over this branch — a later directive;
  then a fix, a confirmation-scoped re-gate, and per-document flips by
  bin/flip-agreed. Cycle 11 of skills/spec-review-cycle.md closes into this
  branch; its findings are disposed here and its flip is this branch's.
- The bin/ package enforcing `converging`: bin/aimeta/frontmatter.py STATUSES
  admits the value; a content edit to a `converging` document is not flipped
  by the hook; bin/flip-agreed accepts `converging` as a source status and as
  a --status target for the entry transition; tests red then green. Its ACs
  are written by the decision session; it lands before any document enters
  `converging`. Tracked in OPEN-ITEMS.md at the next flush.
- The two operating-model riders and every other queued cycle — OPEN-ITEMS.md.

## Execution notes

- Edit only the seven documents in scope and decisions/log.md. One content
  commit per document, in the order CM-1 through CM-7, each flipping that
  document's status to in-review and last-reviewed to null per the revision
  lifecycle; then the CM-8 commit alone. A changed fact changes everywhere it
  appears within these files; name any place outside them in the report.
- Leave every edited document conformant to docs/global-context/review-rubric.md
  and to LEXICON.md (the touch rule).
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin converging-model — no -u; the sandbox refuses the
  .git/config write. Process substitution (<(...)) is refused by the sandbox;
  use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
2c9c5842a96c523529523f986d6a111508d15898. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ 1d6213baf82bd2a9eeb4c10e9dc9b8fb78025390
- operating-model.md @ b206f517d96d59c321917479d49f29b1c1d55798
- roles/test-designer-agent.md @ 0959c1379a3a597b7fdcdc9b53b04aca91cd3480
- skills/spec-review-cycle.md @ 7600590f900fd195eeb0763e87f36bbf4ec1f092
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- LEXICON.md @ 17960bb7570e1a0abe6ca0492e35f95a15d627cf
- context-sets/spec-and-change-discipline.md @ cac23b8c9e6f3335e930acb7ceb024bd4959c8a9
- reviews/spec-review-cycle-cycle-11.md @ d66a89333f85682f69f7424e60fd91d51cbc30f7
- docs/cycles/spec-review-cycle-cycle-11-editor-directive.md @ 9a2e82b3388c71eb30b65da8d7e2202fbf65b9e4
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- decisions/log.md @ f56ec0a85ad8e797c682f5655af637edd96d95c0
- OPEN-ITEMS.md @ f56ec0a85ad8e797c682f5655af637edd96d95c0

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
   "$TMPDIR/fiducial-converging-model-frontmatter.log", exit status reported.
   Expected: exit 0 — no document carries status: converging yet, so the
   hardcoded enum is not exercised.
2. grep -rn -i "converging" over the seven documents, LEXICON.md included,
   output to "$TMPDIR/fiducial-converging-model-grep.log"; state the count per
   file, labelled observed.
3. Read each revised document once against its CM entry and state where the
   change landed (section or line), labelled observed.
4. grep -c "^## DEC-000360" decisions/log.md, expected 1.

STOP CONDITIONS

Pinned to the reviewed ref 2c9c5842a96c523529523f986d6a111508d15898. Cannot execute as written: stop
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

    Converging model — branch-scoped Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
