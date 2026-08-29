# Review: specs/directive-tooling-trd.md — cycle 2

Verdict: changes-required
Reviewed: specs/directive-tooling-trd.md @ 8ab21dd
Reviewer: Spec Reviewer Agent (execution session)
Date: 2026-08-28
Scope: convergence confirmation — the full TRD read against the test suite on
branch `directive-tooling-trd` (`bin/tests/test_directive.py`,
`bin/tests/test_check_directive.py`, `bin/tests/test_directive_trd.py`, and
`bin/tests/helpers.py`, each read whole), on the single question whether every
testable claim the TRD makes has a test asserting it and every test asserts
something the TRD states; plus confirmation that each of the round-1 decision
record's twelve dispositions is reflected in the text as ruled. Three claims
were re-run rather than read: the invariants fixture against §3.3's new
"invariants document's own format" subsection (`invariants_sections()` returns
exactly the 21 sections §3.3 names, 17 region and 4 lint, rendered as `##`
headings with no third level, the three ATX-bodied sections accounting for the
24 rendered `##` lines the first-non-blank-line-is-body rule exists for); §3.6
M2's mechanism steps, each verified against a purpose-built repository
(`cat-file -t` returns `tag` for an annotated tag and `commit` for a lightweight
one; `cat-file -e <sha>^{commit}` and `diff-tree --root` both peel the annotated
tag, so the unpeeled type step is load-bearing; `--root` is required for a root
commit; `git log -1` returns a *different* ancestor for a non-touching citation);
and the region counts against both §3.3 tables (general 14 = 2 author + 12
committed; cycle 16 = 2 author + 14 committed; every row enumerated, cycle rows
9–15 corresponding to general regions 6, 7 and 9–13).
Cross-checked: bin/tests/test_directive.py; bin/tests/test_check_directive.py;
bin/tests/test_directive_trd.py; docs/cycles/directive-tooling-trd-conv1-20260828T1745.md
(the round-1 decision record); bin/tests/helpers.py; bin/cycle-open;
skills/review-artifact.md; the branch's diff against `main` @ 79228c0.
Not inspected: `specs/directive-tooling.md` itself — the PRD is confirmed
unedited on this branch (`git diff --name-only 79228c0..HEAD`), and the three
recorded PRD riders are out of scope by directive; the pre-existing suite's own
correctness beyond its exit state; `bin/tests/test_cycle_open.py`,
`bin/tests/test_cross_cutting.py` and the other eleven pre-existing modules
except where a TRD integration point names them; `bin/tests/red-run-*.log` and
`bin/tests/stubs/` beyond noting that they predate the round-1 convergence;
prose quality and template conformance, this cycle being coherence-scoped; and
the round-1 executor's three disclosed judgment calls **as such** — no report
artifact carrying them exists in the repository, so their content could not be
matched item-for-item against the text (the directive fixes them as standing
as delivered, and every disposition they attach to is confirmed landed below).
Findings: 3 blocking, 5 cycle-1 observations dispositioned, 1 deferred note.
Prior cycle: reviews/directive-tooling-trd-cycle-1.md
Dave should inspect: F-1 — Q5 is ruled and the TRD carries the ruling, but the
two tests that would assert it are still skipped as though it were open, and
round 1's write scope forbade touching them. Whether that edit belongs to the
implementer or to a third convergence round is a call this cycle cannot make.

## Verification runs

- `bin/check-frontmatter --all` — **exit 0**. `NOTE in-scope: [scope-summary] 55
  file(s) matched, from 12 configured glob(s)`.
- `bin/tests/run` — **573 tests, 8 failures, 138 errors, 9 skipped**, exit 1.
  573 = the 424 pre-existing tests plus the three new modules' 149. **Every
  failure and error is inside the three new modules** (`test_check_directive`
  89, `test_directive` 41, `test_directive_trd` 16 reported entries, subtests
  counted separately); no pre-existing module reports a failure, an error, or a
  collection problem, so the 424 are green. 8 of the 9 skips are
  `test_directive_trd`'s skip-with-reason set (confirmed by running that module
  alone: `Ran 22 tests … failures=6, errors=10, skipped=8`); the ninth is a
  pre-existing conditional skip. This is the expected new-module red.

