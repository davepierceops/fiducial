# Rule clusters — Pass 2

Derived artifact. Input: docs/rule-register/rule-register-20260825T1435.md @ 6d2744b. Analysis only; no edits proposed to governed files.

Rows read: 878. Clustered rows: 220. Clusters: 77 (8 divergent, 69 agreeing). Cross-file: 55. Intra-file: 22.

Method notes. (1) The clustering rule "different `binds` values are not the same rule unless one is `all`" is applied with one extension, stated here so it is auditable: a session-kind bind (`decision`, `execution`) is treated as covering the roles that run as that session kind, the way `all` covers everyone — e.g. `decision` covers `chief-of-staff`. Clusters relying on this: C038, C055, C024, C030. (2) Four rows each state two rules and appear in two clusters (R0134, R0212, R0264, R0821); the clustered-rows count is unique rows. (3) A reviewer-side row that checks a rule other rows enact (e.g. a rubric criterion) is clustered with the enacting rows and marked agreeing.

## Divergent clusters, cross-file, largest first

### C001 — Disagreeing sources are surfaced, never resolved by the agent
Rows: R0018 (core.md:25), R0019 (core.md:25), R0094 (review-rubric.md:62), R0492 (source-of-truth-policy.md:49), R0494 (source-of-truth-policy.md:54), R0495 (source-of-truth-policy.md:55), R0496 (source-of-truth-policy.md:58), R0497 (source-of-truth-policy.md:60)
Divergence: core says surface the disagreement and carry on; for a canonical/derived conflict the source-of-truth policy makes it a hard stop — stop work on the item and wait for Dave — so an agent following core alone would keep working where the policy forbids it.
Proposed home: docs/global-context/core.md

### C002 — Every material gap carries a release-impact label
Rows: R0117 (LEXICON.md:66), R0264 (testing-and-verification.md:35), R0511 (verification-boundary-policy.md:101), R0675 (skeptic-risk-agent.md:102), R0731 (test-designer-agent.md:27), R0753 (boundary-audit.md:42), R0821 (evidence-review.md:43)
Divergence: R0264's checklist question offers only three labels ("blocking, deferred, or accepted"), omitting `not-material`; an agent answering that checklist cannot record the fourth label the other six rows require.
Proposed home: LEXICON.md

### C003 — Tests are written and confirmed failing before implementation (red-gate)
Rows: R0139 (operating-model.md:20), R0187 (operating-model.md:130), R0194 (operating-model.md:137), R0198 (operating-model.md:141), R0237 (spec-and-change-discipline.md:31), R0730 (test-designer-agent.md:26), R0874 (test-plan-review.md:37)
Divergence: R0237 requires the red to be behavioral — tests must fail on wrong logic, not on an absent import — for anything beyond trivial fixes; the other rows accept any confirmed failure, so a missing-module red passes them and fails R0237.
Proposed home: operating-model.md

### C004 — A retro closes the session
Rows: R0054 (decision-layer.md:31), R0786 (conversation-retro.md:24), R0787 (conversation-retro.md:26), R0788 (conversation-retro.md:28)
Divergence: decision-layer ends every session with a retro; the retro skill scopes it to ended project decision sessions with durable lessons and forbids retros on reviewer-gated cycle conversations unless directed — after a cycle conversation the two texts order opposite actions.
Proposed home: docs/global-context/decision-layer.md

### C005 — A directive states its required parts every time
Rows: R0037 (core.md:50), R0082 (review-rubric.md:45), R0134 (LEXICON.md:131)
Divergence: core requires route, model tier, AND the execution block "all three stated every time"; the rubric checks only "route and model"; LEXICON says route and model tier and "there is no third part" — a rubric reviewer would pass a directive that core rejects for lacking an execution block.
Proposed home: docs/global-context/core.md

### C006 — Definition of the `blocking` release-impact label
Rows: R0118 (LEXICON.md:69), R0460 (release-readiness-policy.md:14), R0677 (skeptic-risk-agent.md:105)
Divergence: LEXICON makes any gap awaiting Dave's judgment `blocking`; the Skeptic role reserves `blocking` "for gaps the governing policies prohibit" — narrower, so a Skeptic following its role doc would not block a gap LEXICON says must block.
Proposed home: LEXICON.md

