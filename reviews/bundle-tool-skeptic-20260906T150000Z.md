# Review: bin/rulestore/ and bin/bundle — bundle-tool-skeptic-20260906T150000Z

Verdict: changes-required
Verdict (skepticism): changes-required
Reviewed: bin/rulestore/, bin/bundle, bin/tests/test_rulestore*.py, bin/tests/test_bundle_cli.py, bin/tests/helpers.py, bin/tests/red-run-rulestore.log, bin/tests/green-run-rulestore.log @ 70bfd12d5dc25d1386252f63c6d1fa890ce919f1
Baseline: origin/main @ a5d60506d1d1266d8685f498662f514d49e12136
Reviewer: skeptic-risk-agent (execution session, sandboxed)
Date: 2026-09-06
Scope: the whole evidence chain, not the diff alone — the tests directive's interface contract and acceptance criteria, the coder directive, the red run log, the green run log, the code, and the five places the Coder's report says the tests "left room". Every claim below that says "verified by running" was produced by `reviews/bundle-tool-skeptic-probes-20260906T150000Z.py`, committed beside this artifact and re-runnable from the repository root with no arguments.
Cross-checked: decisions/log.md @ a00deba — DEC-000400, DEC-000410, DEC-000420, DEC-000440, DEC-000460, DEC-000490; bin/tests/test_cross_cutting.py and bin/tests/helpers.py @ 70bfd12, for what the pre-existing AC-X-* scans still cover; process/review-artifact.md @ 70bfd12.
Not inspected: the 40 assertions of the deleted `bin/tests/test_bundle_audience.py`, beyond confirming the 697-to-657 arithmetic; `bin/aimeta/`; any behaviour of the real `~/Downloads` default, which no probe wrote to; the tool under concurrent invocation; anything about performance. The quality pass and its findings are `reviews/bundle-tool-quality-20260906T150000Z.md`; findings raised there are not repeated here.
Findings: 1 blocking, 8 non-blocking
Dave should inspect: S1, the one blocking finding — the green suite is actively concealing a violated acceptance criterion rather than merely failing to cover one, and the fix is a one-line fixture change whose consequence is a test that starts failing. Then S2 and S9: S2 because it is your rationale that leaks when it goes wrong, and S9 because the drift it names entered through the one document the review chain does not gate.

## Verdict (skepticism): changes-required

The honest answer to "where is this lying to us" is: not in the red gate, and not in the
sync refusal. Both are exactly what they claim, and the probes confirmed both rather than
taking the logs' word for it. The lying is at the edges. One finding is blocking: three
pre-existing acceptance criteria went vacuous for `bin/bundle` in this commit, hiding a
behaviour that violates one of them, and nothing went red (S1) — verification weakened to
fit an implementation, which R0460 forbids. The other eight are gaps rather than defects:
guarantees whose enforcement is a convention (S2), a scan that catches the obvious
spellings and not the others (S3), three row shapes the store will accept and mishandle
in silence (S4), and a green run of 657 tests that licenses a claim narrower than "the
rule-store tool works" (R0111, R0783). The gate is `changes-required` on S1 alone; the
rest are for triage, not for the ship call (R1094).

## Probe results, one line each

The directive names six probes. Each is a section of the committed script; this is what
each returned in this worktree.

- **(a) the red-gate** — PASS. Five sampled tests across four files and four modules each
  failed on an `AssertionError` raised inside its own test file, on a substantive claim
  about the stub's wrong behaviour. Whole log: 86 `FAIL`, 0 `ERROR`, 86 `AssertionError`.
- **(b) the storage boundary** — FAIL. AC-RS-4 is asserted by an AST scan that a
  processing module can pass while reading the store; see S3.
- **(c) the sync refusal** — PASS. Level-and-clean writes exactly one file and exits 0;
  equal-but-dirty, one commit ahead, and one commit behind each exit 2 with one line on
  stderr and nothing written.
