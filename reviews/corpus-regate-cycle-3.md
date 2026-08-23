# Review: the corpus — Pass 1 re-gate confirmation — cycle 3

Verdict: changes-required
Reviewed: 14 files @ edd8015 for the confirmation pass (enumerated below), and the 51-file corpus set @ edd8015 for the two corpus-wide sweeps
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: every file PR #135 changed, excluding `docs/**` — enumerated from `git diff --name-only f46264b 219b0e7` and listed below — read whole against all eleven criteria of docs/global-context/review-rubric.md @ edd8015 and against the current foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, all @ edd8015. Plus engagements/sre/speed-audit.md:18-19 as a named residual from the part-3 report. Then each of the 15 dispositions in reviews/corpus-regate-cycle-2.md and its twelve companion artifacts — 12 new, 2 carried, 1 reopened — resolved against the landed text. Then two sweeps re-run corpus-wide over the 51-file set, duplicate rules and contradictions, and one re-run over the 14 changed files, role boundaries, per directive. Bundle membership, audience values, and near-duplicate sentences were extracted mechanically at edd8015.
Cross-checked: docs/cycles/pass1-regate-fix-3-20260823T004500.md in full, for the dispositions D9 through D12 each fix was executed under, and docs/cycles/pass1-regate-fix-20260822T230000.md for D1 through D8 where a cycle-2 finding turned on one; reviews/corpus-regate-cycle-2.md and all twelve companion artifacts in full; `git diff f46264b 219b0e7` for every file in scope; engagements/sre/README.md, engagements/sre/system-discovery.md, engagements/assistant.md, roles/spec-reviewer-agent.md, skills/spec-review-cycle.md, roles/release-manager-agent.md, skills/boundary-audit.md, roles/skeptic-risk-agent.md, all @ edd8015, as the other side of a sweep row; `bin/check-frontmatter --all`; every `reviews/*.md` filename at edd8015, resolved against the stem convention as instruction 4 of the part-3 directive rewrote it.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` — the audience bundler is still unbuilt, and every bundle membership in this artifact was computed from frontmatter directly, not by running it; `bin/tests/run`, whose two pre-existing failures are excluded by directive and which this cycle did not execute, so no claim is made about the state of the suite at edd8015; `docs/**`, excluded from the confirmation pass by directive, including this cycle's own directive file; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/, and every reference within them, excluded by directive; the 37 corpus files PR #135 did not change, which were read only as the other side of a sweep row and did not receive a confirmation pass; DR-25 (roles/architect-agent.md / specs/trd-template.md), which persists unchanged at edd8015 and which the directive excludes from report; the term-collision, audience-value, path-reference and retired-vocabulary sweeps, which this directive did not commission and which are therefore not re-run — no claim is made about their state at edd8015 beyond the two spot checks recorded below; whether any rule is *correct* as engineering or product judgment — this role judges coherence and safety as LLM context only; the PRD and TRD instances, which are the Spec Reviewer's and do not exist in this repository; whether decisions D1 through D12 were the right calls, which this cycle treats as settled.
Findings: 6 new — 1 blocking, 5 non-blocking — across 6 companion artifacts. All 15 of the prior cycle's dispositions are closed. This artifact carries the three sweeps (18 rows: 6 duplicate rules, 2 contradictions, 10 role boundaries), the closure table, and the confirmation-pass verdicts; per-file findings are in the six artifacts named below.
Prior cycle: reviews/corpus-regate-cycle-2.md (reviewed @ df35ea7)
Dave should inspect: SA-5 — the only blocking finding, and the only place D10's single-recipient rule did not land. Then OM-2 and DMP-5 together: both are one-line tails of the gate D9 moved, in the two `all-roles` files that reach every bundle.

---

## Scope — the 14 files in the confirmation pass

`git diff --name-only f46264b 219b0e7` returns 14 paths. None is under `docs/`, so the directive's exclusion removes nothing and the confirmation-pass set is the whole diff:

LEXICON.md · engagements/cartographer.md · engagements/critic.md · engagements/sre/baseline-measurement.md · engagements/sre/engagement-change-package.md · engagements/sre/implementer.md · engagements/sre/speed-audit.md · engagements/working-with-dave.md · operating-model.md · policies/document-metadata-policy.md · prose-criteria.md · roles/context-quality-reviewer.md · roles/writer.md · skills/review-artifact.md

## Scope — the 51-file sweep set

Unchanged from the prior cycle, and recomputed mechanically at edd8015: `bin/check-frontmatter --all` matches 36 files from nine globs and exits 0, plus `docs/global-context/*.md` (3), `engagements/**/*.md` (11), and prose-criteria.md (1). The 17 distinct `audience:` values and their file counts are identical to the prior cycle's; PR #135 changed no `audience:` line, so the fourteen bundles are unchanged and are the ones this artifact's delivery claims are computed against.

---

## Closure — the prior cycle's 15 dispositions

**15 closed · 0 still open · 0 reopened differently.**

| Finding | File | State | The landed text |
| --- | --- | --- | --- |
| OM-1 | operating-model.md | closed | operating-model.md:126 — "Methodology and other governed context documents are gated by the Context Quality Reviewer," replacing "The same gate covers any canonical document, methodology documents included." A corpus-wide grep for the old clause over the 51-file set returns nothing. Instruction 1's sweep also caught :103, now "the reviewer that gates it." See OM-2 for the role attribution on the same line. |
| CQR-4 | context-quality-reviewer.md | closed | roles/context-quality-reviewer.md:27-30 — "A governed context document reaches `agreed` only after this role's verdict is `ready`, except on the expedited path and the doc-only cycle the document metadata policy defines, which reach `agreed` without a reviewer." D9, verbatim. The carve-out the role inherited when the gate moved is now stated where the gate is. |
| CQR-3 | context-quality-reviewer.md | closed | :14-17 — "the frontmatter in-scope set, the global-context documents, the engagement documents, and the Public Prose Criteria." The three path-shaped tokens are gone and the third is named by title, which is what the artifact's Fix asked for. |
| CG-1 | cartographer.md | closed | :21-22 "Dave directs the discovery; you run it and return the report"; :28-30 and :31-33 route the access question and the ranked question list through the report to the Assistant, who triages and carries to Dave. One recipient throughout the file. The procedure content is intact. D10. |
| RA-4 | review-artifact.md | closed | skills/review-artifact.md:50-51 — "A file under a subdirectory of engagements/ or roles/ has stem `<parent-dir>-<basename>`; all others use `<basename>`." Verified by deriving a stem for all 51 corpus paths mechanically: all seven `engagements/sre/` artifacts in the tree now derive, `vendors/README.md` derives to `README` (reviews/README-cycle-4.md), and no two corpus paths collide on a stem. D11. |
| SRE-BM-4 | sre/baseline-measurement.md | closed | :9-11 — "Steps 1-5 run in a decision session by the Assistant; step 6 runs in an execution session by whichever of the Cartographer or Implementer re-measures. All three read the whole file." Every step has a runner and all three audience roles are named. No `audience:` change, per D4. See SRE-BM-5 for the one clause that names by description. |
| SA-4 | sre/speed-audit.md | closed | :9-10 — "The Cartographer, Implementer, and Critic read it for the steps assigned to them; they do not run the play." All three execution roles in the audience, named. |
| SA-1 | sre/speed-audit.md | closed (was still open from cycle 1) | :18 and :20-21 — "the Cartographer maps the pipeline, producing the System Map" and "capture per-stage distributions, producing the Measurement Baseline." Both procedure basenames are gone; both artifact terms are defined in engagements/sre/README.md:51-55, which every engagement bundle carries. |
| SA-3 | sre/speed-audit.md | closed (was reopened differently, carried as SA-4) | Resolved with SA-4. Both halves of the session-kind fix are now landed. |
| LX-2 | LEXICON.md | closed | :86-87 — "**Provenance class** — where an assertion came from. Four classes, named by Core: *observed*, *inferred*, *told*, *unknown*." Core Evidence 6's obligation sentence is deleted; the entry points at Core by title. Criterion 4 satisfied. |
| DMP-4 | document-metadata-policy.md | closed | :93-95 — "A role document is one whose first heading is `# Role:`; `engagements/working-with-dave.md` and `engagements/sre/README.md` are not role documents." The artifact's Fix, verbatim; `bin/check-frontmatter --all` still exits 0 with 36 files matched. |
| WR-5 | writer.md | closed | :17 — "state that a Critic read (advisory, reads the piece against the Public Prose Criteria) is available, and stop. Do not start it." The Context Quality Reviewer clause is dropped. This is the narrowing the directive names as WR-5's disposition, and it landed. |
| WD-2 | working-with-dave.md | closed | :10 — "This file is for decision sessions and execution sessions within an engagement," matching engagements/sre/README.md:9 and engagements/sre/override-log-policy.md:9. |
| CR-1 | critic.md | closed | :12 — "An engagement has no release gate, per the engagement README." The two duplicated sentences are cut; the full rule survives once, at engagements/sre/README.md:39-40. D12. See CR-2 for how the citation names its target. |
| PC-3 | prose-criteria.md | closed (was still open from cycle 1) | :10 — "Read by the Writer role, a decision session." Instruction 10's dictated wording. Criterion 7 is now satisfied by the file read on its own, which is what cycle 1's conditional asked for and cycle 2 recorded as unmet. |

