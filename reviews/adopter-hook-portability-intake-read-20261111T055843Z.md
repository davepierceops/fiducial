# Review: intake/adopter-hook-portability — intake-read-20261111T055843Z

Verdict: ready-with-findings
Reviewed: process/adopt.md @ b3be5cc
Baseline: process/adopt.md @ 7288be8
Reviewer: context-quality-reviewer (agent; wrote none of the candidate)
Date: 2026-11-11
Scope: `git diff 7288be8..b3be5cc -- process/ rules/` (one file, process/adopt.md, +11/-2, inside the Python fence only; no rules/ change); prose of steps 1-5 and "Ownership and deterministic create/append" against the new `apply` preflight; fence validity; emission to both harnesses and the chief-of-staff bundle.
Cross-checked: docs/plans/adopter-hook-portability-plan-20261111T053544Z.md (Unit A); issue #412 and its comment; README.md "Adopt into a repository"; rules/ and process/ grep for adopter-behaviour statements.
Not inspected: behaviour of the new preflight by execution (A1-A5 tests in bin/tests/test_adopt.py not run by me); the rest of the diff outside process/ and rules/; row-level intake criteria beyond the delta (no rule row changed); decision-log entry (made at merge).
Findings: 0 blocking, 2 non-blocking

Verdict (quality): ready-with-findings

Checks run
- Diff touches only process/adopt.md lines 362-377, inside the single python fence (verified by diff).
- Fence extracted to /tmp/cqr/adopt.py; `python3 -m py_compile` passes; exactly one python fence in the file; CLI dispatch for `prepare`, `apply`, `labels` unchanged (usage and `labels bad` ran as before).
- `bin/bundle --emit claude-code` and `--emit codex` into /tmp/cqr: the adopt SKILL.md fence is identical to the source fence in both. `bin/bundle --where role=chief-of-staff` output: one python fence, identical to source, and the "Ownership and deterministic" section present.
- README.md and rules/ state nothing about apply preflight or atomicity that the change contradicts.

## F1 — non-blocking
Claim: Step 4's description of what `apply` does omits the new pre-write refusal checks.
Classification: suggestion
Location: process/adopt.md:54-55 ("It rechecks the inventory, writes missing files, and replaces only owned material.")
Evidence: by reading against lines 361-377: apply now also refuses, before any write, a destination that is a directory or lacks write / write+search permission (report included).
Consequence: not false, but a reader of the procedure cannot learn that these refusals exist or that they precede the first write.
Fix: add a clause such as "and, before the first write, refuses a destination that became a directory or that the process cannot write".

## F2 — non-blocking
Claim: The non-transactional boundary sentence is still true but does not say what the preflight now covers or omits.
Classification: suggestion
Location: process/adopt.md:93-96 ("checks protect against changes since review, but installation is not a transaction against a concurrent editor or a filesystem failure; inspect and revert the adoption diff if an I/O failure interrupts it.")
Evidence: by reading; plan Unit A states the preflight reads permission bits and types only and does not see read-only filesystems, ACLs or immutable flags. The document does not say so.
Consequence: a reader may treat the preflight as covering those failures; the plan intends the boundary "narrowed by A1-A3", and the text does not record the narrowing.
Fix: one clause naming that the preflight checks destination type and permission bits only.

Observation (not a finding): at line 377, `str(anchor.relative_to(target) or ".")` — a `Path` is always truthy, so the `or "."` never applies; the message is still correct (`.` for the target root).