- **(d) definitions by term** — FAIL. Whole-word matching is correct (`rowdy` and `rows`
  do not pull `row`; `row-by-row` does); a phrase whose occurrence wraps a line break is
  not matched, and three real rows lose a definition because of it. Carried as Q1 in the
  quality pass.
- **(e) the header** — NOTE. Every blob is the blob at `HEAD`; every body is the working
  tree's file. See S5.
- **(f) the untouched cases** — FAIL. All four misbehave: a `rules/` file with no
  frontmatter is accepted silently, a quoted comma inside a list is torn in two, a
  `### Human` heading publishes the human form, and a rule/process id collision goes
  unguarded. See S2 and S4.

A seventh probe, **(g)**, was not asked for and is reported because it changes what the
green run means: see S1.

## S1 — blocking
Claim: `bundle --keys` and `bundle --near` exit 0 in silence outside a git repository, violating AC-X-4, and three cross-cutting tests that should catch it cannot, because the argv they run `bundle` with now dies at argparse.
Location: bin/tests/helpers.py:52 (`CLI_MINIMAL_ARGS["bundle"] = ["base"]`); bin/bundle:50-54 (`_repo_root`), bin/bundle:103-115
Evidence: Verified by running, probe (g). `bundle base` in a non-repository exits 2 with `bundle: error: one of the arguments --where --keys --near is required` — argparse, before any repository, file or encoding work. The comment above `CLI_MINIMAL_ARGS` says its purpose is "minimal argv that gets each CLI past argparse"; for `bundle` it no longer does, and the old bundle's positional `base` argument no longer exists. With a live argv: `bundle --keys` outside a repository exits 0 with empty stdout and empty stderr, as does `bundle --near anything`. AC-X-4 requires 2 or 3. `_repo_root` falls back to `pathlib.Path.cwd()` when `git rev-parse` fails, and `FileRowSource` finds no `rules/` directory there, so the tool reports an empty store as though the store were empty.
Consequence: Three acceptance criteria went quietly vacuous for this CLI in one commit — AC-X-4 (clean failure outside a repository), AC-X-6 (no traceback with an undecodable document present) and AC-X-7 (no dependence on the platform default encoding) all run `bundle` with the same stale argv and all now stop at argparse. Nothing went red, so nothing announced the loss. Separately, the underlying behaviour is wrong: a user who runs `bundle --keys` from the wrong directory is told the store has no keys rather than that there is no store.
Fix: Set `CLI_MINIMAL_ARGS["bundle"] = ["--keys"]`, and make `_repo_root` refuse — exit 2, one line — when `git rev-parse --show-toplevel` fails, rather than falling back to the cwd. Expect AC-X-4 to go red on the fixture change before the `_repo_root` fix lands; that redness is the finding.
Related: Q5

## S2 — non-blocking
Claim: The `## Human` exclusion holds only for that exact string at that exact heading level, so one wrong heading level publishes a row's human form into a rendered bundle.
Location: bin/rulestore/store.py:26 (`HUMAN_MARKER`), bin/rulestore/store.py:128-136 (`_split_human`)
Evidence: Verified by running, probe (f3). A `rules/` row whose rationale sits under `### Human` instead of `## Human` parses to `human=None` and a body of `'The obligation.\n\n### Human\n\nDEC-000999: the rationale nobody should see.'`; `render.render` on that row emits `DEC-000999` into the bundle. `_split_human` compares `line.strip() == "## Human"` and has no other test. Nothing leaks today: a scan of `rules/` and `process/` finds 68 rows carrying a Human section and every one of their headings is exactly `## Human`.
Consequence: AC-RS-14 and G4 are the two-forms-one-row guarantee — the human form is rationale written for Dave, and it is never rendered to an agent. The guarantee is enforced by one string comparison against handwritten Markdown across 456 rule files and 11 process documents. A typo, a heading level nudged during an edit, or a row written by a session that remembered the section but not its level, and the rationale ships. Nothing in the pipeline would notice: the body is non-empty, the row selects normally, and the render carries whatever the body holds. No test covers a mis-levelled heading, and `test_ac_rs_14_no_human_content_reaches_the_bundle` asserts only `"## Human" not in text`, which a `### Human` body satisfies while carrying the content.
Non-blocking because the store as it stands has no mis-levelled heading and the code meets AC-RS-14 for the input the contract specifies; raised because the guarantee has no mechanism behind it, only a convention 68 files currently happen to keep.
Fix: Match any ATX heading whose text is `Human` — `re.match(r"^#{1,6}\s+Human\s*$", line)` — and add a store test with `### Human` asserting `human` is populated and `body` is not. A check that no row body contains the word `Human` under any heading, run at intake, would close it at the source.

