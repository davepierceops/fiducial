---
status: agreed
last-reviewed: reviews/expedited-log.md @ b31b75af12648585d7ac86f7c0d11ad85f883f5f
audience: [human]
---

# TRD: `bin/land`

This is the standing technical specification for the `bin/land` tool. It sits
beneath `specs/bin-land.md`, which owns *what* the tool does and *why*; this
document owns *how*.

It proposes. Where a choice is product judgment, or where making it would
amend an agreed goal or acceptance criterion in the PRD, this document records
it in §9 as an open technical question naming what would resolve it, rather
than settling it here.

Assertions about this repository carry a provenance class: *observed*,
*inferred*, *told*, *unknown* — the four classes `docs/global-context/core.md`
rule 6 defines (*observed*). The tool's own report carries only two of them,
per PRD G6.

## 1. System overview

`bin/land` is a **single-invocation command-line tool**, not a service. It runs
once, in the working tree of an execution session, and exits. It holds no
process, listens on nothing, and persists no state of its own.

It is the eighth executable in `bin/` and the first that performs any remote
operation: a grep for push, `ls-remote`, or remote across `bin/` returns nothing
at the base of this document (*observed*, per
`docs/research/gh-write-friction-20260823T184149Z.md`, and re-checked by reading
`bin/` at `930c4958`). The local half of what it needs already exists; the
remote half is net-new.

Shape:

- **`bin/land`** — the executable. Argument parsing, exit code, and nothing
  else of substance. Follows the shape the other seven executables use: a
  `#!/usr/bin/env python3` shebang, `argparse`, `sys.path.insert` onto its own
  directory, then `from aimeta import ...` (*observed*, `bin/flip-agreed`).
- **`bin/aimeta/land.py`** — new module. The landing sequence as an ordered
  series of steps, each returning what it established, each able to stop the
  sequence.
- **`bin/aimeta/report.py`** — new module. The report structure and its
  serialization (§5, §7). Separated from `land.py` so the format is testable
  without running a landing.
- **`bin/aimeta/repo.py`** — existing. Its `run`, `git`, and `blob_at_rev`
  primitives are reused unchanged; `run` already returns
  `(returncode, stdout_bytes, stderr_text)` with output captured as bytes and
  never decoded on the caller's behalf (*observed*, read at `930c4958`), which
  is the shape G4 needs.
- **`bin/aimeta/cli.py`** — existing. Supplies the exit-code constants and the
  stdout/stderr discipline: "all human-readable diagnostics go to stderr so
  stdout stays reserved for machine-consumable output" (*observed*, its module
  docstring).

Everything is Python 3 standard library. No third-party import is added;
`bin/tests/test_cross_cutting.py` AC-X-2 enforces that over every production
file under `bin/` (*observed*).

## 2. User journeys and SLOs

The PRD declares Top K = 3: J1 land the directive file, J2 land the session's
work, J3 a landing that cannot be verified.

**None of the three has an SLO.** This is stated explicitly here, as the
template requires, and recorded in §9 as OQ-1.

The reason is structural rather than an omission. An SLO is an objective
observed in production against a running surface. `bin/land` has no production
surface in that sense: it is a script executed inside an execution session's
sandbox, it emits no telemetry to anywhere, nothing aggregates its invocations,
and no error budget can be consumed because no shared service degrades when it
fails. The PRD says the same thing from the product side — "**Performance**: no
latency target" and "**Scalability**: N/A" (*observed*, PRD §4).

Per journey:

### J1 — land the directive file

- **SLO**: none. Unverified in production.
- **Measurement mechanism**: none in production. Pre-release, the acceptance
  criteria in PRD §6 are the evidence, run against the substrate in §4. Post-
  invocation, the only record is the session's own report quoting the tool's
  stdout, which is not an aggregated measurement.
- **Alerting threshold**: N/A. There is no aggregate to threshold and no
  recipient to alert; the tool's non-zero exit is the alert, and its audience
  is the invoking session.

### J2 — land the session's work

- **SLO**: none. Unverified in production. Identical reasoning to J1; the two
  journeys are two invocations of one form (*observed*, PRD §2), so they share
  a code path and would share any measurement.
- **Measurement mechanism**: none in production; as J1.
- **Alerting threshold**: N/A; as J1.

### J3 — a landing that cannot be verified

- **SLO**: none in the production sense. What would otherwise be J3's objective
  — that exit 0 never accompanies an unverified landing — is not an SLO but a
  biconditional the PRD already states as AC-LAND-08 and this document tests
  deterministically (§4). It is a property proven before release, not a rate
  observed after it.
- **Measurement mechanism**: the test suite, pre-release. In production, the
  session's obligation to stop and surface.
- **Alerting threshold**: N/A.

The PRD's §5 outcome signals — the share of write-path vocabulary in directive
text, the absence of a content-loss incident, whether reports cite the tool's
output — are measured by re-counting a corpus and by reading reports, not by
telemetry from this tool. They are outcome measurement, not SLOs, and this
document does not restate them as such.

## 3. Architecture and boundaries

### 3.1 Components and responsibilities

| Component | Responsibility |
| --- | --- |
| `bin/land` | Parse `<branch> <message> [files...]`; call the sequence; serialize the report to stdout; exit with the mapped code. Contains no git logic. |
| `aimeta/land.py` | The ordered sequence: resolve, guard, establish base, stage, commit, push, verify. Each step returns established facts or stops. Never retries, never writes twice. |
| `aimeta/report.py` | The report structure, its provenance labels, and its serialization. Knows nothing about git. |
| `aimeta/repo.py` | The git subprocess layer. Reused unchanged. |
| `aimeta/cli.py` | Exit codes, stream encoding, diagnostic emission. Reused unchanged. |

The split between `land.py` and `report.py` exists so that the report format
lives in a module that runs no subprocess: every report shape, failure shapes
included, can be constructed from synthetic facts without performing a landing,
and the format can be implemented and exercised on its own terms by an agent
that never touches git. That is an architectural property rather than a test
boundary — AC-LAND-T01 asserts the tool's own stdout on a real invocation, and
§5.4 states why. What each exposes to the others is §3.7; it is stated at the end
of this section rather than here so that §3.2's step numbering, which the rest of
this document and its review artifacts cite by number, is not disturbed.

### 3.2 The sequence

One invocation runs these steps in order, and stops at the first that fails.

1. **Parse.** `<branch>`, `<message>`, zero or more paths. No flags and no
   modes (*observed*, PRD G1). `--help` exits 0, as AC-X-3 requires of every
   CLI (*observed*).
2. **Fetch.** `git fetch origin`. Its exit status is the only thing read;
   stderr is captured for diagnostics and never inspected for a decision (G4).
3. **Resolve the base, from the remote rather than from a cached ref.** One
   read: `git ls-remote --heads origin <branch> main`. Its output answers both
   questions at once — whether `<branch>` exists at the remote, which decides
   which of G1's two arms applies, and `main`'s head, which is the base in the
   branch-absent arm. Where `<branch>` is present, its head is the base; where it
   is absent, `main`'s head is the base and the step has established that
   `<branch>` did not exist at the remote, which is G1's first arm. Either way
   the base SHA comes from this read, not from `refs/remotes/origin/<branch>`.
   What the report carries on either outcome is §5.3's table.

   One read rather than one per arm, so §8's stated count of remote reads before
   the write is true on both arms rather than only on the branch-present one.

   The tool selects lines from the output by exact ref name —
   `refs/heads/<branch>` and `refs/heads/main` — never by position or by line
   count. `ls-remote`'s patterns match against the tail of the ref on slash
   boundaries, so `main` also matches a branch named `sub/main` and the output
   may carry more lines than patterns given (*observed* — run against `git`
   2.55.0 over a `file://` remote: with `sub/main` present at the remote,
   `git ls-remote --heads origin feat main` returns three lines). A pattern
   matching nothing is not an error and does not change the exit status
   (*observed*, same substrate), which is what makes branch-absence a readable
   result rather than a failure.

   Reading the remote rather than a tracking ref is a deliberate technical
   decision, not a restatement of environment lore.
   `policies/remote-write-verification-policy.md` rule 1 makes the
   repository's own log against the **fetched** remote the authority on what
   landed (*observed*); a remote-tracking ref is a cache of a previous fetch,
   and the failure it produces — a base cut from a stale ref — has been
   observed in this repository's own sessions (*observed*, recorded in
   `docs/cycles/bin-land-flip-20260823T210300Z.md`). Reading the remote
   directly removes the class rather than warning about it.
