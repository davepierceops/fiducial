# Review: wayfinder adoption candidate (stage-1) — read-20261111T181610Z (redacted copy)

Redacted copy for the public store. The adopting repository is private; its file paths, line numbers, quoted text, and descriptions of its contents are replaced with `[redacted: private target detail]` or removed. Verdicts, finding ids, severities, classifications, staged-side citations, and proposed dispositions are unchanged. The unredacted artifact is kept with the adopting repository.

Verdict: changes-required
Reviewed: the adoption candidate (stage-1) @ plan.json sha256 15e4e360ee6906c30193eb145284fbe82aaaa19950778998a186965a2b98136c (store davepierceops/fiducial @ a8d87bc, tag v2026.11.10)
Baseline: the target @ 1222d888c8bf6863bc5c77487a65bbeaca7e2d29 (main, clean, shallow clone)
Reviewer: independent subagent contradiction reader (adopt step 2); wrote none of the candidate
Date: 2026-11-11
Scope: All 66 candidate files (CLAUDE.md, AGENTS.md, .claude/settings.json, 7 .claude/hooks files, 8 .claude/agents, 15 .claude/skills, .claude/fiducial-ownership.json, .codex/hooks.json, 8 .codex/hooks files, 8 .codex/agents, 15 .agents/skills); plan.json; store process/adopt.md, process/project-setup.md, process/review-artifact.md; the target's own working context ([redacted: private target detail]). Hooks were executed against a throwaway copy of the target overlaid with the candidate, since removed.
Cross-checked: code.claude.com/docs permissions.md and permission-modes.md (first 100,000 characters of the latter) for whether deny rules hold in bypassPermissions.
Not inspected: target data file contents beyond structure and a secret-pattern grep; parts of the target's scripts and research documents ([redacted: private target detail]); target git history beyond the single commit in the shallow clone; GitHub forge state (not queried by the reader); any user-level or managed Claude Code / Codex settings on the machine where the target actually runs; live Claude Code or Codex behaviour (nothing was loaded in a real harness session).
Findings: 1 blocking, 4 non-blocking, 12 observations
The human should inspect: F1; F2; O1.

Label key: [observed] = the reader read or ran it; [inferred] = reasoned from what was read; [told] = stated by the coordinating session or by vendor docs; [unknown] = could not determine.

## Inventory confirmation

