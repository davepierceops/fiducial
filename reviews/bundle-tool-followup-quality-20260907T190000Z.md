# Review: the bundle-tool follow-up delta — bundle-tool-followup-quality-20260907T190000Z

Verdict: changes-required
Verdict (quality): changes-required
Reviewed: the whole diff origin/main..origin/bundle-tool-followup @ 252928b84e19b530b9acc25159a80ab478223848
Baseline: origin/main @ cd5d8fd29477df29a712609e5b50a1a30e2d8d7f
Reviewer: reviewer-agent (execution session, sandboxed)
Date: 2026-09-07
Scope: the whole diff cd5d8fd..252928b — 30 files in 25 commits, +1599/-224: the four DEC entries, `process/named-queries.md` and the eleven `topic:` additions, `bin/rulestore/named_queries.py`, the ordering change in `query.py`, the render rewrite, the new `bin/release`, the eleven accepted findings of item 7, the ruled test edits of item 8, and the amended probe script. Read as one pass over the whole change (R1047). The suite was run in the assigned worktree; the tool and `bin/release` were run against the real store and against purpose-built temporary repositories.
Cross-checked: docs/cycles/bundle-tool-followup-20260907T170000Z.md @ 252928b — the rulings this pass judges against; reviews/bundle-tool-quality-20260906T150000Z.md, reviews/bundle-tool-skeptic-20260906T150000Z.md, reviews/bundle-tool-quality-reread-20260906T170000Z.md and reviews/bundle-tool-skeptic-reread-20260906T170000Z.md @ 252928b — the Fix statements item 7 disposes; decisions/log.md @ 252928b — DEC-000630, DEC-000640, DEC-000650, DEC-000660 as appended; process/named-queries.md and process/review-artifact.md @ 252928b.
Not inspected: `bin/aimeta/` and every CLI outside `bin/bundle` and `bin/release`, untouched by this diff; `bin/rulestore/keys.py` and `near.py`, unchanged; the 468 rows of the real store as content — used as data for the checks, not reviewed; the six non-blocking findings the earlier passes left with "no action" (Q12, S6, S7, S9); performance and concurrency, neither of which any contract states. The skepticism pass over this same delta is `reviews/bundle-tool-followup-skeptic-20260907T190000Z.md`; findings raised there are not repeated here.
Findings: 2 blocking, 3 non-blocking, 2 observations
The human should inspect: F2, because closing it is a ruling only you can make — the code and DEC-000640 state two different sort keys, the code matches the directive you signed and the decision entry does not, and either the entry is amended or the sort changes. Then F1, because item 2 said "verbatim" and the delivered document is not, and the deviation was not among the three the Coder reported.

## Verdict (quality): changes-required

Items 3–6 do what they say and are minimum change. Every one of the eleven accepted
findings in item 7 closes as its Fix stated — checked by running the fixed code, not by
reading the diff for intent — and the ruled test edits of item 8 are the ones ruled, with
the three folded edits the Coder reported each defensible on its own commit message. The
package is well made and the suite is genuinely larger for it: 682 tests against 657, all
25 additions traceable to a ruled clause.

It is gated `changes-required` on two defects that are about the durable record rather
than the running code. `process/named-queries.md` was not written verbatim as item 2
fenced it, and the substitution is load-bearing: the parser recognizes exactly the fence
spelling the delivered file happens to use, so restoring the ruled text empties every
sequence and every bundle in silence (F1). And DEC-000640, which this delta appends and
which downstream artifacts will cite, states a sort key the code does not implement —
observably, in the chief-of-staff bundle as it renders today (F2). Both are the shape S9
named in the first read: a decision and its implementation diverging through the document
between them, with nothing in the chain able to catch it.

