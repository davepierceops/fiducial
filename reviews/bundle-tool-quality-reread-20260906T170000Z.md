# Review: bin/bundle and bin/rulestore/terms.py — bundle-tool-quality-reread-20260906T170000Z

Verdict: ready-with-findings
Verdict (quality): ready-with-findings
Reviewed: bin/bundle, bin/rulestore/terms.py, bin/tests/test_bundle_cli.py, bin/tests/test_cross_cutting.py, bin/tests/green-run-rulestore-fix.log @ a72d9c31ed5e68809f67b965f6ceb12177b6badc
Baseline: origin/bundle-tool-review @ b73635df0097d48447118dab7b826e9a24880c83
Reviewer: reviewer-agent (execution session, sandboxed)
Date: 2026-09-06
Scope: a diff-scoped re-read, not a second full read. Only the diff b73635d..a72d9c3 — 6 files, +241/-9: the four fixes in `bin/bundle` and `bin/rulestore/terms.py`, the one amended assertion in `bin/tests/test_bundle_cli.py`, the `CLI_MINIMAL_ARGS` override in `bin/tests/test_cross_cutting.py`, the added green log, and the fix directive. The one question asked of each of Q1, Q2, Q3 and S1: does it close as its Fix stated, and does the fix introduce anything the first read would have flagged. The suite was run in the assigned worktree; each fix was exercised against the real store or against a purpose-built temporary repository.
Cross-checked: reviews/bundle-tool-quality-20260906T150000Z.md and reviews/bundle-tool-skeptic-20260906T150000Z.md @ a72d9c3 — the four Fix statements this pass judges against; docs/cycles/bundle-tool-fix-20260906T160000Z.md @ a72d9c3 — what the Coder was told; reviews/bundle-tool-skeptic-probes-20260906T150000Z.py @ a72d9c3 — probes (d) and (g); bin/tests/helpers.py and bin/tests/test_directive_trd.py @ a72d9c3, read only for what the `CLI_MINIMAL_ARGS` placement reaches; process/review-artifact.md @ a72d9c3.
Not inspected: every non-blocking finding of the first read — Q4 through Q9 and S2 through S9 — which stay open in their artifacts for a later package and were not re-opened here; all six other files of `bin/rulestore/`, unchanged by this diff; the 456 rule rows and 11 process documents as content, used as data for the checks rather than reviewed; the deleted `test_bundle_audience.py`; performance and concurrency, neither of which the contract states. The skepticism half of this re-read is `reviews/bundle-tool-skeptic-reread-20260906T170000Z.md`; findings raised there are not repeated here.
Findings: 0 blocking, 2 non-blocking, 1 observation
Dave should inspect: Q11, because the fix directive waived Q3's test on a premise that is false — probe (f) does not exercise a malformed row through the CLI, so the refusal this package added is asserted by nothing. And Q10, which is the ruling you are owed on where `CLI_MINIMAL_ARGS["bundle"]` belongs.

## Verdict (quality): ready-with-findings

All four blocking findings close. Each was checked by running the fixed tool rather
than by reading the diff for intent: Q1 against the three real rows the first read
named, Q2 against the sixteen counts it named, Q3 against a malformed row in a clean
synced repository — which is the case the first read could only infer — and S1 from a
directory outside any repository, in every mode. The changes are minimum-change and
carry no collateral: the term pattern adds exactly three matches across the whole store
and no others, and the `--keys` census gains the eleven process rows without gaining or
losing a line.

Nothing here is blocking. Two things should not stand. The `CLI_MINIMAL_ARGS["bundle"]`
override sits in `test_cross_cutting.py` while the canonical table in `helpers.py` still
reads `["base"]` — a follow-up rather than a defect in the fix, for the reasons Q10
gives, but a follow-up whose absence would restore exactly the vacuity S1 was raised
about. And Q3's refusal path has no test, because the fix directive waived Q3's own test
clause by pointing at a probe that does not cover it.

## Closure of the four blocking findings

### Q1 — a phrase term across a line break — CLOSED

*The Fix, as stated:* build the pattern from the term's words joined by `\s+` rather
than escaping the term whole, and add a test in `TestPullDefinitions` whose selected
body carries the phrase across a `\n`.

