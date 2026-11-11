# Review: intake/generator-hook-defects — reread-20261111T174823Z

Verdict: changes-required
Reviewed: intake/generator-hook-defects @ 9baea5a
Baseline: intake/generator-hook-defects @ b11df95
Reviewer: reviewer-agent and skeptic-risk-agent (three passes) and spec-reviewer-agent (specs/rule-store.md hunk only); wrote none of the delta
Date: 2026-11-11
Scope: `git diff b11df95 9baea5a -- specs/ decisions/ docs/plans/`: six edited sentences in specs/rule-store.md (J1, J4, G6, AC-RS-12, AC-RS-14, Failure modes), DEC-001780, DEC-001790, the plan's class line and amendments. No file under bin/ changed between the two revisions (`git diff --stat b11df95 9baea5a -- bin` is empty), so the earlier run results on the code stand. Re-ran bin/bundle on a clone at 9baea5a (/tmp/rvw/c2).
Cross-checked: specs/rule-store.md AC-RS-15, README.md, SPEC.md, decisions/log.md DEC-000630, bin/tests/test_bundle_cli.py, test_release.py, test_emit_bundle.py.
Not inspected: process/adopt.md (another reviewer's); the Spec Reviewer entry-read items (SLOs, NFR dimensions) outside the hunk; agreement of the spec text, which is a proposal awaiting the human's ruling.
Findings: 1 blocking, 2 non-blocking (F2, F3)
The human should inspect: F1 (which way to resolve), and the spec sentences as a whole, since they are a proposal.

## Quality pass
Verdict (quality): ready
Only text changed; no code or test edit to review. Test coverage of each spec claim:
- J1/G6/AC-RS-14 marker on dirty inputs, one line, twelve hex: test_bundle_cli.py TestBundleLocalProvenance test_d3_* (modified, untracked, deleted, renamed, staged), clean tree plain: test_d3_a_clean_tree_keeps_the_plain_revision_header.
- Release asset never carries the marker: test_release.py test_d5_release_assets_carry_the_plain_revision.
- AC-RS-12 repository named: test_c1_the_line_carries_dash_r_owner_repo_from_the_origin_url and test_c1_each_github_url_form_yields_the_same_owner_repo.
- Failure modes: dirty input test_d2_*; non-GitHub origin test_c1_a_remote_that_is_not_a_github_url_is_refused; lacks a row or carries a retired one test_c2_*.
- J4's sentence that a `+local` bundle "is not that revision's text" is interpretation, no test; acceptable as prose.
- A test asserts something the spec does not state or contradicts: test_d3_emit_bundle_output_is_unchanged_by_a_dirty_tree (see F1).

## Skepticism pass
Verdict (skepticism): ready-with-findings
Re-ran on 9baea5a with a modified rules/R0004.md: `--where` header is `...@ 9baea5af...+local.424ad7cb6a1d ...`. The same tree through `--emit bundle --where role=writer` gives the plain header. A README.md-only edit gives the plain header on `--where`. These drive F1 and F2.

## Continuity pass
Verdict (continuity): changes-required
1. DEC-001790 supersedes DEC-000630 as a whole entry: it restates the one-line HTML comment form, the timestamp form and "no member list, no blob list, no title line", all that DEC-000630 said; DEC-000630's own "Supersedes: DEC-000320 (header clause only...)" concerned the predecessor and is not needed. The only other mention of DEC-000630 in specs, README.md, SPEC.md, process and rules was the J1 and G6 citations, both moved to DEC-001790. Nothing outside the log still cites it. It correctly supersedes.
2. The six sentences match the code for: marker on `--where` only (not `--emit`), never on release assets, repository named, the refusals. Two do not (F1, F2).
3. My earlier F1: resolved in substance (decision recorded, G6/J1/J4/AC-RS-14 updated, class corrected, human ruled yes) except that the edit leaves AC-RS-15 contradicted (F1 below). README.md and SPEC.md contain no header or release-refusal prose now contradicted.
4. Plan class line: "routine, except D3 ... consequential ... goes on the gate at the release that first carries it". It matches the spec's section 8 and DEC-001790's context. Consistent.

## F1 — blocking
Claim: AC-RS-15 says `--emit bundle` "writes the file `--where` writes, byte-identical", but a dirty-tree `--where` file now carries the marker and `--emit bundle` does not, and the delta edits neither.
Classification: defect
Location: specs/rule-store.md AC-RS-15 (unedited); G6 and AC-RS-14 (edited); bin/bundle `_local_head` used only by cmd_where; bin/tests/test_bundle_cli.py test_d3_emit_bundle_output_is_unchanged_by_a_dirty_tree
Evidence: ran at 9baea5a with a dirty rules/R0004.md: `--where` header has `+local.424ad7cb6a1d`; `--emit bundle --where` header is plain. test_emit_bundle.py:55 holds byte-identity on a clean tree only, so no test fails.
Consequence: the spec states two incompatible things; a test asserts the divergence the spec does not state.
Fix: either state in AC-RS-15 that `--emit bundle` is byte-identical except for the marker and give it the marker (and change the d3 test), or say in G6 and AC-RS-15 that the marker is `--where` only and `--emit bundle` is exempt on a dirty tree. Human ruling.

## F2 — non-blocking
Claim: G6 and AC-RS-14 say the marker follows "uncommitted generation inputs", but README.md, an input root for release, does not mark a bundle.
Classification: suggestion
Location: specs/rule-store.md G6, AC-RS-14, J1; bin/bundle `_local_head` (README.md excluded)
Evidence: ran: README.md-only edit, `--where` header plain. No test asserts it.
Consequence: a reader of the spec expects a marker the tool does not emit; the effect is nil because README.md is not part of any bundle.
Fix: name the inputs that mark (rules/, process/, bin/bundle, bin/release, bin/rulestore/), or add a test pinning README.md's exclusion.

## F3 — non-blocking
Claim: DEC-001790's "Release assets never carry the marker" is true only because `bin/release` refuses on dirty inputs; gitignored files under rules/ are not seen (earlier F2, unchanged).
Classification: suggestion
Location: bin/rulestore/store.py dirty_input_paths
Evidence: from the earlier run (a gitignored rule file reached a release bundle with the plain SHA); code unchanged.
Consequence: the decision's "never" is stronger than the check.
Fix: --ignored in the status call, or soften the wording.