## S3 — non-blocking
Claim: AC-RS-4 is enforced by a scan a processing module can pass while reading the store, so the storage boundary is asserted rather than guaranteed.
Location: bin/tests/test_rulestore_boundary.py:35-41, 87-144
Evidence: Verified by running, probe (b). A candidate `query.py` of six lines — `import rulestore.store`, a constant built as `("rul" "es/", "proc" "ess/")`, and `def leak(root): return rulestore.store.FileRowSource(root).rows()` — passes every one of the module's eight checks: it imports no module in `FORBIDDEN_IMPORTS`, contains neither literal in `STORAGE_PATHS`, has no `ImportFrom` node for `names_imported_from_store` to inspect, calls none of the file-opening names, and imports nothing outside stdlib plus `rulestore`. The two weaknesses are independent: `names_imported_from_store` reads only `ast.ImportFrom`, so `import rulestore.store` is invisible to it; and the path check is a substring scan over source text, so string concatenation defeats it, as would renaming either store root — at which point `test_ac_rs_4_store_is_the_only_module_that_names_a_storage_path` fails on `store.py` rather than catching anything.
Consequence: DEC-000410's purpose is substitution — replacing the filesystem-backed store should touch one layer. The scan as written does not prevent a later session from reaching around the boundary; it prevents the two most obvious spellings of doing so. The current package is clean — every processing module passes on its merits, not by evasion — so this is a guarantee about the future, not a defect in the present, and the release impact is `deferred`. It matters because the boundary test is the only thing standing between DEC-000410 and ordinary convenience.
Fix: Add `ast.Import` to `names_imported_from_store` so any reference to the storage module is caught whatever its spelling, and assert that no processing module references the name `FileRowSource` at all. Treat the `STORAGE_PATHS` substring scan as a smoke check rather than the guarantee, and say so in the module docstring.

## S4 — non-blocking
Claim: Three shapes the store can hold today are handled wrongly and silently: a `rules/` file with no frontmatter, a list value with a comma inside quotes, and an id collision between a rule and a process document's path stem.
Location: bin/rulestore/store.py:107-125 (`_parse_frontmatter`), bin/rulestore/store.py:91-99 (the list branch of `normalize_fields`), bin/rulestore/store.py:170 (`row_id = fields.get("id") or path.stem`) with bin/rulestore/terms.py:26-34
Evidence: Verified by running, probe (f1, f2, f4).

- **No frontmatter.** `rules/R0777.md` holding only prose returns `id='R0777'`, `keys={}`, `order=None`. `_parse_frontmatter` returns `({}, text)` when the first line is not `---`, and the id falls back to the path stem. The row counts toward the store, is unselectable by any key, and carries the whole file including any `---`-less header as its body. AC-RS-1 says every file under `rules/` parses to an id, a non-empty body, and a dictionary, and that a value the dialect cannot type is a defect; a file with no dictionary at all raises nothing.
- **A quoted comma.** `topic: ["a, b", c]` normalizes to `{'topic': ['"a', 'b"', 'c']}` — split on every comma before quotes come off, so the quoted value is torn in two and both halves keep a quote character. The scalar branch handles quotes correctly (`note: "one, two"` gives `['one, two']`), which makes the list branch's behaviour a genuine inconsistency rather than a documented limit.
- **An id collision.** A `process/R0001.md` alongside `rules/R0001.md` produces two rows sharing `id='R0001'`. Both select. `pull_definitions` builds `already = {row.id for row in selected}` and dedupes `pulled` by `definition.id`, so a definition whose id equals a colliding stem is suppressed from a bundle that needed it; `--near` prints an ambiguous first column; and the render heads one `## R0001` and the other `## process/R0001.md`, so the bundle reads coherently while the pull did not.

