# Review: intake/probe-skill — read-20261124T190213Z

Verdict: changes-required
Reviewed: intake/probe-skill @ b59b8d1
Baseline: intake/probe-skill @ a3f341b
Reviewer: context-quality-reviewer (subagent; did not author the delta)
Date: 2026-11-24
Scope: `git diff a3f341b..b59b8d1`: DEC-001940, DEC-001950 and DEC-001960 in `decisions/log.md` (checked only that the build matches them), new `process/probe.md`, and the two new emitter tests. Requirements: issue #439 body (fetched with `gh api`), those three entries, DEC-001810.
Cross-checked: `.claude/settings.json`; `.claude/hooks/{intake-branch-guard,decision-log-append-only,review-artifact-immutable,push-readback,_hooklib.py}`; `.codex/hooks.json`; `.codex/hooks/codex-hook`; `bin/rulestore/emit/claude_code.py`, `codex.py` and `common.py`; `process/adopt.md:73`; `process/named-queries.md`; `CLAUDE.md` and `AGENTS.md` heads; a fresh `bin/bundle --emit claude-code` and `--emit codex` into a temp directory.
Not inspected: live harness behaviour of any kind. No Claude Code or Codex session was started, so Claude Code's deny-pattern matching, how a permission prompt or a sandbox refusal is worded, Codex skill and agent listing, `codex --version`, and Codex trust are inferred or unknown, as the findings say. `process/release.md` was searched only for the word "probe" (no hits).
Findings: 6 blocking, 6 non-blocking, 3 observations
The human should inspect: F3 (a false pass could reach a live-verified record) and F6 (whether the requirement that release and adoption records cite the probe report belongs in this change or is deferred).

## Verdict (quality): changes-required

The tests: `bin/tests/run` ran 464 tests, OK (verified by running). With `process/probe.md` removed in a temporary worktree at `b59b8d1`, both new tests fail (`FAILED (errors=2)`, verified by running). The emitter writes `.claude/skills/probe/SKILL.md` and `.agents/skills/probe/SKILL.md` with the same body (diff of the bodies is empty, verified by running).

Trace against DEC-001940 (verified by reading, plus running where stated): no step names `origin` or adds a remote. No step commits. The only pushes target a bare repository the probe creates. Each governed edit has a stated revert. If a hook is broken, the worst outcome is a reverted working-tree edit or a ref written in the throwaway. The end-of-run check catches tracked and untracked residue. It misses ignored files (F9). The procedure meets DEC-001940 except for the `$TMP` defect (F1).

## F1 — blocking
Claim: `$TMP` is never assigned, and when the push read-back hook is given the literal `"$TMP/remote.git"` it fails. Followed as written, the push-readback probe therefore always returns a false failure.
Classification: defect
Location: process/probe.md:25-26, 45-47, 55-57
Evidence: Verified by running. I fed `.claude/hooks/push-readback` a PostToolUse payload whose command was `git push "$TMP/remote.git" HEAD:refs/heads/probe`. It exited 2 with `fetch $TMP/remote.git probe failed: ... does not appear to be a git repository`: the hook `shlex`-splits the command text and does no shell expansion. The same payload with the literal mktemp path printed `push-readback: /tmp/tmp.../remote.git/probe is at b59b8d1...` and exited 0. Step 1 says only "Make a temporary directory with `mktemp -d`". Nothing binds it to `TMP`, and a Bash call does not carry shell variables into the next one. Where `TMP` is unset, the `git init --bare` builds the throwaway at `/remote.git`, outside the temporary directory that step 7 removes.
Consequence: Every run reports `hook push-readback: failed` (or not run), and the throwaway may land outside the temp directory.
Fix: In step 1, record the absolute path that `mktemp -d` printed. Write every later command with that literal path, never a variable. Run the plain push and the force push as separate tool calls, so that a deny on the force push cannot also swallow the plain push.

## F2 — blocking
Claim: The context check depends on the repository and SHA marker, which is an HTML comment on line 2 and not "the first line". At least one Claude Code surface does not show that marker to the model, so the check fails falsely.
Classification: defect
Location: process/probe.md:27-30
Evidence: Verified by reading: line 1 of `CLAUDE.md` and `AGENTS.md` is `<!-- fiducial:begin -->`, and the marker `<!-- fiducial davepierceops/fiducial @ a8d87bc... -->` is on line 2. Observed: this reviewer runs as a Claude Code agent in this repository, and the `CLAUDE.md` project instructions it received begin at "Never let a secret value enter context." with neither comment line present. Whether every Claude Code surface strips comments is unknown.
Consequence: Loaded context is reported `context: failed`, or a runner guesses a SHA to make it pass.
Fix: Base the check on body text. For example, state the first and last instruction sentences, then open the file and compare. Report the marker SHA only if the session saw it, and give it separately from the pass/fail.

