# Store map — topic `test-designer`

Source files, in order: `roles/test-designer-agent.md` @ fd54448 (register rows R1140–R1159, 20 rows);
`skills/test-plan-review.md` @ fd54448 (register rows R1495–R1510, 16 rows). 36 rows consumed.
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R1140 | roles/test-designer-agent.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R1141 | roles/test-designer-agent.md | written | R1141 |
| R1142 | roles/test-designer-agent.md | retired-ruling (ruling 4: disclaimer distinguishing this document's list from the test-plan review skill; the construction/review distinction is now the topic's `role` key) | — |
| R1143 | roles/test-designer-agent.md | written | R1143 |
| R1144 | roles/test-designer-agent.md| merged into R1143 (fix 3 item 2) | R1143 |
| R1145 | roles/test-designer-agent.md| merged into R1143 (fix 3 item 2) | R1143 |
| R1146 | roles/test-designer-agent.md| merged into R1143 (fix 3 item 2) | R1143 |
| R1147 | roles/test-designer-agent.md| merged into R1143 (fix 3 item 2) | R1143 |
| R1148 | roles/test-designer-agent.md| merged into R1143 (fix 3 item 2) | R1143 |
| R1149 | roles/test-designer-agent.md | merged into R1141 | R1141 |
| R1150 | roles/test-designer-agent.md | written | R1150 |
| R1151 | roles/test-designer-agent.md | written | R1151 |
| R1152 | roles/test-designer-agent.md | written | R1152 |
| R1153 | roles/test-designer-agent.md | written | R1153 |
| R1154 | roles/test-designer-agent.md | written | R1154 |
| R1155 | roles/test-designer-agent.md | written | R1155 |
| R1156 | roles/test-designer-agent.md | written | R1156 |
| R1157 | roles/test-designer-agent.md | written | R1157 |
| R1158 | roles/test-designer-agent.md | written | R1158 |
| R1159 | roles/test-designer-agent.md| retired-never-observed (fix 3 item 4) | — |
| R1495 | skills/test-plan-review.md | retired-ruling (ruling 9 addendum: a scope statement of which session kind the procedure is for becomes the `session` key) | — |
| R1496 | skills/test-plan-review.md | written | R1496 |
| R1497 | skills/test-plan-review.md | written | R1497 |
| R1498 | skills/test-plan-review.md | merged into R1497 | R1497 |
| R1499 | skills/test-plan-review.md | merged into R1497 | R1497 |
| R1500 | skills/test-plan-review.md | merged into R1497 | R1497 |
| R1501 | skills/test-plan-review.md | merged into R1497 | R1497 |
| R1502 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1503 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1504 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1505 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1506 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1507 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1508 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1509 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |
| R1510 | skills/test-plan-review.md| merged into R1496 (fix 3 item 2) | R1496 |

Counts: rows consumed 36; rows written 29; definitions 1 (R1140); merged away 5 (R1149 into R1141 under C178; R1498–R1501 into R1497 under C032); split 0; retired 2 (R1142 container/disclaimer; R1495 session-scope statement).

Cross-file clusters left unmerged, as ruled: C012 (R1150 run the red-gate / R1507 check the plan provides one) — different role and different obligation; C179 (R1143/R1503), C180 (R1145/R1505), C181 (R1146/R1506), C182 (R1148/R1508) — the designer builds, the reviewer checks, so the `role` key differs and ruling 1 splits them. C025 (R1151), C044 (R1157), C084 (R1154), C096 (R1158), C097 (R1156), C183 (R1155) cluster across topics and are never merged.

Store fix pass 3 item 2 merges R1144-R1148 into R1143 (trigger: designing the test plan) and R1502-R1510 into R1496 (trigger: reviewing a test plan). R1146 and R1506 stated the same obligation on the two sides; each survives inside its own checklist.

Store fix pass 3 item 4 retires R1159 under the never-observed test, disposition `never-observed`: a ban with no incident behind it; R0121 already states positively that the smallest test producing the evidence is the one to choose.

Store fix pass 4 item 8 moves the test-plan-review rows out of the topic, so `test-designer` carries only the
Test Designer's own rows. R1496 — the merged test-plan-review checklist, keyed `reviewer-agent` — moves to topic
`reviewer` at order 120. R1497, its trigger row and also keyed `reviewer-agent`, moves with it at order 130: the
item names R1496, and leaving R1497 behind would leave a reviewer-agent row in the Test Designer's topic, which
is what the item removes. Item 3 moves R0083, R0085 and R0086 into this topic in the same pass.

Store fix pass 4 item 9's cross-topic sweep retires four more of the topic's rows, each stated by a row the Test
Designer's own bundle already loads: R1150 (duplicate of `change-flow`'s R0484), R1152 and R1154 (of
`convergence`'s R1468 and R1473) and R1157 (of `convergence`'s R1479). Topic count: 13 rows before the pass,
10 after — R1496 and R1497 out under item 8, R0083, R0085 and R0086 in under item 3, four out under item 9.