### C007 — Propagating a changed fact across documents
Rows: R0026 (core.md:32), R0499 (source-of-truth-policy.md:65)
Divergence: core orders the agent to find and UPDATE every place stating the changed fact, in every document; source-of-truth orders the agent to FLAG which derived artifacts need updating — on a canonical-document change the two prescribe different acts (edit vs surface), and updating other governed documents can itself be barred outside a cycle.
Proposed home: docs/global-context/core.md

### C008 — Format of a clean review pass
Rows: R0021 (core.md:26), R0835 (review-artifact.md:83)
Divergence: core says a clean pass "says so in one line"; the review-artifact schema requires the full header block and nothing else — a one-line clean pass violates the schema, and a header-only artifact is not one line.
Proposed home: docs/global-context/core.md

## Agreeing clusters, cross-file, largest first

### C009 — Escalate for human code inspection on the named triggers
Rows: R0218 (operating-model.md:229), R0294 (human-review-boundary.md:28), R0295 (human-review-boundary.md:29), R0296 (human-review-boundary.md:30), R0297 (human-review-boundary.md:31), R0298 (human-review-boundary.md:32), R0299 (human-review-boundary.md:33), R0300 (human-review-boundary.md:34), R0301 (human-review-boundary.md:35)
Proposed home: operating-model.md

### C010 — Every meaningful mock answers the six-question boundary checklist
Rows: R0260–R0265 (testing-and-verification.md:31–36), R0507 (verification-boundary-policy.md:29)
Proposed home: context-sets/testing-and-verification.md

### C011 — Spec Reviewer gates PRD/TRD/ACs; Context Quality Reviewer gates everything else
Rows: R0182 (operating-model.md:126), R0183 (operating-model.md:126), R0600 (context-quality-reviewer.md:35), R0691 (spec-reviewer-agent.md:34), R0844 (spec-review-cycle.md:14)
Proposed home: operating-model.md

### C012 — Green tests do not make a change done or shippable
Rows: R0173 (operating-model.md:95), R0210 (operating-model.md:203), R0618 (release-manager-agent.md:62), R0662 (skeptic-risk-agent.md:86)
Proposed home: operating-model.md

### C013 — Consequential changes need Dave's explicit go/no-go; routine flows on evidence
Rows: R0193 (operating-model.md:135), R0200 (operating-model.md:150), R0201 (operating-model.md:152), R0303 (commit-and-change-control-policy.md:20)
Proposed home: policies/commit-and-change-control-policy.md

### C014 — Status flips land as frontmatter-only status-transition commits
Rows: R0393 (document-metadata-policy.md:124), R0412 (document-metadata-policy.md:208), R0861 (spec-review-cycle.md:76), R0866 (spec-review-cycle.md:92)
Proposed home: policies/document-metadata-policy.md

### C015 — Spec territory never overlaps: one delta per document, two tranches at most
Rows: R0107 (LEXICON.md:38), R0243 (spec-and-change-discipline.md:57), R0245 (spec-and-change-discipline.md:62), R0581 (chief-of-staff.md:105)
Proposed home: context-sets/spec-and-change-discipline.md

### C016 — `agreed` requires a qualifying review artifact at the cited SHA
Rows: R0374 (document-metadata-policy.md:78), R0376 (document-metadata-policy.md:81), R0407 (document-metadata-policy.md:196), R0599 (context-quality-reviewer.md:27)
Proposed home: policies/document-metadata-policy.md

### C017 — The gate attaches to exposure/release, not commit or merge (definitions)
Rows: R0199 (operating-model.md:146), R0204 (operating-model.md:163), R0335 (commit-and-change-control-policy.md:112), R0336 (commit-and-change-control-policy.md:113)
Proposed home: policies/commit-and-change-control-policy.md

### C018 — Every verification claim carries an evidence class / states its boundary
Rows: R0108 (LEXICON.md:43), R0170 (operating-model.md:89), R0255 (testing-and-verification.md:17), R0510 (verification-boundary-policy.md:100)
Proposed home: LEXICON.md

### C019 — Specifications are canonical (definitions)
Rows: R0143 (operating-model.md:34), R0234 (spec-and-change-discipline.md:21), R0479 (source-of-truth-policy.md:19), R0480 (source-of-truth-policy.md:20)
Proposed home: policies/source-of-truth-policy.md

