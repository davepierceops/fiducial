# Review: the bundle-tool follow-up delta — bundle-tool-followup-skeptic-20260907T190000Z

Verdict: changes-required
Verdict (skepticism): changes-required
Reviewed: the whole diff origin/main..origin/bundle-tool-followup @ 252928b84e19b530b9acc25159a80ab478223848
Baseline: origin/main @ cd5d8fd29477df29a712609e5b50a1a30e2d8d7f
Reviewer: skeptic-risk-agent (execution session, sandboxed)
Date: 2026-09-07
Scope: the whole evidence chain over the delta, not the diff alone — the four DEC entries against the code that implements them, `process/named-queries.md`'s two lists against the store they claim to describe, `bin/release` end-to-end against a purpose-built store repository and once per refusal it lists, all twelve real bundles rendered directly through `FileRowSource`/`select`/`render`, and the committed probe script re-run whole against this tree. Everything below marked "verified by running" was produced in the assigned worktree at `$TMPDIR/fiducial-bundle-tool-followup-read` under the sandbox. Nothing in the Coder's report was taken as evidence for anything; every construction was built here.
Cross-checked: docs/cycles/bundle-tool-followup-20260907T170000Z.md @ 252928b; reviews/bundle-tool-quality-20260906T150000Z.md, reviews/bundle-tool-skeptic-20260906T150000Z.md, reviews/bundle-tool-quality-reread-20260906T170000Z.md and reviews/bundle-tool-skeptic-reread-20260906T170000Z.md @ 252928b — the Fix statements item 7 disposes, and S3/S10/S11/S12 in particular for what the delta made true or false about them; decisions/log.md and process/named-queries.md @ 252928b; process/review-artifact.md @ 252928b.
Not inspected: the network — `gh` cannot reach the GitHub API from the sandbox, so no probe ran the command `bin/release` prints; the real `~/Downloads` default, which no probe wrote to; the tool or `bin/release` under concurrency; `bin/aimeta/` and every CLI outside `bin/bundle` and `bin/release`; the 468 rows of the real store as content, used as data; the 25 commits individually, the suite having been run once at the tip. The quality half of this read is `reviews/bundle-tool-followup-quality-20260907T190000Z.md`; findings raised there — the fence substitution, DEC-000640's sort key, the definitions band's re-ordering, `bin/release`'s untested refusals, the parser's absent unit tests — are not repeated here.
Findings: 1 blocking, 3 non-blocking
The human should inspect: S13, because a release cut with an uncommitted README.md attaches that README to a tag whose commit does not contain it, exit 0 and no warning, and the release URL is the public face of the whole store. Then S16, because the committed probe script — still the review chain's one re-runnable artefact — now carries five statements the tree contradicts, three of which this delta created while closing S10.

## Verdict (skepticism): changes-required

Where is this lying to us? Not in the twelve bundles. All twelve were rendered here
directly, through `FileRowSource`, `select` and `render` rather than through the CLI, and
all twelve are non-empty, correctly banded and correctly ordered under the rule the code
implements; no listed role selects nothing, and the list matches the twelve `role` values
`bin/bundle --keys` reports, exactly, in both directions. Not in `bin/release` either, at
the level the directive asked about: it was run end-to-end against a store built for the
purpose and it did what DEC-000660 says, down to the `gh` line naming the tag, the target
SHA, README.md and every asset by full path; and each of the nine refusals it lists was
constructed here and each fires with exit 2 and one line.

The lying is at three edges. The one that matters is that `bin/release` guards `rules/`
and `process/` against uncommitted change and does not guard the one asset it does not
generate: README.md is read from the working tree and attached to a tag whose commit holds
something else, silently (S13). Then two shapes a hand-edited list can put into a tool
that is supposed to refuse whole — a name with a glob metacharacter produces a traceback
rather than a refusal (S14), and two entries sharing a name collapse to one asset the
`gh` line then names twice (S15). And the probe script, which the last read gated a
finding on for reporting a state the tree was not in, now reports five (S16) — the delta
closed the two S10 named and opened three more while doing it.

## The twelve bundles, rendered here

