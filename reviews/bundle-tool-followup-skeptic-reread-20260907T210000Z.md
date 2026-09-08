# Review: the bundle-tool follow-up fix — bundle-tool-followup-skeptic-reread-20260907T210000Z

Verdict: ready-with-findings
Verdict (skepticism): ready-with-findings
Reviewed: the diff origin/bundle-tool-followup..origin/bundle-tool-followup-fix @ 02722aa76be18b6da00fa163d0b1a3df05ec7eeb
Baseline: origin/bundle-tool-followup @ 252928b84e19b530b9acc25159a80ab478223848
Reviewer: skeptic-risk-agent (execution session, sandboxed)
Date: 2026-09-07
Scope: the evidence chain over the fix, not the diff alone — `bin/release` run end-to-end against a purpose-built store repository once clean and once with README.md edited, and once each for a list entry whose name carries `[`, a repeated entry name, an absent `process/named-queries.md`, and five conditions the directive did not name; the real chief-of-staff bundle selected and rendered in the worktree through `FileRowSource`, `select`, `pull_definitions` and `render`, its rule band decomposed run by run against DEC-000640 as amended and its process band against the process sequence; the committed probe script re-run whole; the widened `_FENCE_RE` exercised against documents built for it. Everything marked "verified by running" was produced in the assigned worktree at `$TMPDIR/fiducial-bundle-tool-followup-reread` under the sandbox. Nothing in the Coder's report or in the fix's own tests was taken as evidence for anything; every case below was constructed here.
Cross-checked: reviews/bundle-tool-followup-quality-20260907T190000Z.md and reviews/bundle-tool-followup-skeptic-20260907T190000Z.md @ 7a6f3ce5751168946eaa08d4d81c48f447f2479a — the Fix sentence of each finding the fix disposes, and S13/S14/S15/S16 in particular for what the fix made true or false about them; docs/cycles/bundle-tool-followup-fix-20260907T200000Z.md @ 02722aa — the Coder's instructions and the human's ruling on F2; process/review-artifact.md, decisions/log.md and process/named-queries.md @ 02722aa.
Not inspected: the network — `gh` cannot reach the GitHub API from the sandbox, so no probe ran the command `bin/release` prints, and whether GitHub accepts those arguments is inferred from their shape; the real `~/Downloads` default, which no probe wrote to; `bin/release` or the tool under concurrency; the rest of the follow-up delta, read at 7a6f3ce and not re-read here; F7, held; the 13 commits individually, the suite having been run once at the tip; the 468 rows of the real store as content, used as data. The quality half of this re-read is `reviews/bundle-tool-followup-quality-reread-20260907T210000Z.md`; findings raised there — the docstring's refusal count, DEC-000640 against the document's prose, the guard test against the no-filesystem sentence, the untested process-band branch — are not repeated here.
Findings: 0 blocking, 1 non-blocking, 2 observations
The human should inspect: S17, because the widened dirty check counts untracked files, and the clone this repository lives in carries ten untracked retros right now — so `bin/release` as fixed refuses in the store it exists to release, and the first thing the next release cut will produce is a refusal nobody predicted.

## Verdict (skepticism): ready-with-findings

Where is this lying to us? Nowhere that the last read named. Every construction the
directive asked for was built here and every one behaves: a clean store repository cuts a
release with exit 0, two assets and a `gh` line naming the tag, the target SHA, README.md
and both assets by full path; the same repository with README.md edited and uncommitted
refuses with exit 2 and one line, where before the fix it exited 0 and published a README
the tag did not contain; an entry named `a[b]` produces `fiducial-bundle-a[b].md` and exit
0, where before the fix the same construction raised `IndexError` and exited 1; two
entries named `alpha` refuse before the scratch directory is made, naming `alpha`; and a
deleted `process/named-queries.md` refuses with its own message rather than the empty-list
one, which a present document with an empty block still gets. No scratch directory
survived any of the nine runs.

