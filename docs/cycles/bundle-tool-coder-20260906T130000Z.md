# Bundle tool, coder: implement bin/rulestore and bin/bundle to green

ROUTE AND MODEL

Route: fresh
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-coder-20260906T130000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-coder to origin with a plain
`git push origin bundle-tool-coder`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-coder", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-coder" -b bundle-tool-coder origin/bundle-tool-tests

BASE VERIFICATION

Before anything else, fetch origin/bundle-tool-tests and origin/main and confirm the base — the
branch bundle-tool-tests, not main — is at the reviewed ref
ad89e6f482dee18a6538b53eb9b346c725bf7a96, and that origin/main is at
a5d60506d1d1266d8685f498662f514d49e12136, the branch's merge base. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/cycles/bundle-tool-tests-20260906T110000Z.md, read from the base ref
  ad89e6f482dee18a6538b53eb9b346c725bf7a96 — the Test Designer's directive: its INTERFACE
  CONTRACT and ACCEPTANCE CRITERIA are your spec, read whole
- bin/tests/test_rulestore.py, bin/tests/test_bundle_cli.py,
  bin/tests/test_rulestore_store.py, bin/tests/test_rulestore_boundary.py
  and bin/tests/helpers.py, read from the base ref ad89e6f482dee18a6538b53eb9b346c725bf7a96 —
  the 86 tests you turn green, and the fixtures they run against
- bin/rulestore/ (every file) and bin/tests/stubs/bundle, read from the base
  ref ad89e6f482dee18a6538b53eb9b346c725bf7a96 — the deliberately wrong stub you replace
- bin/tests/red-run-rulestore.log, read from the base ref ad89e6f482dee18a6538b53eb9b346c725bf7a96 —
  the confirmed red run: 86 failures, every one an assertion
- bin/bundle @ 70b58bad02bf7caccc6ac6a8eb8bcc0ba2d4014c — the old tool you
  replace; its header lines are the only thing to carry forward
- rules/R0264.md and every file under process/, read from the base ref
  ad89e6f482dee18a6538b53eb9b346c725bf7a96 — real rows and process files, for a manual run
  after green

TASK

You are the Coder for the rule-store bundle tool. Turn the 86 confirmed-red
tests green with the minimum implementation, replacing the stub the Test
Designer left. The tests are the spec: where the test suite and the
interface contract disagree, the test wins, and you report the
disagreement; do not edit any test file or helpers.py — a test you believe
is wrong is a finding in your report, not an edit (DEC-000440).

1. Implement `bin/rulestore/` for real: `store.py` (Row, RowSource,
   FileRowSource, MemoryRowSource, RowShapeError, normalize_fields),
   `query.py`, `terms.py`, `keys.py`, `near.py`, `render.py`. Delete
   `bin/rulestore/legacy.py`. Stdlib only; Python 3.12. The storage boundary
   holds: only `store.py` names `rules/` or `process/`, reads a directory,
   parses frontmatter, or opens a file; the boundary tests assert this
   statically. `store.py` may reuse `bin/aimeta/frontmatter.py` for the
   YAML-subset parse if it fits; if it does not, write the parse in
   `store.py` — do not modify aimeta.

2. Replace `bin/bundle` with the new command — `--where`, `--keys`,
   `--near`, `--name`, `--out` — exactly as the contract and
   `test_bundle_cli.py` state, including the sync refusal (fetch, HEAD
   equals origin/main, no uncommitted changes under rules/ or process/) and
   the exit codes. Executable bit set. Delete `bin/tests/stubs/bundle`.

3. Delete `bin/tests/test_bundle_audience.py` and its red-run logs if any
   name it; the audience mechanism it tested no longer exists. Touch nothing
   else under bin/tests/ and nothing under bin/aimeta/. The other lifecycle
   tools (check-frontmatter, flip-agreed, install-hooks,
   migrate-frontmatter) stay for now; their removal is a later package.

4. Run the whole suite (`bin/tests/run`) and capture to
   `bin/tests/green-run-rulestore.log`; commit it. Every test in the four
   new files passes; nothing elsewhere in the suite regresses from the
   Test Designer's regression baseline (697 tests, 86 failures, all in the
   new suite — so the target is 697 minus the audience suite's count, zero
   failures).

5. A manual run against the real store, from the worktree, output captured
   to `$TMPDIR/bundle-tool-manual.log`: `bin/bundle --keys`;
   `bin/bundle --near "read governed text before emitting anything it
   governs"`; `bin/bundle --where role=chief-of-staff session=decision
   --out "$TMPDIR"`. Report the keys count, the top three --near hits, and
   the written bundle's row count, definitions count, and size. The
   `--where` run will be refused if the worktree's HEAD is not origin/main
   — it will not be, since this branch is ahead — so for this one run only,
   set the environment variable the CLI reads for its sync check, if the
   contract or the tests provide one; if they do not, report the refusal as
   the observed result and do not work around it.

Commits, in order, pushed after each: the directive (FIRST ACT); store.py;
the five processing modules; bin/bundle and the stub deletion; the audience
suite deletion; the green log. Commit messages `bundle: <one clause>`. Do
not open a pull request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-bundle-tool-coder"`) and report that
it is gone. bin/ is outside the frontmatter hook's in-scope set; if the hook
fires, stop and report.

Report also carries: every test-vs-contract disagreement you met and how the
test resolved it; every place the minimum implementation needed a choice the
tests do not constrain, with the choice; the manual-run figures; and, as its
own labelled section, the standard response shape — role, intent, evidence,
boundary, gaps, recommendation, Dave decision points.

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
  ls bin/rulestore/ bin/tests/stubs/
  test -e bin/rulestore/legacy.py && echo LEGACY-PRESENT || echo legacy-gone
  test -e bin/tests/test_bundle_audience.py && echo AUDIENCE-PRESENT || echo audience-gone
  test -x bin/bundle && echo bundle-executable || echo BUNDLE-NOT-EXECUTABLE
  bin/tests/run 2>&1 | tail -3
  bin/tests/run -p 'test_rulestore*.py' 2>&1 | tail -1
  bin/tests/run -p 'test_bundle_cli.py' 2>&1 | tail -1
  grep -cE 'import (os|pathlib|glob|io|subprocess)|from (os|pathlib|glob|io|subprocess)' bin/rulestore/query.py bin/rulestore/terms.py bin/rulestore/keys.py bin/rulestore/near.py bin/rulestore/render.py
  bin/bundle --keys | wc -l
  git -C "$TMPDIR/fiducial-bundle-tool-coder" log --oneline origin/bundle-tool-tests..HEAD | wc -l
  git -C "$TMPDIR/fiducial-bundle-tool-coder" diff --stat origin/bundle-tool-tests..HEAD | tail -1
} 2>&1 | tee "$TMPDIR/bundle-tool-coder-verify.log"
~~~

Expected: the package listing without legacy.py and the stubs listing without
bundle; legacy-gone; audience-gone; bundle-executable; an OK summary for the
whole suite; OK for both patterns; five zeros; the keys line count; 6
commits; a diff-stat touching bin/rulestore/, bin/bundle, bin/tests/, and
the directive file only.

STOP CONDITIONS

Pinned to the reviewed ref ad89e6f482dee18a6538b53eb9b346c725bf7a96. Cannot execute as written: stop
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

    Bundle tool, coder: implement bin/rulestore and bin/bundle to green — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
