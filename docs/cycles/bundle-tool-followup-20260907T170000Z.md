# Bundle tool, follow-up: header, bands, sequence, release, and the review's non-blocking findings

ROUTE AND MODEL

Route: fresh
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-followup-20260907T170000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-followup to origin with a plain push
(git push origin bundle-tool-followup — never with -u), and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-followup", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-followup" -b bundle-tool-followup origin/main

BASE VERIFICATION

Before anything else, fetch origin/main and confirm the base is at the reviewed ref
cd5d8fd29477df29a712609e5b50a1a30e2d8d7f. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/cycles/bundle-tool-tests-20260906T110000Z.md, read from the base ref
  cd5d8fd29477df29a712609e5b50a1a30e2d8d7f — the interface contract; still binding except where TASK overrides it (the
  header, the body form, the ordering, the release asset names)
- reviews/bundle-tool-quality-20260906T150000Z.md,
  reviews/bundle-tool-skeptic-20260906T150000Z.md,
  reviews/bundle-tool-quality-reread-20260906T170000Z.md,
  reviews/bundle-tool-skeptic-reread-20260906T170000Z.md and
  reviews/bundle-tool-skeptic-probes-20260906T150000Z.py, read from the base
  ref cd5d8fd29477df29a712609e5b50a1a30e2d8d7f — the findings TASK item 7 disposes, each with its Location, Consequence and Fix
- bin/rulestore/ (every file), bin/bundle, bin/tests/helpers.py,
  bin/tests/test_bundle_cli.py, bin/tests/test_rulestore.py,
  bin/tests/test_rulestore_store.py, bin/tests/test_rulestore_boundary.py
  and bin/tests/test_cross_cutting.py, read from the base ref
  cd5d8fd29477df29a712609e5b50a1a30e2d8d7f
- process/decision-log.md, read from the base ref cd5d8fd29477df29a712609e5b50a1a30e2d8d7f —
  the entry form for item 1
- the frontmatter block of every file under process/, read from the base ref
  cd5d8fd29477df29a712609e5b50a1a30e2d8d7f — eleven files; item 2 adds one key to each

TASK

You are the Coder. This package applies the human's rulings of 2026-09-06
and 2026-09-07 on the bundle tool, adds bin/release, and disposes every
non-blocking finding the two-pass review and its re-read left open. Where
this directive and the interface contract disagree, this directive wins;
where it and a review artifact's Fix disagree, item 7 states the ruling.
Minimum change per item; the suite stays green at the end of every commit;
every test edit is one this directive rules, and no other. If the frontmatter
hook fires on any file, stop and report.

1. Decisions. Append these four entries to decisions/log.md verbatim, in one
   commit, after the last entry, touching nothing above them. The wording is
   this directive's; downstream artifacts cite the log.

FENCE NOTE: the inner fence is `~~~`, and where a fenced file below carries
fences of its own the outer fence is `~~~~`, so that a nested run of three
tildes does not close it.

~~~markdown
## DEC-000630 — A bundle's header is one comment line
Date: 2026-09-06
Decision: A generated bundle opens with exactly one line, an HTML comment: `<!-- fiducial <owner/repo> @ <full HEAD SHA> <generation timestamp> -->`, the timestamp in the `<YYYYMMDD>T<HHMMSS>Z` form. No member list, no blob list, no title line.
Context: the human's ruling of 2026-09-06 on the first generated bundles: the 240-line member list served no session that loaded a bundle, and the SHA is the one fact a session judges the bundle's age by.
Supersedes: DEC-000320 (header clause only; the filename clause stands)

## DEC-000640 — A bundle is three bands of body text
Date: 2026-09-07
Decision: A bundle renders its rows as body text, one row after another with a blank line between, under no per-row heading; then every selected process document, body only; then the definitions the rows use, under one `## Definitions` heading. Rows sort by their topic's position in the topic sequence, then `order`, then id; process documents sort by their stem's position in the process sequence; a topic or stem the sequence does not name sorts after the last named one, alphabetically.
Context: the human's rulings of 2026-09-06 (no `## R` headings) and 2026-09-07 (rows first, then the process documents as their own band, then the definitions). `order` keeps its meaning as position within a topic.

