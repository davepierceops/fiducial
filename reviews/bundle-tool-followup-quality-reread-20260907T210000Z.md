# Review: the bundle-tool follow-up fix — bundle-tool-followup-quality-reread-20260907T210000Z

Verdict: ready-with-findings
Verdict (quality): ready-with-findings
Reviewed: the diff origin/bundle-tool-followup..origin/bundle-tool-followup-fix @ 02722aa76be18b6da00fa163d0b1a3df05ec7eeb
Baseline: origin/bundle-tool-followup @ 252928b84e19b530b9acc25159a80ab478223848
Reviewer: reviewer-agent (execution session, sandboxed)
Date: 2026-09-07
Scope: the fix alone — 11 files in 13 commits, +604/-66: `bin/release`, `bin/rulestore/named_queries.py`, `bin/rulestore/terms.py`, `process/named-queries.md`, DEC-000640's `Decision:` line in `decisions/log.md`, `bin/tests/test_release.py`, `bin/tests/test_rulestore.py`, `bin/tests/test_bundle_cli.py`, the probe script, the green log, and the fix directive itself. Judged item by item against `docs/cycles/bundle-tool-followup-fix-20260907T200000Z.md` and, behind it, against the Fix sentence of each finding in the read the fix answers. Every behavioural claim below was produced by running the code in the assigned worktree at `$TMPDIR/fiducial-bundle-tool-followup-reread`, not by reading the diff for intent.
Cross-checked: reviews/bundle-tool-followup-quality-20260907T190000Z.md and reviews/bundle-tool-followup-skeptic-20260907T190000Z.md @ 7a6f3ce5751168946eaa08d4d81c48f447f2479a — the findings the fix claims to close; docs/cycles/bundle-tool-followup-fix-20260907T200000Z.md @ 02722aa — what the Coder was told and the human's ruling on F2 (grouped); process/review-artifact.md @ 02722aa; decisions/log.md, process/named-queries.md, bin/tests/test_rulestore_boundary.py and bin/bundle @ 02722aa, read to judge the fix rather than re-reviewed.
Not inspected: the rest of the follow-up delta, read at 7a6f3ce and not re-read here — `bin/rulestore/query.py`, `render.py`, `store.py`, `keys.py`, `near.py`, `bin/bundle` and `helpers.py` are unchanged by this diff and were read only where the fix's correctness turns on them; F7, held for the human's ruling and not a finding here; the network, which `gh` cannot reach from the sandbox, so the printed `gh release create` line is judged as a string and was never executed; the 13 commits individually — the suite was run once, at the tip, and the Coder's per-commit green claim was not reproduced; `bin/aimeta/` and every CLI outside `bin/bundle` and `bin/release`; performance and concurrency. The skepticism half of this re-read is `reviews/bundle-tool-followup-skeptic-reread-20260907T210000Z.md`; findings raised there are not repeated here.
Findings: 0 blocking, 4 non-blocking, 2 observations
The human should inspect: F9 and F10, because both are the directive's own doing rather than the Coder's and neither is his to have fixed under DEC-000440 — F2's amendment moved `decisions/log.md` onto the code and left `process/named-queries.md` saying the opposite, and item 1's guard test falsified a sentence that two module docstrings state as the second half of AC-RS-4. Then F8, because two refusals were added to `bin/release` without extending the docstring sentence that enumerates them, and that sentence is the tool's stated contract.

## Verdict (quality): ready-with-findings

Every item the fix directive names is done, and done the way it says. All eleven findings
the directive dispositions close — checked by running the fixed code against constructions
built here, not by reading the diff for intent — and the package is unusually tight: 13
commits, one per item, and every commit's diffstat touches exactly the files its item
names and no others. Nothing in this diff reaches outside its finding.

The suite is green at 701 tests in the assigned worktree, the same 701 and the same skip
count the committed green log records, and the 19 net new tests are all traceable to a
ruled clause. The three blocking findings are genuinely closed, and closed at the level
that matters rather than at the level of the diff: DEC-000640 now states, byte for byte,
the key `sort_key` implements, and the real chief-of-staff bundle rendered here shows the
rule band as twenty-four contiguous alphabetical runs with `order` ascending inside each —
which is what the amended sentence says and what the human ruled.

