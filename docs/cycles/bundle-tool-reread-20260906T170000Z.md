# Bundle tool, re-read: diff-scoped quality and skepticism passes over the four fixes

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-reread-20260906T170000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-reread to origin with a plain
`git push origin bundle-tool-reread`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-reread", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-reread" -b bundle-tool-reread origin/bundle-tool-fix

BASE VERIFICATION

Before anything else, fetch origin/bundle-tool-fix and origin/main and confirm the base — the
branch bundle-tool-fix, not main — is at the reviewed ref
a72d9c31ed5e68809f67b965f6ceb12177b6badc, and that origin/main is at
a5d60506d1d1266d8685f498662f514d49e12136, the branch's merge base. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/bundle-tool-quality-20260906T150000Z.md and
  reviews/bundle-tool-skeptic-20260906T150000Z.md, read from the base ref
  a72d9c31ed5e68809f67b965f6ceb12177b6badc — the four blocking findings (Q1, Q2, Q3, S1) whose
  closure you judge, and the non-blocking ones you leave alone
- reviews/bundle-tool-skeptic-probes-20260906T150000Z.py, read from the base
  ref a72d9c31ed5e68809f67b965f6ceb12177b6badc — run it before judging
- docs/cycles/bundle-tool-fix-20260906T160000Z.md, read from the base ref
  a72d9c31ed5e68809f67b965f6ceb12177b6badc — what the Coder was told
- the diff origin/bundle-tool-review..origin/bundle-tool-fix
  (b73635df0097d48447118dab7b826e9a24880c83..a72d9c31ed5e68809f67b965f6ceb12177b6badc) — the change under
  review, 6 files, and nothing outside it

TASK

A diff-scoped re-read, not a second full read: review only the diff from
b73635df0097d48447118dab7b826e9a24880c83 to the base ref — the four fixes —
in two passes, each its own artifact with its own verdict. The question for
each pass is narrow: does each of Q1, Q2, Q3, S1 close as its Fix stated,
and does the fix introduce anything the first read would have flagged? Do
not re-open the non-blocking findings; do not review files outside the
diff; do not edit anything under bin/.

PASS 1 — QUALITY. For each of the four: the finding's Fix, what the diff
did, closed or not, and why. Note that the Coder placed the
`CLI_MINIMAL_ARGS["bundle"]` override in test_cross_cutting.py because the
fix directive misnamed the file; judge whether that placement is a defect
in the fix or a follow-up, and say which. Run the suite and cite its
summary line. Artifact: reviews/bundle-tool-quality-reread-20260906T170000Z.md.

PASS 2 — SKEPTICISM. Re-run the probe script; then for Q1 construct the
line-wrapped phrase case yourself and confirm pull_definitions returns the
definition; for Q3 construct the `order: twenty` row in a temp repo and
confirm each mode's exit code and stderr; for S1 run every mode from a
directory outside any repository. Report what you observed, not what the
Coder reported. Artifact: reviews/bundle-tool-skeptic-reread-20260906T170000Z.md.

Both artifacts follow process/review-artifact.md, scoped to the diff, with
a Verdict per pass; the overall verdict is the more severe. If a finding is
not closed, it is blocking and its Fix is stated. Commits, in order, pushed
after each: the directive (FIRST ACT); the quality artifact; the skeptic
artifact. Nothing else. Do not open a pull request. Remove the worktree at
the end (`git worktree remove "$TMPDIR/fiducial-bundle-tool-reread"`) and
report that it is gone. reviews/ is outside the frontmatter hook's in-scope
set; if the hook fires, stop and report.

Report also carries: both verdicts and the overall, and for each of Q1, Q2,
Q3, S1 one line — closed or not, observed.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the last commit and before removing the worktree:

~~~sh
{
  ls reviews/bundle-tool-*reread*
  grep -h '^Verdict' reviews/bundle-tool-quality-reread-20260906T170000Z.md reviews/bundle-tool-skeptic-reread-20260906T170000Z.md
  bin/tests/run 2>&1 | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-reread" diff --stat origin/bundle-tool-fix..HEAD | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-reread" log --oneline origin/bundle-tool-fix..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/bundle-tool-reread-verify.log"
~~~

Expected: two files; the verdict lines; OK from the suite; a diff-stat
touching reviews/ and the directive file only; 3 commits.

STOP CONDITIONS

Pinned to the reviewed ref a72d9c31ed5e68809f67b965f6ceb12177b6badc. Cannot execute as written: stop
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

    Bundle tool, re-read: diff-scoped quality and skepticism passes over the four fixes — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
