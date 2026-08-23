# Review: the corpus — Pass 1 re-gate confirmation — cycle 4

Verdict: changes-required
Reviewed: 7 files @ b6102de for the confirmation pass (enumerated below), and the 51-file corpus set @ b6102de for the two corpus-wide sweeps
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: every file PR #139 changed, excluding `docs/**` — enumerated from `git diff --name-only c8e95d1 9759ed3` and listed below — read whole against all eleven criteria of docs/global-context/review-rubric.md @ b6102de and against the current foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, all @ b6102de. Then each of the 6 findings in reviews/corpus-regate-cycle-3.md and its six companion artifacts resolved against the landed text. Then two sweeps re-run corpus-wide over the 51-file set, contradictions and role boundaries, per directive. Bundle membership, audience values, and near-duplicate sentences were extracted mechanically at b6102de.
Cross-checked: docs/cycles/pass1-regate-fix-4-20260823T013000.md in full, for the dispositions D13 and D10-restated each fix was executed under; reviews/corpus-regate-cycle-3.md and all six companion artifacts in full; `git diff c8e95d1 9759ed3` for every file in scope; engagements/cartographer.md, engagements/assistant.md, engagements/sre/README.md, engagements/sre/implementer.md, engagements/sre/override-log-policy.md, roles/context-quality-reviewer.md, roles/spec-reviewer-agent.md, roles/reviewer-agent.md, roles/skeptic-risk-agent.md, roles/release-manager-agent.md, roles/architect-agent.md, roles/coder-agent.md, roles/test-designer-agent.md, roles/chief-of-staff.md, roles/writer.md, skills/review-artifact.md, skills/evidence-review.md, skills/boundary-audit.md, skills/spec-review-cycle.md, policies/source-of-truth-policy.md, policies/verification-boundary-policy.md, context-sets/spec-and-change-discipline.md, boundaries/human-review-boundary.md, prose-criteria.md, specs/trd-template.md, specs/prd-template.md, all @ b6102de, as the other side of a sweep row; `bin/check-frontmatter --all`; `bin/tests/run`; reviews/corpus-regate-cycle-2.md for the CN-7 and CN-8 dispositions this cycle carries.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is still unbuilt, and every bundle membership in this artifact was computed from frontmatter directly, not by running it; `docs/**`, excluded from the confirmation pass by directive, including this cycle's own directive file; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/, and every reference within them, excluded by directive; the 44 corpus files PR #139 did not change, which were read as the other side of a sweep row and did not receive a confirmation pass; the duplicate-rules sweep, which this directive did not commission and which is therefore not re-run — no claim is made about its state at b6102de, including whether DR-26 and DR-27 still stand as cycle 3 recorded them; the term-collision, audience-value, path-reference and retired-vocabulary sweeps, likewise not commissioned and not re-run, beyond the two spot checks recorded below; DR-25 (roles/architect-agent.md / specs/trd-template.md), which persists unchanged at b6102de and which the directive excludes from report; the structural path references in policies/document-metadata-policy.md and roles/chief-of-staff.md, excluded by directive; the two pre-existing `bin/tests` failures, excluded by directive; whether any rule is *correct* as engineering or product judgment — this role judges coherence and safety as LLM context only; the PRD and TRD instances, which are the Spec Reviewer's and do not exist in this repository; whether decisions D1 through D13 were the right calls, which this cycle treats as settled.
Findings: 2 new — 1 blocking, 1 non-blocking — across 2 companion artifacts. Of the prior cycle's 6 findings, 5 are closed and 1 is reopened differently. This artifact carries the two sweeps (12 rows: 1 contradiction, 11 role boundaries), the closure table, and the confirmation-pass verdicts; per-file findings are in the two artifacts named below.
Prior cycle: reviews/corpus-regate-cycle-3.md (reviewed @ edd8015)
Dave should inspect: SA-6 — the only blocking finding, and the one place D13 did not land. It is one clause in engagements/sre/speed-audit.md, and until it is fixed the Implementer reads a bundle that both requires and forbids it to measure its own change.

---

## Scope — the 7 files in the confirmation pass

`git diff --name-only c8e95d1 9759ed3` returns 7 paths. None is under `docs/`, so the directive's exclusion removes nothing and the confirmation-pass set is the whole diff:

engagements/critic.md · engagements/sre/baseline-measurement.md · engagements/sre/engagement-change-package.md · engagements/sre/speed-audit.md · engagements/sre/system-discovery.md · operating-model.md · policies/document-metadata-policy.md

## Scope — the 51-file sweep set

