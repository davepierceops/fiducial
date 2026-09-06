# Store map — topic `decision-log-policy`

Source file: `policies/decision-log-policy.md` @ fd54448. Register rows R0579–R0594 (16 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0579 | policies/decision-log-policy.md | retired-ruling (9: scope statement becomes the `session` key, not a row) | — |
| R0580 | policies/decision-log-policy.md | written | R0580 |
| R0581 | policies/decision-log-policy.md | written | R0581 |
| R0582 | policies/decision-log-policy.md | merged into R0581 | R0581 |
| R0583 | policies/decision-log-policy.md | written | R0583 |
| R0584 | policies/decision-log-policy.md | merged into R0583 | R0583 |
| R0585 | policies/decision-log-policy.md | written | R0585 |
| R0586 | policies/decision-log-policy.md | written | R0586 |
| R0587 | policies/decision-log-policy.md | merged into R0580 | R0580 |
| R0588 | policies/decision-log-policy.md | written | R0588 |
| R0589 | policies/decision-log-policy.md | written | R0589 |
| R0590 | policies/decision-log-policy.md | merged into R0586 | R0586 |
| R0591 | policies/decision-log-policy.md | written | R0591 |
| R0592 | policies/decision-log-policy.md | written | R0592 |
| R0593 | policies/decision-log-policy.md | merged into R0592 | R0592 |
| R0594 | policies/decision-log-policy.md | written | R0594 |

Counts: rows consumed 16; rows written 10; definitions 3 (R0580, R0589, R0594); merged away 5 (R0582, R0584, R0587, R0590, R0593); split 0; retired 1 (R0579, scope statement).

Store fix pass 2 item 4 replaces `role: [all]` on 10 rows of this topic with an explicit role list, decided per row: 6 rows to `[chief-of-staff, writer, copy-editor, critic]`; 4 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.
