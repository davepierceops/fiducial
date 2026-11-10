# Review: intake/adopter-preserve-modes — read-20261110T235700Z

Verdict: ready-with-findings
Reviewed: intake/adopter-preserve-modes @ b71922a
Baseline: main @ 5b2a62f
Reviewer: Skeptic/Risk agent (skepticism pass; wrote none of the delta)
Date: 2026-11-10
Scope: `git diff 5b2a62f..b71922a` (process/adopt.md fence and prose, bin/tests/test_adopt.py, the plan). Experiments ran the fence from 5b2a62f and from b71922a side by side under `python3 -I` in /tmp, as uid 65534 via setpriv, because root ignores file modes. The fence was loaded the way bin/tests/test_adopt.py loads it. Also ran `python3 -m unittest tests.test_adopt` (22 tests OK, as root) and listed the modes the real store emits.
Cross-checked: docs/plans/adopter-preserve-modes-20261110T233500Z.md; .claude/agents/skeptic-risk-agent.md; .claude/skills/verification-checklists/SKILL.md; process/review-artifact.md.
Not inspected: the other review passes; the self-adoption refresh (.claude/ and .agents/ copies; the installed adopt skill's fence differs from process/adopt.md at b71922a, which is plan step 5, not in this delta); any real target repository; non-POSIX filesystems; ACLs, umask and setuid effects; Claude Code and Codex loading behaviour; whether the manifest-mode issue named in the plan has been filed.
Findings: 1 — 0 blocking, 1 non-blocking; plus 4 observations
The human should inspect: Finding F1, whether a store-driven change of mode on a Markdown or JSON file should ever reach an existing file.

## Skepticism pass

Verdict (skepticism): ready-with-findings

Every claim below is tagged observed (a run) or inferred (reading). "Base" is 5b2a62f, "head" is b71922a.

### Experiments

| # | Setup | Base | Head | Tag |
|---|---|---|---|---|
| E1 | Existing 0400 `CLAUDE.md` needing a content write, plus other writes | `apply` raises PermissionError at CLAUDE.md. The manifest, `.claude/settings.json` and `AGENTS.md` were already written; `src/AGENTS.md` was not. | Identical | observed |
| E11 | Rerun `build_plan` after the E1-style failure | Conflict "managed prose edited or missing" on CLAUDE.md; the manifest claims ownership of text that was never written | Identical | observed |
| E1c | Existing 0400 `settings.json`, content already current, only the mode differs | Plans a write; `apply` raises PermissionError | Plans no write; applies cleanly; stays 0400 | observed |
| E2 | Existing 0000 `settings.json` | `build_plan` raises PermissionError (uncaught, from `inventory`) | Identical | observed |
| E3 | Existing 0755 `CLAUDE.md` and 0666 `settings.json`; staged 0600 | Normalised to 0644 and 0600 | Stay 0755 and 0666; repeat plan has no writes | observed |
| E4 | Wholly-owned skill `SKILL.md` installed at staged 0755, locally chmodded to 0600, then upgraded | Reset to 0755 | Stays 0600; no conflict | observed |
| E5 | `settings.json` deleted between plan and apply | Refused ("target changed since review"); nothing written | Identical | observed |
| E6 | Mode-only change between plan and apply | Refused before any write | Identical | observed |
| E7 | Existing `.JSON` (0600), `.sh` (0600), new hook (0755), new `.toml` | Hook lands 0755, `.toml` 0644, others untouched | Identical | observed |
| E8 | Store tightens an owned agent `.md` from 0644 to 0600 on upgrade | Existing file becomes 0600 | Existing file stays 0644 | observed |
| E10 | Manifest at 0600, upgrade | Written back as 0644 | Written back as 0644 | observed |
| Modes | Real store emission, both harnesses | n/a | 50 files at 0644 and 15 at 0755; every `.md` and `.json` is 0644; the 0755 files are hooks with no `.md` or `.json` suffix | observed |

Answers to the questions asked:

- **0400 shared file needing a write.** Apply fails part-way after other files were written. This is not new: base and head fail identically (E1, E11), and the prose already says installation "is not a transaction against ... a filesystem failure". The change narrows the trigger. A mode-only difference on a 0400 file used to plan a write and now does not (E1c). It does not remove the content-write case.
- **0000 file.** It fails in `inventory` before any write, the same as at base (E2). The change is irrelevant here.
- **Odd modes (0755 `.md`, 0666 `.json`).** They are now preserved, including world-writable (E3). Not widened, not tightened.
- **Wholly-owned `.md` whose staged mode differs.** The local mode wins and the staged mode is no longer re-asserted (E4, E8). The plan states the scope ("covers fiducial-wholly-owned Markdown"), so this is intended; the consequence is F1.
- **Deleted between plan and apply.** The inventory check refuses it before any write (E5). The new `path.exists()` branch is plan-time only, so there is no plan-to-apply window of its own. Inferred from reading, with E5 and E6 as support.
- **`prepare()` candidate tree.** `prepare` chmods candidates to the planned mode, so for existing `.md` and `.json` it now mirrors the existing mode. It does not apply at install time, so it is a preview only. Inferred from reading; no experiment ran `prepare` itself, because it needs `bin/bundle` and a store checkout. The `build_plan` output it consumes was exercised.
- **Any path that still widens?** Yes, one: the ownership manifest, hard-coded 0644 (E10, observed). Out of scope per the plan. Whole-file objects (scripts, TOML) still take the staged mode on first install, by design (criterion 5, E7). Case-variant suffixes such as `.JSON` fall to the whole-file branch only if they are staged. An existing one with no staged counterpart is untouched (E7).
- **Security direction.** It can reverse: an existing permissive file stays permissive (E3, E8). Nothing in today's store depends on tightening, because every emitted `.md` and `.json` is 0644 (observed). Nobody relies on the old behaviour for tightening that this delta can be shown to break. The risk is latent: a future staged restrictive `.md` or `.json` would not reach an existing file.

## F1 — non-blocking
Claim: An existing Markdown or JSON file now ignores every staged mode, so the adopter can no longer tighten (or loosen) a file's permissions through a store change.
Classification: suggestion
Location: process/adopt.md:286-287 (`if path.exists() and name.endswith((".md", ".json")): new_mode = mode`)
Evidence: Observed in E3 (0666 `settings.json` stays 0666 against staged 0600) and E8 (owned agent `.md` stays 0644 when the store moves to 0600). Observed that the real store emits only 0644 for these suffixes, so no current behaviour regresses. The security-direction reading is inferred.
Consequence: If the store ever stages a restrictive `.md` or `.json`, adopters with an existing permissive copy keep it, with no plan write and no diff to show it. This is the same silent-persistence property that fixes #411, applied in the other direction.
Fix: Accept and record the one-way rule (the human's call; no authorization is recorded yet, so this is not an accepted risk). Or limit preservation to shared files and let wholly-owned `.md` follow the staged mode. If it stays, add a line in the process prose that store modes on existing `.md` and `.json` are advisory.
Related: O1

## O1 — observation
Claim: Partial apply after a mid-run PermissionError leaves the target wedged, and the change does not alter that.
Location: process/adopt.md apply loop, lines 375-382
Evidence: E1 and E11 on base and head, identical. After the failure the manifest records ownership of content that was never written, and the next plan reports "managed prose edited or missing".
Consequence: The human repairs by hand (the prose says to revert the adoption diff). Release impact: `not-material` for this delta, because it is pre-existing and documented. Any later hardening, such as a writability check before the first write, is `deferred`.

## O2 — observation
Claim: The 0000 and unreadable-file case aborts `build_plan` rather than reporting a conflict.
Location: `inventory`, process/adopt.md:143-155
Evidence: E2, identical at base and head.
Consequence: A clear failure before any write; no damage. `not-material`.

## O3 — observation
Claim: The ownership manifest is still rewritten at 0644, so a user's 0600 manifest is widened on upgrade.
Location: process/adopt.md:310
Evidence: E10 on both revisions. The plan lists this as out of scope, "to be filed as its own issue". I did not verify the issue exists.
Consequence: Small. The manifest is a hash and mode ledger, not a secret. Release impact: `deferred`, owned by the plan's follow-up issue.

## O4 — observation
Claim: The tests cannot detect behaviour that depends on file permissions being enforced, and they omit the read-only and restrictive-direction cases.
Location: bin/tests/test_adopt.py (new tests)
Evidence: `unittest tests.test_adopt` passed 22 tests, run as root, where 0400 and 0000 files remain writable. No new test covers a 0400 file, a 0666 file, or a staged mode tighter than the existing one. The new tests do cover 0600 on both suffixes across adoption, upgrade and repeat, retire, edit-only, user-chmod, mode drift, and the hook staying executable.
Consequence: The #411 widening fix is well covered. E1, E3 and E8 above are evidence from this review's runs, not repository tests. Release impact: `not-material`.

## Unverified, with release impact

| Gap | Label |
|---|---|
| Non-POSIX filesystems (the plan already lists this) | deferred |
| Real target repository and real adoption diff (the plan's deferred verification) | deferred |
| Self-adoption refresh: installed `.claude/` and `.agents/` adopt skill copies differ from `process/adopt.md`; plan step 5 | deferred (must complete before the release candidate assets refresh) |
| `prepare()` run end to end with `bin/bundle` | not-material (candidate dir is preview only; `build_plan` output exercised) |
| ACLs, umask, setuid and group-write effects on preserved modes | not-material |
| Whether the manifest-mode follow-up issue exists | deferred |
| Native harness loading and hook enforcement | deferred (unchanged boundary from the release package) |
| Rule that store modes are advisory on existing `.md` and `.json` (F1) | deferred, pending the human's call |

No `blocking` gap found. Nothing here is labelled `accepted-risk`, because no authorization to accept is recorded.
