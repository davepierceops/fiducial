# Store map — topic `review-artifact-schema`

Source file: `skills/review-artifact.md` @ fd54448. Register rows R1395–R1428 (34 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R1395 | skills/review-artifact.md | split into R1395a, R1395b | R1395a, R1395b |
| R1396 | skills/review-artifact.md | written | R1396 |
| R1397 | skills/review-artifact.md | retired-ruling (4: precedence of documents — role documents govern the review, this schema the artifact) | — |
| R1398 | skills/review-artifact.md | written | R1398 |
| R1399 | skills/review-artifact.md | written | R1399 |
| R1400 | skills/review-artifact.md | written | R1400 |
| R1401 | skills/review-artifact.md | written | R1401 |
| R1402 | skills/review-artifact.md | written | R1402 |
| R1403 | skills/review-artifact.md | written | R1403 |
| R1404 | skills/review-artifact.md | written | R1404 |
| R1405 | skills/review-artifact.md | merged into R1401 | R1401 |
| R1406 | skills/review-artifact.md | merged into R1396 | R1396 |
| R1407 | skills/review-artifact.md | retired-DEC-000380 | — |
| R1408 | skills/review-artifact.md | written | R1408 |
| R1409 | skills/review-artifact.md | written | R1409 |
| R1410 | skills/review-artifact.md | retired-DEC-000380 | — |
| R1411 | skills/review-artifact.md | written | R1411 |
| R1412 | skills/review-artifact.md | written | R1412 |
| R1413 | skills/review-artifact.md | written | R1413 |
| R1414 | skills/review-artifact.md | written | R1414 |
| R1415 | skills/review-artifact.md | written | R1415 |
| R1416 | skills/review-artifact.md | written | R1416 |
| R1417 | skills/review-artifact.md | written | R1417 |
| R1418 | skills/review-artifact.md | written | R1418 |
| R1419 | skills/review-artifact.md | merged into R1417 | R1417 |
| R1420 | skills/review-artifact.md | merged into R1414 | R1414 |
| R1421 | skills/review-artifact.md | written | R1421 |
| R1422 | skills/review-artifact.md | written | R1422 |
| R1423 | skills/review-artifact.md | written | R1423 |
| R1424 | skills/review-artifact.md | written | R1424 |
| R1425 | skills/review-artifact.md | written | R1425 |
| R1426 | skills/review-artifact.md | written | R1426 |
| R1427 | skills/review-artifact.md | written | R1427 |
| R1428 | skills/review-artifact.md | written | R1428 |
| R1448 | skills/spec-review-cycle.md | written (restored by store-fix-1 item 2) | R1448 |
| R1449 | skills/spec-review-cycle.md | merged into R1448 | R1448 |
| R1450 | skills/spec-review-cycle.md | written (restored by store-fix-1 item 2) | R1450 |
| R1451 | skills/spec-review-cycle.md | merged into R1450 | R1450 |

Counts: rows consumed 38 (34 from `skills/review-artifact.md`, 4 from `skills/spec-review-cycle.md`); rows written 30; definitions 2; merged away 6; split 1 (R1395 → R1395a, R1395b); retired 3 (R1397 container rule; R1407, R1410 DEC-000380).

Amended by `docs/cycles/store-fix-1-20260906T040000Z.md` item 2: the finding-triage rows R1448-R1451, retired by the store-all directive with the spec-review cycle, are restored here as two rows — R1448 (absorbing R1449) and R1450 (absorbing R1451) — in open/closed vocabulary. Their register ids sit outside this topic's R1395-R1428 span; the header's row range names the source file's span, not the topic's.

Notes.

- The verdict row R1414 is amended per process/change-flow.md @ 81310de1: one
  overall `Verdict:` in the header, one `Verdict (<pass>):` per pass section,
  overall being the most severe of the passes. R1420's ban on the word `agreed`
  is folded in, positive.
- Retired under DEC-000380 by substance: R1407 (a per-entry agreement log is
  not an artifact in this sense — the agreement machinery it excepts is gone,
  and the residue is a scope disclaimer) and R1410 (the stem-ends-in-`-cycle`
  repetition case, which exists only because of per-document cycle numbering).
- Restated rather than retired, in change-flow's vocabulary: R1409 (the
  filename keeps its derivable stem, loses `-cycle-<n>`), R1412 (`Prior cycle`
  still names the predecessor stem; the restart-at-1 half is gone), R1418
  (`Baseline` required over a range — a read at a delta's close or a
  reconciliation, not an exit gate over a `converging` document), R1396
  (one artifact per read over one delta, not per document cycle).
- The review-artifact field placements are not collapsed (clusters artifact,
  method note 4): R1398–R1404 are seven rows.
- C115 (R1396 with sre-critic.md's R0311) is cross-file with an engagement
  file; R1396's body is written from this file's text alone (ruling 1,
  ruling 12).
