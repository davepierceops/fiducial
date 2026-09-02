# Decision Layer cycle 12 — Context Quality Reviewer gate Directive

Date: 2026-09-02
Documents in scope:
- docs/global-context/decision-layer.md @ 3e89a2117e35f34746aff005c19bc3c6227bf8f4

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/decision-layer-cycle-12-gate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-decision-layer-cycle-12-gate", created by: git fetch origin decision-layer-human-review && git worktree add --no-track "$TMPDIR/fiducial-decision-layer-cycle-12-gate" -b decision-layer-cycle-12-gate origin/decision-layer-human-review

## Decisions

No findings precede this gate; nothing is disposed here. This directive
opens cycle 12's review of the human-review revision on branch
decision-layer-human-review.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored
nothing under review. Full-depth review of
docs/global-context/decision-layer.md @ 3e89a2117e35f34746aff005c19bc3c6227bf8f4
against docs/global-context/review-rubric.md and LEXICON.md, with these
bounds:

1. The revision's content is Dave's, ruled 2026-08-31 (topic-walk ruling 1)
   and 2026-09-01 (in the review): the seven applied changes, rule 3's
   inversion, rule 12's retro-on-request, the compression, and old rule
   16's deletion are rulings. A finding against a ruled intent is not
   filed; a finding on wording, conformance, or a consequence the ruling
   did not weigh is.
2. Verify the deletions left no orphan: every cut sentence's behavior
   survives in Core, the Lexicon, the decision log, or a governed skill —
   or its absence was the ruling. Cite where each survives.
3. Verify the renumbering blast radius: no in-scope document cites a
   Decision Layer rule number now stale (the directive-tooling spec and
   TRD cite rule 14, which kept its number — confirm by reading both).
4. Known and queued, record but do not file: skills/conversation-retro.md
   at HEAD defers to rule 12's standing obligation and auto-runs at chat
   close; its conforming revision is queued as its own full cycle.

ARTIFACT. Produce reviews/decision-layer-cycle-12.md per
skills/review-artifact.md, verdict first; Prior cycle is
reviews/decision-layer-cycle-11.md. This session creates exactly two
files — this directive file and the review artifact — and modifies
nothing. Review only.

## Deferred / out of scope

- Findings triage, any fix, the agreement flip, and the merge of
  decision-layer-human-review to main — the decision session's next steps.
- The conversation-retro conforming cycle — queued separately.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin decision-layer-cycle-12-gate, without -u.
- Do not open a pull request; the decision session opens it, into
  decision-layer-human-review, not main.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
3e89a2117e35f34746aff005c19bc3c6227bf8f4 on branch decision-layer-human-review. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/global-context/decision-layer.md @ 3e89a2117e35f34746aff005c19bc3c6227bf8f4
- docs/global-context/core.md @ 941d7f2482fa260f42147ab52647d813bac17e16
- LEXICON.md @ 17960bb7570e1a0abe6ca0492e35f95a15d627cf
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- reviews/decision-layer-cycle-11.md @ d85daf4f75251f3cce23ff261456c2556dadd4cd

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
   "$TMPDIR/fiducial-decision-layer-cycle-12-gate-frontmatter.log", exit
   status reported.
2. grep -rniE "decision.layer rule [0-9]+" over the frontmatter in-scope
   set and specs/, output captured to the same directory; every hit stated
   with whether its cited number is current at the reviewed ref.
3. The review artifact's verdict line stated verbatim in the report, with
   findings by severity.

STOP CONDITIONS

Pinned to the reviewed ref 3e89a2117e35f34746aff005c19bc3c6227bf8f4 on branch decision-layer-human-review. Cannot execute as written: stop
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

    Decision Layer cycle 12 — Context Quality Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