## F1 — blocking
Claim: `process/named-queries.md` was not written verbatim as item 2 fenced it — its three data blocks use ``` where the ruled text uses `~~~` — and the parser recognizes only the spelling the delivered file happens to carry, so restoring the ruled text empties both sequences and the bundle list without an error.
Location: process/named-queries.md:24, 37, 52, 62, 67, 79 (the six fence lines); bin/rulestore/named_queries.py:16 (`_FENCE_RE = re.compile(r"^```")`); docs/cycles/bundle-tool-followup-20260907T170000Z.md § TASK item 2
Evidence: Verified by reading and by running. Item 2 says "Write process/named-queries.md verbatim as fenced below", and its FENCE NOTE explains that the outer fence is `~~~~` precisely because the file's own fences are three tildes; the fenced text therefore specifies `~~~text` blocks. The committed file carries ` ```text `. Run in the assigned worktree, feeding the committed document's text with `~~~` substituted for ``` :

    named_queries.sequences(text) -> ([], [])
    named_queries.bundles(text)   -> []

`_section` finds both headings; `_fenced_blocks` matches nothing, and item 3's own rule — "A missing heading or block is an empty result, not an error" — turns the miss into silence. Downstream, `bin/bundle --where` then renders every bundle with `sequences=([], [])`, so band-0 rows fall back to alphabetical-by-topic and the process band loses its order entirely; `bin/release` exits 2 with `refused: the bundle list is empty`, which is the message for a document that has no list rather than one whose list it could not read. The deviation is not among the three the Coder's report names (the four folded fixture and assertion changes, Q5's `LOCAL_MODULES` line landing early, and the probe (f) rewrite).
Consequence: Two things, and the second is the one that matters. First, a document the directive ruled verbatim differs from the ruling and the difference went unreported, so the decision session would sign off on text it did not receive. Second, `process/named-queries.md` is now the one place a bundle and an ordering live (DEC-000650) and it is edited by hand; a later session that writes a new block with the other of Markdown's two interchangeable fence spellings — or that restores the text this directive actually ruled — gets twelve bundles rendered in the wrong order, with no error, no red test, and a header that still stamps the right SHA. That is the silent-wrong-answer shape S4 was raised about, arriving through the document rather than the store.
Fix: Make `_FENCE_RE` accept both spellings — `re.compile(r"^(```|~~~)")` — which closes the fragility whichever text the document carries; then either restore item 2's ruled `~~~` fences or record the backtick fences as the deviation they are, in the decision session's ruling rather than silently. Add the parser tests F5 names, one of them over a `~~~`-fenced document.
Related: F5