## F-1 — blocking
Claim: Q5 is ruled (c) and `OQ-Q5` is gone from §9, but `test_directive_trd.py`
still skips both Q5 tests on the ground that the question is open and cites a
TRD entry that no longer exists — so neither testable consequence of the ruling
is asserted by any running test.
Location: `bin/tests/test_directive_trd.py:5`, `:57-63`, `:400`, `:420`;
against `specs/directive-tooling-trd.md:340-351`, `:373`, `:398-403`, and §9.
Evidence: **Verified by running.** `grep -n "OQ-Q5" specs/directive-tooling-trd.md`
returns nothing; §9's only near-neighbour is `OQ-5`, a different question (the
PRD's "plus" clause). `python3 -m unittest tests.test_directive_trd` reports
`skipped=8`, and `SKIP_Q5` — "PRD §8 Q5 … is open; TRD OQ-Q5 recommends (c)" —
decorates `test_q5_route_and_model_are_substituted_into_a_committed_region` and
`test_q5_the_element_set_stays_at_eight`. The module docstring's §9 list at `:5`
names `OQ-Q5` alongside the three genuinely open questions.
Consequence: the ruling's two mechanical consequences — that `ROUTE AND MODEL`
is classified **committed** in the manifest, keeping AC-DT-18's author count at
two, and that the element set stays at eight with route and model in AC-DT-08's
unchecked set — have no running assertion behind them. An implementer who put
route and model in a third author slot, or added a ninth element, would clear
the suite; those are exactly the two shapes the ruling rejected, and exactly the
two the skipped tests were written to catch. The skip reason also misreports the
document a reader is sent to, which is how a ruled question gets re-opened by a
later session reading the tests.
Fix: remove `@unittest.skip(SKIP_Q5)` from both tests and delete `SKIP_Q5` — the
two then join the module's expected reds rather than its skips — and correct the
module docstring's §9 list at `:5` to `(OQ-Q2, OQ-Q4, OQ-Q6)`.
Related: F-3.

## F-2 — blocking
Claim: §3.3's "Cycle mode's region 5 is a committed region an author writes
into" names a row its own table makes the `WORKING-TREE DISPOSITION` **author**
region; the paragraph describes `## Decisions`, which the Q5 ruling's insertion
of `ROUTE AND MODEL` at row 2 moved to row 6.
Location: `specs/directive-tooling-trd.md:420-429`, against the cycle-mode table
at `:372-387`.
Evidence: **Verified by running**, parsing the table out of the document: cycle
row 5 is `` `WORKING-TREE DISPOSITION` `` | **author region**, row 6 is
`` `Decisions` (heading) `` | `§Decisions`. The neighbouring subsection written
in the same round has the post-insertion numbering right — `:452` places
`Decisions`, `Deferred` and `Execution notes` at "rows 6, 7 and 8 of the cycle
table" — which is what identifies `:420` as the one cross-reference the
insertion left behind rather than a second numbering scheme.
Consequence: read literally, the sentence says the disposition slot is a
committed region, which contradicts the table, contradicts §3.3's own
"Sixteen regions: two author, fourteen committed", and contradicts
`test_ac_dt_18_exactly_two_author_regions_cycle_mode`, which asserts cycle
mode's author entries are exactly the label and `Execution notes`. An
implementer taking the prose over the table classifies one region wrongly and
reds AC-DT-18 for cycle mode; one taking the table over the prose is left with
a paragraph about the manifest over-reading the generator-supplied share that
appears to be about the wrong region.
Fix: change "region 5" to "region 6" at `:420`.

## F-3 — blocking
Claim: five test docstrings still argue from the pre-convergence TRD, each
stating that the document says something the round-1 dispositions changed;
round 1's write scope — the TRD plus one named test — could not reach them.
Location: `bin/tests/test_directive.py:756-759` and `:387`;
`bin/tests/test_check_directive.py:374`, `:454`, and `:535`.
Evidence: **Verified by reading**, each against the amended text.
(a) `test_directive.py:756-759` says "Expected red against the TRD's current
design: §3.3's cycle-mode region table has no route-and-model region, and states
so — 'general mode's region 2, `ROUTE AND MODEL`, has no counterpart either'";
the cycle table's row 2 **is** `ROUTE AND MODEL` (`:373`), `:393` states the
correspondence outright, and `grep -n "counterpart"` finds the quoted sentence
only in its surviving form about `TASK` (`:396`).
(b) `test_check_directive.py:374` says the annotated-tag test is written "to
AC-DT-09 as agreed, not to TRD §3.6's mechanism", because an annotated tag SHA
satisfies that mechanism; F-A1 added the unpeeled `cat-file -t` step (`:715-726`)
precisely so it does not — verified by running, `cat-file -t` returns `tag`.
(c) `test_check_directive.py:454` says "the TRD names no other" induceable form
of a failed git read and that it is "Recorded as a finding"; F-A7 named the
class and two further members at §3.6 step 5 and FM-L5.
(d) `test_directive.py:387` says "§3.6 says elsewhere that it runs over the
lint's source too; F-8"; §3.6 now states the opposite in bold — "AC-DT-02's scan
walks the generator's source and nothing else".
(e) `test_check_directive.py:535` attributes the unchecked status of route and
model to `OQ-Q5`, which §9 no longer carries.
Consequence: in every case the *assertion* agrees with the amended TRD — no test
would change verdict — so this is a defect in the record rather than in the
behaviour. What it costs is the thing the convergence pass exists to produce: a
reader who opens the tests to learn what the TRD decided is told, in five
places, that it decided the reverse, and three of the five present a closed
question or a discharged finding as still live. (a) is the sharpest, because it
quotes a sentence that no longer exists as though it were the current design.
Fix: rewrite the five docstrings to the amended text — (a) to state that row 2
carries the region and the criterion is discharged by the cycle emission, (b) to
state that the test and §3.6's object-type step now agree, (c) to name the class
§3.6 step 5 fixes, (d) to drop the F-8 clause, (e) to drop the `OQ-Q5` citation.
Related: F-1.

