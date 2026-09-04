# PRD and TRD templates audience cycle 3 — Editor revision Directive

Date: 2026-09-03
Documents in scope:
- specs/prd-template.md @ 39b04d90e87267d260ee925ed3d5e3b3ccfd1f67
- specs/trd-template.md @ ba513f824993ab5cd1d0e9e7ce8134a93bb491c5

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/templates-audience-cycle-3-directive.md, commit it alone with a
message naming the cycle it opens, push with git push origin templates-audience-cycle-3 (no -u), verify by git ls-remote origin templates-audience-cycle-3, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-templates-audience-cycle-3", created by: git worktree add --no-track "$TMPDIR/fiducial-templates-audience-cycle-3" -b templates-audience-cycle-3 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch templates-audience-cycle-3, if a branch of that name already exists locally or on origin (git ls-remote origin templates-audience-cycle-3 returns a ref), or if "$TMPDIR/fiducial-templates-audience-cycle-3" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

This is an Editor revision opening cycle 3 for each of the two templates, not
a findings disposition. Two documents are in scope, each carrying the same
one-line defect; a Spec Reviewer gate follows in a later directive, one
artifact per document. The ruling is Dave's, 2026-08-28 (told — OPEN-ITEMS.md
@ a5c66510af7d85186217a103b29e09f1da13a52e, entry "PRD and TRD templates carry
the wrong audience — directed fix"; observation O-5 of
reviews/bundle-system-cycle-1.md records the same defect on the PRD template).
Wording is dictated.

### TA3-1 — accept (prd-template skeleton audience)
Finding: the frontmatter skeleton inside specs/prd-template.md (the fenced
block near line 98 at the reviewed ref) reads `audience: [all-roles, human]`.
A PRD copied from it literally would join every bundle; AC-BS-5 of
specs/bundle-system.md forbids a spec in the floor, and every spec in specs/
at main is audience [human].
Resolution: in that skeleton line, and nowhere else in the file, replace the
value. Read the whole document once for any prose that states or presupposes
the old default (Core 13) and report what you find; do not edit prose unless
it states the value.
Dictated wording: audience: [human]

### TA3-2 — accept (trd-template skeleton audience)
Finding: the frontmatter skeleton inside specs/trd-template.md (the fenced
block near line 137 at the reviewed ref) reads `audience: [all-roles, human]`.
Same defect, same ruling.
Resolution: as TA3-1, in specs/trd-template.md.
Dictated wording: audience: [human]

## Deferred / out of scope

- The Spec Reviewer gate over each revised template — a later directive from
  the decision session; artifacts reviews/prd-template-cycle-3.md and
  reviews/trd-template-cycle-3.md, one per document.
- The two templates' own top-level frontmatter audience values are not in
  scope; they are correct as they stand. Do not edit them.
- specs/bundle-system.md — read for AC-BS-5 only; do not edit it.

## Execution notes

- Two content commits after the directive's own commit: one touching
  specs/prd-template.md only, then one touching specs/trd-template.md only.
  Each commit flips that document to status: in-review and last-reviewed:
  null; the pre-commit hook does this — never bypass it.
- Nothing else in either file changes. The Lexicon touch rule applies; if it
  would require a further edit, stop and report rather than make it.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin templates-audience-cycle-3 — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-templates-audience-cycle-3"
  (no --force). If it fails, report the failure; do not retry. Your report's
  final line states whether the worktree was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
ff0632c344e81b994698abb75a9e54021182ef18. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- specs/prd-template.md @ 39b04d90e87267d260ee925ed3d5e3b3ccfd1f67
- specs/trd-template.md @ ba513f824993ab5cd1d0e9e7ce8134a93bb491c5
- specs/bundle-system.md @ 4d6373a6d73e44023fdc86961e1d49a36eb0b342 — AC-BS-5 only.
- OPEN-ITEMS.md @ a5c66510af7d85186217a103b29e09f1da13a52e — the entry "PRD and TRD templates carry the wrong audience — directed fix" only.
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5 — revision lifecycle.
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41 — the touch rule.

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
   "$TMPDIR/fiducial-templates-audience-cycle-3-frontmatter.log", exit status
   reported (expected 0).
2. grep -n "all-roles" specs/prd-template.md specs/trd-template.md in the
   worktree, output captured to
   "$TMPDIR/fiducial-templates-audience-cycle-3-grep.log"; expected zero
   matches; state the count, labelled observed.
3. git diff --stat of each content commit: exactly one file each; state both,
   labelled observed. Expected per file: the skeleton line, the status line,
   and the last-reviewed line change — three lines changed, no more.
4. head -5 of each template in the worktree: status in-review, last-reviewed
   null, top-level audience unchanged; state each, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref ff0632c344e81b994698abb75a9e54021182ef18. Cannot execute as written: stop
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

    PRD and TRD templates audience cycle 3 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
