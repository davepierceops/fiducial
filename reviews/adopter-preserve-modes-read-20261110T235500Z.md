# Review: intake/adopter-preserve-modes — read-20261110T235500Z

Verdict: ready-with-findings
Reviewed: intake/adopter-preserve-modes @ b71922a
Baseline: main @ 5b2a62f
Reviewer: context-quality-reviewer (subagent; wrote none of the delta)
Date: 2026-11-10
Scope: the governed-context change in `process/adopt.md` — the added sentence in "Ownership and deterministic create/append" and the two added lines in `build_plan` in the Python fence — read against the changed fence, the rest of `process/adopt.md`, and the plan's Change section
Cross-checked: `docs/plans/adopter-preserve-modes-20261110T233500Z.md`; `process/adopt.md` whole (step 4 "replaces only owned material", the whole-file hash/mode rule, `prepare`/`apply` chmod); grep of `process/` and `rules/` for permission, mode, chmod, 0644, 0755 and executable claims about adoption (none found outside `process/adopt.md`); `.claude/skills/adopt/SKILL.md` and `.agents/skills/adopt/SKILL.md`
Not inspected: the quality or sufficiency of the tests in `bin/tests/test_adopt.py`; code risk beyond whether the prose matches the fence (Reviewer and Skeptic/Risk passes cover these); no part of the fence was run — every claim below comes from reading the code; behaviour on filesystems without POSIX modes; the installed adopt skill copies, which have not yet been regenerated (the plan schedules that for Sequence step 5, after review)
Findings: 1 non-blocking
The human should inspect: F1 — whether to say in the prose that the manifest is the exception, or leave it to the separate issue the plan names

## Verdict (quality): ready-with-findings

The sentence matches the fence for every path that goes through the `.md`/`.json` branches. That includes wholly-owned agent and skill Markdown, which is what the plan says the change covers. The sentence also holds for retired and edit-only files that survive, and for files fiducial created that the user chmodded later. It is not ambiguous, nothing else says it, and it agrees with "replaces only owned material" (step 4), which is now more accurate than before. By contrast it implies the whole-file objects (TOML, hooks) keep their hash rule and generated mode, and the fence does that. Nothing in `process/` or `rules/` has become false. The one gap is the ownership manifest.

## F1 — non-blocking
Claim: "An existing Markdown or JSON file keeps its permissions" has no exception, but the ownership manifest `.claude/fiducial-ownership.json`, which is an existing JSON file, is still rewritten at 0644 whenever its text changes.
Classification: defect
Location: process/adopt.md, "Ownership and deterministic create/append", lines 89–90; fence `build_plan`, `writes[MANIFEST] = {"text": manifest, "mode": 0o644}` (line 310), and the chmod in `apply` (line 382)
Evidence: inferred by reading. `MANIFEST` is excluded from `desired` and `edited`, so it never reaches the new `.md`/`.json` mode branch. When the ownership state changes (any upgrade that adds or retires a contribution), `writes[MANIFEST]` is planned with a fixed 0644 and `apply` chmods to it. The plan puts this out of scope on purpose ("The ownership manifest's hard-coded 0644 … to be filed as its own issue"), but the prose sentence does not mention the exception.
Consequence: an agent or human reading cold who chmods the manifest, for example to 0600 or group-writable, trusts the sentence, and after the next upgrade finds the mode reset with nothing explaining why. The sentence then contradicts the code it documents. The harm is small because the manifest holds no secrets, but this is the document the fence is published from.
Fix: limit the sentence to what is true, e.g. "An existing Markdown or JSON file, other than the ownership manifest, keeps its permissions; a new file and the manifest take the generated ones." Alternatively, fix the manifest's mode in the separate issue the plan names and leave the sentence as it is, linking the issue from the plan. Criterion failed: Stand alone within its bundle for an agent unfamiliar with the repository (an unqualified claim the code contradicts).

## O1 — observation
Claim: the existing prose calls the TOML/hook rule "exact file hashes", but the fence also records each file's mode and refuses when it changes. The new sentence brings out that contrast without stating it.
Location: process/adopt.md, lines 87–89; fence line 297
Evidence: inferred by reading. `require(... and mode == old["mode"] ...)` refuses a locally chmodded owned script with "occupied or modified structured file" (plan criterion 5). "A later local edit is refused" covers this only if a reader counts a chmod as an edit. This predates the delta.
Consequence: none is introduced by this delta. A reader can work it out from "exact file hashes" plus the new sentence, but only by inference.
Fix: optional — "use exact file hashes and modes".