Rendered in the assigned worktree by calling `store.FileRowSource(".").rows()`,
`query.select(rows, parse_where(tokens), sequences)` and `render.render(...)` directly —
the CLI's sync refusal fires on a branch, and that refusal is correct. Sequences read from
the committed `process/named-queries.md` through `named_queries.sequences()`. The store
holds 468 rows: 456 rules and 12 process documents.

| bundle (role) | rows selected | of which process documents | definitions pulled | rendered bytes |
|---|---|---|---|---|
| chief-of-staff | 180 | 7 | 57 | 57333 |
| architect-agent | 80 | 2 | 50 | 28551 |
| spec-reviewer-agent | 86 | 4 | 51 | 36752 |
| test-designer-agent | 107 | 1 | 53 | 31360 |
| coder-agent | 97 | 1 | 52 | 28937 |
| reviewer-agent | 108 | 2 | 52 | 36054 |
| skeptic-risk-agent | 106 | 2 | 53 | 36439 |
| release-manager-agent | 96 | 3 | 52 | 38518 |
| context-quality-reviewer | 64 | 2 | 50 | 27243 |
| writer | 107 | 3 | 47 | 31812 |
| copy-editor | 138 | 3 | 47 | 35992 |
| critic | 122 | 3 | 47 | 34514 |

No bundle renders empty and no role in the list selects nothing; the smallest,
context-quality-reviewer, is 64 rows and 27KB. Continuity, checked in both directions:
`bin/bundle --keys` reports exactly twelve `role=` values, and the set of those values and
the set of the list's twelve names are identical — nothing listed is unqueryable, and
nothing queryable is unlisted.

## The sort for a topic the sequence does not name

Two cases, and they are opposite. Verified by running.

**A sequence name with no rows.** `architect-agent` and `context-quality-reviewer` sit on
the sequence's second line (`process/named-queries.md:54`) and no rule row carries either
as a `topic` — they are role slugs, and the topics the architect-agent bundle's rows
actually carry are `core`, `change-control`, `change-flow`, `commit-control`,
`convergence`, `remote-write-verification-policy`, `verification-boundaries`,
`decision-log-policy`, `review-artifact-schema`, `trd` and `lexicon`. They cost nothing:
`_position` looks a row's topic up in the band's lists, so a name no row carries is simply
never looked up. Nine of the twelve names on that line do carry rows, and because they
share one position they tie there.

**A topic no sequence line names.** `lexicon` carries 48 rows across the store, 14 of them
in the chief-of-staff bundle and 10 in architect-agent, and no line of the topic sequence
names it. Those rows land at position 9 — `len(topic_positions)`, one past the last named
position (8, `public-prose-criteria voice trd prd-template`) — so they render as the last
run of the rule band, immediately before the first process document, ordered among
themselves by name (all `lexicon`, so it ties), then `order`, then id. That is exactly
what DEC-000640 specifies for an unnamed topic, so the sort is right; what it means in
practice is that the store's second-largest topic renders in a position nobody chose. The
process band has the same shape: `named-queries` is not in the process sequence's eleven
stems, so `process/named-queries.md` renders last of the seven process documents in the
chief-of-staff bundle, after `decision-log`.

The chief-of-staff bundle's rule band, run by run, as it renders today:

    core 28 | chief-of-staff 7, copy-editor 1, critic 1, release-manager-agent 1,
    spec-reviewer-agent 1, writer 1 | decision-layer 16 | change-control 12,
    change-flow 6, commit-control 2, convergence 7 | command-blocks 12,
    directive-invariants 21, remote-write-verification-policy 3 |
    human-review-boundary 1, verification 11, verification-boundaries 9 |
    decision-log-policy 3, retro 6, review-artifact-schema 7 | prd-template 2,
    trd 1 | lexicon 14

The runs between the bars are one sequence position each. Within a position the runs are
alphabetical by topic name rather than interleaved by `order`; that is the divergence from
DEC-000640's stated key, and it is the quality pass's F2.

