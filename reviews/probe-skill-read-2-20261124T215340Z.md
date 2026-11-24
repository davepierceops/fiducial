# Review: intake/probe-skill — read-2-20261124T215340Z

Verdict: changes-required
Reviewed: intake/probe-skill @ 8e86f03
Baseline: intake/probe-skill @ f79f348
Reviewer: context-quality-reviewer (subagent; did not author the delta or the amendment)
Date: 2026-11-24
Scope: `git diff f79f348..8e86f03` (`process/probe.md`, `process/release.md`, `process/adopt.md`), checked against findings F1–F12 of `reviews/probe-skill-read-20261124T190213Z.md`, DEC-001940, DEC-001950 and DEC-001960, and #439 as the first read quotes it.
Cross-checked: `.claude/settings.json`; `.codex/hooks.json`; `.codex/hooks/codex-hook`; `.claude/hooks/{push-readback,review-artifact-immutable,intake-branch-guard,decision-log-append-only,_hooklib.py}`; `.gitignore`; `CLAUDE.md` head and tail; a fresh `bin/bundle --emit claude-code` and `--emit codex` into a temp directory; the hooks run against payloads in two scratch clones under `/tmp`.
Not inspected: live harness behaviour of any kind. No Claude Code or Codex session was started, so `/probe`, `$probe`, Codex skill listing and agent dispatch, `claude --version` and `codex --version`, Claude Code's deny wording, and its matching of `Bash(kubectl apply*)` against `kubectl apply --help` stay unknown. The #439 body was not re-fetched; the first read's quotation of it was relied on. Whether adopted repositories such as crow ignore `__pycache__/` was not checked (no adopted repository is in this session). Whether the author invoked the command-blocks skill for the start pastes cannot be seen in the diff.
Findings: 1 blocking, 5 non-blocking
The human should inspect: N1 (a new false failure in the clean-tree check) and N2 (whether a pre-existing hook byproduct that can stop the probe at step 1 belongs in this change or in a follow-up issue).

## Verdict (quality): changes-required

`bin/tests/run`: 464 tests, OK (verified by running at 8e86f03; the working tree was clean afterwards). The emitter writes `.claude/skills/probe/SKILL.md` and `.agents/skills/probe/SKILL.md` with the amended text and identical bodies (verified by running a fresh emit and diffing the bodies).

Disposition of the first read's findings (verified by reading the amended `process/probe.md` at 8e86f03, plus running where stated):

- F1 resolved, at probe.md:29-32 and 58-65. Step 1 records the literal `mktemp -d` path and forbids variables. The plain push and the force push are separate tool calls. Verified by running: in a scratch clone, given `git push /tmp/tmp.1IA5oPjqKO/remote.git HEAD:refs/heads/probe` with that literal path, `push-readback` printed `push-readback: /tmp/tmp.1IA5oPjqKO/remote.git/probe is at 8e86f033…` and exited 0. `git for-each-ref` and `git config --local --list | sha256sum` were the same before and after.
- F2 resolved, at probe.md:33-38. The check now rests on the first and last instruction sentences, and the marker is reported separately. Verified by running a grep: the first sentence appears nowhere under `.claude/`, so a session that did not load `CLAUDE.md` cannot pass by drawing on another emitted file.
- F3 resolved, at probe.md:52, 65 and 77-80. A pass needs output that names the deny entry or the hook. Prompts, sandbox refusals and approval refusals are not run, and "command not found" is failed. The wording of Claude Code's deny message is still unknown, and probe.md:137-138 labels it inferred.
- F4 resolved, at probe.md:120-125 and 142-147. `/probe` and `$probe` are each labelled as inferred, not observed.
- F5 resolved, at probe.md:43-49, 130-132 and 156-158. A reply made in the main session is failed. Codex dispatch is labelled unverified, and step 4 is not run when no dispatch tool exists. `/agents` is marked as run by the human. See N4 for the Claude Code mechanism.
- F6 resolved, at release.md:47 and adopt.md:81. Both now require the citation, or a statement that no probe was run. See N3 for scoping.
- F7 resolved, at probe.md:69-72. Verified by running: `git ls-tree --name-only origin/main reviews/` lists blobs (417, no subtrees). `review-artifact-immutable` refused the first of them, `reviews/LEXICON-cycle-1.md`, with exit 2 naming R1408. It allowed the branch-only `reviews/probe-skill-read-20261124T190213Z.md` with exit 0, which is the false failure the fix removes.
- F8 resolved, at probe.md:50-52 and 135. Verified by running: `intake-branch-guard` refused a Write of `process/probe-throwaway.txt` on a non-intake branch, and `decision-log-append-only` refused a Write that retitled the first entry. Both exited 2 naming the rule.
- F9 is partly resolved, at probe.md:27-28 and 84-87, and the amendment introduces N1 here.
- F10 resolved, at probe.md:75-82 and 110-111.
- F11 resolved, at probe.md:103-104 and 112.
- F12 resolved, at probe.md:24-26, 95 and 149-150.

