# Bundle tool, tests: the rule-store query tool's test suite, confirmed red

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-tests-20260906T110000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-tests to origin with a plain
`git push origin bundle-tool-tests`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-tests", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-tests" -b bundle-tool-tests origin/main

BASE VERIFICATION

Before anything else, fetch origin/main and confirm the base is at the reviewed ref
a5d60506d1d1266d8685f498662f514d49e12136. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- bin/bundle @ 70b58bad02bf7caccc6ac6a8eb8bcc0ba2d4014c — the tool being
  replaced; read for the header format and the sync refusal it already
  implements, nothing else carries forward
- bin/tests/helpers.py and bin/tests/run, read from the base ref
  a5d60506d1d1266d8685f498662f514d49e12136 — the fixture conventions this suite reuses: real git in a
  temp directory, isolated environment, stdlib only
- bin/tests/test_bundle_audience.py, read from the base ref
  a5d60506d1d1266d8685f498662f514d49e12136 — the suite this one replaces; its shape, not its assertions
- rules/R0264.md, rules/R0456.md, rules/R0030.md and ten more rows of your
  choosing, read from the base ref a5d60506d1d1266d8685f498662f514d49e12136 — the row shape as it is on
  disk; note the 78 definition rows that carry `term` and no role, session,
  or corpus
- every file under process/, read from the base ref a5d60506d1d1266d8685f498662f514d49e12136 — the
  process documents' frontmatter keys, which the same query selects
- decisions/log.md @ a00deba150c0736f77562ec80d858c3986cd7f11 — DEC-000400
  (the row), DEC-000410 (the storage boundary), DEC-000420 (definitions by
  term), DEC-000490 (process documents selected by key)

TASK

You are the Test Designer for the rule-store bundle tool. Write the test
suite, confirm it red against a deliberately wrong stub, and land it. Write
no production code beyond the stub the red-gate needs; the Coder is a
separate session that receives your suite as its spec. The PRD this derives
from is not on main; its acceptance criteria are stated here in full and are
the contract, prefixed AC-RS- as in the PRD.

INTERFACE CONTRACT — the Coder builds to this; test against it.

Package `bin/rulestore/` (stdlib only, Python 3.12), with:

- `store.py` — the storage boundary (DEC-000410). `Row` is a dataclass:
  `id: str`, `body: str` (the agent form, everything above `## Human`,
  stripped), `human: str | None` (the `## Human` section, stripped, or None),
  `keys: dict[str, list[str]]` (every frontmatter key except `id`, values as
  lists of normalized words; `order` excluded), `order: int | None`,
  `kind: str` ("rule" or "process"), `path: str | None` (repo-relative, for
  the header), `blob: str | None` (the git blob SHA of the file at HEAD, for
  the header). `RowSource` is a Protocol with one method, `rows() -> list[Row]`.
  `FileRowSource(root: pathlib.Path)` reads every `rules/*.md` as kind
  "rule" and every `process/*.md` as kind "process"; nothing under
  `rules/retired/` is returned. `MemoryRowSource(rows)` returns what it was
  given. Normalization: a value is a list; a bare word is a list of one;
  `[a, b]` splits on commas; every element is stripped and lower-cased;
  `null` and an empty list are an absent key. `order` parses to int; any
  other typed value (a quoted number on another key is text) is a defect
  the source raises `RowShapeError` for, naming the id and the key.
- `query.py` — `parse_where(args: list[str]) -> dict[str, str]` from
  `k=v` tokens; a token with no `=`, an empty key, or an empty value raises
  `QueryError`. `select(rows, where) -> list[Row]`: a row matches when,
  for every named key, the row has the key and its list contains the value;
  a missing key is a non-match. Result ordered by `order` (None sorts after
  every integer), then by the first `topic` value (process rows sort by
  their path stem), then by `id`.
- `terms.py` — `pull_definitions(selected, all_rows) -> list[Row]` (DEC-000420):
  a definition is a row with a `term` key and no `role` key. Scan every
  selected row's body for any definition's term (whole-word, case-insensitive,
  each term a phrase); add matched definitions; scan the added definitions'
  bodies the same way until no new definition is added. Definitions already
  in the selection are not added twice. Returned in the same order rule as
  select.
