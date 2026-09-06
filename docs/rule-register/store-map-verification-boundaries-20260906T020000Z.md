# Store map — topic `verification-boundaries`

Source files, in order: `policies/verification-boundary-policy.md` @ fd54448 (register rows R0778–R0811, 34 rows); `skills/boundary-audit.md` @ fd54448 (register rows R1177–R1192, 16 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0778 | policies/verification-boundary-policy.md | retired-DEC-000380 (ruling 9, cluster C004: session-kind scope statement becomes the `session` key) | — |
| R0779 | policies/verification-boundary-policy.md| retired-ruling (fix 3 item 6: describes) | — |
| R0780 | policies/verification-boundary-policy.md | written | R0780 |
| R0781 | policies/verification-boundary-policy.md | written | R0781 |
| R0782 | policies/verification-boundary-policy.md | written | R0782 |
| R0783 | policies/verification-boundary-policy.md | written | R0783 |
| R0784 | policies/verification-boundary-policy.md | written | R0784 |
| R0785 | policies/verification-boundary-policy.md | written | R0785 |
| R0786 | policies/verification-boundary-policy.md | merged into R0785 | R0785 |
| R0787 | policies/verification-boundary-policy.md | retired (store-fix-4 item 9: duplicate — core's R0456) | — |
| R0788 | policies/verification-boundary-policy.md | retired (store-fix-4 item 9: duplicate — the Lexicon's R0030) | — |
| R0789 | policies/verification-boundary-policy.md | written | R0789 |
| R0790 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0791 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0792 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0793 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0794 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0795 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0796 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0797 | policies/verification-boundary-policy.md | merged into R0789 | R0789 |
| R0798 | policies/verification-boundary-policy.md | written | R0798 |
| R0799 | policies/verification-boundary-policy.md | written | R0799 |
| R0800 | policies/verification-boundary-policy.md | written | R0800 |
| R0801 | policies/verification-boundary-policy.md | merged into R0800 | R0800 |
| R0802 | policies/verification-boundary-policy.md | written | R0802 |
| R0803 | policies/verification-boundary-policy.md | written | R0803 |
| R0804 | policies/verification-boundary-policy.md | written | R0804 |
| R0805 | policies/verification-boundary-policy.md | retired-ruling (container rule 4: "apply the obligation for the role you are filling" is the `role` key) | — |
| R0806 | policies/verification-boundary-policy.md | merged into R0799 | R0799 |
| R0807 | policies/verification-boundary-policy.md | written | R0807 |
| R0808 | policies/verification-boundary-policy.md | retired (store-fix-4 item 9: duplicate — the Skeptic's R1058) | — |
| R0809 | policies/verification-boundary-policy.md | written | R0809 |
| R0810 | policies/verification-boundary-policy.md| merged into R0809 (fix 3 item 2) | R0809 |
| R0811 | policies/verification-boundary-policy.md | retired-ruling (ruling 5: negation of R0810) | — |
| R1177 | skills/boundary-audit.md | retired-DEC-000380 (ruling 9, C004 by substance: session-kind scope statement becomes the `session` key) | — |
| R1178 | skills/boundary-audit.md | written | R1178 |
| R1179 | skills/boundary-audit.md | written | R1179 |
| R1180 | skills/boundary-audit.md | merged into R1179 | R1179 |
| R1181 | skills/boundary-audit.md | merged into R1179 | R1179 |
| R1182 | skills/boundary-audit.md | merged into R1179 | R1179 |
| R1183 | skills/boundary-audit.md | written | R1183 |
| R1184 | skills/boundary-audit.md | merged into R1183 | R1183 |
| R1185 | skills/boundary-audit.md| merged into R1178 (fix 3 item 2) | R1178 |
| R1186 | skills/boundary-audit.md| merged into R1178 (fix 3 item 2) | R1178 |
| R1187 | skills/boundary-audit.md| merged into R1178 (fix 3 item 2) | R1178 |
| R1188 | skills/boundary-audit.md| merged into R1178 (fix 3 item 2) | R1178 |
| R1189 | skills/boundary-audit.md| merged into R1178 (fix 3 item 2) | R1178 |
| R1190 | skills/boundary-audit.md | merged into R1189 | R1189 |
| R1191 | skills/boundary-audit.md| merged into R1178 (fix 3 item 2) | R1178 |
| R1192 | skills/boundary-audit.md | merged into R0788 | R0788 |

Counts: rows consumed 50; rows written 29; definitions 4; merged away 17; split 0; retired 4 (R0778, R1177 session-kind scope statements; R0805 container rule; R0811 negation).

Store fix pass 2 item 4 replaces `role: [all]` on 17 rows of this topic with an explicit role list, decided per row: 16 rows to `[architect-agent, chief-of-staff, coder-agent, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent]`; 1 row to `[coder-agent, test-designer-agent]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 3 define rows (R0780, R0782, R0785), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms; and re-verbs 1 `define` row carrying a null term (R0798), each body restated as the instruction it carries.

Store fix pass 3 item 2 merges R0810 into R0809 (trigger: before release) and R1185-R1189, R1191 into R1178 (trigger: running a boundary audit).

Store fix pass 3 item 6 retires R0779 as `describes`, on a re-read of the source file's opening section at fd54448: the Purpose section states what the policy does; R0781 is the obligation underneath it.

Store fix pass 4 item 9's cross-topic sweep retires three rows. R0787 is a duplicate of core's R0456 (core is
loaded by every role, this topic by eight); R0788 of the lexicon's R0030, which names the four release-impact
labels and is loaded by every role; R0808 of the Skeptic's stance row R1058, the pair the directive names. R0799
survives its pair with `trd`'s R1556, which retires into it. R0110/R0787 is moot with R0787 gone. Topic count:
21 rows before, 18 after.

Store fix pass 5 item 10 confirms both retirements landed: neither `rules/R0787.md` nor `rules/R0808.md` exists
on this branch, and `docs/rule-register/store-fix-4-20260906T070000Z.md` carries a line for each — R0787 as a
duplicate of core's R0456, R0808 as a duplicate of the Skeptic's R1058. Neither survives, so nothing is retired
now. What this item did find is that store fix pass 4 recorded the three sweep retirements in the prose note
above but left their per-id disposition cells reading `written`; the cells for R0787, R0788 and R0808 are
corrected here. No row changes.