Also confirmed closed, from the prior cycle's sweeps rather than its findings: **TC-5** — `grep -rn agreed engagements/` at edd8015 returns nothing; the four ordinary-word uses are now "given Dave's go" or the natural equivalent, and no use of `agreed` referring to a governed document's status was disturbed. **DR-23** and **DR-24** — see sweep (a). **CN-9** through **CN-13** — see sweep (b). **BD-9** — see sweep (g).

## Sweep (a) — Duplicate rules

Corpus-wide over the 51-file set. A rule stated in two or more files whose bundles overlap. Re-run mechanically as a 4-gram near-duplicate scan over all 1,142 sentences of the set at a Jaccard floor of 0.40, then read; boilerplate session-kind and reader declarations and pointer lines ("in the shape the review-artifact skill states") are not rules and are excluded, as in the prior cycle.

| # | Rule | Locations | State |
| --- | --- | --- | --- |
| DR-2r | Reconciliation charges the reviewer gate once over the whole delta, not once per edit | LEXICON.md:31-36 (the term) · policies/commit-and-change-control-policy.md:117-124 (the mechanism) | Unchanged. Deliberate two-home split, term and mechanism. |
| DR-19r | A recommendation is a next step, never a ship call; signal no-ship with `blocking` | roles/skeptic-risk-agent.md:124-126 · skills/evidence-review.md:38-39 | Unchanged. Deliberate; the skill reaches three bundles the role does not. |
| DR-20r | Retros carry no lifecycle metadata | policies/document-metadata-policy.md:36-41 · skills/conversation-retro.md:45-47 | Unchanged. Resolved as proposed at cycle 2. |
| DR-22 | Filename convention `<descriptor>-<timestamp>`, no random strings, hashes, or UUIDs | docs/global-context/core.md:33 · docs/global-context/review-rubric.md:44-46 | Unchanged. Exempted by the rubric's line 13. |
| DR-26 | Mark every material/unresolved gap with one of LEXICON's four release impact labels | roles/skeptic-risk-agent.md:101 · skills/boundary-audit.md:42 | **New to the sweep, pre-existing in the tree.** Near-verbatim; both in the `skeptic-risk-agent` bundle. Not open: both instruct the labelling without redefining the labels, which is the disposition cycle 2 recorded when it closed RA-3 over the same pattern in skills/evidence-review.md. Recorded so the standard stays visible. |
| DR-27 | "SLO status and error budget consumption for affected Top K user journeys" | operating-model.md:179 (change package item 7) · roles/release-manager-agent.md:36 (release readiness item 6) | **New to the sweep, pre-existing in the tree.** Shared by the `chief-of-staff` and `release-manager-agent` bundles. Not open: roles/release-manager-agent.md:43-44 states the relation explicitly — "This package is assembled from the change package where the change package states it, not written fresh" — so the repetition is the seam between two artifacts, declared. |