Nor is it lying about the ordering. The real chief-of-staff bundle was rendered here, and
its rule band is twenty-four runs across nine sequence positions, contiguous and
alphabetical within each position, with `order` ascending inside each run and no topic
appearing twice — which is what DEC-000640 as amended says and what the human ruled when
he chose "grouped". Its process band is the six documents the sequence names, in the
sequence's order, followed by `process/named-queries.md`, which the sequence does not name.
The probe script, which the last read gated a finding on for reporting five states the tree
was not in, now reports none: re-run whole here it exits 0 and every one of the five lines
tracks what the run observed.

What the fix bought at a price it did not price is one thing. S13 was closed by the second
of the two forms its Fix offered — widen the guard rather than read the asset from the
commit — and `git status --porcelain` with no pathspec counts untracked files, not only
modified ones. So the tool now refuses on a scratch file that will never be attached to
anything, and it refuses in this repository as it stands today (S17). That is the safe
direction: it exits 2 with one line and writes nothing, and no release is published wrong.
It is still a behaviour nobody in the chain stated, arriving in the tool that is run by
hand once per release.

## The nine constructions, one line each

Built here from a bare origin and a level clone with `rules/`, `process/change-flow.md`,
`README.md` and a `~~~`-fenced `process/named-queries.md`; committed and pushed, so `HEAD`
equals `origin/main`. `TMPDIR` was pointed at a directory of this pass's own so no run
could disturb the suite's `fiducial-release-*` cleanup assertion. Full log:
`$TMPDIR/reread-release-probes.log`.

| construction | exit | stderr | `--out` | scratch left |
|---|---|---|---|---|
| clean store, end to end | 0 | — | 2 assets | none |
| README.md edited, uncommitted | 2 | `refused: uncommitted changes under <root>` | not created | none |
| one untracked file at the root | 2 | `refused: uncommitted changes under <root>` | not created | none |
| a list entry named `a[b]` | 0 | — | `fiducial-bundle-a[b].md`, `fiducial-bundle-beta.md` | none |
| a list entry named `a*b` | 0 | — | `fiducial-bundle-a*b.md` | none |
| two entries named `alpha` | 2 | `refused: the bundle list repeats the name 'alpha'` | not created | none |
| `process/named-queries.md` deleted | 2 | `refused: no process/named-queries.md under <root>` | not created | none |
| the document present, its list block empty | 2 | `refused: the bundle list is empty` | not created | none |
| a list entry named `a/b` | 2 | `refused: a/b: bin/bundle exited 2` | not created | none |

On the clean run, the printed line is `gh release create v2026.09.07 --target
ec140d38… --title v2026.09.07 --notes 'fiducial v2026.09.07 at ec140d38…'
<clone>/README.md <out>/fiducial-bundle-alpha.md <out>/fiducial-bundle-beta.md`, and
`ec140d38…` is `git rev-parse HEAD` at the clone. On the `a[b]` run the asset's path is
quoted by `shlex.quote` in that line, which is what makes the S14 fix safe at the shell as
well as at the glob. On the `a/b` run the refusal comes from `bin/bundle`'s Q8 `--name`
check reaching `bin/release` as a non-zero exit — the item's second branch, which did not
need to be taken because `[` passes that check.

Two things the read's S13 evidence turned on, re-derived on the fixed tree: with README.md
edited, `git status --porcelain -- rules process` is empty and `git status --porcelain` is
` M README.md`. The pre-fix guard read the first and the fixed guard reads the second.

## The real chief-of-staff bundle, rendered here

Rendered by calling `store.FileRowSource(".").rows()`, `query.select(rows,
parse_where(["role=chief-of-staff"]), sequences)`, `terms.pull_definitions` and
`render.render` directly — the CLI's sync refusal fires on a branch, and that refusal is
correct. Sequences read from the committed `process/named-queries.md`, which parses to 9
topic lines, 11 process stems and 12 bundles. 180 rows selected, 7 of them process
documents, 57 definitions pulled, 57370 bytes rendered. Full log:
`$TMPDIR/reread-chief-render.log`.

