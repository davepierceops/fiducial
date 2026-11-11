# Review: intake/generator-hook-defects — reread2-20261111T180211Z

Verdict: ready
Reviewed: intake/generator-hook-defects @ c2b06c8
Baseline: intake/generator-hook-defects @ 9baea5a
Reviewer: reviewer-agent and skeptic-risk-agent (three passes) and spec-reviewer-agent (specs/rule-store.md hunk); wrote none of the delta
Date: 2026-11-11
Scope: `git diff 9baea5a c2b06c8 -- bin/ specs/ docs/plans/`: one line in bin/bundle (cmd_emit marks the revision for target `bundle` only), tests in bin/tests/test_bundle_cli.py, three reworded spec sentences (J1, G6, AC-RS-14), one plan amendment. Overall verdict covers the whole delta 76a6c14..c2b06c8 as it now stands. `ready` means ready for the human's ruling on the spec text, not that it is agreed.
Cross-checked: specs/rule-store.md AC-RS-12, AC-RS-15, AC-RS-16a, Failure modes; DEC-001790; my earlier artifacts reviews/generator-hook-defects-read-20261111T170619Z.md and -reread-20261111T174823Z.md.
Not inspected: process/adopt.md (another reviewer's); live `gh` or GitHub; the gitignored-file gap is carried unchanged.
Findings: 0 blocking, 2 non-blocking, 1 observation
The human should inspect: the three proposed spec sentences, and whether to leave the gitignored-file gap (N1) filed.

## Quality pass
Verdict (quality): ready
Suite run once on c2b06c8: `sh bin/tests/run` Ran 459 tests, OK. The change is one expression, `_local_head(root) if target_name == "bundle" else _head(root)`, the smallest that gives AC-RS-15. The replaced test (emit bundle unchanged by a dirty tree) is replaced by three that assert the opposite for the right reason; no other existing assertion moved.

## Skepticism pass
Verdict (skepticism): ready
Ran on a clone at c2b06c8 (/tmp/rvw/c3), explicit --out under /tmp/rvw, `--where role=writer` against `--emit bundle --where role=writer`:
- clean tree: byte-identical apart from the timestamp; header plain.
- dirty rules/R0004.md: byte-identical apart from the timestamp; both headers `<sha>+local.424ad7cb6a1d`.
- dirty bin/rulestore (generator): both headers `+local.9369443e26c4`, identical.
- dirty README.md only: both plain.
- `--emit claude-code` and `--emit codex` on the dirty tree: no file contains `+local`.
Release refusal on a dirty rule, process, README or generator file was shown in my first read (D2 matrix) and the code is unchanged.

## Continuity pass
Verdict (continuity): ready
- F1 of the re-read is resolved: AC-RS-15 ("`--emit bundle` writes the file `--where` writes, byte-identical") now holds on dirty and clean trees, and `--emit` harness targets stay unmarked, consistent with AC-RS-15's byte-stable harness tree and AC-RS-16a.
- F2 resolved: J1 and G6 name "rules, process documents or generator", which excludes README.md as the code does (README.md-only gives a plain header); AC-RS-14 defers to G6.
- F3 resolved in text: G6 now says `bin/release` refuses such a tree rather than "never carries", which is what the code does. The gitignored-file gap remains (N1).
- J4, AC-RS-12 and Failure modes were consistent at 9baea5a and are unchanged. No other sentence in specs/rule-store.md, README.md or SPEC.md is contradicted at c2b06c8.
- Test per spec claim: marker on dirty and clean, test_d3_*; `--emit bundle` equals `--where`, test_d3_emit_bundle_equals_where_on_a_clean_tree and test_d3_emit_bundle_carries_the_same_local_marker_as_where_on_a_dirty_tree; harness unmarked, test_d3_harness_emissions_are_unchanged_by_a_dirty_tree; release plain, test_d5_*; `-R`, test_c1_*; refusals, test_d2_*, test_c1_*, test_c2_*. No test asserts something the spec does not state.

## N1 — non-blocking
Claim: A gitignored rule file under rules/ reaches a release bundle with a plain header, because neither the marker nor the release check sees ignored files; G6's "refuses such a tree" is true only of non-ignored changes.
Classification: defect
Location: bin/rulestore/store.py dirty_input_paths
Evidence: ran in the first read (ignored rules/ign.md, role writer; release exit 0, text in the bundle); code unchanged; base behaves the same.
Consequence: a release can carry a row that is in no commit.
Fix: add ignored files to the status query, or state the limit; file it.

## N2 — non-blocking
Claim: DEC-001790's decision text says "where a `--where` bundle is rendered", but the code and AC-RS-15 now mark `--emit bundle` as well.
Classification: suggestion
Location: decisions/log.md DEC-001790
Evidence: read against the bin/bundle diff and the run above.
Consequence: the entry reads narrower than the behaviour. The log is append-only, so it cannot be edited.
Fix: leave it; the spec and the plan amendment state the wider behaviour, or add a clarifying entry if the human wants one.

## O1 — observation
Earlier non-blocking findings (hyphen and `.md.bak` rewrites, permissive E1 test, spec refusal list) were not part of this diff; the spec refusal-list one was resolved at 9baea5a.