## F3 — blocking
Claim: Step 6 counts any refusal as passed. A refusal that did not come from the deny entry would be recorded as a pass in a live-verified report: a permission prompt the human declined, a sandbox denial, or a Codex approval refusal.
Classification: defect
Location: process/probe.md:58-62
Evidence: Verified by reading. Step 5 requires "a refusal by the named hook", but step 6 says only "a refusal is passed". In Claude Code, a command that the deny list does not match and the allow list does not cover prompts the human, and the human's "no" comes back as a refusal (inferred from the harness's permission model, not observed in a session). Verified by running: the Codex adapter's own refusal text is `codex-hook: denied by Bash(kubectl apply*)`, so it can be told apart from other refusals.
Consequence: A broken deny entry is reported `passed`, and release and adoption records then cite it as live-verified. This is the false confidence #439 exists to remove.
Fix: Count step 6 as passed only when the quoted output names the deny entry or the harness's deny-by-settings message. Report any other refusal as not run, with the quote. State that "command not found" for `kubectl` or `terraform` is failed, as step 6 already says for the missing `~/.ssh` file.

## F4 — blocking
Claim: #439's acceptance criterion "a human can start with a single paste" has no counterpart: the procedure never gives a start line for either harness.
Classification: defect
Location: process/probe.md (whole document; the "Claude Code" and "Codex" sections)
Evidence: Verified by reading the #439 body and the document. The Codex emitter writes skill references as `$<stem>` (`bin/rulestore/emit/codex.py:243, 372`), which suggests `$probe` there and `/probe` in Claude Code. Both are inferred and not observed.
Consequence: The human has to compose the start step himself, which is the thing the acceptance criterion rules out.
Fix: Add one start paste to each harness section, composed under the command-blocks skill, and mark the invocation form as inferred until the first run observes it.

## F5 — blocking
Claim: DEC-001960 says each harness section names "how agents are listed and dispatched". The Codex section names only the file location for agents and skills. The Claude Code section's `/agents` is an interactive command that the human runs, not the model.
Classification: defect
Location: process/probe.md:98-99, 111-112
Evidence: Verified by reading DEC-001960 and the sections. How Codex lists skills and dispatches agents is unknown to this reviewer, and the procedure does not say it is unknown.
Consequence: In Codex, step 4 gives the runner no mechanism, so the agent results are improvised, and a dispatch that silently ran in the main session could pass as dispatchable.
Fix: Name the Codex listing and dispatch mechanism, or say it is unverified and that step 4 is not run where no dispatch tool exists. Say that `/agents` is human-run, or drop it, since step 4 needs only dispatch. Require the agent's reply to come from a dispatched subagent, quoted with the harness's dispatch output.

## F6 — blocking
Claim: DEC-001950 and the #439 acceptance criterion require release and adoption records to cite the probe report (or say none was run). The delta does not build that, and `adoptions/` does not exist yet.
Classification: defect
Location: process/release.md and process/adopt.md (unchanged); process/adopt.md:73; repository root
Evidence: Verified by running `grep -rn probe process/ rules/`: the only hit outside `probe.md` is R1616's unrelated "probe". `ls adoptions` fails. Neither commit message records a deferral.
Consequence: Nothing obliges a release or adoption record to cite the probe, so the acceptance criterion is unmet and the unverified boundary keeps being restated without a link to evidence.
Fix: Add the citation requirement to `process/release.md` and `process/adopt.md`, with the `adoptions/probe-<repo>-<harness>-<UTC timestamp>.md` name, or record Dave's deferral of it to a named issue.

## F7 — non-blocking
Claim: The landed-review probe picks "a tracked file under `reviews/`", but the hook refuses only files that exist on `origin/main` or `main`. A file that is tracked on the branch but not landed is allowed, which gives a false failure.
Classification: defect
Location: process/probe.md:53-54
Evidence: Verified by reading `.claude/hooks/review-artifact-immutable` and `_hooklib.on_default_branch` (lines 101-109).
Consequence: On a branch that carries a new review artifact, `hook review-artifact: failed` is recorded for a working hook.
Fix: Pick the file from `git ls-tree --name-only origin/main reviews/`, falling back to `main`.

## F8 — non-blocking
Claim: The hook probes do not say which tool makes the edit. The hooks match only `Edit|Write` (in Codex, `apply_patch` through the adapter), so an edit made through the shell bypasses them and is reported as a hook failure.
Classification: defect
Location: process/probe.md:42-54
Evidence: Verified by reading `.claude/settings.json` (PreToolUse matcher `Edit|Write`) and `.codex/hooks.json`.
Consequence: A `sed -i` attempt makes the decision-log, intake-guard and review-artifact probes fail although the hooks work.
Fix: State that each edit goes through the harness's file-edit tool: Edit or Write in Claude Code, `apply_patch` in Codex.

