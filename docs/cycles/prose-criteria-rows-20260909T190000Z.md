# Prose-criteria rows: merge the three read-first rows, re-cite R1013 and R0038

ROUTE AND MODEL

Route: fresh session
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/prose-criteria-rows-20260909T190000Z.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-prose-criteria-rows", created by: git worktree add --no-track "$TMPDIR/fiducial-prose-criteria-rows" -b prose-criteria-rows origin/main

Holder check, before the worktree is created: fetch origin main, run git worktree list, and stop and report if any worktree holds branch prose-criteria-rows or the path already exists. Push every commit with: git push origin prose-criteria-rows — no upstream is set.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
28dfdb0560cafcda026c70cd1c7697751b3eac26. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- rules/R1161.md @ 28dfdb0
- rules/R0953.md @ 28dfdb0
- rules/R1001.md @ 28dfdb0
- rules/R1013.md @ 28dfdb0
- rules/R0038.md @ 28dfdb0
- rules/R1603.md @ 28dfdb0 — the newest row; its frontmatter is the convention for a row born in the store
- process/named-queries.md @ 28dfdb0 — the topic list; voice is an existing topic
- every row whose frontmatter carries topic public-prose-criteria (17 rows at the reviewed ref; list them with: grep -l '^topic:.*public-prose-criteria' rules/*.md)

TASK

This is a rules delta: one commit carrying the proposed rows, for the Context Quality Reviewer's intake read. It is a Dave-agreed change (decision session, 2026-09-09); the rulings are in the Decisions section below.

1. Read the seventeen public-prose-criteria rows and identify by ID: (a) the row or rows whose body holds the list of tells; (b) the row or rows holding the structure defects; (c) the row or rows naming the four claim-strength tiers (relayed, demonstrated, grounded, opinion). If any of the three is not identifiable as one or more specific rows, stop and report which.
2. Create one new row with the next ID from bin/next-id, frontmatter per R1603's convention, keys exactly: topic [voice]; role [writer, copy-editor, critic]; session [decision]; corpus [writing]; verb require; condition "before you write, edit, or read the piece"; term null; order: the lowest unused position in the voice topic. Body is the dictated wording in Decisions D-1.
3. Delete rules/R1161.md, rules/R0953.md, rules/R1001.md.
4. Rewrite the body of rules/R1013.md per D-2, and the body of rules/R0038.md per D-3, substituting the IDs found in step 1. Frontmatter of both unchanged.
5. Sweep rules/ and process/ for any remaining citation of R1161, R0953, or R1001 by ID; if one exists, stop and report it — do not edit the citing file.
6. Sweep rules/ (excluding the seventeen criteria rows) and process/ for any other body that names "Public Prose Criteria" as a thing to read or fetch. Report each as an observation; do not edit.
7. One commit for steps 2–4 together, message "rules: one read-first row for the writing roles; R1013 and R0038 cite the criteria rows by ID". Push.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- bin/tests/run 2>&1 | tee "$TMPDIR/prose-criteria-rows-tests.log" — expected: OK, exit 0.
- For each of writer, copy-editor, critic: bin/bundle --where role=<slug> --name <slug> --out "$TMPDIR" 2>&1 | tee -a "$TMPDIR/prose-criteria-rows-bundles.log"; then grep -c the new row's ID in each generated bundle — expected 1 in each — and grep -c 'R1161\|R0953\|R1001' — expected 0 in each. Report the three bundle paths.
- git diff --stat origin/main..HEAD — expected: 6 files (the directive, the new row, three deletions, two edits).

STOP CONDITIONS

Pinned to the reviewed ref 28dfdb0560cafcda026c70cd1c7697751b3eac26. Cannot execute as written: stop
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
- the new row's ID and the IDs substituted into R1013 and R0038
- the step-6 observations, one line each

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

## Decisions

### D-1 — accept
Finding: R1161, R0953, R1001 state one rule three times, each keyed to one role and each telling the role to read a document (the Public Prose Criteria) that no longer exists as a document; the criteria are rows already in the role's bundle.
Resolution: one row keyed to all three roles supersedes the three; it names only the Voice document, which exists in the bundle as process/voice.md.
Dictated wording: Read the Voice document before you write, edit, or read the piece, every time.

### D-2 — modify
Finding: R1013 names "the Public Prose Criteria's list" and "its structure defects" as a container the critic cannot locate in a bundle.
Resolution: cite the rows by ID. Angle-bracketed slots are yours to fill from step 1; everything else is verbatim.
Dictated wording: Check the piece against every tell in [<tells row IDs>] and every structure defect in [<structure-defect row IDs>], and report each occurrence at its location.

### D-3 — modify
Finding: R0038 says "the four tiers the Public Prose Criteria name".
Resolution: replace that phrase only; the rest of the body is verbatim as it stands at the reviewed ref.
Dictated wording: the four tiers [<tier row IDs>] name

## Deferred / out of scope

- Other parallel rows across writer, copy-editor, and critic — loose-end tracker, this session.
- Any step-6 observation — triaged by the decision session from your report.

## Execution notes

Edit R1013 and R0038 by replacing the body line in place; leave frontmatter byte-identical. Do not run bin/check-directive against this file if it is absent at the reviewed ref; if present, run it and report the result as an observation, not a gate.

SOURCE MANIFEST

- # heading — author region
- ROUTE AND MODEL — process/directive-invariants.md @ 2383eae
- FIRST ACT — process/directive-invariants.md @ 2383eae
- WORKING-TREE DISPOSITION — author region (form per process/directive-invariants.md @ 2383eae)
- BASE VERIFICATION — process/directive-invariants.md @ 2383eae
- COMPANIONS — process/directive-invariants.md @ 2383eae
- TASK — author region
- SANDBOX — process/directive-invariants.md @ 2383eae
- VERIFICATION — process/directive-invariants.md @ 2383eae
- STOP CONDITIONS — process/directive-invariants.md @ 2383eae
- REPORT — process/directive-invariants.md @ 2383eae, plus two author lines
- CLAIM LABELS — process/directive-invariants.md @ 2383eae
- Decisions, Deferred, Execution notes — author regions
