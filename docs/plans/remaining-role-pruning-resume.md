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

Review resumed on 2026-11-07. Ruling 45 consolidates R0166/R1513/R0090 and shortens R0939’s description, as recorded in the inventory ruling log. The checkpoint, manifest, tests and independent artifacts remain the historical 44-ruling snapshot at 8fd292d; the new continuation requires its own validation at the next checkpoint. Ruling 46 shortens R0472 while retaining its requirements. Ruling 47 keeps R0486 unchanged. Ruling 48 revises R1473 to explicitly keep spec and tests provisional during joint development, preserving the human-reported incident rationale. Ruling 49 consolidates editing/finding prose in R1478 and makes R0091/R1156 hook-only, with their enforcement preserved. The next undecided row is R1479. No merge has been authorized.
