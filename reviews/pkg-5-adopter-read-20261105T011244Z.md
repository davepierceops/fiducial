# Review: codex/pkg-5-adopter — read-20261105T011244Z

Verdict: ready-with-findings
Reviewed: process/adopt.md and bin/tests/test_adopt.py @ bb2ebcb4ea140deb40d7148d7dbffcae56806fe2
Baseline: package 5 delta @ 95e77f71c771de5a216a2c3f4900c0ff21435eed
Reviewer: independent package 5 reviewer; authored neither procedure nor tests
Date: 2026-11-04
Scope: complete two-file delta; published executable Python; deterministic creation and upgrade ownership; independent contradiction/human-ruling boundary; report and label behavior; focused runtime probes
Cross-checked: SPEC.md §§3, 4, 6, 7, 8, 9; approved docs/plans/subtraction-plan-20261104.md §5; DEC-001100, DEC-001280, DEC-001530, DEC-001540; process/review-artifact.md, gate.md, project-setup.md; initial independent Illuminait contradiction report at /private/tmp/fiducial-adoption-contradiction-read/reviews/adoption-contradiction-read-read-20261105T011008Z.md
Not inspected: live forge labels/protection, fresh Claude Code /context, Codex trust/enforcement, the entire repository test suite, or final real adoption/PR; the real candidate's semantic review is a separate reader's work
Findings: 2 non-blocking
The human should inspect: real adoption's independent contradiction dispositions and gate package before append; this review does not supply that ruling

## Quality

Verdict (quality): ready-with-findings

### P5-1 — non-blocking
Claim: Appending to an existing shared Markdown or JSON file replaces its project-owned permission mode with the emitted file's mode.
Location: process/adopt.md:282, process/adopt.md:299, process/adopt.md:377
Evidence: Verified by executing the published fence through its test module in an isolated stand-in. Created target .claude/settings.json containing an unrelated env object with mode 0600; staged settings.json contained a permissions.deny contribution with mode 0644. After a valid stand-in read/approval and apply, unrelated JSON values remained but the target mode was 0644. The shared-file branches select new_mode from the emitter and apply unconditionally chmods to it. The same path is used for shared Markdown.
Consequence: Adoption broadens local read access to a project configuration that deliberately had restrictive permissions, despite requiring only an append. It can also discard a project-owned executable bit on shared Markdown. The first Illuminait target has no existing shared settings file, so this does not block that prepared run.
Fix: Preserve the existing mode for shared Markdown/JSON unless an explicit mode change is part of the approved candidate; use emitted modes for missing files and whole-file-owned hooks/agents. Add one focused 0600 settings preservation check.

## Skepticism

Verdict (skepticism): ready-with-findings

### P5-2 — non-blocking
Claim: A destination that becomes an empty directory after preparation passes apply's inventory and destination checks and can interrupt installation after earlier writes.
Location: process/adopt.md:354, process/adopt.md:359
Evidence: Verified by executing the published fence in an isolated stand-in. Prepared an empty target from staged CLAUDE.md and AGENTS.md and recorded valid stand-in review/approval. Created target/CLAUDE.md as an empty directory before invoking apply. The inventory was still equal to the recorded snapshot, safe() accepted the final directory, AGENTS.md was written, and CLAUDE.md raised IsADirectoryError; no adoption report was written. A companion probe adding a CLAUDE.md symlink instead correctly refused before any target write.
Consequence: Pre-existing structural drift at apply time can leave an incomplete adoption and no report even though all destinations are described as validated before the first write. This is reversible and is narrower than a transactional installer requirement; the procedure already discloses partial-install recovery and requires an idle branch, so the finding is non-blocking.
Fix: During apply's existing preflight, require every occupied write destination to be a regular file (and check expected absence/existence as needed), before any mutation; add the empty-directory drift case to the focused refusal tests.

## Continuity

Verdict (continuity): ready

The delta stays within package 5's two implementation paths. The procedure retains the store as source, stages both harness layouts, inventories nested instructions/overrides, separates mechanical conflicts from semantic contradictions, binds the read and human ruling to exact plan bytes, and describes actual human approval as authority. The labels command is scoped to installation authorization; the helper itself neither commits nor merges. Structured files retain valid formats: JSON is merged structurally, Markdown frontmatter stays first, and TOML/hooks are whole-file owned rather than concatenated. Existing project paragraphs, unrelated JSON entries, nested overrides and config survive the tested create/upgrade paths. Idempotency includes preserving the prior report when no writes remain.

The real adoption remains pending its own human ruling and append; that pending orchestration work is not a defect in this procedure. Likewise, emitted files establish contract verification only, and the document preserves the fresh-session /context and Codex trust boundaries. The observed emitter warning that CLAUDE.md has 287 lines concerns unchanged generator/store output, outside this package's two-file delta.

## Verification record

- Ran `PYTHONPATH=bin python3 -m unittest tests.test_adopt -v` in the review worktree: all 13 tests passed in 9.254 seconds. These extract the actual published Python fence; the real-emission test stages both emitters and proves a second prepare/apply makes no content or mode diff. Focused cases cover ownership changes, preserved borrowed JSON entries, obsolete contributions, structural refusal, managed-content edits, exact legacy replacements, stale approval/inventory, frontmatter, CRLF, non-directory parents, and mocked label create/read-back.
- Ran independent local probes using that same extracted module: reproduced P5-1 and P5-2 and confirmed symlink drift refusal before writes. Reproduction script: /private/tmp/pkg5-review-probes.py; fixtures use stand-in approval records, not a human ruling for a real repository.
- Read the complete added procedure and tests, and compared the whole range's file list: process/adopt.md and bin/tests/test_adopt.py only. No production code, decision log, real adoption target, label, or remote was changed by this review.

Both findings are file-and-land under the approved review policy; neither calls for reopening this package or a reread absent a human escalation.