The rule band, run by run, with the sequence position each run sits at:

    0 | core 28
    1 | chief-of-staff 7, copy-editor 1, critic 1, release-manager-agent 1,
        spec-reviewer-agent 1, writer 1
    2 | decision-layer 16
    4 | change-control 12, change-flow 6, commit-control 2, convergence 7
    5 | command-blocks 12, directive-invariants 21,
        remote-write-verification-policy 3
    6 | human-review-boundary 1, verification 11, verification-boundaries 9
    7 | decision-log-policy 3, retro 6, review-artifact-schema 7
    8 | prd-template 2, trd 1
    9 | lexicon 14

Checked mechanically rather than by eye: within every position the topic names ascend and
no topic name recurs, so each is one contiguous run; within every run `order` ascends,
`None` last. That is DEC-000640 as amended — "then by topic name, then `order`, then id —
so topics sharing a position render as contiguous alphabetical runs" — holding on the real
store, and it is the behaviour the human saw when he ruled item 4 and then ruled "grouped"
on F2. Position 3 is absent because no row of this bundle carries a topic on that line, and
`lexicon` sits at 9, the sequence's length, because no line names it: F7's shape, held.

The process band, in render order, with the position each resolved to:

    process/change-flow.md      change-flow      0
    process/prd-template.md     prd-template     1
    process/decomposition.md    decomposition    6
    process/spec-test-suite.md  spec-test-suite  7
    process/retro.md            retro            8
    process/decision-log.md     decision-log    10
    process/named-queries.md    named-queries   11

The process sequence is `change-flow prd-template trd-template review-artifact voice
outline decomposition spec-test-suite retro project-setup decision-log`, eleven stems, and
the six the bundle selects come out in it in the sequence's order; `named-queries` is not
in the sequence and takes position 11, the list's length, so it renders last. Every one of
these rows carries `topic: [<stem>]`, so this observation cannot distinguish the amended
rule from the one it replaced — the branch that would is untested, which is the quality
pass's F11.

The definitions band comes back strictly `(order, id)` with `None` last: `R0108(10),
R0003(20), R0535(20), R0780(20), R0004(30), R1474(30), …`, where the read recorded the
pre-fix key giving `R0108, R0535, R0003, R0780`. F3's pin holds on the real store.

## The probe script, re-run whole

`python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py` in the assigned
worktree, exit 0. Full output: `$TMPDIR/reread-probes.log`.

    (a) PASS  5/5 sampled tests failed on their own assertion; log has 86 FAIL, 0 ERROR
    (b) PASS  the two load-bearing checks catch `import rulestore.store` + a split
              string literal; the STORAGE_PATHS substring scan alone would still miss it
    (c) PASS  ahead/behind/dirty all refuse exit 2 with one line; level+clean writes one file
    (d) PASS  whole-word matching is right; a phrase across a line break is not missed
              (0 real rows lose a definition)
    (e) NOTE  blob is HEAD's, body is the working tree's; only the --where refusal keeps
              them consistent
    (f) PASS  untested cases that misbehave: none
    (g) PASS  AC-X-4 now refuses outside a repo for --keys and --near; bin/rulestore/ is
              inside the AC-X static scans (Q5)

All five statements S16 named are now computed from what the run observes, and all five
report the tree correctly. Probe (b)'s headline flipped from a frozen "every boundary
check passes on this module: True" to the two real assertions catching the candidate;
(d)'s clause and its own count now agree; (g1) runs `['--keys']`, the argv the table
actually holds, and concludes from whether `usage:` appears rather than from a sentence
about `bundle base`; (g3) calls `production_files()` and finds the seven `bin/rulestore/`
files Q5 added, and greps `bin/bundle` for `importlib` rather than asserting it. The
summary tail is conditional. S16 is closed, and the chain has a re-runnable artefact again
rather than a record of a revision.