*What the diff did:* `bin/rulestore/terms.py:20-21` now reads
`words = r"\s+".join(re.escape(word) for word in term.split())`, used in the same
`(?<!\w)…(?!\w)` frame. Character-for-character the Fix's first clause. No test was
added — the fix directive's item 1 named the probe script's (d) case as the confirmation
and told the Coder to add no tests beyond item 2's one edit, so the second clause was
countermanded by the directive rather than dropped by the Coder.

*Closed, and why.* Verified by running, in the assigned worktree against the real store:
`terms.pull_definitions` now returns R0004 for `change-flow` on `spec branches`, R0208
for `retro` on `command block`, and R0055 for `spec-test-suite` on `decomposition doc` —
the three rows the first read named as losing a definition today. Synthetic cases also
run: the phrase pulls on one line, wrapped at the space, wrapped with a following
indent, across two spaces, and for a three-word term; it does not pull for `specdelta`,
so whole-word matching survives the change.

*Collateral, checked rather than assumed.* Over all 467 rows against all 78 definitions,
the new pattern matches exactly three (row, definition, term) triples the old pattern
missed — the three above — and no others. The change adds nothing and removes nothing
else. The absent test is noted as coverage, not as a defect: it is the directive's
call, and unlike Q3 the behaviour it would assert is exercised by the committed probe.

### Q2 — the `--keys` census — CLOSED

*The Fix, as stated:* drop the `row.kind == "rule"` filter and amend the fixture
assertion to `role=writer 3`. Ruled by Dave on 2026-09-06 under DEC-000440 in favour of
censusing both kinds.

*What the diff did:* `bin/bundle:106-111` — `cmd_keys` now passes
`FileRowSource(root).rows()` whole to `keys_mod.keys_in_use`; the list comprehension is
gone. `bin/tests/test_bundle_cli.py:249` asserts `role=writer 3`, and the docstring on
line 241 now says the census covers the whole store. No other assertion moved.

*Closed, and why.* Verified by running, against the real store in the assigned worktree:
the census now covers 467 rows rather than 456, and all sixteen key-value counts the
first read named as understated now report the whole-store figure — `role=chief-of-staff`
180 (was 173), `session=decision` 288 (was 277), `corpus=software` 284 (was 275), and
thirteen more. `bin/bundle --keys` prints 862 lines. `cmd_where` and `cmd_near` already
read the whole store, so all three modes now agree on what the store is, which is the
larger half of Q6 settled as a side effect.

*One note, not a finding.* The amended docstring at `test_bundle_cli.py:241` is 127
characters, the longest line in that file. Nothing lints it and the suite is green; it
is recorded because it is the only place in the diff where the fix is wider than the
file's own habit.

### Q3 — a malformed row — CLOSED (behaviour); see Q11 (coverage)

*The Fix, as stated:* wrap the three `FileRowSource(...).rows()` calls in
`except store.RowShapeError as exc: return refuse(...)`, and add a CLI test whose fixture
store carries a row with `order: twenty`.

*What the diff did:* `bin/bundle:38-39` binds `store_mod` so the exception type is
reachable; each of the three call sites — `cmd_keys` at 107, `cmd_near` at 119,
`cmd_where` at 140 — is wrapped and refuses with `refused: %s` on the exception. A grep
for `FileRowSource` in `bin/bundle` returns exactly those three call sites and the
import binding, so no call site is left unguarded. No test was added; the fix directive's
item 3 said to add none.

*Closed, and why.* Verified by running. A temporary repository was built with a bare
origin and a clone level with it, its `rules/R0001.md` carrying `order: twenty`,
committed — so the tree is clean and `HEAD` equals `origin/main`, and `--where` reaches
the read rather than stopping at the sync refusal. That is the case the first read could
only infer. All three modes:

    $ bundle --keys                                  exit 2   refused: R0001: order: not an integer: 'twenty'
    $ bundle --near obligation                       exit 2   refused: R0001: order: not an integer: 'twenty'
    $ bundle --where topic=core --name q3 --out …    exit 2   refused: R0001: order: not an integer: 'twenty'