It is not `ready`, because the fix closed three findings by moving a claim into one
document and left the other document that carries the same claim behind. `bin/release`
gained two refusals its docstring does not list (F8). DEC-000640 now says process
documents sort on their `topic` value; `process/named-queries.md`, which DEC-000650 makes
the place a bundle and its ordering are defined, still says "by stem" (F9). And
`test_rulestore.py` now reads the real store through `FileRowSource` while its own
docstring — and `test_rulestore_boundary.py`'s — state that nothing in it touches the
filesystem (F10). That is S9's shape again, one document further along each time: none of
the three can redden a test, and each was created by an instruction that forbade touching
the second document. They are non-blocking because in every case the code is right and the
prose is stale, which is the direction that misleads a reader rather than the tool.

## Item by item: does the fix do what the directive says

Each judged against the item's own sentences, in the assigned worktree, by running.

**Item 1 — F1, the fences and `_FENCE_RE`. Yes.** `process/named-queries.md`'s six fence
lines are `~~~`; the file carries six tilde fences and zero backtick fences, and no other
line of it changed (the commit's diffstat is 12 lines, six pairs). `_FENCE_RE` is
`^(`{3,}|~{3,})`, which accepts a run of three or more of either. The guard test
`TestNamedQueriesRealDocument.test_the_real_document_parses_to_its_full_counts` reads the
real document through `FileRowSource(REPO_ROOT).named_queries_text()` and asserts 9 topic
lines, 11 stems and 12 entries; re-derived here independently, the real document parses to
exactly 9, 11 and 12. The guard would have caught the fence substitution the read found —
under the pre-fix `^```` regex the restored document parses to `([], [])` and `[]`. Its
cost is F10 and F13.

**Item 2 — F2, the human's ruling. Yes, verbatim.** The `Decision:` line committed at
`decisions/log.md` and the line fenced in the fix directive were extracted and compared as
strings: byte-identical. No other line of DEC-000640 or of the log changed — the commit is
one insertion and one deletion. No code change, as the item says.

**Item 3 — S13, the widened dirty check. Yes.** `_dirty_under(root)` takes no path
arguments and runs `git status --porcelain` with no pathspec; the refusal message is
`refused: uncommitted changes under <root>`; the docstring's refusal sentence is amended
and says why README.md is the reason. One test,
`test_refuses_when_readme_is_uncommitted`. Constructed and run in the skepticism pass: a
store repository level with its origin, README.md edited and left uncommitted, refuses
with exit 2 and one line where it previously exited 0 and published. What the widening
also does is S17, in the skepticism pass.

**Item 4 — F3, the definitions band. Yes.** `terms.py` no longer imports
`query.sort_key`; `pull_definitions` sorts on `(order or inf, id)`; the docstring says so
and names F3 and DEC-000640. The existing definitions test was renamed
`test_ac_rs_13_pulled_definitions_sort_by_order_then_id_none_last` and gained a
`None`-order row. The rename is beyond the item's literal "add the assertion", and it is
the right call rather than an overreach: the old name asserted that definitions "use the
select ordering rule", which this item makes false, so adding an assertion under the old
name would have left the suite carrying a sentence the code contradicts. Run against the
real store's chief-of-staff selection, the 57 definitions come back strictly `(order, id)`
— `R0108(10), R0003(20), R0535(20), R0780(20), …`, where the read recorded the pre-fix key
giving `R0108, R0535, R0003, R0780`.

**Item 5 — F4, the untested refusals and the cleanup assertion. Yes, all seven.** One test
each for the six refusals that had none: outside a git repository, neither `rules/` nor
`process/`, uncommitted under `rules/`, a fetch that cannot reach origin, HEAD not
`origin/main`, and the tag already on origin. Each asserts exit 2 and, in four of the six,
the exact message string. The cleanup test captures `fiducial-release-*` under
`tempfile.gettempdir()` before and after a run that fails on a fourth list entry after
three assets are written, and asserts the sets are equal — and it is not vacuous the way
the assertion it replaces was: `helpers.base_env` inherits `TMPDIR` rather than overriding
it, so the test process and the `bin/release` subprocess resolve the same temporary
directory, and deleting the `finally` would leave a directory the `after` set sees.