One caution about running it, learned here rather than read: probe (g) creates its
"outside a repository" directory with `tempfile.mkdtemp()`, and when `TMPDIR` names a
directory that does not exist, Python's fallback chain ends at `os.getcwd()` — the store
root. A first run of this pass, made with a mistyped `TMPDIR`, therefore ran `bundle
--keys` *inside* the repository and printed `(g) FAIL … hidden by a stale argv`, which is
not the tree's state. The script's `finally` removed the directory and the worktree was
clean afterwards, confirmed by `git status --porcelain`. This is not a defect in the fix —
the `mkdtemp` line is unchanged by this diff — but the probe's verdict is environment-
sensitive in a way its output does not disclose, and the corrected run above is the one
this pass cites.

## S17 — non-blocking
Claim: S13 was closed by widening `_dirty_under` to `git status --porcelain` with no pathspec, which counts untracked files as well as modified ones — so `bin/release` refuses on a scratch file that will never be attached to anything, and it refuses in this repository as it stands today.
Location: bin/release:61-63 (`_dirty_under(root)`), bin/release:94-95 (the refusal); docs/cycles/bundle-tool-followup-fix-20260907T200000Z.md § TASK item 3; bin/tests/test_release.py:59-68 and :131-139 (both new dirty tests use tracked, modified files)
Evidence: Verified by running. A store repository built here, level with its origin and clean but for one untracked `notes.txt` at the root, refuses: exit 2, `refused: uncommitted changes under <root>`, `--out` never created. `git status --porcelain` reports `?? notes.txt`; `git status --porcelain --untracked-files=no` reports nothing. In the clone this repository lives in, `git status --porcelain` reports ten untracked files under `retros/` right now, so `bin/release` run there would refuse for a reason that has nothing to do with any asset. Neither of the two tests the fix adds for the widened check covers the untracked case — `test_refuses_when_readme_is_uncommitted` edits a tracked README.md and `test_refuses_when_rules_is_uncommitted` appends to a tracked rule — so the widening past "modified" to "untracked" is asserted by nothing.
Consequence: `bin/release` is run by hand, once per release, by a human who has just decided to cut one. The state it will most often find is the store's ordinary working state, which carries untracked retros and scratch files as a matter of course, and in that state it now refuses with a message naming the whole root and no indication of which file it means. The operator's remedy — commit or remove files unrelated to the release — is real work done under a message that does not say what to do, and the likeliest response to an unexplained refusal on a tool with no `--force` is to widen the search for a bug that is not there. It is the safe direction and it is not silent, which is why this is not blocking; it is also a strictly larger refusal than S13 needed, and the read's own Fix preferred the other form for that reason ("the smaller behaviour change and the more honest one").
Fix: Either narrow the check to `git status --porcelain --untracked-files=no` and take S13's first form for the asset — write `git show HEAD:README.md` into the scratch directory and attach that path, which makes every asset a HEAD object and matches the docstring's "all generated at HEAD" — or keep the widened check and make the refusal name what it found, printing the first offending path from the porcelain output on the same line. Either way, one test with an untracked file, which is the case the two new tests do not reach.