DEC-001940 trace of the amendment (verified by reading and by the scratch-clone runs). No new step names `origin`, adds a remote or commits. The additions to steps 1 and 7 only read. `git config --local --list` is piped through `sha256sum`, so a credential in a remote URL does not enter context. The push read-back's fetch writes `FETCH_HEAD` and objects, not refs (`for-each-ref` was unchanged). The amendment adds no new false pass. It adds one new false failure (N1).

O3, the Codex list form (verified by running every probe command through the `.*` PreToolUse deny hooks of `.codex/hooks.json`). As a string under `Bash`, `exec_command` and `shell`, `kubectl apply --help`, `terraform apply -help`, `cat ~/.ssh/probe-does-not-exist` and `git push --force <literal tmp>/remote.git HEAD:refs/heads/probe` each exited 2 with `codex-hook: denied by <entry>`. `Read` and `read_file` of `~/.ssh/probe-does-not-exist` exited 2 with `denied by Read(~/.ssh/**)`. Each command in list form (`["bash","-lc",…]`) exited 0: the adapter joins the list into `bash -lc kubectl …`, which no entry's glob matches from the start. The probe would surface this honestly. The command runs, so the result is either execution or not-found, and probe.md:73 and 80-81 make both failed. The quoted output is the evidence, and probe.md:165-167 names the cause. If the force push slips through in list form, it lands only in the throwaway bare remote, as DEC-001940 requires. The adapter gap itself remains, outside this delta.

## N1 — blocking
Claim: Step 7 compares `git status --porcelain --ignored` with step 1, but step 1 never records that output. The hooks themselves create `.claude/hooks/__pycache__/`, so the clean-tree check reports failed in a run where nothing was left behind, or else the runner has to improvise the comparison.
Classification: defect
Location: process/probe.md:26-28, 84-88
Evidence: Verified by reading: step 1 lists `git status --porcelain`, `git for-each-ref` and `git config --local --list | sha256sum`. `--ignored` appears only in step 7. Verified by running in a fresh clone: `.claude/hooks/__pycache__` was absent. One `push-readback` invocation on a non-push payload (`claude --version`) then created it, and `git status --porcelain --ignored` showed `!! .claude/hooks/__pycache__/`. `push-readback` imports `_hooklib` at module load, before it checks for a push, and it is the `PostToolUse` hook on every Bash call (`.claude/settings.json`). `codex-hook` runs the same scripts under `sys.executable`, so the same is inferred for Codex.
Consequence: In a probe run from a fresh clone, `tree unchanged: failed` is reported for a byproduct of the hooks working. Alternatively, with no baseline to compare against, the `--ignored` check means nothing.
Fix: Record `git status --porcelain --ignored` in step 1. In step 7, report a new `__pycache__/` under `.claude/hooks/` or `.codex/hooks/` as a known hook byproduct, quoted in the evidence and not counted as failed. Any other new ignored path is failed.
Related: N2