**6 rows. Prior cycle: 7. Delta −1.** DR-23 closed by D12 (instruction 8) and DR-24 by instruction 9 — those were the prior cycle's only two open rows, and both are gone. DR-25 (roles/architect-agent.md:28 / specs/trd-template.md:18, verbatim, both in the `architect-agent` bundle) persists unchanged at edd8015 and is excluded from report by directive; counting it the table would be 7 rows and the delta 0. DR-26 and DR-27 are new to the sweep and pre-existing in the tree; both are recorded as not open. **No row in this table is open.**

## Sweep (b) — Contradictions

Corpus-wide over the 51-file set. Two files, or two passages of one file, stating incompatible rules.

| # | Statement A | Statement B | Why incompatible |
| --- | --- | --- | --- |
| CN-14 | engagements/cartographer.md:28-33 — the report names the access question and carries the ranked question list; "The Assistant triages the report and carries the question to Dave" · engagements/sre/system-discovery.md:35 — "the unknowns list ready for the Assistant's triage" | engagements/sre/speed-audit.md:19 — "unknowns go to Dave; Dave decides what to ask the client" · engagements/sre/system-discovery.md:24-25 — "The unknowns become the question list for Dave" | Two recipients for one output. D10 gave the Cartographer's report one recipient, the Assistant; the fix landed in engagements/cartographer.md and in system-discovery.md's opening, and not in speed-audit.md's step 1 or in system-discovery.md's step 3. The second of these is a within-file contradiction: system-discovery.md:24-25 against its own :35. All four passages are in the `cartographer` bundle. **Open.** The speed-audit half is SA-5, in scope; the system-discovery half is outside this cycle's changed-file scope and is recorded here only. |
| CN-15 | operating-model.md:126 — "Methodology and other governed context documents are gated by the Context Quality Reviewer." | operating-model.md:126, the same line's role attribution — *(PM/EM/Owner + Architect + Spec Reviewer)* | Within one line: the prose names two gates and the roster names one reviewer. Not a rule conflict — the roster is a summary and the sentence governs — but the roster is the artifact a reader consults for the stage's roles, and it now omits the role the sentence adds. operating-model.md is `all-roles` and reaches all fourteen bundles. **Open.** OM-2. |

