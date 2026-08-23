---
status: draft
audience: [human, chief-of-staff]
---

# Research: remote-write friction on the agent write path

Directive: `docs/cycles/gh-write-friction-research-20260823T184149Z.md` @ `e63098c`.
Research and analysis only. No governed document was edited.

Claim classes are marked inline: **[obs]** observed in this repository or this
session, **[inf]** reasoned to, **[told]** carried from the directive or a
committed artifact without independent check, **[unk]** not determinable from
this session.

---

## 1. Report, up front

**Ranked shortlist**

1. **Standing write-path document** — one governed file holding the whole write path; directives cite it by path and SHA instead of restating it. Removes the drift and refusal surface at near-zero cost; is a precondition for every other option being citable rather than re-narrated.
2. **`bin/land`** — a tested script wrapping branch/commit/push/verify, including content verification, not landing verification. Encapsulates the mechanics the standing document would otherwise have to describe; closes the remote-write policy's named open gap.
3. **Do less: batch landings, fewer branches** — cuts the number of times the path is walked at all. Free, immediately available, but caps out; does not make any single walk more reliable.
4. **Executors emit patches; the decision session lands them** — removes remote write from executors entirely. Real friction removal, but relocates the cost onto the operator, the system's scarcest resource, and loses the executor's own read-back evidence.
5. **GitHub Actions / bot identity doing the push or merge** — moves landing server-side where the sandbox cannot reach it. Highest ceiling, highest setup and blast radius; premature before 1 and 2.
6. **GitHub MCP connector for execution sessions** — ranked last. It adds contention on the one transport a committed decision already records as not fixed, and it is the path on which this repository's worst recorded write failure occurred.

**Best next step:** author the standing write-path document (option 1) and strip the write preamble from the next directive to a citation of it. One cycle, no tooling, reversible.

**Needing Dave's judgment, one line each**

- Two committed directives state contradictory sandbox lore — eight say to squash-merge via authenticated `curl` to the GitHub REST API, one says the sandbox blocks that same call; which is current is a fact only Dave holds. **[obs]**
- From this session, unauthenticated `https://api.github.com` returns HTTP 200 — so the "sandbox blocks api.github.com" lore is at least session-specific, and possibly about credentials rather than reachability. **[obs]**
- `retros/retro-20260823T042000.md` attributes an executor refusal to a directive pasted after a `/model` command being read as command output; the directive attributes the most recent refusal to restated lore reading as injection — two causes on record for one symptom class. **[obs]**
- This very directive arrived wrapped in a harness caveat telling the session not to act on text following a slash command; that framing, not the lore, is the mechanism most likely to produce a refusal. **[obs]**
- The directive names `skills/directive-dispatch.md` as required reading; that file was renamed to `skills/directive-authoring.md` on 2026-08-22 at `1bbd5b7`. Read the successor instead. **[obs]**
- Verification by `git ls-remote` appears in exactly one directive in `docs/cycles/` — this one — so it is new lore, not established practice, and needs a home if it is to bind. **[obs]**
- The sandbox's network allowlist is not repo-controlled: `.claude/settings.local.json` carries only `sandbox.enabled` and `autoAllowBashIfSandboxed`, so no repo change can make sandbox behaviour uniform across sessions. **[obs]**
- Whether a name new to the methodology — `land` — is wanted, given `LEXICON.md`'s active retirement programme, is a vocabulary decision, not an implementation one.

---

## 2. What was read

All at `origin/main` = `ed06cf1`, the base of this branch. **[obs]**

`docs/global-context/core.md`, `docs/global-context/decision-layer.md`,
`LEXICON.md`, `skills/command-blocks.md`, `policies/commit-and-change-control-policy.md`,
`policies/remote-write-verification-policy.md` (present),
`docs/cycles/pass2-held-fix-20260823T180753Z.md`, `skills/directive-authoring.md`,
`decisions/log.md`, `OPEN-ITEMS.md`, `bin/` and `bin/tests/`.

