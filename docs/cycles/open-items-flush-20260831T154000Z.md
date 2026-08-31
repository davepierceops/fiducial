You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Flush the 2026-08-31 retrospective session's follow-ups into OPEN-ITEMS.md, a tracker outside the frontmatter in-scope set. You edit OPEN-ITEMS.md only. You do not edit any governed document, any file under retros/, or bin/. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/open-items-flush-20260831T154000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: OPEN-ITEMS flush 2026-08-31 (retrospective session)", push with git push origin open-items-flush-20260831 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-oi-flush-retro", created by: git worktree add --no-track "$TMPDIR/fiducial-oi-flush-retro" -b open-items-flush-20260831 298b1c72157ef3c4adea29a097583560e4ffadd1
Before creating it, run git fetch origin, then git worktree list; if any existing worktree holds branch open-items-flush-20260831, or if "$TMPDIR/fiducial-oi-flush-retro" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. Judge the fetch by the refs it reports, not by credential-helper noise on stderr. The reviewed ref 298b1c72157ef3c4adea29a097583560e4ffadd1 must be an ancestor of origin/main (git merge-base --is-ancestor 298b1c72157ef3c4adea29a097583560e4ffadd1 origin/main, exit 0); if not, stop and report. In the worktree, git rev-parse HEAD:OPEN-ITEMS.md must be ebea5f8b6c81d633d41bf4f9e2a4b6463027d383; if it differs, stop and report.

READ before writing, whole, from the worktree: OPEN-ITEMS.md; retros/retro-synthesis-20260831T163000.md (the source of every entry below; it is cited, not restated).

EDITS, in order, to OPEN-ITEMS.md. Anchors are exact strings in the file at the reviewed blob; if an anchor is not found exactly once, stop and report.

E1. Replace the line "Last updated: 2026-08-30" with "Last updated: 2026-08-31".

E2. In the section headed "## Bundle-system PRD draft is uncommitted", append after its last paragraph (the one beginning "**Recorded requirement for the PRD's cycle 1**") a new paragraph:

**Seven further requirements for cycle 1 (retrospective session, 2026-08-31):** provenance and staleness stamps on every bundle; filename and header per DEC-000210; stated regeneration triggers; per-rule selection or a stated reason for file granularity; Releases distribution as recorded above; how an adopting project reaches the corpus with a document and a chat and nothing else; a home for sandbox and connector lore with a stated audience. Each is stated in full under "Follow-ups — bundle-system PRD inputs" in retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203, with the retros that raised it.

E3. Append at the end of the file, after the last line of the "## Writing methodology landed — follow-ups" section, a separator and a new section:

---

## Retrospective session 2026-08-31 — follow-ups

**Source:** retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203, the first synthesis over this repository's `retros/` (29 files, 33 deduplicated topics, each with count, most recent session, and state against `main` at 37c6818). Topic numbers below are that document's. Each item is a candidate for a review cycle on the named document; none is decided. The prior retrospective session, 2026-08-05, ran over wne-crm's corpus; its board is `retros/retro-triage-board.md` and its action items have no recorded disposition (item 14).