One line on stderr in each, carrying the row id and the key as `RowShapeError` was built
to; no traceback; nothing written to `--out`. The `--where` line is the observation the
first read said it had not made.

The coverage half of the Fix is not closed, and the reason it was waived does not hold.
That is Q11.

### S1 — outside a repository — CLOSED

*The Fix, as stated:* set `CLI_MINIMAL_ARGS["bundle"] = ["--keys"]`, and make
`_repo_root` refuse — exit 2, one line — when `git rev-parse --show-toplevel` fails,
rather than falling back to the cwd.

*What the diff did:* `bin/bundle:51-57` — `_repo_root` returns `None` on a non-zero
`rev-parse`, with a docstring saying so; `main:165-167` refuses with
`refused: not inside a git repository` before dispatching to any mode, so the guard
covers every mode including any added later. `bin/tests/test_cross_cutting.py:39-44`
sets `CLI_MINIMAL_ARGS["bundle"] = ["--keys"]` with a four-line comment naming S1 and its
artifact.

*Closed, and why.* Verified by running, from a temporary directory confirmed to be
outside any repository (`git rev-parse --show-toplevel` exits 128 there). `--keys`,
`--near anything` and `--where topic=core --name s1 --out …` each exit 2 with the single
line `refused: not inside a git repository`, no traceback, and nothing written to `--out`
or to the working directory. AC-X-4 requires 2 or 3, so the criterion is met
substantively rather than by argparse. `--help` still exits 0 with a usage block, so
AC-X-3 is untouched. AC-X-4, AC-X-6 and AC-X-7 now run `bundle` with a live argv and
reach the tool's repository, file and encoding handling.

The placement of the `CLI_MINIMAL_ARGS` override is Q10, and it is a follow-up, not a
defect in this fix.

## Q10 — non-blocking
Claim: The `CLI_MINIMAL_ARGS["bundle"]` correction was written as a module-level mutation in `test_cross_cutting.py`, leaving the canonical table in `helpers.py` still reading `["base"]` under a comment that says it gets each CLI past argparse — which for `bundle` it does not.
Location: bin/tests/test_cross_cutting.py:39-44; bin/tests/helpers.py:47-57 (`CLI_MINIMAL_ARGS`, `"bundle": ["base"]` at line 52)
Evidence: Verified by running. `from tests.helpers import CLI_MINIMAL_ARGS` alone yields `['base']`; importing `tests.test_cross_cutting` afterwards yields `['--keys']`, and `CLI_MINIMAL_ARGS is tcc.CLI_MINIMAL_ARGS` is `True` — the override mutates the shared dictionary object, not a local copy. The committed probe script reads the table from `helpers.py` source text and still reports `helpers.CLI_MINIMAL_ARGS['bundle'] = ["base"]` beside its own quotation of that comment. `bundle base` run outside a repository against the fixed tool still exits 2 at `bundle: error: one of the arguments --where --keys --near is required`, before any repository work — so the stale entry still buys a vacuous pass for AC-X-4. The only other importer, `test_directive_trd.py:307`, tests membership (`assertIn(name, CLI_MINIMAL_ARGS)`) and never a value, so nothing observes the stale entry today; the three consumers of the values are all in `test_cross_cutting.py`, at lines 134, 232 and 307.
Consequence: `helpers.py` is where a reader looks for each CLI's minimal argv, and for one CLI it now states a value its own comment's contract rules out. The correction survives only as long as `test_cross_cutting.py` is the module that imports and mutates the table: move the AC-X tests, run a module in isolation, or add a fourth consumer elsewhere, and `bundle` silently returns to the argv that dies at argparse — with AC-X-4 still green, because argparse also exits 2. That is S1's failure mode restored by one edit, and nothing would announce it. It is a live wrongness in a canonical table rather than a wrong behaviour: the suite is green and the three criteria genuinely reach the tool today.
Fix: Set `"bundle": ["--keys"]` in `bin/tests/helpers.py:52` and delete the override and its comment from `test_cross_cutting.py`, keeping the comment's substance in `helpers.py` beside the entry. The judgment this pass was asked for: **this is a follow-up, not a defect in the fix.** The Coder was told, in item 4 of the fix directive, to make the edit in `test_cross_cutting.py`; S1's own Location names `helpers.py:52`, so the directive misnamed the file and the Coder complied with the instruction it was given rather than substituting its own. Under DEC-000440 a Coder does not widen a test edit past what a directive rules, the effect S1 required is achieved and verified, and the override is documented rather than silent. What makes it a follow-up that must actually be taken, rather than a stylistic preference, is that the canonical table is now false and the correction is import-order dependent.
Related: S11