4. **Confirm the base object is present locally.** `git cat-file -e <base>^{commit}`.
   If the object is absent, the tool refuses rather than fetching again — a
   second fetch would race the same way, and the tool does not loop (§6, FM-2).

   The tool refuses without asserting *why* the object is absent. The cause the
   design has in mind is that the remote moved between step 2's fetch and step
   3's read (*inferred* — not reproduced here; demonstrating it needs a
   concurrent writer). It is not the only cause: a narrowed
   `remote.origin.fetch` refspec produces the same state with the remote never
   having moved (*observed* — run against `git` 2.55.0 over a `file://` remote,
   with `remote.origin.fetch` restricted to `main`, `ls-remote` reports another
   branch's head and `cat-file -e` on that SHA exits non-zero). A shallow or
   partial clone is a third. The refusal is identical in every case, so the tool
   reports the state it observed and names no cause — which is the only thing a
   report carrying just *observed* and *unknown* can honestly do here.
5. **Divergence guard, before anything is staged.** Two checks, both against
   the base step 3 resolved, both before any ref moves. `merge-base
   --is-ancestor` prints nothing and answers only in its exit status, so each
   check carries the read that establishes the SHA §5.3's table attributes to
   it; neither SHA falls out of the check itself.

   - `git rev-parse HEAD`, then `git merge-base --is-ancestor HEAD <base>`. The
     read comes first because `detail.local_head` is established on every path
     this step runs, the one where this check refuses included (§5.3). Exit 0
     means local HEAD is at or behind the base. Non-zero means the local tree
     carries at least one commit the base does not.
   - `git rev-parse --verify --quiet <branch>`, and, where that exits 0 — the
     ref exists locally — `git merge-base --is-ancestor <branch> <base>`. The
     one read answers both of this check's questions: whether `<branch>` exists
     locally at all, and, where it does, the SHA `detail.branch_head` carries.
     It belongs to this check rather than to the step, which is what keeps the
     ordering guarantee below true of a command and not merely of a value. This
     is the ref step 6 rewrites, and local HEAD is not it. With HEAD on any other
     branch the first check passes while `<branch>` carries unpushed commits the
     base does not, and step 6 then resets `<branch>` and leaves those commits
     reachable from no ref at all (*observed* — run against `git` 2.55.0 in a
     throwaway repository: with `feature` two commits ahead of the base and HEAD on
     `main`, `merge-base --is-ancestor HEAD <base>` exits 0,
     `git checkout -B feature <base>` reports "Switched to and reset branch
     'feature'", and the prior tip is thereafter absent from `git rev-list --all`
     and not an ancestor of HEAD). The second check exits non-zero on exactly
     that state (*observed*, same substrate), and it is the only thing standing
     between the ordinary post-checkout tree state and the destructive class PRD
     §7 puts under "Not accepted".

   **Order is part of the guard.** The two checks run in the order written and
   the guard stops at the first one that refuses; where the first check refuses,
   the second is not evaluated at all and `<branch>`'s local SHA is never read.
   Stopping costs nothing, because the tool refuses rather than acts: no ref has
   moved, so the session resolves the divergence the refusal named and invokes
   again, and the second check's answer would not make that repair cheaper. It
   also keeps the refusal honest — a report naming both causes at once would have
   to describe a state in which the tool went on reading refs after deciding not
   to act, which is not something a report carrying only *observed* and *unknown*
   can say. So at most one check refuses on any path that reaches FM-3.

   Either check failing produces one refusal in one shape — FM-3 (§6), not two
   failure modes: the tool refuses before any ref has moved and exits non-zero
   (PRD G1, AC-LAND-01c). What that refusal's report carries is §5.3's table, and
   under it the report says which of the two checks refused: `detail.branch_head`
   present, the second check refused; absent, the first did, the guard having
   stopped before `<branch>`'s SHA was read. That absence is a claim and not a
   silence — §5.3's emission rule makes it one — so a session may act on the
   discrimination and a criterion may assert it. Where `<branch>` does not exist
   locally the second check has no subject and is skipped, which is not a pass
   being assumed: there is no ref to orphan.

   The guard runs **before** step 6 because step 6 moves a ref. Ordering is
   load-bearing: AC-LAND-01c requires every local-only commit to remain
   reachable afterwards, and that holds precisely because the tool has touched
   no ref by the time it refuses.
6. **Establish the base.** `git checkout -B <branch> <base>`. See §3.3.
7. **Stage, authoritatively over the index.** The index is first reset to the
   base — `git reset --mixed <base>` — and only then is content staged:
   `git add -- <paths>` for named paths, `git add -A` when none are named
   (PRD G2). Paths are always separated by `--`.

   The reset is not redundant with step 6, because `git checkout -B` does not
   clear a pre-populated index. Without it, content staged before the invocation
   survives into the commit alongside the named paths and defeats AC-LAND-02
   (*observed* — run against `git` 2.55.0: with `unrelated.txt` staged
   beforehand, `git checkout -B target <base>` leaves `git status --short` still
   reporting `A  unrelated.txt`, and a following `git add -- wanted.txt` and
   `git commit` produce a commit listing both files). With the reset in place
   the same setup commits `wanted.txt` alone, and the no-paths arm commits every
   change the tree carries — the formerly-staged file included, since by then it
   is simply one of the tree's changes, which is what G2's second arm asks for
   (*observed*, same substrate).

   The reset touches the index only: working-tree modifications and untracked
   files are left exactly as they were, and no ref moves, because step 6 has
   already put both HEAD and `<branch>` at the base (*observed*, same
   substrate). `git read-tree <base>` is equivalent for this purpose
   (*observed*); `reset --mixed` is named because it also refreshes the index's
   stat cache. Neither touches the working tree, which is the property that
   rules them in — the tool must never discard what it exists to land.
8. **Commit.** `git commit -m <message>`, with the message passed as an argv
   element and never through a shell. The repository's hooks run: `bin/land`
   never passes `--no-verify`. The pre-commit frontmatter hook is part of this
   repository's governance, and a tool on the write path that bypassed it would
   be landing work the governance never saw. A hook refusal is a failure mode
   (§6, FM-6), not something to work around.
9. **Push.** `git push origin <branch>`. Plain: never `-u`, never `--force`,
   never `--delete`. The exit status is the outcome (PRD G4).
10. **Verify.** `git ls-remote --heads origin <branch>` must equal the new head
    SHA (AC-LAND-05); then `git fetch origin refs/heads/<branch>` and, for each
    path in the commit, compare the blob SHA at the fetched remote commit
    against the blob SHA in the local commit (AC-LAND-06). The head check runs
    first and the comparison runs only where it passed. That order is why a
    remote whose content was mutated between the push and this step stops at the
    head check rather than at the comparison — §6 states what follows from it,
    for AC-LAND-06's failure branch and for PRD §5's measurement alike.
11. **Report and exit.** The report is serialized to stdout on every terminal
    path the sequence reaches — the success path and every failure mode §6
    enumerates as detected, including each of the paths §5.4 individuates
    within them (§5). Two terminal paths lie outside that rule, and are stated
    here rather than left for an implementer to decide:

    - **A usage error.** Parsing belongs to `argparse`, in `bin/land`, and runs
      before the sequence begins (§3.1). `argparse` writes its own diagnostic to
      stderr and exits 2; **stdout carries nothing and no report is emitted.**
      That is consistent with `aimeta/cli.py`'s standing discipline —
      diagnostics on stderr, stdout reserved for machine-consumable output — and
      with §7's mapping of 2 to a usage error. Nothing is intercepted and no
      failure mode is added for it: an invocation that never named a branch has
      established no fact for a report to carry — not even `branch`, which
      §5.3's table gives every terminal path the sequence does reach. §3.1's
      division of responsibility is unchanged by this.
    - **FM-10**, an invocation killed mid-sequence, which emits nothing because
      no code of the tool's runs to emit it (§6).

Steps 2, 3, 9, and 10 are the only network operations, and there is exactly one
of each write: one push per invocation, on every path. §8 states how that is
enforced.

### 3.3 Base establishment for the at-or-behind case

PRD G1 fixes the base at remote state and PRD G2 stages from the local tree,
and the operation joining them is not stated at PRD level — recorded as
`reviews/bin-land-cycle-4.md` O1, which names three candidates: fetch-and-reset,
`commit-tree` against the fetched base, and checkout-then-stage (*observed*).

**Decision: `git checkout -B <branch> <base>`.** One command. It creates or
resets the local branch `<branch>` to the fetched base, checks it out, and
carries uncommitted working-tree changes across.

What the working tree **and the index** hold afterwards, stated because O1
records that the three candidates "differ only in what they leave in the tree
afterwards" (*observed*), and because the index is the half of that answer
`checkout -B` gets wrong:

- **Immediately after step 6**: the tracked content of the fetched base, plus
  every uncommitted modification and untracked file the session had before the
  invocation. Nothing the session produced is discarded; that is the property
  that rules out `git reset --hard`, which would destroy exactly the work the
  tool exists to land. The **index is carried across unchanged**: `checkout -B`
  does not clear it, so anything the caller staged before the invocation is
  still staged at this point (*observed*, §3.2 step 7). This is the reason step
  7 resets the index rather than merely adding to it; left alone, that
  pre-staged content would enter the commit and defeat AC-LAND-02.
- **Immediately after step 7**: the working tree is untouched by the reset, and
  the index holds the base plus exactly what was staged from the named paths —
  or plus every change in the tree, where none were named. What the caller had
  staged before the invocation has no bearing on the commit either way.
- **After a successful invocation**: HEAD on `<branch>`, at the new commit,
  which is also the branch's head at the remote. Paths that were landed are
  clean. Where paths were named and other changes existed, those other changes
  are still present in the working tree, uncommitted — and unstaged, since step
  7's reset dropped them from the index and the named paths were all that was
  added back.

Two consequences are stated rather than left to be discovered:

- **The J1→J2 sequence works without the session doing anything between
  invocations.** After J1 the local branch is at the landed head, so J2's
  divergence guard sees a tree at the base and proceeds. A design that left
  local HEAD where it was — `commit-tree` against the fetched base, writing the
  ref directly — would leave the session's second invocation staging the same
  file again against a base that already contains it.
- **HEAD moves.** If the checkout was on some branch other than `<branch>`,
  `checkout -B` moves HEAD off it, and the prior branch's ref is not touched.
  That no commit becomes unreachable is **not** a property of `checkout -B`, and
  step 5's first check does not establish it: that check speaks for the branch
  HEAD was on, while the ref this step rewrites is `<branch>`. Run without a
  guard on `<branch>`, this step orphans whatever unpushed commits `<branch>`
  carried (*observed*, the probe recorded at §3.2 step 5). The claim holds only
  because step 5's guard refuses before this step runs: the second check refuses
  in that state, or, where local HEAD has diverged as well and the guard stops
  before reaching it, the first check does. Either way no ref has moved by the
  time the tool exits. The guard is what makes the claim true, not the
  mechanism.

  **In the cases the guard permits, the tool moves HEAD rather than refusing.**
  That is a settled decision, not an open question. Refusing would rule out J1 in
  any session whose worktree was not created on the target branch — the ordinary
  opening state, since the first invocation is the one that creates the branch —
  so the refusal would cost the journey the tool exists to serve. What it costs
  instead is that the session's checked-out branch changes under it, and that is
  reported rather than left silent: the report names the branch HEAD was moved
  off, on the paths §5.3's table states. OQ-5 asked this question; §9 records the
  answer and retires the identifier.

`checkout -B` fails when a locally-modified file's committed content differs
between the old HEAD and the base (*observed* — run against `git` 2.55.0 in a
throwaway repository: with `f.txt` modified in the working tree and its
committed content differing between the old HEAD and the base,
`git checkout -B target <base>` prints "Your local changes to the following
files would be overwritten by checkout", exits 1, and leaves the modification
in place; where the modified file's committed content is identical in the two,
the same command exits 0 and carries the modification across). That is a real
and reachable state, it is caught before any commit or push, and the tool stops
there (§6, FM-4). A false stop is cheap (*observed*, PRD §7).

### 3.4 The branch-absent diverged case

`reviews/bin-land-cycle-5.md` O1 records that PRD G1 states the divergence
refusal inside its second arm only, so a local tree carrying commits
`origin/main` lacks, with the named branch absent at the remote, is governed by
no explicit sentence and by no acceptance criterion; both refusing and
proceeding satisfy every stated goal (*observed*).

**Proposed behaviour: the tool refuses, uniformly.** The guard at step 5 runs
against whatever base step 3 resolved and does not know which arm produced it,
so refusal in this state is what the natural implementation does rather than an
extra rule. The reason to prefer it over proceeding is concrete: with
`checkout -B` as the base-establishment mechanism, proceeding in this state
would move `<branch>` — which, in the branch-absent arm, may be the very local
branch carrying those commits — and abandon them to the reflog. Refusing costs
a stall; proceeding costs commits.

Step 5's guard makes this mechanical rather than merely intended: where some
other branch carries the commits, the first check refuses; where the local
`<branch>` carries them and local HEAD is at or behind the base, the second does;
and where both carry them, the guard stops at the first, which is the same
refusal in the same shape. So the refusal in this arm falls out of the guard on
every route, and the proposal below is a question about whether the PRD should
*say* so, not about what the tool would do.

This is a proposal, not a decision. No PRD goal or criterion decides it, and
Dave has held cycle-5 O1 out of scope. Recorded as OQ-2.

### 3.5 External dependencies

- **`git`**, as an executable on `PATH`. The only dependency, and the only
  thing on the network path. No HTTP client, no SDK, no `gh` — PRD's non-goals
  forbid `gh` "never, for anything, including auth checks" (*observed*).
- **The remote git service.** In production, GitHub over HTTPS. The tool makes
  no assertion about it and never names it in code; `origin` is whatever the
  invoking repository has configured.
- **The ambient credential helper.** Used by `git` internally and never by the
  tool. The tool reads no credential, writes none, logs none, and passes none.
- **The sandbox's host allowlist.** Supplied by the runner, not by this
  repository, and not something any change here can make uniform (*observed*,
  PRD §4 Non-goals, per the research findings).
- **The repository's own pre-commit hook**, when installed by
  `bin/install-hooks`. In-process from the tool's perspective: it runs inside
  step 8's `git commit`. In-process is not the same as controlled — it is
  declared as boundary B5 (§3.6, §4.2), and its evidence class is the one this
  design leaves weakest.

### 3.6 Boundaries

The points where the tool meets something it does not control:

- **B1 — the remote git service.** The receive-pack that accepts the push and
  the upload-pack that answers `ls-remote` and `fetch`.
- **B2 — the credential path.** Whatever `git` does to authenticate, including
  the helper whose stderr output PRD G4 exists to be indifferent to.
- **B3 — the sandbox network policy.** Whether the remote is reachable at all.
- **B4 — `git` itself.** The plumbing this design relies on:
  `ls-remote --heads`, `merge-base --is-ancestor`, `cat-file -e <rev>^{commit}`,
  `checkout -B`, `reset --mixed`, and `rev-parse` in three forms — `<rev>`,
  `--verify --quiet <rev>`, and `<rev>:<path>`.
- **B5 — this repository's own pre-commit hook.** Installed by
  `bin/install-hooks`, it runs inside step 8's `git commit` and can refuse it
  (§6, FM-6). Running in-process is what made it easy to miss as a boundary, and
  it is not what decides the question: the hook is this repository's governance
  standing on the write path, the tool deliberately does not bypass it, and the
  tool does not control what it does. That is a boundary.

Each is declared in §4 with its representation and evidence class.

### 3.7 Interfaces between components

The sequence in §3.2 fixes the semantics; this states the seams that sequence
implies. It is here because `land.py` and `report.py` are written by separate
agents, from this text and from each other, under this repository's separation of
test authorship from implementation — so the seam has to be in the document or
the two modules do not meet. Names and signatures are proposals at the
granularity an implementer needs, not a frozen API.

**`bin/land` → `land.py`.** One entry point:

    land(branch: str, message: str, paths: list[str], cwd: str) -> Report

`paths` is empty for G2's no-paths arm. It raises nothing for an expected
failure: every terminal state of §3.2 that the sequence reaches, success and
failure alike, comes back as a `Report`. `bin/land` serializes what it is handed
and maps the report's exit code onto its own. That is the whole of `bin/land`'s
substance, which is what §3.1's "contains no git logic" means concretely.

**Within `land.py` — what a step returns.** Each step of §3.2 returns either the
facts it established or a stop:

    StepResult(ok: bool, facts: dict, stage: str, git_status: int | None)

`facts` carries what that step established, keyed as §5.2 and §5.3 name the
fields. **Which fact each step establishes is §5.3's key table**, whose middle
column names the establishing step for every field and key the report can carry.
This section does not restate it and carries no parallel account of it: an
implementer writing `land.py` reads that table. `stage` is the token §5.3's token
table assigns to that stop, carried on the stop so the report can say where the
sequence halted; it is one token per stop rather than one per step, which is why
the table and not the step number is what an implementer reads. `git_status` is
the failing invocation's exit status; the signature admits `None` because not
every stop is a subprocess, and §5.3's row for that key names which. The sequence
accumulates `facts` across steps and halts at the first `ok: False`. No step
reads another step's git output; a step consumes established facts, never text.

**`land.py` → `report.py`.** `land.py` never formats:

    Report.build(branch: str, facts: dict, stop: StepResult | None) -> Report

`build` assembles the report from the accumulated `facts` and from nothing else,
under §5.3's key table. What `facts` holds is not what decides emission: §5.3's
"Established on" column decides it, for the terminal path the sequence reached —
the unit §5.4 defines and individuates. For each field and key that table
establishes on that path, `build` emits what `facts` carries, in the shape and
the value domain §5.2 fixes. Where the table
does not establish one there, `build` does not emit it as established, whatever
`facts` happens to hold; what stands in its place — a contract field still
present but `unknown`, a `detail` key absent — is §5.3's to state, and §5.3
states it once. Accumulation and emission are two questions and only the second
is this seam's: `facts` records what the sequence established, and the table
decides what the report carries. That is one rule, read from one place, rather
than a rule each failure path has to remember — and it is the whole of the
separation §3.1 claims between establishing a fact and reporting one. `build`
implements that rule and this section does not restate it.

**How `build` knows which terminal path it is on.** That rule is keyed to the
terminal path, so `build` has to determine the path from `branch`, `facts` and
`stop` and from nothing else. It can, on every path, and this is how. `stop is
None` is the success path; the sequence has no other way to finish. Otherwise
`stop.stage` carries the token, and the token names the failure mode outright on
every token but one — `fetch` FM-1, `base-object` FM-2, `guard` FM-3, `base`
FM-4, `stage` and `nothing-staged` FM-5, `commit` FM-6, `push` FM-7, `verify`
FM-8. The exception is `resolve`, which two modes reach: FM-1 where step 3's read
failed, FM-11 where it succeeded and named no base. `stop.git_status` separates
them — FM-1's stop is a failed subprocess and carries that invocation's exit
status, FM-11's stop is a read that exited 0 and carries none — which is the
same distinction §5.3's `detail.git_status` row draws between a stop that is a
failed subprocess and a stop that is a comparison. Within a mode, the two rows
§5.3 conditions are decided by whether `facts` carries that row's own key, and
that is well defined because each condition is a state the establishing step
observed and recorded: `facts` carries `detail.branch_head` exactly where step
5's second check refused, the guard having short-circuited before the ref was
read where the first check refused (§3.2 step 5), and carries
`detail.prior_branch` exactly where step 6 found HEAD on a branch other than
`<branch>` (§3.3).

None of that reads an emission outcome, and none of it makes `facts` the
discriminant of emission. The two questions stay apart, and `detail.branch_head`
is where the difference is visible: step 5's second check reads `<branch>`'s SHA
whenever it runs, so `facts` carries that key on every path past a guard that
passed, and §5.3's table names it on none of them. `build` identifies the path
first and emits under the table second, so on those paths the key is not
emitted, whatever `facts` holds.

Two properties of `build` are seams between the two modules rather than entries
in §5.3's table, and are stated here for that reason:

- **`branch` comes from the parameter**, not from `facts`. No step establishes
  it; `bin/land` passes it in. That is what makes it available even on a path
  where the sequence established nothing else at all.
- **`verification` is computed, not carried.** No step returns it. `build`
  derives it from what `facts` holds, under the biconditional §5.2 states — the
  same biconditional §7's exit mapping reads. Deriving both from it in one place
  is what stops the report and the exit code from drifting apart, which is
  AC-LAND-T02.

`files` is the one contract field that is a list rather than a leaf, so its
unknown-ness is carried per entry, or by the absence of entries, never by a
`class` on the list — no union type enters the parse contract, which is the
property AC-LAND-T01 tests. Its shape is §5.2's; what it carries on a given path
is §5.3's.

**What `report.py` exposes.** A `Report` carries the five contract fields and the
`detail` object of §5.3, and offers:

    Report.to_json(self) -> str      # §5.2's format: two-space indent, sorted
                                     # keys, UTF-8, one trailing newline
    Report.exit_code(self) -> int    # §7's mapping

`to_json` is a pure function of the `Report`: it touches no git, no filesystem,
and no clock, and `build` is handed facts rather than reading them. Together
those are the surface §3.1's split rests on — every report shape, failure shapes
included, is constructible by calling `Report.build` with synthetic facts and
never performing a landing. That is not what AC-LAND-T01 does: that criterion
asserts the tool's own stdout on a real invocation, for the reasons §5.4 gives.
What the purity buys is the architectural half — the format is fixed by a module
a second agent can implement and exercise with no git in front of it.

**`report.py` → nothing.** It imports no `repo.py` and starts no subprocess. The
dependency runs one way — `bin/land` → `land.py` → `report.py` — with `land.py`
reaching `repo.py` for git, and both executables taking their exit constants from
`cli.py`. A cycle between the two new modules would defeat the reason for
splitting them.

## 4. Verification boundaries (standing)

### 4.1 Test substrate — decided

PRD §6's preamble carries the substrate as *inferred*: "the test substrate is
expected to be a bare repository served over `file://`" (*observed*).

**Decision: a bare repository served over `file://`, created per test by a new
helper in `bin/tests/helpers.py`, added as `origin` of a repo built by the
existing `make_repo`.**

Rationale:

- The suite's standing constraint is "**No mocked git.** Every git interaction
  in this suite runs against a real repository created with `git init` in a
  throwaway temp directory" (*observed*, `bin/tests/helpers.py` docstring). A
  bare repo keeps that true for the remote half.
- `file://` rather than a bare filesystem path is deliberate. A plain path lets
  git take its local shortcuts; a `file://` URL drives the actual
  upload-pack/receive-pack transport, so fetch, push, and `ls-remote` exercise
  the code paths a real remote would (*inferred* — the distinction is git's
  documented behaviour, not something run in this session).
- It is offline, has no credential surface, needs no port and no daemon
  process, and cannot be affected by the sandbox's host allowlist.

Alternatives considered and rejected: **`git daemon` on localhost** — needs a
port, a background process, and network permission the sandbox may not grant,
and buys nothing `file://` does not; **mocking the git subprocess layer** —
forbidden by the suite's own constraint above, and it would make the whole
suite prove nothing about the operations that matter.

New helpers required: a bare-remote factory, a remote-head reader, a way to
mutate the bare repository between push and verification, and a way to install a
`pre-receive` hook into the bare repository that refuses a push. The third is
what induces FM-8, the `ls-remote` disagreement (§6), and it is therefore also
how the content-verification test PRD §5 names produces its mismatch: under git
transport a mutation of the pushed content moves the branch's head at the remote,
so it is the head check that mutation trips. The fourth is what induces FM-7: a
bare repository accepts what it is given, so a push git rejects has to come from
the remote refusing it, and the refusal happens during the push rather than after
receive-pack has answered, which is what distinguishes it from the third
(*inferred* — `pre-receive`'s place in receive-pack is git's documented
behaviour, not something run in this session). The two
inducement helpers are named here because the substrate as decided produces
neither state on its own; what each stands in for, and what it therefore does not
prove, is §5.4's and §4.2's.

### 4.2 Standing boundaries

**B1 — remote git service.**
- Production surface: GitHub's receive-pack and upload-pack over HTTPS, reached
  as `origin`.
- Currently represented as: a local bare repository over `file://`.
- Evidence class: **contract-verified**. The git wire protocol and the exit-
  status contract are exercised for real; the provider is not.
- Does not prove: live credentials, provider availability, provider-side ref
  policies (protected branches, push rules), or behaviour under a concurrent
  push from another session.
- Deferred-verification path: one live landing onto a scratch branch at the
  real `origin`, read back with `ls-remote`, recorded in the change package for
  the implementing change. OQ-7 asks whether that is required before release
  and on what cadence it re-runs.

**B2 — credential path and its stderr.**
- Production surface: `git`'s credential helper, whose store step writes
  `fatal: failed to store: 100001` to stderr while fetch, push, and `ls-remote`
  exit 0 and take effect (*observed*, per the research findings, and *observed*
  again in this session's own push at step 1 of the directive).
- Currently represented as: two induced cases for AC-LAND-04, using a `git`
  shim on a temporary `PATH` — one that writes that line to stderr and exits 0,
  one that writes nothing and exits non-zero. `bin/tests/helpers.py` already
  provides `fake_path_dir` for building a sparse `PATH` (*observed*).
- Evidence class: **mock-verified** for the two induced cases.
- Does not prove: that any particular sandbox produces that line, which is not
  a claim this repository can make about a runner it does not own.
- The durable half of AC-LAND-04 is not the induced cases but the static one:
  no code path in the source matches or branches on stderr content, verifiable
  by scanning the source, in the manner AC-X-1 and AC-X-2 already scan `bin/`
  (*observed*). A static scan does not go stale when a message changes.

**B3 — sandbox network policy.**
- Production surface: whether the runner's allowlist permits reaching `origin`.
- Currently represented as: **not represented**. Assumed.
- Evidence class: **assumed**.
- Deferred-verification path: none, and deliberately none. The tool attempts
  the operation and reports what it observed; PRD §4 Non-goals makes surviving
  this variance the design and controlling it a non-goal (*observed*).

**B4 — `git` itself.**
- Production surface: the `git` binary the runner supplies.
- Currently represented as: whatever `git` the test host has.
- Evidence class: **live-verified, incidentally** — every test in the suite
  runs against a real `git`, but only the one version present.
- Does not prove: behaviour on another version. No minimum version is asserted,
  and §9 records that as a decision rather than an omission; the identifier OQ-8,
  which once asked whether a floor should be pinned and tested, is retired there.

**B5 — this repository's own pre-commit hook.**
- Production surface: the `pre-commit` hook `bin/install-hooks` installs, running
  inside step 8's `git commit` in a real clone of this repository. It is what
  makes FM-6 a failure mode rather than a hypothetical.
- Currently represented as: **not represented.** `bin/tests/helpers.py`'s
  `make_repo` runs `git init` and three `git config` calls and installs no hook
  (*observed*), and the suite's isolation constraint states that its subprocesses
  "never inherit the developer's `AI_METHODOLOGY_HOME`, global git config, or
  global hooks" (*observed*, that module's docstring). The substrate §4.1 decides
  therefore produces FM-6's trigger only where a hook is installed into it
  deliberately, and the hook §5.4's AC-LAND-T01 installs is a **stand-in that
  refuses** rather than this repository's own.
- Evidence class: **assumed**, and the stand-in does not raise it. What T01
  installs it controls completely, and a boundary is the thing the tool does not
  control; the stand-in exercises git's refusal contract and the tool's conduct
  on that path, and represents nothing about the hook this boundary is about.
- Does not prove: that this repository's `pre-commit` hook refuses the commits it
  exists to refuse; that it refuses them by exiting non-zero rather than by some
  other outcome; or that its own diagnostics stay off stdout, which AC-LAND-T01's
  "stdout carries no text outside that object" requires and which is checked for
  the stand-in and for nothing else. What T01's hook-refusal cases do establish is
  the report's shape and status on that path, which is a property of the tool
  rather than of the hook.
- Deferred-verification path: a test that installs this repository's `pre-commit`
  hook into the substrate repo and induces FM-6 with a file the frontmatter check
  rejects.

Leaving B5 **assumed** is a permitted outcome; leaving it undeclared was not.
§3.2 step 8 makes the hook load-bearing on purpose — a tool on the write path
that bypassed governance would be landing work the governance never saw — so a
dependency the design routes governance through, which produces an enumerated
failure mode, and which the substrate exercises only through a stand-in, is
exactly what this section exists to name. The declaration is what puts the choice
in front of Dave: buy the deferred path, or accept the class knowingly. What it
removes is the third option, of shipping FM-6 on evidence nobody classified.

### 4.3 A note on what the per-file comparison proves

Stated plainly because it bears on how much B1's contract-verified class
carries, and because PRD §1 names closing the content-verification gap as this
tool's distinguishing goal.

Under git's content addressing a commit SHA determines its tree, so once
`ls-remote` returns the same commit SHA the tool pushed, the per-file blob SHAs
necessarily agree (*inferred*). **Under git transport, therefore, the per-file
comparison adds nothing to the `ls-remote` check.** It cannot fail where that
check passed. It is not independent evidence, and this document does not claim
it as any, in either of the two senses an earlier draft of this section did.

It is still required, for one reason, and the reason is not evidential: PRD G6
requires the report to carry a per-file result, and the comparison is how that
field gets its value.

The check that would catch the failure class
`policies/remote-write-verification-policy.md` records is the other one. That
policy's Known gap describes a write whose response is truthful and whose commit
is real, because the *request* was wrong: a call carrying a placeholder string as
its content parameter replaced a ~64KB file with 19 bytes, and
landing-verification confirmed the destruction as a success (*observed*, that
policy's Known gap). The git-transport analogue of a wrong request is a
**mis-staged file** — and a mis-staged file is committed locally with the wrong
content, so its blob SHA in the local commit and its blob SHA at the remote agree
exactly, and AC-LAND-06's comparison passes (*inferred*). What would catch it is
a comparison of the bytes fetched back from the remote against the bytes of the
named file on disk: the form that does not reduce to commit-SHA equality.

That stronger form is not adopted here, because AC-LAND-06 states the comparison
as "equals the blob SHA committed locally" (*observed*), and changing what an
agreed criterion asserts is Dave's, not this document's. The consequence is
recorded rather than softened: as AC-LAND-06 is written, the tool would ship a
content-verification step arithmetically redundant with its own landing check,
and the gap PRD §1 and G5 name as this tool's reason for existing would remain
open while the PRD, this document, and every change package recorded it as
closed. That is OQ-6 — not a question of optional strengthening, but the question
G5's stated purpose depends on.

## 5. Data and state

### 5.1 State

`bin/land` owns no persistent state. It writes no configuration, no cache, no
log file, and nothing outside the invoking repository. AC-X-5 already asserts
containment for every CLI in `bin/` (*observed*); see OQ-9 for how that scan
accommodates the first tool that writes to a remote.

State it touches, and who is authoritative:

| State | Touched how | Authoritative |
| --- | --- | --- |
| Local object database | Objects written by fetch and commit | Local, until pushed |
| Local branch ref `<branch>` | Reset to the base at step 6; advanced by the commit | Local |
| `HEAD` | Moved to `<branch>` at step 6 | Local |
| The index | **Not** cleared by step 6's checkout — `checkout -B` carries a pre-populated index across intact (*observed*, §3.2 step 7). Reset to the base by step 7, then written by step 7's staging | Local |
| `refs/remotes/origin/*` | Updated by step 2's fetch | A cache — never read as the base (§3.2, step 3) |
| The remote ref | Advanced by step 9's push | **The remote.** Rule 1 of the remote-write policy makes the repository's own log against the fetched remote the record (*observed*) |
| stdout | The report | Derived; nothing reads it back |

### 5.2 The report: shape and serialization

PRD G6 names five fields and states that "how they are serialized is a
technical decision, named at the TRD stage, and the format the TRD names
carries all five" (*observed*). AC-LAND-07 tests presence and labelling and
defers mechanical parseability to this document (*observed*).

**Decision: one JSON object, pretty-printed with two-space indentation and
sorted keys, UTF-8, one trailing newline, written to stdout and nowhere else.**
Diagnostics go to stderr, per `aimeta/cli.py`'s existing contract.

Rationale, against the obvious alternative of one `key: value` line per field:

- The per-file result is a variable-length list and each field carries a
  provenance label, so the format needs two levels of nesting. A flat line
  format needs a quoting convention invented for this tool.
- A commit message, a branch name, or a path containing a newline, a colon, or
  a quote cannot corrupt JSON framing. A line format's framing is exactly what
  such content breaks — and the message is caller-supplied text.
- Both ends of the contract have a parser in the standard library: `json` for
  the tests and for any future consumer, and every plausible reader of the
  output already parses JSON.
- Pretty-printing keeps it readable by the actual consumer, an agent session
  that will paste it into a report, without costing parseability.

Shape, shown on one path — a first landing that created `<branch>`, invoked from
a worktree standing on `main`:

```json
{
  "branch":     {"value": "bin-land-trd", "class": "observed"},
  "head":       {"value": "<40-hex>", "class": "observed"},
  "prior_head": {"value": "created", "class": "observed"},
  "files": [
    {"path": "specs/bin-land-trd.md", "match": true, "class": "observed"}
  ],
  "verification": {"value": "complete", "class": "observed"},
  "detail": {
    "base":         {"value": "<40-hex>", "class": "observed"},
    "local_head":   {"value": "<40-hex>", "class": "observed"},
    "prior_branch": {"value": "main", "class": "observed"},
    "remote_head":  {"value": "<40-hex>", "class": "observed"}
  }
}
```

The `detail` object above is this path's, not a template for the others: which
keys it carries on a given path is §5.3's table, and this section states only the
shape they all share.

Rules the format holds on every path:

- The five contract keys — `branch`, `head`, `prior_head`, `files`,
  `verification` — and the `detail` object of §5.3 are **always present**, in
  success and in every failure. This rule fixes the top-level key set and
  nothing more: what each key carries on a given path, and which keys `detail`
  itself carries there, are §5.3's table.
- Every leaf object carries `class`, whose value is `"observed"` or
  `"unknown"` and nothing else. These are the two of Core's four classes PRD G6
  permits the tool to emit, stated there as a subset rather than a redefinition
  (*observed*).
- A leaf object carries **exactly** `value` and `class`, and no other key; a
  `files` entry, the one leaf whose established value is not named `value`,
  carries exactly `path`, `match`, and `class`. The format's key sets are closed
  at every level it has — the top level by the rule above, `detail`'s by §5.3's
  table, and a leaf's by this rule — so a reader meeting a key it did not expect
  has met a defect rather than an extension, and a criterion may say so.
- `value` is `null` wherever `class` is `"unknown"`. An unestablished fact is
  never rendered as an empty string or a plausible placeholder. A `files` entry
  is the one leaf that names its established value `match` rather than `value`,
  and carries no `value` key at all, so on such an entry this rule reads over
  `match` — which the `files` rule below states directly.
- **A non-ASCII character in any value is written as a `\uXXXX` escape.** The
  object is serialized with `ensure_ascii=True`, so stdout is pure ASCII on every
  path, whatever a value carries. This does not contradict the UTF-8 the decision
  above names: ASCII is a subset of it, so the stream is UTF-8 and happens to use
  none of it past the first 128 code points. Nor does it narrow any value domain
  stated here — an escape and the raw character parse to the same string, so a
  rule about what a field may carry is indifferent to which of the two forms
  carried it. The rule belongs to the serialization rather than to any one field,
  and reaches every string the report emits.
- `branch.value` is the branch name the invocation named, as a JSON string,
  carried exactly as the argument gave it. Its `class` is always `"observed"`
  and its `value` is never `null`: `branch` comes from the parameter rather than
  from a step (§3.7), and §5.3's table establishes it on every path a report is
  emitted at all, so there is no path on which it is a fact the tool failed to
  establish.
- `head.value` is a 40-character SHA or `null`; `null` only with
  `class: "unknown"`.
- `prior_head.value` is a 40-character SHA, the literal string `"created"`
  (PRD G1, first arm), or `null`; `null` only with `class: "unknown"`.
- `files` is a list, possibly empty. Each entry carries `path`, `match`, and
  `class`. `match` is `true`, `false`, or `null`; `null` only with
  `class: "unknown"`.
- `verification.value` is `"complete"`, `"incomplete"`, or `null`; `null` only
  with `class: "unknown"`. `"complete"` if and only if `ls-remote` confirmed the
  head SHA and every per-file comparison matched — the same biconditional as
  AC-LAND-08's exit status, so the two can never disagree.
- `detail.git_status.value` is git's exit status for the invocation that failed:
  a JSON **number**, and an integer, never a string. It has no `null` branch,
  because §5.3's emission rule leaves a `detail` key the table does not establish
  on that path **absent** rather than present-and-unknown — so every `detail` key
  a report carries, it carries with `class: "observed"`, and this rule is the
  worked instance of that for the one `detail` key whose value is not a SHA or a
  name.

The four value-domain rules that admit `null` — `head`, `prior_head`, a `files`
entry's `match`, and `verification` — are written to one shape on purpose. Each
admits `null`, and each admits it only under `class: "unknown"`, so none of them
contradicts the null-on-unknown rule above it on the paths where §5.3's table
does not establish the contract fields. A rule list that permitted only
`"complete"` or `"incomplete"` would force an implementer to emit
`verification: {"value": "incomplete", "class": "observed"}` on a fetch failure —
asserting the tool observed an incomplete verification it never attempted, which
inverts exactly the distinction PRD G6 exists to draw.

The two that admit no `null` are the two that cannot need one, and each rule says
why in its own words: `branch` is established wherever a report exists at all,
and an unestablished `detail` key is absent rather than unknown.

**Why the escaped form and not the raw one.** Both forms satisfy every other
rule in this section, and both parse to the identical string, so what separates
them is not what the report means but what the stream survives.
`ensure_ascii=False` would write such a character as UTF-8 bytes, and the
readability this section chose pretty-printing for pulls that way. It is
outweighed by a kind of argument readability does not answer: a script's stdout
must not depend on the ambient locale being UTF-8. The raw form has failure
modes the escaped form does not — a locale that is not UTF-8 can mangle the
bytes on the way out, or the write can fail outright — and the escaped form has
no failure mode of its own to set against them, in any environment. Nothing is
given up for that, because the two parse to identical data. The state is
reachable rather than hypothetical: the branch name and the paths are
caller-supplied text, which this section's own framing rationale already reasons
about on exactly that footing, and both are carried in report values — `branch`
and each `files` entry's `path` — so a real invocation can put a non-ASCII
character into the object this rule is about. OQ-11 asked this question; §9
records the answer and retires the identifier.

**What an empty `files` list means.** Where no commit was made there are no
per-file entries and `files` is `[]`. That `[]` is **not** a claim that the
commit contained no files — there is no commit for it to be a claim about. It is
the absence of entries. `detail.stage` is what distinguishes it from the stop at
which an empty staged set is itself the established answer and the same `[]`
means something different; §5.3 closes that field's value set, which is what
makes the distinction firm enough to rest this on. No union type is introduced:
giving `files` a leaf form of `{"value": null, "class": "unknown"}` in place of
the list would put a type switch into a parse contract whose whole burden is that
a failed landing stays mechanically readable, and it would buy nothing the stage
token does not already carry. Its unknown-ness is carried by the stage token and
by having no entries, never by a `class` on the list.

**What an entry with no match means.** Where a commit was made and no per-file
comparison result exists for it, `files` is **not** empty. It carries one entry
per path in the commit, each of the form
`{"path": "<path>", "match": null, "class": "unknown"}`. The rules above already
admit that shape and no new type is introduced: `match` is `null` under
`class: "unknown"`, which is the per-entry unknown-ness the list was given in
place of a leaf form.

The paths themselves were established — the tool staged them at step 7 and
committed them at step 8 — and the match was not, so the entry claims the first
and declines the second. That is what AC-LAND-07's per-file requirement and
AC-LAND-09's split between what was established and what was not both ask for on
a commit that exists; an empty list there would claim neither, and would be
indistinguishable in shape from the empty list a stop before the commit produces.
A session handed such a report has to be able to name the files sitting in the
local commit it must now resolve. **Which paths carry entries, and of which of
the two shapes, is §5.3's table.**

### 5.3 The failure path and the five-field contract

`reviews/bin-land-cycle-4.md` O3 records the tension: G1's refusal requires the
output to name "the divergence and both heads", and the local head is not among
G6's five fields; G6 nonetheless presents the five as "the PRD-level contract",
so "a TRD author deriving the serialization format from G6 alone would not
leave room for it" (*observed*).

**Resolution: a sixth top-level key, `detail`, which is an object and is always
present.** The five contract keys keep their exact meanings and are never
overloaded to carry something else. `detail` holds path-specific established
facts, each an object with the same `value`/`class` shape.

**The key table — this document's single statement of which path carries what.**
For every contract field and every `detail` key, the table below names the fact,
the step of §3.2 that establishes it, and the paths on which the report carries
it as established. No other passage in this document states any of that on its
own authority, and none may: §3.2 states what each step does, and reads an FM-3
refusal's report off this table rather than stating a rule of its own for it;
§3.7 states that `build` emits under this table rather than from whatever `facts`
holds; §5.2 states the shape and the value domains; and §6's cells are derived
from this table for the path each row is about. Where any of those and this table
disagree, this table is normative and the other passage is wrong.

**This section's prose is not a second voice.** That rule holds within §5.3 as
well as outside it. The key table's rows are where this document states which
path carries which key, and the one emission rule below them states what follows
where a row does not name a path; between them that is the whole of what this
section asserts. No other passage here states or implies that a given path
carries a given key, and none may. The paragraphs around the table explain it —
why the column is exact, what a row's condition turns on, what the table's
success-path entries reflect — and assert nothing of their own about scope. Where
such a passage and the table would disagree there is nothing to weigh: the
passage was explaining, and it is wrong.

**Established** means the report carries the fact with `class: "observed"`. What
follows from a path not being named is the one emission rule, stated below the
table.

| Key | The fact, and the step of §3.2 that establishes it | Established on |
| --- | --- | --- |
| `branch` | The branch the invocation named. Taken from the argument; no step establishes it (§3.7) | Every path on which a report is emitted |
| `head` | The SHA of the commit step 8 made | FM-7, FM-8, and the success path |
| `prior_head` | The head `<branch>` held at the remote as step 3 read it, or the literal `created` where that read found `<branch>` absent there | Every path on which step 3's read succeeded: FM-2 through FM-8, FM-11, and the success path |
| `files` | One entry per path in the commit, each naming the path and, where step 10 compared it, whether the remote blob matched | Entries with `class: "observed"` on the success path. On FM-7 and FM-8 — a commit exists and step 10 produced no comparison — one entry per committed path with `match: null` and `class: "unknown"`, taken from the paths step 8 committed. On every other path, no entries |
| `verification` | Whether the landing was verified end to end, under §5.2's biconditional. Computed by `build`; returned by no step | `"complete"` on the success path; `"incomplete"` on FM-7 and FM-8 |
| `detail.stage` | Which stop of §3.2 the sequence made. Its value set is closed by the token table below | Every detected failure mode: FM-1 through FM-8, and FM-11 |
| `detail.base` | The SHA step 3 resolved as the landing base | Every path on which step 3 resolved one: FM-2 through FM-8, and the success path |
| `detail.local_head` | The local `HEAD` SHA step 5's first check read before evaluating (§3.2 step 5) | Every path on which step 5 ran: FM-3 through FM-8, and the success path |
| `detail.branch_head` | The local SHA of `<branch>` read by step 5's second check, where that check is the one that refused, before step 6 would rewrite that ref (§3.2 step 5) | FM-3, and there only where the local `<branch>` is the ref whose check refused |
| `detail.prior_branch` | The branch HEAD was on before step 6 moved it onto `<branch>` (§3.3) | FM-5 through FM-8, and the success path — the paths on which step 6 completed — and there only where it found HEAD on some branch other than `<branch>` |
| `detail.git_status` | The exit status of the git invocation that failed | FM-1 through FM-7: the modes whose stop is a failed subprocess rather than a comparison |
| `detail.remote_head` | The head `ls-remote` returned for `<branch>` after the push | FM-8 and the success path; on the success path it equals `head` and is redundant rather than wrong, and on FM-8 it is the SHA that disagreed with it |

**The one emission rule, stated here and nowhere else in this document.** It
governs contract fields and `detail` keys alike. The "Established on" column is a
**ceiling as well as a floor** — exact, not a minimum. On the paths a row names,
the report carries that fact with `class: "observed"`. Off them it does not,
whatever the accumulated `facts` happen to hold: a contract field is still
present, with `value: null` and `class: "unknown"` — `files`, being a list rather
than a leaf, instead carries no entries — and a `detail` key is **absent**. Both
of those are claims, and both are assertable. The report is saying that the tool
did not establish that fact on that path, and a test written to this document may
assert it.

**Why exact and not a minimum.** A rule that let a fact the accumulated `facts`
happened to carry on an unnamed path be emitted there anyway would guard one
direction only. It rules out a report dropping a fact the tool observed — but so
does this table, once every column names every path on which its fact is
established, which is what the columns above do. What it would still permit is a
report carrying `class: "observed"` for a fact the tool never established, on a
path no column names. That is the more damaging direction for a tool whose whole
product is a provenance-labelled report, it is the direction PRD G6 exists to
rule out, and no criterion written to this document could catch it: a test
allowed to assert only what is present can never catch what should not be there.
Exactness makes both directions testable, and the way exactness itself fails is
the recoverable one — a row that under-names its paths is a one-line correction
here, and it is the correction the test exactness licenses will demand.

What that costs falls on this table rather than on the implementation, and is
stated as a constraint on the table: **no row's column may under-name the paths
on which its fact is established.** A column that does is a defect here, to be
fixed here, and never a permission to emit past it.

**Why the success-path entries read as they do.** `stage`, `branch_head`, and
`git_status` record where the sequence stopped, which is why no row names the
success path for them. Three of the remaining four rows name it without a
condition: `base` and `local_head` because the steps that establish them run on
every path that gets past them, and `remote_head` because step 10's read runs on
the success path too. The fourth, `prior_branch`, names it under one, because the
mutation it records — one §3.3 decides the tool is permitted to make — is not one
every successful landing performs: where step 6 found HEAD already on `<branch>`
it moved HEAD off nothing and there is no prior branch to name. That is the
ordinary second landing of a session that used the tool for its first, which §3.3
designs for, and the row's condition is what excludes it.

**The permitted `detail.stage` values.** `stage` is the one field a machine
reader branches on to interpret a failure report, so its value set is closed
rather than open text. One token per stop the sequence can make — which is one
per step of §3.2 at which it can stop, except at step 8, which carries two:

| Token | §3.2 step it names | Failure modes reaching it |
| --- | --- | --- |
| `fetch` | 2, fetch | FM-1 |
| `resolve` | 3, resolve the base from the remote | FM-1's class, where the remote read is what failed; and FM-11, where it succeeded and named no base |
| `base-object` | 4, confirm the base object is present locally | FM-2 |
| `guard` | 5, divergence guard | FM-3 |
| `base` | 6, establish the base | FM-4 |
| `stage` | 7, stage | FM-5, where a named path does not exist and `git add` refuses |
| `nothing-staged` | 8, commit | FM-5, where the staged set is empty and there is nothing to commit |
| `commit` | 8, commit | FM-6 |
| `push` | 9, push | FM-7 |
| `verify` | 10, verify | FM-8 |

Ten tokens and no others. Two readings the table is meant to foreclose:
`detail.stage` is one field carrying one value on any report, so FM-5's two
tokens are two paths and not two steps one failure passed through — the token
`stage` and the step named "Stage" being otherwise easy to conflate; and
`base-object` is step 4's own token rather than step 3's, so a report from the
step-4 refusal no longer says `resolve` and name a step that succeeded.

**Why the set was reopened from nine to ten.** It closed at nine with `commit`
serving both FM-5's empty staged set and FM-6's hook refusal, and it is reopened
here deliberately rather than drifting. The reason is the consumer. This report is
read by an agent session; attempting a landing with nothing staged is not a rare
state for such a session to reach; and a hook refusing a commit and a commit with
nothing in it are different situations that session must answer differently — one
is a policy rejection to be repaired in the content, the other is an empty landing
to be repaired in what was staged. `detail.stage` is the field that reader
branches on, so a token serving both leaves the branch it exists for unmade. Step
8 is therefore the one step with two tokens, and the token rather than the step
number is what a reader keys on.

Steps 1 and 11 have no token, deliberately. A usage error emits no report at all
(§3.2 step 11), so there is nothing to label; step 11 is where the report is
written rather than a place the sequence can halt.

This reconciles the two requirements without either being weakened.
AC-LAND-07's presence-and-labelling test is unaffected: it asserts the five,
and the five are there. AC-LAND-09's requirement that failure output name what
was established and what was not is served twice over — by `detail`, and by the
`unknown` class on every contract field that was not established. G6's wording
is "The report carries five fields", not "only five", which cycle-4 O3 already
notes and which AC-LAND-09 already licenses (*observed*). Whether Dave wants
G6 amended to say so explicitly is OQ-3; the format above is correct under
either disposition.

### 5.4 The mechanical-parse test

Named here as AC-LAND-07 defers it. These are TRD-stage criteria; they are
proposed for the derived acceptance-criteria artifact and are not an amendment
to PRD §6.

- **AC-LAND-T01 — the report parses mechanically, on every terminal path the
  sequence reaches.**

  **The unit is the terminal path, not the failure mode.** A terminal path is one
  end state of §3.2's sequence, individuated by the report §5.3 gives it. The
  success path and each detected failure mode contribute one such path, and
  contribute more than one wherever §5.3 makes the report depend on state
  *within* the mode. Two things do that, and only two:

  - a **conditional row** in §5.3's key table — `detail.branch_head`, established
    on FM-3 "there only where the local `<branch>` is the ref whose check
    refused", and `detail.prior_branch`, established "there only where it found
    HEAD on some branch other than `<branch>`" — splits its mode into the path
    where the row's condition holds and the path where it does not, and the two
    carry different `detail` key sets;
  - a **conditional token** — §5.3's token table giving one mode two tokens, as it
    gives FM-1 `fetch` or `resolve` and FM-5 `stage` or `nothing-staged` — splits
    its mode into one path per token, and the two carry different values of
    `detail.stage`.

  A mode carrying both is split by both, one path per combination. Nothing else
  splits a mode: two states that differ only in the *value* of a field they both
  establish — a `prior_head` reading `created` rather than a SHA — are one
  terminal path, because the established set and the report's shape are the same
  on each.

  **The enumeration follows from those two tables and comes to nineteen cases**:
  two on the success path, and two on each of FM-6, FM-7 and FM-8, on the
  `prior_branch` condition; two on FM-1, on its token; two on FM-3, on the
  `branch_head` condition; four on FM-5, which carries a token split and the
  `prior_branch` condition both; and one each on FM-2, FM-4 and FM-11, which
  carry neither. Two terminal paths are outside it. **FM-10** — an invocation
  killed mid-sequence — is not detected and emits nothing by construction, so it
  is not a case this criterion can be written against; and the usage-error path
  emits no report either, what it does emit being AC-LAND-T01a's.

  **The boundary is end to end.** Each case is a real invocation of `bin/land`
  over the §4.1 substrate, and the stdout asserted on is the process's. Two of
  the assertions below can be made no other way: that stdout carries no text
  outside the object is a claim about what the tool writes, which no call to
  `Report.build` can make; and AC-LAND-T02 binds exit status to `verification`
  across this same enumeration, and an exit status exists only where a process
  ran. §3.1 and §3.7 state the separate property the `land.py`/`report.py` split
  buys — that every report shape is constructible from synthetic facts without a
  landing — as an architectural one, and it is not this criterion's boundary.
  With the per-file mismatch mode struck (§6), every one of the nineteen is
  reachable end to end; reaching all of them needs three things the plain
  substrate does not supply, and none of the three is left implicit. FM-6's two
  cases need a `pre-commit` hook
  installed into the substrate repository that refuses the commit, and that hook
  is a stand-in rather than this repository's own, which §4.2's B5 leaves
  **assumed** and which this criterion does not upgrade. FM-1's `resolve` case
  needs a remote read that fails after a fetch that succeeded, which one bare
  repository cannot produce on its own; it is induced with a `git` shim on a
  temporary `PATH`, in the manner §4.2's B2 already uses `fake_path_dir`, so that
  one case is mock-verified rather than exercised against the transport. FM-7's
  two cases need a push git rejects, and the §4.1 substrate is a bare repository
  that accepts the pushes it is given; the rejection is induced with a
  `pre-receive` hook installed into that bare repository, which refuses **during**
  the push. That is a different helper from the mutation between push and
  verification §4.1 also provides: the mutation is FM-8's inducement and lands
  after receive-pack has already answered. What the induced rejection carries is
  the same limit the hook stand-in carries at FM-6, on the other boundary: §4.2's
  B1 lists provider-side ref policies — protected branches, push rules — among
  what the `file://` substrate does not prove, and a `pre-receive` hook the suite
  itself owns is a stand-in for exactly that class. It exercises git's
  push-refusal contract and the tool's conduct on that path, and represents
  nothing about how a real provider refuses a push, so B1's evidence class is
  what it was and this criterion does not upgrade it either.

  **What each case asserts.** The tool's **stdout** parses with `json.loads`
  without error; the parsed value is an object; its keys are exactly `branch`,
  `head`, `prior_head`, `files`, `verification`, `detail`; every leaf object
  carries a `class` in `{"observed", "unknown"}` and exactly the keys §5.2 closes
  it at — `value` and `class`, or, in a `files` entry, `path`, `match` and
  `class`; every leaf whose `class` is `"unknown"` has `value` of `null`, or, in
  a `files` entry, `match` of `null`, that being the one leaf shape whose
  established value is not named `value` (§5.2); §5.2's value-domain rules hold;
  and stdout carries no text outside that object. For each case the report also
  carries every field and `detail` key §5.3's table establishes on that path,
  each with the class and the value shape that table states for it —
  `detail.stage` with the token §5.3's token table assigns to that terminal path,
  and `files` with the entries the key table gives it, so what §5.3 states is
  tested rather than only written down. The criterion asserts the exact set
  rather than a minimum, because §5.3's column is exact: each case also asserts
  that every contract field the table does not establish on that path carries
  `value: null` with `class: "unknown"` — or, for `files`, no entries — and that
  the keys of `detail` are exactly the `detail` keys the table establishes there,
  with none beyond them. Enumerating the failure paths is what makes this a real
  test rather than a test of the success path: the format's whole burden is that
  a failed landing is still machine-readable.

- **AC-LAND-T01a — the usage-error path emits no report.** Given an invocation
  `argparse` rejects, stdout is empty, stderr is non-empty, and the exit status
  is 2 (§3.2 step 11, §7). Stated as its own case rather than folded into T01
  because the property under test is the opposite one — that nothing is written
  to stdout — and a criterion asserting both shapes at once would be satisfied by
  either.

- **AC-LAND-T01b — every refusal carries the code §7 names, and a successful
  landing carries none.** Across T01's enumeration: on each of the seventeen
  refusal terminal paths, stderr carries the bracketed code §7's table assigns to
  that refusal, extracted with `bin/tests/helpers.py`'s existing `bracket_codes`
  (*observed*) — the helper whose form §7 pins the codes to — and on
  the two success paths the tool emits no diagnostic of its own and stderr
  carries no bracketed code at all.

  Where §7's table is coarser than this enumeration — the five
  `detail.prior_branch` pairs, which §7 states and gives its reason for — both
  members of a pair assert the same code. So what a case asserts is that stderr
  carries the code its own row names, never that a code appears on one path
  alone.

  Stated as its own criterion rather than folded into T01 because the stream is
  the other one: T01's assertions are about stdout throughout, and its boundary
  paragraph is written about what the process writes there. What makes this
  assertable at all is §7 fixing the codes. Before that a criterion could have
  asserted only that *some* bracketed code was present, which is the state OQ-12
  named and §9 records as closed — and a criterion asserting presence alone would
  have passed two implementations whose codes disagreed, which is the whole of
  what was wrong with it.

- **AC-LAND-T02 — `verification` and exit status agree.** Across T01's
  enumeration, exit status is 0 if and only if `verification.value` is
  `"complete"`. This is AC-LAND-08 read through the serialization, and it is
  what stops the report and the exit code from drifting apart.

- **AC-LAND-T03 — the guard refuses when the named branch, not local HEAD, is
  what diverges.** Given a repository in which the local `<branch>` exists and
  carries at least one commit the base does not, with local HEAD on some other
  branch and at or behind the base: the invocation stops before anything is
  staged, in FM-3's shape — `detail.stage` is `guard`, `detail.branch_head`
  carries the tip `<branch>` held before the invocation, no ref has moved, no
  commit exists, and the exit status is 3 — and that prior tip is still reachable
  from `<branch>` afterwards. Stated as its own case because §3.2 step 5's second
  check is induced by no PRD criterion: AC-LAND-01c requires every local-only
  commit to remain reachable **from local HEAD**, which does not describe this
  state, where the commits are on `<branch>` and HEAD is elsewhere, so a test
  written to that criterion's given exercises the first check only. §3.3 calls
  the second check the only thing standing between the ordinary post-checkout
  tree state and the destructive class PRD §7 puts under "Not accepted"; this is
  the criterion that keeps it from shipping unverified.

## 6. Failure modes and recovery

Recovery is uniform and stated once: **there is none inside the tool.** It
never retries, never force-pushes, never deletes a ref, never merges, and never
undoes its own local commit — undoing would be a destructive operation it does
not offer. Every failure is handed to the invoking session, which stops and
surfaces. This is PRD G7 and PRD §7's escalation clause (*observed*).

What the user — an execution session — sees on every one of these: the report
of §5 on stdout with the established fields labelled `observed` and the
unestablished ones labelled `unknown`, a bracket-coded diagnostic on stderr
carrying the code §7's table assigns to that refusal, and a non-zero exit. Which
code that is, is §7's to state and not this section's; no cell below names one.

**The last column, one rule.** The cells are **derived from §5.3's key table**,
not authored beside it. Each names, for the path its failure mode reaches, the
contract fields and `detail` keys §5.3's table establishes there — exhaustively,
so the row can be read whole — and it names them because that table does. That
table's column is exact rather than a minimum, so the derived set is exact too: a
cell names every field and key established on its path and no others. The
`detail.stage` column is derived the same way, from §5.3's token assignment.
§5.3 is normative: where a cell and that table disagree, the cell is wrong. No
cell states an emission rule of its own, and what a key's absence from a cell
means is §5.3's to state and not this section's.

Nothing is thereby missing from the report: §5.2 fixes the key set on every path,
and §5.3 states what a field or key a cell does not name carries, or whether it
is present at all. `detail.stage` is established on every detected mode and has
its own column, so it is not repeated in the last one.

| # | Failure mode | Detected by | `detail.stage` | Established at that point |
| --- | --- | --- | --- | --- |
| FM-1 | A remote read fails — no network, no such remote, auth refused | `git fetch` or step 3's `git ls-remote` exit status | `fetch` / `resolve` | `branch`, and no other contract field: the read that would have established them is the one that failed. `detail.git_status`. |
| FM-2 | The base object is not present locally (§3.2 step 4 names the candidate causes; the tool asserts none of them) | `git cat-file -e` | `base-object` | `branch`, `prior_head`. `detail.base`, `detail.git_status`. |
| FM-3 | **Divergence refusal, before staging** — local HEAD, or the local `<branch>` the sequence would rewrite, carries a commit the base does not | either `merge-base --is-ancestor` non-zero (§3.2 step 5) | `guard` | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.branch_head` where the local `<branch>` is the ref whose check refused. Nothing staged, no ref moved, no commit made. |
| FM-4 | Base establishment fails — a locally-modified file differs between old HEAD and base | `git checkout -B` exit status | `base` | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`. Step 6 is the step that failed, so no ref moved and HEAD stayed where it was. |
| FM-5 | Nothing to commit — a named path does not exist, or the staged set is empty | `git add` / `git commit` exit status | `stage` or `nothing-staged` — one field, one value (§5.3) | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. No commit exists. |
| FM-6 | A repository hook refuses the commit | `git commit` exit status | `commit` | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. No commit exists. |
| FM-7 | Push fails | `git push` exit status | `push` | `branch`, `prior_head`, `head` — the **local** commit's SHA, `observed` — `verification`, the value `incomplete`, and `files`, carrying one entry per path in the commit with `match: null` and `class: "unknown"` (§5.3). `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. |
| FM-8 | `ls-remote` disagrees with the pushed head | Comparison at step 10 | `verify` | `branch`, `prior_head`, `head`, `verification` — the value `incomplete` — and `files`, carrying one entry per path in the commit with `match: null` and `class: "unknown"` (§5.3). `detail.base`, `detail.local_head`, `detail.remote_head`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. |
| FM-10 | The invocation is killed mid-sequence | Not detected by the tool | — | Nothing: no report is emitted, so there is no field for the column to be about. See §3.2 step 11's second bullet and OQ-4. |
| FM-11 | **The remote read succeeds and names no base** — neither `<branch>` nor `main` is present at the remote, so the branch-absent arm has nothing to resolve a base from | Step 3's `ls-remote` exits 0 having returned no line for either ref | `resolve` | `branch`, and `prior_head` — the literal `created`, step 3 having observed that `<branch>` is absent at the remote (§3.2 step 3). Nothing further: no base was resolved, no ref moved, nothing was staged, no commit was made. |

**A mode was struck, and the numbering keeps its hole.** FM-9, which read "a
per-file blob comparison mismatches", is struck as unreachable. The rows below it
do **not** move up: FM-10 and FM-11 keep the numbers they have always had, and
the sequence runs FM-1 through FM-8, then FM-10, then FM-11, with nothing at 9.
Dave authorised a renumbering for this change; the authorisation was offered and
is deliberately unused, because closing the gap would buy contiguity at the price
of making two identifiers mean something they did not mean before, and a reader
arriving from a review artifact or a directive that cites FM-10 or FM-11 by
number would then read the wrong row without any signal that it had happened. The
hole costs a reader one moment of "where is 9", which this paragraph answers, and
it costs nothing else. It is the same instinct §9 follows in keeping a retired
`OQ-n` in place rather than reusing the identifier: a number that has meant one
thing does not get to mean another.

**Why the struck mode was unreachable.** Step 10 runs the `ls-remote` head check
before the per-file comparison and runs the comparison only where that check
passed (§3.2 step 10), and §4.3 gives the argument that under git's content
addressing the comparison cannot fail where the check passed (*inferred*). A
remote whose content is mutated between the push and the verification therefore
answers the head check with a different SHA and stops there: it surfaces as FM-8,
and never as a per-file mismatch.

That is also what keeps two commitments from being orphaned by the strike. PRD §5
measures the content-verification outcome by "a test that mutates the pushed
content and asserts the tool exits non-zero" (*observed*); under git transport
that mutation lands on the FM-8 path, which exits 4 (§7), so the mechanism still
bites. AC-LAND-06 requires that "[w]here any file differs, the invocation exits
non-zero and names that file" (*observed*); its exit branch is met exactly, and
its naming branch is met in the only form a stop at the head check can produce —
the report names every path in the commit, in the shape §5.3's table gives FM-8,
rather than singling out one path as the differing one. The reason it can produce
no stronger form is §4.3's and is recorded there rather than softened here: the
comparison that would single a path out is arithmetically unreachable, not
omitted.

**The strike is scoped to the verification the tool performs today**, and settles
nothing beyond it. The struck mode's unreachability follows from AC-LAND-06 as
agreed — a blob-SHA comparison against the commit fetched back from the remote —
and not from §4.3's fetched-bytes question being answered. OQ-6 stays open
exactly as §9 states it. A resolution of OQ-6 that adopted the stronger
comparison — the bytes fetched back against the bytes of the named file on disk —
would give step 10 a check that does not reduce to commit-SHA equality, and a
failure mode of the struck kind would become reachable again and would have to be
enumerated here.
The strike removes an unreachable row; it does not stand in the way of that.

FM-11 is appended rather than inserted at the step it belongs to. Its stage is
step 3's, so by sequence it sits beside FM-1; the existing numbers are cited by
number in this document's review artifacts and in the directives that produced
them, and moving them to restore sequence order would strand those citations —
the same cost the paragraph above declines to pay for contiguity, declined again
here for the same reason. The out-of-order row is the cheaper of the two costs.

It is a distinct mode rather than a case of FM-1: FM-1 is a read that failed, and
this is a read that succeeded. Step 3's own text establishes that the state is
reachable — "A pattern matching nothing is not an error and does not change the
exit status" — so a remote with neither ref present yields exit 0 and empty
output, and the base `main`'s head would have supplied does not exist for step 4
to confirm. §3.5 declares `origin` to be whatever the invoking repository has
configured and asserts nothing further about it, so nothing in the design
excludes such a remote.

Two of these need more than a row.

**FM-3 is the pre-staging refusal path, and it is a first-class failure mode
here.** `reviews/bin-land-cycle-4.md` O2 records that PRD §3's J3 trigger —
"any step fails, or verification does not establish a match" — does not reach
it, because no step failed and verification was never attempted (*observed*).
That is a PRD-side documentation gap, held out of scope by Dave; this section
does not depend on it. FM-3 is detected, reported, and tested regardless, and
AC-LAND-01c already states the behaviour directly (*observed*). It is one failure
mode reached by either of §3.2 step 5's two checks: the second check exists
because local HEAD is not the ref step 6 rewrites, and a refusal it produces is
FM-3 in the same shape, not a mode of its own. Whether J3's
trigger should enumerate it is a question for the PRD and is not resolved here;
cycle-4 O2's proposed three-word fix is on the record there. This document
notes only that its own §6 is complete over the failure modes the design
produces, which is what the template asks of it.

**FM-7 is the accepted risk, and it is the one that leaves residue.** PRD §7
accepts "an invocation that stops with work committed locally but not verified
at the remote", the session then being obliged to stop and surface
(*observed*). The tool leaves the local commit in place deliberately: the work
exists, it is reachable from local HEAD, and a human or a later session
resolves it. Reporting `head` as `observed` while `verification` is
`incomplete` is exactly the distinction the report format exists to carry — the
commit was observed, the landing was not. `files` carries the same distinction
one level down, in the shape §5.3's table gives this path: the paths are named
because the tool staged and committed them, and each `match` is `unknown`
because step 10 never ran. That is what lets the session handed this report see
which files sit in the local commit it is now obliged to resolve, rather than
reconstruct them from the invocation it made.

### 6.1 Detection outside the tool

There is no monitoring. Detection of a systemic problem — a sandbox whose push
never lands, a remote that has started rejecting — is the invoking session
noticing a non-zero exit and surfacing it, and
`policies/remote-write-verification-policy.md` rule 2's two-consecutive-failures
signal operating at the session level (*observed*). PRD G7 is stricter than
that rule and does not conflict with it: the tool stops at the first failure
because it never retries, so the policy's counting happens across invocations
rather than within one (*observed*, PRD §4).

## 7. Operational concerns

**Observability.** stdout carries the report and nothing else. stderr carries
human-readable diagnostics, each with a stable bracketed code — the convention
`bin/tests/helpers.py` already relies on, where "tests assert on codes, never on
English wording, so that rewording a message does not break the suite"
(*observed*). Which code a given refusal carries is the table below. Exit status
is the third channel. Nothing else is emitted anywhere; there is no log file and
no telemetry sink (§2).

**The diagnostic codes — this document's single statement of which refusal
carries which code.** No other passage in this document assigns a code, and none
may: §6 says that a refusal puts a bracket-coded diagnostic on stderr and reads
which code off this table, and §5.4's AC-LAND-T01b asserts the code this table
names. Where any other passage and this table disagree, this table is normative
and the other passage is wrong. Every code matches the form
`bin/tests/helpers.py` already pins — a lowercase letter, then lowercase
alphanumerics and hyphens, inside square brackets (*observed*, its
`BRACKET_CODE_RE`) — so the `bracket_codes` helper the suite already has reads
them without amendment. Fixing them here rather than leaving the strings to the
implementer is OQ-12's answer; §9 records the reasoning and retires the
identifier.

| Code | The situation it names | `detail.stage` | Failure mode |
| --- | --- | --- | --- |
| `fetch-failed` | Step 2's fetch did not complete | `fetch` | FM-1 |
| `remote-read-failed` | Step 3's read of the remote failed | `resolve` | FM-1 |
| `no-base-at-remote` | Step 3's read succeeded and named neither `<branch>` nor `main` | `resolve` | FM-11 |
| `base-object-missing` | The resolved base is not present in the local object database | `base-object` | FM-2 |
| `head-diverged` | Local HEAD carries a commit the base does not | `guard` | FM-3, first check |
| `branch-diverged` | The local `<branch>` carries a commit the base does not, and it is the ref step 6 would have rewritten | `guard` | FM-3, second check |
| `base-checkout-failed` | Step 6 could not put `<branch>` at the base | `base` | FM-4 |
| `path-not-found` | A named path does not exist and `git add` refused it | `stage` | FM-5 |
| `nothing-staged` | The staged set is empty and there is nothing to commit | `nothing-staged` | FM-5 |
| `commit-refused` | A repository hook refused the commit | `commit` | FM-6 |
| `push-rejected` | Step 9's push was rejected | `push` | FM-7 |
| `remote-head-mismatch` | `ls-remote` disagreed with the head the push wrote | `verify` | FM-8 |

Twelve codes, and no others. A reader counting them against §5.4's nineteen
terminal paths meets two differences, and both are decisions stated here rather
than gaps to be discovered.

**The rule the set follows.** One code per situation a session must answer
differently — which is what makes a code worth matching on rather than a second
spelling of `detail.stage`. A situation is what caused the refusal. Facts about
the state the refusal left behind are the report's to carry, under §5.3's table,
and are not codes. That one rule makes the set finer than §5.3's token table in
two places and coarser than §5.4's enumeration in five.

**A successful landing emits no diagnostic and therefore no code.** Two of
§5.4's nineteen terminal paths are the success path's, and the diagnostic §6
describes is stated for refusals. So the table above is the seventeen refusal
paths', and carries no row for a landing that worked: there is no situation to
answer.

**Five pairs of refusal paths share a code, and the coarseness is deliberate.**
Ten of the seventeen fall into five pairs under §5.4's `detail.prior_branch`
condition — FM-5 on each of its two tokens, and FM-6, FM-7 and FM-8 — each pair
being one path on which step 6 moved HEAD off another branch and one on which it
found HEAD already on `<branch>`. Those ten yield five codes, the remaining seven
paths one each, and that is the twelve. The
two members of each pair carry the same code, because that condition is not a
cause. It records a side effect of a step that **succeeded**: step 6 moved HEAD,
and then something else failed. It is the same move a successful landing makes,
on a path that emits no code at all, so a code splitting on it would speak
loudest exactly where the tool is silent. `detail.stage` does not split on it
either — §5.3's token table gives one token per stop, and no conditional row
produces one — so a code that did would be finer than its stdout peer on an axis
that is not about where the sequence stopped. And the repair is the same on both
members of every pair: fix the path argument, stage something, repair what the
hook rejected, or stop and surface the local commit. Nothing is lost by the
sharing, because the fact itself is carried: §5.3's table puts
`detail.prior_branch` on exactly those paths, and its emission rule makes the
key's absence as much a claim as its presence. The report carries the fact; the
code names the situation.

**Two codes are finer than the token that serves them, by the same rule.** Both
splits discriminate a cause. `resolve` serves two modes: FM-1, where step 3's
read of the remote failed, and FM-11, where it succeeded and named neither ref. A
session answers those differently — a remote it could not reach, against a remote
it reached and found empty of both — and `detail.stage` alone does not separate
them. `guard` serves FM-3's two checks: local HEAD carrying a commit the base
does not, against the local `<branch>` carrying one, which §3.3 calls the only
thing standing between the ordinary post-checkout tree state and the destructive
class PRD §7 puts under "Not accepted". Two different refs, two different
repairs. In both cases the report can separate the pair already — by whether
`detail.git_status` is present at `resolve`, and whether `detail.branch_head` is
present at `guard` — and the code says outright what would otherwise be inferred
from a key's absence. That is the difference from the five shared pairs, and it
is not that one fact is in the report and the other is not: both are. It is that
these two are causes and `prior_branch` is not.

**Exit codes.** `aimeta/cli.py` defines `EXIT_OK=0`, `EXIT_POLICY=1`,
`EXIT_USAGE=2`, `EXIT_PRECONDITION=3`, `EXIT_SELF_VERIFY=4`, and
`bin/tests/helpers.py` pins `DOCUMENTED_EXIT_CODES = (0, 1, 2, 3, 4)`
(*observed*). Proposed mapping:

| Code | Used for |
| --- | --- |
| 0 | Full verification (AC-LAND-08) |
| 2 | Usage error; also the outside-a-repo case AC-X-4 permits as 2 or 3 |
| 3 | FM-1 through FM-6, and FM-11 — every precondition that stops the sequence before a write |
| 1 | FM-7 — a write the tool attempted and git rejected |
| 4 | FM-8 — the tool's own verification of its own write failed, which is exactly what `EXIT_SELF_VERIFY` already means for `bin/flip-agreed` |

Code 1's constant is named `EXIT_POLICY`, which fits this tool's use of it
poorly, and **the mapping stands anyway**. A distinct code for a failed remote
write was considered and is not added: a caller that must tell that failure from
the others has a better source than an integer, because the report on that path
already says where the sequence stopped and what git returned, under §5.3's
table, and says it in a form a machine reads. Giving one mode of ten a code of
its own is an asymmetry besides, and an asymmetry wants a caller demanding it;
none does, and adding one would change `DOCUMENTED_EXIT_CODES`, which every CLI's
tests read. OQ-10 asked this question; §9 records the answer and retires the
identifier.

**Configuration and secrets.** None. The tool reads no configuration file and
introduces no environment variable of its own. It sets `GIT_TERMINAL_PROMPT=0`
on its git subprocesses so that a missing or rejected credential fails fast
rather than blocking on a prompt no agent session can answer; this is a
decision, and `bin/tests/helpers.py` already sets the same variable in its test
environment (*observed*). It never reads, writes, displays, or logs a
credential.

**Quotas and billing exposure.** N/A. No metered service is called.

**Deployment assumptions.** The tool is a file in `bin/`, executable, with a
`python3` shebang. There is no build, no package, no install step. It is
present in a clone or it is not.

**Release model — deploy and release are separate events.**

- **Deploy** is the commit landing on `main`: the file exists in the repository
  and anyone reading the tree can run it.
- **Release** is the first directive instructing an executor to invoke it —
  which PRD §8 defines as the moment the tool "becomes agent-facing"
  (*observed*).
- **The release decision sits after deploy and is Dave's**, and it is gated:
  PRD §8 records his sequencing decision that a governed standing write-path
  document must be agreed before that first directive (*observed*).
- Implementation may proceed before that document exists, under the
  build-gating rule in `policies/document-metadata-policy.md` (*observed*, PRD
  §8). That rule attaches a condition — explicit per-task human confirmation
  while the spec's status is `draft` — which `reviews/bin-land-cycle-7.md` F1
  records as unnamed in PRD §8 and which is Dave's to dispose of (*observed*).
  This document does not restate the permission without the condition: an
  executor building `bin/land` while either spec is `draft` needs that
  confirmation.
- **Flag mechanism: none, and none is needed.** Separating deploy from release
  usually needs a flag backend because the deployed code is reachable by users
  the moment it ships. Here it is not: `bin/land` has no runtime exposure to
  gate. Nothing invokes it but a directive, so the gate is the absence of such
  a directive, and it is documentary rather than technical. No flag backend is
  chosen, and there is nothing to make swappable. If a future change gave the
  tool an automatic trigger — a hook, a scheduled run — this paragraph would
  stop being true and a real gate would be needed. Naming no flag backend is a
  **departure** from `specs/trd-template.md` §7, which requires one; the
  departure is deliberate rather than an oversight, and Dave accepted it at
  cycle 1, recorded in
  `docs/cycles/bin-land-trd-1-20260823T221914Z.md` @ `3de6098b`.

**Operating it responsibly.** Three standing obligations follow from §4. B1's
contract-verified class means the change package for the implementing change
should record whether a live landing was performed (OQ-7). B2's mock
representation means the static no-stderr-branching scan is the part that must
never be deleted, because it is the only half of AC-LAND-04 that cannot go
stale. And B5 is **assumed**: FM-6's report shape is exercised against a stand-in
hook and this repository's own hook is installed in no test, so either B5's
deferred-verification path is bought or that class is accepted knowingly — and
whichever it is, the boundary audit at the implementing change's release decision
is where it is said out loud rather than inherited.

## 8. Constraints, NFRs, and non-goals

The technical instantiation of PRD §4's non-functional goals, dimension by
dimension.

**Performance.** No latency target, per the PRD. The concrete constraint is
negative and enforceable: one invocation performs exactly one `fetch` for
objects, one `ls-remote` before the write, one `push`, and one `ls-remote` plus
one targeted `fetch` after it. The pre-write count is one on **both** of G1's
arms, because §3.2 step 3 reads `<branch>` and `main` in a single `ls-remote`
rather than one per arm. No sleep, no backoff, no retry loop, and no second write
on any path. Enforced by a test that records the git argv sequence
of a full invocation — over the `file://` substrate, where every git call is
observable — and asserts that `push` appears exactly once on the success path
and at most once on every failure path. That test is also what makes
AC-LAND-09's "no failure path issues a second write of any kind" testable
rather than merely asserted.

**Reliability.** No uptime target; there is nothing to be up. The reliability
property is AC-LAND-08's biconditional, tested deterministically, plus
AC-LAND-T02 binding it to the report. No error budget. No retry or fallback
strategy — deliberately, per G7.

**Scalability.** N/A. One repository, one branch, one invocation. The only
dimension that grows is the number of files in the commit, which costs one
`rev-parse` per file at verification; there is no load model because there is
no concurrent load.

**Security.** No authentication of its own; `git` authenticates and the tool
never sees the result. No credential is read, stored, displayed, or logged. The
threat surface is the argv the tool constructs: a branch name, a commit
message, or a path is caller-supplied text, so every git invocation passes
arguments as an argv list through `repo.run`'s `subprocess.run` with no shell
(*observed*, `bin/aimeta/repo.py`), and pathspecs are always separated by `--`.
No force-push, no ref deletion, no merge, and no `gh` — verifiable statically
over the source, which is what AC-LAND-10 asks for, in the manner AC-X-1 and
AC-X-2 already scan `bin/` (*observed*).

**Maintainability.** Standard library only; no third-party dependency, enforced
by AC-X-2. Two new modules rather than one, so the report format is testable
without a landing (§3.1). The existing `repo.py` and `cli.py` are reused and
not modified. The design rule the PRD states — "every sandbox workaround is a
line of code with a test, not a sentence in a directive" (*observed*) — has one
concrete instance here: G4's indifference to stderr is a static scan, not a
comment.

**Usability.** The reader is an agent. stdout is the report, small enough to
paste into an execution report whole. stderr is diagnostics. The invocation is
`bin/land <branch> <message> [files...]` with no flags and no modes.

**Observability.** As §7. Instrumented: nothing, in the telemetry sense. What
surfaces: the report, the diagnostics, the exit code.

**Portability / Compatibility.** Python 3, standard library, and `git`. No
assertion about the operating system beyond what the other seven tools already
assume. **No minimum `git` version is asserted**, and that is a decision rather
than an omission: the plumbing used is long-stable, and §9 records the decision
and retires OQ-8, which had asked whether to pin and test a floor. §4.2's B4
carries what that costs — the suite is live-verified against one `git` version
incidentally and proves nothing about another. The tool makes no assertion about
what the sandbox permits (*observed*, PRD §4).

**Compliance.** N/A. No regulatory, legal, or data-residency dimension.

### Technical non-goals

Stated so no implementer has to infer them.

- **No merge path.** Not a flag, not a code path, not an option.
- **No `gh` invocation**, for anything, including auth checks.
- **No retry, backoff, or wait** of any kind.
- **No force-push and no ref deletion.** The absence is structural, not
  guarded: there is no code path that could take those arguments.
- **No shell.** Every subprocess is an argv list.
- **No interactive prompt.** `GIT_TERMINAL_PROMPT=0`.
- **No configuration file, no state file, no cache, no log file.**
- **No parsing of git's stderr for any decision**, in either direction.
- **No inference of the branch from the checkout.** The invocation names it.
- **No judgment about whether the remote head was the expected one.** PRD G1
  assigns that to the evidence trail, not to the tool (*observed*).

### Required integration points

- `bin/tests/helpers.py`: `land` added to `CLI_NAMES`, and a `CLI_MINIMAL_ARGS`
  entry so the cross-cutting suite can drive it past `argparse` (*observed*,
  both structures exist and every CLI appears in them).
- New bare-remote helpers (§4.1).
- `bin/tests/test_land.py`, new.
- AC-X-5's containment scan — see OQ-9.

## 9. Open technical questions

Seven open, and five retired. Each open question names what would resolve it;
none is settled here. A retired identifier is kept in place rather than reused,
so a reader arriving from a review artifact that cites it by number can still
find what it referred to — the precedent PRD §8 sets for its own Q1–Q4
(*observed*), and the precedent §6 follows in leaving a hole at the struck
failure mode rather than closing it up. The five retirements differ in kind: OQ-8
is retired because the question had no closing move, and OQ-5, OQ-10, OQ-11 and
OQ-12 because they have been answered.

- **OQ-1 — No SLO exists for J1, J2, or J3.** §2 states this explicitly, as the
  template requires, and gives the structural reason: no production surface, no
  telemetry, no aggregate. *Resolved by*: Dave deciding whether any post-
  adoption signal about the tool is wanted at all and, if so, where it would be
  recorded — since it could not come from the tool, it would have to come from
  reading execution reports, which is PRD §5's mechanism rather than an SLO.

- **OQ-2 — Whether the PRD should govern the branch-absent diverged case.** What
  the tool does in that state is no longer what is open. §3.2 step 5's guard
  refuses on every route — the first check where some branch other than
  `<branch>` carries the commits, the second where the local `<branch>` does, and
  the first again where both do, the guard stopping there — so §3.4's
  uniform refusal falls out of the guard rather than resting on this document's
  proposal, and an implementer needs no disposition of this question to write the
  tool correctly. What remains open is the PRD side: G1 states its refusal inside
  the second arm only, no acceptance criterion reaches the first, and a reader of
  the PRD alone still finds the state governed by nothing (*observed*,
  `reviews/bin-land-cycle-5.md` O1). *Resolved by*: Dave's disposition of cycle-5
  O1 — either lifting G1's refusal sentence into its "In both arms" paragraph, or
  widening AC-LAND-01c's given. Both are content edits to an agreed spec, and
  neither is in this document's gift.

- **OQ-3 — Whether G6's five-field contract should say explicitly that failure
  paths may carry more.** §5.3's `detail` key is correct under either reading,
  so nothing is blocked; what is open is whether the PRD says so.
  *Resolved by*: Dave's disposition of `reviews/bin-land-cycle-4.md` O3.

- **OQ-4 — Whether G1's "print that prior head SHA in the output *before*
  landing" requires incremental output.** §5.2 emits one report on every
  terminal path, which carries the prior head whenever a step after the branch
  was resolved fails — satisfying the purpose G1 states. The residual gap is
  FM-10: a process killed mid-sequence emits nothing. Literal compliance would
  need a JSON-Lines stream — an early partial object, a final complete one —
  at the cost of a more complex parse contract. *Resolved by*: Dave's reading
  of whether G1's clause states a purpose or a mechanism.

- **OQ-5 — retired, answered.** It asked whether the tool should refuse when the
  checkout is on a branch other than the named one. **The decision is that the
  tool is permitted to move HEAD onto `<branch>`**, and reports having done so.
  Refusing would rule out J1 in every session whose worktree was not created on
  the target branch — which is the ordinary opening state, since the first
  invocation is the one that creates the branch — so the refusal would cost the
  journey the tool exists to serve in order to avoid a mutation the session can
  simply be told about. The residue the question named is real and is now carried
  in the output rather than only in this document: the report names the branch
  HEAD was moved off, on the paths §5.3's table states (§3.3). That the move
  loses no commit remains a property of §3.2 step 5's guard and never was one of
  `checkout -B`.

  The identifier is retired rather than reused, on the same footing as OQ-8, so a
  reader arriving from a review artifact that cites OQ-5 by number can still find
  what it referred to.

- **OQ-6 — Whether PRD G5's stated purpose is achieved by AC-LAND-06 as
  written.** G5 states that the goal "is what closes the gap
  `policies/remote-write-verification-policy.md` names as open" (*observed*).
  §4.3 gives the argument that it does not: under git transport AC-LAND-06's
  comparison adds nothing to the `ls-remote` check, and the gap's failure class —
  whose git analogue is a mis-staged file — passes that comparison. The form that
  would catch it compares fetched bytes against the named file on disk. This is
  not an optional strengthening but the question the goal depends on, which is
  why it is ranked here rather than as a refinement. *Resolved by*: Dave deciding
  whether AC-LAND-06 changes — a content edit to an agreed spec, which flips
  `specs/bin-land.md` to `in-review` and takes its own reviewer cycle. Until then
  this document specifies AC-LAND-06 as agreed and says plainly what that leaves
  unclosed.

- **OQ-7 — Whether a live landing against the real `origin` is required before
  release, and on what cadence B1's deferred verification re-runs.** §4.2
  proposes one, recorded in the implementing change's package.
  *Resolved by*: the boundary audit at that change's release decision, under
  `policies/verification-boundary-policy.md`.

- **OQ-8 — retired, not answered.** It asked whether a minimum `git` version is
  pinned and tested. **The decision is that no minimum `git` version is
  asserted**, and the reason is on the record rather than left to be inferred.
  The resolver OQ-8 named was establishing the oldest `git` any target
  environment supplies, and that is not this repository's to establish: the
  sandbox runner is supplied from outside it, which PRD §4's non-goals already
  treat as a variance to survive rather than control (*observed*). So the
  question had no closing move and would have stood open at every future cycle —
  which is a different thing from an open question. The plumbing §3.2 relies on —
  `ls-remote --heads`, `merge-base --is-ancestor`, `cat-file -e <rev>^{commit}`,
  `checkout -B`, `reset --mixed`, and `rev-parse` in its `<rev>`,
  `--verify --quiet <rev>` and `<rev>:<path>` forms — is long-stable,
  and §4.2's B4 states the residual honestly: the suite is live-verified against
  one `git` version incidentally and proves nothing about another. If a floor
  ever becomes load-bearing, the evidence will be a failure observed on a real
  runner, and that opens a new question rather than reopens this one.

  The identifier is retired rather than reused, so a reader of
  `reviews/bin-land-trd-cycle-1.md`, whose O3 is about OQ-8 by that number, can
  still find what it referred to.

- **OQ-9 — How AC-X-5's containment scan accommodates a tool that writes to a
  remote.** That criterion asserts "no tool writes outside the invoking repo"
  (*observed*, `bin/tests/test_cross_cutting.py`), and `bin/land` is the first
  tool in `bin/` that deliberately writes somewhere else — to a bare repository
  outside the temp repo, under the §4.1 substrate. *Resolved by*: deciding
  whether the scan's scope is amended to exempt a declared remote, or whether
  `bin/land` is excluded from that scan with the exclusion itself asserted.

- **OQ-10 — retired, answered.** It asked whether a failed remote write should
  get an exit code of its own, §7 mapping FM-7 onto `1`, whose constant is named
  `EXIT_POLICY`. **The decision is that no code is added and FM-7 keeps `1`.**
  Two reasons, and the first carries the weight: a caller that must distinguish a
  failed remote write from the other failures has a better source than an
  integer, because the report on that path already names the failure precisely —
  where the sequence stopped and what git returned — and names it in the machine-
  readable form the report exists to provide. One integer spanning the whole of
  §7's mapping was never going to carry that discrimination; the report is the
  channel that does. The second reason is proportion: giving one mode of
  ten a code of its own is an asymmetry, an asymmetry wants a caller demanding
  it, and no caller does. The name `EXIT_POLICY` still fits this use poorly, and
  that is the cost being accepted rather than a defect being overlooked. If a
  caller ever demands the distinction, adding a code then changes
  `DOCUMENTED_EXIT_CODES` and the tests that read it and changes nothing about
  the report — which is a cheaper thing to do late than to undo, and is why the
  asymmetry is not bought in advance.

  The identifier is retired rather than reused, on the same footing as OQ-5 and
  OQ-8, so a reader arriving from a review artifact that cites OQ-10 by number
  can still find what it referred to.

- **OQ-11 — retired, answered.** It asked whether a non-ASCII character in a
  report value is serialized as UTF-8 or as a `\uXXXX` escape. **The decision is
  that it is escaped**: the report is serialized with `ensure_ascii=True`, so
  stdout is pure ASCII whatever any value carries, and §5.2 now states that as a
  rule beside its other value-domain rules. The reason is not readability — that
  is the one thing pulling the other way, and the raw form wins it. It is that a
  script's stdout must not depend on the ambient locale being UTF-8. The raw form
  has failure modes the escaped form does not: a locale that is not UTF-8 can
  mangle the bytes on the way out, or the write can fail outright. The escaped
  form has no such branch in any environment and no failure mode of its own to
  set against them, and nothing is given up for it, because both forms parse to
  identical data. What it costs is a reader meeting a six-character escape where
  the raw form would have shown the character itself, in a value that is
  caller-supplied text either way; what it buys is a stdout with no environmental
  branch in it at all.

  The state the question named is reachable rather than hypothetical — `branch`
  and each `files` entry's `path` are caller-supplied text — which is why the
  encoding is fixed here rather than left to whichever default an implementer's
  serializer happens to carry. And closing it buys what the question said it
  would: the encoding is now asserted, so a criterion written to this document
  may assert stdout's bytes and not only what `json.loads` returns.

  The identifier is retired rather than reused, on the same footing as OQ-5,
  OQ-8 and OQ-10, so a reader arriving from a review artifact that cites OQ-11 by
  number can still find what it referred to.

- **OQ-12 — retired, answered.** It asked whether §7 fixes the bracketed
  diagnostic codes or leaves the strings to the implementer. **The decision is
  that §7 fixes them**, and it now carries the table as this document's single
  statement of which refusal carries which code. The reason is who reads them.
  This report's consumer is an agent session, and the bracketed code is the most
  prominent thing on stderr it can match on — the one token in a human-readable
  line that is not English wording, which is why the suite's own convention keys
  on it. A code set invented by whoever writes the tool and written down
  afterwards is an interface nobody agreed to: it would be load-bearing for every
  session that read it and settled by no one, and the first change to it would
  break callers who had no way to know they were callers. §7 requiring "a stable
  bracketed code" while naming none left exactly that — stability promised over
  content nobody had fixed — which is what made this a question rather than a
  refinement. Two implementations could have satisfied every word of this
  document while emitting different codes for the same stop, and no criterion
  written to it could have told them apart.

  **The set is twelve codes over seventeen refusal paths, and the coarseness is
  part of the answer rather than a shortfall against it.** Two of §5.4's nineteen
  terminal paths are the success path's and carry no code, there being no
  situation to answer. Ten of the seventeen refusals fall into five pairs under
  the `detail.prior_branch` condition, and the members of each pair share a code:
  that condition records a side effect of a step that succeeded rather than a
  cause of the refusal, the session's repair is the same on both members, and the
  fact itself is carried on stdout by `detail.prior_branch`, whose absence
  §5.3's emission rule makes as much a claim as its presence. The set is finer
  than §5.3's token table in the two places where one token serves two causes —
  `resolve` for FM-1 and FM-11, `guard` for FM-3's two checks — which is the same
  rule read the other way round: one code per situation a session must answer
  differently, and none per fact the report already carries. §7 states the rule
  and the table; this entry records that the fineness and the coarseness were
  both decided, so that a later reader counting nineteen paths against twelve
  codes finds an answer rather than a defect. What closing this buys a criterion
  is AC-LAND-T01b, which asserts the code on each refusal path and asserts that
  the success paths carry none.

  The identifier is retired rather than reused, on the same footing as OQ-5,
  OQ-8, OQ-10 and OQ-11, so a reader arriving from a review artifact that cites
  OQ-12 by number can still find what it referred to.
