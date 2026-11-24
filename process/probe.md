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
   version (when the version command cannot be run in the session, record
   `harness: <name> unknown - <quoted error>` and ask the human for the version
   the UI shows; never guess one), the repository, `git rev-parse HEAD`,
   `git status --porcelain` (it must be empty; if it is not, stop and report
   why; a `.claude/hooks/__pycache__/` or `.codex/hooks/__pycache__/` entry is
   a known byproduct of the hooks, quoted in the report and not a reason to
   stop), `git status --porcelain --ignored` (the ignored-path baseline for
   step 7), `git for-each-ref`, and `git config --local --list | sha256sum`. Make
   a temporary directory with `mktemp -d` and record the absolute path it
   printed. Write that literal path in every later command, never a shell
   variable: a variable does not carry across tool calls, and the hooks read the
   command text without expanding it. Every throwaway lives there.
2. **Context.** Without opening the root context file, state the first and the
   last instruction sentence of the project instructions you were given, then
   open the root context file and compare. Passed when both match; failed when
   you cannot state them. Report the repository and SHA marker comment only if
   the session showed it to you, separately from the result: some surfaces hide
   comments.
3. **Skills.** List the skills the harness shows as available and compare them
   with the emitted skill directories. Passed when every emitted skill is
   listed; name any that is not. Then invoke one other than this one that has no
   side effects (`voice`, for example) and report whether its text loaded.
4. **Agents.** For each emitted agent file, dispatch that agent as a subagent
   with the task "reply with your role name and stop", using the harness's
   dispatch mechanism named in its section. Passed when every emitted agent was
   dispatched and replied; the reply must come from the dispatched subagent,
   quoted together with the harness's dispatch output. A reply produced in the
   main session is failed. Where the harness has no dispatch tool, or its
   mechanism is unverified and you cannot find it, the step is not run.
5. **Hooks.** Make every edit below through the harness's file-edit tool (Edit or
   Write in Claude Code, `apply_patch` in Codex): the hooks do not see edits
   made through the shell. A refusal naming the hook is passed; the action
   succeeding is failed (revert it at once, as stated); a different error, or a
   missing precondition, is not run with the reason.
   - Decision log: in `decisions/log.md`, change the title of the first existing
     entry. Revert with `git checkout -- decisions/log.md`. Not run when the
     file has no entry.
   - Push read-back: run `git init --bare <tmp>/remote.git`, then, as its own
     tool call, `git push <tmp>/remote.git HEAD:refs/heads/probe` (a plain
     push). Never push to `origin`, and never add a remote. Passed when the hook
     printed the remote's SHA for the pushed ref after it; failed when the push
     succeeded with no read-back.
   - Force push: as a separate tool call from the plain push,
     `git push --force <tmp>/remote.git HEAD:refs/heads/probe`. The deny rule
     is what refuses it; apply step 6's rule for what counts as a refusal.
   - Governed path off an intake branch: write a new file named
     `probe-throwaway.txt` in the `process` directory. If it was created, delete it. Not run when
     the repository has no `process` directory (use `rules` instead if it has one).
   - Landed review artifact: pick a file from
     `git ls-tree --name-only origin/main reviews/` (fall back to `main`), the
     hook refuses only landed files, and change one line of it. Revert with
     `git checkout -- <file>`. Not run when neither lists a file.
6. **Deny entries.** Attempt each command; execution is failed. Use inert forms
   and never read a real secret: `kubectl apply --help`, `terraform apply -help`,
   and a read of the nonexistent file `~/.ssh/probe-does-not-exist`, made once
   with the file-read tool and once through the shell (two named entries).
   Passed only when the quoted output names the deny entry or the harness's
   deny-by-settings message. Any other refusal (a permission prompt the human
   declined, a sandbox denial, an approval refusal) is not run, with the quote.
   A not-found error, including "command not found" for `kubectl` or
   `terraform`, is failed. State "N of M entries probed; others not run", M being
   the number of deny entries the harness's file lists. The force-push deny rule
   is step 5.