- [observed] The target contains no CLAUDE.md, AGENTS.md, AGENTS.override.md, .claude/, .codex/, .agents/, .fiducial/, SPEC.md, decisions/ or log.md at any depth.
- [observed] plan.json: inventory = {}, conflicts = [], edits = [], writes = 66. The empty inventory matches the target.
- [observed] sha256 of plan.json recomputed: 15e4e360…8136c, matching the value given.
- [observed] All 66 candidate files were read. Where two files are duplicates one was read and the other verified mechanically: the six hook scripts and _hooklib.py under .codex/hooks are byte-identical to .claude/hooks; AGENTS.md is byte-identical to CLAUDE.md; each .agents/skills/*/SKILL.md differs from its .claude/skills twin only in quoted frontmatter values; each .codex/agents/*.toml contains the full body of the matching .claude/agents/*.md, plus a two-line lane-guard preamble. .claude/fiducial-ownership.json was parsed (version 1, 65 entries: 40 markdown, 23 file, 2 json) and covers every candidate file except itself.

## Contradiction pass

Verdict (contradiction): changes-required

## F1 — blocking
Claim: The target has an automated job that pushes straight to the default branch, while the staged context and the project-setup fallback it rests on require every landing by pull request and never a push to the default branch.
Classification: defect
Location: [redacted: private target detail]. Staged: .claude/skills/command-blocks/SKILL.md:24 and :20; .claude/skills/change-flow/SKILL.md:20. Store, not installed in the target: process/project-setup.md:21-27.
Evidence: [observed] by reading the cited lines. [told] the forge returned HTTP 403 for branch protection and rulesets (private repo, GitHub Free), so project-setup.md:21-27 applies. [observed] the target has no decisions/log.md, hence no accepted-risk entry. [observed] no staged hook blocks a push to main: push-readback is PostToolUse and only reads back (ran it against a stand-in remote).
Consequence: After install the repo would carry fiducial context while its unattended job keeps doing what the precondition forbids, with the accepted-risk record absent; or the job reads command-blocks, refuses to push, and stops. [inferred] which of the two happens.
Fix: Human ruling before go: change the job to push a branch and land by PR, or record an accepted-risk decision. Not expressible as an adopt "exact legacy edit", because the files involved are not inventoried harness context. Proposed disposition: needs human structural resolution.
Related: F5

## F2 — non-blocking
Claim: The staged change flow routes every meaningful software change through an approved SPEC.md, test-designer red gate, pull request and two review passes, while the target changes its code by executing a directive directly and reporting.
Classification: defect
Location: [redacted: private target detail]. Staged: .claude/skills/change-flow/SKILL.md:27-28; .claude/skills/build/SKILL.md:21; CLAUDE.md:8.
Evidence: [observed] by reading. [observed] the target has no SPEC.md, tests, or decisions/log.md.
Consequence: An agent given the next directive has two incompatible procedures; build step 1 cannot be met, so it stalls and asks, or ignores the skill. CLAUDE.md:8 by itself is compatible. Whether a session in the target counts as a "software decision and execution session" is [unknown].
Fix: Human rules which governs. Proposed disposition: needs human structural resolution (a decision-log entry would suffice); accept as risk is the lighter alternative.

## F3 — non-blocking
Claim: The target has its orchestrating session report results from subagent verdicts without reading the underlying material itself, while staged CLAUDE.md requires claims about results to be checked against the underlying source.
Classification: defect
Location: [redacted: private target detail]. Staged: CLAUDE.md:36 (last sentence).
Evidence: [observed] by reading.
Consequence: Read strictly, the staged rule pushes the orchestrator to read the underlying material, a cost the target's design deliberately removed. Read loosely, nothing changes. [inferred] behaviour; not run.
Fix: Rule that the pipeline's verify subagent is the check of the underlying source. Proposed disposition: accept as risk, with that ruling recorded.

## F4 — non-blocking
Claim: A target directive tells the agent to resolve a directive-versus-convention disagreement itself and note it, while staged CLAUDE.md says to ask the human before relying on either source.
Classification: defect
Location: [redacted: private target detail]. Staged: CLAUDE.md:14.
Evidence: [observed] by reading.
Consequence: An unattended run that hits such a disagreement stops where today it would proceed and note it. Narrow: it only bites when the directive and repo convention actually disagree.
Fix: None needed in the candidate. Proposed disposition: accept as risk.

## F5 — non-blocking
Claim: A human-run procedure in the target has a commit block carrying a placeholder the human must substitute, while the staged command-blocks skill says a block has no placeholders and runs verbatim as pasted.
Classification: suggestion
Location: [redacted: private target detail]. Staged: .claude/skills/command-blocks/SKILL.md:34 and :16.
Evidence: [observed] by reading. [observed] the commit itself trips no staged hook (18 pre-hook and 18 post-hook invocations on the target's normal paths, all exit 0).
Consequence: An agent asked to walk the human through the procedure must recompose that step rather than quote it. The block also lands on main with no PR, which falls under F1's ruling.
Fix: Target-side edit when convenient. Proposed disposition: accept as risk.
Related: F1

## O1 — observation
Claim: project-setup precondition 1 is unmet and its fallback is not yet in place. [told] branch protection and rulesets return 403 for this private Free-plan repo. [observed] process/project-setup.md:21-27 then requires precondition 2, every landing by PR, and an accepted-risk entry in the project's decisions/log.md. [observed] the target has none of the three before install; the candidate supplies only the deny.
Location: process/project-setup.md:18-29 (store)

## O2 — observation
Claim: Precondition 2 is met on paper for Claude Code once installed. [observed] .claude/settings.json:78-85 denies eight force-push forms. [told] Claude Code docs say deny rules block in every mode, including bypassPermissions, and that deny rules match the command text as written and are not a security boundary; `git -C <dir> push --force` matches none of the eight patterns [inferred from the patterns]. For Codex the deny is a PreToolUse hook using fnmatch over the whole command string (.codex/hooks/codex-hook:126-128), so `cd x && git push --force` is not matched [observed in code]. Not live-verified. Whether Codex is ever run in the target is [unknown].
Location: .claude/settings.json:78; .codex/hooks.json:43

## O3 — observation
Claim: Hooks do not misfire on the target's normal paths. [observed by running] intake-branch-guard, decision-log-append-only, review-artifact-immutable and all three store-lint checks exit 0 for writes under the target's working directories (the guards match only top-level rules/, process/, reviews/, retros/ and decisions/log.md). They depend on no file absent from the target. They would bite only if the target later grows top-level process/, rules/, reviews/ or retros/ directories.
Location: .claude/hooks/intake-branch-guard:13; .claude/hooks/store-lint:33

## O4 — observation
Claim: Eight agent types join the Agent tool in a repo whose pipeline dispatches untyped subagents by tier. If a run picked a lane-bound type, lane-guard would block its write to a non-lane path (ran: exit 2) and it would run on the opus tier. Likelihood [unknown].
Location: .claude/agents/reviewer-agent.md:4-12

## O5 — observation
Claim: Every unattended run in the target would load the 47-line CLAUDE.md plus skill and agent listings into a cost-capped session, and push-readback adds a git fetch after each push. [inferred] higher cost per run; magnitude [unknown]. Whether project hooks run under `claude -p --permission-mode bypassPermissions` without a trust prompt is [unknown].
Location: [redacted: private target detail]

## O6 — observation
Claim: Store-only skills are installed. intake edits rules/ and process/ rows that do not exist in the target (.claude/skills/intake/SKILL.md:17-23); adopt needs a store checkout and its bin/bundle (.claude/skills/adopt/SKILL.md:15-20); voice and outline govern the author's published prose and cite "rows in this bundle" that are not in the target (.claude/skills/voice/SKILL.md:8-11). [inferred] mostly harmless: they are loaded on demand, and gate is disable-model-invocation. The one misfire path: intake's description could match a request to change the target's own instructions and send it down an intake branch path that has nothing to act on.
Location: .claude/skills/intake/SKILL.md:3

## O7 — observation
Claim: Staged skills point at files that will not exist in the target: process/change-flow.md, process/review-artifact.md, process/release.md, process/gate.md, process/decision-log.md, process/verification-checklists.md (build:10-11,36,38; intake:28,31,36; release:14; adopt:54), a `project-setup` document with no skill of that name (adopt:11,15,61), and rule IDs such as [R0462] that resolve only in the store. The same content exists as skills, so an agent can recover, but the precondition text of project-setup is nowhere in the target after install.
Location: .claude/skills/build/SKILL.md:10

## O8 — observation
Claim: Naming overlaps without collision. The target has directories and files whose names resemble staged conventions ([redacted: private target detail]); none collides with a staged skill, hook-guarded path, or file. No candidate file mentions "directive"; the staged term for the same thing is "execution block" (command-blocks:14).
Location: [redacted: private target detail]

## O9 — observation
Claim: No secret value found in the target. [observed] a pattern grep for API keys, tokens, private keys and password assignments over the working tree returned nothing. One non-secret privacy note about a file the target's procedure would commit is redacted.
Location: [redacted: private target detail]

## O10 — observation
Claim: What the adoption will not do, and what the procedure still requires afterwards (adopt steps 4-5): create decisions/log.md and append the adoption ruling and the O1 accepted-risk entry; create docs/fiducial-adoption-20261111T180953Z.md (helper does this); create the five forge labels; open the target's own PR rather than push main; keep a report copy in fiducial reviews/; have the human open a fresh session at the target and run /context before Claude Code loading is called anything but contract-verified. The candidate creates no SPEC.md, retros/, reviews/ or tracker. Whether GitHub Issues is enabled on the target is [unknown].
Location: .claude/skills/adopt/SKILL.md:47-73

## O11 — observation
Claim: The models named in the agents (.claude/agents: opus, sonnet; .codex/agents: gpt-6-astra, gpt-6.1-sol) are fixed by the emitter; whether those Codex model names are valid for the human's account is [unknown].
Location: .codex/agents/architect-agent.toml:3

## O12 — observation
Claim: The target clone the reader used is shallow (one commit), so the target's commit conventions could be checked only against its written procedure and the single commit subject, not against history.
Location: [redacted: private target detail]
