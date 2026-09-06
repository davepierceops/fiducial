# Store map — topic `reconciliation`

Source file: `skills/spec-review-cycle.md` @ fd54448. Register rows R1489–R1494 (6 rows); the file's earlier rows, R1429–R1488, are consumed by topic `convergence`.
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R1489 | skills/spec-review-cycle.md | written | R1489 |
| R1490 | skills/spec-review-cycle.md | written | R1490 |
| R1491 | skills/spec-review-cycle.md | written | R1491 |
| R1492 | skills/spec-review-cycle.md | retired-DEC-000380 (runs the retired per-document cycle from its step 1) | — |
| R1493 | skills/spec-review-cycle.md | retired-DEC-000380 (C002: the agreement flip after the merge) | — |
| R1494 | skills/spec-review-cycle.md | retired-DEC-000380 (order of the retired flip against the merge) | — |

Counts: rows consumed 6; rows written 3; definitions 1; merged away 0; split 0; retired 3.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 1 define row (R1490), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms.
