# Bundle tool, review: quality pass and skepticism pass over the rule-store tool

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-review-20260906T150000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-review to origin with a plain
`git push origin bundle-tool-review`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-review", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-review" -b bundle-tool-review origin/bundle-tool-coder

BASE VERIFICATION

Before anything else, fetch origin/bundle-tool-coder and origin/main and confirm the base — the
branch bundle-tool-coder, not main — is at the reviewed ref
70bfd12d5dc25d1386252f63c6d1fa890ce919f1, and that origin/main is at
a5d60506d1d1266d8685f498662f514d49e12136, the branch's merge base. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/cycles/bundle-tool-tests-20260906T110000Z.md and
  docs/cycles/bundle-tool-coder-20260906T130000Z.md, read from the base ref
  70bfd12d5dc25d1386252f63c6d1fa890ce919f1 — the interface contract, the acceptance
  criteria, and what each session was told to do
- bin/rulestore/ (every file), bin/bundle, bin/tests/test_rulestore.py,
  bin/tests/test_bundle_cli.py, bin/tests/test_rulestore_store.py,
  bin/tests/test_rulestore_boundary.py, bin/tests/helpers.py,
  bin/tests/red-run-rulestore.log, bin/tests/green-run-rulestore.log, read
  from the base ref 70bfd12d5dc25d1386252f63c6d1fa890ce919f1 — the change under review
- process/review-artifact.md, read from the base ref 70bfd12d5dc25d1386252f63c6d1fa890ce919f1 — the
  form your two artifacts take
- every row in the store keyed reviewer-agent or skeptic-risk-agent, read
  from the base ref 70bfd12d5dc25d1386252f63c6d1fa890ce919f1 — find them with
  `grep -l 'reviewer-agent' rules/*.md` and `grep -l 'skeptic-risk-agent'
  rules/*.md`; they are your obligations for each pass
- decisions/log.md @ a00deba150c0736f77562ec80d858c3986cd7f11 — DEC-000410
  (the storage boundary), DEC-000420 (definitions by term), DEC-000460
  (every PR gets this review; two passes always)

TASK

Review the bundle-tool change — the diff from origin/main
(a5d60506d1d1266d8685f498662f514d49e12136) to the base ref — in two passes,
each its own artifact, each with its own verdict, under DEC-000460. You
neither wrote the tests nor the code; you gate both. Do not edit any file
under bin/; findings go in the artifacts, and fixes are a later session's.

PASS 1 — QUALITY, as the Reviewer. Over the diff and the green log:
correctness against the interface contract and the ACs; maintainability;
consistency with the existing bin/ conventions (helpers, stdlib-only,
real-git fixtures); test adequacy — does the suite actually constrain the
behaviour the contract states, or does it pass on a weaker one; and every
place the Coder's report says the tests "left room" (the --keys census
excluding process rows, the refusal-check ordering, the repo label from
remote.origin.url, the importlib load, the process row's id as path stem).
Run the suite yourself (`bin/tests/run`) and cite its summary line. Artifact:
reviews/bundle-tool-quality-20260906T150000Z.md.

PASS 2 — SKEPTICISM, as the Skeptic/Risk agent, over the whole evidence
chain — directives, red log, green log, code, and the Coder's report. Where
is this lying to us? At minimum, test each of these and state what you found:
(a) the red-gate — pick five tests and confirm from the red log that each
failed on its own assertion against the stub, not on scaffolding; (b) the
storage boundary — is AC-RS-4 actually enforced or only asserted by a string
scan a rename would defeat; (c) the sync refusal — build a temp repo, put HEAD
one commit ahead of origin/main, one behind, and equal-but-dirty, and observe
what --where does in each; (d) definitions by term — construct a row whose
body contains a term as part of a longer word, and one whose term is a phrase
crossing a line break, and observe pull_definitions; (e) the header — is
every blob the blob at HEAD, or the blob of the working-tree file; (f)
anything the tests never touch: a rules/ file with no frontmatter, a value
containing a comma inside quotes, a `## Human` heading at a different level,
an id collision between a rule and a process stem. Every probe you run goes in
a script committed beside the artifact,
reviews/bundle-tool-skeptic-probes-20260906T150000Z.py, so the next reader can
re-run it. Artifact: reviews/bundle-tool-skeptic-20260906T150000Z.md.

Both artifacts follow process/review-artifact.md: header block, Scope,
Cross-checked, Not inspected, findings each marked blocking or non-blocking
with Location, Consequence, and Fix, Dave should inspect, Verdict — ready,
ready-with-findings, or changes-required. A clean pass says so in the header.
The overall verdict is the more severe of the two.

Commits, in order, pushed after each: the directive (FIRST ACT); the quality
artifact; the probe script; the skeptic artifact. Nothing else changes. Do
not open a pull request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-bundle-tool-review"`) and report that
it is gone. reviews/ is outside the frontmatter hook's in-scope set; if the
hook fires, stop and report.

Report also carries: both verdicts and the overall; every blocking finding in
one line each with its Fix; the count of non-blocking findings per pass; and
the probe results for (a) through (f) in one line each.

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
  ls reviews/bundle-tool-*
  grep -h '^Verdict' reviews/bundle-tool-quality-20260906T150000Z.md reviews/bundle-tool-skeptic-20260906T150000Z.md
  grep -c 'blocking' reviews/bundle-tool-quality-20260906T150000Z.md reviews/bundle-tool-skeptic-20260906T150000Z.md
  python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py 2>&1 | tail -8
  bin/tests/run 2>&1 | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-review" diff --stat origin/bundle-tool-coder..HEAD | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-review" log --oneline origin/bundle-tool-coder..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/bundle-tool-review-verify.log"
~~~

Expected: three files under reviews/; two Verdict lines; the blocking counts;
the probe script's summary; OK from the suite, unchanged; a diff-stat touching
reviews/ and the directive file only; 4 commits.

STOP CONDITIONS

Pinned to the reviewed ref 70bfd12d5dc25d1386252f63c6d1fa890ce919f1. Cannot execute as written: stop
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

    Bundle tool, review: quality pass and skepticism pass over the rule-store tool — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