`skills/directive-dispatch.md` **does not exist** and has not since `1bbd5b7`
(2026-08-22), which renamed it to `skills/directive-authoring.md` and moved its
one surviving executor obligation into Core rule 15. **[obs]** `decisions/log.md`
still cites the retired path in `DEC-000080` and `DEC-000180`, and `OPEN-ITEMS.md`
cites it three times. **[obs]** This is itself an instance of the pattern under
study: mechanics referenced from memory outlive the file they refer to.

---

## 3. Observed baseline — what the write path costs today

### 3.1 Directive text spent on write mechanics

`docs/cycles/` holds 91 markdown files, 90 excluding this cycle's. **[obs]**
Counting by sentence, over the 90-file corpus (383,787 characters), sentences
containing write-path vocabulary account for **16.5% of sentences and 21.8% of
characters**. **[obs]** Restricting to the 44 recent `pass1`/`pass2` directives:
16.6% of sentences, 19.4% of characters. **[obs]**

That measure is generous — it catches "branch" in its spec sense. The narrow
measure is sharper. Sentences carrying *sandbox lore specifically* (`gh`, `curl`,
keychain, sandbox, `ls-remote`, `checkout origin/main`, do-not-merge, connector)
are **2,716 characters, 0.7% of the corpus — but they appear in 35 of 90
directives (39%)**. **[obs]**

The concentration matters more than the total. In the six `pass2` directives the
same block of four to five sentences opens every one, and write mechanics run
**13.9% to 43.3% of each file**: **[obs]**

| directive | write-mechanic sentences | share of text |
|---|---|---|
| `pass2-confirm-20260823T173321Z.md` | 10 of 33 | 43.3% |
| `pass2-flips-20260823T155912Z.md` | 7 of 26 | 31.9% |
| `pass2-holdout-fix-2-20260823T171849Z.md` | 7 of 28 | 29.3% |
| `pass2-held-fix-20260823T180753Z.md` | 8 of 25 | 27.1% |
| `pass2-holdout-regate-20260823T160907Z.md` | 6 of 25 | 26.1% |
| `pass2-holdout-fix-20260823T164555Z.md` | 5 of 37 | 13.9% |

Phrase counts across `docs/cycles/`, excluding this cycle's file: "Never invoke
gh" in 6 directives, `git checkout origin/main` in 9, "do not merge" in 23,
`ls-remote` in 0. **[obs]**

### 3.2 The restatements have already drifted

Eight committed directives instruct the executor to "open and squash-merge a PR
via curl against the GitHub REST API using the credential-helper token held in an
environment variable." One — `pass2-held-fix-20260823T180753Z.md`, the most
recent — instructs the opposite: "the sandbox blocks authenticated curl to
api.github.com; the decision session merges over its repository connector."
**[obs]** Both are committed. Neither supersedes the other in any governed
document. A future session reading `docs/cycles/` for precedent finds both.

`OPEN-ITEMS.md` predicted exactly this in 2026-08-02, in an entry still marked
open: "a per-dispatch restatement is an unversioned derived copy of governed
text, and derived copies written fresh drift." **[obs]** The entry names
`skills/directive-execution.md` as its proposed fix and records that branch
naming, the pre-PR test gate, and STOP semantics "still have no canonical home."
**[obs]**

### 3.3 What actually failed in this session

I walked the whole path. Results: **[obs]**

- `git fetch origin main` — succeeded. Emitted `fatal: failed to store: 100001`; the fetch updated `origin/main` from `a60b2e2` to `ed06cf1` regardless.
- `git checkout origin/main` then `git checkout -b gh-write-friction-research` — both succeeded, no error.
- `git commit` — succeeded.
- `git push -u origin gh-write-friction-research` — the push landed; `-u` failed with `could not lock config file .git/config: Operation not permitted`.
- `git ls-remote origin gh-write-friction-research` — returned `e63098c8…`, confirming the push landed. Also emitted the keychain line.
- `git config --local test.probe 1` — `Operation not permitted`. The config really is unwritable. **[obs]**
- Unauthenticated `curl https://api.github.com/rate_limit` — **HTTP 200 in 98ms**. `https://github.com` — HTTP 200. **[obs]**