## DEC-000650 — process/named-queries.md is where a bundle and the sequence are defined
Date: 2026-09-07
Decision: The list of distributed bundles — one per role, the query `role=<slug>` — and the two sequences DEC-000640 orders by live in `process/named-queries.md`, in fenced blocks the tool reads. A process document carries `topic: [<its stem>]`. Nothing else names a bundle or an ordering.
Context: resolves the rule-store PRD's OQ-1. A durable rule lives in the store and the tool derives from it (R0763); a new role or a reordered topic is an edit to the document, never to the tool.

## DEC-000660 — Release assets carry no timestamp; a release is tagged by date
Date: 2026-09-06
Decision: A release attaches README.md and one `fiducial-bundle-<slug>.md` per entry in the list, each generated at the release's SHA, and is tagged `v<YYYY>.<MM>.<DD>`. The file bin/bundle writes for a session keeps its timestamped name. bin/release generates the assets from a synced clone, refuses whole on any failure, and prints the `gh release create` command; the human runs it.
Context: the human's ruling of 2026-09-06 on distribution: a stable asset name gives `releases/latest/download/` a stable URL; the date is the version, since a methodology's semantic version cannot be computed.
~~~

2. process/named-queries.md and the `topic` key. Write process/named-queries.md
   verbatim as fenced below. Then add `topic: [<stem>]` to the frontmatter of
   each of the eleven files already under process/, on its own line directly
   after the `order:` line, the stem being the filename without `.md` — and
   change nothing else in those files. One commit for the new document, one
   for the eleven edits.

~~~~markdown
---
order: 120
topic: [named-queries]
role: [chief-of-staff, release-manager-agent]
session: [decision]
corpus: [software, writing]
---

# Process: Named Queries

The list of bundles fiducial distributes and the order every bundle renders
in. Each list entry is one query over the store; a release attaches one
bundle per entry, generated at the release's SHA. This document is the one
place a bundle's definition and the render order live; the tool reads both
from the fenced blocks below and nothing else names them.

## The list

One bundle per role, named by the role's slug. The query is `role=<slug>`
and nothing more: a role's rows are whatever carries its value, and the
definitions those rows use follow by term. One line per bundle: the name,
then the query.

~~~text
chief-of-staff            role=chief-of-staff
architect-agent           role=architect-agent
spec-reviewer-agent       role=spec-reviewer-agent
test-designer-agent       role=test-designer-agent
coder-agent               role=coder-agent
reviewer-agent            role=reviewer-agent
skeptic-risk-agent        role=skeptic-risk-agent
release-manager-agent     role=release-manager-agent
context-quality-reviewer  role=context-quality-reviewer
writer                    role=writer
copy-editor               role=copy-editor
critic                    role=critic
~~~

A new role is a new line here and a new value on `role`; the tool does not
change.

## Sequence

A bundle is three bands: the rows, then the process documents, then the
definitions. Within the first band a row's `order` is its position within
its topic; the first block below is the position of topics, one position
per line, the topics on a line sharing it. Within the second band the
second block is the position of process documents, by stem. A topic or a
stem neither block names sorts after the last named one, alphabetically.
Definitions render last, always.

~~~text
core
chief-of-staff architect-agent spec-reviewer-agent test-designer coder-agent reviewer skeptic release-manager-agent context-quality-reviewer writer copy-editor critic
decision-layer
intake
change-flow convergence change-control commit-control
directive-invariants command-blocks remote-write-verification-policy
verification verification-boundaries human-review-boundary
review-artifact-schema retro decision-log-policy
public-prose-criteria voice trd prd-template
~~~

The second line holds the twelve role topics at one position: one per
bundle, and they never co-occur.

~~~text
change-flow
prd-template
trd-template
review-artifact
voice
outline
decomposition
spec-test-suite
retro
project-setup
decision-log
~~~

## Generating

Running `bin/bundle --where role=<slug> --name <slug>` on a synced clone
writes `fiducial-bundle-<slug>-<timestamp>Z.md` to `~/Downloads`. The file opens
with one line, an HTML comment naming the repository, HEAD and the
generation time; a session judges the bundle's age from HEAD.

## Releasing

