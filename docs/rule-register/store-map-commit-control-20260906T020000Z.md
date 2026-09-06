# Store map — topic `commit-control`

Source files, in order: `policies/commit-and-change-control-policy.md` (commit half) @ fd54448; `policies/project-setup-requirements.md` @ fd54448.
Register rows consumed: R0532, R0533, R0564–R0571, R0574–R0578 (15 of the 47 rows of `commit-and-change-control-policy.md`; the other 32 are `change-control`'s) and R0703–R0714 (12 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0532 | policies/commit-and-change-control-policy.md | retired-DEC-000380 (C004: scope statement becomes the `session` key) | — |
| R0533 | policies/commit-and-change-control-policy.md | written | R0533 |
| R0564 | policies/commit-and-change-control-policy.md | written | R0564 |
| R0565 | policies/commit-and-change-control-policy.md | written | R0565 |
| R0566 | policies/commit-and-change-control-policy.md | written | R0566 |
| R0567 | policies/commit-and-change-control-policy.md | merged into R0566 | R0566 |
| R0568 | policies/commit-and-change-control-policy.md | written | R0568 |
| R0569 | policies/commit-and-change-control-policy.md | merged into R0568 | R0568 |
| R0570 | policies/commit-and-change-control-policy.md | written | R0570 |
| R0571 | policies/commit-and-change-control-policy.md | merged into R0570 | R0570 |
| R0574 | policies/commit-and-change-control-policy.md | written | R0574 |
| R0575 | policies/commit-and-change-control-policy.md | written | R0575 |
| R0576 | policies/commit-and-change-control-policy.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0577 | policies/commit-and-change-control-policy.md | merged into R0575 | R0575 |
| R0578 | policies/commit-and-change-control-policy.md | retired-DEC-000380 (the `agreed` status and its frontmatter-only transition commit) | — |
| R0703 | policies/project-setup-requirements.md | written | R0703 |
| R0704 | policies/project-setup-requirements.md | merged into R0703 | R0703 |
| R0705 | policies/project-setup-requirements.md | written | R0705 |
| R0706 | policies/project-setup-requirements.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0707 | policies/project-setup-requirements.md | merged into R0568 | R0568 |
| R0708 | policies/project-setup-requirements.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0709 | policies/project-setup-requirements.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0710 | policies/project-setup-requirements.md | retired-DEC-000380 (C144: the pre-commit frontmatter check, `check-frontmatter`) | — |
| R0711 | policies/project-setup-requirements.md | retired-DEC-000380 (the frontmatter in-scope set) | — |
| R0712 | policies/project-setup-requirements.md | retired-DEC-000380 (metadata-schema adoption, per-project hook install) | — |
| R0713 | policies/project-setup-requirements.md | retired-DEC-000380 (hook installation as local per-clone state) | — |
| R0714 | policies/project-setup-requirements.md | retired-DEC-000380 (`reviews/expedited-log.md` must exist) | — |

Counts: rows consumed 27; rows written 14; definitions 7; merged away 6; split 0; retired 7 (R0532 C004 scope statement; R0578; R0710–R0714 document-lifecycle machinery — all DEC-000380).

Store fix pass 2 item 4 replaces `role: [all]` on 10 rows of this topic with an explicit role list, decided per row: 5 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`; 2 rows to `[chief-of-staff]`; 2 rows to `[chief-of-staff, spec-reviewer-agent]`; 1 row to `[chief-of-staff, release-manager-agent]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 2 define rows (R0533, R0705), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms; and re-verbs 1 `define` row carrying a null term (R0564), each body restated as the instruction it carries.