## S13 — blocking
Claim: `bin/release` guards `rules/` and `process/` against uncommitted change and does not guard README.md, the one asset it does not generate — so a release cut with an edited README attaches a file the tagged commit does not contain, exit 0 and silently.
Location: bin/release:92 (`_dirty_under(root, "rules", "process")`), bin/release:104-106 (`readme = root / "README.md"`), bin/release:139 (`assets = [readme]`), bin/release:149-152 (the `gh` line)
Evidence: Verified by running. A store repository was built here with a bare origin, a level clone, `rules/`, `process/named-queries.md` listing one role, and `README.md` reading `# readme at the commit`; it was committed and pushed, so `HEAD` equals `origin/main`. `README.md` was then edited in the working tree and left uncommitted. Observed:

    git status --porcelain -- rules process   ->  (empty)
    git status --porcelain                    ->   M README.md
    bin/release --tag v2026.09.07 --out …     ->  exit 0, no stderr

The printed command reads `gh release create v2026.09.07 --target e117a89f… … /…/clone/README.md /…/fiducial-bundle-alpha.md`. The README.md at that path holds `# AN UNCOMMITTED README`; `git show e117a89f:README.md` holds `# readme at the commit`. The bundle assets are unaffected — `_dirty_under` covers the two roots `FileRowSource` reads, so every row body does come from the tagged commit, which is S5's gap closed for exactly the two directories it was closed for.
Consequence: DEC-000660 makes a release a set of artifacts at one SHA, and `--target <HEAD>` publishes that claim; `process/named-queries.md` § Consuming makes `releases/latest/download/` the URL anyone outside the project reaches. README.md is the first thing they read and it is the one asset taken from whatever happened to be in the working tree. The failure is silent in both directions that matter: nothing on stderr, exit 0, and the tag's own commit is the thing the reader would have to fetch to notice. Cutting a release right after editing the README — which is the likeliest moment to be editing it — is enough. This is the S5 blob/body split arriving at the distribution boundary, where the earlier reads' reasoning that "the `--where` refusal keeps the two consistent" no longer applies, because the refusal never looked at README.md.
Fix: One line, either way. Read the asset from the commit — `git show HEAD:README.md` written into the scratch directory, and attach that path — which makes every asset a `HEAD` object and matches the module docstring's own "all generated at HEAD"; or widen the guard to `_dirty_under(root)` with no path arguments, so any uncommitted change refuses the release. The first is the smaller behaviour change and the more honest one, since the tool already builds a scratch directory. Add the test with the two cases: an edited README and a clean one.
Related: S15