### C020 — Reconciliation closes a delta; the gate runs once over the accumulated diff (definitions)
Rows: R0103 (LEXICON.md:31), R0184 (operating-model.md:127), R0337 (commit-and-change-control-policy.md:119)
Proposed home: LEXICON.md

### C021 — Generated filenames are descriptor-timestamp unless a stated convention names the file
Rows: R0027 (core.md:33), R0028 (core.md:33), R0084 (review-rubric.md:47)
Proposed home: docs/global-context/core.md

### C022 — Adopting projects install their own frontmatter enforcement
Rows: R0361 (document-metadata-policy.md:47), R0451 (project-setup-requirements.md:44), R0452 (project-setup-requirements.md:47)
Proposed home: unsure

### C023 — Escalate spec/requirement ambiguity to Dave
Rows: R0212 (operating-model.md:223), R0570 (chief-of-staff.md:69), R0586 (chief-of-staff.md:119)
Proposed home: operating-model.md

### C024 — Live tests do not belong in every fast/unit run
Rows: R0289 (testing-and-verification.md:258), R0524 (verification-boundary-policy.md:139), R0656 (skeptic-risk-agent.md:57)
Proposed home: context-sets/testing-and-verification.md

### C025 — Mocked evidence never supports live-behavior claims
Rows: R0175 (operating-model.md:97), R0663 (skeptic-risk-agent.md:87), R0673 (skeptic-risk-agent.md:97)
Proposed home: operating-model.md

### C026 — A headless DOM is not browser verification
Rows: R0286 (testing-and-verification.md:255), R0649 (skeptic-risk-agent.md:47), R0664 (skeptic-risk-agent.md:88)
Proposed home: context-sets/testing-and-verification.md

### C027 — Reviews state what was and was not inspected
Rows: R0093 (review-rubric.md:62), R0627 (reviewer-agent.md:26), R0832 (review-artifact.md:75)
Proposed home: skills/review-artifact.md

### C028 — Every meaningful mock has a declared verification boundary
Rows: R0282 (testing-and-verification.md:246), R0504 (verification-boundary-policy.md:20), R0512 (verification-boundary-policy.md:109)
Proposed home: policies/verification-boundary-policy.md

### C029 — Review procedures output the review-artifact shape
Rows: R0754 (boundary-audit.md:46), R0821 (evidence-review.md:43), R0878 (test-plan-review.md:44)
Proposed home: unsure

### C030 — No ship call from skeptic/evidence review; `blocking` is the no-ship signal
Rows: R0682 (skeptic-risk-agent.md:130), R0683 (skeptic-risk-agent.md:131), R0820 (evidence-review.md:38)
Proposed home: roles/skeptic-risk-agent.md

### C031 — `audience:` takes role slugs or the reserved values only
Rows: R0071 (review-rubric.md:22), R0382 (document-metadata-policy.md:93), R0385 (document-metadata-policy.md:99)
Proposed home: policies/document-metadata-policy.md

### C032 — No random strings, hashes, or UUIDs as filenames
Rows: R0029 (core.md:33), R0085 (review-rubric.md:49)
Proposed home: docs/global-context/core.md

### C033 — Force-push to the default branch is denied
Rows: R0331 (commit-and-change-control-policy.md:91), R0444 (project-setup-requirements.md:27)
Proposed home: policies/commit-and-change-control-policy.md

### C034 — Unreviewed spec text never reaches the default branch
Rows: R0105 (LEXICON.md:35), R0338 (commit-and-change-control-policy.md:126)
Proposed home: unsure

### C035 — One-time per-document disposition list recorded at adoption
Rows: R0379 (document-metadata-policy.md:87), R0456 (project-setup-requirements.md:65)
Proposed home: policies/document-metadata-policy.md

### C036 — Ask one question at a time, then wait
Rows: R0038 (decision-layer.md:14), R0561 (chief-of-staff.md:42)
Proposed home: docs/global-context/decision-layer.md

### C037 — Directives are self-contained
Rows: R0060 (decision-layer.md:36), R0803 (directive-authoring.md:13)
Proposed home: docs/global-context/decision-layer.md

### C038 — Mid-delta directives cite the spec branch and pin its SHA
Rows: R0241 (spec-and-change-discipline.md:53), R0580 (chief-of-staff.md:102)
Proposed home: context-sets/spec-and-change-discipline.md