Two things follow. First, **the mechanics did not fail; the noise did**. Every
operation that mattered succeeded, and the two error strings were an upstream-
config write and a keychain store, neither of which is the operation. **[inf]**
Second, **the lore is not uniformly true**. `api.github.com` is reachable
unauthenticated from here. Whether an *authenticated* call would succeed is
**[unk]** — I hold no credential and did not seek one. The distinction the lore
collapses — reachability versus credential — is the distinction that would tell
Dave which of the two contradictory directives is right.

The stated reason for `git checkout origin/main` followed by `git checkout -b` —
"sandbox config is unwritable; this form works where `git checkout -b` from a
stale tree does not" **[told]** — is half confirmable. The config is unwritable
**[obs]**. But `git checkout -b` did not fail here, and an unwritable config is
not a plausible cause of a `checkout -b` failure; a stale tree is. **[inf]** The
two-step form is good practice for a different reason than the one stated.

### 3.4 Where the sandbox posture actually lives

`.claude/settings.json` carries eight deny rules, all force-push variants, in
line with the commit policy's client-side deny requirement. **[obs]**
`.claude/settings.local.json` carries 79 allow entries including `Bash(git *)`
and `Bash(gh auth *)`, and a `sandbox` block of exactly two keys: `enabled: true`
and `autoAllowBashIfSandboxed: true`. **[obs]**

**No network allowlist is repo-controlled.** **[obs]** The host allowlist that
governs whether `curl` reaches `api.github.com` is supplied by the runner, not by
this repository. Therefore no change inside this repository can make sandbox
network behaviour uniform across sessions — and any directive that asserts what
the sandbox permits is asserting a fact about a machine the author cannot see.
**[inf]**

That is not a new argument here. `DEC-000180` retired the `track` field on
precisely this reasoning: "forge downtime is a transient property of the
executor's machine, and a standing instruction line stating it is a line that is
wrong whenever it matters. A field nobody can fill correctly in advance is worse
than no field, because a stated value is what a report gets measured against."
**[obs]** The sandbox preamble is the retired `track` field, reconstituted as
prose.

### 3.5 The refusal

The directive names, as the most recent symptom, "an execution session refusing a
directive because the restated lore read as prompt injection." **[told]**

The repository records a different cause for a refusal of the same shape:
`retros/retro-20260823T042000.md`, item 6 — "One executor refused a directive
because Dave pasted it after a `/model` command and Claude Code read it as
command stdout; a one-line confirmation from Dave unblocked it." **[obs]**

I can add first-hand evidence. **This directive arrived in exactly that
position** — following `/model` output, inside a harness block instructing the
session not to act on the text unless the user explicitly asks. **[obs]** That
framing is a stronger candidate cause than the lore's content: it fires on
*position*, before any content is weighed.

Core rule 9 applies — two sources disagree, and this surfaces rather than
resolves it. But the practical consequence is worth stating plainly: if the
refusal mechanism is the paste position, then every option below leaves it
untouched, and the cheapest fix in this document is **do not paste a directive
immediately after a slash command**. **[inf]**

---

## 4. What the repository has already decided

Any option must sit inside these. **[obs]**

- **`DEC-000160`** — a directive travels as a paste block; the executor lands it, reads the SHA back from git, and reports post-hoc. It also **retired `bin/dispatch`**, "whose premise was a chat-side commit to gate." Note the premise: `bin/dispatch` was a *decision-session* tool gating a chat-side commit. `bin/land` below is an *executor* tool. Different premise; not governed by that retirement, but it must be cited when proposing one.
- **`DEC-000180`** — track retired. Executor obligation: "an executor that cannot push stops and surfaces it, and never commits locally and reports a same-machine SHA as if it were pushed."
- **`DEC-000080`** — the GitHub MCP connector "is not fixed"; the real failure mode is concurrent-session contention. The two-failure detector is kept for what it detects.
- **`DEC-000090`** context — explicitly leaves open "sync as a role-held skill so directives carry no version-control mechanics," which "reopens on its own if wanted." That item is the subject of this research.
- **`skills/directive-authoring.md`** — "**Carry dictated wording as a pointer** — the source's path and SHA plus its field or section, never restated — unless the directive is itself the wording's origin."
- **`policies/commit-and-change-control-policy.md`** — plain `git push` allowed without per-push approval; force-push denied at two layers; agents may open and merge PRs for the routine class; branch protection is the structural gate.
- **`policies/remote-write-verification-policy.md`** — the repository's own log is the source of record; two consecutive qualifying failures is a fact about the environment; and a **named open gap**: "these rules verify that a write landed. They do not verify that what landed is what was intended."

