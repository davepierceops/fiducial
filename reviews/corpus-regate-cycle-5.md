# Review: the corpus — Pass 1 re-gate confirmation — cycle 5

Verdict: ready-with-findings
Reviewed: engagements/sre/speed-audit.md and engagements/sre/baseline-measurement.md @ b0b3540 for the confirmation pass, and the 10-file engagement set @ b0b3540 for the two sweeps
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: the two confirmation-pass files read whole against all eleven criteria of docs/global-context/review-rubric.md @ b0b3540 and against the current foundation — docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, engagements/sre/README.md, roles/context-quality-reviewer.md, all @ b0b3540. Then SA-6 and SRE-BM-6 resolved against the landed text. Then two sweeps — contradictions and role boundaries — over the seven engagements/sre/ files (README.md, baseline-measurement.md, engagement-change-package.md, implementer.md, override-log-policy.md, speed-audit.md, system-discovery.md) plus engagements/cartographer.md, engagements/assistant.md and engagements/critic.md. Bundle membership and audience values were extracted mechanically at b0b3540; the contradiction sweep was run as a 4-gram near-duplicate scan over all 153 sentences of the 10-file set at a Jaccard floor of 0.35, then read, plus targeted greps over the subjects PR #143 moved.
Cross-checked: docs/cycles/pass1-regate-fix-5-20260823T020500.md in full, for the text each fix was dictated to land; reviews/corpus-regate-cycle-4.md, reviews/sre-speed-audit-cycle-4.md and reviews/sre-baseline-measurement-cycle-4.md in full; skills/review-artifact.md for this artifact's shape; `git diff b68fe87 821e246` for both changed files; `git diff --stat babda5b b0b3540` to verify the starting state; `bin/check-frontmatter --all`; `bin/tests/run`.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is still unbuilt, and every bundle membership in this artifact was computed from frontmatter directly, not by running it; the 41 corpus files outside the 10-file engagement set, which this directive's sweeps do not reach — no claim is made about their state at b0b3540; the confirmation-pass criteria as applied to the eight sweep-set files that are not the two named files, which were read as the other side of a sweep row and did not receive a confirmation pass; cycle 4's role-boundary rows BD-1, BD-8 and BD-9, whose both sides lie outside this cycle's sweep set and which are therefore not re-run — no claim is made about their state at b0b3540; the duplicate-rules sweep, which this directive did not commission and which is therefore not re-run, including the J=1.0 pair the near-duplicate scan surfaced between engagements/cartographer.md:9-10 and engagements/sre/system-discovery.md:9-10; the term-collision, audience-value, path-reference and retired-vocabulary sweeps, likewise not commissioned and not re-run; the all-decision-roles selector, the unbuilt bundler, the two pre-existing `bin/tests` failures, baton delivery's home in Core, and every reference in docs/history/, docs/batons/, docs/cycles/, reviews/ and retros/, all excluded by directive; whether any rule is *correct* as engineering or product judgment — this role judges coherence and safety as LLM context only; the PRD and TRD, which are the Spec Reviewer's and do not exist in this repository; whether decisions D1 through D13 were the right calls, which this cycle treats as settled.
Findings: 1 new — 0 blocking, 1 non-blocking — in 1 companion artifact. Of the prior cycle's 2 findings, 1 is closed and 1 is reopened differently. This artifact carries the two sweeps (9 rows: 1 contradiction, 8 role boundaries), the closure table, the confirmation-pass verdicts, and one observation; the per-file finding is in the artifact named below.
Prior cycle: reviews/corpus-regate-cycle-4.md (reviewed @ b6102de)
Dave should inspect: the observation below — instruction 1's dictated replacement text dropped the clause "after each landing, not in batches," and no file in the corpus now states that re-measurements are not batched. No rubric criterion fails on it, so it is not a finding; whether the rule should come back is a call this role cedes.

---

## Starting state

`git rev-parse HEAD` is b0b3540ed63f37aa63d0361803289f3652e92b1c. `git diff --stat babda5b b0b3540` reports one file changed, 33 insertions, 0 deletions — docs/cycles/pass1-regate-confirm-4-20260823T025500.md, this cycle's own directive file. The starting state is the stated one. No file this session did not change moved; HEAD did not move; no index lock appeared.

## Scope — the 10-file sweep set

`audience:` at b0b3540, read directly:

