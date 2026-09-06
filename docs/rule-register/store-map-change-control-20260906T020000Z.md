# Store map — topic `change-control`

Source files, in order: `policies/commit-and-change-control-policy.md` (change-control half) @ fd54448; `policies/release-readiness-policy.md` @ fd54448.
Register rows consumed: R0534–R0563, R0572, R0573 (32 of the 47 rows of `commit-and-change-control-policy.md`; the other 15 are `commit-control`'s) and R0715–R0718 (4 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0534 | policies/commit-and-change-control-policy.md | written | R0534 |
| R0535 | policies/commit-and-change-control-policy.md | written | R0535 |
| R0536 | policies/commit-and-change-control-policy.md | written | R0536 |
| R0537 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0538 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0539 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0540 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0541 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0542 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0543 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0544 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0545 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0546 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0547 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0548 | policies/commit-and-change-control-policy.md | merged into R0535 | R0535 |
| R0549 | policies/commit-and-change-control-policy.md | retired-DEC-000380 (C004: section scope statement becomes `session: [decision]`) | — |
| R0550 | policies/commit-and-change-control-policy.md | retired-ruling (ruling 5: negation of R0551 and R0553) | — |
| R0551 | policies/commit-and-change-control-policy.md | written | R0551 |
| R0552 | policies/commit-and-change-control-policy.md | written | R0552 |
| R0553 | policies/commit-and-change-control-policy.md | written | R0553 |
| R0554 | policies/commit-and-change-control-policy.md | merged into R0553 | R0553 |
| R0555 | policies/commit-and-change-control-policy.md | written | R0555 |
| R0556 | policies/commit-and-change-control-policy.md | merged into R0552 | R0552 |
| R0557 | policies/commit-and-change-control-policy.md | merged into R0553 | R0553 |
| R0558 | policies/commit-and-change-control-policy.md | written | R0558 |
| R0559 | policies/commit-and-change-control-policy.md | written | R0559 |
| R0560 | policies/commit-and-change-control-policy.md | written | R0560 |
| R0561 | policies/commit-and-change-control-policy.md | written | R0561 |
| R0562 | policies/commit-and-change-control-policy.md | written | R0562 |
| R0563 | policies/commit-and-change-control-policy.md | merged into R0562 | R0562 |
| R0572 | policies/commit-and-change-control-policy.md | written | R0572 |
| R0573 | policies/commit-and-change-control-policy.md | written | R0573 |
| R0715 | policies/release-readiness-policy.md | retired-DEC-000380 (C004: scope statement becomes the `session` key) | — |
| R0716 | policies/release-readiness-policy.md | written | R0716 |
| R0717 | policies/release-readiness-policy.md | merged into R0716 | R0716 |
| R0718 | policies/release-readiness-policy.md | merged into R0534 | R0534 |

Counts: rows consumed 36; rows written 15; definitions 6; merged away 18; split 0; retired 3 (R0549 and R0715 C004 scope statements, DEC-000380; R0550 ruling 5).

Store fix pass 2 item 4 replaces `role: [all]` on 15 rows of this topic with an explicit role list, decided per row: 9 rows to `[chief-of-staff]`; 6 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 2 define rows (R0535, R0716), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms; and re-verbs 4 `define` rows carrying a null term (R0555, R0560, R0572, R0573), each body restated as the instruction it carries.