The directive-authoring rule is the load-bearing one. **The methodology already
forbids restating the lore.** A pointer, though, needs a target, and today the
only target is another directive file — an artifact `DEC-000160` classifies as
transport, "whose value expires at execution," rather than record. **[inf]** The
lore is being carried on the wrong kind of artifact. That is the defect.

---

## 5. Approaches

Axes, for each: friction removed · friction remaining · failure modes · security
posture · maintenance cost · blast radius · fit with the evidence rules · what
happens to the sandbox lore.

### A. Standing write-path document

One governed file — `skills/directive-execution.md` is the name `OPEN-ITEMS.md`
already proposes — holding the whole executor write path: fetch, branch from
`origin/main`, commit, push, verify by reading state back, what to do when a push
appears to fail, when to stop and surface, and the report shape. Directives cite
it by path and SHA as a companion document and say nothing else about mechanics.

- **Friction removed.** The 13.9–43.3% of each recent directive spent on mechanics collapses to one citation. **[obs, projected]** Drift ends: one file, versioned, reviewable, with a supersession record. The eight-versus-one contradiction becomes impossible to author.
- **Friction remaining.** All of it, in the mechanical sense. The config is still unwritable, the keychain still noisy, `push -u` still fails. The document describes the path; it does not smooth it.
- **Failure modes.** The document goes stale against a changed environment — the same failure as the lore, but now with one place to fix and a review gate on the fix. A directive that needs a genuine exception must state it and risks contradicting the standing text; `skills/directive-authoring.md` already covers this ("no blanket constraint may contradict an explicit instruction in the same file").
- **Security posture.** Unchanged. No new credential, no new surface. It **reduces injection surface**: an executor asked to read a committed, `agreed` file behaves differently from one handed unsourced imperatives about credentials in a pasted block. **[inf]** This is the axis on which A beats every other option.
- **Maintenance cost.** One document through one review cycle. Lowest of any option here.
- **Blast radius when it breaks.** A stale sentence in one file, caught at the next cycle. No credential, no automation, nothing that can destroy content.
- **Evidence-rule fit.** Excellent, and it is where the remote-write policy's open gap can be given a rule: the document is the natural home for "verify content, not landing."
- **Sandbox lore: mostly deleted, remainder encapsulated as principle.** The environment-specific assertions ("the sandbox blocks X", "gh is unusable") should not survive at all — per `DEC-000180` they are unfillable in advance. What survives is transposed into executor-observable rules: *verify every push by reading remote state back; a transport error string is not evidence that the operation failed — check; if you cannot verify, stop and surface.* Those bind regardless of which sandbox the executor woke up in.

### B. `bin/land`

A tested repository script wrapping the path: fetch, branch, commit, push, verify.

