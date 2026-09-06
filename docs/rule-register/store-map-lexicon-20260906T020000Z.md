# Store map — topic `lexicon`

Source file: `LEXICON.md` @ fd54448. Register rows R0001–R0064 (64 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0001 | LEXICON.md | retired-DEC-000380 | — |
| R0002 | LEXICON.md | written | R0002 |
| R0003 | LEXICON.md | written | R0003 |
| R0004 | LEXICON.md | written | R0004 |
| R0005 | LEXICON.md | merged into R0004 | R0004 |
| R0006 | LEXICON.md | written | R0006 |
| R0007 | LEXICON.md | written | R0007 |
| R0008 | LEXICON.md | written | R0008 |
| R0009 | LEXICON.md | written | R0009 |
| R0010 | LEXICON.md | written | R0010 |
| R0011 | LEXICON.md | written | R0011 |
| R0012 | LEXICON.md | written | R0012 |
| R0013 | LEXICON.md | written | R0013 |
| R0014 | LEXICON.md | retired-DEC-000380 | — |
| R0015 | LEXICON.md | written | R0015 |
| R0016 | LEXICON.md | written | R0016 |
| R0017 | LEXICON.md | written | R0017 |
| R0018 | LEXICON.md | split into R0018a, R0018b | R0018a, R0018b |
| R0019 | LEXICON.md | retired-DEC-000380 | — |
| R0020 | LEXICON.md | retired-DEC-000380 | — |
| R0021 | LEXICON.md | written | R0021 |
| R0022 | LEXICON.md | written | R0022 |
| R0023 | LEXICON.md | written | R0023 |
| R0024 | LEXICON.md | written | R0024 |
| R0025 | LEXICON.md | written | R0025 |
| R0026 | LEXICON.md | written | R0026 |
| R0027 | LEXICON.md | written | R0027 |
| R0028 | LEXICON.md | written | R0028 |
| R0029 | LEXICON.md | written | R0029 |
| R0030 | LEXICON.md | written | R0030 |
| R0031 | LEXICON.md | written | R0031 |
| R0032 | LEXICON.md | written | R0032 |
| R0033 | LEXICON.md | written | R0033 |
| R0034 | LEXICON.md | merged into R0033 | R0033 |
| R0035 | LEXICON.md | merged into R0028 | R0028 |
| R0036 | LEXICON.md | merged into R0029 | R0029 |
| R0037 | LEXICON.md | written | R0037 |
| R0038 | LEXICON.md | written | R0038 |
| R0039 | LEXICON.md | merged into R0038 | R0038 |
| R0040 | LEXICON.md | written | R0040 |
| R0041 | LEXICON.md | merged into R0038 | R0038 |
| R0042 | LEXICON.md | merged into R0043 | R0043 |
| R0043 | LEXICON.md | written | R0043 |
| R0044 | LEXICON.md | written | R0044 |
| R0045 | LEXICON.md | written | R0045 |
| R0046 | LEXICON.md | written | R0046 |
| R0047 | LEXICON.md | retired-ruling (5: negation of R0046) | — |
| R0048 | LEXICON.md | merged into R0045 | R0045 |
| R0049 | LEXICON.md | retired-ruling (1, 5: positive form is core's R0207) | — |
| R0050 | LEXICON.md | retired-ruling (1: same obligation written in core as R0212 and R0208) | — |
| R0051 | LEXICON.md | retired-ruling (1: same obligation written in core as R0220) | — |
| R0052 | LEXICON.md | retired-ruling (1: same obligation written in core as R0212) | — |
| R0053 | LEXICON.md | retired-ruling (1: same obligation written in core as R0208) | — |
| R0054 | LEXICON.md | written | R0054 |
| R0055 | LEXICON.md | written | R0055 |
| R0056 | LEXICON.md | retired-ruling (1, 2: same obligation written in core as R0207) | — |
| R0057 | LEXICON.md | written | R0057 |
| R0058 | LEXICON.md | written | R0058 |
| R0059 | LEXICON.md | merged into R0058 | R0058 |
| R0060 | LEXICON.md | written | R0060 |
| R0061 | LEXICON.md | merged into R0060 | R0060 |
| R0062 | LEXICON.md | retired-ruling (1, 5: positive form is core's R0212) | — |
| R0063 | LEXICON.md | retired-ruling (1: same obligation written in core as R0212) | — |
| R0064 | LEXICON.md | written | R0064 |

Counts: rows consumed 64; rows written 42; definitions 24; merged away 10; split 1 (R0018 → R0018a, R0018b); retired 13 (4 under DEC-000380 — R0001 the per-document review cycle, R0014 the `converging` status value, R0019 its re-entry transition, R0020 converging as an interval distinct from a delta; 9 under the general rulings — R0047 the negation of R0046, and R0049, R0050, R0051, R0052, R0053, R0056, R0062, R0063, whose obligations are written once, in topic `core`).

Store fix pass 2 item 4 replaces `role: [all]` on 42 rows of this topic with an explicit role list, decided per row: 32 rows to `[architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer]`; 4 rows to `[chief-of-staff]`; 2 rows to `[chief-of-staff, spec-reviewer-agent]`; 1 row to `[chief-of-staff, spec-reviewer-agent, test-designer-agent]`; 1 row to `[chief-of-staff, coder-agent]`; 1 row to `[architect-agent, chief-of-staff, spec-reviewer-agent]`; 1 row to `[chief-of-staff, test-designer-agent] (test-designer is not a role-document slug)`. `all` is not a value; the lists are the role documents' own basename slugs at fd54448.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 23 define rows (R0003, R0004, R0006, R0009, R0012, R0022, R0023, R0024, R0025, R0026, R0027, R0028, R0029, R0031, R0037, R0038, R0040, R0043, R0045, R0054, R0055, R0057, R0064), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms; and re-verbs 1 `define` row carrying a null term (R0011), each body restated as the instruction it carries.

Store fix pass 2 item 9 notes, without changing anything: the topic name stays lowercase `lexicon`, though its source file is `LEXICON.md`. Topic names are the source basename without extension, lowercased like every other topic; the divergence from the filename is deliberate and is recorded here rather than fixed.

Store fix pass 4 changes the topic on four counts. Item 3: R0006's body takes the second sentence of R0092,
which retires as its duplicate — a revision of an agreed spec opens a new delta on a new branch. Item 4 brings
in R0604 (`term: [version, versions]`) and R0611 (`term: [agreed]`) from the dissolved `spec-gating`, orders 430
and 440. Item 7 brings in R0757 (`PRD`), R0758 (`TRD`), R0759 (`acceptance criteria`), R0760 (`architecture
summary`) and R0761 (`tracker issue`) from the dissolved `source-of-truth-policy`, orders 450–490. Item 9's
cross-topic sweep retires five obligation rows the topic carried from LEXICON.md, each stated by a row some role
loads alongside it: R0010 (duplicate of `reconciliation`'s R1491), R0015 and R0016 (of `convergence`'s R1468,
which takes R0015's "whatever its verdict" clause), R0018a (of `convergence`'s R1481) and R0018b (of
`change-flow`'s R0481). Topic count: 42 rows before, 44 after.

Store fix pass 5 item 1 makes the Lexicon the store's one home for definitions by term. Four rows arrive and one
new row is written:

- **R1601** (new, order 500) defines `known gap` / `known gaps`. It is the first row in the store whose register
  id is not the register's: the register's highest id is R1600, and the three rows this pass writes take R1601,
  R1602 and R1603 in order of writing. Its `source` names the directive that ordered it.
- **R0083** arrives from `test-designer` (order 510), the `red-gate` define. It already carried `term` and
  nothing else — store fix pass 2 item 7 stripped `role`, `session` and `corpus` from every define — so the
  move changes only `topic` and `order`. This settles the question store fix pass 4 left open at its summary
  item 3.
- **R0580** and **R0594** arrive from `decision-log-policy` (orders 520 and 530) as defines, `term: [DEC ID,
  decision ID]` and `term: [live decision, live decisions]`, their `verb` changed from `require` to `define`
  and their `role`, `session` and `corpus` keys deleted. R0580's obligation to cite by DEC ID goes with the
  form; what stays is what the ID *is*.
- **R1512** (`prd-template`) retires into **R0757**, whose `term` list becomes the union of both —
  `[PRD, PRDs, Product Requirements Document, standing product specification]` — and whose body states the one
  PRD definition at its shortest. This settles the question store fix pass 4 left open at its summary item 4.

The topic holds 48 rows.
