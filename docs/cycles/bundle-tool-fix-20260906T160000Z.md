# Bundle tool, fix: the four blocking findings from the two-pass review

ROUTE AND MODEL

Route: fresh
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-fix-20260906T160000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-fix to origin with a plain
`git push origin bundle-tool-fix`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-fix", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-fix" -b bundle-tool-fix origin/bundle-tool-review

BASE VERIFICATION

Before anything else, fetch origin/bundle-tool-review and origin/main and confirm the base — the
branch bundle-tool-review, not main — is at the reviewed ref
b73635df0097d48447118dab7b826e9a24880c83, and that origin/main is at
a5d60506d1d1266d8685f498662f514d49e12136, the branch's merge base. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/bundle-tool-quality-20260906T150000Z.md,
  reviews/bundle-tool-skeptic-20260906T150000Z.md and
  reviews/bundle-tool-skeptic-probes-20260906T150000Z.py, read from the base
  ref b73635df0097d48447118dab7b826e9a24880c83 — the findings you fix, with each one's
  Location, Consequence and Fix; run the probe script before and after
- docs/cycles/bundle-tool-tests-20260906T110000Z.md, read from the base ref
  b73635df0097d48447118dab7b826e9a24880c83 — the interface contract; unchanged except where item 2
  says
- bin/rulestore/ (every file), bin/bundle, bin/tests/test_rulestore.py,
  bin/tests/test_bundle_cli.py, bin/tests/test_cross_cutting.py and
  bin/tests/helpers.py, read from the base ref b73635df0097d48447118dab7b826e9a24880c83

TASK

You are the Coder. Fix the four blocking findings the two-pass review
raised, nothing else; every non-blocking finding stays in the artifacts for
a later package. Each fix is one commit whose message names the finding.
Minimum change; the suite stays green; no test file changes except the one
item 2 rules.

1. Q1 — terms across a line break. In `terms.py`, build each term's pattern
   from the term's words joined by `\s+` (whole-word, case-insensitive),
   so a phrase wrapped across a line in a body still matches. Confirm with
   the probe script's (d) case, and confirm on the real store that
   process/change-flow.md pulls R0004, retro pulls R0208, and
   spec-test-suite pulls R0055 (the review names these three as lost today).

2. Q2 — `--keys` censuses rules and process documents together (Dave's
   ruling, 2026-09-06, under DEC-000440). In `bin/bundle` drop the
   `kind == "rule"` filter on the `--keys` census. In
   `bin/tests/test_bundle_cli.py` amend the one expected count the review
   names (`role=writer 2` becomes `3`) and its docstring to say the census
   covers both kinds; touch no other assertion. This is the only test edit
   in this package.

3. Q3 — a malformed row. In `bin/bundle`, catch `RowShapeError` at every
   `FileRowSource(...).rows()` call and refuse: exit 2, one line on stderr
   naming the row id and the key, nothing written, no traceback. Add no
   test; the store fixture test for RowShapeError already exists, and the
   CLI behaviour is confirmed by the probe script's (f) case.

4. S1 — outside a repository. In `bin/bundle`, `_repo_root` (or its
   equivalent) refuses when the working directory is not inside a git
   repository: exit 2, one line on stderr, for every mode including
   `--keys` and `--near`. In `bin/tests/test_cross_cutting.py`, set
   `CLI_MINIMAL_ARGS["bundle"]` to `["--keys"]` so AC-X-4, X-6 and X-7 reach
   the tool again; this is a fixture-argument correction the review names
   and is not a change to any assertion.

Then run the whole suite (`bin/tests/run`), capture to
`bin/tests/green-run-rulestore-fix.log`, commit it; run the probe script
and capture its output to `$TMPDIR/bundle-tool-probes-after.log`; report
(b) through (f) as they now read — (b), (e) and the three untested shapes
in (f) other than the malformed row are expected to still read as the
review left them, since they are non-blocking and out of scope.

Commits, in order, pushed after each: the directive (FIRST ACT); Q1; Q2;
Q3; S1; the green log. Commit messages `bundle: fix <finding> — <one
clause>`. Do not open a pull request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-bundle-tool-fix"`) and report that
it is gone. bin/ is outside the frontmatter hook's in-scope set; if the hook
fires, stop and report.

Report also carries: the diff-stat per fix; the three real-store definition
pulls from item 1, observed; and the standard response shape as its own
labelled section.

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
  bin/tests/run 2>&1 | tail -1
  grep -c 'role=writer 3' bin/tests/test_bundle_cli.py
  grep -n 'CLI_MINIMAL_ARGS' bin/tests/test_cross_cutting.py | head -3
  ( cd /tmp && "$OLDPWD/bin/bundle" --keys >/dev/null 2>&1; echo "outside-repo exit $?" )
  bin/bundle --keys | wc -l
  python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py 2>&1 | grep -E '^\((b|c|d|e|f)\)|PASS|FAIL' | head -12
  git -C "$TMPDIR/fiducial-bundle-tool-fix" diff --stat origin/bundle-tool-review..HEAD | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-fix" log --oneline origin/bundle-tool-review..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/bundle-tool-fix-verify.log"
~~~

Expected: OK from the suite; 1; the CLI_MINIMAL_ARGS line showing
["--keys"] for bundle; outside-repo exit 2; a keys count above 862; the
probe lines with (c) and (d) passing; a diff-stat touching bin/rulestore/,
bin/bundle, bin/tests/, and the directive file only; 6 commits.

STOP CONDITIONS

Pinned to the reviewed ref b73635df0097d48447118dab7b826e9a24880c83. Cannot execute as written: stop
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

    Bundle tool, fix: the four blocking findings from the two-pass review — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