- `keys.py` — `keys_in_use(rows) -> dict[str, dict[str, int]]`: every key
  with every value and the count of rows carrying it, computed from the rows
  given; `id` and `order` excluded.
- `near.py` — `near(text, rows, threshold=0.3) -> list[tuple[Row, float]]`:
  normalize (lower-case, strip punctuation, split on whitespace, drop words
  of two letters or fewer), score each row's body by Jaccard similarity of
  word sets against the text, return rows scoring at or above threshold,
  highest first.
- `render.py` — `render(rows, definitions, *, repo, head, generated) -> str`.
  Header first: `# fiducial-bundle`, then `- Repo:`, `- HEAD:` (full SHA),
  `- Generated:` (ISO 8601 basic, UTC, with Z), `- Rows:` then one line per
  row, `  - <id> (<blob>)` for rules, `  - <path> (<blob>)` for process
  documents, in bundle order, definitions listed after the selected rows
  under `- Definitions:`. Then the rows in order, each as
  `## <id>` followed by the body, a blank line between; a process document
  renders as its body under `## <path>`; definitions render last under
  `## Definitions`, each as `**<first term>** — <body>`. No `## Human`
  content anywhere in the output. Nothing else.
- `bin/bundle` — the command. `bin/bundle --where k=v [k=v ...] [--name
  <name>] [--out <dir>]`; `bin/bundle --keys`; `bin/bundle --near "<text>"`.
  With `--where`: refuse (exit 2, one line on stderr, nothing written) when
  the query is malformed, when the working tree has uncommitted changes to
  rules/ or process/, or when HEAD is not equal to origin/main after a
  fetch; otherwise write exactly one file to `<out>` (default `~/Downloads`)
  named `fiducial-bundle-<name>-<timestamp>Z.md`, where `<name>` defaults to
  the query's key-value pairs joined `k-v` with `-`, and print its path on
  stdout, exit 0. An empty selection is refused (exit 2), not written.
  `--keys` prints one line per key-value, `<key>=<value> <count>`, sorted by
  key then value, exit 0; needs no sync. `--near` prints one line per row,
  `<id> <score to two places>`, exit 0; needs no sync.

ACCEPTANCE CRITERIA — every test names the AC it asserts, in its docstring.

- AC-RS-1 Row shape. Every file under rules/ parses to id, a non-empty body,
  and a dictionary; every value is a list of words after normalization;
  order is an integer where present; any other typed value is a defect.
- AC-RS-2 Query. --where k=v [k=v ...] returns exactly the rows where every
  named key contains the value; a missing key is a non-match; the result is
  ordered by order, then topic, then id.
- AC-RS-3 Keys computed. --keys lists every key in use with its values and
  counts, computed from the store at invocation; no key list exists anywhere
  else in the tool.
- AC-RS-4 Storage boundary. The processing modules (query, terms, keys,
  near, render) import nothing from store.py but the Row type and the
  RowSource protocol; only store.py names rules/ or process/, reads a
  directory, parses frontmatter, or opens a file; every processing test
  constructs rows in memory via MemoryRowSource and passes without touching
  the filesystem.
- AC-RS-5 Near. --near returns the rows whose normalized body scores at or
  above threshold against the text, highest first.
- AC-RS-6 One command, header, refusal. One file, the ruled name and
  directory, the header fields, non-zero exit with a reason on an unsynced
  tree or a malformed query, nothing written.
- AC-RS-13 Definitions by term (DEC-000420). A selected row whose body uses
  a definition's term pulls that definition; a pulled definition's body pulls
  further definitions, transitively; a definition is never included twice;
  a definition's role-less shape excludes it from ordinary selection by
  role.
- AC-RS-14 Two forms, one row (G4). The ## Human section never appears in
  rendered output; it is present on the Row object.
- AC-RS-15 Process documents (DEC-000490). A process/ file is selected by
  the same query, interleaved with rules by order, rendered under its path.

WHAT TO WRITE