### C039 — Model selection speaks in tiers, not model names
Rows: R0062 (decision-layer.md:37), R0081 (review-rubric.md:44)
Proposed home: docs/global-context/decision-layer.md

### C040 — "Prompt" is not a term of this methodology
Rows: R0033 (core.md:45), R0130 (LEXICON.md:105)
Proposed home: docs/global-context/core.md

### C041 — "Track" does not appear in directives
Rows: R0083 (review-rubric.md:45), R0134 (LEXICON.md:131)
Proposed home: LEXICON.md

### C042 — Verification reporting expands the standard response shape, not a second shape
Rows: R0209 (operating-model.md:188), R0280 (testing-and-verification.md:229)
Proposed home: operating-model.md

### C043 — Definition: contract-verified
Rows: R0110 (LEXICON.md:48), R0271 (testing-and-verification.md:46)
Proposed home: LEXICON.md

### C044 — Definition: live-verified
Rows: R0111 (LEXICON.md:50), R0272 (testing-and-verification.md:48)
Proposed home: LEXICON.md

### C045 — Definition: browser-verified
Rows: R0112 (LEXICON.md:52), R0273 (testing-and-verification.md:50)
Proposed home: LEXICON.md

### C046 — Definition: production-verified
Rows: R0113 (LEXICON.md:54), R0274 (testing-and-verification.md:52)
Proposed home: LEXICON.md

### C047 — Definition: a mock is a claim with its proof elsewhere
Rows: R0259 (testing-and-verification.md:27), R0505 (verification-boundary-policy.md:22)
Proposed home: unsure

### C048 — Agreement attaches at reconciliation, to the version of record (definitions)
Rows: R0104 (LEXICON.md:34), R0140 (operating-model.md:20)
Proposed home: LEXICON.md

### C049 — The Chief of Staff operates as a decision session (definitions)
Rows: R0148 (operating-model.md:47), R0551 (chief-of-staff.md:10)
Proposed home: roles/chief-of-staff.md

### C050 — Chief of Staff proposes tranches for Dave's approval
Rows: R0146 (operating-model.md:45), R0568 (chief-of-staff.md:65)
Proposed home: roles/chief-of-staff.md

### C051 — Chief of Staff decomposes an approved tranche into ordered change packages
Rows: R0147 (operating-model.md:46), R0569 (chief-of-staff.md:67)
Proposed home: roles/chief-of-staff.md

### C052 — Acceptance criteria derive from the PRD and are Dave's (definitions)
Rows: R0152 (operating-model.md:57), R0481 (source-of-truth-policy.md:21)
Proposed home: policies/source-of-truth-policy.md

### C053 — The architecture summary is per-change and derived from the TRD (definitions)
Rows: R0482 (source-of-truth-policy.md:22), R0547 (architect-agent.md:39)
Proposed home: unsure

### C054 — Tracker issues are derived views onto the specs (definitions)
Rows: R0144 (operating-model.md:34), R0483 (source-of-truth-policy.md:24)
Proposed home: policies/source-of-truth-policy.md

### C055 — The first response is the artifact/state, not a plan
Rows: R0047 (decision-layer.md:23), R0553 (chief-of-staff.md:19)
Proposed home: docs/global-context/decision-layer.md

## Intra-file clusters

All 22 intra-file clusters agree; none diverge. Most are deliberate summary-plus-expansion or body-plus-checklist restatements within one file.

### C056 — Escalation triggers: summary line restated as a list (operating-model.md)
Rows: R0172 (operating-model.md:91), R0212 (operating-model.md:223), R0213 (operating-model.md:224), R0215 (operating-model.md:226)

### C057 — Sync commands name remote and ref; exit status checked (command-blocks.md)
Rows: R0761 (command-blocks.md:38), R0762 (command-blocks.md:43), R0763 (command-blocks.md:44), R0780 (command-blocks.md:101)

### C058 — One purpose per block, no placeholders (command-blocks.md)
Rows: R0770 (command-blocks.md:77), R0771 (command-blocks.md:77), R0781 (command-blocks.md:103)

### C059 — Expected output below the block, blast radius above (command-blocks.md)
Rows: R0772 (command-blocks.md:80), R0773 (command-blocks.md:80), R0782 (command-blocks.md:104)