A release is cut on the human's go at one SHA of `main` and tagged
as `v<YYYY>.<MM>.<DD>`. It attaches README.md and every bundle in the list,
each generated at that SHA and named `fiducial-bundle-<slug>.md`, and
nothing else. `bin/release` generates them and prints the `gh release
create` command; the human runs it. A bundle attached to a release is the
version of record for that role until the next release.

## Consuming

- A chat session loads its bundle as a project file, replaced at each
  release.
- A project repository's adapter vendors the bundle file at a pinned
  release tag and points the harness at it; the session reads, never
  fetches. Bumping the tag is the adoption of a release.
- Anyone else reaches a bundle by its release URL:
  `releases/latest/download/fiducial-bundle-<slug>.md`.

The store itself is not distributed. An agent needs its bundle, not the
rows.
~~~~

3. The named-queries reader. The storage boundary stays where AC-RS-4 puts
   it: `bin/rulestore/store.py` is the only module that opens a file. Give
   `FileRowSource` one method, `named_queries_text()`, returning the text of
   `process/named-queries.md` under the root, or `""` when the file is
   absent. Add `bin/rulestore/named_queries.py`, pure over text, with two
   functions: `sequences(text)` → `(topic_positions, process_positions)`,
   the first a list of lists of names (one inner list per line of the first
   fenced block under the `## Sequence` heading), the second a list of stems
   (one per line of the second block); and `bundles(text)` → a list of
   `(name, query_tokens)` from the block under `## The list`, one entry per
   non-blank line, the first field the name and the remaining fields the
   `k=v` tokens. A missing heading or block is an empty result, not an error.
   `MemoryRowSource` gains the same method returning `""`.

4. Ordering (DEC-000640). In `bin/rulestore/query.py`, `select(rows, where,
   sequences=([], []))` sorts the hits with a `sort_key(row, sequences)`
   whose key is: band (0 for a rule, 1 for a process row); then position —
   the index of the line naming the rule's first `topic`, or the process
   row's `topic` (falling back to its path stem when the key is absent), in
   the band's list, with an unnamed name getting the list's length; then the
   name itself (so unnamed ones sort alphabetically among themselves); then
   `order` (`None` last); then id. Rows' `order` values are not changed
   anywhere. `bin/bundle` reads the sequences through
   `named_queries.sequences(FileRowSource(root).named_queries_text())` and
   passes them to `select`.

5. Rendering (DEC-000630, DEC-000640). In `bin/rulestore/render.py`:
   - the header is exactly one line, `<!-- fiducial <repo> @ <head>
     <generated> -->`, followed by one blank line; `TITLE`, the `- Repo:`,
     `- HEAD:`, `- Generated:`, `- Rows:` and `- Definitions:` lines and the
     manifest lines are gone, and `render` no longer reads `row.blob`;
   - each selected row, rules then process documents in the order `select`
     gave, renders as `row.body` followed by one blank line, with no heading
     of its own;
   - `## Definitions` and its entries render exactly as today.
   `_heading` stays, used only by `--near` for its label (item 7, Q6).

6. bin/release (DEC-000660). A new executable `bin/release`, Python 3,
   stdlib plus `rulestore` imported plainly (item 7, Q5), with `--tag TAG`
   (default `v<YYYY>.<MM>.<DD>` for today, UTC) and `--out DIR` (default
   `~/Downloads/fiducial-release-<tag>`), that:
   - refuses — exit 2, one line on stderr, nothing written — outside a git
     repository, in a repository with neither `rules/` nor `process/`, on
     uncommitted changes under `rules/` or `process/`, when the fetch of
     `origin main` fails, when HEAD is not `origin/main`, when `README.md` is
     absent at the root, when the tag already exists on origin
     (`git ls-remote --tags origin <tag>` non-empty), when `--out` exists,
     or when the list is empty;
   - for every entry of `bundles(...)`, in list order, runs `bin/bundle
     --where <tokens> --name <name> --out <tmpdir>` as a subprocess; on any
     non-zero exit, prints one line naming the entry, removes everything it
     wrote, and exits 2;
   - copies each written file to `<out>/fiducial-bundle-<name>.md`;
   - prints the out directory on one line, then as its last line the command
     the human runs: `gh release create <tag> --target <HEAD> --title <tag>
     --notes "fiducial <tag> at <HEAD>" <root>/README.md <asset> ...`, every
     asset by full path in list order; exit 0.
   Add `release` to `CLI_NAMES` in `bin/tests/helpers.py` with
   `CLI_MINIMAL_ARGS["release"] = []` (the refusals above put it past
   argparse into the tool; if a cross-cutting criterion needs another argv,
   use the smallest one that reaches the tool and say which in the report).

