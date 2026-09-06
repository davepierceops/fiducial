# Store map — topic `spec-and-change-discipline`

Source file: `context-sets/spec-and-change-discipline.md` @ fd54448. Register rows R0080–R0107 (28 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0080 | context-sets/spec-and-change-discipline.md | retired-DEC-000380 (C004: the file's session-kind scope becomes the `session` key) | — |
| R0081 | context-sets/spec-and-change-discipline.md | written | R0081 |
| R0082 | context-sets/spec-and-change-discipline.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0083 | context-sets/spec-and-change-discipline.md | written | R0083 |
| R0084 | context-sets/spec-and-change-discipline.md | written | R0084 |
| R0085 | context-sets/spec-and-change-discipline.md | written | R0085 |
| R0086 | context-sets/spec-and-change-discipline.md | written | R0086 |
| R0087 | context-sets/spec-and-change-discipline.md | written | R0087 |
| R0088 | context-sets/spec-and-change-discipline.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0089 | context-sets/spec-and-change-discipline.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0090 | context-sets/spec-and-change-discipline.md | written | R0090 |
| R0091 | context-sets/spec-and-change-discipline.md | written | R0091 |
| R0092 | context-sets/spec-and-change-discipline.md | written | R0092 |
| R0093 | context-sets/spec-and-change-discipline.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0094 | context-sets/spec-and-change-discipline.md | written | R0094 |
| R0095 | context-sets/spec-and-change-discipline.md| merged into R0094 (fix 3 item 2) | R0094 |
| R0096 | context-sets/spec-and-change-discipline.md | written | R0096 |
| R0097 | context-sets/spec-and-change-discipline.md | written | R0097 |
| R0098 | context-sets/spec-and-change-discipline.md | merged into R0096 | R0096 |
| R0099 | context-sets/spec-and-change-discipline.md | written | R0099 |
| R0100 | context-sets/spec-and-change-discipline.md | written | R0100 |
| R0101 | context-sets/spec-and-change-discipline.md | written | R0101 |
| R0102 | context-sets/spec-and-change-discipline.md | written | R0102 |
| R0103 | context-sets/spec-and-change-discipline.md | written | R0103 |
| R0104 | context-sets/spec-and-change-discipline.md | written | R0104 |
| R0105 | context-sets/spec-and-change-discipline.md | written | R0105 |
| R0106 | context-sets/spec-and-change-discipline.md | written | R0106 |
| R0107 | context-sets/spec-and-change-discipline.md | written | R0107 |

Counts: rows consumed 28; rows written 26; definitions 6; merged away 1 (R0098 into R0096); split 0; retired 1 (R0080, DEC-000380 / C004).

Notes on the rulings applied:

- C004 (R0080) — retired; the file's "governs both session kinds" statement
  becomes `session: [decision, execution]` on the topic's rows, narrowed per row
  where a row plainly binds one side (ruling 7).
- C097 (R0091) — written as Dave ruled: the spec-editing side of the pair,
  positive, `role: [architect-agent]`, with the body binding any session working
  under a spec-editing directive. Verb moved `forbid` → `require` because the
  ruled body is positive. The Test Designer's twin row belongs to the
  `test-designer` topic and is not written here.
- C017 (R0092) — the `converging` status and its definition retire per
  process/change-flow.md's closing section; what survives is restated in
  open/closed vocabulary as the definition of an open spec delta.
- C096 (R0087) — restated: the red-gate is run while the branch is open and its
  result is the close's evidence for the tests.
- C012 (R0084), C014 (R0082), C057 (R0102) — cross-file clusters; written from
  this file's own text only, no cluster-mate content merged in (ruling 1).
- Ruling 2/5 (R0098) — the convergent-edit refusal is the named instance of
  R0096's "never by merging" and is written into that one row.
- Rows restated in open/closed vocabulary: R0085 (`converging` → the spec branch
  is open), R0087, R0092, R0093 (reconciliation → the delta's close), R0103
  ("before a spec is agreed" → before the spec delta closes).

Store fix pass 2 item 4 replaces `role: [all]` on 19 rows of this topic with an explicit role list, decided per row: 8 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`; 6 rows to `[chief-of-staff]`; 3 rows to `[test-designer-agent]`; 1 row to `[coder-agent]`; 1 row to `[coder-agent, release-manager-agent, reviewer-agent]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 2 define rows (R0083, R0092), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms.

Store fix pass 3 item 2 merges R0095 into R0094: both fire on one trigger, issuing a directive while a spec delta is open.

Store fix pass 4 item 3 dissolves the topic; it ceases to exist. The red-gate rows: R0084 and R0087 retire,
`ruled` — the Test Designer states them (R1150; R1152 with R1158). R0083 (the `red-gate` define), R0085 and
R0086 (the interface contract's source per stage, DEC-000370) move to topic `test-designer`, orders 210–230.
The open-delta and concurrency rows: R0096, R0097 and R0099 retire, `ruled` — `process/decomposition.md` step 4
states them, amended in the same commit to carry "never two deltas over one tranche", the refusal of a merged
two-delta edit, and the no-territory-left branch. R0092 retires as a duplicate of the lexicon's R0006, whose
body takes its second sentence. R0090, R0091 and R0094 move to topic `change-flow`, orders 260–280, corpus
narrowed to `[software]`. R0100–R0105 become one checklist row, R0100, in topic `decision-layer`, keyed to the
four decision roles: the loose-end tracker's five checkpoints. R0106 and R0107 become one row, R0106, in topic
`coder-agent`, keyed `[coder-agent, test-designer-agent]`. R0081 retires, `describes`. R0082, R0088 and R0089
were already retired by earlier passes and are unchanged here. Topic count: 21 rows before, 0 after.
