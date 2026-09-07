# Review: bin/bundle and bin/rulestore/terms.py — bundle-tool-skeptic-reread-20260906T170000Z

Verdict: ready-with-findings
Verdict (skepticism): ready-with-findings
Reviewed: bin/bundle, bin/rulestore/terms.py, bin/tests/test_bundle_cli.py, bin/tests/test_cross_cutting.py, bin/tests/green-run-rulestore-fix.log @ a72d9c31ed5e68809f67b965f6ceb12177b6badc
Baseline: origin/bundle-tool-review @ b73635df0097d48447118dab7b826e9a24880c83
Reviewer: skeptic-risk-agent (execution session, sandboxed)
Date: 2026-09-06
Scope: the evidence for the four closures, not the closures as reported. Only the diff b73635d..a72d9c3. The committed probe script was re-run whole; then each of the three cases the re-read directive names was constructed here and run against the fixed tool rather than read from the Coder's report — Q1's line-wrapped phrase through `pull_definitions`, Q3's `order: twenty` row in a purpose-built repository across all three modes, and S1's every mode from a directory outside any repository. Every "verified by running" line below was produced in the assigned worktree under the sandbox. Nothing in the Coder's report was taken as evidence for anything.
Cross-checked: reviews/bundle-tool-quality-20260906T150000Z.md and reviews/bundle-tool-skeptic-20260906T150000Z.md @ a72d9c3 — the Fix statements judged against; reviews/bundle-tool-skeptic-probes-20260906T150000Z.py @ a72d9c3, read whole for probes (d), (f) and (g); docs/cycles/bundle-tool-fix-20260906T160000Z.md @ a72d9c3; bin/tests/helpers.py @ a72d9c3; process/review-artifact.md @ a72d9c3.
Not inspected: the eight non-blocking findings of the first skepticism pass — S2 through S9 — which are not re-opened here and stay open in their artifact; Q4 through Q9 likewise; the six unchanged files of `bin/rulestore/`; the network, `~/Downloads`, concurrency, and a failed fetch, none of which this diff touches and none of which the sandbox offers. The quality half of this re-read is `reviews/bundle-tool-quality-reread-20260906T170000Z.md`; findings raised there are not repeated here.
Findings: 0 blocking, 3 non-blocking
Dave should inspect: S12, because the wrong directory a user is actually in is another repository, not no repository, and that case still exits 0 in silence. Then S10, because the committed probe script — the review chain's one re-runnable artefact — now reports that Q1 did not land and that AC-X-4 is still violated, and both are false.

## Verdict (skepticism): ready-with-findings

Where is this lying to us, now that the four are reported closed? Not in the fixes. All
four were reconstructed here from scratch and all four hold, including the two cases the
first read could only infer: `--where` reaching an unguarded read in a clean synced
repository, and every mode outside a repository. The lying is again at the edges, and
this time one piece of it is the review chain's own evidence.

Three things. The committed probe script reports two falsehoods when run against the
fixed tree, because both were written as static text rather than computed (S10). The
`CLI_MINIMAL_ARGS` correction lives in the consuming test module while the canonical
table still carries the value that made AC-X-4 vacuous, so the vacuity is one refactor
away and would return green (S11). And S1's stated Fix closed the case AC-X-4 tests
while leaving the case a user will actually hit — a git repository that is not the rule
store — exiting 0 with empty stdout (S12). None is blocking: the four Fix statements are
each satisfied as written, and the gate is not a place to re-litigate what the fix
directive scoped.

## Probe results, one line each

`python3 reviews/bundle-tool-skeptic-probes-20260906T150000Z.py`, re-run whole in the
assigned worktree at `$TMPDIR/fiducial-bundle-tool-reread`, sandboxed. Full output:
`$TMPDIR/reread-probes-after.log`. The script's own summary, then what it actually shows.

- **(a) the red-gate** — PASS, unchanged. The red log is untouched by this diff.
- **(b) the storage boundary** — FAIL, unchanged and expected: S3 is non-blocking and out
  of this package's scope.
- **(c) the sync refusal** — PASS, unchanged. Level-and-clean writes one file and exits 0;
  ahead, behind and dirty each refuse with exit 2 and one line. The Q3 guard added to
  `cmd_where` did not disturb the ordering of the refusals ahead of it.
- **(d) definitions by term** — the script prints FAIL; the fix landed. Its three
  `pull_definitions` cases all now return `['R0902']` — one line, wrapped at the space,
  two spaces — where the first read recorded the wrapped case not pulling. Its real-store
  section still prints "3 real rows … missed" because that section re-implements the old
  pattern inline instead of calling `terms.pull_definitions`; it cannot observe the fix.
  See S10.
- **(e) the header** — NOTE, unchanged: blob is `HEAD`'s, body is the working tree's. S5,
  out of scope.
- **(f) the untouched cases** — FAIL, unchanged: no frontmatter accepted, quoted comma
  torn, `### Human` leaks, id collision unguarded. All four are S2 and S4, out of scope.
  Note for the record that (f) contains **no** malformed-row case and never invokes
  `bin/bundle`; the fix directive cited it as Q3's confirmation and it is not one.