**Item 6 — F5, `TestNamedQueries`. Yes for the six branches the item lists.** Pure over
text, one assertion pair per branch: `""`, a document with no heading, blank lines inside
a block, a name split across two lines, a `~~~`-fenced document and a backtick-fenced one.
The sort test for a process row with no `topic` against a non-empty process sequence is
there and discriminates — the row resolves to its stem at position 1, where a broken
fallback would give the list's length, 2. Two branches the read's F5 named are not in the
item's list and remain untested: F12.

**Item 7 — S14, the glob. Yes, the first form.** `matches = sorted(scratch.glob(...))` and
`matches[-1]` are gone; `bin/release` reads `pathlib.Path(proc.stdout.strip())`.
`bin/bundle`'s `--where` write path prints exactly one line, `print(str(dest))` at
`bin/bundle:173`, so `strip()` is the whole path and nothing else — the modes that print
more (`--keys`, `--near`) are never the ones `bin/release` runs. `bin/bundle`'s `--name`
check passes `[`, so the item's second branch did not apply and the test asserts the
success form: `test_a_name_carrying_a_glob_metacharacter_still_produces_one_asset` names
an entry `a[b]` and asserts the asset exists. It discriminates — under the pre-fix glob
the same construction raises `IndexError` and exits 1.

**Item 8 — S15, the repeated name. Yes.** The check sits after the empty-list refusal and
before the scratch directory is made, so nothing is written; the message names the
repeated name. Constructed and run: two entries named `alpha` refuse with `refused: the
bundle list repeats the name 'alpha'`, exit 2, `--out` never created. `names.count(name)`
inside the generator is quadratic in the list's length, which for twelve entries is not
worth changing.

**Item 9 — the tenth refusal. Yes.** An absent `process/named-queries.md` refuses with
`refused: no process/named-queries.md under <root>`, distinct from `refused: the bundle
list is empty`, which a present document with an empty list block still gets. Both were
constructed and run. The check is placed after the `--out` existence check, so a run that
would fail both reports the `--out` one first; nothing states an order for the refusals, so
this is a choice rather than a defect. It is F8's other half.

**Item 10 — S16, the four remaining static statements. Yes, and the script now passes.**
Probe (b) writes the candidate module to a scratch directory and calls
`test_rulestore_boundary.names_imported_from_store` and `source_of` against it, restoring
`PACKAGE_DIR` in a `finally`, so the probe fails exactly when those assertions fail;
(d)'s `note()` clause is built from `missed`; (g1) runs the argv the table actually holds
and branches on whether `usage:` appears; (g3) calls `test_cross_cutting.production_files()`
and greps `bin/bundle` for `importlib`; the summary tail is conditional on what g3
computed. Re-run whole here, exit 0: every line the read named as static now reports the
tree's real state — (b) PASS "the two load-bearing checks catch …", (d) "a phrase across a
line break is **not** missed (0 real rows …)", (g) PASS "… bin/rulestore/ is inside the
AC-X static scans (Q5)".

**Item 11 — F6, the rename. Yes.** `test_dec_000630_the_header_is_one_comment_line_naming_
head_and_a_timestamp`, matching the two render-side tests that already carry that label.
Its docstring still reads "AC-RS-14/DEC-000630", which is now accurate as a citation of
both rather than a misfiled label.

## Does the fix reach outside its finding

No. Every commit's diffstat was read against its item's sentences:

| commit | files | outside the item |
|---|---|---|
| cba8937 F1 | named_queries.py, test_rulestore.py, process/named-queries.md | none |
| 564d885 F2 | decisions/log.md (1 line) | none |
| fa28042 S13 | bin/release, test_release.py | none |
| 47719fb F3 | terms.py, test_rulestore.py | the test rename, judged above and within the grant |
| 0a8f4b7 F4 | test_release.py | none |
| d451b0d F5 | test_rulestore.py | none |
| d2fdbe2 S14 | bin/release, test_release.py | none |
| ffcdb3f S15 | bin/release, test_release.py | none |
| 8426186 tenth | bin/release, test_release.py | none |
| 2376c73 S16 | the probe script | none |
| bbf68e3 F6 | test_bundle_cli.py | none |
| 02722aa green | the green log | none |

