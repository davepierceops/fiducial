# Chief of Staff cycle 7 — agreement flips (two documents)

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/chief-of-staff-cycle-7-flips-20260903T054500Z.md, commit it alone with a
message naming the flips it lands, push with git push origin chief-of-staff-cycle-7-flips (no -u), verify by git ls-remote origin chief-of-staff-cycle-7-flips, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-chief-of-staff-cycle-7-flips", created by: git worktree add --no-track "$TMPDIR/fiducial-chief-of-staff-cycle-7-flips" -b chief-of-staff-cycle-7-flips origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch chief-of-staff-cycle-7-flips, if a branch of that name already exists locally or on origin (git ls-remote origin chief-of-staff-cycle-7-flips returns a ref), or if "$TMPDIR/fiducial-chief-of-staff-cycle-7-flips" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
171bad79fbce21c95df28a4bd116706116f6898f. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- roles/chief-of-staff.md @ 00bdd4648f8e0efdc687886b341c1ef71b259393 — first document being flipped; at the base it reads status: in-review, last-reviewed: null (told).
- context-sets/spec-and-change-discipline.md @ 0c1a51dcede20c823c4cea85796fb362cfb9f2a8 — second document being flipped; same frontmatter at the base (told).
- reviews/chief-of-staff-cycle-7.md @ 00edf6a6ac978f9f3fef6f7e1a6307832a717225 — the gate artifact, verdict ready-with-findings, reviewing both documents at the SHAs above.
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5 — the agreement flip's status-transition rule.

TASK

Two agreement flips, ruled by Dave 2026-09-02 on the cycle-7 gate verdict ready-with-findings (CS7-1 and CS7-2 ride to later cycles; the decision session records that in the flush, not you). Each flip is its own frontmatter-only commit made by the tool; run the two as sequential standalone calls, never in a loop, the role first.

Precondition, both: in the worktree, each document's frontmatter reads exactly status: in-review and last-reviewed: null. If either does not, stop and report before running anything.

Flip 1, from the worktree:

    bin/flip-agreed roles/chief-of-staff.md --review "reviews/chief-of-staff-cycle-7.md @ 00bdd4648f8e0efdc687886b341c1ef71b259393"

Flip 2, from the worktree, only after flip 1 exited 0:

    bin/flip-agreed context-sets/spec-and-change-discipline.md --review "reviews/chief-of-staff-cycle-7.md @ 0c1a51dcede20c823c4cea85796fb362cfb9f2a8"

The tool makes each commit itself and self-verifies. If either exits non-zero, stop and report its output — do not edit frontmatter by hand and do not retry. After each exits 0: git show --stat HEAD must list exactly that document with 2 insertions and 2 deletions, and git show HEAD must change only the status line (in-review → agreed) and the last-reviewed line (null → the pointer given). State both, per flip, labelled observed.

Then run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-chief-of-staff-cycle-7-flips-fm.log" and state its exit status (expected 0).

Push with git push origin chief-of-staff-cycle-7-flips (no -u) and verify by git ls-remote origin chief-of-staff-cycle-7-flips: the tip must be the flip-2 commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-chief-of-staff-cycle-7-flips" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref 171bad79fbce21c95df28a4bd116706116f6898f. Cannot execute as written: stop
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

    Chief of Staff cycle 7 — agreement flips (two documents) — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