## S18 — observation
Claim: The assets of one release carry different `generated` timestamps, because each is produced by its own `bin/bundle` subprocess; a release is stamped at a range of instants rather than at one.
Location: bin/release:135-145 (the per-entry subprocess loop); bin/bundle:160 (`generated = datetime.datetime.now(...)`)
Evidence: Verified by running. On the clean two-entry construction, the assets' first lines are `<!-- fiducial clean/origin @ ec140d38… 20260908T023933Z -->` and `<!-- fiducial clean/origin @ ec140d38… 20260908T023934Z -->` — the same repo label and the same SHA, one second apart. On the real store, where a bundle takes appreciably longer to render, the spread across twelve entries would be larger.
Consequence: None for correctness: DEC-000630 stamps the generation time and DEC-000660's "carry no timestamp" is about the filename, which it is; the SHA, which is what a reader should compare, is identical across every asset and is the tag's own commit. Recorded beside the read's note that two releases at one SHA produce byte-different assets, because it is the same fact one level down — within a single release the headers are not identical either, so nothing downstream should treat the header line as a release identifier. The SHA in it is the identifier.
Fix: None required. If a single stamp is wanted, `bin/release` would have to pass `generated` down to `bin/bundle`, which is a new flag on a CLI this package is not otherwise touching.

## S19 — observation
Claim: The widened `_FENCE_RE` accepts either spelling but does not pair on it — an opening fence can be closed by the other spelling, and a run of four or more is a fence — so a document that nests fenced text inside a fenced block, which is this repository's own convention for quoting one, still parses to an empty result in silence.
Location: bin/rulestore/named_queries.py:16 (`_FENCE_RE = re.compile(r"^(`{3,}|~{3,})")`), :36-48 (`_fenced_blocks`)
Evidence: Verified by running, against documents built here. A `## The list` section whose block opens `~~~text`, carries a stray ` ``` ` line, and closes `~~~` now yields one entry — the stray fence closed the block and the line after it was dropped — where the pre-fix regex yielded none. A section whose block is fenced `~~~~markdown` and quotes a `~~~text` block inside it, which is exactly the FENCE NOTE convention the base directive and the fix directive both use to fence text that itself contains fences, yields `[]` under both the fixed and the pre-fix regex. The real `process/named-queries.md` is unaffected — six tilde fences, none nested, parsing to 9, 11 and 12.
Consequence: Not a regression: neither spelling of the parser handles nesting, and the widening strictly increased what parses. Recorded because F1's lesson was that a fence the parser does not recognize empties every sequence and every bundle without an error, and that lesson is only half learned — the alphabet was widened and the silence was kept. What now stands between a nesting edit and twelve mis-ordered bundles is the F1 guard test, which is a real guard and covers only the real document at its current counts; a `bin/release` run against a store whose document nests would still report `refused: the bundle list is empty`, which is the conflated message the read named.
Fix: None required for this package. The durable form is to make an unparseable document an error rather than an empty result — `sequences()` and `bundles()` raising when a `## Sequence` or `## The list` heading is present and its expected blocks are not — which would turn every one of these silences into one line on stderr. That reverses item 3's "a missing heading or block is an empty result, not an error", so it is a decision rather than a fix.

## Boundary of this pass

Stated because omitting it is how an unbounded claim gets made by accident. Everything
above rests on: one whole `bin/tests/run` in the assigned worktree (`Ran 701 tests in
196.002s`, `OK (skipped=7)`, log at `$TMPDIR/reread-suite-run.log`); nine purpose-built
store repositories, each with a real bare origin and a real clone, one per row of the
table; the real chief-of-staff bundle selected and rendered once through the library
rather than the CLI, and its three bands checked mechanically against DEC-000640 as
amended; `sort_key` against constructed process rows on both branches; the probe script
re-run whole, twice, the second run being the one cited; four documents built for the
fence probe; and the committed `Decision:` line compared as a string against the fix
directive's fenced text. The claim "every construction behaves" covers one construction
per row, each in a fresh repository with real git, and does not cover two refusal
conditions at once, a detached HEAD, a repository whose `.git` is a file, or `gh` actually
accepting the printed arguments — no probe ran that command, because the sandbox cannot
reach the GitHub API. The claim about the chief-of-staff bundle covers the store and the
sequences at 02722aa, rendered in one process. Nothing here re-examines the parts of the
follow-up delta this diff does not touch, which were read at 7a6f3ce.