- **(g) the pre-existing scans** — the script prints PASS, and its computed verdict is
  right while its printed prose is not. `bundle --keys` and `bundle --near anything`
  outside a repository now both exit 2 with `refused: not inside a git repository`, so
  `acx4_violated` is false and the verdict flips to PASS. The lines printed underneath
  still assert "Both modes exit 0 in silence", and the summary line still reads "AC-X-4 is
  violated"; both are static strings. g1 also still reports
  `helpers.CLI_MINIMAL_ARGS['bundle'] = ["base"]`, which is true and is S11. g3 is
  unchanged: `bin/rulestore/` remains outside every AC-X static scan (Q5, out of scope).

## The three cases the directive names, constructed here

**Q1 — a phrase across a line break.** Built directly against `terms.pull_definitions`
with a definition row carrying `term: [spec delta]`. Observed: `"While a spec delta is
open"` pulls; `"While a spec\ndelta is open"` pulls; `"While a spec\n   delta is open"`
pulls; `"While a spec  delta is open"` pulls; a three-word term wrapped pulls;
`"A specdelta is not a phrase."` does not, so whole-word matching survives. Against the
real store's 467 rows, `pull_definitions` now returns R0004 for `change-flow`, R0208 for
`retro`, and R0055 for `spec-test-suite` — the three rows the first read named. Sweeping
all 467 bodies against all 78 definitions, the new pattern adds exactly those three
matches and no others.

**Q3 — a malformed row.** A bare origin and a clone level with it, built with real git in
a temporary directory, its `rules/R0001.md` carrying `order: twenty` and committed — so
`git status --porcelain` is empty and `HEAD` equals `origin/main`, which is what makes
`--where` reach the read instead of stopping at the sync refusal. Observed, each mode:

| mode | exit | stderr | lines | traceback | written |
|---|---|---|---|---|---|
| `--keys` | 2 | `refused: R0001: order: not an integer: 'twenty'` | 1 | no | — |
| `--near obligation` | 2 | `refused: R0001: order: not an integer: 'twenty'` | 1 | no | — |
| `--where topic=core --name q3 --out …` | 2 | `refused: R0001: order: not an integer: 'twenty'` | 1 | no | nothing in `--out` |

The row id and the key both survive into the message, which is what `RowShapeError` was
built to carry and what the traceback threw away.

**S1 — outside any repository.** A temporary directory in which `git rev-parse
--show-toplevel` exits 128. Observed: `--keys`, `--near anything`, and
`--where topic=core --name s1 --out …` each exit 2 with the single line `refused: not
inside a git repository`, no traceback, nothing written to `--out` and nothing created in
the working directory. `--help` still exits 0 with a usage block, so AC-X-3 is intact.
AC-X-4 requires 2 or 3 and now gets it from the tool rather than from argparse.

## S10 — non-blocking
Claim: Run against the fixed tree, the committed probe script reports that Q1 did not land and that AC-X-4 is still violated. Both are false, and both are printed rather than computed.
Location: reviews/bundle-tool-skeptic-probes-20260906T150000Z.py:373-400 (probe (d)'s real-store section); :551-586 (probe (g)'s printed prose and its `note()` text)
Evidence: Verified by running. Probe (d)'s real-store loop builds `as_written = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(term), re.I)` inline — the pre-fix pattern — and compares it against a whitespace-flattened body; it never calls `terms.pull_definitions`, so it reports the same three missed rows whatever `_term_pattern` does. Its `note()` verdict is `"FAIL" if missed else "PASS"`, so the summary line reads `(d) FAIL … 3 real rows lose a definition` against a tree where `pull_definitions` returns all three, as this pass confirmed directly. Probe (g)'s verdict is genuinely computed — `acx4_violated = bundle(outside, "--keys")[0] == 0` — and correctly flips to PASS; but the three `print` lines under g2 still say "Both modes exit 0 in silence" immediately below their own output showing exit 2, and the summary string still reads "AC-X-4 is violated by --keys/--near (exit 0 outside a repo)".
Consequence: This script is the one re-runnable artefact the review chain committed, and the fix directive told the Coder to run it before and after. A reader who runs it now is told, in the summary, that the first blocking finding is unfixed and that the fourth is unfixed — and in (g)'s case the summary contradicts the verdict on its own line. That is verification reporting a state the tree is not in, which is the failure S1 was raised about pointed the other way: there, a green test hid a defect; here, a red probe hides a fix. The next session to consult it has to read 600 lines of Python to find out which half to believe.
Fix: Have probe (d)'s real-store section call `terms.pull_definitions(selected, rows)` and report the definitions actually not pulled, so its verdict tracks the code. Derive probe (g)'s g2 prose and its `note()` text from the observed exit codes rather than stating them. Failing either, mark the script as pinned to `b73635d` in its docstring so it is read as a record of that revision rather than as a check of the current one. Not blocking: the script is a review artefact, not shipped code, and both falsehoods are visible to anyone who reads the output beside the summary.