`bin/bundle` keeps its own `_dirty_under(root, "rules", "process")`; item 3 changed only
`bin/release`'s. The two CLIs now hold different dirty policies, which is right — only
`bin/release` attaches an asset it does not generate — and neither docstring claims
otherwise.

## F8 — non-blocking
Claim: `bin/release`'s module docstring enumerates the refusals and lists nine; the code now has eleven. Items 8 and 9 added refusals without extending the sentence item 3 did extend.
Location: bin/release:6-15 (the docstring's refusal sentence); bin/release:121 (`no process/named-queries.md`), bin/release:130 (`the bundle list repeats the name`)
Evidence: Verified by reading and by running. The docstring names: outside a git repository, neither `rules/` nor `process/`, any uncommitted change under the root, a failed fetch, HEAD not `origin/main`, README.md absent, the tag on origin, `--out` exists, the bundle list empty — nine, plus the per-entry `bin/bundle` clause. `grep -n 'refuse('` returns eleven call sites in `main` (89, 92, 95, 98, 104, 108, 111, 118, 121, 125, 130) plus the per-entry `return EXIT_REFUSED` at 144. The two the sentence omits were both constructed and run here and both fire: `refused: no process/named-queries.md under <root>` and `refused: the bundle list repeats the name 'alpha'`. Item 3 amended this same sentence for S13, so the pattern was established in the same package and not followed for items 8 and 9.
Consequence: The docstring is `bin/release`'s stated contract — it is what the read's own F4 counted refusals against ("lists nine refusals and the suite exercises three of them"), and it is the only enumeration anywhere; DEC-000660 states "refuses whole on any failure" and names none of them individually. A later pass counting coverage against the docstring will conclude the suite is complete when two refusals are outside the count, which is the same arithmetic F4 used to find a gap. It is also the shape F4's Fix was meant to end: a refusal that can regress without reddening anything is now a refusal that can regress without being listed either.
Fix: Extend the sentence with the two conditions, in the code's order — after "when `--out` exists": "when `process/named-queries.md` is absent, when the bundle list is empty, or when two entries in it share a name". One line.

## F9 — non-blocking
Claim: F2 amended DEC-000640's process-band rule from the stem to the row's `topic` value; `process/named-queries.md`, which DEC-000650 makes the place a bundle and its ordering are defined, still says the second block is "the position of process documents, by stem".
Location: process/named-queries.md:47-48 ("Within the second band the second block is the position of process documents, by stem."); decisions/log.md:739 (DEC-000640 as amended); bin/rulestore/query.py:34-45 (`_topic_sort_value`)
Evidence: Verified by reading and by running. The amended `Decision:` reads "process documents sort by their `topic` value's position in the process sequence, the path stem standing in where the key is absent". The document's prose was not touched — item 1 ruled "change nothing else in the file", so this is the directive's own doing and not the Coder's to have fixed under DEC-000440. The two readings differ observably: a process row at `process/zzz-late.md` carrying `topic: [intake]`, against the process sequence `["intake", "change-flow"]`, sorts at position 0 under the code and the amended log, and at position 2 — after every named stem — under the document's sentence. Constructed and run: `sort_key` returns `(1, 0, 'intake', 10, 'P1')`. Latent in the real store only because all twelve process documents carry `topic: [<stem>]`, which DEC-000650 requires; the amendment is precisely what makes the two diverge when one does not.
Consequence: The divergence F2 was raised about has not been eliminated, only moved. Before the fix the log and the document agreed with each other and disagreed with the code; now the log agrees with the code and the document disagrees with both. DEC-000650 says a durable rule lives in the store and the tool derives from it, and `process/named-queries.md` is the store document a session reads to learn the ordering — it is the one hand-edited file in the chain, and it is now the one that is wrong. The same paragraph is also silent on the topic-name tiebreak the amendment added: it says the topics on a line share a position and never says that they render as contiguous alphabetical runs, so a reader tuning the sequence cannot predict the output from the document alone.
Fix: One sentence in `process/named-queries.md` § Sequence, in a package permitted to edit it — "by their `topic` value, the path stem standing in where the key is absent" for the second band, and a clause in the first band's sentence saying topics sharing a position render as contiguous alphabetical runs ordered by topic name. The code and the log need no change; they are what the human ruled.
Related: F10

## F10 — non-blocking
Claim: `TestNamedQueriesRealDocument` reads the real `process/named-queries.md` through `FileRowSource`, while `test_rulestore.py`'s own docstring and `test_rulestore_boundary.py`'s both state that nothing in that module touches the filesystem — the sentence they call the second half of AC-RS-4.
Location: bin/tests/test_rulestore.py:13-16 ("**Nothing in this module touches the filesystem.**"); bin/tests/test_rulestore.py:44-45 (the `FileRowSource` and `REPO_ROOT` imports), :653-666 (`TestNamedQueriesRealDocument`); bin/tests/test_rulestore_boundary.py:10-12 ("`bin/tests/test_rulestore.py` carries the other half of AC-RS-4 — every processing test there builds its rows in memory and touches no file")
Evidence: Verified by reading and by running. The guard test calls `FileRowSource(REPO_ROOT).named_queries_text()`, which reads `process/named-queries.md` off disk; run here, it returns the real document and the assertions pass. Both docstrings were read at the fix ref and neither was touched by the diff. This is the directive's own doing: item 1 specifies the test in exactly this form, and DEC-000440 leaves the Coder no grant to amend an unruled docstring. Nothing enforces either sentence — no test asserts it, which is why the suite is green with the claim false.
Consequence: AC-RS-4 is a two-part guarantee and `test_rulestore_boundary.py` names where each part lives. One of the two named locations no longer holds, and the module that names it says it does — so a reader checking whether the storage boundary is still enforced is told by the boundary module itself to look at a file whose property has silently lapsed. The practical cost is the next processing test: the module's rule was "build the row in memory", and the precedent now sitting in it is "read the real store", which is exactly the drift AC-RS-4 exists to prevent. The guard test itself is worth having; it is the only thing standing between a fence-spelling edit and twelve silently mis-ordered bundles.
Fix: Either amend both docstrings to name `TestNamedQueriesRealDocument` as the one deliberate exception and say why a guard over the real document has to read it — or move the guard to a module already allowed the filesystem, `test_rulestore_store.py` or `test_bundle_cli.py`, which is the smaller change and leaves AC-RS-4's second half intact. Whichever the decision session picks, it is a ruling rather than a code fix.
Related: F9, F13

## F11 — non-blocking
Claim: The amended DEC-000640's process-band rule has a test for its fallback half and none for its primary half — no test resolves a process row whose `topic` differs from its stem against a non-empty process sequence.
Location: bin/tests/test_rulestore.py:647-652 (`test_a_process_row_with_no_topic_falls_back_to_its_stem`); bin/rulestore/query.py:34-45 (`_topic_sort_value`); decisions/log.md:739
Evidence: Verified by reading and by running. Every test in the suite that constructs a process row lives in `test_rulestore.py`; there are six, and the three AC-RS-2 ordering tests plus the two AC-RS-15 render tests either run with `sequences=([], [])` or use rows whose `topic` equals their stem. The one new test covers the branch where `topic` is absent. The uncovered branch is the one the amendment newly blesses and the one F2's second bullet named as the divergence: constructed here, a row at `process/zzz-late.md` with `topic: [intake]` against `["intake", "change-flow"]` sorts to position 0, and nothing in the suite would notice if `_topic_sort_value` stopped reading `topic` for process rows and returned the stem unconditionally — which is exactly the change DEC-000640's pre-amendment wording asked for.
Consequence: The sentence the human just ruled into the log is the half without a test. `decisions/log.md` is now the only place that says process rows sort on `topic`, `process/named-queries.md` says the opposite (F9), and the suite would stay green under either implementation — so if the next package resolves F9 by changing the code to match the document rather than the document to match the log, nothing reddens. That is the same silent-divergence chain the read gated F2 on, with the test that would break it still missing.
Fix: One test beside the existing one, same shape: a process row whose `path` stem is not in the sequence and whose `topic` is, asserting `sort_key(row, sequences)[1]` is the topic's index rather than the list's length. Two lines.

## F12 — observation
Claim: Two of the seven branches the read's F5 named are absent from the fix directive's item 6 and remain untested.
Location: bin/rulestore/store.py:192 (`MemoryRowSource.named_queries_text`); bin/rulestore/named_queries.py:56-62 (`sequences`'s `len(blocks) >= 2` guard)
Evidence: Verified by reading and by grep. F5's Fix listed a missing file, a missing heading, a section with one block where two are expected, blank lines in a block, a name split across two lines, `MemoryRowSource.named_queries_text()`, and the process-row sort gap. Item 6 lists six of these plus the sort test and drops two. `grep -rn named_queries_text bin/tests/` returns one hit, the F1 guard, which calls it on `FileRowSource`; no test calls `MemoryRowSource.named_queries_text()`, so the method that exists to let the processing layer be tested without the disk is itself never exercised. `grep -n '## Sequence' bin/tests/test_rulestore.py` returns three documents, each with either zero or two blocks; the one-block case, where `process_block` falls back to `[]` and the process band silently loses its order, has no test.
Consequence: Nothing today. Both are small and both are latent, and the item's six branches are the ones that carry the failure the package was gated on. Recorded because F5 is being closed against the directive's list rather than the read's, and the difference should be visible to whoever decides F5 is finished rather than discovered by the next reader who greps for it.
Fix: Two assertions in `TestNamedQueries`, the same two lines each as the six that are there. Not required for this package.
Related: F11

## F13 — observation
Claim: The F1 guard hard-codes 9, 11 and 12, so adding a role to the bundle list now reddens the unit suite — where `process/named-queries.md` says a new role is "a new line here and a new value on `role`; the tool does not change".
Location: bin/tests/test_rulestore.py:659-665; process/named-queries.md:37-39
Evidence: Verified by reading. The guard asserts `len(topic_positions) == 9`, `len(process_positions) == 11` and `len(bundles(text)) == 12` against the real document, which today parses to exactly those. Adding a thirteenth bundle line — the documented way to add a role — makes the third assertion fail; adding a position line to either sequence block fails the first or second.
Consequence: The document's own claim that adding a role touches nothing but the document is now false: it touches the document and this test. That is a small tax and it is the price of the guard, which is worth paying — an assertion that the counts are non-zero would not have caught the fence substitution, because the substitution took them to zero and a later one might take them to a wrong non-zero. Recorded so the coupling is known before someone adds a role and reads the red as a defect in their change.
Fix: None required. If the tax is unwanted, assert the shape rather than the census — that both sequence blocks are non-empty and that every bundle name in the list is a `role` value `--keys` reports — which keeps the guard against an unparsed document and survives a new role. Say either way in `process/named-queries.md`, so the "the tool does not change" sentence is true as written.
Related: F10

## What this pass does constrain

Stated so the boundary is legible rather than implied. Every behavioural claim above was
produced by running, in the assigned worktree at 02722aa, under the sandbox: the real
`process/named-queries.md` parsed through `FileRowSource` and `named_queries`; the real
chief-of-staff bundle selected and rendered directly through `FileRowSource`, `select`,
`pull_definitions` and `render`, and its rule band decomposed run by run; `sort_key`
against constructed process rows on both branches; `bin/release` run end-to-end and once
per refusal against nine purpose-built repositories (the table is in the skepticism pass);
the probe script re-run whole; and the committed `Decision:` line compared as a string
against the directive's fenced text. The closure judgments were made item by item against
the fix directive's sentences and, behind each, the Fix sentence of the finding it
answers. Not established: that the 13 commits are each individually green — the suite was
run once, at the tip; that `bin/release` behaves against a remote it must reach over a
network; or that anything outside the eleven changed files is unaffected beyond what the
701-test run asserts.

## Evidence run

`bin/tests/run` in the assigned worktree at
`$TMPDIR/fiducial-bundle-tool-followup-reread`, sandboxed:

    Ran 701 tests in 196.002s
    OK (skipped=7)

The same 701 and the same skip count as `bin/tests/green-run-rulestore-followup.log` as
this diff overwrites it (`Ran 701 tests in 196.572s` / `OK (skipped=7)`), so the log is
accurate and it is the reproduction rather than the log that this pass cites. The 701 is
the read's 682 plus a net 19, counted from the diff. Full output:
`$TMPDIR/reread-suite-run.log`.
