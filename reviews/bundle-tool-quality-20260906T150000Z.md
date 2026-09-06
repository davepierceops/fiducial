# Review: bin/rulestore/ and bin/bundle — bundle-tool-quality-20260906T150000Z

Verdict: changes-required
Verdict (quality): changes-required
Reviewed: bin/rulestore/, bin/bundle, bin/tests/test_rulestore*.py, bin/tests/test_bundle_cli.py, bin/tests/helpers.py, bin/tests/red-run-rulestore.log, bin/tests/green-run-rulestore.log @ 70bfd12d5dc25d1386252f63c6d1fa890ce919f1
Baseline: origin/main @ a5d60506d1d1266d8685f498662f514d49e12136
Reviewer: reviewer-agent (execution session, sandboxed)
Date: 2026-09-06
Scope: the whole diff a5d6050..70bfd12 — 18 files, +3777/-996: the seven modules of `bin/rulestore/`, the rebuilt `bin/bundle`, the four new test files, the additive `bin/tests/helpers.py` fixtures, the red and green run logs, the deleted `bin/tests/test_bundle_audience.py`, and the two directive files. Read as one pass over the whole change (R1047). The suite was run in this worktree; the tool was run against the real store and against purpose-built temporary repositories.
Cross-checked: docs/cycles/bundle-tool-tests-20260906T110000Z.md § INTERFACE CONTRACT and § ACCEPTANCE CRITERIA @ 70bfd12; docs/cycles/bundle-tool-coder-20260906T130000Z.md @ 70bfd12; decisions/log.md @ a00deba — DEC-000400, DEC-000410, DEC-000420, DEC-000440, DEC-000460, DEC-000490; bin/tests/test_cross_cutting.py and bin/tests/helpers.py @ 70bfd12; process/review-artifact.md @ 70bfd12.
Not inspected: `bin/aimeta/` (untouched by this diff, and out of the change's reach); the deleted `test_bundle_audience.py`'s 40 assertions, read only for what their removal costs the count; the retired `bin/bundle` @ 70b58ba beyond the header lines the contract carries forward; the 467 rows of the real store as content — they were used as data for the probes, not reviewed; performance and concurrency, neither of which the contract states. The skepticism pass and its probes are `reviews/bundle-tool-skeptic-20260906T150000Z.md`; findings raised there are not repeated here.
Findings: 3 blocking, 6 non-blocking
Dave should inspect: Q1 and Q2, because both are test-versus-contract disagreements the Coder could not resolve alone under DEC-000440 — the fix touches a test file, so it needs your ruling on which side is right.

## Verdict (quality): changes-required

The suite is genuinely strong where it reaches: 86 tests, a clean red gate, real git
throughout, in-memory rows for every processing test, and a package that honours the
storage boundary in its own structure. The change is well made. It is gated
`changes-required` on three defects that produce wrong output or a stack trace against
the store as it stands today, two of which are the contract and the test disagreeing
with each other rather than the Coder making a mistake.

## Q1 — blocking
Claim: A definition whose term is a phrase is not pulled when the selected row's body wraps the phrase across a line break, so three real rows in the store lose a definition today.
Location: bin/rulestore/terms.py:20 (`_term_pattern`)
Evidence: Verified by running. `reviews/bundle-tool-skeptic-probes-20260906T150000Z.py` probe (d), over `FileRowSource` on this worktree's real store: 467 rows, 78 definitions, 98 multi-word terms. `process/change-flow.md` uses "spec branches" across a wrap and does not pull R0004; `process/retro.md` uses "command block" across a wrap and does not pull R0208; `process/spec-test-suite.md` uses "decomposition doc" across a wrap and does not pull R0055. Single-line control cases pull correctly, and whole-word matching itself is right — `rowdy` and `rows` do not pull `row`.
Consequence: A bundle reaches an agent using a term whose definition was silently omitted — precisely the failure DEC-000420 exists to prevent. The three rows are all `process/` documents, which are hard-wrapped prose, so the defect concentrates exactly where multi-word terms and wrapped text meet. Nothing in the output says a definition was dropped.
Fix: Build the pattern from the term's words joined by `\s+` rather than escaping the term whole: `r"(?<!\w)%s(?!\w)" % r"\s+".join(re.escape(w) for w in term.split())`. Add a test in `TestPullDefinitions` whose selected body carries the phrase across a `\n`.
Related: S2

## Q2 — blocking
Claim: `--keys` computes its census from `rules/` rows alone, so it misreports the store it claims to be computed from (AC-RS-3).
Location: bin/bundle:104 (`cmd_keys`), constrained by bin/tests/test_bundle_cli.py:249-250
Evidence: Verified by running. `keys_in_use` over the 456 rule rows against `keys_in_use` over all 467 rows of this worktree's real store: 16 key-value counts are understated — `role=chief-of-staff` 173 against 180, `session=decision` 277 against 288, `corpus=software` 275 against 284, and thirteen more. The filter is what makes `test_ac_rs_3_keys_lists_every_key_value_with_its_count` pass: the fixture's `process/change-flow.md` carries `role: [writer, critic]`, so the whole store would give `role=writer 3` where the test asserts `role=writer 2`.
Consequence: AC-RS-3 states the census is computed from the store at invocation, and DEC-000490 with AC-RS-15 puts `process/` documents in that store and makes them selectable by the same query. A query author reads counts from `--keys` that do not match what `--where` returns. Today no key-value pair vanishes entirely, but that is contingent: a `process/` document carrying a value no rule carries — a new `topic` on a template — would be invisible to the census while remaining queryable, which is the drift AC-RS-3's "computed, never maintained" wording exists to prevent. The exclusion carries no comment in `cmd_keys`, so a reader cannot tell it is deliberate.
Fix: Drop the `row.kind == "rule"` filter and amend the fixture assertion to `role=writer 3`. If rules-only is genuinely intended, AC-RS-3 should say so and `cmd_keys` should carry the sentence explaining why. Either way it is a test change, so under DEC-000440 it is the decision session's ruling, not the Coder's.

## Q3 — blocking
Claim: A single malformed row makes `bin/bundle` exit 1 with a Python traceback in every mode, instead of naming the offending row and key on one line.
Location: bin/bundle:104, 113, 130 (each `FileRowSource(root).rows()` call, none guarded); bin/rulestore/store.py:86, 102 (`RowShapeError`)
Evidence: Verified by running. A temporary repository holding one row whose `order` reads `twenty`: `bundle --keys` exits 1 with `rulestore.store.RowShapeError: R0001: order: not an integer: 'twenty'` on a full traceback; `bundle --near x` the same. `--where` exits 2 in that repository only because the sync refusal fires before the read — in a synced repository it reaches the same unguarded call (inferred by reading, not run: constructing a synced repository with a malformed row was not attempted).
Consequence: `RowShapeError` was built to carry the row id and the key so a defect is locatable without the file in hand (`store.py:29-42`); a traceback throws that away and reports a Python internal instead. The repo's own convention is that no CLI ever tracebacks — `helpers.no_traceback` is asserted for every CLI in AC-X-4, AC-X-6 and AC-X-7 — and the interface contract says a refusal is "one line on stderr". The suite cannot catch this: `test_rulestore_store.py` asserts `RowShapeError` is raised from `FileRowSource` directly, and no CLI test puts a malformed row in the fixture store.
Fix: Wrap the three `FileRowSource(...).rows()` calls in `main` (or in each `cmd_*`) in `except store.RowShapeError as exc: return refuse("refused: %s" % exc)`, and add a CLI test whose fixture store carries a row with `order: twenty`.

## Q4 — non-blocking
Claim: The tool's definition predicate is narrower than DEC-000420's: it tests for a `term` key and no `role` key, where the decision says a `term` key and no role, session, or corpus key.
Location: bin/rulestore/terms.py:16 (`is_definition`); the same wording in the contract at docs/cycles/bundle-tool-tests-20260906T110000Z.md § INTERFACE CONTRACT, and in bin/tests/test_rulestore.py:347
Evidence: Verified by running. Over the real store: 79 rows carry `term`; 78 satisfy DEC-000420's shape and the same 78 satisfy the tool's; the sets are identical today, and the one excluded row (R0241) carries both `term` and `role`. So the divergence is latent, not live. The drift entered at the contract — the tests directive itself notes "the 78 definition rows that carry `term` and no role, session, or corpus" and then states the predicate as "a `term` key and no `role` key".
Consequence: A future definition row keyed to a session or a corpus but not to a role would be treated as a definition by the tool and as an ordinary row by the decision, and would be pulled into bundles that never selected it. Nothing today exercises the difference, so nothing would go red when it starts to.
Fix: Bring `is_definition` and the contract to DEC-000420's wording — `term` present and none of `role`, `session`, `corpus` — and add the two-row case to `TestPullDefinitions`. If the narrower predicate is preferred, DEC-000420 needs a superseding entry rather than a silent divergence (R0183: two sources disagree; this one is surfaced rather than reconciled).

## Q5 — non-blocking
Claim: `bin/bundle` reaches its own package through `importlib.import_module` for the sole purpose of keeping a static scan green, which removes the code that does the work from the graph that scan reads.
Location: bin/bundle:29-38
Evidence: Verified by reading, confirmed by running. The comment states the reason: `test_cross_cutting.py`'s `LOCAL_MODULES` allowlist names only `aimeta`, and editing that test is not this package's to do (DEC-000440). Confirmed against `test_cross_cutting.production_files()`, which covers every file directly under `bin/` plus `bin/aimeta/*.py` and no subpackage — so `bin/rulestore/` is outside AC-X-1, AC-X-2 and AC-X-7 entirely. `bin/rulestore/terms.py:11` imports `rulestore.query` with a plain `from`, which would fail AC-X-2 if the package were scanned.
Consequence: AC-X-2 still passes and now proves less: `bin/bundle`'s real dependency is invisible to it, and the 700 lines of new production code it depends on are scanned by nothing. The workaround was the right call inside the Coder's remit; leaving it in place is not.
Fix: Add `rulestore` to `LOCAL_MODULES` and `bin/rulestore/*.py` to `production_files()` in a follow-up package, then restore plain `import rulestore.query` in `bin/bundle`. Until then the indirection should not be read as evidence that the package is stdlib-only — `bin/tests/test_rulestore_boundary.py:146` checks that separately, and does pass.
Related: S1

## Q6 — non-blocking
Claim: The three modes disagree about what "the store" is: `--keys` sees rules only, `--where` and `--near` see rules and process documents.
Location: bin/bundle:104 against bin/bundle:113 and bin/bundle:130
Evidence: Verified by reading, with the census difference verified by running under Q2. `cmd_near` and `cmd_where` pass `FileRowSource(root).rows()` whole; `cmd_keys` filters on `row.kind`. `cmd_near` also prints `row.id`, which for a process row is the path stem, where `render` heads the same row with its full path — so `--near` and the bundle name the same document two different ways.
Consequence: A reader cannot form one mental model of the store from the tool's three modes. `--near` reporting `change-flow` where the bundle says `process/change-flow.md` is a small thing on its own and a confusing one next to Q2.
Fix: Settle on one row set for all three modes when Q2 is ruled, and have `--near` print the same label `render._heading` uses.

## Q7 — non-blocking
Claim: The typed-value defect is detected only on bare scalars, never on the elements of a bracketed list.
Location: bin/rulestore/store.py:91-103 (`normalize_fields`)
Evidence: Verified by running. `weight: 12` raises `RowShapeError`; `weight: [12]` returns `{'weight': ['12']}`; `weight: [12, true]` returns `{'weight': ['12', 'true']}`; `flag: yes` raises, `flag: [yes]` does not. The bracket branch returns before `TYPED_SCALAR_RE` is ever consulted.
Consequence: AC-RS-1 says any typed value other than `order` is a defect. Bracketing one hides it, so the intake check the row shape is supposed to give is one keystroke away from silence. No row in the store does this today.
Fix: Apply the same `TYPED_SCALAR_RE` test to each unquoted element of the list branch, and add the case to `TestRowShape`.

## Q8 — non-blocking
Claim: `--name` is interpolated into the output path without normalization, so a name containing `../` writes outside `--out`.
Location: bin/bundle:142-146
Evidence: Verified by reading. `dest = out_dir / ("fiducial-bundle-%s-%s.md" % (bundle_name, generated))`; `pathlib` does not normalize, so `--name ../escaped` yields `<out>/fiducial-bundle-../escaped-<ts>.md`, which resolves into `<out>`'s parent. Not run against the real command — the effect is a pure path join and reading it is sufficient evidence for a non-blocking entry.
Consequence: On a local developer tool with a name the user typed themselves, the blast radius is a file written one directory up. It matters because `--out` reads as a containment promise and is not one.
Fix: Reject a `--name` containing a path separator or `..`, refusing on the same exit-2 path as a malformed query.

## Q9 — non-blocking
Claim: Of the five places the Coder's report says the tests "left room", the suite constrains two, constrains one only by accident, and leaves two open.
Location: bin/tests/test_bundle_cli.py, bin/tests/test_rulestore_store.py
Evidence: Verified by reading the four test files whole and by running the suite. Taking them in the order the review directive names them:

- **The `--keys` census excluding process rows.** Not left open — actively required. `test_ac_rs_3_keys_lists_every_key_value_with_its_count:249` asserts `role=writer 2`, which is only true with process rows excluded. The suite constrains the behaviour and constrains it against AC-RS-3. This is Q2.
- **The refusal-check ordering.** Left open. `cmd_where` checks a malformed query, then a dirty tree, then sync, then an empty selection; the contract states the first three in that order and the tests assert each refusal in isolation, never two conditions at once. Any ordering would pass. The order implemented happens to match the contract's sentence, so nothing is wrong — it is simply unasserted.
- **The repo label from `remote.origin.url`.** Left open. `test_ac_rs_6_the_header_stamps_repo_head_generated_and_the_rows:154` asserts only that some line starts with `- Repo: `. Against the fixture's local bare origin the label comes out as a pair of temp-directory segments; against a GitHub remote it comes out `davepierceops/fiducial`. Neither is asserted.
- **The importlib load.** Left open by this suite and covered nowhere. This is Q5.
- **The process row's id as the path stem.** Constrained. `test_ac_rs_15_a_process_document_carries_its_path_and_stem_id:106` asserts `row.id == "change-flow"` directly. What is not constrained is what happens when that stem equals a rule id, which the skepticism pass takes up.

Consequence: The two genuinely open places — refusal ordering and the repo label — are low-consequence, and a test for each would be cheap. Naming them matters more than fixing them: the green run should not be read as evidence for behaviour nothing asserts (R0111).
Fix: Add a test asserting the malformed-query message wins over a dirty tree, and one asserting the `Repo:` label's shape for a remote of a known form. Neither needs to block.

## What the suite does constrain

Stated so the boundary of the pass is legible rather than implied (R0110). The
processing tests do build every row in memory and touch no file — AC-RS-4's behavioural
half holds as written. The red gate is real: 86 failures, 86 `AssertionError`s, zero
import or attribute errors, verified against the log in the skepticism pass's probe (a).
The CLI tests run the command as a subprocess against a real bare origin plus a clone,
so the sync refusal and the blob SHA are tested against git rather than against a mock —
the convention `bin/tests/helpers.py` establishes and this suite follows. The
`helpers.py` additions are purely additive, so no pre-existing test's fixtures moved.
Ordering, the missing-key non-match, the `None`-order rule, the threshold boundary, the
`## Human` exclusion for the exact heading, and the process document's interleaving are
each asserted directly.

## Evidence run

`bin/tests/run` in the assigned worktree, sandboxed:

    Ran 657 tests in 169.051s
    OK (skipped=7)

Identical to `bin/tests/green-run-rulestore.log`'s summary. The 657 is the Test
Designer's 697 baseline less the 40 tests of the deleted `test_bundle_audience.py`;
the arithmetic was checked, not assumed. Full output: `$TMPDIR/review-suite-run.log`.