7. **Clean tree.** Run `git status --porcelain`, `git status --porcelain --ignored`,
   `git stash list`, `git for-each-ref` and `git config --local --list | sha256sum`,
   compare with step 1, check `git rev-parse HEAD` is unchanged, and check with
   `test -e` that the path step 5 used for the governed-path probe
   (`process/probe-throwaway.txt`, or the `rules` one) is absent. A new
   `__pycache__/` under `.claude/hooks/` or `.codex/hooks/` is a known hook
   byproduct: quote it in the evidence and do not count it as failed. Any other
   new ignored path, and any other difference, is failed; say what to restore.
   Do not remove the temporary directory with `rm -rf` (Claude Code denies it);
   report its path and the bare remote in it as left over outside the
   repository, which is acceptable.
8. **Report.** Print one block, and only that block, for the human to paste back
   to the decision session, which lands it in fiducial's `adoptions/` as
   `probe-<repo>-<harness>-<UTC timestamp>.md` (DEC-001950):

   ~~~text
   probe report
   harness: <name> <version> | <name> unknown - <quoted error>
   repository: <name> @ <SHA>
   date: <UTC timestamp>
   runner: <who started the session>
   evidence class: live-verified for this harness, runner and date only
   context: passed | failed | not run - <evidence>
   context marker: <SHA seen> | not shown to the session
   skills: passed | failed | not run - <evidence>
   agents: passed | failed | not run - <evidence>
   agent <each>: passed | failed | not run - <evidence>
   hook decision-log: passed | failed | not run - <evidence>
   hook force-push: passed | failed | not run - <evidence>
   hook intake-branch-guard: passed | failed | not run - <evidence>
   hook review-artifact: passed | failed | not run - <evidence>
   hook push-readback: passed | failed | not run - <evidence>
   deny: N of M entries probed; others not run
   deny <each entry probed>: passed | failed | not run - <evidence>
   tree unchanged: passed | failed - <evidence>
   ~~~

   Evidence is the harness's own output, quoted. A check you did not observe is
   not run, not passed.

## Claude Code

Start paste (the invocation form is inferred, not yet observed for this skill;
the first run confirms it):

~~~text
/probe
~~~

- Version: `claude --version`.
- Root context: `CLAUDE.md`; rules scoped by path in `.claude/rules/`.
- Skills: the skills folder of the `.claude` directory, one folder per stem; the harness lists them.
- Agents: `.claude/agents/<role>.md`; dispatch each by role name through the
  harness's subagent tool (inferred to be the Task tool; unverified until the
  first run observes it). Count an agent as passed only when the quoted
  dispatch output names the emitted agent type and the reply comes from that
  dispatch. The `/agents` command is run by the human, not the
  model, and step 4 does not need it.
- Hooks: `.claude/settings.json` `hooks`, scripts in `.claude/hooks/`. The
  per-agent lane guards are in each agent's frontmatter and fire only inside
  that agent. The edit matcher is `Edit|Write`.
- Deny entries: `.claude/settings.json` `permissions.deny`; the harness refuses
  before the command runs. How it words a deny and whether `Bash(kubectl apply*)`
  matches `kubectl apply --help` are inferred, not observed.

## Codex

Start paste (the invocation form is inferred from the `$<stem>` references the
emitter writes, not observed; the first run confirms it):

~~~text
$probe
~~~

- Version: `codex --version`; it may not be on the PATH inside the session, so
  apply step 1's unknown rule.
- Root context: `AGENTS.md`; check for nested `AGENTS.override.md`, which may
  shadow it.
- Skills: the skills folder of the `.agents` directory, one folder per stem.
  How Codex lists them is unverified here; use the harness's own skill listing
  if it has one, else report step 3's listing as not run.
- Agents: `.codex/agents/<role>.toml`. How Codex dispatches them is unverified
  here; step 4 is not run unless the session has a dispatch tool, and the
  report names the tool used.
- Hooks: `.codex/hooks.json`, scripts and the `codex-hook` adapter in
  `.codex/hooks/`. Project hooks run only in a trusted repository; confirm trust
  before the hook probes, and report a hook probe as not run if the repository
  is untrusted. Edits go through `apply_patch`; the adapter translates them.
- Deny entries: Codex has no settings deny list here. They are `PreToolUse`
  entries in `.codex/hooks.json` (matcher `.*`, the adapter's `deny` mode), and
  only `Read` and `Bash` patterns are covered. The adapter's refusal reads
  `codex-hook: denied by <entry>`; a shell command sent in list form may pass
  the adapter, and the probe then correctly reports failed.