Consequence: Each is a silent wrong answer rather than a crash, which is the worse failure mode for a tool whose output an agent then acts on. None is triggered by the store as it stands — the probe had to construct all three — so the release impact is `deferred`: non-blocking today, and a defect the tool will not announce on the day it arrives. Intake is the only thing standing between the store and all three.
Fix: Raise `RowShapeError` when a `rules/` file has no frontmatter block, naming the path. Split the list branch on commas outside quotes rather than on every comma. Make `FileRowSource.rows()` raise on a duplicate id across the two roots, or key the row's identity on its path and carry `id` as a label — the second is the larger change and the more honest one.

## S5 — non-blocking
Claim: A row's `blob` is the blob at `HEAD` while its `body` is the working tree's file, and only the `--where` refusal keeps the two consistent.
Location: bin/rulestore/store.py:155-182 (`_blob` runs `git rev-parse HEAD:<path>`; `_row` runs `path.read_text`)
Evidence: Verified by running, probe (e). After an uncommitted edit to `rules/R0001.md`, `row.blob` still names the committed blob `f2a2ac1…` while the working-tree file hashes to `0e4e87a…` and `row.body` reads `'AN UNCOMMITTED EDIT.'`.
Consequence: For the written bundle the gap is closed, and closed correctly: `cmd_where` refuses on any uncommitted change under `rules/` or `process/` before it reads. For any other caller of `FileRowSource` it is open, and the header's promise — that a blob identifies the content beside it — does not hold. One narrow hole remains in the guard itself: `_dirty_under` runs `git status --porcelain -- rules process`, which respects `.gitignore`, so an ignored file under `rules/` is invisible to the dirty check while `FileRowSource`'s glob picks it up.
Fix: Read the body from `git show HEAD:<path>` so the row is wholly a `HEAD` object, or drop `blob` for callers who did not pass the sync check. At minimum, state in `store.py`'s docstring that the two fields come from different revisions.

## S6 — non-blocking
Claim: The green log is the Coder's own capture of its own run, and the review directive treats it as evidence without an independent reproduction being required.
Location: bin/tests/green-run-rulestore.log
Evidence: Verified by running. The log's paths name `/private/tmp/claude-501/fiducial-bundle-tool-coder`, the Coder's worktree, and it records `Ran 657 tests in 160.964s` / `OK (skipped=7)`. An independent run in this review's worktree returned `Ran 657 tests in 169.051s` / `OK (skipped=7)` — the same counts, so the log is accurate. The 657 was checked rather than assumed: the Test Designer's 697 baseline less the 40 tests of the deleted `test_bundle_audience.py`.
Consequence: The claim stands this time. It stands because it was reproduced, not because the log says so, and the distinction should survive into the next package: a committed log is a record of a run, not verification of one (R0157).
Fix: None needed. Noted so the reproduction, not the log, is what the decision session cites.