- **Feasibility, checked.** `bin/` already holds seven executables, an `aimeta` package, and 13 test modules under `bin/tests/`. **[obs]** `bin/aimeta/repo.py` provides a `subprocess` git layer with `run`, `git`, `blob_at_rev`, `file_at_rev`, `last_commit_sha`. **[obs]** `bin/tests/helpers.py` provides `make_repo`, `commit`, `head_sha`, `porcelain`, `run_cli`. **[obs]** **No script in `bin/` performs any remote operation today** — grep for push/ls-remote/remote across `bin/` returns nothing. **[obs]** So the local half is reusable and the remote half is net-new. A bare repository as a `file://` origin makes the remote half testable offline. **[inf]**
- **Precedent.** `bin/flip-agreed` already implements the exact discipline wanted: "the tool proves its own claim twice: before committing, the staged body must equal the body at HEAD; after committing, the committed file must re-validate and HEAD must touch exactly one path." **[obs]** `bin/land` is that pattern extended across the remote boundary.
- **Friction removed.** Mechanics become implementation detail: the two-step checkout, `push` without `-u`, tolerating the keychain line, reading state back. A directive says `bin/land --branch <name> --message <m>` and the report shape is the tool's output. Non-determinism between sessions drops, because the tool does the same thing every time whatever the session's memory of the lore.
- **Friction remaining.** Environment variance still bites — a sandbox with no network at all still cannot push, and `bin/land` can only detect and stop. It cannot create credentials it does not have. Every directive still needs a branch name.
- **Failure modes.** The script becomes a second oral tradition if untested; the mitigation is that `bin/tests/` exists and is already a gate in directives ("run `bin/tests/run`"). **[obs]** A subtler mode: the script succeeds and the executor reports the script's exit code as the evidence — which the policy calls a claim, not evidence. The tool must therefore print the read-back state, not a success word.
- **Security posture.** No new credential. The script uses whatever the environment already gives `git`. It **shrinks** what the agent must be trusted with: the agent never composes a REST call, never touches a token, never chooses a merge method. Force-push stays impossible — the client deny rules already cover it and `bin/land` need never offer it. **[obs]**
- **Maintenance cost.** Moderate and ongoing: a script plus tests, and the tests are where the real cost sits. Justified only if the path is walked often — it is walked in every directive. **[inf]**
- **Blast radius.** Bounded by what git itself permits under branch protection. The worst case is a wrong branch name or an empty commit, both cheap. It cannot merge, cannot force, cannot delete.
- **Evidence-rule fit.** Best of any option, and the reason it ranks second rather than fourth: it is the only option that can *close* the remote-write policy's named gap. `bin/land` can verify the pushed tree's content — compare the blob SHA it intended against the blob SHA now at the remote ref — turning "verify content, not landing" from an aspiration into a tool contract. The 64KB-file-replaced-by-19-bytes incident is exactly what such a check catches. **[obs, from `OPEN-ITEMS.md`]**
- **Sandbox lore: encapsulated.** Every workaround becomes a line of Python with a comment and a test. Directives stop restating it; the standing document (A) points at the tool rather than describing the path by hand. Note the dependency: **B without A still needs a governed home** to explain when to invoke it and what its output means. A is the prerequisite; B is the payoff.

### C. Do less — batch landings, fewer branches

Fewer branches per cycle, several edits per landing, one push where there were four.

- **Friction removed.** Linear in the count. The `pass2` series ran six directives in about four hours, most creating two branches each. **[obs]** Halving branch count halves every mechanical failure opportunity and every restatement.
- **Friction remaining.** All per-walk friction. And batching trades against something real: `DEC-000170` establishes reconciliation as the gate that charges review once over an accumulated diff, so batching is already the methodology's stated direction for spec work — but a larger batch is a larger diff to review, and the operator is the reviewer. **[inf]**
- **Failure modes.** A failed landing loses more work. Concurrent-tree hazards grow with batch size, and the retro record already shows collisions from parallel sessions in one clone. **[obs, `retros/retro-20260823T003000.md`]**
- **Security posture.** Unchanged.
- **Maintenance cost.** Zero — it is a habit, not an artifact.
- **Blast radius.** None new.
- **Evidence-rule fit.** Neutral, mildly negative: coarser batches make it harder to attribute a defect to a change.
- **Sandbox lore: still required, unchanged, just recited less often.** This is why C is a ranked third rather than a rival to A: it reduces exposure without addressing the defect.

### D. Executors emit patches; the decision session lands

Executors work in a tree, produce a `git bundle` or `git format-patch` series, and stop. The decision session — which holds a working connector **[told]** — lands everything.