## N2 — non-blocking
Claim: In an adopted repository that does not ignore `__pycache__/`, the probe stops at step 1. Any earlier Bash call in the session, `claude --version` included, makes the `PostToolUse` hook write `.claude/hooks/__pycache__/`, so the required-empty `git status --porcelain` is not empty. This predates the amendment.
Classification: defect
Location: process/probe.md:22-28 (step 1, unchanged in substance); `.claude/hooks/push-readback` (outside the delta)
Evidence: The byproduct was verified by running, as in N1. This repository ignores it (`.gitignore`: `__pycache__/`). Nothing found in `bin/rulestore/emit/` or `process/adopt.md` writes an ignore entry for adopted repositories (verified by grep). Whether crow ignores it is unknown.
Consequence: The probe stops and says why. That outcome is honest, but it blocks every check in such a repository, and the cause is the hooks, not the repository.
Fix: Outside this delta: have the hooks set `sys.dont_write_bytecode` before importing `_hooklib`, or have the adopter emit the ignore entry. Record it as a follow-up issue. In this delta, step 1 could exempt that path, as N1's fix does.
Related: N1

## N3 — non-blocking
Claim: The new citation lines say "the latest probe report under fiducial `adoptions/`" without scoping it to the repository and harness. In `release.md`, the requirement is added after "otherwise N/A", which leaves unclear whether a release with no live verification must cite one.
Classification: suggestion
Location: process/release.md:47; process/adopt.md:81
Evidence: Verified by reading. DEC-001950 names the report `probe-<repo>-<harness>-<UTC timestamp>.md`, so there is one report per repository and harness. probe.md:15-17 says a probe goes stale when the hooks, adopter or emitted context change.
Consequence: A record can cite another repository's report, or only one harness's report, or a stale one, as evidence of live verification.
Fix: Say "cite the latest probe report for this repository and each harness under fiducial `adoptions/`, with its emitted SHA, or state that none was run", and in `release.md` put the citation outside the N/A clause.

## N4 — non-blocking
Claim: The Claude Code dispatch mechanism, "the subagent (Task) tool", is stated as fact although it is unverified. Step 4 also does not require the dispatch output to show the emitted agent's name, so a generic subagent told to role-play could pass.
Classification: defect
Location: process/probe.md:43-47, 130-132
Evidence: Verified by reading. The Codex mechanisms are labelled unverified and this one is not. Inferred: the tool's name has varied across Claude Code versions. The "reply with your role name" task can be satisfied by any subagent whose prompt names the role. The role-play gap was in the original step 4 too.
Consequence: The step can report `agent <role>: passed` without showing that `.claude/agents/<role>.md` loaded.
Fix: Label the Claude Code mechanism as inferred until the first run observes it. Count an agent as passed only when the quoted dispatch output names the emitted agent type, and the reply comes from that dispatch.

## N5 — non-blocking
Claim: Step 7's `test -e` checks only `process/probe-throwaway.txt`, but step 5 allows the `rules` directory as a fallback, so in that case a leftover throwaway goes unchecked.
Classification: defect
Location: process/probe.md:66-68, 86-87
Evidence: Verified by reading.
Consequence: In a repository with `rules/` and no `process/`, `tree unchanged` rests on `git status` alone for that path. That misses the file if `rules/` is ignored.
Fix: Check with `test -e` the path the step-5 probe actually used.

## N6 — non-blocking
Claim: Step 7 says "Remove the temporary directory" without saying how, and in Claude Code the obvious `rm -rf <tmp>` is refused by the `Bash(rm -rf *)` deny entry.
Classification: suggestion
Location: process/probe.md:88; `.claude/settings.json` `permissions.deny`
Evidence: Verified by reading the deny list. Claude Code's matching of that entry is inferred.
Consequence: The temp directory and bare remote stay behind in `/tmp`, outside the tree, or the runner improvises. Neither changes the result.
Fix: Name a command that is not denied (for example `rm -r <tmp>`), or say that a leftover temp directory outside the repository is acceptable and should be reported.
