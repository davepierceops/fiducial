# Store map — topic `remote-write-verification-policy`

Source file: `policies/remote-write-verification-policy.md` @ fd54448. Register rows R0719–R0754 (36 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0719 | policies/remote-write-verification-policy.md | retired-ruling (9 / C004: scope statement becomes the `session` key) | — |
| R0720 | policies/remote-write-verification-policy.md | written | R0720 |
| R0721 | policies/remote-write-verification-policy.md | merged into R0720 | R0720 |
| R0722 | policies/remote-write-verification-policy.md | written | R0722 |
| R0723 | policies/remote-write-verification-policy.md | merged into R0722 | R0722 |
| R0724 | policies/remote-write-verification-policy.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0725 | policies/remote-write-verification-policy.md | written | R0725 |
| R0726 | policies/remote-write-verification-policy.md | merged into R0725 | R0725 |
| R0727 | policies/remote-write-verification-policy.md | written | R0727 |
| R0728 | policies/remote-write-verification-policy.md | written | R0728 |
| R0729 | policies/remote-write-verification-policy.md | written | R0729 |
| R0730 | policies/remote-write-verification-policy.md | written | R0730 |
| R0731 | policies/remote-write-verification-policy.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0732 | policies/remote-write-verification-policy.md | written | R0732 |
| R0733 | policies/remote-write-verification-policy.md | written | R0733 |
| R0734 | policies/remote-write-verification-policy.md | written | R0734 |
| R0735 | policies/remote-write-verification-policy.md | written | R0735 |
| R0736 | policies/remote-write-verification-policy.md | written | R0736 |
| R0737 | policies/remote-write-verification-policy.md | written | R0737 |
| R0738 | policies/remote-write-verification-policy.md | merged into R0737 | R0737 |
| R0739 | policies/remote-write-verification-policy.md | written | R0739 |
| R0740 | policies/remote-write-verification-policy.md | retired-DEC-000380 (pre-commit hook) | — |
| R0741 | policies/remote-write-verification-policy.md | retired-DEC-000380 (frontmatter fields, in-scope set) | — |
| R0742 | policies/remote-write-verification-policy.md | retired-DEC-000380 (`bin/check-frontmatter --all`) | — |
| R0743 | policies/remote-write-verification-policy.md | written | R0743 |
| R0744 | policies/remote-write-verification-policy.md | written | R0744 |
| R0745 | policies/remote-write-verification-policy.md | written | R0745 |
| R0746 | policies/remote-write-verification-policy.md | written | R0746 |
| R0747 | policies/remote-write-verification-policy.md | written | R0747 |
| R0748 | policies/remote-write-verification-policy.md | written | R0748 |
| R0749 | policies/remote-write-verification-policy.md | merged into R0743 | R0743 |
| R0750 | policies/remote-write-verification-policy.md | written | R0750 |
| R0751 | policies/remote-write-verification-policy.md | written | R0751 |
| R0752 | policies/remote-write-verification-policy.md | written | R0752 |
| R0753 | policies/remote-write-verification-policy.md | written | R0753 |
| R0754 | policies/remote-write-verification-policy.md | written | R0754 |

Counts: rows consumed 36; rows written 27; definitions 8; merged away 5 (R0721, R0723, R0726, R0738, R0749); split 0; retired 4 (R0719 ruling 9/C004; R0740, R0741, R0742 DEC-000380).

Store fix pass 2 item 4 replaces `role: [all]` on 25 rows of this topic with an explicit role list, decided per row: 23 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`; 2 rows to `[chief-of-staff, writer, copy-editor, critic]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 2 define rows (R0727, R0736), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms; and re-verbs 4 `define` rows carrying a null term (R0728, R0729, R0753, R0754), each body restated as the instruction it carries.