- **Friction removed.** Total, for the executor. No push, no credential, no sandbox network dependency, no lore. The executor's write path becomes local-only, which the sandbox already permits fully. **[obs]**
- **Friction remaining.** Relocated, not removed, and relocated onto the operator. `decision-layer.md` rule 8 says hand him the block, never the task — so every landing becomes a block Dave pastes. Six directives becomes six-plus landings in his lap. `DEC-000170`'s design test is explicit that "operator attention is the system's scarcest, non-parallelizable resource." **[obs]** D spends exactly that.
- **Failure modes.** A bundle is a file that can be lost, truncated, or mis-transferred between sessions — the same transport-integrity problem the paste rules exist to handle, in a bigger and less inspectable form. **[inf]** Multi-session pipelining stalls: executor two cannot branch from executor one's work until Dave lands it.
- **Security posture.** **Best of any option.** The executor is trusted with nothing remote at all. Zero credential exposure. The injection surface shrinks to whatever the decision session accepts.
- **Maintenance cost.** Low in artifacts, high in ceremony.
- **Blast radius.** Smallest. An executor that goes wrong cannot reach the remote.
- **Evidence-rule fit.** **Poor, and this is the disqualifier.** `policies/remote-write-verification-policy.md` rule 1 makes the repository's own log the authority on what landed, and `DEC-000180` obliges the executor never to report a local SHA as if it were pushed. Under D the executor *structurally cannot* verify its own work landed — it reports a SHA it made locally, and something else lands it. That is the anti-pattern the decision explicitly names. It could be repaired by having the executor `ls-remote` after Dave lands, but that reintroduces the remote read the option was meant to avoid. **[inf]**
- **Sandbox lore: deleted for executors, still required by the decision session.** The lore does not die; it moves to the party who already has it in chat, where it is unversioned again.

### E. Server-side landing — bot identity or GitHub Actions

Either a bot account with a fine-grained PAT or deploy key, or an Action that performs the push or merge on the agent's behalf when it sees a branch or a labelled PR.

- **Current state.** The repository has **no `.github/` directory and no workflows at all**. **[obs]** This is greenfield, not an extension.
- **Friction removed.** Potentially the most: the agent pushes to a branch (or does not push at all, if a bot pulls), and an Action handles PR opening, checks, and merge. It also puts `bin/tests/run` and `bin/check-frontmatter --all` — currently run by hand and reported by hand in every directive **[obs]** — behind a status check that cannot be forgotten or misreported.
- **Friction remaining.** The agent still has to get *something* to GitHub to trigger anything. If the sandbox has no network, an Action cannot help; if it has network, the plain `git push` that already works is most of what was needed. **[inf]** The lore about the push half survives either way.
- **Failure modes.** New and unfamiliar: workflow permissions, `GITHUB_TOKEN` scope, an Action that merges something it should not, a check that passes for the wrong reason. Debugging moves off the machine into logs the executor cannot read from a sandbox. Blast radius grows precisely because it works unattended.
- **Security posture.** The weakest of the six on credential exposure. A bot PAT or deploy key is a standing credential with write access to the default branch, held outside any session's sandbox — good, in that no agent ever sees it — but it must be scoped, rotated, and stored. An Action with `contents: write` that merges on a label makes **the label a write primitive**, which means an agent that can set labels can merge. Every option above requires trusting the agent with a push; this one requires trusting it with a merge, and `policies/commit-and-change-control-policy.md` reserves the release gate for the human. **[obs]** Automating the merge does not breach that policy — the policy already permits agents to merge routine-class PRs — but it removes the moment where a human might notice.
- **Maintenance cost.** Highest. Workflow YAML, a bot identity, secrets management, and a second place where the write path is defined.
- **Evidence-rule fit.** Mixed. A CI status check is genuinely better evidence than an agent's report of a local test run — it is reproducible and third-party. Against that, an Action's own success is once more a claim, and now one the executor cannot read back without network access it may not have.
- **Sandbox lore: partly deleted, partly still required.** The merge half dies. The push half survives, and now there is workflow lore alongside it.

