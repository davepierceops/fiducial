# Converging model — nine agreement flips Directive

Date: 2026-09-02
Documents in scope:
- policies/document-metadata-policy.md @ d96ef65a802fba5735aae432222cab44c976fdc6
- operating-model.md @ bf0fa24d250325f1b63ee138752803288ce34f67
- roles/test-designer-agent.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
- skills/spec-review-cycle.md @ 0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e
- skills/review-artifact.md @ 96a18367a5d316ecc29032e5692bda60b314eede
- LEXICON.md @ 2ae1d055380a780b351e04c364dfd47d22cd5d48
- context-sets/spec-and-change-discipline.md @ 468798e83dd076b2f5772faa03e1749b3ead9176
- roles/chief-of-staff.md @ 0685f4d7fb34910e36ca94a51cc1fdf94fa13308
- roles/spec-reviewer-agent.md @ eb15a8bbdd03fdff075bf75539802d2eca3455f5

ROUTE AND MODEL

Route: fresh
Model: solid

FIRST ACT

Write this directive verbatim to docs/cycles/converging-model-agree-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-converging-model-agree", created by: git worktree add --no-track "$TMPDIR/fiducial-converging-model-agree" -b converging-model-agree origin/main

## Decisions

Dave agreed the nine documents of the converging-model branch on
2026-09-02 (told), on reviews/converging-model-cycle-2.md — verdict
ready-with-findings, zero blocking — which satisfies the agreed gate; its
two non-blocking findings (N-6, N-7) open their own cycle and do not bar
this flip. No judgment is exercised here: nine flips, in the order below,
each citing the artifact at that document's reviewed SHA as the artifact's
Reviewed line names it.

### FLIP-1 — policies/document-metadata-policy.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for policies/document-metadata-policy.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ d96ef65a802fba5735aae432222cab44c976fdc6
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only policies/document-metadata-policy.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-2 — operating-model.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for operating-model.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ bf0fa24d250325f1b63ee138752803288ce34f67
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only operating-model.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-3 — roles/test-designer-agent.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for roles/test-designer-agent.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only roles/test-designer-agent.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-4 — skills/spec-review-cycle.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for skills/spec-review-cycle.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ 0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only skills/spec-review-cycle.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-5 — skills/review-artifact.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for skills/review-artifact.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ 96a18367a5d316ecc29032e5692bda60b314eede
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only skills/review-artifact.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-6 — LEXICON.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for LEXICON.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ 2ae1d055380a780b351e04c364dfd47d22cd5d48
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only LEXICON.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-7 — context-sets/spec-and-change-discipline.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for context-sets/spec-and-change-discipline.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ 468798e83dd076b2f5772faa03e1749b3ead9176
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only context-sets/spec-and-change-discipline.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-8 — roles/chief-of-staff.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for roles/chief-of-staff.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ 0685f4d7fb34910e36ca94a51cc1fdf94fa13308
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only roles/chief-of-staff.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

### FLIP-9 — roles/spec-reviewer-agent.md
Run bin/flip-agreed once, as a single standalone invocation (never inside a
loop), for roles/spec-reviewer-agent.md with the review pointer exactly:
reviews/converging-model-cycle-2.md @ eb15a8bbdd03fdff075bf75539802d2eca3455f5
The tool commits on its own — one commit per invocation, never a
caller-authored combined commit. Before the next flip, verify the commit
touches only roles/spec-reviewer-agent.md and only its frontmatter (git show --stat; the diff is
status: in-review → agreed and last-reviewed: null → the pointer above,
nothing else). If the tool fails or the diff is anything else, stop and
report; do not edit frontmatter by hand and do not retry with different
flags.

## Deferred / out of scope

- N-6 and N-7 of reviews/converging-model-cycle-2.md — the next cycle on
  context-sets/spec-and-change-discipline.md and roles/chief-of-staff.md;
  tracked at the flush.
- The bin/ package enforcing `converging`.

## Execution notes

- This session runs a tree that contains the review artifact it cites:
  reviews/converging-model-cycle-2.md must exist at the base ref; if not,
  stop and report.
- Nine flip commits and the directive-file commit are this branch's whole
  content; nothing else is edited.
- Push with git push origin converging-model-agree — no -u; the sandbox
  refuses the .git/config write.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed (git ls-remote
  origin converging-model-agree shows the ninth flip commit), remove your own
  worktree from the main tree: git worktree remove "$TMPDIR/fiducial-converging-model-agree"
  (no --force). Report the result as the final line.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
fcdecf330a0ab34277e23ac069634a2aa80dda40. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ d96ef65a802fba5735aae432222cab44c976fdc6
- operating-model.md @ bf0fa24d250325f1b63ee138752803288ce34f67
- roles/test-designer-agent.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
- skills/spec-review-cycle.md @ 0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e
- skills/review-artifact.md @ 96a18367a5d316ecc29032e5692bda60b314eede
- LEXICON.md @ 2ae1d055380a780b351e04c364dfd47d22cd5d48
- context-sets/spec-and-change-discipline.md @ 468798e83dd076b2f5772faa03e1749b3ead9176
- roles/chief-of-staff.md @ 0685f4d7fb34910e36ca94a51cc1fdf94fa13308
- roles/spec-reviewer-agent.md @ eb15a8bbdd03fdff075bf75539802d2eca3455f5
- reviews/converging-model-cycle-2.md @ 01c29474ee4d6be7c8c387c348de28321c7ec9bb

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Named verification, after the ninth flip and before the push:

1. bin/check-frontmatter --all, output captured to
   "$TMPDIR/fiducial-converging-model-agree-frontmatter.log", exit status
   reported; expected exit 0.
2. git log --oneline against the base ref, captured to
   "$TMPDIR/fiducial-converging-model-agree-log.log"; expected: exactly ten
   commits — the directive file, then nine flips in the order above.
3. grep -c "^status: agreed" across the nine documents, expected 9; state
   the count, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref fcdecf330a0ab34277e23ac069634a2aa80dda40. Cannot execute as written: stop
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

    Converging model — nine agreement flips Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