**2 rows, both open. Prior cycle: 5 rows, all open. Delta −3 rows, −3 open.** CN-9 closed by instruction 2 (the carve-out landed in roles/context-quality-reviewer.md), CN-10 by instruction 1, CN-11 by instruction 3, CN-12 by instruction 5, CN-13 by instruction 6. CN-7 and CN-8, recorded not-open at cycle 2, are unchanged. Spot-checked and not open: skills/spec-review-cycle.md:14-16 states the gate split in the same unconditional form the cycle-2 CQR-4 evidence flagged, and is reconciled by its own :24-25 — "This skill governs the reviewer-gated cycle only. It does not govern interactive co-authoring or artifact-pane review" — which is exactly the pair of paths D9's carve-out names.

## Sweep (g) — Role boundaries

Re-run over the 14 changed files, per directive: the role and skill documents among them, against the full role set. The prior cycle ran this over 30 files, so the row sets are not directly comparable and the delta below is stated against the prior table's count, not against a like-for-like set.

| # | Boundary | Role A | Role B | State at edd8015 |
| --- | --- | --- | --- | --- |
| BD-1 | Gating a governed methodology document | roles/context-quality-reviewer.md:34-35 — "Nothing else is" | roles/spec-reviewer-agent.md:33-35 — the PRD, TRD, ACs "and nothing else" | **Closed, and now stated the same way in four files.** operating-model.md:126 joined roles/spec-reviewer-agent.md, skills/spec-review-cycle.md and roles/context-quality-reviewer.md under instruction 1. |
| BD-2 | A read of a finished piece of public prose | roles/writer.md:17 (offers the Critic read only) | engagements/critic.md (advisory) · roles/context-quality-reviewer.md:14-17 (scope excludes public prose) | **Closed** by the WR-5 narrowing. The offer and the reviewable set now agree; no role is offered work its scope excludes. |
| BD-4 | Building the change | roles/coder-agent.md | engagements/sre/implementer.md:9-11 | **Not open** — disjoint bundles, different upstream artifact. Unchanged. |
| BD-5 | Who may override a procedural step | engagements/sre/override-log-policy.md:13-14, :34 | engagements/working-with-dave.md:36-38 | **Closed** by D1. Unchanged. |
| BD-6 | Reviewing the Implementer's own diff | engagements/sre/implementer.md:37-39 | engagements/critic.md:9-10 | **Closed.** Unchanged. |
| BD-7 | Proposing an improvement | engagements/sre/speed-audit.md:34-36 — "The Cartographer does not propose; the Implementer does not self-authorize" | engagements/cartographer.md | **Closed, now stated in one direction.** The CG-1 rewrite deleted cartographer.md's "hand that to Dave — he decides whether to do it or ask the client," which was the prior cycle's second direction. No finding: engagements/sre/speed-audit.md carries `cartographer` in its `audience:` and is in the 24-file `cartographer` bundle, so the rule still reaches the role it binds. |
| BD-8 | Emitting a ship recommendation | roles/skeptic-risk-agent.md:124-126 | roles/release-manager-agent.md:50-57 | **Not open.** Neither file is in this cycle's changed set; carried from the prior table unchanged, as DR-19r's deliberate split. |
| BD-9 | Who gates a methodology document, and what `agreed` requires | operating-model.md:126 | roles/context-quality-reviewer.md:27-30 · policies/document-metadata-policy.md:124-125, :204-205 | **Closed.** Four files, one answer: the Context Quality Reviewer gates, its `ready` precedes `agreed`, and the two named paths reach `agreed` without a reviewer. This was the prior cycle's largest finding. The one residue is that policies/document-metadata-policy.md's gate-document class list does not name roles/context-quality-reviewer.md, now that the role document states a gate — DMP-5, non-blocking. |
| BD-10 | Who receives the Cartographer's unknowns | engagements/cartographer.md:28-33 — the Assistant, who triages and carries to Dave | engagements/sre/speed-audit.md:19 — Dave directly · engagements/sre/system-discovery.md:24-25 — Dave directly | **New, and open.** Three files in the `cartographer` bundle, two answers. SA-5, CN-14. |
| BD-11 | Who re-measures after a change | engagements/cartographer.md (read-only; no measurement duty stated) | engagements/sre/implementer.md:23-31 (five responsibilities; re-measurement not among them) | **New, and open.** engagements/sre/baseline-measurement.md:9-11 assigns step 6 to "whichever of the Cartographer or Implementer re-measures" and no document in any engagement bundle says which. SRE-BM-5. |
| BD-12 | Who reads the engagement change package | engagements/sre/engagement-change-package.md:9-10 — the Assistant | engagements/critic.md — in the file's `audience:`, and the subject of its item 6 | **New, and open.** An enumerative reader clause omitting a role in its own audience — SA-4's defect in a sibling file. SRE-ECP-4. |