| File | `audience:` |
| --- | --- |
| engagements/sre/README.md | assistant, cartographer, critic, implementer, human |
| engagements/sre/baseline-measurement.md | cartographer, implementer, assistant, human |
| engagements/sre/engagement-change-package.md | implementer, critic, assistant, human |
| engagements/sre/implementer.md | implementer, assistant, human |
| engagements/sre/override-log-policy.md | assistant, cartographer, critic, implementer, human |
| engagements/sre/speed-audit.md | assistant, cartographer, critic, implementer, human |
| engagements/sre/system-discovery.md | cartographer, assistant, human |
| engagements/cartographer.md | cartographer, human |
| engagements/assistant.md | assistant, human |
| engagements/critic.md | critic, human |

PR #143 changed no `audience:` line. Over the 51-file corpus set the role-slug counts are unchanged from the prior cycle, so the bundles this artifact's delivery claims are computed against are the prior cycle's: `implementer` 24 files, `cartographer` 24, `critic` 24, `assistant` 26 — each being the 17 `all-roles` files plus that role's own.

---

## Closure — the prior cycle's 2 findings

**1 closed · 0 still open · 1 reopened differently.**

| Finding | File | State | The landed text |
| --- | --- | --- | --- |
| SA-6 | sre/speed-audit.md | closed | engagements/sre/speed-audit.md:28-29 — "5. **Attack** — the Implementer builds; the Critic reviews where a review is requested; the Cartographer re-measures against the baseline." Instruction 1. The third clause now carries an explicit subject, and it is the subject D13 names; the sentence engagements/sre/baseline-measurement.md:9-12 states as a prohibition is no longer contradicted anywhere. The Cartographer now appears in two steps of the play — 1 and 5 — which is what :9-10 promises its readers when it says they read it "for the steps assigned to them." |
| SRE-BM-6 | sre/baseline-measurement.md | **reopened differently** | :32-35 — "The Cartographer delivers the re-measurement to the Assistant; the Implementer cites it in the change package's Expected-delta item." Instruction 2, verbatim. SRE-BM-6's stated defect is gone: the route is stated in the sentence that assigns the duty, and it terminates at the Assistant, who is in the Cartographer's bundle, so the Cartographer no longer holds a duty whose destination it cannot resolve. Naming the destination item created one defect on the same subject — the item named is defined at engagements/sre/engagement-change-package.md:20-21 as the pre-stated claim citing the baseline, which does not admit a post-change measurement (SRE-BM-7). |

## Sweep (b) — Contradictions

Over the 10-file set. Two files, or two passages of one file, stating incompatible rules. Run as a 4-gram near-duplicate scan over all 153 sentences of the set at a Jaccard floor of 0.35, then read, plus targeted greps over the subjects PR #143 moved: re-measurement and the stopwatch, the expected delta, and every session-kind, producer and reader clause in the set. The scan returned 6 near-duplicate pairs; all six are agreements — the Cartographer report enumeration stated identically in two files, the engagement session-kind line in two, the no-fixed-filename record in two, the Assistant-carries-to-Dave routing in two, the no-release-gate rule in two, and the Artifacts-list deferral in two — and none is a contradiction.

| # | Statement A | Statement B | Why incompatible |
| --- | --- | --- | --- |
| CN-17 | engagements/sre/baseline-measurement.md:34-35 — "the Implementer cites it in the change package's Expected-delta item" | engagements/sre/engagement-change-package.md:20-21 — "3. **Expected delta** — the pre-stated measurement claim, citing the baseline (or the logged override that waived it)" | One item, two contents. The instruction puts the post-change measurement in item 3; item 3's own definition admits only the pre-stated claim and the baseline cite, and this file's step 5 and engagements/sre/implementer.md:19 both state the expectation as pre-stated, before implementation. The `implementer` bundle (24 files) and the `assistant` bundle (26 files) each hold both files, so the role the clause instructs reads the instruction and the narrower definition at once. **Open.** SRE-BM-7. |

**1 row, open. Prior cycle: 1 row, open, over the 51-file corpus set. Delta 0 rows, 0 open — but not the same row: CN-16 closed and CN-17 is new.** CN-16 is directly comparable — both its sides, engagements/sre/baseline-measurement.md and engagements/sre/speed-audit.md, are inside this cycle's 10-file set — and it is closed by instruction 1. The row *count* is not comparable: the prior cycle swept 51 files and this one sweeps 10, so a corpus-wide contradiction outside the engagement pack would not be visible here, and none is claimed either way.

## Sweep (g) — Role boundaries

Over the 10-file set. Every role attribution, producer clause, reader clause and prohibition in the set, resolved against the owning role document. Cycle 4's rows BD-1, BD-8 and BD-9 have both sides outside this set and are not re-run; BD-4's other side (roles/coder-agent.md) is outside it and the row is not re-run either. Rows BD-2 and BD-5 have one side outside the set, and that side was read as part of this cycle's required reading, so they are resolved rather than dropped.