### F. GitHub MCP connector for execution sessions

Give executors the connector the decision session uses, replacing git-over-shell for remote writes.

- **Friction removed.** The shell path's specific irritants — keychain noise, unwritable config, `push -u` — vanish, because git is not involved. Credentials are handled by the connector, so no agent composes an authenticated request.
- **Friction remaining.** Everything about *which* connector, whether it is present this session, and what to do when it is not. `DEC-000080` records that the connector **"is not fixed"** and that the real failure mode is **concurrent-session contention** — and the proposal is to add more concurrent sessions to it. **[obs]** The `pass2` series ran multiple sessions in the same window. **[obs]**
- **Failure modes.** "Connector absent mid-session" is named in the remote-write policy's own list of qualifying transport failures. **[obs]** The two-failure detector exists because this path fires it.
- **Security posture.** Superficially good — no token in context — and materially worse in one specific way: **this is the path on which the repository's worst recorded write failure happened**. `OPEN-ITEMS.md` records a call carrying a placeholder string as its content parameter that "replaced a ~64KB file on the default branch with 19 bytes," and notes that landing-verification alone would have confirmed the destroyed file as a successful commit. **[obs]** A shell-based `git push` cannot make that mistake; it pushes a commit whose content is already in a local object database. A content-parameter API can and did.
- **Maintenance cost.** Externalised, which is not the same as low: the repository cannot fix it when it breaks.
- **Blast radius.** Largest of the six. Default-branch writes with no local clone to diff against and no working tree to inspect.
- **Evidence-rule fit.** **Worst.** The remote-write policy's rule 1 makes the local clone's log authoritative "where a local clone exists." A connector-only executor has no clone, so the authority the policy names is absent, and the tool's own response — which Core rule 12 classes as a claim — becomes the only signal. This inverts the methodology's central discipline.
- **Sandbox lore: deleted, and replaced by connector lore of equal or greater volume.** Which connector, whether it is attached, what its failure strings mean, when to fall back. There is no reason to expect the new lore to be smaller, and `DEC-000080` is evidence it will not be.

---

## 6. Rejected without full evaluation

- **Local relay the sandbox can reach** — a daemon on the host, outside the sandbox, that the agent calls to perform pushes. Rejected: it is a credential-bearing service whose entire purpose is to let sandboxed code reach the network the sandbox denies, i.e. a sanctioned sandbox escape. It also creates a second implementation of the write path with no review gate, and one more component that can be down. If the sandbox's network policy is wrong, the fix is the network policy, not a tunnel around it. **[inf]**
- **Deploy keys per repository** — rejected in favour of the bot-PAT variant folded into E. A deploy key is repository-scoped write with no identity, so the audit trail says only "the key"; `git log` authorship becomes uninformative exactly where change control needs it. A fine-grained PAT on a named bot account gives the same scoping with attribution. Same axes, strictly worse on one.
- **Worktree handoff** (`git worktree` in a shared directory, second session picks it up) — rejected: `skills/directive-authoring.md` warns that two sessions sharing a tree mutate each other's preconditions, and Core rule 15 makes concurrent tree mutation a stop condition. **[obs]** `retros/retro-20260823T003000.md` records four parallel-session collisions in one clone, one of which landed a commit on another session's branch. **[obs]** Handoff-by-shared-tree institutionalises the failure the rules exist to catch. The bundle variant of the same idea is kept and evaluated as D.
- **Teach every executor the lore better — a longer, more careful preamble** — rejected on the repository's own recorded reasoning: `OPEN-ITEMS.md` classes a per-dispatch restatement as an unversioned derived copy that drifts, and adds the sharper objection — "if the executor *needs* the restatement to comply, that is the load-bearing-context failure relocated from bundles to prompts." **[obs]** The observed eight-versus-one contradiction is that prediction coming true.
- **Retry harder / tolerate the errors informally** — rejected: it is the status quo, and it is what produced a refused directive. It also collides with the remote-write policy's two-failure rule, which forbids absorbing a second failure as another retry. **[obs]**