**10 rows, 3 open. Prior cycle: 9 rows, 1 open (BD-9), over a 30-file set. Delta +1 row, +2 open.** All four of the prior cycle's closed-this-cycle rows stayed closed, and BD-9 — the prior cycle's single open row and its largest finding — is closed. The three new open rows are all in the engagement pack, and all three are the same shape: a role in a file's audience whose relation to the file is stated by description, by omission, or not at all.

## Confirmation pass — one line per file

14 files. 8 clean, 6 with findings. A clean line means the file was read whole against all eleven criteria at edd8015 and nothing in it fails at the current foundation; cross-file matters are in the sweeps above and are not counted against the file here.

| File | Verdict | Findings | Artifact |
| --- | --- | --- | --- |
| engagements/sre/speed-audit.md | changes-required | 1 blocking | reviews/sre-speed-audit-cycle-3.md |
| operating-model.md | ready-with-findings | 1 non-blocking | reviews/operating-model-cycle-7.md |
| policies/document-metadata-policy.md | ready-with-findings | 1 non-blocking | reviews/document-metadata-policy-cycle-16.md |
| engagements/sre/baseline-measurement.md | ready-with-findings | 1 non-blocking | reviews/sre-baseline-measurement-cycle-3.md |
| engagements/sre/engagement-change-package.md | ready-with-findings | 1 non-blocking | reviews/sre-engagement-change-package-cycle-2.md |
| engagements/critic.md | ready-with-findings | 1 non-blocking | reviews/critic-cycle-2.md |
| LEXICON.md | ready | none | — |
| engagements/cartographer.md | ready | none | — |
| engagements/sre/implementer.md | ready | none | — |
| engagements/working-with-dave.md | ready | none | — |
| prose-criteria.md | ready | none | — |
| roles/context-quality-reviewer.md | ready | none | — |
| roles/writer.md | ready | none | — |
| skills/review-artifact.md | ready | none | — |