## S14 — non-blocking
Claim: A list entry whose name carries a glob metacharacter makes `bin/release` exit 1 on an `IndexError` traceback rather than refusing on one line, because it locates the file `bin/bundle` just wrote by globbing a pattern the name itself breaks.
Location: bin/release:135-136 (`matches = sorted(scratch.glob("fiducial-bundle-%s-*.md" % name))`, then `matches[-1]`); bin/bundle:141-142 (the Q8 `--name` check, which rejects only `/`, `\` and `..`)
Evidence: Verified by running. A store repository built here whose list holds one entry, `a[b]   role=alpha`. `bin/bundle --where role=alpha --name 'a[b]' --out <scratch>` exits 0 and writes `fiducial-bundle-a[b]-20260907T…Z.md` — the Q8 guard passes it, since it contains no separator and no `..`. `bin/release` then globs `fiducial-bundle-a[b]-*.md`, in which `[b]` is a character class matching the single character `b`, so it matches nothing:

    bin/release --tag v2026.09.07 --out …   ->  exit 1
    …
    IndexError: list index out of range

Same for `*` and `?` in a name. The scratch directory is still removed — the `finally` runs on the exception — so nothing leaks; what is lost is the refusal.
Consequence: `bin/release`'s docstring and DEC-000660 both say it "refuses whole on any failure", and the repo's convention across every CLI is that a refusal is one line on stderr and never a traceback — Q3 was gated blocking on precisely this shape, and `helpers.no_traceback` is asserted for every CLI in AC-X-4, AC-X-6 and AC-X-7. `bin/release` is now in `CLI_NAMES`, so it is held to that convention, and this path escapes it with exit 1, which is neither of the codes those criteria accept. Non-blocking because reaching it needs a bracket, star or question mark in a bundle name, and every name in the list today is a plain role slug; raised because the guard that would have caught it already exists one module away and was written for the adjacent reason, and because the tool's whole value is that it refuses cleanly.
Fix: Do not glob for a file whose exact name the tool can compute. `bin/bundle` prints the written path on stdout; read `proc.stdout.strip()` and use it, which removes the pattern entirely and also removes the `matches[-1]` "newest wins" heuristic. Failing that, `glob.escape(name)`, and extend `bin/bundle`'s `--name` check to reject anything outside `[A-Za-z0-9._-]`.
Related: S15

## S15 — non-blocking
Claim: Two list entries sharing a name silently collapse to one asset, the second overwriting the first, and the printed `gh` line names that one asset twice.
Location: bin/release:124-143 (`written` is a list, `dest` is keyed on the name, `assets.append(dest)` runs per entry); bin/rulestore/named_queries.py:67-82 (`bundles` returns a list and checks nothing for uniqueness)
Evidence: Verified by running. A store repository built here whose list holds `alpha role=alpha` and `alpha topic=core` — two different queries, one name. Observed: exit 0, no stderr; `--out` holds exactly one file, `fiducial-bundle-alpha.md`, whose content is the second entry's bundle; and the printed command names `/…/fiducial-bundle-alpha.md` twice among its arguments. `shutil.copyfile` overwrites without complaint and nothing compares names.
Consequence: The release is cut and published with one bundle missing and no signal that anything was dropped — the count of entries and the count of assets differ and nothing checks them against each other. The duplicated argument would make `gh release create` itself fail on the second upload, so the human would eventually see *an* error, but it would be `gh`'s, at the end, naming a file rather than a list defect. A duplicate name is a plausible hand edit: the list is a text block edited by adding a line, and the same slug appearing twice is what a copied line looks like.
Fix: Refuse — exit 2, one line naming the repeated name — when `bundles(...)` returns two entries with the same name, beside the existing empty-list refusal. Two lines in `bin/release`, before the scratch directory is made.
Related: S14

## S16 — non-blocking
Claim: The committed probe script reports five statements this tree contradicts. Three of them this delta created: closing S3 and Q5 falsified probes (b), (g1) and (g3), which S10's grant did not reach, and the two S10 did reach are only half computed.
Location: reviews/bundle-tool-skeptic-probes-20260906T150000Z.py — probe (b) at :87-144 (its own copies of the boundary checks); probe (d)'s `note()` at :400-402; probe (g)'s g1 conclusion at :579-581, its g3 section at :600-609, and the `note()` tail at :611-615
Evidence: Verified by running — the script re-run whole in the assigned worktree, output at `$TMPDIR/read-probes.log` — and by running the real checks against the probe's own fixtures. Five, one by one:

- **(b), the whole verdict.** The probe prints "every boundary check passes on this module: True" for a candidate `query.py` that does `import rulestore.store` and calls `rulestore.store.FileRowSource(root).rows()`, and summarises `(b) FAIL`. It carries its own five copies of the boundary checks, frozen at the pre-S3 versions. Run against the real post-S3 `test_rulestore_boundary.py`: `names_imported_from_store` now returns `{'rulestore.store'}` for that candidate, so `test_ac_rs_4_no_processing_module_imports_more_than_row_types` fails on it, and the new `test_ac_rs_4_no_processing_module_references_filerowsource` fails on it too. The candidate is caught on two checks, not clean on five. What remains true is the probe's *second* claim, that a renamed storage root defeats the `STORAGE_PATHS` substring scan — which is why the summary line is not simply wrong, only its headline.
- **(d)'s note.** The count is computed and reads 0; the sentence beside it is not, and the line prints `(d) PASS whole-word matching is right; a phrase across a line break is missed (0 real rows lose a definition)`. The clause and its own number contradict each other on one line.
- **(g1)'s conclusion.** The value is read from `helpers.py`'s source and correctly reads `["--keys"]` after S11. The three lines under it still run `bundle base` and conclude "it dies AT argparse, never reaching the repo, file or encoding work AC-X-4, AC-X-6 and AC-X-7 exist to exercise" — a conclusion about an argv the table no longer holds.
- **(g3).** It re-implements `production_files()` inline as `bin/` plus `bin/aimeta/` and prints "production_files() covers 23 files under bin/ and bin/aimeta/" and "bin/rulestore/ files it covers: none". Q5 added `sorted((BIN_DIR / "rulestore").glob("*.py"))` to the real function, which covers seven. It then prints "bin/bundle reaches it through importlib", where `grep -c importlib bin/bundle` is 0.
- **(g)'s summary tail.** `note()` appends "; bin/rulestore/ is outside every AC-X scan" unconditionally, outside the conditional the delta added for the AC-X-4 half. False since Q5.

Consequence: This script is still the review chain's one re-runnable artefact and the one thing a later session will run instead of re-deriving. A reader who runs it today is told the storage boundary is defeatable by a spelling that is now caught, that a phrase across a wrap is missed when the same line says zero rows are, and — in the summary, which is the part anyone reads — that the new package is outside every static scan when it is inside them. S10's Consequence paragraph is now true of three more places than it was, and two of the three exist because this delta fixed the code without touching the probe that describes it. That is verification drifting from the tree in the direction that hides work rather than hides defects, which is the benign direction and still leaves the next session unable to trust any line of the output.
Fix: Compute the remaining four, as S10's Fix computed the first two. (b) should import `names_imported_from_store` and the two assertions from `bin/tests/test_rulestore_boundary.py` rather than re-implementing them, so it fails when they fail and passes when they pass. (d)'s `note()` text should be built from `len(missed)` the way its verdict already is. (g1)'s conclusion should run the argv the table actually holds. (g3) should call `test_cross_cutting.production_files()` and grep `bin/bundle` for `importlib` rather than asserting both. The `note()` tail should be conditional on what g3 computed. Failing all of that, S10's own fallback stands and should be taken: pin the script's docstring to `b73635d` so it reads as a record of that revision rather than a check of this one — but a pinned script is not a re-runnable artefact, and the chain would then have none.

## Probe results, one line each, and what each now tracks

`python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py`, re-run whole in the
assigned worktree, exit 0. Full output: `$TMPDIR/read-probes.log`.

| probe | prints | tracks the tree as it stands? |
|---|---|---|
| (a) the red-gate | PASS | reads `bin/tests/red-run-rulestore.log`, untouched by this delta — a faithful record of that revision, not a statement about this tree |
| (b) the storage boundary | FAIL | **no** — headline verdict false since S3; the rename half still true (S16) |
| (c) the sync refusal | PASS | yes — four repository states built and run; ahead, behind and dirty each refuse with one line, level-and-clean writes one file |
| (d) definitions by term | PASS | verdict yes, prose no (S16) |
| (e) the header | NOTE | yes — the blob/body split is unchanged by this delta and the probe re-observes it |
| (f) the untouched cases | PASS, "none" | yes — all four sub-probes now computed; f1 and f4 report the `RowShapeError` S4 added, f2 reports the quoted comma surviving, f3 reports the `### Human` heading no longer leaking |
| (g) the pre-existing scans | PASS | g2 yes; g1's value yes and its conclusion no; g3 no; the summary tail no (S16) |

The four still printing static text are named in S16. Probe (f)'s rewrite was wider than
S10's grant and was also necessary — S4 makes f1's and f4's fixtures raise, so without the
two `try/except` blocks the script would die before reaching (g), which S10 required to be
re-run; the quality pass takes that judgment.

## bin/release, end to end and once per refusal

Constructed here, not read. A bare origin, a clone level with it, `README.md`,
`rules/R0001.md`, `rules/R0002.md`, `rules/R0100.md` (a definition carrying `term:
[tranche]`), `process/change-flow.md`, and a `process/named-queries.md` listing three
roles — `alpha`, `beta`, `gamma` — each `role=<slug>`, with a two-line topic sequence and
a one-line process sequence. Committed and pushed, so `HEAD` equals `origin/main`.

`bin/release --tag v2026.09.07 --out <dir>` exits 0 with empty stderr. Observed:

- **Asset names.** Exactly three files, `fiducial-bundle-alpha.md`,
  `fiducial-bundle-beta.md`, `fiducial-bundle-gamma.md` — one per entry, in list order, no
  timestamp in any name.
- **Every asset's first line.** Each is
  `<!-- fiducial rel-probe/origin @ 82c63a33984a3af34556128cf6d9226121262b32 20260907T175312Z -->`,
  matching `^<!-- fiducial \S+ @ \S+ \d{8}T\d{6}Z -->$`, and the SHA in each is
  `git rev-parse HEAD` at the clone — the one-line header at that HEAD, for all three.
- **The printed `gh` line.** `gh release create 'v2026.09.07' --target
  82c63a33… --title 'v2026.09.07' --notes 'fiducial v2026.09.07 at 82c63a33…'
  /…/clone/README.md /…/release-out/fiducial-bundle-alpha.md
  /…/release-out/fiducial-bundle-beta.md /…/release-out/fiducial-bundle-gamma.md`. It
  names the tag (three times, as `--target`'s peer, `--title` and inside `--notes`), the
  target SHA, README.md by full path, and every asset by full path in list order. Every
  argument passes through `shlex.quote`.
- **A listed query that selects nothing.** With `nobody role=nobody` appended to the list,
  `bin/release` exits 2 with the single line `refused: nobody: bin/bundle exited 2`,
  stdout empty, `--out` never created, and no `fiducial-release-*` scratch directory left
  in `$TMPDIR`. Refused whole, as DEC-000660 says.

Each of the nine refusals the tool lists, constructed separately — all exit 2, one line on
stderr, no traceback, nothing written:

| refusal | message |
|---|---|
| outside a git repository | `refused: not inside a git repository` |
| neither `rules/` nor `process/` | `refused: no rules/ or process/ under <dir>` |
| uncommitted under `rules/` | `refused: uncommitted changes under rules/ or process/` |
| fetch cannot reach origin | `refused: could not fetch origin/main` |
| HEAD ahead of `origin/main` | `refused: HEAD is not origin/main` |
| README.md absent | `refused: README.md is missing at <dir>` |
| tag already on origin | `refused: tag v2026.09.07 already exists on origin` |
| `--out` already exists | `refused: --out already exists: <dir>` |
| the list is empty | `refused: the bundle list is empty` |

A tenth, not listed but reachable: `process/named-queries.md` absent entirely gives
`refused: the bundle list is empty`, since `named_queries_text()` returns `""` for a
missing file and `bundles("")` returns `[]`. The message names the wrong cause — the same
conflation the quality pass's F1 describes for a document whose fences the parser does not
recognize — but the tool does refuse, which is what matters here.

## One thing that is not a finding

Two releases cut at the same SHA produce byte-different assets. Verified by running:
rendering the writer selection twice with different `generated` values gives two files
identical on every line but the first, and different SHA-256s. That is DEC-000630 working
as decided — the header stamps the generation time — and DEC-000660's "carry no timestamp"
is about the filename, which it is. It is recorded only so that nobody later reads
`releases/latest/download/` as diffable: to tell whether a release changed anything,
compare the SHA in the header, not the file.

## Boundary of this pass

Stated because omitting it is how an unbounded claim gets made by accident. Everything
above rests on: one whole `bin/tests/run` in the assigned worktree (`Ran 682 tests in
177.586s`, `OK (skipped=7)`, log at `$TMPDIR/read-suite-run.log`); one whole re-run of the
committed probe script; all twelve real bundles rendered through the library rather than
the CLI; `bin/release` run end-to-end twice and once per refusal against thirteen
purpose-built repositories; four constructions written for this pass — the uncommitted
README, the glob-metacharacter name, the duplicate list name, and the `~~~`-refenced
document; and reading the diff, the four prior artifacts and the four DEC entries. The
claim "all twelve bundles render" covers the store at 252928b and the sequences at
252928b, rendered in one process, and says nothing about the CLI writing them, which the
sync refusal correctly prevented on a branch. The claim "every refusal fires" covers one
construction per refusal, each in a fresh repository with real git, and does not cover two
refusal conditions at once, a detached HEAD, a repository whose `.git` is a file, or a
`git` binary absent from `PATH`. The claim about the `gh` line covers the string
`bin/release` prints; no probe ran it, because `gh` cannot reach the GitHub API from the
sandbox, so whether GitHub accepts those arguments is inferred from their shape and not
observed. Nothing here re-examines the findings the earlier reads left open beyond what
the delta changed about them.
