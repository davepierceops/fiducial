# Store map — topic `source-of-truth-policy`

Source file: `policies/source-of-truth-policy.md` @ fd54448. Register rows R0755–R0777 (23 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0755 | policies/source-of-truth-policy.md | retired-DEC-000380 (C004: session scope becomes the `session` key) | — |
| R0756 | policies/source-of-truth-policy.md | retired-ruling (ruling 4: purpose statement; its obligation is carried by R0757–R0762 and R0770) | — |
| R0757 | policies/source-of-truth-policy.md | written | R0757 |
| R0758 | policies/source-of-truth-policy.md | written | R0758 |
| R0759 | policies/source-of-truth-policy.md | written | R0759 |
| R0760 | policies/source-of-truth-policy.md | written | R0760 |
| R0761 | policies/source-of-truth-policy.md | written | R0761 |
| R0762 | policies/source-of-truth-policy.md | written | R0762 |
| R0763 | policies/source-of-truth-policy.md | written | R0763 |
| R0764 | policies/source-of-truth-policy.md | merged into R0763 | R0763 |
| R0765 | policies/source-of-truth-policy.md | written | R0765 |
| R0766 | policies/source-of-truth-policy.md | written | R0766 |
| R0767 | policies/source-of-truth-policy.md | merged into R0763 | R0763 |
| R0768 | policies/source-of-truth-policy.md | written | R0768 |
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