---

## The single largest remaining problem

**The Cartographer's report has one recipient in its role document and another in the document that describes the whole engagement.** D10 settled it — the report goes to the Assistant, who triages and carries questions to Dave — and instruction 3 conformed engagements/cartographer.md completely. engagements/sre/speed-audit.md:19 still reads "unknowns go to Dave; Dave decides what to ask the client," and engagements/sre/system-discovery.md:24-25 still reads "The unknowns become the question list for Dave" against its own :35, "the unknowns list ready for the Assistant's triage." All three files are in the 24-file `cartographer` bundle. It is the same failure mode as the cycle-2 winner and a smaller instance of it: a decision executed exactly where its instruction named, in a corpus where the same fact is stated in three places. It is one clause in each of two files, and only one of the two is in this cycle's changed-file scope.

## Departures from the directive

Two, both in what could be claimed rather than what was done.

1. **The sweeps are three, not seven, and the un-run four are named rather than estimated.** The directive commissions contradictions and duplicate rules corpus-wide, and role boundaries over the changed files. The prior cycle ran seven. Term collisions, audience values, path references and retired vocabulary are therefore not re-run, and this artifact makes no claim about their state at edd8015 — they are listed in `Not inspected`. Two spot checks were run because a fix in this pull request touched their subject and a silent regression would have been invisible: `grep -rn agreed engagements/` returns nothing (TC-5), and the 17 `audience:` values and their counts are identical to the prior cycle's (sweep d), PR #135 having changed no `audience:` line.

2. **The role-boundaries delta is stated against the prior table's row count, not against a like-for-like set.** The directive scopes this sweep to the changed files, and the changed set is 14 files where the prior cycle's was 30. A row count over 14 files is not comparable to one over 30; both numbers are given in the sweep note and the incomparability is stated there rather than absorbed into a delta.

Also noted, and not acted on: `bin/check-frontmatter --all` exits 0 at edd8015, reporting 36 files matched from 9 globs. `bin/tests/run` was not executed this cycle and no claim is made about it. The path-shaped tokens instruction 4 introduced into skills/review-artifact.md — `engagements/` and `roles/` in the stem rule — are structural in a document whose subject is filenames, on the same reading the prior two cycles applied to policies/document-metadata-policy.md, and the wording is the artifact Fix cycle 2 wrote; no finding is raised.

No document was edited. No status was flipped. No finding was resolved.