## F9 — non-blocking
Claim: The end-of-run check misses ignored files, empty directories, new refs and local config, so a throwaway left under an ignored path would go unnoticed.
Classification: suggestion
Location: process/probe.md:63-66
Evidence: Verified by reading. `git status --porcelain` omits ignored files. In an adopted repository, `process/probe-throwaway.txt` could match a `.gitignore` entry. No step writes refs or config (traced), so for those this is defence in depth.
Consequence: `tree unchanged: yes` could be reported over residue.
Fix: Add `git status --porcelain --ignored`, and `test -e` on the throwaway path. Optionally, compare `git for-each-ref` and `git config --local --list` with their values at step 1.

## F10 — non-blocking
Claim: Step 6 probes 3 of the deny entries (37 in Claude Code), and the ssh read does not say whether it is the `Read(~/.ssh/**)` entry (Read tool) or the `Bash(cat ~/.ssh/*)` entry (shell).
Classification: suggestion
Location: process/probe.md:58-62, 86
Evidence: Verified by reading `.claude/settings.json` and `.codex/hooks.json`. Verified by running: the Codex adapter refuses `kubectl apply --help`, `terraform apply -help`, `cat ~/.ssh/probe-does-not-exist` and `git push --force "<path>" ...` as string commands, so the inert forms do match there. Claude Code's matching of `Bash(kubectl apply*)` against `kubectl apply --help` is inferred, not observed.
Consequence: A report reading `deny: passed` can be taken to cover entries never probed. Skipping `printenv` and `cat *.env*` is correct, because they are unsafe if the deny is broken.
Fix: Probe the ssh read once with each tool, as two named entries. Have the report state "N of M entries probed; others not run".

## F11 — non-blocking
Claim: The report's `agents` and `tree unchanged` lines use dispatchable/not dispatchable and yes/no instead of #439's passed, failed or not run.
Classification: suggestion
Location: process/probe.md:80, 87
Evidence: Verified by reading the #439 acceptance criteria and the report template.
Consequence: The vocabulary is inconsistent across a record meant to be parsed and cited.
Fix: Add `agents: passed | failed | not run` above the per-agent lines, and make the last line `tree unchanged: passed | failed`.

## F12 — non-blocking
Claim: The report requires the harness version, but the procedure does not say what to record when `claude --version` or `codex --version` cannot be run from inside the session.
Classification: suggestion
Location: process/probe.md:23-24, 96, 108
Evidence: Inferred. Whether the CLI is on PATH inside a Codex or cloud session is unknown.
Consequence: The runner may guess a version.
Fix: Have the runner record `harness: <name> unknown - <quoted error>` and ask the human for the version shown in the UI.

## O1 — observation
Claim: The per-harness paths match the emitters and the emitted trees: `CLAUDE.md`, `.claude/rules/`, `.claude/skills/<stem>/`, `.claude/agents/<role>.md`, `.claude/settings.json` hooks and deny, `.claude/hooks/`; `AGENTS.md`, `.agents/skills/<stem>/`, `.codex/agents/<role>.toml`, `.codex/hooks.json` with `deny` mode on matcher `.*` covering only `Read|Bash`.
Location: process/probe.md:94-119
Evidence: Verified by reading `claude_code.py:18-34`, `codex.py:1-15, 270-375` and `codex-hook:113-143`, and by listing `.claude/`, `.codex/` and `.agents/`. The `AGENTS.override.md` note matches the emitter's documented interface (inferred, not observed live).
Consequence: None.
Fix: None.

## O2 — observation
Claim: The role choice is sound. Chief-of-staff is the role of the main session that runs the probe. Every process document except `project-setup` and `named-queries` is emitted as a skill whatever its role frontmatter says, so adopted repositories receive `probe` through both emitters. `adopt.md` sets the same precedent: it is chief-of-staff only and is not listed in `named-queries.md`.
Location: process/probe.md:1-7; bin/rulestore/emit/common.py:24, 180-183
Evidence: Verified by running the emit and by reading.
Consequence: None. The tests are meaningful as emission tests, since they fail without the document. Their remaining assertions only confirm that source strings pass through.
Fix: None.

## O3 — observation
Claim: The Codex deny adapter passes a shell command given in list form (`["bash","-lc","kubectl apply --help"]`). If Codex sends commands that way, the probe will report the deny entries as failed. That would be a correct result about the adapter, not a probe defect. Separately, whether Codex reports edits under a name that the `Edit|Write` matcher sees is for the first run to show.
Location: .codex/hooks/codex-hook:113-128 (outside the delta)
Evidence: Verified by running. The list-form payload exited 0 with no refusal, and the string form exited 2 with `denied by Bash(kubectl apply*)`.
Consequence: The first Codex probe may expose an adapter gap.
Fix: None in this delta. Check against the first Codex probe report.
