# Review: intake/generator-hook-defects — read-20261111T165900Z

Verdict: changes-required
Reviewed: process/adopt.md @ b11df95
Baseline: process/adopt.md @ 76a6c14
Reviewer: context-quality-reviewer (subagent; wrote none of the candidate)
Date: 2026-11-11
Scope: `git diff 76a6c14..b11df95 -- process/ rules/` (only process/adopt.md changed: step 4, boundary sentence, ownership preflight at line 375); fence extraction and py_compile; emission for claude-code, codex and the chief-of-staff bundle into /tmp/rv.
Cross-checked: docs/plans/generator-hook-defects-plan-20261111T161818Z.md E1/E2; rules/ and process/ grep for adopter-behaviour statements (none found about apply permissions or ownership).
Not inspected: running the preflight as uid 65534; ACL and immutable-flag behaviour (inferred from access(2), not run); issue #440 text; tests/; other harness emissions; the fence's non-preflight logic.
Findings: 1 blocking, 2 non-blocking

## F1 — blocking
Claim: The boundary sentence says apply "does not see read-only filesystems, ACLs or immutable flags", but the preflight does see read-only filesystems.
Classification: defect
Location: process/adopt.md:96-98 (claim); fence lines 374 and 380-381 (`os.access(..., os.W_OK)` and `os.W_OK | os.X_OK`)
Evidence: Ran as uid 0: `os.access` returns False for a file on a read-only squashfs (/mnt/skills/public/docx/SKILL.md) and for a directory on a `tmpfs -o ro` mount. Both are the calls the preflight makes, so apply refuses with "no write permission". Read-only is therefore seen, for existing files and for new-file anchors. ACLs and immutable flags: inferred from access(2), which honours both; not run.
Consequence: An adopter is told a check does not exist when it does, and plans around a false gap. The sentence says more than the code does.
Fix: State only the gaps shown: for example "does not see failures that only occur at write time" (disk full, I/O error). Drop or verify each of read-only, ACLs and immutable before listing it. The plan's E2 wording needs the same correction.

## F2 — non-blocking
Claim: The ownership check applies only to existing files being written, not to every destination, and also refuses when no mode change is needed.
Classification: suggestion
Location: process/adopt.md:54-55; fence line 375
Evidence: By reading: the check sits inside `if path.exists() and item["text"] is not None`. New files and deletions are checked on the parent directory only. A non-owner who can write a file whose mode is unchanged is still refused.
Consequence: Step 4's "ownership" is slightly broad; the over-refusal is unstated.
Fix: "on destination type, write permission and, for existing files, ownership".

## F3 — non-blocking
Claim: The same fact is stated twice in one document.
Classification: suggestion
Location: process/adopt.md:53-56 and 94-99
Evidence: Both give the refuse-before-writing list (type, permission bits, ownership).
Consequence: The two copies drift, as F1 shows for the second.
Fix: Keep it in step 4 and have the boundary sentence state only what is not seen.

## Checks that passed
- Fence is one valid Python block: extracted to /tmp/rv/adopt.py, `py_compile` OK.
- Emitted claude-code and codex adopt skills and the chief-of-staff bundle: each carries one python fence byte-identical to the source, and both changed sentences.
- No rule row or other process document states adopter permission or ownership behaviour the change contradicts.
- No repository changes other than this file.
