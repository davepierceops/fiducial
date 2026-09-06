# Store map — topic `decision-log-policy`

Source file: `policies/decision-log-policy.md` @ fd54448. Register rows R0579–R0594 (16 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0579 | policies/decision-log-policy.md | retired-ruling (9: scope statement becomes the `session` key, not a row) | — |
| R0580 | policies/decision-log-policy.md | moved to topic `lexicon` (store-fix-5 item 1e) | R0580 |
| R0581 | policies/decision-log-policy.md | retired (store-fix-5 item 8: process — process/decision-log.md states the one-log rule) | — |
| R0582 | policies/decision-log-policy.md | merged into R0581 | R0581 |
| R0583 | policies/decision-log-policy.md | written | R0583 |
| R0584 | policies/decision-log-policy.md | merged into R0583 | R0583 |
| R0585 | policies/decision-log-policy.md | retired into process/decision-log.md (store-fix-5 item 8); its statement of form yields the new row R1603 | — |
| R0586 | policies/decision-log-policy.md | retired into process/decision-log.md (store-fix-5 item 8: the id arithmetic) | — |
| R0587 | policies/decision-log-policy.md | merged into R0580 | R0580 |
| R0588 | policies/decision-log-policy.md | retired into process/decision-log.md (store-fix-5 item 8); its statement of form yields the new row R1603 | — |
| R0589 | policies/decision-log-policy.md | retired into process/decision-log.md (store-fix-5 item 8: the no-author rule) | — |
| R0590 | policies/decision-log-policy.md | merged into R0586 | R0586 |
| R0591 | policies/decision-log-policy.md | retired into process/decision-log.md (store-fix-5 item 8: the collision rule) | — |
| R0592 | policies/decision-log-policy.md | written | R0592 |
| R0593 | policies/decision-log-policy.md | merged into R0592 | R0592 |
| R0594 | policies/decision-log-policy.md | moved to topic `lexicon` (store-fix-5 item 1e) | R0594 |

Counts: rows consumed 16; rows written 10; definitions 3 (R0580, R0589, R0594); merged away 5 (R0582, R0584, R0587, R0590, R0593); split 0; retired 1 (R0579, scope statement).

Store fix pass 2 item 4 replaces `role: [all]` on 10 rows of this topic with an explicit role list, decided per row: 6 rows to `[chief-of-staff, writer, copy-editor, critic]`; 4 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 re-verbs 3 `define` rows carrying a null term (R0580, R0589, R0594), each body restated as the instruction it carries.

Store fix pass 5 item 8 rules the topic to three rows plus a process document. The rows that stay are the ones
with teeth: **R0583**, its body cut to "Append to `decisions/log.md`; never edit or delete an entry already
there"; **R1603**, new at order 40 — "One decision per entry." — the substance R0585 and R0588 stated as form;
and **R0592**, unchanged. R0580 and R0594 went to `lexicon` in item 1 as the `DEC ID` and `live decision`
defines.

`process/decision-log.md` takes the rest: the entry form and its fields, the id arithmetic (last plus ten), the
collision rule (plus one within the gap), and the no-author rule. R0585, R0586, R0589 and R0591 retire into it;
R0581 and R0588 retire because the document states them. R0582, R0584, R0587, R0590 and R0593, which merged
into these rows in the store-all pass, retire with their survivors. The document is keyed `role:
[chief-of-staff]`, `session: [decision]`, `corpus: [software]`, order 110, and opens with the draft line and a
citation of the three rows by id. Topic count: 10 rows before, 3 after.
