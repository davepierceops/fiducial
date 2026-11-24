# Review: intake/probe-skill — read-3-20261124T222600Z

Verdict: ready-with-findings
Reviewed: intake/probe-skill @ cc22fb9
Baseline: intake/probe-skill @ cdc1a32
Reviewer: reviewer-agent (subagent; did not author the delta or the amendment)
Date: 2026-11-24
Scope: `git diff cdc1a32..cc22fb9` (`process/probe.md`, `process/release.md`, `process/adopt.md`), against N1, N3, N4, N5, N6 of `reviews/probe-skill-read-2-20261124T215340Z.md`; every command the amended procedure names, checked against `.claude/settings.json` `permissions.deny` and the `.codex/hooks.json` deny entries.
Cross-checked: `.claude/settings.json`; `.codex/hooks.json`; the amended steps 1, 5, 6, 7, 8 and the Claude Code section of `process/probe.md` as read at cc22fb9.
Not inspected: live harness behaviour (no Claude Code or Codex session was started); whether adopted repositories ignore `__pycache__/`; whether the hooks create `__pycache__/` in a fresh clone (relied on read-2's run); the emitted skill bodies (not re-emitted; only the process sources were read); N2 (out of scope, #454).
Findings: 0 blocking, 0 non-blocking, 2 observations
The human should inspect: O1 (where the leftover temp path is reported).

## Verdict (quality): ready-with-findings

`bin/tests/run`: 464 tests, OK (verified by running at cc22fb9; working tree clean afterwards).

Disposition of the read-2 findings (verified by reading):

- N1 resolved. probe.md:26-31 records `git status --porcelain --ignored` in step 1 as the baseline; probe.md:87-94 compares against it, exempts a new `.claude/hooks/__pycache__/` or `.codex/hooks/__pycache__/` as a quoted known byproduct, and fails any other new ignored path or difference. Step 1 (probe.md:27-30) also no longer stops on that entry, so the probe does not fail or stop on a hook-created `__pycache__/` (N2's out-of-scope symptom is covered in the procedure).
- N3 resolved. release.md:47 puts the citation outside the N/A clause ("`<where relevant; otherwise N/A>`. Probe: <...>") and scopes it to this repository and each harness, with the emitted SHA, or "none was run". adopt.md:81 has the same scoping.
- N4 resolved. probe.md:140-141 labels the Task tool as inferred and unverified until observed; probe.md:141-143 passes an agent only when the quoted dispatch output names the emitted agent type and the reply comes from that dispatch.
- N5 resolved. probe.md:89-91 checks with `test -e` the path step 5 used, `process/probe-throwaway.txt` or the `rules` one.
- N6 resolved. probe.md:95-97 forbids `rm -rf`, and says to report the path and bare remote as left over outside the repository, which is acceptable.

New false pass / false failure / origin change / commit / deny-refused command (verified by reading each named command against the deny lists):

- New commands the amendment names: `git status --porcelain --ignored` (read only) and `test -e` (read only). Neither matches any `permissions.deny` entry or any `.codex/hooks.json` deny glob. `rm -rf` is named only to forbid it; no `rm` is run. The `Bash(rm -rf *)` deny entry is not in `.codex/hooks.json`, so the prohibition is conservative there and harmless.
- Origin: no step names `origin` or adds a remote; the push targets stay the literal temp bare remote (probe.md:61-67). No commit: the amendment adds only reads. DEC-001940 is not touched.
- False pass: the `__pycache__/` exemption is scoped to two exact hook directories; any other new path, tracked or ignored, still fails. Residual (inferred): a real untracked file placed inside those directories would be absorbed into the exemption. This needs a deliberate act and is not a realistic path.
- False failure: the baseline now includes the ignored list, so a `__pycache__/` present before step 1 does not register as new in step 7, and one created during the run is exempt. In a repository that does not ignore it, step 1's `--porcelain` shows it and step 7 shows the same, so there is no difference to flag.

## O1 — observation
Claim: Step 7 tells the runner to report the leftover temp path and bare remote, but step 8 says "Print one block, and only that block" and the report block has no line for it.
Location: process/probe.md:95-97, 98
Evidence: Verified by reading.
Consequence: The runner has to choose where to put it; the natural place is the `tree unchanged` evidence. No effect on the result.

## O2 — observation
Claim: Step 5's fallback ("use `rules` instead") does not name the file path, while step 7 now checks "the `rules` one".
Location: process/probe.md:55-57, 89-91
Evidence: Verified by reading. Inferred: the intended path is `rules/probe-throwaway.txt`.
Consequence: The runner infers the path; a different inference would make `test -e` check the wrong file.
