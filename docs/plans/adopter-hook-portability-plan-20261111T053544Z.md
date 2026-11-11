# Plan: adopter and hook portability (#412, #415, #416)

Base: main at `7288be896b7058cbf59b8db3db757318838123ae`. Branch: `intake/adopter-hook-portability`.
Told (Dave, 2026-11-10): do this group before the live probe (#439).
Class: routine. No change to authorization, data, public interface shape or a verification class. Adopters see nothing until the next release decision; fiducial's own installed hooks change at merge through the self-adoption refresh (C5). `process/adopt.md` is process text, so its delta takes one independent read and a decision-log entry at merge.

## Unit A — #412: adopter refuses before the first write

Source: the Python fence in `process/adopt.md` (`apply`, lines 339–386 at base); `bin/tests/test_adopt.py` extracts it.

Observed at base: `apply` calls `safe()` on each planned destination, which rejects symlinks and non-directory parents but not a final path that has become a directory, and does not check writability. Writes then run in one loop, so a late failure leaves earlier files written and the ownership manifest inconsistent.

Acceptance criteria (from #412 and its 2026-11-11 comment):

- A1. An absent planned destination replaced by a directory after `prepare` is refused before any target write. Afterwards the target is unchanged: every file's bytes and mode, and the set of directories.
- A2. A planned operation the process cannot perform is refused before any target write, target unchanged as in A1: a content write to an existing file without write permission on the file (the 0400 case in #412's comment); a delete without write and search permission on the parent; a create without write and search permission on the nearest existing ancestor.
- A3. The report destination is covered by the same preflight.
- A4 (plan-derived regression guard). Existing refusals still hold: symlink, mode drift after plan, inventory change since review.
- A5 (plan-derived regression guard). A clean apply and a repeat no-op apply behave as before, including #411's mode preservation.

Not in scope: transactional apply or rollback after a mid-write I/O failure. The procedure's stated non-transactional boundary stays, narrowed by A1–A3. The preflight reads permission bits and directory types without writing; it does not see read-only filesystems, ACLs or immutable flags.

Test note: permission bits are not enforced for uid 0. The A2 tests run the adopter as an unprivileged uid in a subprocess when the suite runs as root, and directly otherwise; where neither is possible the case is skipped and reported unverified. The test makes its temporary target traversable by that uid.

## Unit B — #415: push read-back under Codex and with qualified branches

Source: `bin/hooks/push-readback` (line 103 at base strips to the last path segment); Codex adapter template in `bin/rulestore/emit/codex.py`.

Acceptance criteria (from #415):

- B1. `git push origin HEAD:refs/heads/codex/probe` reads back `codex/probe` and compares its SHA; only the literal `refs/heads/` prefix is stripped.
- B2. A Codex shell-tool payload carrying `tool_input.cmd`, as a string or a list joined the way the adapter's deny check joins it, is read back exactly as one carrying `tool_input.command`; normalisation happens before dispatch, in the adapter, for shell tools only. `apply_patch` keeps its own use of `command`.
- B3. A push the remote did not take still fails loudly in both payload forms.
- B4. Regression cases run against a local bare origin and compare actual SHAs.
- B5. No claim of arbitrary shell equivalence: the recognised command patterns are unchanged.

## Unit C — #416: cross-procedure references resolve in each emitted layout

Source: `bin/rulestore/emit/claude_code.py`, `codex.py`, `common.py`. Observed at base: emitted skills carry nine references to six source paths (`process/change-flow.md`, `review-artifact.md`, `release.md`, `gate.md`, `decision-log.md`, `verification-checklists.md`) that an adopted repository does not have.

Design: the emitters rewrite a reference to `process/<stem>.md` into the harness's name for that skill when `<stem>` is emitted as a skill in that layout, from the one list of skill documents (`common.skill_documents`). The rewritten form is fixed per harness: Claude Code, `the <stem> skill (.claude/skills/<stem>/SKILL.md)`; Codex, `$<stem> (.agents/skills/<stem>/SKILL.md)`, the form `codex.py` already uses. The replacement consumes the backticks around a quoted reference, so no stray backtick is left. Source process documents are not edited; the role bundles are unchanged. Emission fails when an emitted skill refers to a `process/` document that is not a skill in that layout.

Acceptance criteria (from #416):

- C1. No emitted Claude Code or Codex skill contains a `process/<stem>.md` reference to a document emitted as a skill; each such reference names that skill in the form the harness resolves.
- C2. A reference to a process document that is not emitted as a skill fails emission with the file and reference named.
- C3. A focused test emits from the real store into an empty target, for each harness, and asserts every cross-procedure reference resolves to a file present in that layout.
- C4 (plan-derived regression guard). The twelve role bundles are byte-identical before and after.
- C5 (plan-derived). Fiducial's own installed context is refreshed by the adopt procedure after the change, as its own commit.

## Sequence and dispatch

All subagents run at the solid general-purpose tier (sonnet), model set explicitly on every dispatch. No frontier dispatch is planned.

1. Plan review: one reviewer that did not draft this plan.
2. Test designer: writes tests for A, B and C; shows each new test failing on base for the right reason; commits tests only.
3. Coder (a different agent): implements A, B, C to green; full suite; commits.
4. Self-adoption refresh (C5) by the adopt procedure, with its independent contradiction read.
5. Review: Reviewer (quality), Skeptic/Risk (skepticism), and a Context Quality read over the `process/adopt.md` delta (governed text, intake), each by an agent that wrote none of it; one artifact per read in `process/review-artifact.md`'s form.
6. Pull request to main for Dave to merge as a merge commit; decision entry appended at merge; #412, #415, #416 closed with evidence.

## Verification boundary

Contract-verified only: local source tests, a local bare origin, emission into empty targets. Live harness loading and hook delivery stay unverified and are #439's subject.

## Plan review

Independent read of this plan at `21df755` on 2026-11-11: ready-with-findings, one blocking (A2's parent-directory clause was wrong for a content write and absent from #412) and five non-blocking. All six are applied in this revision. Re-read over the amendment at `54013b0`: all six resolved; two further non-blocking notes (traversable test target, backticks consumed) applied without another read.

## Amendments during the build

- C5 withdrawn (decision session, 2026-11-11, at `5bd4170`). DEC-001760 pins fiducial's installed context to the released commit `a8d87bc`; refreshing it from this unreleased branch would move the pin off a release. Fiducial's own installed context picks this change up when the next release is adopted, the same way any adopter does. Sequence step 4 does not run, and the class statement's clause about fiducial's own hooks changing at merge no longer applies. The suite passes without the refresh (381 tests, OK).
- Three older tests compared hook bytes emitted from the working tree against a frozen baseline and so forbade #415's change to `bin/hooks/push-readback`. The test designer pinned each comparison to its batch's landed snapshot (`5bd4170`), following the DEC-001730 precedent, after confirming baseline and landed emissions are equal for all three.
- Review runs as two reads, not three: one Reviewer session with separate quality, skepticism and continuity passes over the whole diff (routine class), and one Context Quality read over the `process/adopt.md` delta.
