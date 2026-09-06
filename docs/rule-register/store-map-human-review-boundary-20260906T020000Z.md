# Store map — topic `human-review-boundary`

Source file: `boundaries/human-review-boundary.md` @ fd54448. Register rows R0065–R0069 (5 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0065 | boundaries/human-review-boundary.md | written | R0065 |
| R0066 | boundaries/human-review-boundary.md| retired-ruling (fix 3 item 6: describes) | — |
| R0067 | boundaries/human-review-boundary.md | written | R0067 |
| R0068 | boundaries/human-review-boundary.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0069 | boundaries/human-review-boundary.md | retired-ruling (store-fix-1 item 4: describes) | — |

Counts: rows consumed 5; rows written 5; definitions 4 (R0066–R0069); merged away 0; split 0; retired 0.

Store fix pass 2 item 4 replaces `role: [all]` on 3 rows of this topic with an explicit role list, decided per row: 2 rows to `[chief-of-staff, writer, copy-editor, critic]`; 1 row to `[chief-of-staff]`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 2 define rows (R0066, R0067), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms.

Store fix pass 3 item 6 retires R0066 as `describes`, on a re-read of the source file's opening section at fd54448: the Summary section states the boundary as a thesis; R0065 carries the obligation, and no surviving row uses the term.