Unchanged from the prior cycle, and recomputed mechanically at b6102de: `bin/check-frontmatter --all` matches 36 files from nine globs and exits 0, plus `docs/global-context/*.md` (3), `engagements/**/*.md` (11), and prose-criteria.md (1). The 17 distinct `audience:` values and their file counts are identical to the prior cycle's; PR #139 changed no `audience:` line, so the fourteen bundles are unchanged and are the ones this artifact's delivery claims are computed against.

---

## Closure — the prior cycle's 6 findings

**5 closed · 0 still open · 1 reopened differently.**

| Finding | File | State | The landed text |
| --- | --- | --- | --- |
| SA-5 | sre/speed-audit.md | closed | engagements/sre/speed-audit.md:18-21 — "unknowns go to the Assistant in the Cartographer's report; the Assistant carries to Dave what needs his decision, and Dave decides what to ask the client." Instruction 1, verbatim. The routing D10 settled now reads the same way in all three files that state it. |
| OM-2 | operating-model.md | closed | operating-model.md:126 — the role attribution is now *(PM/EM/Owner + Architect + Spec Reviewer for specs; Context Quality Reviewer for governed context documents)*. Instruction 2, verbatim. A corpus-wide grep for "Spec Reviewer" over the 51-file set returns 16 occurrences and every one is spec-scoped; no clause attaches the Spec Reviewer to a non-spec document. |
| DMP-5 | document-metadata-policy.md | closed | policies/document-metadata-policy.md:152 — `roles/context-quality-reviewer.md` added to the gate-document class list, immediately after the four peer role documents at :148-151. Instruction 3. `bin/check-frontmatter --all` still exits 0 with 36 files matched. |
| SRE-BM-5 | sre/baseline-measurement.md | **reopened differently** | :9-12 — "step 6 runs in an execution session by the Cartographer, who re-measures with the baseline's instrument; the Implementer does not measure its own change." Instruction 4 under D13, verbatim. SRE-BM-5's stated defect is gone: a document now says which role re-measures. Naming the role created two adjacent defects on the same subject — the route the measurement takes to the change package that must cite it is unstated (SRE-BM-6), and engagements/sre/speed-audit.md:28-29 still reads as assigning re-measurement to the Implementer (SA-6). |
| SRE-ECP-4 | sre/engagement-change-package.md | closed | :9-10 — "Produced in an execution session by the Implementer. The Assistant and the Critic read it; neither produces one." Instruction 5, verbatim. All three role slugs in the file's `audience:` are now accounted for by the reader clause. |
| CR-2 | critic.md | closed | engagements/critic.md:12 — "An engagement has no release gate, per the Engagement Pack." Instruction 6. The target's own first heading is `# Engagement Pack` (engagements/sre/README.md:7), so the citation now names the document by the title it carries, and the last filename-shaped cross-reference in the engagement pack is gone. |

Also confirmed closed, from the prior cycle's sweeps rather than its findings: **CN-14** — both halves of the Cartographer routing are conformed; see sweep (b). **CN-15** — closed with OM-2. **BD-10** and **BD-12** — see sweep (g).

## Sweep (b) — Contradictions

Corpus-wide over the 51-file set. Two files, or two passages of one file, stating incompatible rules. Re-run mechanically as a 4-gram near-duplicate scan over all 1,388 sentences of the set at a Jaccard floor of 0.40, then read, plus targeted greps over the subjects PR #139 moved: re-measurement and the stopwatch, Cartographer output routing, "Spec Reviewer", "Context Quality Reviewer", and every session-kind and producer/reader clause in the set.

| # | Statement A | Statement B | Why incompatible |
| --- | --- | --- | --- |
| CN-16 | engagements/sre/baseline-measurement.md:9-12 — "step 6 runs in an execution session by the Cartographer, who re-measures with the baseline's instrument; the Implementer does not measure its own change" | engagements/sre/speed-audit.md:28-29 — "5. **Attack** — the Implementer builds; the Critic reviews where a review is requested; re-measure after each landing, not in batches." | One act, two answers. D13 assigns re-measurement to the Cartographer and forbids the Implementer measuring its own change; step 5's re-measure clause carries no subject and follows two clauses that name the Implementer and the Critic, so the nearest available subject is the role the other sentence prohibits. Both files are in the `implementer` bundle (24 files) and the `cartographer` bundle (24 files), so each role reads both at once. **Open.** SA-6, and the speed-audit half of BD-11. |