## F2 — blocking
Claim: DEC-000640, appended by this delta, states a sort key the code this delta ships does not implement: the code inserts the topic's name ahead of `order`, and keys the process band on a row's `topic` rather than on its stem.
Location: decisions/log.md:739 (DEC-000640's Decision sentence); bin/rulestore/query.py:60-77 (`sort_key`), bin/rulestore/query.py:34-45 (`_topic_sort_value`); docs/cycles/bundle-tool-followup-20260907T170000Z.md § TASK item 4
Evidence: Verified by running, in the assigned worktree. DEC-000640 reads "Rows sort by their topic's position in the topic sequence, then `order`, then id; process documents sort by their stem's position in the process sequence". `sort_key` returns `(band, position, name, order, row.id)` — `name` sits between position and `order` — and `_topic_sort_value` returns a process row's `topic` value when it has one, falling back to the stem only when it does not. Both divergences are the directive's item 4, which the Coder implemented correctly; item 1 ruled the log's wording separately, and the two do not agree. Two constructions:

- Co-positioned topics. Four rows on one sequence line `["writer", "critic"]`, orders 10/20/30/40: `select` returns `R0002, R0004, R0001, R0003` — grouped by topic name, `critic` before `writer`. DEC-000640's key gives `R0001, R0002, R0003, R0004`. This is live, not hypothetical: `process/named-queries.md`'s second sequence line holds twelve role topics at one position, and the real chief-of-staff bundle renders that position as six alphabetical runs — `chief-of-staff` (7 rows), `copy-editor` (1), `critic` (1), `release-manager-agent` (1), `spec-reviewer-agent` (1), `writer` (1) — where DEC-000640 asks for one run interleaved by `order`.
- The process band's key. A process row at `process/change-flow.md` carrying `topic: [zzz]`, against the process sequence `["change-flow"]`, gets position 1 (unnamed) rather than 0. Latent only: all twelve process documents carry `topic: [<stem>]` today, which DEC-000650 requires, so stem and topic coincide.

Consequence: `decisions/log.md` is the durable record downstream artifacts cite; `process/named-queries.md`'s own prose ("a row's `order` is its position within its topic") reads with the code, and the decision entry does not. A session re-deriving the sort from DEC-000640 — which is exactly what DEC-000650's "a durable rule lives in the store and the tool derives from it" invites — produces a different bundle from the tool's and has no way to tell which is right. The first read's S9 named this failure and it has recurred one document further down: the directive was the intermediate that carried the fuller rule, and the log entry it dictated dropped it.
Fix: Dave's ruling, either way. Amend DEC-000640 to state the key the code implements — position, then the topic name, then `order`, then id, and the process band keyed on `topic` with the stem as fallback — or drop `name` from `sort_key` and read the stem for process rows, and change the two ordering tests that assert alphabetical grouping among unnamed topics. The first is the smaller change and matches the behaviour the human saw when he ruled item 4; the second matches the words in the log. A silent divergence is the one option the store exists to forbid (R0183).

## F3 — non-blocking
Claim: The `## Definitions` band's internal order changed, where item 5 said the definitions "render exactly as today".
Location: bin/rulestore/terms.py:49 (`sorted(pulled.values(), key=sort_key)`); bin/rulestore/query.py:60 (`sort_key`'s new default `sequences=([], [])`)
Evidence: Verified by running, against the real store's chief-of-staff selection (57 definitions). `pull_definitions` still calls `sort_key` with no sequences, so its key went from `(order, topic, id)` to `(band, 0, topic, order, id)` — the topic now dominates `order`, where before `order` dominated. The two orderings differ from the first entry: the new band opens `R0535, R0470, R0493, R0465, …` where the old key gives `R0108, R0535, R0003, R0780, …`. Nothing went red, because `test_ac_rs_13_pulled_definitions_use_the_select_ordering_rule` asserts that definitions use `select`'s rule, and they still do — the rule itself moved underneath the assertion.
Consequence: Small in itself: no decision states an order for the definitions band, and a definitions list is read by lookup rather than in sequence. It is worth naming because it is an unruled behaviour change riding on a ruled one, and because the test that covers definition ordering is written so that it cannot notice — it compares the definitions to `select`'s output rather than to a stated order, so any future change to `sort_key` also silently re-orders every bundle's definitions.
Fix: None required for correctness. If the band's order is meant to be stable, pin it — `sorted(pulled.values(), key=lambda r: (r.order if r.order is not None else _NO_ORDER, r.id))` in `terms.py` — and say so in the docstring; otherwise record in `terms.py` that the definitions band inherits whatever `sort_key` currently is, so the coupling is visible where it bites.

## F4 — non-blocking
Claim: `bin/release` lists nine refusals and the suite exercises three of them; the "removes everything it wrote" guarantee is asserted only in the one case where nothing had been written yet.
Location: bin/tests/test_release.py:46-79 (`TestReleaseRefusals`); bin/release:85-120 (the nine refusals), bin/release:122-145 (the scratch directory and its `finally`)
Evidence: Verified by reading and by running. `test_release.py` covers README.md absent, `--out` already exists, and a list entry that selects nothing. Six refusals have no test: outside a git repository, a repository with neither `rules/` nor `process/`, uncommitted changes under `rules/` or `process/`, a fetch that cannot reach origin, HEAD not equal to `origin/main`, and the tag already on origin — the last of which is the only guard against re-cutting a released tag. Each was constructed and run for this pass, and each behaves: exit 2, one line on stderr, no traceback, nothing written (the full table is in the skepticism pass). So this is coverage, not behaviour. On cleanup: `test_refuses_whole_when_a_list_entry_selects_nothing` asserts `self.out` does not exist, which is true by construction — `out_dir.mkdir()` runs only after every entry has succeeded, so the assertion would hold with the `finally` deleted. The scratch directory the `finally` actually removes is asserted by nothing.
Consequence: `bin/release` is the tool that decides what a release contains, run once per release by hand, and its refusals are the whole of its safety. Six of them can regress without reddening anything — the tag-exists check in particular, whose failure mode is overwriting a published release's assets. The cleanup guarantee is stated in the module docstring and in DEC-000660 ("refuses whole on any failure") and is currently held up by a test that cannot distinguish a working `finally` from a missing one.
Fix: One test per untested refusal, each the same shape as the two that exist — the constructions in the skepticism pass are directly reusable. For cleanup, assert the scratch directory is gone: capture `tempfile.gettempdir()`'s `fiducial-release-*` entries before and after a failing run and assert the set is unchanged.

## F5 — non-blocking
Claim: `bin/rulestore/named_queries.py` has no unit test at all; every branch item 3 specifies is exercised only end-to-end, through one well-formed fixture document.
Location: bin/rulestore/named_queries.py (whole module); bin/tests/ (no file imports it)
Evidence: Verified by reading and by running. A grep for `named_queries` across `bin/tests/` returns four hits, none of them a call: the module's name in `test_rulestore_boundary.py`'s `PROCESSING_MODULES` tuple, a fixture path string in `test_rulestore_store.py`, a fixture edit in `test_release.py`, and a docstring in `test_bundle_cli.py`. `sequences()` and `bundles()` are reached only as a side effect of running `bin/bundle --where` or `bin/release` against `rs_store_files()`'s single fixture document, which has both headings, both blocks, no blank lines inside a block, and backtick fences. Untested, each named in item 3 or item 4: a missing file (`named_queries_text()` returning `""`); a missing `## Sequence` or `## The list` heading; a section with one block where two are expected; blank lines inside a block (the `if line.strip()` filters exist and nothing asserts them); a name split across two lines; `MemoryRowSource.named_queries_text()`; and — the sort key's own gap — a process row with no `topic` key resolved against a non-empty process sequence, since both process rows in `test_rulestore.py` run with `sequences=([], [])` and the CLI fixture's process documents now all carry a `topic`.
Consequence: This is the module F1 turns on. Its stated contract is that a miss is an empty result rather than an error, which means every one of these paths fails silently by design — and the only thing that would announce a regression in the parser is a test that reads its return value directly, of which there are none. The green run should not be read as evidence that the parser handles a malformed document (R0111); it is evidence that it handles one well-formed one.
Fix: A `TestNamedQueries` case in `bin/tests/test_rulestore.py`, pure over text, one assertion per branch above — the module takes text and returns data, so each is two lines. Include a `~~~`-fenced document (F1) and a process row whose `topic` is absent against a non-empty process sequence.
Related: F1

## Items 3–6: does the code do what the item says

Each judged against the item's own sentences, in the worktree.

**Item 3 — the named-queries reader. Yes, and minimum change.** `FileRowSource.named_queries_text()` is the one new file read and it lives in the one module allowed to name a storage path; it returns `""` for an absent file (`store.py:202-207`). `MemoryRowSource` gains the same method returning `""`. `named_queries.py` is pure over text — no import beyond `re`, and `test_rulestore_boundary.py` now enumerates it among the processing modules and holds it to their rules. `sequences()` returns a list of lists and a list of stems as specified; `bundles()` splits each non-blank line into a name and its remaining tokens. A missing heading or block is an empty result. The one edit outside the item's letter — adding `named_queries.py` to `PROCESSING_MODULES` — is mechanical, is named in its commit message, and its absence would have left the new module outside the boundary scan, which is the Q5 failure the same package is closing.

**Item 4 — ordering. Yes to the item, and see F2 for the log.** `sort_key(row, sequences=([], []))` returns `(band, position, name, order, id)`, `_position` returns the list's length for an unnamed name, and `select(rows, where, sequences=([], []))` threads it through. No row's `order` value is touched anywhere in the diff. `bin/bundle` reads the sequences through `named_queries.sequences(source.named_queries_text())` and reuses the one `FileRowSource` it already built rather than constructing a second — minimum change, and it keeps the two reads on one object.

**Item 5 — rendering. Yes.** `render` emits `["<!-- fiducial %s @ %s %s -->" % (repo, head, generated), ""]` and then bodies; `TITLE`, `_manifest_line`, the five `- ` lines and every `## <id>` heading are gone, and `row.blob` is no longer read in `render.py`. `_heading` survives with a docstring saying it is `--near`'s alone. `## Definitions` and its `**<term>** — <body>` entries are unchanged in form; their order is not, which is F3.

**Item 6 — bin/release. Yes.** All nine refusals are present, in the item's own order, each exit 2 with one line and nothing written; `rulestore` is imported plainly; `--tag` defaults to `v<YYYY>.<MM>.<DD>` UTC and `--out` to `~/Downloads/fiducial-release-<tag>`; each entry runs `bin/bundle --where <tokens> --name <name> --out <tmpdir>` as a subprocess in list order, a non-zero exit prints one line naming the entry and returns 2 through a `finally` that removes the scratch tree, assets are copied to `<out>/fiducial-bundle-<name>.md`, and the last line is the `gh release create` command with every asset by full path. `helpers.py` gains `"release"` in `CLI_NAMES` and `CLI_MINIMAL_ARGS["release"] = []` as the item specifies. Verified end-to-end against a purpose-built store in the skepticism pass. Coverage is F4.

## Item 7: does each accepted finding close as its Fix stated

Eleven accepted, eleven closed. Each checked against the Fix sentence in its own artifact.

| Finding | Fix as stated | Closed |
|---|---|---|
| Q4 | `term` present and none of `role`, `session`, `corpus`; contract sentence amended; two-row case in `TestPullDefinitions` | yes — `terms.py:16-22`, docstring amended, `test_ac_rs_13_a_row_carrying_term_and_session_is_not_a_definition` |
| Q5 | `rulestore` in `LOCAL_MODULES`, `bin/rulestore/*.py` and `bin/release` in `production_files()`, plain imports in `bin/bundle` | yes — all three; `grep -c importlib bin/bundle` is 0 |
| Q6 | `--near` prints `render._heading(row)` | yes — `bin/bundle:131` |
| Q7 | `TYPED_SCALAR_RE` on each unquoted list element; case in `TestRowShape` | yes — `store.py:133-140`, `test_ac_rs_1_a_typed_value_inside_a_bracket_list_is_also_a_defect` |
| Q8 | refuse a `--name` containing `/`, `\` or `..` on the exit-2 path; one CLI test | yes — `bin/bundle:141-142`, `test_q8_a_name_containing_a_path_separator_or_dotdot_is_refused` |
| Q9 | the two tests its Fix names | yes — `test_q9_the_malformed_query_message_wins_over_a_dirty_tree`, `test_q9_the_repo_label_reflects_a_remote_of_a_known_form` |
| Q10 / S11 | `"bundle": ["--keys"]` in `helpers.py`, override and comment deleted from `test_cross_cutting.py`, substance kept beside the entry | yes — `helpers.py:53-59` (the entry at 59), override gone |
| Q11 | CLI test with an `order: twenty` row, all three modes | yes — `TestBundleMalformedRow`, three tests, the `--where` one also asserting `--out` empty |
| S2 | any ATX heading whose text is `Human`; store test with `### Human` | yes — `HUMAN_MARKER_RE`, `test_s2_a_human_heading_at_any_atx_level_still_splits_the_row` |
| S3 | `ast.Import` in `names_imported_from_store`; a `FileRowSource`-name assertion; the docstring sentence | yes — all three; the candidate module the probe uses is now caught on two checks (see the skepticism pass) |
| S4 | `RowShapeError` on a `rules/` file with no frontmatter, commas outside quotes, a duplicate id across the roots; three store tests | yes — `store.py:225`, `_split_list_items`, `rows()`'s `seen` map; three tests |
| S5 | the docstring sentence saying `blob` is HEAD's and `body` the working tree's | yes — `Row`'s docstring, `store.py:54-61` |
| S8 | `_synced_with_main` refuses on a non-zero fetch, message distinguishing the two; one CLI test | yes — returns `(synced, reason)`; `test_s8_a_failed_fetch_is_distinguished_from_an_unsynced_head` |
| S10 | probe (d)'s real-store section calls `pull_definitions`; probe (g)'s g2 prose and `note()` computed | yes as scoped — and the delta opens three new instances of the same class elsewhere in the file; that is the skepticism pass's finding, not repeated here |
| S12 | refuse, exit 2, one line naming the directory, when the root holds neither `rules/` nor `process/`; one CLI test | yes — `bin/bundle:182-183`, `TestBundleNotTheRuleStore`, three tests |

## Item 8: are the ruled test edits the ones ruled, and no others

Every edit item 8 names is present and correct: `rs_store_files()` gains `topic=["change-flow"]` and a `process/named-queries.md` listing writer, critic and coder-agent with `intake` before `core`; the header assertion is the one comment line with HEAD and `\d{8}T\d{6}Z`; the `- Definitions:` assertion is now `## Definitions`; the AC-RS-2 ordering tests take the new key and gain the two-line-sequence case; `test_release.py` carries the four cases ruled; and the module-docstring citations name this directive beside the tests directive in `query.py`, `render.py`, `store.py`, `terms.py`, `bin/bundle`, `test_rulestore_boundary.py`, `test_release.py` and `TestRender`.

The four deviations the Coder reports, each judged:

- **The four fixture and assertion changes folded into items 3, 4, 5 and 8 — within the grant.** Item 8's own commit clause permits folding "into the item it tests where that is smaller — say which", and each commit message says which. Item 3's `PROCESSING_MODULES` entry is the one that is not an item-8 edit at all; it is a package-membership fact that follows from creating the module, and omitting it would have left `named_queries.py` outside the boundary scan.
- **Q5's `LOCAL_MODULES` line landing early, under item 6 — within the grant, and required.** `bin/release` imports `rulestore` plainly because item 6 says so; without `"rulestore"` in `LOCAL_MODULES` that commit would have failed AC-X-2, and the directive requires the suite green at the end of every commit. The commit message states the split and points at item 7 for the rest. There was no smaller way to satisfy both sentences.
- **Rewriting probe (f) beyond S10's scope — within the grant, and required, though it should have been reported as a necessity rather than an overreach.** S10's grant covers probe (d)'s real-store section and probe (g)'s g2. But S4 makes `FileRowSource.rows()` raise on probe (f)'s f1 and f4 fixtures, so without the two `try/except RowShapeError` blocks the script would die before reaching probe (g) — which S10 explicitly required to be re-run. The f2 and f3 prose branches are wider than strictly necessary and are the part that is discretionary; both are computed rather than printed, so they move the file toward S10's stated intent rather than away from it. No finding.
- **The `process/named-queries.md` fence substitution — not reported, and a finding.** That is F1.

Beyond those, no other test edit appears in the diff. Confirmed by reading every hunk in the five test files and `helpers.py`.

## F6 — observation
Claim: The header test is named for AC-RS-14, which is the two-forms criterion, leaving no test named for AC-RS-6's header clause.
Location: bin/tests/test_bundle_cli.py:145 (`test_ac_rs_14_the_header_is_one_comment_line_naming_head_and_a_timestamp`), against bin/tests/test_bundle_cli.py:204 (`test_ac_rs_14_no_human_content_reaches_the_bundle`)
Evidence: Verified by reading. The pre-delta test was `test_ac_rs_6_the_header_stamps_repo_head_generated_and_the_rows`; item 8 says "AC-RS-14 asserts the one comment line with HEAD and a `\d{8}T\d{6}Z` timestamp and nothing else in the header", and the Coder renamed as instructed. Two tests now carry the AC-RS-14 label for two unrelated criteria, and `grep 'def test_ac_rs_6'` returns nine tests, none of them about the header.
Consequence: Nothing runs differently. It matters only for the next person who greps the suite by criterion: the header criterion is findable under the wrong number, and AC-RS-14's name now covers a clause it never stated. The label came from the directive, so it is not the Coder's to have fixed under DEC-000440.
Fix: Rename to `test_dec_000630_...`, matching the two render-side tests that already carry that label, next time a package touches the file.

## F7 — observation
Claim: Two names in the topic sequence carry no row in the store, and one topic carrying 48 rows is named nowhere in it.
Location: process/named-queries.md:52-62 (the topic sequence block; its second line is 54)
Evidence: Verified by running, over the real store's 468 rows. `architect-agent` and `context-quality-reviewer` appear on the sequence's second line (named-queries.md:54) and no rule row carries either as a `topic` — they are role slugs that happen to have no matching topic, which is why the directive names the first as its worked example. In the other direction, `lexicon` carries 48 rows (14 of them in the chief-of-staff bundle, 10 in architect-agent) and the sequence does not name it, so those rows take position 9 — after every named topic and immediately before the process band. That is exactly what DEC-000640 specifies for an unnamed topic, so the behaviour is right; the document is incomplete rather than the code wrong.
Consequence: None today: the two dead names occupy a shared position line and cost nothing, and `lexicon` rows landing last is a reasonable place for them. Recorded because `process/named-queries.md` presents its block as "the position of topics" and it is not one — it names two topics that do not exist and omits the store's second-largest. A reader tuning the order will not learn from the document that `lexicon` is there to tune.
Fix: None required. If the sequence is meant to be exhaustive, add `lexicon` at the position it should hold and drop the two names no row carries; the tool needs no change either way (DEC-000650).

## What this pass does constrain

Stated so the boundary is legible rather than implied (R0110). Every claim above about the
code's behaviour was produced by running it in the assigned worktree at 252928b, against
the real 468-row store or against repositories built for the check: the twelve bundles
rendered directly through `FileRowSource`, `select` and `render`; `bin/release` end-to-end
against a purpose-built bare origin and clone, and once per refusal; the sort key against
constructed rows; the parser against the committed document and against the same document
re-fenced. The closure table was checked finding by finding against each artifact's Fix
sentence, by reading the code at the named line and running it where the Fix names a
behaviour. Not established: that the 25 commits are each individually green — the suite
was run once, at the tip, and the Coder's per-commit claim was not reproduced; that
`bin/release` behaves against a remote it must reach over a network, which the sandbox
does not offer; or that any behaviour outside `bin/bundle` and `bin/release` is unaffected
beyond what the 682-test run asserts.

## Evidence run

`bin/tests/run` in the assigned worktree at `$TMPDIR/fiducial-bundle-tool-followup-read`,
sandboxed:

    Ran 682 tests in 177.586s
    OK (skipped=7)

The same 682 and the same skip count as `bin/tests/green-run-rulestore-followup.log`,
which records `Ran 682 tests in 175.768s` / `OK (skipped=7)` from the Coder's worktree —
so the log is accurate, and it is the reproduction rather than the log that this pass
cites (S6). The 682 is the first read's 657 plus a net 25 — 34 test
functions added and 9 removed across the five test files, counted from the diff
rather than assumed. Full output:
`$TMPDIR/read-suite-run.log`.
