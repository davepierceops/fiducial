# Store map — topic `source-of-truth-policy`

Source file: `policies/source-of-truth-policy.md` @ fd54448. Register rows R0755–R0777 (23 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0755 | policies/source-of-truth-policy.md | retired-DEC-000380 (C004: session scope becomes the `session` key) | — |
| R0756 | policies/source-of-truth-policy.md | retired-ruling (ruling 4: purpose statement; its obligation is carried by R0757–R0762 and R0770) | — |
| R0757 | policies/source-of-truth-policy.md | written; `prd-template`'s R1512 merges into it (store-fix-5 item 1c) | R0757 |
| R0758 | policies/source-of-truth-policy.md | written | R0758 |
| R0759 | policies/source-of-truth-policy.md | written | R0759 |
| R0760 | policies/source-of-truth-policy.md | written | R0760 |
| R0761 | policies/source-of-truth-policy.md | written | R0761 |
| R0762 | policies/source-of-truth-policy.md | written | R0762 |
| R0763 | policies/source-of-truth-policy.md | written | R0763 |
| R0764 | policies/source-of-truth-policy.md | merged into R0763 | R0763 |
| R0765 | policies/source-of-truth-policy.md | written | R0765 |
| R0766 | policies/source-of-truth-policy.md| merged into R0765 (fix 3 item 2) | R0765 |
| R0767 | policies/source-of-truth-policy.md | merged into R0763 | R0763 |
| R0768 | policies/source-of-truth-policy.md| merged into R0765 (fix 3 item 2) | R0765 |
| R0769 | policies/source-of-truth-policy.md | written | R0769 |
| R0770 | policies/source-of-truth-policy.md | written | R0770 |
| R0771 | policies/source-of-truth-policy.md | merged into R0770 | R0770 |
| R0772 | policies/source-of-truth-policy.md | merged into R0770 | R0770 |
| R0773 | policies/source-of-truth-policy.md | merged into R0770 | R0770 |
| R0774 | policies/source-of-truth-policy.md | merged into R0770 | R0770 |
| R0775 | policies/source-of-truth-policy.md | written | R0775 |
| R0776 | policies/source-of-truth-policy.md | written | R0776 |
| R0777 | policies/source-of-truth-policy.md | merged into R0775 | R0775 |

Counts: rows consumed 23; rows written 14; definitions 6; merged away 7; split 0; retired 2 (R0755 session scope, DEC-000380 per C004; R0756 purpose statement, ruling 4).

Notes.

- C072 (R0763, R0764, R0767) merged to R0763, as ruled.
- C018 (R0756, R0772, R0773), C060 (R0770, R0774) and C104 (R0771) are the
  conflict rows. `core` owns the general disagreement rule as R0183 and it is
  not restated here (ruling 1: no merging across topics). R0770 carries only
  what R0183 does not: this policy's named canonical/derived pairs, the
  same-response surfacing, and the explicit hard-stop declaration.
- C073 (R0775, R0777) merged to R0775: one obligation, on everyone, to surface
  suspected drift on meeting it. R0775's designation of the Spec Reviewer as
  the proactive mechanism is that role's own topic to state; the scan itself is
  R0776.
- C020 (R0776) restated per process/change-flow.md @ 81310de1: the continuity
  scan's trigger is a spec delta's close, not every spec revision, and the
  wider scan follows the delta's reach rather than an on-demand request. The
  two canonical C020 rows belong to the `spec-reviewer-agent` topic; this row
  is written from this file's own text, re-triggered. Re-keyed
  `role: [spec-reviewer-agent]`, `session: [execution]` (ruling 7) — the Spec
  Reviewer runs as an execution session (roles/spec-reviewer-agent.md:5,10
  @ fd54448).
- C014 and C071 are cross-file clusters with operating-model.md,
  prd-template.md and trd-template.md; R0757, R0758, R0759 and R0762 are
  written from this file's own text (ruling 1).

Store fix pass 2 item 4 replaces `role: [all]` on 13 rows of this topic with an explicit role list, decided per row: 13 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 6 define rows (R0757, R0758, R0759, R0760, R0761, R0762), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms.

Store fix pass 3 item 2 merges R0766 and R0768 into R0765: all three fire on one trigger, creating a vendor-specific artifact.

Store fix pass 4 item 7 dissolves the topic; it ceases to exist. R0757 (`PRD`), R0758 (`TRD`), R0759
(`acceptance criteria`), R0760 (`architecture summary`) and R0761 (`tracker issue`) move to topic `lexicon`,
orders 450–490. R0763, R0765 and R0769 become one row, R0763, in topic `core` at order 420, keyed
`[chief-of-staff, coder-agent]`: a durable rule lives in the store, never only in vendor tooling; the adapter
is derived from it. R0770 and R0775 retire, `duplicate` — core's R0183 states the obligation to surface a
disagreement between sources and leave the resolution to Dave. R0776 retires, `duplicate` — the Spec Reviewer's
R1104 and R1105 state the continuity scan at the close and its widening by the delta's reach. R0762 retires,
`describes`; no surviving row uses the term `portable operating-model document`. R0757 and `prd-template`'s
R1512 both define `PRD` across two topics; item 9's sweep disposes of the pair. Topic count: 12 rows before,
0 after.