**1 row, open. Prior cycle: 2 rows, both open. Delta −1 row, −1 open.** CN-14 closed by instruction 1, which conformed both halves — engagements/sre/speed-audit.md:18-21 and engagements/sre/system-discovery.md:24-26 — so the corpus now states the Cartographer routing identically in engagements/cartographer.md:9-10 and :28-33, engagements/sre/system-discovery.md:10, :24-26 and :36, and engagements/sre/speed-audit.md:18-21. CN-15 closed by instruction 2. CN-7 and CN-8, recorded not-open at cycle 2, are unchanged and were re-checked: the narrowed Spec Reviewer gate still does not reach the documents the doc-only path covers, and the shared name behind CN-8 is still gone. CN-16 is new, and is the only open row.

## Sweep (g) — Role boundaries

Corpus-wide over the 51-file set, per directive. Every role and skill document in the set against the full role set, plus every role attribution in the policies, context sets, boundaries and spec templates. The prior cycle ran this over 14 changed files and the cycle before it over 30, so the row sets are not directly comparable and the delta below is stated against the prior table's count, not against a like-for-like set.

| # | Boundary | Role A | Role B | State at b6102de |
| --- | --- | --- | --- | --- |
| BD-1 | Gating a governed methodology document | roles/context-quality-reviewer.md:34-35 — "Nothing else is" | roles/spec-reviewer-agent.md:33-35 — the PRD, TRD, ACs "and nothing else" | **Closed, and now stated the same way in five places.** operating-model.md:126's role attribution joined its prose, roles/spec-reviewer-agent.md, roles/spec-reviewer-agent.md:105-107 and roles/context-quality-reviewer.md under instruction 2. |
| BD-2 | A read of a finished piece of public prose | roles/writer.md:17 (offers the Critic read only) | engagements/critic.md (advisory) · roles/context-quality-reviewer.md:14-17 (scope excludes public prose) | **Closed.** Unchanged. |
| BD-4 | Building the change | roles/coder-agent.md | engagements/sre/implementer.md:9-11 | **Not open** — disjoint bundles (`coder-agent` 18 files, `implementer` 24, no shared role slug), different upstream artifact. Unchanged. |
| BD-5 | Who may override a procedural step | engagements/sre/override-log-policy.md:13-14, :34 | engagements/working-with-dave.md:36-38 | **Closed** by D1. Unchanged. |
| BD-6 | Reviewing the Implementer's own diff, and who may summon the Critic | engagements/sre/implementer.md:37-39 — "A Critic read happens only when Dave requests one" | engagements/critic.md:9-10 — "when Dave (or his Assistant, at a completion point) explicitly asks" · engagements/assistant.md:13-14 — "offer a Critic pass" | **Not open, carried.** Cycle 2 closed this row on the reading that who reviews, who requests, and what happens when nobody does are all stated. Re-checked corpus-wide: the two sentences differ on whether the Assistant may summon, but the pair is in disjoint bundles (engagements/critic.md is `[critic, human]`, engagements/sre/implementer.md is `[implementer, assistant, human]`), and engagements/assistant.md:13-14 has the Assistant *offering* rather than requesting, which reconciles them. Recorded so the reconciliation stays visible; not re-opened, and PR #139 changed neither clause. |
| BD-7 | Proposing an improvement | engagements/sre/speed-audit.md:36-38 | engagements/cartographer.md | **Closed, stated in one direction.** Unchanged. |
| BD-8 | Emitting a ship recommendation | roles/skeptic-risk-agent.md:124-126 — "You do not emit a ship recommendation; that call is the Release Manager's" | roles/release-manager-agent.md:50-57 · skills/evidence-review.md:38-39 | **Not open.** Neither file is in this cycle's changed set; re-checked and unchanged, as the deliberate split cycle 3 recorded. |
| BD-9 | Who gates a methodology document, and what `agreed` requires | operating-model.md:126 | roles/context-quality-reviewer.md:27-30 · policies/document-metadata-policy.md:140-156 | **Closed, and the residue is closed too.** DMP-5 added `roles/context-quality-reviewer.md` to the gate-document class list at :152, so the list now names the role document holding the gate for every methodology document in the repository. |
| BD-10 | Who receives the Cartographer's unknowns | engagements/cartographer.md:9-10, :28-33 — the Assistant, who triages and carries to Dave | engagements/sre/speed-audit.md:18-21 · engagements/sre/system-discovery.md:24-26, :36 | **Closed.** Three files in the `cartographer` bundle, one answer. This was the prior cycle's largest finding. |
| BD-11 | Who re-measures after a change, and where the measurement goes | engagements/sre/baseline-measurement.md:9-12 — the Cartographer, per D13 | engagements/sre/speed-audit.md:28-29 — reads as the Implementer · engagements/cartographer.md:9-10 — report enumerated as the question list and the rendered map, neither a measurement | **Reopened differently, and open.** The runner question D13 answered is answered. Two adjacent questions are not: which role step 5 of the play assigns (SA-6, CN-16), and by what route the Cartographer's measurement reaches the change package that must cite it — engagements/sre/engagement-change-package.md is not in the `cartographer` bundle (SRE-BM-6). |
| BD-12 | Who reads the engagement change package | engagements/sre/engagement-change-package.md:9-10 — the Implementer produces; the Assistant and the Critic read | engagements/critic.md — in the file's `audience:`, and the subject of its item 6 | **Closed.** All three role slugs in the `audience:` are accounted for. Whether D13 now puts the Cartographer in that set is BD-11's question, not this row's. |