1. `bin/tests/test_rulestore.py` — the processing tests, in-memory rows only,
   one test class per module, at least: shape and normalization (AC-RS-1,
   including the defect case); select with single and multiple keys, the
   missing-key non-match, and the full ordering rule with None order
   (AC-RS-2); keys_in_use counts (AC-RS-3); pull_definitions with a direct
   pull, a transitive pull, a phrase term, a no-duplicate case, and the
   role-less exclusion (AC-RS-13); near with a threshold boundary case and
   ordering (AC-RS-5); render header lines, row order, process rendering,
   definitions last, and no Human content (AC-RS-14, AC-RS-15).
2. `bin/tests/test_bundle_cli.py` — the command, run as a subprocess against
   a real git repository built in a temp directory per the helpers'
   conventions: a bare "origin" plus a clone with three rules, one
   definition, one process file, and one retired row; assert the file
   written, its name, its header, the stdout path (AC-RS-6); assert refusal
   with nothing written for a malformed query, a dirty rules/ tree, a HEAD
   behind origin/main, and an empty selection (AC-RS-6); assert --keys and
   --near output shape (AC-RS-3, AC-RS-5) with no sync required (run them
   on the dirty tree).
3. `bin/tests/test_rulestore_boundary.py` — AC-RS-4 as a static check: read
   the source of every processing module and assert none imports os,
   pathlib, glob, io, or subprocess, and none contains the strings "rules/"
   or "process/"; assert store.py is the only module that does.
4. `bin/tests/test_rulestore_store.py` — FileRowSource against the temp
   repository: the retired row absent, kinds correct, blob equal to
   `git rev-parse HEAD:<path>`, and RowShapeError on a row whose `order`
   reads `twenty`.

THE RED-GATE. Write `bin/rulestore/` as a stub package whose every function
exists with the right signature and returns deliberately wrong values — the
wrong order, an extra row, the Human text in the render, a definition
included twice — and `bin/bundle` as a stub that exits 0 and writes a file
with a wrong name. Run the suite with `bin/tests/run` and capture the output
to `bin/tests/red-run-rulestore.log`. Every test must fail on an assertion,
not on an import or an attribute error; a test that fails for any other
reason is rewritten until it fails on its assertion. Commit the log with the
suite. Leave the stub in place: the Coder replaces it.

Do not touch bin/aimeta, the old bin/bundle, or test_bundle_audience.py;
their removal is the Coder's package.

Commits, in order, pushed after each: the directive (FIRST ACT); the
interface stub; the four test files; the red-run log. Do not open a pull
request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-bundle-tool-tests"`) and report that
it is gone. bin/ is outside the frontmatter hook's in-scope set; if the hook
fires, stop and report.

Report also carries: the test count per file; the count of tests failing on
assertion (must equal the total); any AC you could not write a test for and
why; and any place where the interface contract above was ambiguous enough
that you had to choose, with the choice you made.

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
  ls bin/rulestore/*.py bin/tests/test_rulestore*.py bin/tests/test_bundle_cli.py
  grep -c 'def test_' bin/tests/test_rulestore.py bin/tests/test_bundle_cli.py bin/tests/test_rulestore_boundary.py bin/tests/test_rulestore_store.py
  bin/tests/run -p 'test_rulestore*.py' 2>&1 | tail -3
  bin/tests/run -p 'test_bundle_cli.py' 2>&1 | tail -3
  grep -c 'AssertionError' bin/tests/red-run-rulestore.log
  grep -cE 'ImportError|AttributeError|ModuleNotFoundError' bin/tests/red-run-rulestore.log
  git -C "$TMPDIR/fiducial-bundle-tool-tests" log --oneline origin/main..HEAD | wc -l
  git -C "$TMPDIR/fiducial-bundle-tool-tests" diff --stat origin/main..HEAD | tail -1
} 2>&1 | tee "$TMPDIR/bundle-tool-tests-verify.log"
~~~

Expected: the stub and four test files listed; the test counts; two FAILED
summaries whose failure count equals the test count; an AssertionError count
equal to the test count; zero import or attribute errors; 4 commits; a
diff-stat touching bin/rulestore/, bin/tests/, and
the directive file only.

STOP CONDITIONS

Pinned to the reviewed ref a5d60506d1d1266d8685f498662f514d49e12136. Cannot execute as written: stop
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

    Bundle tool, tests: the rule-store query tool's test suite, confirmed red — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