## S11 — non-blocking
Claim: `bin/tests/helpers.py` still carries `"bundle": ["base"]`, so the argv that made AC-X-4, AC-X-6 and AC-X-7 vacuous for this CLI is still the canonical one; only a module-level mutation in `test_cross_cutting.py` keeps the three criteria substantive, and its removal would not redden anything.
Location: bin/tests/helpers.py:52; bin/tests/test_cross_cutting.py:44
Evidence: Verified by running. Importing `tests.helpers` alone gives `CLI_MINIMAL_ARGS['bundle'] == ['base']`; importing `tests.test_cross_cutting` afterwards gives `['--keys']` on the same dictionary object (`is` comparison, `True`). Probe (g1), which reads the table out of `helpers.py`'s source text, still prints `["base"]`. Against the *fixed* tool, `bundle base` outside a repository exits 2 at `bundle: error: one of the arguments --where --keys --near is required` — argparse, before `_repo_root` is ever called. AC-X-4 asserts `rc in (2, 3)` and no traceback, both of which that argparse exit satisfies.
Consequence: The substance of AC-X-4, AC-X-6 and AC-X-7 for `bundle` now depends on which module imports the table first and on `test_cross_cutting.py` continuing to be the module that mutates it. Move those tests, split the module, run one module in isolation, or add a consumer that reads the table without importing `test_cross_cutting`, and `bundle` reverts to the argv that dies at argparse — with the three criteria still green, because a vacuous pass and a real one are indistinguishable at the assertion. That is precisely the shape S1 reported, restored by an edit that would look like tidying. `test_directive_trd.py:307` is the only other importer and checks membership rather than values, so nothing today observes the stale entry — which is also why nothing would announce its return.
Fix: Move the correction to its canonical home: `"bundle": ["--keys"]` at `bin/tests/helpers.py:52`, with the comment's substance beside it, and delete the override from `test_cross_cutting.py`. Non-blocking because the three criteria genuinely reach the tool today and this pass verified the behaviour they now exercise. The judgment on whether the placement is a defect in the fix or a follow-up is stated in the quality pass.
Related: Q10

## S12 — non-blocking
Claim: S1's Fix closed the case AC-X-4 tests — no repository at all — and left the case a user will actually hit: inside a git repository that is not the rule store, `--keys` and `--near` still exit 0 with empty stdout and empty stderr.
Location: bin/bundle:51-57 (`_repo_root`), bin/bundle:165-167 (the guard in `main`)
Evidence: Verified by running. A temporary git repository was built with one commit, a `README.md`, and no `rules/` or `process/` directory. `bundle --keys` there exits 0, stdout empty, stderr empty; `bundle --near anything` the same. The guard fires only when `git rev-parse --show-toplevel` itself fails; inside any repository it succeeds, `FileRowSource` globs two directories that do not exist, and the tool reports a store of zero rows as though the store were empty. Control: run from `bin/tests/` inside the real store, `--keys` exits 0 with 862 lines, so toplevel resolution from a subdirectory is unaffected.
Consequence: S1's Consequence paragraph named two things — three acceptance criteria gone vacuous, and "a user who runs `bundle --keys` from the wrong directory is told the store has no keys rather than that there is no store". The first is closed. The second is closed for the one directory shape AC-X-4 happens to test and open for every other: a sibling checkout, another project, a submodule, the home directory if it is a repository. Silence and exit 0 is the same wrong answer the traceback of Q3 was gated for being, arriving from the more likely direction. No test covers it, and none would: AC-X-4's fixture is a non-repository by construction.
Fix: Refuse — exit 2, one line naming the directory — when the resolved root contains neither `rules/` nor `process/`, so the tool distinguishes "this is not the rule store" from "the store is empty". Non-blocking because S1's Fix was stated narrowly and is satisfied as written, and because widening it is a decision about the tool's contract rather than a correction to this package.

## Boundary of this pass

Stated because omitting it is how an unbounded claim gets made by accident. Everything
above rests on: one whole re-run of the committed probe script; one whole `bin/tests/run`
(`Ran 657 tests in 168.539s`, `OK (skipped=7)`, log at `$TMPDIR/reread-suite-run.log`);
four purpose-built probes written for this pass — the Q1 phrase cases and the real-store
sweep, the Q3 malformed row across three modes, the S1 non-repository across four
invocations, and the non-store repository of S12; and reading the diff and the two prior
artifacts. The claim "Q3 refuses in every mode" covers one malformed shape, `order:
twenty`, in one repository state, clean and synced; it does not cover two malformed rows,
a malformed row under `process/`, or a `RowShapeError` raised from a path other than
`normalize_fields`. The claim "S1 refuses outside a repository" covers one temporary
directory with no `.git` above it; it does not cover a detached `HEAD`, a repository
whose `.git` is a file, or a `git` binary absent from `PATH` — that last would take the
same refusal path and report "not inside a git repository" for a different reason, which
was reasoned about and not run. Nothing here re-examined the eight non-blocking findings
of the first pass; where a probe still reports one, it is reported as unchanged and not
re-verified.
