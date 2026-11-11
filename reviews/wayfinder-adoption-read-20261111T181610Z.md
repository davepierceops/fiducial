# Review: wayfinder adoption candidate (stage-1) — read-20261111T181610Z

Verdict: changes-required
Reviewed: /home/claude/adopt-work/stage-1/candidate @ plan.json sha256 15e4e360ee6906c30193eb145284fbe82aaaa19950778998a186965a2b98136c (store davepierceops/fiducial @ a8d87bc, tag v2026.11.10)
Baseline: /home/claude/wayfinder @ 1222d888c8bf6863bc5c77487a65bbeaca7e2d29 (main, clean, shallow clone)
Reviewer: independent subagent contradiction reader (adopt step 2); wrote none of the candidate
Date: 2026-11-11
Scope: All 66 candidate files (CLAUDE.md, AGENTS.md, .claude/settings.json, 7 .claude/hooks files, 8 .claude/agents, 15 .claude/skills, .claude/fiducial-ownership.json, .codex/hooks.json, 8 .codex/hooks files, 8 .codex/agents, 15 .agents/skills); plan.json; store process/adopt.md, process/project-setup.md, process/review-artifact.md; target skills/refresh.md, all six prompts/, both directives/, sourcing-notes.md, bin/product-builder-search, data/product-builder/README.md, employer-research/README.md, topics/data/20260822T1624Z/run.md, directory layout. Hooks were executed against a throwaway copy of the target overlaid with the candidate (in /tmp, since removed).
Cross-checked: code.claude.com/docs permissions.md and permission-modes.md (first 100,000 characters of the latter) for whether deny rules hold in bypassPermissions.
Not inspected: data file contents (CSV/JSON/JSONL) beyond structure and a secret-pattern grep; scripts/product_builder_fetch.py read only at lines 1-60 plus a grep for git, subprocess, environment, credential and network calls (585 lines total); employer-research/RESEARCH_SPEC.md and RESEARCH_SPEC_v2.md only grepped, not read; employer-research/scripts and logs not read; target git history beyond the single commit in this shallow clone; GitHub forge state (not queried by me); any user-level or managed Claude Code / Codex settings on the machine where wayfinder actually runs; live Claude Code or Codex behaviour (nothing was loaded in a real harness session).
Findings: 1 blocking, 4 non-blocking, 12 observations
The human should inspect: F1 (automated launches push to main under bypassPermissions; project-setup's fallback forbids that); F2 (is wayfinder SPEC.md-governed or directive-governed); O1 (decisions/log.md accepted-risk entry does not exist yet).

Label key: [observed] = I read or ran it; [inferred] = reasoned from what I read; [told] = stated by the coordinating session or by vendor docs; [unknown] = could not determine.

## Inventory confirmation

- [observed] The target contains no CLAUDE.md, AGENTS.md, AGENTS.override.md, .claude/, .codex/, .agents/, .fiducial/, SPEC.md, decisions/ or log.md at any depth (find over the tree excluding .git returned nothing).
- [observed] plan.json: inventory = {}, conflicts = [], edits = [], writes = 66, target = /home/claude/wayfinder. The empty inventory matches the target.
- [observed] sha256 of plan.json recomputed: 15e4e360…8136c, matching the value given.
- [observed] All 66 candidate files were read. Where two files are duplicates I read one and verified the other mechanically: the six hook scripts and _hooklib.py under .codex/hooks are byte-identical to .claude/hooks (cmp); AGENTS.md is byte-identical to CLAUDE.md (diff); each .agents/skills/*/SKILL.md differs from its .claude/skills twin only in quoted frontmatter values (diff -r); each .codex/agents/*.toml was parsed and its developer_instructions contains the full body of the matching .claude/agents/*.md, plus a two-line lane-guard preamble. .claude/fiducial-ownership.json was parsed (version 1, 65 entries: 40 markdown, 23 file, 2 json) and covers every candidate file except itself.

## Contradiction pass

Verdict (contradiction): changes-required

## F1 — blocking
Claim: The target's automated launch commits and pushes checkpoints straight to the default branch from a bypassPermissions session, while the staged context and the project-setup fallback it rests on require every landing by pull request and never a push to the default branch.
Classification: defect
Location: bin/product-builder-search:28 ("Checkpoint (write state + commit + push + check budget …)") and :33 (--permission-mode bypassPermissions); data/product-builder/README.md:46-47; directives/product-builder-search-20260903T222301Z.md:56 and :63. Staged: .claude/skills/command-blocks/SKILL.md:24 ("A block pushes a branch, never the default branch; the decision session merges that branch through a pull request"); also :20 (name remote and ref; the launch prompt says a bare "push"); .claude/skills/change-flow/SKILL.md:20. Store, not installed in the target: process/project-setup.md:21-27.
Evidence: [observed] by reading the cited lines. [told] the forge returned HTTP 403 for branch protection and rulesets (private repo, GitHub Free), so project-setup.md:21-27 applies: the fallback is precondition 2 alone plus every landing by pull request, never a push to the default branch, recorded in the project's decision log as an accepted-risk entry naming the plan that restores the forge layer. [observed] the target has no decisions/log.md, hence no such entry. [observed] no staged hook blocks a push to main: push-readback is PostToolUse and only reads back (ran it: exit 0 with "origin/main is at <sha>" after a successful push to a stand-in remote, exit 2 when the fetch fails).
Consequence: After install the repo would carry fiducial context while its one unattended job keeps doing what the precondition forbids; nothing mechanical stops it, and the accepted-risk record the fallback requires is absent. Alternatively a launch that reads command-blocks may refuse to push, and since the launch prompt says to stop when anything cannot be executed as written, cron launches would stop at the first checkpoint. [inferred] which of the two happens.
Fix: Human ruling before go. Options: (a) change bin/product-builder-search and the two directive lines so launches push a branch and land by PR; (b) rule data-checkpoint pushes to main an accepted risk and record it in decisions/log.md with the plan that would restore the forge layer. This is not expressible as an adopt "exact legacy edit": adopt.py only edits inventoried harness context, and bin/ and directives/ are not that. Proposed disposition: needs human structural resolution.
Related: F5

## F2 — non-blocking
Claim: The staged change flow routes every meaningful software change through an approved SPEC.md, test-designer red gate, pull request and two review passes, while the target changes its code by executing a directive directly and reporting.
Classification: defect
Location: directives/product-builder-fixup-20260904T165335Z.md:9 and :23 (make the changes, run one launch, report); directives/product-builder-search-20260903T222301Z.md:11; prompts/03-product-builder-search.md:13-17 ("The full specification is the directive"). Staged: .claude/skills/change-flow/SKILL.md:27-28; .claude/skills/build/SKILL.md:21; CLAUDE.md:8.
Evidence: [observed] by reading. [observed] the target has no SPEC.md, tests, or decisions/log.md; employer-research/RESEARCH_SPEC.md is a research brief, not the project spec the template describes.
Consequence: An agent given the next directive has two incompatible procedures. Build step 1 cannot be met (no SPEC.md), so it either stalls and asks, or ignores the skill. CLAUDE.md:8 by itself is compatible (a directive is a human-approved requirement; the SPEC.md clause is conditional). [inferred] how often the skill would be loaded; change-flow scopes itself to named roles in "software decision and execution sessions" and whether a wayfinder session counts is [unknown].
Fix: Human rules which governs: write a SPEC.md for wayfinder, or record a decision that directives are the approved requirements here and the build flow applies only where he invokes it. Proposed disposition: needs human structural resolution (a decision-log entry would suffice); accept as risk is the lighter alternative.

## F3 — non-blocking
Claim: The target forbids the orchestrating session from reading posting text, while staged CLAUDE.md requires claims about results to be checked against the underlying source.
Classification: defect
Location: prompts/03-product-builder-search.md:26-29; directives/product-builder-fixup-20260904T165335Z.md:9. Staged: CLAUDE.md:36 (last sentence).
Evidence: [observed] by reading. The launch report states hits found, taken from subagent verdicts and script summary lines only.
Consequence: Read strictly, the staged rule pushes the orchestrator to open batch files before reporting hits, which the directive calls a defect and which is the cost the fix-up was written to remove (fixup:5, "orchestrator token cost dominates"). Read loosely, nothing changes. [inferred] behaviour; not run.
Fix: Rule that the stage-2 verify subagent is the check of the underlying source for this pipeline. Proposed disposition: accept as risk, with that ruling recorded.

## F4 — non-blocking
Claim: The search directive tells the agent to resolve a directive-versus-convention disagreement itself and note it, while staged CLAUDE.md says to ask the human before relying on either source.
Classification: defect
Location: directives/product-builder-search-20260903T222301Z.md:11. Staged: CLAUDE.md:14.
Evidence: [observed] by reading. bin/product-builder-search:28 tells every launch to follow that directive "exactly".
Consequence: In an unattended launch nobody can answer; a launch that hits such a disagreement stops (consistent with directive:76) where today it would proceed and note it. Narrow: it only bites when the directive and repo convention actually disagree.
Fix: None needed in the candidate. Proposed disposition: accept as risk.

## F5 — non-blocking
Claim: The refresh procedure's commit block carries a placeholder the human must substitute, while the staged command-blocks skill says a block has no placeholders and runs verbatim as pasted.
Classification: suggestion
Location: skills/refresh.md:97-101 (git add data/YYYY-MM/ ; git commit -m "refresh YYYY-MM"). Staged: .claude/skills/command-blocks/SKILL.md:34 and :16.
Evidence: [observed] by reading. [observed] the commit itself trips no staged hook: push-readback exits 0 on a git add/commit command, and Edit/Write hooks exit 0 on data/, directives/, prompts/ and skills/ paths (18 pre-hook and 18 post-hook invocations, all exit 0).
Consequence: An agent asked to walk Dave through a refresh must recompose step 6 rather than quote it; a pasted "YYYY-MM" block would add a nonexistent path. The block also lands on main with no PR, which falls under F1's ruling.
Fix: Target-side edit of skills/refresh.md when convenient. Proposed disposition: accept as risk.
Related: F1

## O1 — observation
Claim: project-setup precondition 1 is unmet and its fallback is not yet in place. [told] branch protection and rulesets return 403 for this private Free-plan repo. [observed] process/project-setup.md:21-27 then requires: precondition 2, every landing by PR, and an accepted-risk entry in the project's decisions/log.md naming the plan that would restore the forge layer. [observed] the target has none of the three today: no force-push deny (no .claude/), no decisions/log.md, and direct-to-main practice (F1). The candidate supplies only the deny.
Location: process/project-setup.md:18-29 (store)

## O2 — observation
Claim: Precondition 2 is met on paper for Claude Code once installed. [observed] .claude/settings.json:78-85 denies eight force-push forms. [told] Claude Code docs: "Deny rules block in every mode, including bypassPermissions". Not live-verified. [told, same docs] deny rules match the command text as written and are "not a security boundary"; e.g. `git -C <dir> push --force` matches none of the eight patterns [inferred from the patterns]. For Codex the deny is a PreToolUse hook using fnmatch over the whole command string (.codex/hooks/codex-hook:126-128), so `cd x && git push --force` is not matched [observed in code]; Codex hook trust is a live boundary (adopt step 5). Whether Codex is ever run in wayfinder is [unknown]; the target's own docs name only Claude Code (skills/refresh.md:11).
Location: .claude/settings.json:78; .codex/hooks.json:43

## O3 — observation
Claim: Hooks do not misfire on the target's normal paths. [observed by running] intake-branch-guard, decision-log-append-only, review-artifact-immutable and all three store-lint checks exit 0 for writes under directives/, data/, prompts/, skills/ and employer-research/reviews/ (the guards match only top-level rules/, process/, reviews/, retros/ and decisions/log.md). They depend on no file absent from the target. They would bite only if the target later grows top-level process/, rules/, reviews/ or retros/ directories: e.g. a new reviews/ file without a timestamped name or Verdict lines fails store-lint (ran: exit 2), and any write under process/ on main is blocked (ran: exit 2).
Location: .claude/hooks/intake-branch-guard:13; .claude/hooks/store-lint:33

## O4 — observation
Claim: Eight agent types join the Agent tool in a repo whose pipeline dispatches untyped subagents by tier (prompts/03-product-builder-search.md:57-64). If a launch picked reviewer-agent or another lane-bound type for the screen/verify/extract stages, lane-guard would block its write to the result file (ran lane-guard on non-lane paths: exit 2) and it would run on the opus tier. [unknown] how likely; the prompts name tiers, not agent types.
Location: .claude/agents/reviewer-agent.md:4-12

## O5 — observation
Claim: Every unattended launch would load the 47-line CLAUDE.md plus skill and agent listings into a session capped at $2.00 whose orchestrator cost already dominated (fixup directive:5), and push-readback adds a git fetch after each checkpoint push. [inferred] fewer fetches per dollar; magnitude [unknown]. Whether project hooks run under `claude -p --permission-mode bypassPermissions` without a trust prompt is [unknown].
Location: bin/product-builder-search:32-36

## O6 — observation
Claim: Store-only skills are installed. intake edits rules/ and process/ rows that do not exist here (.claude/skills/intake/SKILL.md:17-23); adopt needs a store checkout and its bin/bundle (.claude/skills/adopt/SKILL.md:15-20); voice and outline govern Dave's published prose and cite "rows in this bundle" that are not in the target (.claude/skills/voice/SKILL.md:8-11). [inferred] mostly harmless: they are loaded on demand, and gate is disable-model-invocation. The one misfire path: intake's description ("a proposed change to governed context") could match a request to change wayfinder's prompts or directives and send it down an intake/<slug> branch and Context Quality Reviewer path that has nothing to act on. Not a contradiction with target text.
Location: .claude/skills/intake/SKILL.md:3

## O7 — observation
Claim: Staged skills point at files that will not exist in the target: process/change-flow.md, process/review-artifact.md, process/release.md, process/gate.md, process/decision-log.md, process/verification-checklists.md (build:10-11,36,38; intake:28,31,36; release:14; adopt:54), a `project-setup` document with no skill of that name (adopt:11,15,61), and rule IDs such as [R0462] that resolve only in the store. The same content exists as skills, so an agent can recover, but the precondition text of project-setup is nowhere in the target after install.
Location: .claude/skills/build/SKILL.md:10

## O8 — observation
Claim: Naming overlaps without collision. The target's skills/refresh.md is a human-run procedure, not a harness skill; no staged skill is named refresh. The target's employer-research/reviews/ holds reviewer CSVs and is outside the staged reviews/ convention and hooks. The target's directives/<descriptor>-<timestamp>Z.md naming is compatible with the staged timestamp form; no candidate file mentions "directive" (grep), and the staged term for the same thing is "execution block" (command-blocks:14).
Location: skills/refresh.md:1

## O9 — observation
Claim: No secret value found in the target. [observed] a pattern grep for API keys, tokens, private keys and password assignments over the working tree returned nothing; the fetch script's grep shows no environment reads, no Authorization headers, no git or subprocess calls; both directives forbid fetching or storing anything requiring credentials (search:78, fixup:35). Separate from secrets: skills/refresh.md:66 and :99 would commit companies_with_connections.csv, which holds names of LinkedIn connections; no such file is in data/ at this commit.
Location: scripts/product_builder_fetch.py:146

## O10 — observation
Claim: What the adoption will not do, and what the procedure still requires afterwards (adopt steps 4-5): create decisions/log.md and append the adoption ruling and the O1 accepted-risk entry; create docs/fiducial-adoption-20261111T180953Z.md (helper does this); create the five forge labels (touches GitHub, needs the same authorization); open the target's own PR rather than push main; keep a report copy in fiducial reviews/; have Dave open a fresh session at the target and run /context before Claude Code loading is called anything but contract-verified. The candidate creates no SPEC.md, retros/, reviews/ or tracker. Whether GitHub Issues is enabled on the target (the staged "loose-end tracker", CLAUDE.md:46) is [unknown].
Location: .claude/skills/adopt/SKILL.md:47-73

## O11 — observation
Claim: The models named in the agents (.claude/agents: opus, sonnet; .codex/agents: gpt-6-astra, gpt-6.1-sol) are fixed by the emitter; whether those Codex model names are valid for Dave's account is [unknown].
Location: .codex/agents/architect-agent.toml:3

## O12 — observation
Claim: The target clone I read is shallow (one commit), so the "existing refresh commit convention" could be checked only against skills/refresh.md:100 and the single commit subject, not against history.
Location: skills/refresh.md:100