| # | Boundary | Role A | Role B | State at b0b3540 |
| --- | --- | --- | --- | --- |
| BD-2 | A read of a finished piece of public prose | engagements/critic.md:9-13 — summoned only; verdict is input, not a gate | roles/context-quality-reviewer.md:14-17 — scope excludes public prose | **Closed.** Neither side changed in PR #143. |
| BD-5 | Who may override a procedural step | engagements/sre/override-log-policy.md:13-14, :34 — "Only Dave overrides. The client's humans do not; the agent does not." | engagements/working-with-dave.md:36-38 — "Overridable by Dave only, logged" | **Closed** by D1. Unchanged; both sentences state the same rule and neither grants an agent the call. |
| BD-6 | Reviewing the Implementer's own diff, and who may summon the Critic | engagements/sre/implementer.md:37-39 — "A Critic read happens only when Dave requests one; do not request it and do not review your own diff" | engagements/critic.md:9-10 — "when Dave (or his Assistant, at a completion point) explicitly asks" · engagements/assistant.md:13-14 — "offer a Critic pass" | **Not open, carried.** Re-checked at b0b3540 on cycle 2's reading and unchanged: the two sentences differ on whether the Assistant may summon, but the pair is in disjoint bundles — engagements/critic.md is `[critic, human]`, engagements/sre/implementer.md is `[implementer, assistant, human]` — and engagements/assistant.md:13-14 has the Assistant *offering* rather than requesting, which reconciles them. PR #143 changed none of the three. |
| BD-7 | Proposing an improvement | engagements/sre/speed-audit.md:36-38 — "Drafted by the Assistant ... The Cartographer does not propose; the Implementer does not self-authorize" | engagements/cartographer.md — no proposal duty stated; :25-27 maps, :37-38 never flattens provenance | **Closed, stated in one direction.** Unchanged. |
| BD-10 | Who receives the Cartographer's unknowns | engagements/cartographer.md:9-10, :28-33 — the Assistant, who triages and carries to Dave | engagements/sre/system-discovery.md:9-10, :24-26, :36 · engagements/sre/speed-audit.md:18-21 | **Closed.** Re-checked: instruction 1 rewrote only step 5 of engagements/sre/speed-audit.md, leaving step 1's routing intact, so all four statements still read the same way. |
| BD-11 | Who re-measures after a change, and where the measurement goes | engagements/sre/baseline-measurement.md:9-12, :34 — the Cartographer measures and delivers to the Assistant | engagements/sre/speed-audit.md:28-29 — the Cartographer · engagements/cartographer.md:9-10 — report enumerated as the question list and the rendered map | **Closed.** Both halves are answered. Which role measures is now stated identically in the two files that state it. Where the measurement goes is stated in the sentence that assigns the duty, and it goes to the Assistant, who is in the `cartographer` bundle. engagements/cartographer.md:9-10 does not contradict it: it enumerates what the Cartographer's *report* carries, not everything the role ever delivers, and the delivery duty reaches the Cartographer through engagements/sre/baseline-measurement.md, which is in its bundle. The residue is not a boundary question — no role's claim is in doubt — and is carried as CN-17. |
| BD-12 | Who reads the engagement change package | engagements/sre/engagement-change-package.md:9-10 — the Implementer produces; the Assistant and the Critic read | engagements/critic.md — in the file's `audience:`, and the subject of its item 6 | **Closed.** All three role slugs in the `audience:` are accounted for. PR #143 changed neither file, and instruction 2's "no audience change" held: the `audience:` line is byte-identical at b0b3540. |
| BD-13 | Who produces the post-change measurement the change package cites | engagements/sre/baseline-measurement.md:9-12 — the Cartographer measures; "the Implementer does not measure its own change" | engagements/sre/implementer.md:11 — builds "measurement code" · :26 — "verify as far as read-only access allows" · :28 — "assemble the engagement change package" | **New, and not open.** Building the instrument, assembling the package and citing the number are the Implementer's; running the post-change measurement is the Cartographer's. The general responsibility at :26 and the specific prohibition at :11 stand in a general/specific relation, not a clash, and the prohibition is explicit and in the same bundle (`implementer`, 24 files) as the responsibility. Recorded because instruction 2 made this pairing load-bearing for the first time. |

**8 rows, 0 open. Prior cycle: 11 rows, 1 open, over the 51-file corpus set. Delta −1 open; +1 new row (BD-13); 4 of the prior cycle's rows not re-run because their sides lie outside this cycle's set.** The row counts are not comparable — 51 files against 10 — and the −1 open is stated against the one prior row that lies inside this set, BD-11, which closed. No open row remains in this sweep.

## Confirmation pass — one line per file