## Q11 — non-blocking
Claim: The refusal Q3 added is asserted by no test, and the evidence the fix directive substituted for Q3's own test clause does not exist — probe (f) covers four other shapes and never puts a malformed row through the CLI.
Location: docs/cycles/bundle-tool-fix-20260906T160000Z.md § TASK item 3; reviews/bundle-tool-skeptic-probes-20260906T150000Z.py:449-538 (`probe_f`); bin/bundle:107-108, 119-120, 140-141
Evidence: Verified by reading and by running. Item 3 says "Add no test; the store fixture test for RowShapeError already exists, and the CLI behaviour is confirmed by the probe script's (f) case." `probe_f` was read whole: its four sub-probes are f1 a `rules/` file with no frontmatter, f2 a comma inside quotes, f3 a `### Human` heading, f4 a rule/process id collision. None constructs a typed-value defect, none invokes `bin/bundle`, and the probe script's summary line for (f) names those four shapes and not a malformed row. Running the committed probe script in this worktree confirms it: the (f) section prints f1 through f4 and nothing about `order: twenty`. The first read's own words on Q3 still hold verbatim — "The suite cannot catch this: `test_rulestore_store.py` asserts `RowShapeError` is raised from `FileRowSource` directly, and no CLI test puts a malformed row in the fixture store" — and this package changed neither of those files.
Consequence: The three `try/except` blocks are the whole of the guarantee that a malformed row produces a locatable one-line refusal rather than a traceback, and nothing will redden if a later session removes one, adds a fourth `FileRowSource` call site, or changes `RowShapeError`'s message. The waiver was reasonable on its face and rested on a false premise, so the decision session ruled on a coverage question it was told was already answered. The behaviour itself is right — this pass verified all three modes by running — so what is lost is the regression, not the fix.
Fix: Add one CLI test to `bin/tests/test_bundle_cli.py` whose fixture store carries a row with `order: twenty`, asserting exit 2, one line on stderr containing the row id and the key, no traceback, and nothing written — the test Q3's Fix asked for. Cheap, and it closes the sentence the first read wrote about this exact hole.

## Q12 — observation
Claim: Joining a term's words with `\s+` matches across any run of whitespace, a blank line included, so a phrase whose halves straddle a paragraph break now pulls a definition.
Location: bin/rulestore/terms.py:20-21 (`_term_pattern`)
Evidence: Verified by running. Over the real store, every one of the 467 bodies against every multi-word term of the 78 definitions: three matches are added by the fix and zero of them span a `\n\n`. Constructed directly, a body of `"a spec\n\ndelta"` does match the term `spec delta`, because `\s+` does not stop at a line boundary.
Consequence: A definition can be pulled on an occurrence that is not one — the last word of a paragraph and the first word of the next, read as a phrase. The cost is a definition present in a bundle that did not need it, which is the benign direction of the two: Q1's defect was a definition silently absent, and DEC-000420 exists to prevent that one. No row in the store does this today.
Fix: None required, and none recommended without a reason: `[^\S\n]+\n?[^\S\n]*` would confine the match to a single wrap at the cost of a pattern nobody will read correctly later. Recorded so that the widening is a known property of the fix rather than a surprise the day a body straddles.

## Evidence run

`bin/tests/run` in the assigned worktree at `$TMPDIR/fiducial-bundle-tool-reread`,
sandboxed:

    Ran 657 tests in 168.539s
    OK (skipped=7)

The same 657 and the same skip count as `bin/tests/green-run-rulestore-fix.log`, which
records `Ran 657 tests in 163.757s` / `OK (skipped=7)` from the Coder's worktree. The
count is unchanged from the first read's run, as it should be: this package added no
test. Full output: `$TMPDIR/reread-suite-run.log`.