### C060 — A block runs verbatim, no manual steps (command-blocks.md)
Rows: R0755 (command-blocks.md:17), R0775 (command-blocks.md:89)

### C061 — Evidence-producing blocks capture output to a named path (command-blocks.md)
Rows: R0757 (command-blocks.md:23), R0777 (command-blocks.md:95)

### C062 — The block must be copyable whole (command-blocks.md)
Rows: R0764 (command-blocks.md:48), R0778 (command-blocks.md:97)

### C063 — A block cannot terminate the shell it is pasted into (command-blocks.md)
Rows: R0768 (command-blocks.md:66), R0779 (command-blocks.md:98)

### C064 — Whoever produces an artifact does not approve/gate it (operating-model.md)
Rows: R0176 (operating-model.md:102), R0177 (operating-model.md:103)

### C065 — Nothing is built without written acceptance criteria (operating-model.md)
Rows: R0138 (operating-model.md:20), R0185 (operating-model.md:128)

### C066 — A content edit to an agreed document flips it to in-review (document-metadata-policy.md)
Rows: R0391 (document-metadata-policy.md:119), R0395 (document-metadata-policy.md:128)

### C067 — Any finding escalates a lighter path to a full cycle (document-metadata-policy.md)
Rows: R0404 (document-metadata-policy.md:182), R0420 (document-metadata-policy.md:235)

### C068 — Lighter agreement paths exclude documents under specs/ (document-metadata-policy.md)
Rows: R0402 (document-metadata-policy.md:176), R0423 (document-metadata-policy.md:245)

### C069 — Definition: deferred = postponed with a named mechanism (LEXICON.md)
Rows: R0115 (LEXICON.md:59), R0120 (LEXICON.md:72)

### C070 — Log entries are never edited or deleted (decision-log-policy.md)
Rows: R0343 (decision-log-policy.md:23), R0351 (decision-log-policy.md:56)

### C071 — Decision IDs advance in steps of ten (decision-log-policy.md)
Rows: R0344 (decision-log-policy.md:36), R0348 (decision-log-policy.md:44)

### C072 — Secret values are never stated or entered into context (core.md)
Rows: R0001 (core.md:14), R0003 (core.md:14)

### C073 — A file failing the rubric is proposed for retirement (review-rubric.md)
Rows: R0066 (review-rubric.md:12), R0087 (review-rubric.md:53)

### C074 — A lighter-path content commit touches exactly one document (document-metadata-policy.md)
Rows: R0396 (document-metadata-policy.md:139), R0428 (document-metadata-policy.md:263)

### C075 — Each review cycle starts a fresh conversation (spec-review-cycle.md)
Rows: R0845 (spec-review-cycle.md:29), R0846 (spec-review-cycle.md:32)

### C076 — Dave does not read diffs / act as primary reviewer by default (operating-model.md)
Rows: R0136 (operating-model.md:18), R0157 (operating-model.md:65), R0158 (operating-model.md:66)

### C077 — Material boundary gaps discharged before release (verification-boundary-policy.md)
Rows: R0530 (verification-boundary-policy.md:160), R0531 (verification-boundary-policy.md:165)

## Verification

The 10 largest clusters (C009, C001, C002, C003, C010, C011, C056, C012, C013, C014) were re-checked member-by-member against each row's `source`; every divergent cluster's divergence was confirmed visible in `source` text, not only in the `rule` paraphrase. Two clusters were split during verification, none dissolved:

- C009: R0217 ("reviewers disagree materially" — a general escalation, not an escalation *for code inspection*) was removed; its obligation differs from the human-review-boundary triggers.
- C056: R0214 ("evidence is insufficient") was removed; R0172's summary line covers product, risk, and release decisions but not evidence sufficiency, so the rows are not restatements.

## Register rows that could not be placed as written

- R0129 — the paraphrase matches the source, but `binds: execution` does not: the source ("the TRD sets SLO targets against it and does not redefine it") binds whoever authors the TRD, which roles/architect-agent.md:10 places in a *decision* session for the standing TRD. The binds value blocked otherwise-plausible pairings with architect rows.
- R0473 — the paraphrase resolves an ambiguity the source does not settle: the source says a timed-out read-back "is the second" failure yet also "fires immediately, at the first failure"; the row states only the second reading. The row could not be clustered with confidence against the other failure-counting rows.
