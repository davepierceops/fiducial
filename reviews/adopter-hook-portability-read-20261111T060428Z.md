# Review: intake/adopter-hook-portability — read-20261111T060428Z

Verdict: ready-with-findings
Reviewed: intake/adopter-hook-portability @ b3be5cc
Baseline: main @ 7288be8
Reviewer: reviewer session (quality, skepticism, continuity passes), wrote none of the delta
Date: 2026-11-11
Scope: git diff 7288be8..b3be5cc (13 files); plan and amendments; issues #412, #415, #416 with comments; red/green logs. Ran: full suite at b3be5cc (uid 0): "Ran 381 tests in 113.499s / OK", no skips reported. Throwaway experiments under /tmp/rv only.
Cross-checked: process/review-artifact.md, verification-checklists skill, decisions/log.md (DEC-001730 area), README.md, role bundles via bin/bundle at base and tip, emitted hooks.
Not inspected: live Claude Code or Codex hook delivery and skill loading (#439); ACL, read-only-filesystem and immutable-flag cases for A; the Context Quality read over the process/adopt.md delta (separate read); decision-log entry (due at merge); GitHub close-out of the issues.
Findings: 0 blocking, 7 non-blocking, 2 observations
The human should inspect: F1 (whether A2's "cannot perform" covers chmod by a non-owner) and F5 (C4 wording).

## Pass: quality
Verdict (quality): ready-with-findings
Each unit is small. A is one loop in the apply function. B is a 2-line strip plus an 8-line adapter normaliser. C is one regex helper plus two call sites. Red log: 52 failures (17 distinct tests) at base, 381 OK after; failures are the new behaviour tests, not import errors. See F2, F4, F6.

## Pass: skepticism
Verdict (skepticism): ready-with-findings
Experiments (scripts /tmp/rv/expA.py, shell session in /tmp/rv/bo). I ran as uid 0, which makes os.access always true and hides every permission case. I therefore ran apply as uid 65534 with setpriv.
- A, nobody-uid, 66 planned writes: clean apply rc=0; directory-for-file after prepare rc=2 target unchanged; a parent dir turned into a file ("docs") rc=2 unchanged; .claude at 0500 and 0100, target root 0555 each rc=2 "no write and search permission" with target unchanged. Held.
- B, via the emitted Codex adapter against a local bare origin: cmd string, cmd list and command string read back origin/codex/probe at the right SHA; unpushed commit rc=2 in both forms; +HEAD:refs/heads/a/b/c, bare slash branch, tags, HEAD:HEAD ok; apply_patch and non-shell tools unaffected. Held, with F2 and F3.
- C: see F4; real-store emission is clean.

## F1 — non-blocking
Claim: A refuses before writing for the listed cases but not when the runner can write a file it does not own; chmod then fails mid-apply.
Classification: defect
Location: process/adopt.md:371-376 (preflight), :405 region (path.chmod in the write loop)
Evidence: ran. CLAUDE.md owned by root, mode 0666, runner uid 65534: preflight passes (os.access W_OK true), apply writes 65 files, then "adopt: [Errno 1] Operation not permitted: .../CLAUDE.md", rc=2, target changed (65 new files, no report).
Consequence: same partial-write class #412 targets, in a shared-checkout case. A2 lists three cases, all met; its lead sentence ("cannot perform") is wider.
Fix: preflight also requires os.stat(path).st_uid == os.geteuid() (or euid 0) for any existing path that will be chmodded, or the plan records it as an accepted boundary in adopt.md's stated limits.

## F2 — non-blocking
Claim: push-readback mis-parses a `+` refspec without a colon: dst keeps the `+`.
Classification: defect (pre-existing, not in the delta's criteria)
Location: bin/hooks/push-readback:101,103
Evidence: ran. `git push origin +main` through the adapter, rc=2 "origin/+main reads back caad814...; local main is dd16f2c" although the push is correct.
Consequence: false loud failure, not a silent pass. `+HEAD:refs/heads/a/b/c` works.
Fix: lstrip("+") on dst when there is no colon.

## F3 — non-blocking
Claim: the adapter normalises `cmd` lists only; a shell payload with `command` as a list reaches push-readback unjoined and crashes.
Classification: defect (pre-existing; deny() joins command lists, normalisation does not)
Location: bin/rulestore/emit/codex.py:204-209
Evidence: ran. tool_name shell, tool_input.command a list: rc=2 with a Python traceback from push-readback line 78.
Consequence: loud, noisy block of a valid push. B2 names only cmd.
Fix: join a list under command as well, as deny() already does.

## F4 — non-blocking
Claim: the reference rewrite has no left boundary and no right boundary, so text that merely resembles a reference is altered.
Classification: defect (latent; the real store is clean)
Location: bin/rulestore/emit/common.py (_PROCESS_REF_RE)
Evidence: ran the helper directly with a placeholder form. "docs/process/gate.md" -> "docs/SK(gate)"; "subprocess/gate.md" -> "subSK(gate)"; "https://x.io/process/gate.md" -> "https://x.io/SK(gate)"; "process/gate.mdx" -> "SK(gate)x"; "process/gate.md#sec" -> "SK(gate)#sec"; a lone backtick on one side is dropped. A name outside the stem set fails emission, and process/sub/gate.md is left alone.
Consequence: a future skill that mentions a path ending in process/<skill>.md is silently rewritten. No current skill is affected (real emission checked).
Fix: anchor with (?<![\w/.-]) on the left and (?![\w-]) on the right of the match.

## F5 — non-blocking
Claim: C4 ("twelve role bundles byte-identical") is not true as written: the chief-of-staff bundle changes.
Classification: defect (plan and verification wording)
Location: docs/plans/adopter-hook-portability-plan-20261111T053544Z.md C4
Evidence: ran bin/bundle --where role=<each> on git-archive copies of 7288be8 and b3be5cc, ignoring the provenance line. 11 identical; chief-of-staff differs by exactly the process/adopt.md preflight hunk (adopt.md is in that bundle). Agent files from both emissions are identical.
Consequence: the guard is over-stated; the difference is the intended A change, so no behaviour is wrong. The Project's pinned chief-of-staff bundle doc is also now stale for that text.
Fix: reword C4 to "eleven identical; chief-of-staff differs only by the adopt.md hunk", and note the bundle doc as stale.

## F6 — non-blocking
Claim: an unrelated line was added to an existing test.
Classification: suggestion
Location: bin/tests/test_hooks.py:483
Evidence: read; git diff shows a second write(self.repo, "README.md", "never pushed\n") directly after write(... "changed\n") in test_git_dash_c_push_the_remote_did_not_take_fails_loudly.
Consequence: none functional; the line before it is now dead; it is outside any criterion.
Fix: drop the added line.

## F7 — non-blocking
Claim: the plan amendment names the wrong pin.
Classification: defect (record)
Location: plan "Amendments", second bullet
Evidence: read. It says the comparisons are pinned to the batch's landed snapshot "(`5bd4170`)"; 5bd4170 is the commit that makes the change. The tests pin LANDED/EXTRACTED to 2be5327 (test_review_verification_pruning.py:26), cb0194a (test_claude_rule_pruning.py:35) and fb310dd (test_skill_context_extraction.py:29), all ancestors of main.
Consequence: a reader looking for the snapshot finds the wrong commit.
Fix: cite the three commits.

## O1 — observation
Emitted change-flow skill still says "prose in `process/`" (cc/.claude/skills/change-flow/SKILL.md:18). It names the directory, not a `process/<stem>.md` document, so C1/C2 do not reach it; an adopter has no such directory.

## O2 — observation
Continuity pass on the three pinned pruning tests: each still compares landed-commit emission against its own baseline with assertTrue(paths) guarding emptiness, so they prove the historical claim. They no longer detect later drift in hook bytes; that was the plan's ruling.

## Pass: continuity
Verdict (continuity): ready-with-findings
Checked: adopt.md prose (:93-96, idle branch and I/O-failure boundary) still holds and was not edited; README/SPEC.md references to process/ are source-repo links and unaffected; role bundles per F5; emitted Claude Code and Codex trees both have 9 rewritten references, 0 missing targets, and no remaining `process/<stem>.md` in any skill; C2 verified by editing a copy of release.md in /tmp to reference process/nonesuch.md: both harnesses refuse rc=2 naming the file and reference. Findings F5, F7.
