# Bundle-system PRD cycle 2 — confirmation-scoped re-gate Directive

Date: 2026-09-02
Documents in scope:
- specs/bundle-system.md @ 7c50f0fd1c8f648d3e95a527edaf7125b7b07ab4

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-system-cycle-2-regate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-bundle-cycle-2-regate", created by: git worktree add --no-track "$TMPDIR/fiducial-bundle-cycle-2-regate" -b bundle-cycle-2-regate origin/main

## Decisions

This is a re-gate. It disposes nothing and takes no new decision; the
cycle-1 dispositions are ruled and stand. This session fills one role:
Spec Reviewer per roles/spec-reviewer-agent.md, independent — it authored
nothing under review. Confirm exactly three things, NOT a second full
read — cycle 1 read the document whole:

1. Each cycle-1 disposition is realized as ruled in
   docs/cycles/bundle-system-cycle-1-fix-directive.md — B-1's stated
   collision, ruled rename, and dictated uniqueness phrase; R-2's lore
   home with the four labels verbatim; N-1 through N-8 per the artifact's
   Fix lines; O-1 through O-3 and O-5 applied or queued as ruled; O-4
   queued. The fix report's landing locations are chat-held, so confirm
   against the document and the diff, not a report.
2. The two Editor judgment calls hold: (a) O-1 resolved by reordering so
   G11 keeps meaning lore — confirm no goal reference in the document or
   in reviews/bundle-system-cycle-1.md went stale; (b) N-1's AC-BS-4
   states the writing sets under both outcomes of OQ-1 rather than
   choosing — confirm it is conditional, consistent, and decides nothing
   OQ-1 owns.
3. No new contradiction between the changed text (the diff cf3b87e to
   7c50f0f) and the governed text it cites. Do not re-derive cycle-1
   findings; do not re-open dispositioned items.

A finding outside these confirmations is out of scope unless it is a new
blocking contradiction introduced by the fix, in which case file it.

ARTIFACT. Produce reviews/bundle-system-cycle-2.md per
skills/review-artifact.md, verdict first; state the confirmation scope in
the Scope line; Prior cycle is reviews/bundle-system-cycle-1.md. Expected
verdicts: ready or ready-with-findings if the confirmations hold;
changes-required only on a failed confirmation or a new blocking
contradiction. Before writing it, confirm by listing that
reviews/bundle-system-cycle-2.md does not exist at the base; if it exists,
stop and report. This session creates exactly two files — this directive
file and the review artifact — and modifies nothing. Review only.

## Deferred / out of scope

- The tagging package (sre-critic rename, retags, order: fields), the
  remaining OQs, and spec agreement — the decision session's later steps.
- The sre-critic decision-log entry — the next flush.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin bundle-cycle-2-regate, without -u.
- Do not open a pull request; push the branch and report. The decision
  session opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
270c44aa9520dff29dc7a0073156b2d491f94438. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- specs/bundle-system.md @ 7c50f0fd1c8f648d3e95a527edaf7125b7b07ab4
- reviews/bundle-system-cycle-1.md @ 42636f35f4407ffacc37626ab8f0240fb0c70740
- docs/cycles/bundle-system-cycle-1-fix-directive.md @ 267ad210c189b630570736808faf8001d4fe3fd2
- roles/spec-reviewer-agent.md @ a092f4938256503a5d894eeb9c05c5a777b72cde
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- specs/prd-template.md @ 39b04d90e87267d260ee925ed3d5e3b3ccfd1f67

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
   "$TMPDIR/fiducial-bundle-cycle-2-regate-frontmatter.log", exit status
   reported.
2. The confirmation diff (git diff cf3b87e08cf6257ee09c7066a3a53ed2adafcd15
   7c50f0fd1c8f648d3e95a527edaf7125b7b07ab4 -- specs/bundle-system.md)
   captured beside it.
3. The review artifact's verdict line stated verbatim in the report, with
   each confirmation stated pass/fail and its evidence class.

STOP CONDITIONS

Pinned to the reviewed ref 7c50f0fd1c8f648d3e95a527edaf7125b7b07ab4 (the document commit) on main at 270c44aa9520dff29dc7a0073156b2d491f94438. Cannot execute as written: stop
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

    Bundle-system PRD cycle 2 — confirmation-scoped re-gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
