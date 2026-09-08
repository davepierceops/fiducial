# Bundle tool, follow-up: fixes for the read's findings

ROUTE AND MODEL

Route: fresh
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-followup-fix-20260907T200000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-followup-fix to origin with a plain push
(git push origin bundle-tool-followup-fix — never with -u), and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-followup-fix", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-followup-fix" -b bundle-tool-followup-fix origin/bundle-tool-followup

BASE VERIFICATION

Before anything else, fetch origin/bundle-tool-followup and origin/bundle-tool-followup-read and
confirm the base — the branch bundle-tool-followup, not main — is at the
reviewed ref 252928b84e19b530b9acc25159a80ab478223848, and that
origin/bundle-tool-followup-read is at 7a6f3ce5751168946eaa08d4d81c48f447f2479a. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/bundle-tool-followup-quality-20260907T190000Z.md and
  reviews/bundle-tool-followup-skeptic-20260907T190000Z.md, read from
  origin/bundle-tool-followup-read at 7a6f3ce5751168946eaa08d4d81c48f447f2479a —
  every finding's Location, Evidence and Fix; the read branch carries only
  the two artifacts and its directive over the base, and is not merged here
- docs/cycles/bundle-tool-followup-20260907T170000Z.md, read from the base
  ref 252928b84e19b530b9acc25159a80ab478223848 — item 2's ruled text for
  process/named-queries.md, which F1 restores
- bin/rulestore/named_queries.py, bin/rulestore/query.py,
  bin/rulestore/terms.py, bin/release, bin/tests/test_release.py,
  bin/tests/test_rulestore.py, bin/tests/test_bundle_cli.py,
  bin/tests/helpers.py, decisions/log.md, process/named-queries.md and
  reviews/bundle-tool-skeptic-probes-20260906T150000Z.py, read from the base
  ref 252928b84e19b530b9acc25159a80ab478223848

TASK

You are the Coder. Close the read's three blocking findings and the
non-blocking ones the human accepted, minimum change each, one commit per
finding, the suite green at every commit. Every test edit below is ruled
by this directive (DEC-000440). Do not edit anything on main; DEC-000640
is amended in place because it exists only on this branch — nothing on
main is touched.

1. F1. Restore process/named-queries.md's six fence lines to `~~~`, as item
   2 of docs/cycles/bundle-tool-followup-20260907T170000Z.md fenced them;
   change nothing else in the file. Make `_FENCE_RE` in
   bin/rulestore/named_queries.py accept a run of three or more backticks
   or three or more tildes. Add one test in bin/tests/test_rulestore.py
   that reads the real process/named-queries.md through
   `FileRowSource(repo_root).named_queries_text()` and asserts
   `sequences(...)` gives 9 topic lines and 11 stems and `bundles(...)`
   gives 12 entries — the guard against this exact failure.

2. F2, the human's ruling (2026-09-07): grouped. Replace DEC-000640's
   `Decision:` line in decisions/log.md with this one, verbatim, touching
   no other line of the entry or the log:

FENCE NOTE: the inner fence is `~~~`.

~~~markdown
Decision: A bundle renders its rows as body text, one row after another with a blank line between, under no per-row heading; then every selected process document, body only; then the definitions the rows use, under one `## Definitions` heading. Rows sort by their topic's position in the topic sequence, then by topic name, then `order`, then id — so topics sharing a position render as contiguous alphabetical runs; process documents sort by their `topic` value's position in the process sequence, the path stem standing in where the key is absent. A topic or stem the sequence does not name sorts after the last named one, alphabetically. Definitions sort by `order`, then id.
~~~

   No code change for F2.

3. S13. Widen bin/release's dirty check to `_dirty_under(root)` with no path
   arguments, so any uncommitted change under the root refuses; amend the
   refusal message and the module docstring; one test.

4. F3 — accept: pin the definitions band in bin/rulestore/terms.py to
   `(order, id)` with `None` order last, say so in its docstring, and add
   the assertion to the existing definitions test.

5. F4 — accept: one test per untested refusal in bin/tests/test_release.py,
   the skepticism pass's constructions reused; and the cleanup assertion
   that the scratch `fiducial-release-*` entries under `tempfile.gettempdir()`
   are unchanged across a run that fails after writing at least one asset.

6. F5 — accept: `TestNamedQueries` in bin/tests/test_rulestore.py, pure over
   text — missing file text (`""`), missing heading, a block with blank
   lines, a name split across two lines, a `~~~`-fenced document, a
   backtick-fenced document — and one sort test for a process row whose
   `topic` is absent against a non-empty process sequence.

7. S14 — accept the first form: bin/release reads the written path from
   bin/bundle's stdout and uses it; the glob and `matches[-1]` go. One
   test with a name carrying `[` — if bin/bundle's `--name` check rejects
   it, extend the check to `[`, `]`, `*` and `?` and assert the refusal
   instead.

8. S15 — accept: refuse, exit 2, one line naming the repeated name, when
   `bundles(...)` returns two entries with the same name, beside the
   empty-list refusal. One test.

9. The tenth refusal the read observed: an absent process/named-queries.md
   gets its own message — "no process/named-queries.md under <root>" —
   distinct from the empty-list one. One test.

10. S16 — accept: compute the four remaining static statements in
    reviews/bundle-tool-skeptic-probes-20260906T150000Z.py as its Fix
    states — probe (b) imports `names_imported_from_store` and the two
    assertions from bin/tests/test_rulestore_boundary.py; (d)'s `note()`
    is built from the observed set; (g)'s g1 conclusion and g3 section are
    built from what the run observed.

11. F6 — accept: rename the AC-RS-14 header test in
    bin/tests/test_bundle_cli.py to its `test_dec_000630_` form.

F7 is held for the human's ruling on the sequence; do nothing for it.

Commits, in order, pushed after each: the directive (FIRST ACT); then one
per numbered item, messages `bundle: <finding> — <one clause>` or, for
bin/release, `release: <finding> — <one clause>`; then the green log, re-run and
overwritten at bin/tests/green-run-rulestore-followup.log. Do not open a
pull request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-bundle-tool-followup-fix"`) and
report that it is gone. If the frontmatter hook fires, stop and report.

Report also carries: for each of F1, F2, S13 one line — closed, observed;
the diff-stat per commit; and the suite's summary line.

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
  grep -c '^~~~' process/named-queries.md
  grep -n 'FENCE_RE' bin/rulestore/named_queries.py | head -2
  sed -n '/^## DEC-000640/,/^## DEC-000650/p' decisions/log.md | grep -c 'then by topic name'
  grep -n '_dirty_under(root' bin/release | head -3
  grep -c 'glob' bin/release
  python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py > "$TMPDIR/bundle-tool-probes-followup-fix.log" 2>&1; echo "probes exit $?"
  git -C "$TMPDIR/fiducial-bundle-tool-followup-fix" diff --stat origin/bundle-tool-followup..HEAD | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-followup-fix" log --oneline origin/bundle-tool-followup..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/bundle-tool-followup-fix-verify.log"
~~~

Expected: OK from the suite; 6 tilde fence lines; a FENCE_RE accepting both
runs; 1 from the DEC-000640 grep; a dirty check with no path arguments; 0
glob; probes exit 0; a diff-stat touching bin/, decisions/log.md, process/,
reviews/ and the directive file only; 13 commits.

STOP CONDITIONS

Pinned to the reviewed ref 252928b84e19b530b9acc25159a80ab478223848. Cannot execute as written: stop
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

    Bundle tool, follow-up: fixes for the read's findings — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