7. The review findings. Each is one commit whose message names it; "no
   action" ones get no commit.
   - Q4 — accept: `is_definition` tests `term` present and none of `role`,
     `session`, `corpus` (DEC-000420's wording); amend the contract's
     sentence in `terms.py`'s docstring; add the two-row case to
     `TestPullDefinitions`.
   - Q5 — accept: add `rulestore` to `LOCAL_MODULES` in
     `test_cross_cutting.py`, add `bin/rulestore/*.py` and `bin/release` to
     `production_files()` in `helpers.py`, and replace every
     `importlib.import_module` in `bin/bundle` with a plain import.
   - Q6 — accept the label half: `--near` prints `render._heading(row)` where
     it prints `row.id`; the store half was settled by Q2.
   - Q7 — accept: apply `TYPED_SCALAR_RE` to each unquoted list element; add
     the case to `TestRowShape`.
   - Q8 — accept: refuse (exit 2, the malformed-query path) a `--name`
     containing `/`, `\`, or `..`; one CLI test.
   - Q9 — accept: the two tests its Fix names.
   - Q10 / S11 — accept: `"bundle": ["--keys"]` at its place in
     `CLI_MINIMAL_ARGS` in `helpers.py`, the override and its comment deleted
     from `test_cross_cutting.py`, the comment's substance kept beside the
     entry.
   - Q11 — accept: the CLI test with an `order: twenty` row, all three modes.
   - Q12 — no action.
   - S2 — accept: match any ATX heading whose text is `Human`; the store
     test with `### Human`.
   - S3 — accept: `ast.Import` in `names_imported_from_store`, the
     `FileRowSource`-name assertion, and the docstring sentence.
   - S4 — accept the first two and the smaller third: raise `RowShapeError`
     naming the path on a `rules/` file with no frontmatter; split list
     values on commas outside quotes; raise on a duplicate id across the two
     roots. Three store tests.
   - S5 — accept the minimum: the docstring sentence in `store.py` saying
     `blob` is HEAD's and `body` is the working tree's; the render no longer
     emits blobs (item 5), so nothing downstream sees the two disagree.
   - S6, S7, S9 — no action.
   - S8 — accept: `_synced_with_main` refuses on a non-zero fetch with a
     message distinguishing "could not reach origin" from "not synced"; one
     CLI test.
   - S10 — accept: probe (d)'s real-store section calls
     `terms.pull_definitions`; probe (g)'s g2 prose and `note()` text are
     computed from the observed exits.
   - S12 — accept: refuse, exit 2, one line naming the directory, when the
     resolved root contains neither `rules/` nor `process/`; one CLI test.

8. Ruled test edits (DEC-000440: every test change here is the human's
   ruling, carried by this directive). In `bin/tests/helpers.py`,
   `rs_store_files()` gains `topic=["change-flow"]` on the process document
   and a `process/named-queries.md` whose list names `writer`, `critic` and
   `coder-agent` with their `role=` queries and whose sequence puts `intake`
   before `core` and names `change-flow` in the process block — so a test
   can tell sequence order from alphabetical order. In
   `bin/tests/test_bundle_cli.py`: AC-RS-14 asserts the one comment line
   with HEAD and a `\d{8}T\d{6}Z` timestamp and nothing else in the header;
   AC-RS-15 asserts R0003 (intake) precedes R0001 and R0002 (core), the
   process document's body follows every rule body, no line matches
   `^## R`, and `## Definitions` is the last heading; the `- Definitions:`
   assertion becomes `## Definitions`. In `bin/tests/test_rulestore.py` the
   AC-RS-2 ordering tests take the new key: topic position (alphabetical
   when unnamed) before `order`; add one case with a two-line sequence
   showing a later-named topic sorting after an earlier one whatever its
   `order`. Add `bin/tests/test_release.py` against the fixture repository:
   refuses without README.md; with README.md writes one timestamp-free asset
   per list entry and prints a last line starting `gh release create`
   naming the tag, HEAD, README.md and every asset; a list entry whose query
   selects nothing makes it exit 2 with nothing left under `--out`; refuses
   when `--out` exists. Amend the interface-contract citations in module
   docstrings to name this directive beside the tests directive where the
   contract changed. No other test edit.

9. Write this check script, verbatim, to `$TMPDIR/followup-check.py`
   (uncommitted; VERIFICATION runs it from the worktree):

~~~python
import sys; sys.path.insert(0, "bin")
from rulestore import store, query, terms, render, named_queries
src = store.FileRowSource(".")
rows = src.rows()
seq = named_queries.sequences(src.named_queries_text())
sel = query.select(rows, {"role": "chief-of-staff"}, seq)
text = render.render(sel, terms.pull_definitions(sel, rows), repo="davepierceops/fiducial", head="HEAD", generated="0T0Z")
lines = text.splitlines()
print(lines[0]); print("blank-after-header", lines[1] == "")
print("R-headings", sum(1 for l in lines if l.startswith("## R")))
print("headings", [l for l in lines if l.startswith("## ")][-3:])
print("first-process", next(i for i, r in enumerate(sel) if r.kind == "process"), "of", len(sel))
print("rules-after-first-process", sum(1 for r in sel[next(i for i, r in enumerate(sel) if r.kind == "process"):] if r.kind == "rule"))
~~~

10. Then run the whole suite (`bin/tests/run`), capture to
   `bin/tests/green-run-rulestore-followup.log`, commit it; run the probe
   script and capture to `$TMPDIR/bundle-tool-probes-followup.log`.

Commits, in order, pushed after each: the directive (FIRST ACT); item 1;
item 2 (two); items 3–6 as one commit each; item 7 one per accepted finding;
item 8 as one commit or folded into the item it tests where that is
smaller — say which; the green log. Messages `bundle: <item> — <one
clause>` and `release: <one clause>`. Do not open a pull request. Remove the
worktree at the end (`git worktree remove "$TMPDIR/fiducial-bundle-tool-followup"`)
and report that it is gone.

Report also carries: the diff-stat per commit; the first two lines and the
last three headings of a real chief-of-staff bundle rendered in the worktree
through `FileRowSource`, `select` and `render` directly (the CLI's sync
refusal fires on a branch, and that refusal is correct); the position each
of the eleven process documents took in that bundle; and the standard
response shape as its own labelled section.

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
  python3 "$TMPDIR/followup-check.py"
  grep -c '^topic: \[' process/*.md | grep -vc ':1$'
  grep -n '"bundle"\|"release"' bin/tests/helpers.py | head -4
  grep -c importlib bin/bundle
  ( cd /tmp && "$OLDPWD/bin/release" >/dev/null 2>&1; echo "release-outside-repo exit $?" )
  python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py 2>&1 | grep -E '^\((a|b|c|d|e|f|g)\)' | head -8
  git -C "$TMPDIR/fiducial-bundle-tool-followup" diff --stat origin/main..HEAD | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-followup" log --oneline origin/main..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/bundle-tool-followup-verify.log"
~~~

Expected: OK from the suite; a line beginning with a comment opener carrying
the repo and `@ HEAD 0T0Z`; blank-after-header True; R-headings 0; the last
heading `## Definitions`; the first process row somewhere past the middle of
the selection with 0 rules after it; 0 from the topic-count grep (every
process file has exactly one `topic:` line); helpers lines
showing `["--keys"]` for bundle and an entry for release; 0 importlib; release exit 2
outside a repository; probe (d) and (g) now reading as the tree stands; a
diff-stat touching bin/, decisions/log.md, process/, reviews/ and the
directive file only; a commit count matching the list you report.

STOP CONDITIONS

Pinned to the reviewed ref cd5d8fd29477df29a712609e5b50a1a30e2d8d7f. Cannot execute as written: stop
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

    Bundle tool, follow-up: header, bands, sequence, release, and the review's non-blocking findings — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
