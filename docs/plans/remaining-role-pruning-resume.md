# Remaining role-pruning checkpoint and resumption

Checkpoint baseline: `2be5327e9704b0066eed7e8ef44302aa55179b18` (merged PR #429).
Branch/worktree: `intake/remaining-role-pruning`, `/private/tmp/fiducial-remaining-role-pruning`.

The human requested this checkpoint after 44 rulings covering 45 single-role rows across Coder, Test Designer, Architect, Spec Reviewer, Context Quality Reviewer, Reviewer, Skeptic, Release Manager and Chief of Staff. The checkpoint request authorizes writing, independent review and testing; it does not authorize merge or further policy choices. Resume the one-row-at-a-time conversation when the human returns.

## Records

- Approved wording and rationale: `docs/plans/remaining-role-pruning-inventory-20261107T001928Z.md`, rulings 1–44 and checkpoint amendment.
- Fixed original inventory: companion `.json`; its coverage counts are a baseline, not current deletion counts.
- Applied and pending changes: `docs/plans/remaining-role-pruning-checkpoint.json`.
- Native and all 12 named bundle measurements: `docs/plans/remaining-role-pruning-checkpoint-measurements.json`. `checkpoint` is the actual source state; `preview` excludes all five pending retirements. Provenance is held constant for content comparison.
- Test contracts: `bin/tests/test_remaining_role_pruning.py`; rerun the complete suite with `bin/tests/run`.

## Applied versus pending

Twenty-one row bodies are revised; seventeen reviewed rows remain unchanged. R0943 is archived into R0110 and R0950 into R1621. All rule selectors, Human notes and enforcement blocks are preserved. The intake procedure cites R1621 in place of R0950.

R0940, R0499, R0284, R1091 and R1485 are approved for retirement without a successor. Their original live files remain byte-identical until the decision session allocates an actual retirement decision ID at merge, as `process/decision-log.md` requires. At that point, archive each original with only the retirement reference added; remove R0284 from the intake rubric citation. The preview exercises precisely these removals without using a fabricated decision ID. Do not merge the checkpoint before doing that finalization.

Independent review caught a shortening error in R0264: requiring each row to add an “obligation” excluded definitions. The correction, “Add something absent from its existing bundles,” preserves the approved intent to retain all twelve criteria. It is documented separately from the historical user ruling.

Installed harness files and the main checkout remain unchanged. Before any adoption, follow the adopt skill against the finalized source pin, obtain its required independent inventory review, apply only authorized changes, and read back exact results. Local generation tests do not establish live harness loading, adherence or hook execution.

## Next work

Begin with R0090, the shared spec-edit ownership rule. No disposition for it has been proposed or approved in this pass. Continue shared software/workflow rows from the inventory before the writing roles. Remaining inventory groups are 58 shared rows, 72 writing-role-only rows and 37 definitions; these counts describe coverage, not recommended deletions.

Keep risk-tier design (#430), Jev experimentation (#431), deeper review-policy redesign (#427), SLO/Top K policy (#428), and tracker portability (#425) separate. R0064 remains pending. Do not infer permission for universal CI policy, cross-repository adoption, or additional retirements. The user's preference is concise positive instructions, useful findings, and a human ruling for meaningful policy changes.

The human's R1485 ruling removes explicit whole-diff delivery: he inspects GitHub diffs and asks about tests as needed. R0481's separately approved reviewed-diff/spec-close duty remains; do not revive a separate report requirement or claim that all review obligations disappeared.

## Continuation after the checkpoint

Review resumed on 2026-11-07. Ruling 45 consolidates R0166/R1513/R0090 and shortens R0939’s description, as recorded in the inventory ruling log. The checkpoint, manifest, tests and independent artifacts remain the historical 44-ruling snapshot at 8fd292d; the new continuation requires its own validation at the next checkpoint. Ruling 46 shortens R0472 while retaining its requirements. Ruling 47 keeps R0486 unchanged. Ruling 48 revises R1473 to explicitly keep spec and tests provisional during joint development, preserving the human-reported incident rationale. Ruling 49 consolidates editing/finding prose in R1478 and makes R0091/R1156 hook-only, with their enforcement preserved. Ruling 50 shortens R1479 while retaining reciprocal checks and deviation reporting. Ruling 51 merges R1480 into R1479, retaining correction and reporting duties. Ruling 52 keeps R1489 unchanged, completing the shared change-flow group. Ruling 53 shortens R0106 while retaining computed-field checks. Ruling 54 replaces R0199’s automatic stop with preserving others’ changes and coordination before potentially destructive recovery. Ruling 55 retains shortened R0259 guidance for standalone orchestration while preserving native model configuration. Ruling 56 shortens R0583 while preserving its append-only hook and standalone policy. Ruling 57 shortens R0592 while retaining its supersession mechanism. Ruling 58 keeps R1603 unchanged. Ruling 59 shortens R1605 while preserving its citation lint hook and standalone authoring guidance. Ruling 60 shortens R0527 while retaining all eight human-code-inspection triggers. Ruling 61 keeps hook-only R0720 unchanged. Ruling 62 removes Copy Editor/Critic from all five retro instruction rows, preserving the retro skill and Chief of Staff/Writer coverage; R1237 wording stays. Ruling 63 shortens R1241’s insight selection criteria. Ruling 64 permits relevant project evidence for retros, removing the remote-input prohibition. Ruling 65 retires R1249 pending merge-time allocation and revises the retro template to recurring preferences and questions for follow-up; include R1249 among pending removals in the next preview. Ruling 66 shortens R1270’s conditional review routing. Ruling 67 shortens R1408 while preserving its immutability hook and historical-record policy. Ruling 68 shortens R1448’s class-first review disposition instruction. Ruling 69 extends shared R1478 to the four reviewer roles and makes R1622 hook-only. Ruling 70 keeps R0862b’s architecture-summary requirement unchanged. Ruling 71 keeps R1573 unchanged. Ruling 72 shortens R0070’s opening while retaining its entire relevance-based checklist. Ruling 73 keeps R0073 unchanged pending risk-tier review; carry that item into the project’s follow-up tracking at the next checkpoint. Ruling 74 keeps R0158 unchanged. Ruling 75 approves R0159 retirement pending merge-time allocation; include it in the next removal preview. Ruling 76 also approves R0800 retirement pending merge-time allocation; add it to the next removal preview. The shared software/workflow group is complete. The next content review is Writer R1162. No merge has been authorized.