## S7 — non-blocking
Claim: At its default threshold `--near` is a near-exact-match lookup, not a similarity search, and no `process/` document can be returned by it at any realistic query length.
Location: bin/rulestore/near.py:19-34 (`_jaccard`, `near`)
Evidence: Verified by running. Jaccard divides by the union, so a query of n words scores at most n/m against a body of m words. Median normalized word-set size in the real store is 16 words for a rule and 250 for a process document, with process bodies ranging 140 to 594 words; reaching 0.3 against the smallest of them needs a 42-word query every word of which appears in that document. Four natural queries were run against the whole store — including the one the Coder's manual run used, "read governed text before emitting anything it governs". Each returned exactly one hit, the row whose own text the query was, scoring 1.00, 0.58, 0.44 and 1.00; in every case the second-nearest row scored 0.12 to 0.25 and was dropped. `bin/bundle --near "read governed text before emitting anything it governs"` prints one line, `R0180 1.00`.
Consequence: `--near` is a discovery aid, not a gate, so a weak measure costs a user a missed row rather than a wrong bundle — and AC-RS-5 says only "at or above threshold", which the implementation meets exactly. What is worth saying is that the tool answers a narrower question than its name suggests: it finds the row you have already quoted, and it will never surface a process document. The 0.3 in the contract has no stated basis, so a later session tuning it is not defending a decision.
Fix: None required for AC-RS-5. If `--near` becomes load-bearing, normalize by the shorter of the two word sets rather than by the union, and let `--threshold` reach the command line so the number stops being invisible.

## S8 — non-blocking
Claim: `_synced_with_main` treats a failed fetch as a successful one, so the tool can pass its own freshness check against a stale ref.
Location: bin/bundle:78-84
Evidence: Verified by reading. `_git(root, "fetch", "-q", "origin", "main")`'s return code is discarded; the comparison that follows reads whatever `origin/main` the local repository already had. Not run — reproducing it needs a network failure the sandbox does not offer, so this is inferred by reading and stated as such.
Consequence: Offline, or with a remote that rejects the fetch, `bundle --where` compares `HEAD` against a possibly weeks-old `origin/main` and reports success. The refusal exists so that a bundle is reproducible from the ref in its header; a stale comparison gives the same header for a store that has moved. The failure is quiet, which is what makes it worth naming — the observable behaviour is a bundle that writes normally.
Fix: Refuse when the fetch exits non-zero, with a message distinguishing "could not reach origin" from "HEAD is not synced".

## S9 — non-blocking
Claim: The interface contract, not the implementation, is where DEC-000420 was narrowed, and the same document is the tests' spec — so the drift was un-catchable by the process that was supposed to catch it.
Location: docs/cycles/bundle-tool-tests-20260906T110000Z.md § INTERFACE CONTRACT (`terms.py`) and § COMPANIONS
Evidence: Verified by reading. The COMPANIONS section instructs the Test Designer to note "the 78 definition rows that carry `term` and no role, session, or corpus"; the INTERFACE CONTRACT four paragraphs later states "a definition is a row with a `term` key and no `role` key". The tests were written against the contract, the code against the tests, and the green run confirms all three agree with each other and not with DEC-000420. The predicate difference is latent on today's store — verified by running: the two definitions of "definition" select the same 78 rows.
Consequence: This is the shape of drift the store exists to prevent, arriving through the one document that sits between a decision and its tests. The defect itself is Q4 in the quality pass; what belongs here is that no gate in the chain could have caught it, because every downstream artifact derived from the contract rather than from the decision.
Fix: Have the contract quote the decision it implements verbatim where it restates one, and cite it by number inline. The Spec Reviewer's coherence check reaches spec-to-test; nothing reaches decision-to-contract.
Related: Q4

## Boundary of this pass

Stated because omitting it is how an unbounded claim gets made by accident. Everything
above rests on: the committed probe script, run once in this worktree under the sandbox;
one full `bin/tests/run`; and reading. No probe touched a network, a real `~/Downloads`,
or the tool under concurrency. The claim "the sync refusal is real" covers exactly four
repository states — level-and-clean, equal-but-dirty, one ahead, one behind — built with
real git in a temporary directory; it does not cover a detached HEAD, a repository with
no `origin`, a fetch that fails, or a `main` that has diverged rather than moved, and
S8 is the one of those that was reasoned about rather than run. The claim "the red gate
is real" covers five of 86 tests read from the log plus the log's aggregate counts; the
other 81 were not read individually.