**11 rows, 1 open. Prior cycle: 10 rows, 3 open, over a 14-file set; the cycle before that, 9 rows over a 30-file set. Delta +1 row, −2 open, over a set 3.6× larger than the prior cycle's.** All three of the prior cycle's open rows moved: BD-10 and BD-12 closed outright, BD-11 reopened differently. No row is new to the corpus-wide run that the prior narrower runs did not already carry: the role attributions in policies/source-of-truth-policy.md:22-23 and :70, policies/verification-boundary-policy.md:155, :159-160, boundaries/human-review-boundary.md:14, context-sets/spec-and-change-discipline.md:30-32, prose-criteria.md:10, specs/trd-template.md:20-34 and specs/prd-template.md:79 were each resolved against the owning role document and each agrees with it.

## Confirmation pass — one line per file

7 files. 5 clean, 2 with findings. A clean line means the file was read whole against all eleven criteria at b6102de and nothing in it fails at the current foundation; cross-file matters are in the sweeps above and are not counted against the file here.

| File | Verdict | Findings | Artifact |
| --- | --- | --- | --- |
| engagements/sre/speed-audit.md | changes-required | 1 blocking | reviews/sre-speed-audit-cycle-4.md |
| engagements/sre/baseline-measurement.md | ready-with-findings | 1 non-blocking | reviews/sre-baseline-measurement-cycle-4.md |
| engagements/critic.md | ready | none | — |
| engagements/sre/engagement-change-package.md | ready | none | — |
| engagements/sre/system-discovery.md | ready | none | — |
| operating-model.md | ready | none | — |
| policies/document-metadata-policy.md | ready | none | — |

---

## The single largest remaining problem

**The decision that made measurement independent is stated in the file that defines the measurement and contradicted in the file that describes the whole engagement.** D13 says the Cartographer re-measures and the Implementer does not measure its own change; engagements/sre/baseline-measurement.md:9-12 says exactly that, and engagements/sre/speed-audit.md:28-29 still reads "the Implementer builds; the Critic reviews where a review is requested; re-measure after each landing" — a subjectless clause whose nearest subject is the role D13 rules out. Both files are in the `implementer` bundle and the `cartographer` bundle, so both roles read the instruction and the prohibition together. This is the third consecutive cycle whose largest problem has the same shape: a decision executed exactly where its instruction named, in a corpus that states the same fact in three places. Cycle 2's winner was the agreement gate across four files, cycle 3's was the Cartographer's recipient across three, and this one is a single unconformed clause — the shape is unchanged and the surface is shrinking.

## Departures from the directive

Two, both in what could be claimed rather than what was done.

1. **The sweeps are two, and the un-run five are named rather than estimated.** The directive commissions contradictions and role boundaries, corpus-wide, and no others. Duplicate rules — run corpus-wide at cycle 3 — is therefore not re-run, and this artifact makes no claim about its state at b6102de, including whether DR-26 and DR-27 still stand as recorded; term collisions, audience values, path references and retired vocabulary are likewise not re-run. All five are listed in `Not inspected`. Two spot checks were run because PR #139 touched their subject and a silent regression would have been invisible: the 17 `audience:` values and their file counts are identical to the prior cycle's, PR #139 having changed no `audience:` line, and a corpus-wide grep for "Spec Reviewer" over the 51-file set finds every one of its 16 occurrences spec-scoped.

2. **The role-boundaries delta is stated against the prior table's row count, not against a like-for-like set.** The directive scopes this sweep corpus-wide, where the prior cycle's was 14 files. A row count over 51 files is not comparable to one over 14; both numbers are given in the sweep note, along with the observation that the corpus-wide run surfaced no row the narrower runs had missed, and the incomparability is stated there rather than absorbed into a delta.

Also noted, and not acted on: `bin/check-frontmatter --all` exits 0 at b6102de, reporting 36 files matched from 9 globs. `bin/tests/run` ran 367 tests with exactly two failures, both `test_bn10` — the two pre-existing failures the directive excludes from report; no third failure appeared.

No document was edited. No status was flipped. No finding was resolved.