## Round-1 dispositions — all twelve confirmed landed

- **F-A10 + Q5, ruled (c)** — cycle table row 2 is `ROUTE AND MODEL` from
  `§Route and model` (`:373`); M5's preamble list carries the entry and states
  one list serves both modes (`:786-799`), matching `invariants_sections()`'s
  `Preamble markers` block; `OQ-Q5` is removed, not marked closed; both modes
  carry the region and AC-DT-14's clause is discharged by the cycle emission
  (`:398-403`); the lint checks neither value (`:340-351`). Landed in the TRD;
  see F-1 and F-3(a) for the test-side residual.
- **F-A1** — §3.6 M2 gains the object-type step before the touch test, with the
  lightweight-tag bound and "only an annotated tag is rejectable" stated
  (`:715-726`); the fixture builds an annotated tag (`helpers.py:1134`). PRD
  unedited.
- **F-A2** — the marker beginning the statement's own region does not precede it,
  stated as the general rule rather than as a list entry (`:774-785`);
  `FIRST ACT` is absent from the preamble list.
- **F-A3** — §3.3's "The invariants document's own format" subsection is present
  and matches `invariants_sections()` exactly: 21 sections, `##` headings, no
  third level, the first-non-blank-line-is-body rule, §3.4's three parts plus
  the sole-tree sentence in one `## Disposition label` section, and
  `## Match phrases` with blocks for M1, M4, M5, M6, M7 and none for M2, M3, M8.
- **F-A4** — a committed region's marker line is the first line of its committed
  section body, and an author region's marker is out of AC-DT-02's reach
  (`:471-486`).
- **F-A5** — §3.6 step 4 scopes the read to committed content with FM-L7 as
  FM-G3's analogue and the Q9 reason in one sentence; FM-L7 is in §6's lint
  table and `invariants-dirty` in §7's code table, with §7's exit-2 row naming
  it. The named test is rewritten and renamed to
  `test_fm_l7_the_lints_read_is_scoped_to_committed_content`.
- **F-A6** — §4.1 states the M2 and M8 substitutions and why `omit=` cannot build
  them; `citation_fixtures` and `DT_M8_FAILING_NAMES` instantiate both.
- **F-A7** — §3.6 step 5 names the unknown class as "a git read that fails for a
  reason the lint cannot attribute to the directive", maps it to
  `element-unknown` and exit 1, and draws the boundary against
  `citation-unresolvable`; FM-L5 restates it. PRD unedited.
- **F-A8** — §6 opens with AC-DT-04's clause discharged by the input set, and
  places the enforceable half on the lint's G4 posture. PRD unedited.
- **F-A9** — §4.1 states that both helper changes land with the implementation
  and that `make_home_repo` is the additive test-side form; `helpers.py:792`
  carries it with that reason in its docstring.
- **F-A11** — cycle row 1 names both marker forms, and the following paragraph
  states how AC-DT-05's partition and AC-DT-18's counts read identically under
  each.
- **The four removal categories and the frontmatter** — no provenance tags, no
  changelog prose, no question marked closed (`OQ-Q5` is absent, not annotated),
  no per-citation SHAs; frontmatter is exactly `status: draft`,
  `last-reviewed: null`, `audience: [human]`.

## Cycle-1 observations — disposition, one line each

- **O-1 — survives.** `:36-37` still reads "the ninth and tenth executables in
  `bin/`" / "existing eight", and `:1146` and `:1489` still say "eight", while
  `bin/` holds seven executables and `CLI_NAMES` six; no convergence edit touched
  the count.
- **O-2 — survives.** The "144-file" corpus and the 63/46 timestamp split are
  still stated in the TRD's present tense at `:241`, `:954`, `:1171` and `:1514`.
- **O-3 — survives, now honestly represented.** §3.4 still calls
  `WORKING-TREE DISPOSITION (exclusive assignment):` "the form a decision session
  writes today", but `test_the_space_spelled_label_variant_does_not_match` pins
  the decision with the corpus cost named in its own docstring, so the cost is
  now carried by a test rather than only by a review.
- **O-4 — survives, and reaches the fixture.** §3.9's "What moves" still omits
  `bin/cycle-open:126`'s `- <item> — <where it is tracked>` and `:130`'s
  `<constraints on how edits are made, if any>`; §3.3 makes `§Deferred` and
  `§Execution notes` their marker lines and nothing else, and
  `invariants_sections()` follows, so the two lines are dropped from the cycle
  skeleton rather than moved — a change to AC-CO-3's output that no test in the
  new modules or in `test_cycle_open.py` asserts either way.
- **O-5 — mooted.** F-A11 gave cycle row 1 both marker forms and a paragraph
  stating how the counts and the partition read under each.

## Deferred — one line, no Fix

- `bin/tests/red-run-with-stubs.log` and `red-run-no-stubs.log` are the red-gate
  evidence as of `fb8e536`, before the round-1 convergence; they carry the
  superseded `OQ-Q5` skip reasons and are a record of that run, not a claim
  about this one.