---

## 7. Ranking, next step, and what would change it

### Ranking

1. **A — standing write-path document.** Highest ratio of friction removed to cost, the only option that reduces the injection surface rather than moving it, and a prerequisite for B being citable. It is also the option the methodology has already decided it wants: `OPEN-ITEMS.md` names `skills/directive-execution.md` as the fix and marks the item still open; `DEC-000090` leaves "directives carry no version-control mechanics" explicitly reopenable; `skills/directive-authoring.md` already forbids restating what should be pointed at. **[obs]**
2. **B — `bin/land`.** The payoff, and the only option that can close the remote-write policy's named content-verification gap. Sequenced second because a tool with no governed home is new lore with an exit code.
3. **C — do less.** Free, available now, compounds with A and B, but caps out.
4. **D — patches only.** Strong security, real friction removal, disqualified from the top by the evidence rules: it structurally prevents the executor from verifying its own landing, which `DEC-000180` names as the thing an executor must never fake.
5. **E — server-side landing.** Highest ceiling, genuinely better evidence via status checks, but greenfield here and the wrong thing to build before the path it would automate is written down once.
6. **F — MCP connector for executors.** Adds contention to a transport a committed decision calls not fixed, removes the local log the evidence policy names as authoritative, and is the path on which the one catastrophic write in this repository's record occurred.

### Single best next step

**Author the standing write-path document, then cite it from the next directive instead of restating the preamble.**

Concretely, one cycle: create `skills/directive-execution.md` holding the executor
write path; move into it the environment-independent rules the recent preambles
have been carrying (branch from `origin/main`; push without relying on upstream
config; verify by reading remote state back, not by absence of errors; a
transport error string is not evidence of failure — check; cannot verify → stop
and surface; the report shape). Leave out every assertion about what a particular
sandbox permits. Fix the three dangling `skills/directive-dispatch.md` references
in `decisions/log.md` and `OPEN-ITEMS.md` in the same change, per Core rule 13.
Close or update the `OPEN-ITEMS.md` entry that proposed it.

It is one document, one review cycle, no credential, no tooling, and fully
reversible. It converts about a fifth of every recent directive into a citation,
and it gives the next `bin/land` proposal somewhere to be described.

### What evidence would change the ranking

- **A drops** if a reviewer finds the write path genuinely does vary per environment in ways a single document cannot state without becoming a decision tree. Test: draft it, and see whether it can be written without a single "if your sandbox…" branch.
- **B rises to first** if Dave wants the content-verification gap closed now rather than later — that gap is a live, recorded, data-destroying failure mode, and B is the only option here that closes it. It would also rise if a second executor session reproduces a *mechanical* failure that a script would have absorbed, rather than the noise observed here.
- **C rises** if branch-count data shows the path is walked far more often than the directive count suggests. Not measured here.
- **D rises to first** if the operator cost is smaller than assumed — measurable by timing one cycle run that way — or if a session is found where the sandbox truly has no network, making D the only option that works at all.
- **E rises** if the manual `bin/tests/run` and `check-frontmatter` reporting proves unreliable — a single instance of an executor reporting a green run that was not green would justify moving that evidence server-side immediately.
- **F rises** only if `DEC-000080` is superseded by evidence the connector is fixed *and* a content-verification step is specified for it. Neither exists today. **[obs]**
- **All of it is reprioritised** if the refusal cause is confirmed to be paste position rather than lore content — see §3.5. In that case the first fix is a habit change costing nothing, and the write-path work proceeds on its own merits rather than as an incident response.

### One thing to check before building anything

The two contradictory committed directives (§3.2) should be reconciled before a
standing document is written, because the document will have to say something
about merge, and today the record says two incompatible things. Reconciling it
needs one fact only Dave holds: whether an authenticated call to `api.github.com`
currently succeeds from an execution sandbox. Unauthenticated reachability is
confirmed **[obs]**; the authenticated case is **[unk]** from here and this
session did not and will not probe it.