2 files. 1 clean, 1 with a finding. A clean line means the file was read whole against all eleven criteria at b0b3540 and nothing in it fails at the current foundation; cross-file matters are in the sweeps above and are not counted against the file here.

| File | Verdict | Findings | Artifact |
| --- | --- | --- | --- |
| engagements/sre/speed-audit.md | ready | none | — |
| engagements/sre/baseline-measurement.md | ready-with-findings | 1 non-blocking | reviews/sre-baseline-measurement-cycle-5.md |

engagements/sre/speed-audit.md passes all eleven. Criterion 1: every artifact it names — System Map, Measurement Baseline, Improvement Proposal, "the shape the Artifacts list states" — is defined in engagements/sre/README.md, whose `audience:` is identical to this file's, so the definition is in every bundle the file lands in. Criterion 3: the only slash in the file is "before/after" at :30, which is not a path. Criterion 8: no model name and no occurrence of "track." Criterion 11: steps 1, 4, 5 and the Improvement Proposal section each name their actor, Dave's go is recorded and cited, and the two prohibitions at :37-38 are explicit.

## Observation — OBS-1

Claim: Instruction 1's dictated replacement text dropped the clause "after each landing, not in batches," and no file in the corpus now states that re-measurements are not batched.
Location: engagements/sre/speed-audit.md:28-29 at b0b3540, against the same lines at b68fe87.
Evidence: Verified by running. `git diff b68fe87 821e246 -- engagements/sre/speed-audit.md` replaces "re-measure after each landing, not in batches" with "the Cartographer re-measures against the baseline," which is instruction 1's dictated text executed verbatim. A corpus-wide grep for `re-?measur|stopwatch|delta-verified`, excluding the directories this directive excludes, returns engagements/sre/baseline-measurement.md:10, :32, :33, :34, :45, engagements/sre/README.md:32, engagements/sre/speed-audit.md:29 and engagements/working-with-dave.md:28 — and none of the eight states a cadence or forbids batching. The affirmative rule survives: engagements/sre/baseline-measurement.md:32 is "**Re-measure after the change**," per change, and that file is in the `cartographer`, `implementer` and `assistant` bundles, which are the three roles that measure, build and run the play. The Critic, which reads engagements/sre/speed-audit.md but not engagements/sre/baseline-measurement.md, does not measure and does not need the cadence.
Why this is not a finding: no rubric criterion fails. Criterion 1 holds because the per-change rule is in the bundle of every role that needs it; criterion 11 holds because no actor and no escalation is left to inference. What was lost is a prohibition against batching, which is engagement practice — whether it should be restated is a judgment this role cedes.

---

## The single largest remaining problem

**A reference was added and the definition it points at was not conformed.** Instruction 2 landed the route SRE-BM-6 asked for, and in naming its destination it named an item that engagements/sre/engagement-change-package.md:20-21 defines as the pre-stated claim citing the baseline. Both files are in the `implementer` bundle, so the role being instructed reads the instruction and the narrower definition together. This is the fourth consecutive cycle whose largest problem has the same shape — a fix executed exactly where its instruction named, in a corpus that states the same fact in more than one place — and the surface has shrunk again: cycle 2's was the agreement gate across four files, cycle 3's the Cartographer's recipient across three, cycle 4's a single unconformed clause, and this one is a single unconformed item definition, non-blocking, with the requirement it would enforce already stated one sentence earlier.

## Departures from the directive

Two, both in what could be claimed rather than what was done.

1. **The sweeps are scoped to 10 files, and the prior cycle's were corpus-wide, so neither delta is like-for-like.** Both deltas are stated against the individual prior rows that lie inside this cycle's set — CN-16 for the contradiction sweep, BD-11 for the role-boundary sweep — and not against the prior row counts. The four prior role-boundary rows whose sides lie outside this set (BD-1, BD-4, BD-8, BD-9) are named in `Not inspected` rather than carried with a stale state, and no claim is made about the 41 corpus files this cycle's sweeps do not reach.

2. **The verdict is not `ready`, and instruction 7's `ready` condition is therefore not met.** Instruction 7 makes the verdict `ready` if the pass is clean and both sweeps show zero open rows. The role-boundary sweep does show zero open rows; the contradiction sweep shows one (CN-17), and the confirmation pass is not clean. The verdict is `ready-with-findings` — the single finding is non-blocking — and the one-line `ready` sentence instruction 7 specifies is therefore not written.

Also noted, and not acted on: `bin/check-frontmatter --all` exits 0 at b0b3540, reporting 36 files matched from 9 configured globs. `bin/tests/run` ran 367 tests with exactly two failures, both `test_bn10` — the two pre-existing failures the directive excludes from report; no third failure appeared.

No document was edited. No status was flipped. No finding was resolved.