1. **`skills/conversation-retro.md` — one cycle, four changes (T17, T18).** The retro reads nothing from and writes nothing to any remote — the file is handed in chat, placement is a separate command-block step from a decision session; `date:` is the session's last interaction, derived from the last dated artifact the session touched, with `generated:` added and the filename timestamp kept as the opaque handle; a synthesis lists the retro filenames it covers, so unsynthesized retros are computed; a prompt for standing preferences repeated across sessions, held separate from in-session corrections (the 08-05 board's AI-15, never landed). The document is on the expedited path's ineligible list; full gate.
2. **`roles/chief-of-staff.md` read-sequence — "what else is running" (T05).** A check for other chats holding the connector and other worktrees before any connector write; and the constraint itself — one chat holds GitHub at a time — stated where decision sessions read it.
3. **Decision Layer 13 vs the 2026-08-24 recovery retro (T08).** Rule 13 says a baton carries "pointers and state"; the retro says a baton carries never computed state, which is re-read from the repo. Two governed-adjacent sources disagree; Dave's ruling, then the losing text moves.
4. **Decision Layer 5 or the Chief of Staff role (T08).** The baton's ordered next-step list is Dave's ruling; the successor session's first response dispatches item one and does not ask whether to.
5. **Decision Layer register (T16, T17).** "Say what the item is before the choice" and "y/n where possible" — repeated across sessions, in no governed text.
6. **`skills/spec-review-cycle.md` (T09).** A re-gate disposes findings and takes no new decisions; the agreement bar and gate cadence are stated at loop start; findings below the reviewed document's stage are routed to the next stage's question list, not filed as blockers.
7. **`skills/command-blocks.md` (T19).** No ``` fence inside a paste block — inner fences are `~~~` with a fence note; an expected-output line is observed in the environment the block runs in, or is qualitative; a block never pushes the default branch.
8. **`skills/directive-authoring.md`, after the consolidation cycle (T20, T21, T22).** Reviewer Fix text carried verbatim unless the record states the departure; every fix names its seam and the sweep that checks it; position-bearing derived artifacts get a mechanical re-check; dispositions are intent — the executor verifies against the counterparty artifact and discloses deviation.
9. **Trivial-additive fast lane (T25).** An owner-approved, additive, tool-verifiable-green change that neither the doc-only nor the expedited path covers: scope it or refuse it.
10. **Session rotation and the autonomous run (T23).** A stated trigger for the Chief of Staff to propose handoff and take an ack; a named skill for the autonomous overnight run if it is to recur — two instances exist as its evidence.
11. **Files handed to Dave (T26).** `~/Downloads`, named to sort to the top; long documents presented rendered and navigable. One line in the Decision Layer; today it lives in memory only.
12. **Tooling-facts artifact (T30, T04).** A dated, falsifiable record of connector and sandbox behaviour — or the decision that the bundle-system PRD's lore-home requirement is that artifact.
13. **SLO gate hole (T29, open since 2026-08-05).** The consequential class and the change package reference Top K journeys and SLO budgets that nothing defines or maintains, so a gate criterion cannot fire: define them or remove the criterion and the field.
14. **The 2026-08-05 board pass (T33).** One disposition — landed, superseded, or still open — per action item AI-1 through AI-15 of `retros/retro-triage-board.md`, recorded so the board can be called synthesized.
15. **Test counts carry their environment (T06).** A count reported by an executor states the environment it was observed in (clone, worktree, sandbox); a count measured elsewhere is not an expectation.
16. **`bin/check-directive` M2 rejects a backticked citation (TRD rider).** Observed 2026-08-31 linting this directive: a `path @ sha` citation written with the path in backticks fails M2 as path-absent, because the citation pattern takes the backtick as part of the path. Either the pattern strips inline-code delimiters or the authoring skill states that citations are written bare. Add to the `specs/directive-tooling-trd.md` rider queue above.

Confirmed by the corpus and already tracked above, no new entry: convergence-process canonization; multi-document gates; substance-only governed documents; rubric negation, bundle invariant, agent-instruction test; landmine test; executor self-recovery; six unlogged decisions; skills conformance and name/description; Illuminait retro; `bin/land` usage document; PRD/TRD template audience; Critic vs review-artifact audience.

SCOPE, one commit after the directive-file commit: OPEN-ITEMS.md only. Commit message: "OPEN-ITEMS flush 2026-08-31: retrospective-session follow-ups (15 entries), PRD cycle-1 inputs pointer". Push with git push origin open-items-flush-20260831.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-oi-flush-retro-run.log": bin/check-frontmatter --all (state exit code and count); git diff --stat of the content commit (expected: exactly one file); grep -c "^## " OPEN-ITEMS.md before and after (expected: after = before + 1); grep -c "retro-synthesis-20260831T163000.md" OPEN-ITEMS.md (expected: 2).
Expected state, and a stop if it differs: check-frontmatter exit 0, 61 files / 14 globs — OPEN-ITEMS.md is outside the in-scope set and the count does not move.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin open-items-flush-20260831 shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-oi-flush-retro" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 298b1c72157ef3c4adea29a097583560e4ffadd1. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any anchor not found exactly once, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the content commit SHA, and the branch it is on
- the run-log path
- per edit E1–E3, done, with the resulting line range
- the diff stat
- check-frontmatter exit code and count
- the two grep counts
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
