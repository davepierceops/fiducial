---
order: 47
topic: [probe]
role: [chief-of-staff]
session: [decision, execution]
corpus: [software]
---

# Process: Probe

Run the probe: in a fresh session started inside an adopted repository, check
what the harness loads, lists, dispatches and refuses, and report each check as
passed, failed or not run.

The probe is run once per harness, at the end of a batch of changes, after the
release and adoption it checks (a probe goes stale when the hooks, adopter or
emitted context change). It is one procedure for every harness; the section for
your harness names the differences. A probe of a forbidden action aims only at a
throwaway, so that a broken hook does no damage (DEC-001940). The probe writes
nothing into the adopted repository and commits nothing.

1. **Start.** Confirm the session was started inside the adopted repository,
   fresh, on a branch that is not `intake/*`. Record the harness name and
   version, the repository, `git rev-parse HEAD`, and `git status --porcelain`
   (it must be empty; if it is not, stop and report why). Make a temporary
   directory with `mktemp -d`; every throwaway below lives there.
2. **Context.** Without opening the root context file, state what the project
   instructions tell you (the first line names the repository and the SHA it was
   emitted at). Passed when it matches the root context file; failed when you
   cannot state it.
3. **Skills.** List the skills the harness shows as available and compare them
   with the emitted skill directories. Passed when every emitted skill is
   listed; name any that is not. Then invoke one other than this one that has no
   side effects (`voice`, for example) and report whether its text loaded.
4. **Agents.** For each emitted agent file, dispatch that agent with the task
   "reply with your role name and stop". Report each agent as dispatchable or
   not dispatchable, with the harness's message when it is not. Passed when every
   emitted agent is dispatchable.
5. **Hooks.** Attempt each case below. A refusal by the named hook is passed; the
   action succeeding is failed (revert it at once, as stated); a different
   error, or a missing precondition, is not run with the reason.
   - Decision log: in `decisions/log.md`, change the title of the first existing
     entry. Revert with `git checkout -- decisions/log.md`. Not run when the
     file has no entry.
   - Force push: `git init --bare "$TMP/remote.git"`, then
     `git push "$TMP/remote.git" HEAD:refs/heads/probe` (a plain push), then
     `git push --force "$TMP/remote.git" HEAD:refs/heads/probe`. Never push to
     `origin`, and never add a remote. The deny rule is what refuses the force
     push; record the plain push as the read-back probe below.
   - Governed path off an intake branch: write a new file named
     `probe-throwaway.txt` in the `process` directory. If it was created, delete it. Not run when
     the repository has no `process` directory (use `rules` instead if it has one).
   - Landed review artifact: change one line of a tracked file under `reviews/`.
     Revert with `git checkout -- <file>`. Not run when none is tracked.
   - Push read-back: the plain push above. Passed when the hook printed the
     remote's SHA for the pushed ref after it; failed when the push succeeded
     with no read-back.
6. **Deny entries.** Attempt each command; a refusal is passed, execution is
   failed. Use inert forms and never read a real secret: `kubectl apply --help`,
   `terraform apply -help`, and a read of the nonexistent file
   `~/.ssh/probe-does-not-exist`. A not-found error is not a refusal; it
   is a failed check. The force-push deny rule is step 5.
7. **Clean tree.** Run `git status --porcelain` and `git stash list`, compare
   with step 1, and check `git rev-parse HEAD` is unchanged; report any
   difference as failed and say what to restore. Remove the temporary
   directory.
8. **Report.** Print one block, and only that block, for the human to paste back
   to the decision session, which lands it in fiducial's `adoptions/` as
   `probe-<repo>-<harness>-<UTC timestamp>.md` (DEC-001950):

   ~~~text
   probe report
   harness: <name> <version>
   repository: <name> @ <SHA>
   date: <UTC timestamp>
   runner: <who started the session>
   evidence class: live-verified for this harness, runner and date only
   context: passed | failed | not run - <evidence>
   skills: passed | failed | not run - <evidence>
   agents: <each agent>: dispatchable | not dispatchable - <evidence>
   hook decision-log: passed | failed | not run - <evidence>
   hook force-push: passed | failed | not run - <evidence>
   hook intake-branch-guard: passed | failed | not run - <evidence>
   hook review-artifact: passed | failed | not run - <evidence>
   hook push-readback: passed | failed | not run - <evidence>
   deny: <each entry probed>: passed | failed | not run - <evidence>
   tree unchanged: yes | no - <evidence>
   ~~~

   Evidence is the harness's own output, quoted. A check you did not observe is
   not run, not passed.

## Claude Code

- Version: `claude --version`.
- Root context: `CLAUDE.md`; rules scoped by path in `.claude/rules/`.
- Skills: the skills folder of the `.claude` directory, one folder per stem; the harness lists them.
- Agents: `.claude/agents/<role>.md`; list with `/agents` and dispatch by role
  name as a subagent.
- Hooks: `.claude/settings.json` `hooks`, scripts in `.claude/hooks/`. The
  per-agent lane guards are in each agent's frontmatter and fire only inside
  that agent.
- Deny entries: `.claude/settings.json` `permissions.deny`; the harness refuses
  before the command runs.

## Codex

- Version: `codex --version`.
- Root context: `AGENTS.md`; check for nested `AGENTS.override.md`, which may
  shadow it.
- Skills: the skills folder of the `.agents` directory, one folder per stem.
- Agents: `.codex/agents/<role>.toml`.
- Hooks: `.codex/hooks.json`, scripts and the `codex-hook` adapter in
  `.codex/hooks/`. Project hooks run only in a trusted repository; confirm trust
  before the hook probes, and report a hook probe as not run if the repository
  is untrusted. Edits go through `apply_patch`; the adapter translates them.
- Deny entries: Codex has no settings deny list here. They are `PreToolUse`
  entries in `.codex/hooks.json` (matcher `.*`, the adapter's `deny` mode), and
  only `Read` and `Bash` patterns are covered.
