You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial, doing two edit-in-place appends that discharge specs/directive-tooling.md AC-DT-16 for the cycle-mode landing (PR #244). The wording below is dictated by the decision session; carry it verbatim. You do not touch any other file.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-ac-dt-16-20260830T0400Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: AC-DT-16 gate — DEC-000270 and the OPEN-ITEMS cycle-open section", push with git push origin directive-tooling-ac-dt-16 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-ac-dt-16", created by: git worktree add --no-track "$TMPDIR/fiducial-ac-dt-16" -b directive-tooling-ac-dt-16 origin/main
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-ac-dt-16, or if "$TMPDIR/fiducial-ac-dt-16" already exists, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. origin/main must contain 395850b7d1650d4ee9b70ab6b6a042a1bccbb41c. If origin/main is beyond it, proceed only if no commit past it touches decisions/log.md or the OPEN-ITEMS.md section named below; otherwise stop and report.

READ before writing: decisions/log.md in full (confirm DEC-000260 is the last entry and no DEC-000270 exists; confirm the entry shape); OPEN-ITEMS.md section "## `bin/cycle-open` and the retirement of Track" in full, and the section headings on either side of it; DEC-000180 in full.

EDIT 1 — decisions/log.md: append the following entry after DEC-000260, separated by one blank line, verbatim, preserving the file's existing entry shape exactly (heading line, then Date, Decision, Context, Supersedes lines as below):

## DEC-000270 — bin/directive's cycle mode bears DEC-000180's tooling consequence; bin/cycle-open becomes a forwarder
Date: 2026-08-30
Decision: The tooling consequence DEC-000180 attached to `bin/cycle-open` — the cycle skeleton emits Route and Model and no Track — is borne by `bin/directive`'s cycle mode. Both of `bin/directive`'s modes emit route and model from the committed `Route and model` section of `skills/directive-invariants.md` into a committed region of the skeleton, and nothing checks either value (`specs/directive-tooling-trd.md` §3.3, Q5 ruled (c)); no region of either mode emits a `Track:` line, and the invariants document is the only place a region's text lives. `bin/cycle-open` survives as a forwarding executable, passing argv to the same entry point and emitting no skeleton of its own (TRD §3.9 step 4); its acceptance suite runs unchanged against both names, which is the migration's evidence (AC-DT-15). `OPEN-ITEMS.md`'s guard against resurrecting the field is re-anchored on the cycle mode. Everything else DEC-000180 decided is carried forward unchanged and restated here so it stays live under whole-entry supersession: `track` is removed from the methodology entirely; a dispatch states three requirements every time — route, model, and the execution block; a reviewer-gated cycle directive states them like any other dispatch, with route *fresh* and model *frontier tier* as class defaults, stated per directive and overridable (the tier wording is Core's and the Decision Layer's; DEC-000180 named the model, and the default is unchanged); an executor that cannot push stops and surfaces it, and never reports a same-machine SHA as if pushed; `LEXICON.md` carries a tombstone for track; the sync block precedes every execution block.
Context: `specs/directive-tooling.md` AC-DT-16 (agreed at `d3ab472`, cycle 23) and TRD §3.9 step 5 bind the decision session, not the implementer, to land this entry and the `OPEN-ITEMS.md` rewrite before the cycle-mode migration lands. The landing is PR #244 (`docs/cycles/directive-tooling-impl-3-20260829T2300Z.md`, commit `3d1f921`), which put cycle mode in `bin/directive` with `bin/cycle-open` untouched; the forwarder is the next package. Owner decision (Dave), 2026-08-30, in the decision session that merged the tooling.
Supersedes: DEC-000180

EDIT 2 — OPEN-ITEMS.md, section "## `bin/cycle-open` and the retirement of Track": replace the section's body — everything between that heading and the next "## " heading — with the following, verbatim:

**Track is retired — do not resurrect the field.** `DEC-000180` removed `track` from the methodology entirely; the requirements are **route, model, execution block**, three not four, and `LEXICON.md` carries a tombstone. The obligation that the cycle skeleton emit **Route and Model and nothing else** of the three is borne by **`bin/directive`'s cycle mode** (`DEC-000270`, 2026-08-30): route and model come from the committed `Route and model` section of `skills/directive-invariants.md` into a committed region of every skeleton, in both modes, and no region emits a `Track:` line. `bin/cycle-open` is a forwarder (TRD §3.9 step 4) and holds no skeleton text of its own, so there is no shelved spec left to guard; the guard is the invariants document, which is governed text and changes only through its review cycle.

**Landing precondition recorded 2026-08-24 — discharged 2026-08-30.** `specs/directive-tooling.md` AC-DT-16 made two acts preconditions on the landing that migrates the cycle mode: the entry superseding `DEC-000180` (now `DEC-000270`) and this rewrite. Both landed in the decision session that merged PR #244.

Leave the section heading itself unchanged. Nothing else in OPEN-ITEMS.md changes.

Commit both edits as one commit with message "AC-DT-16: DEC-000270 supersedes DEC-000180; OPEN-ITEMS names bin/directive's cycle mode as bearer". Push with git push origin directive-tooling-ac-dt-16.

VERIFICATION, from the worktree: bin/check-frontmatter --all (state exit code and count); git diff origin/main --stat must show exactly decisions/log.md and OPEN-ITEMS.md plus the directive file; grep -c "DEC-000270" on both edited files (expect 1 in the log, at least 1 in OPEN-ITEMS).

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-tooling-ac-dt-16 shows your edit commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-ac-dt-16" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 395850b7d1650d4ee9b70ab6b6a042a1bccbb41c: on any failed command, any precondition not met, a DEC-000270 already present, the named OPEN-ITEMS section absent or not shaped as read, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; edit commit SHA; branch name; the diff of both files in full; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
