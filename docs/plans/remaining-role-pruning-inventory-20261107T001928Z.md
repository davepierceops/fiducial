# Remaining role-rule cleanup — inventory and rulings

Baseline: `2be5327e9704b0066eed7e8ef44302aa55179b18`. Generated 20261107T001928Z (UTC).

Dave asked to inventory the remaining role-specific rules against completed pruning rulings, then resume one-by-one cleanup. This authorizes inspection and proposal preparation, not blanket retirement. Risk tiers (#430), Jev (#431), review-policy redesign (#427), SLO/Top K reconsideration (#428), and tracker portability (#425) remain separate. Current CI policy stays unchanged.

## Coverage accounting

- 269 live rows: 57 have an individual ruling or explicit deferral in the completed pruning passes.
- 117 remaining rows apply to exactly one role.
- 58 remaining rows apply to multiple roles; count them once, not once per generated role file.
- 37 additional definitions remain outside the completed root-definition review.

These are inventory counts, not deletion targets or a promise of that many new decisions. Some entries are agent descriptions, skill-routing records or hooks; some requirements were already retained as part of a procedure-level ruling even though their source wording was not individually reviewed. Preserve those obligations unless the human explicitly changes them. No claim is made that these rows have never been reviewed historically.

Method and exact per-row status are in the companion JSON. The shared-rule record’s named leading-ID decisions and modified live source paths identify its covered rows; the later manifests supply retained, shortened, successor, hook-only and deferred records. Source/skill duplicates are checked by actual emitted behavior, and role scope differences remain meaningful.

## Remaining single-role rows

| Role | Count | Rows |
|---|---:|---|
| chief-of-staff | 3 | R0481, R0934, R1485 |
| architect-agent | 7 | R0091, R0499, R0500, R0501b, R0863, R0876, R1618 |
| coder-agent | 6 | R0485, R0939, R0940, R0941, R0942, R0943 |
| test-designer-agent | 6 | R0478, R1141, R1143, R1151, R1155, R1156 |
| context-quality-reviewer | 6 | R0264, R0266, R0284, R0944, R0950, R1621 |
| spec-reviewer-agent | 5 | R1107, R1116, R1122, R1133, R1619 |
| reviewer-agent | 2 | R0807, R1056 |
| skeptic-risk-agent | 4 | R1088, R1090, R1091, R1620 |
| release-manager-agent | 6 | R0502, R0503, R0809, R1031, R1032, R1044 |
| writer | 10 | R1162, R1163, R1164, R1165, R1167, R1168, R1169, R1171, R1173, R1174 |
| copy-editor | 39 | R0954, R0955, R0956, R0957, R0958, R0959, R0960, R0961, R0962, R0963, R0964, R0965, R0966, R0967, R0968, R0969, R0970, R0971, R0972, R0973, R0975, R0976, R0977, R0979, R0980, R0981, R0982, R0983, R0984, R0985, R0987, R0988, R0990, R0991, R0992, R0993, R0994, R0997, R0998 |
| critic | 23 | R1002, R1004, R1005, R1006, R1007, R1008, R1009, R1011, R1012, R1013, R1015, R1016, R1017, R1018, R1019, R1020, R1021, R1022, R1023, R1024, R1026, R1027, R1028 |

## Remaining shared rows

| Topic | Rows |
|---|---|
| change-flow | R0090, R0472, R0486, R1473, R1478, R1479, R1480, R1489 |
| coder-agent | R0106 |
| core | R0199 |
| decision-layer | R0259 |
| decision-log-policy | R0583, R0592, R1603 |
| intake | R1605 |
| public-prose-criteria | R0817, R0818, R0819, R0820, R0821, R0829, R0830, R0831, R0832, R0833, R0835, R0844, R0846, R0849, R0853, R0854 |
| release-manager-agent | R0527 |
| remote-write-verification-policy | R0720 |
| retro | R1237, R1241, R1244, R1249, R1270 |
| review-artifact-schema | R1408, R1448, R1622 |
| spec | R0862b, R1573 |
| verification | R0070, R0073, R0158, R0159 |
| verification-boundaries | R0800 |
| voice | R1577, R1579, R1585, R1587, R1588, R1591, R1594, R1598, R1600, R1604 |

## Remaining definitions

R0004, R0006, R0009, R0029, R0031, R0037, R0038, R0040, R0057, R0067, R0083, R0131, R0133, R0135, R0137, R0139, R0150, R0175, R0176, R0189, R0200, R0220, R0247, R0464, R0465, R0493, R0531, R0580, R0594, R0604, R0716, R0782, R0785, R0845, R0893, R1010, R1474.

## Known procedure-level coverage

- R0485: Build ruling 1 preserves green/mechanical behavior; no individual source wording ruling.
- R0478: Build ruling 1 preserves meaningful red tests; no individual source wording ruling.
- R0486: Build ruling 1 preserves test-author/implementer separation; policy redesign deferred.
- R0502: Release ruling 35 preserves required package fields; source unchanged.
- R0503: Release ruling 35 preserves test-plan/results details; source unchanged.
- R1032: Release ruling 35 preserves evidence/readiness requirements; source unchanged.
- R1044: Release ruling 35 preserves missing-source-as-gap requirement; source unchanged.
- R0944: Intake procedure retained; artifact behavior remains governed.
- R0934: Existing intake branch hook; metadata/mechanism is not removable prose.

## Explicit deferrals

- R0064: #425; unchanged pending that work. Related policy machinery also remains reserved to its separate review, even when not individually named here.
- R0129: #428; unchanged pending that work. Related policy machinery also remains reserved to its separate review, even when not individually named here.
- R0130: #428; unchanged pending that work. Related policy machinery also remains reserved to its separate review, even when not individually named here.
- R0152: #427; unchanged pending that work. Related policy machinery also remains reserved to its separate review, even when not individually named here.
- R0558: #427; unchanged pending that work. Related policy machinery also remains reserved to its separate review, even when not individually named here.
- R1183: #428; unchanged pending that work. Related policy machinery also remains reserved to its separate review, even when not individually named here.

## Proposed review sequence

1. Coder and Test Designer: start with clear duplication of the shared evidence rules; preserve the current test-first/separation policy.
2. Architect and Spec Reviewer: shorten design/completeness obligations while retaining deferred SLO content unless separately authorized.
3. Context Quality Reviewer and remaining release/review role instructions.
4. Shared software/workflow residue and cross-role overlaps.
5. Writer, Copy Editor and Critic, including near-identical role rows and shared prose/voice rules.
6. Remaining definitions and other skill content, coordinated with the above so removed instructions do not reappear through generation.

All steps use source rows; regeneration and full output comparison occur at batch finalization. Continue exact approved wording, retain original archives with valid successor/decision references, and obtain required independent review before landing. No live or installed source change has been made for this inventory.

## First proposal — R0943

Current: “Do not remove meaningful coverage without explaining why.”

Recommend retirement into R0110, whose first sentence requires keeping verification aligned with approved requirements and justifying changes to checks against those requirements. R0110 covers all of R0943’s Coder/execution/software-and-writing scope. This removes the duplicate sentence without permitting unexplained coverage removal or changing test policy. DEC-001690 records the earlier shared-evidence consolidation. No active process/rule citation to R0943 was found beyond its own ID.

Status: approved and applied on the intake branch; see ruling 1. Installed context remains unchanged until batch finalization.

## Human rulings

1. R0943: Dave answered “y” to retiring the Coder coverage-removal rule into unchanged R0110. Archive the original body and metadata unchanged except `retired: R0110`. R0110 covers the full Coder/execution/software-and-writing scope and requires justification of changes to checks against approved requirements. No active rule/process references need rewriting. This removes a duplicate sentence without changing testing policy. The inventory JSON remains the fixed baseline accounting, not a live count after rulings. R0940 is next for discussion; no change to it is approved yet.

2. R0940: Dave answered “yes” to retiring the small/coherent-change preference without replacement. This explicitly removes the general size preference; the approved-spec, test-plan and unit-of-work obligations remain. No active rule/process citation to R0940 was found beyond its own ID. Keep the original source intact until batch finalization allocates the actual retirement decision; then archive it without changing its original body or metadata except the retirement reference, and verify its prose is removed rather than relocated. R0941 is next for discussion; no change to it is approved yet.

3. R0941: Dave answered “y” to keeping the existing-behavior rule unchanged: “Preserve existing behavior unless you were asked to change it.” Preserve body and metadata. This retains an explicit compatibility obligation for behavior not enumerated by the spec or test plan, including during refactoring. R0942 is next for discussion; no change to its red-gate handoff requirement is approved yet.

4. R0942: Dave answered “y” to keeping the test-handoff rule unchanged. Preserve its body, stop condition and Coder/execution/software-and-writing scope. The Test Designer’s evidence obligation remains separate from the receiving Coder’s responsibility to flag missing confirmation or import-only failures rather than proceed. Whether every change needs this handoff remains part of later risk-tier/review-policy work, not this cleanup. R0485 is next for wording review; no change to it is approved yet.

5. R0485: Dave answered “y” to replacing the body with: “Write the minimum code needed to pass the tests and mechanical checks.” Preserve metadata, including the condition that the unit’s tests are confirmed red, and the Coder/execution/software scope. Mechanical checks retain their existing lint/type/static-analysis meaning; no test-first, minimum-code or passing-check requirement changes. This shortens the survivor retained by DEC-001310 without changing that consolidation. R0939, the Coder’s emitted agent description, is next for discussion; no change to it is approved yet.

6. R0939: Dave answered “y” to keeping the Coder agent description unchanged: “Implement changes according to the spec and the test plan.” Preserve metadata and its agent-description block. This retains the concise native description established by DEC-001270. The six Coder-only inventory rows now have rulings; shared rows affecting the Coder remain in the inventory. R1141, the Test Designer’s agent description, is next for discussion; no change to it is approved yet.

7. R1141: Dave answered “y” to keeping the Test Designer agent description unchanged: “Define how correctness will be evaluated, and what evidence it requires, before implementation begins.” Preserve metadata and agent-description block. R1143, the test-plan checklist, is next for discussion; no change to it is approved yet. Its software-and-writing execution scope differs from the verification-checklists skill’s software-only planning section, and its explicit affected-Top-K SLO verification requirement remains within the deferred #428 policy.

8. R1143: Dave answered “y” to replacing the six-bullet checklist with: “Design tests from the acceptance criteria and spec’s testable claims. Choose appropriate test levels; identify mocked dependencies, required live/browser checks, and SLO verification for each affected Top K user journey; specify failure cases.” Preserve metadata and its Test Designer/execution/software-and-writing scope. Retain all six requirements; the SLO requirement remains pending the separate #428 review. The software-only planning section of verification-checklists does not replace the row’s full corpus scope. R0478 is next for discussion; no change to its meaningful-red-test requirement is approved yet.

9. R0478: Dave answered “y” to keeping the Test Designer’s meaningful-red-test requirement unchanged. Preserve the original wording and metadata, including its open-spec-branch condition and software-only execution scope. This assigns writing/running the tests and confirming bad-logic failures to the Test Designer; R0942 separately checks the evidence at the Coder handoff. Test-first policy remains for later risk-tier work. R1151, labeling gaps during test planning, is next for discussion; no change to it is approved yet.

10. R1151: Dave answered “y” to keeping the test-plan gap labeling rule unchanged: “Mark each gap the test plan leaves open with its release-impact label.” Preserve metadata and Test Designer/execution/software-and-writing scope. Its planning-stage obligation is distinct from the verification skill’s release-decision labeling trigger. R1155, reporting an inability to derive tests as a spec finding, is next for discussion; no change to it is approved yet.

11. R1155: Dave answered “y” to replacing the body with: “Report a spec finding when an unstated contract or untestable claim prevents deriving a test.” Preserve metadata, including the inability-to-derive-test condition and Test Designer/execution/software-and-writing scope. The trigger and required spec finding are unchanged. R1156, the Test Designer’s test-only editing boundary and hook, is next for discussion; no prose or enforcement change to it is approved yet.

12. R1156: Dave answered “y” to replacing only the emitted prose with: “Edit only tests. Report needed changes elsewhere as findings.” Preserve metadata, the entire YAML hook block, and the Human note unchanged. This shortens the editing-boundary/finding instruction established by DEC-001240 without changing its test-only edit scope, hook configuration, or reporting responsibility. All six Test Designer-only inventory rows now have rulings; shared rules and deferred policy remain separate. R0091, the analogous Architect spec-editing boundary, is next for discussion; no change to it is approved yet.

13. R0091: Dave answered “y” to replacing only the emitted prose with: “Edit only specs. Report needed changes elsewhere as findings.” Preserve metadata, the entire YAML hook block and the Human note unchanged, including Architect/execution/software scope and the editing-specs condition. The spec-only boundary and outside-scope finding responsibility from DEC-001240 remain intact. R1618, the Architect’s native agent description, is next for discussion; no change to it is approved yet.
