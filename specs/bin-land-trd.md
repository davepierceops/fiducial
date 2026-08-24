---
status: draft
last-reviewed: null
audience: [all-roles, human]
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

The split between `land.py` and `report.py` exists so that the mechanical-parse
test (§5, AC-LAND-T01) can construct every report shape — including every
failure shape — without performing a landing. What each exposes to the others is
§3.7; it is stated at the end of this section rather than here so that §3.2's
step numbering, which the rest of this document and its review artifacts cite by
number, is not disturbed.

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
   branch-absent arm. Where `<branch>` is present, its head is the base and the
   report's prior-head field carries that SHA; where it is absent, `main`'s head
   is the base and the prior-head field reads `created` (PRD G1, first arm).
   Either way the base SHA comes from this read, not from
   `refs/remotes/origin/<branch>`.

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
   the base step 3 resolved, both before any ref moves.

   - `git merge-base --is-ancestor HEAD <base>`. Exit 0 means local HEAD is at
     or behind the base. Non-zero means the local tree carries at least one
     commit the base does not.
   - Where `<branch>` exists locally,
     `git merge-base --is-ancestor <branch> <base>`. This is the ref step 6
     rewrites, and local HEAD is not it. With HEAD on any other branch the first
     check passes while `<branch>` carries unpushed commits the base does not,
     and step 6 then resets `<branch>` and leaves those commits reachable from
     no ref at all (*observed* — run against `git` 2.55.0 in a throwaway
     repository: with `feature` two commits ahead of the base and HEAD on
     `main`, `merge-base --is-ancestor HEAD <base>` exits 0,
     `git checkout -B feature <base>` reports "Switched to and reset branch
     'feature'", and the prior tip is thereafter absent from `git rev-list --all`
     and not an ancestor of HEAD). The second check exits non-zero on exactly
     that state (*observed*, same substrate), and it is the only thing standing
     between the ordinary post-checkout tree state and the destructive class PRD
     §7 puts under "Not accepted".

   Either check failing produces one refusal in one shape — FM-3 (§6), not two
   failure modes: the tool names the divergence, the base SHA, the local HEAD
   SHA, and, where it was the second check that failed, the local head of
   `<branch>`; then exits non-zero (PRD G1, AC-LAND-01c). Where `<branch>` does
   not exist locally the second check has no subject and is skipped, which is
   not a pass being assumed: there is no ref to orphan.

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
    against the blob SHA in the local commit (AC-LAND-06).
11. **Report and exit.** The report is serialized to stdout on every terminal
    path the sequence reaches — the success path and every failure mode §6
    enumerates as detected (§5). Two terminal paths lie outside that rule, and
    are stated here rather than left for an implementer to decide:

    - **A usage error.** Parsing belongs to `argparse`, in `bin/land`, and runs
      before the sequence begins (§3.1). `argparse` writes its own diagnostic to
      stderr and exits 2; **stdout carries nothing and no report is emitted.**
      That is consistent with `aimeta/cli.py`'s standing discipline —
      diagnostics on stderr, stdout reserved for machine-consumable output — and
      with §7's mapping of 2 to a usage error. Nothing is intercepted and no
      failure mode is added for it: an invocation that never named a branch has
      established no fact for a report to carry, and `branch` is precisely the
      field every other failure path does carry. §3.1's division of
      responsibility is unchanged by this.
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
  because step 5's second check refuses in that state — the guard is what makes
  it true, not the mechanism.

  **In the cases the guard permits, the tool moves HEAD rather than refusing.**
  That is a settled decision, not an open question. Refusing would rule out J1 in
  any session whose worktree was not created on the target branch — the ordinary
  opening state, since the first invocation is the one that creates the branch —
  so the refusal would cost the journey the tool exists to serve. What it costs
  instead is that the session's checked-out branch changes under it, and that is
  reported rather than left silent: where HEAD was on a branch other than
  `<branch>` before this step, the report carries `detail.prior_branch` naming it
  (§5.3). OQ-5 asked this question; §9 records the answer and retires the
  identifier.

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

Step 5's second check makes this mechanical rather than merely intended: where
the local `<branch>` is the ref carrying the commits, that check refuses; where
some other branch carries them, the first check does. So the refusal in this arm
now falls out of the guard on both routes, and the proposal below is a question
about whether the PRD should *say* so, not about what the tool would do.

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
  `checkout -B`, `reset --mixed`, `rev-parse <rev>:<path>`.
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

`facts` carries only what that step established, keyed as §5.2 and §5.3 name the
fields — step 3 returns `base` and `prior_head`; step 5 returns `local_head`, and
also `branch_head` where the local `<branch>` existed and was the ref its second
check ran against, which is the field §5.3 requires on that refusal; step 6
returns `prior_branch` where HEAD was on some branch other than `<branch>` when
it ran; step 8 returns `head` and the paths the commit contains; step 10 returns
the head `ls-remote` reported for `<branch>` as `remote_head`, and then the
per-file results. `stage` is that step's token from §5.3's enumeration, carried
on the stop so the report can report where the sequence halted. `git_status` is
the failing invocation's exit status, or `None` where the stop was a comparison
rather than a subprocess. The sequence accumulates `facts` across steps and
halts at the first `ok: False`. No step reads another step's git output; a step
consumes established facts, never text.

Step 8's paths are what `files` is built from on the two failure paths where a
commit exists and step 10 produced no per-file result of its own: on FM-7 the
push failed before step 10 ran, and on FM-8 the head comparison failed before the
per-file comparison was reached. Step 10 is therefore not the source of those
entries, and naming step 8 as their source is what keeps `build` from having to
invent them or omit them — on both modes it emits one entry per committed path,
with the match unknown, as §5.2 states the shape.

**`land.py` → `report.py`.** `land.py` never formats:

    Report.build(branch: str, facts: dict, stop: StepResult | None) -> Report

`build` is where §5.2's rules are applied: a contract field that §5.2 gives a leaf
form and that is absent from `facts` is emitted with `class: "unknown"` and
`value: null`. `detail` is populated from the same accumulated `facts` under
§5.3's key table: each key that table names is emitted where `facts` carries it
and absent where it does not. Unknown-ness is therefore a property of what was
established, computed in one place, rather than something each of ten failure
paths has to remember to say — which is what makes the failure paths correct by
construction and makes B4's class of defect structurally hard to reintroduce.

Three of the five contract fields do not take their value from that rule, and the
exceptions belong to §5.2 and §6 rather than to this section. Stating them here is
what keeps `build` from being written to a rule those sections contradict:

- **`branch` comes from the parameter**, not from `facts`. It is therefore
  `observed` on every path the sequence reaches, including the ones on which
  nothing else was established — which is why §6's last column names it in every
  row of the failure table, FM-1's included, where no other contract field is
  established at all.
- **`files` is exempt.** §5.2 gives it no leaf form: it is a list on every path,
  and `build` emits it as one. Where entries exist each carries its own `class`;
  where no commit was made there are no entries and the list is empty; and where
  a commit was made but no comparison result exists for it, the entries are
  present and each of them is `unknown`. Its unknown-ness is carried per entry,
  or by the absence of entries together with the stage token, never by a `class`
  on the list — so no union type enters the parse contract, which is the property
  AC-LAND-T01 tests.
- **`verification` is computed, not carried.** No step returns it. `build`
  derives it from what `facts` holds, under §5.2's biconditional: `"complete"`
  where `ls-remote` confirmed the head and every per-file comparison matched;
  `"incomplete"` where a step after the commit established that it was not — the
  push failing, or a comparison mismatching — so the local commit is reported
  `observed` while the landing is not; and `null` with `class: "unknown"` where
  nothing about the landing was established, which is every path on which no
  commit was made. Deriving it in one place from the same biconditional §7's
  exit mapping reads is what stops the report and the exit code from drifting
  apart, which is AC-LAND-T02.

**What `report.py` exposes.** A `Report` carries the five contract fields and the
`detail` object of §5.3, and offers:

    Report.to_json(self) -> str      # §5.2's format: two-space indent, sorted
                                     # keys, UTF-8, one trailing newline
    Report.exit_code(self) -> int    # §7's mapping

`to_json` is a pure function of the `Report`: it touches no git, no filesystem,
and no clock. That is what lets AC-LAND-T01 construct every report shape,
failure shapes included, by calling `Report.build` with synthetic facts and never
performing a landing — the property §3.1 claims for the split, which until now
had no stated surface to rest on.

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

New helpers required: a bare-remote factory, a remote-head reader, and a way to
mutate the bare repository between push and verification (which is how the
content-verification test in PRD §5 induces its mismatch).

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
  therefore cannot produce FM-6's trigger at all.
- Evidence class: **assumed.**
- Does not prove: that a hook refusal surfaces as a non-zero `git commit` exit
  rather than some other outcome; that the report on that path carries the stage
  and status §6 states; or that the hook's own diagnostics stay off stdout, which
  AC-LAND-T01's "stdout carries no text outside that object" requires and which
  nothing currently checks.
- Deferred-verification path: a test that installs this repository's `pre-commit`
  hook into the substrate repo and induces FM-6 with a file the frontmatter check
  rejects.

Leaving B5 **assumed** is a permitted outcome; leaving it undeclared was not.
§3.2 step 8 makes the hook load-bearing on purpose — a tool on the write path
that bypassed governance would be landing work the governance never saw — so a
dependency the design routes governance through, which produces an enumerated
failure mode, and which the substrate provably does not exercise, is exactly what
this section exists to name. The declaration is what puts the choice in front of
Dave: buy the deferred path, or accept the class knowingly. What it removes is
the third option, of shipping FM-6 on evidence nobody classified.

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

Shape:

```json
{
  "branch":     {"value": "bin-land-trd", "class": "observed"},
  "head":       {"value": "<40-hex>", "class": "observed"},
  "prior_head": {"value": "created", "class": "observed"},
  "files": [
    {"path": "specs/bin-land-trd.md", "match": true, "class": "observed"}
  ],
  "verification": {"value": "complete", "class": "observed"},
  "detail": {}
}
```

Rules the format holds on every path:

- The five contract keys — `branch`, `head`, `prior_head`, `files`,
  `verification` — are **always present**, in success and in every failure.
- Every leaf object carries `class`, whose value is `"observed"` or
  `"unknown"` and nothing else. These are the two of Core's four classes PRD G6
  permits the tool to emit, stated there as a subset rather than a redefinition
  (*observed*).
- `value` is `null` wherever `class` is `"unknown"`. An unestablished fact is
  never rendered as an empty string or a plausible placeholder. A `files` entry
  is the one leaf that names its established value `match` rather than `value`,
  and carries no `value` key at all, so on such an entry this rule reads over
  `match` — which the `files` rule below states directly.
- `prior_head.value` is a 40-character SHA, the literal string `"created"`, or
  `null`; `null` only with `class: "unknown"` (PRD G1, first arm).
- `files` is a list, possibly empty. Each entry carries `path`, `match`, and
  `class`. `match` is `true`, `false`, or `null`; `null` only with
  `class: "unknown"`.
- `verification.value` is `"complete"`, `"incomplete"`, or `null`; `null` only
  with `class: "unknown"`. `"complete"` if and only if `ls-remote` confirmed the
  head SHA and every per-file comparison matched — the same biconditional as
  AC-LAND-08's exit status, so the two can never disagree.

The three value-domain rules are written to one shape on purpose. Each admits
`null`, and each admits it only under `class: "unknown"`, so none of them
contradicts the null-on-unknown rule above it on the failure paths where §6 says
the contract fields are unestablished. A rule list that permitted only
`"complete"` or `"incomplete"` would force an implementer to emit
`verification: {"value": "incomplete", "class": "observed"}` on a fetch failure —
asserting the tool observed an incomplete verification it never attempted, which
inverts exactly the distinction PRD G6 exists to draw.

**An empty `files` list where no commit was made.** On FM-1 through FM-6, and on
FM-11, no commit exists, so there are no per-file entries and `files` is `[]`.
That `[]` is **not** a claim that the commit contained no files — there is no
commit for it to be a claim about. It is the absence of entries. `detail.stage` is what
distinguishes it from FM-5, where an empty staged set is the established answer
and the same `[]` means something different; §5.3 closes that field's value set,
which is what makes the distinction firm enough to rest this on. No union type is
introduced: giving `files` a leaf form of `{"value": null, "class": "unknown"}` in
place of the list would put a type switch into a parse contract whose whole
burden is that a failed landing stays mechanically readable, and it would buy
nothing the stage token does not already carry. Where §6's rows say the contract
fields are `unknown`, `files` is read accordingly — its unknown-ness is carried
by the stage token and by having no entries, not by a `class` on the list.

**Where a commit exists and the comparison did not produce a result.** FM-7 and
FM-8 are the complement of that set among the detected modes: on both a commit
was made, and on neither did step 10 produce a per-file result — the push failed
before step 10 ran on one, the head comparison failed before the per-file
comparison was reached on the other. On those two paths `files` is **not** empty.
It carries one entry per path in the commit, each of the form
`{"path": "<path>", "match": null, "class": "unknown"}`, sourced from the paths
step 8 returns (§3.7). The rules above already admit that shape and no new type
is introduced: `match` is `null` under `class: "unknown"`, which is the per-entry
unknown-ness the list was given in place of a leaf form.

The paths themselves were established — the tool staged them at step 7 and
committed them at step 8 — and the match was not, so the entry claims the first
and declines the second. That is what AC-LAND-07's per-file requirement and
AC-LAND-09's split between what was established and what was not both ask for on
a commit that exists; an empty list on those two paths would claim neither, and
would be indistinguishable in shape from FM-5's `[]`, where an empty staged set
is the established answer. FM-7 is the state PRD §7 accepts, so its report is the
artifact a session is handed when the accepted risk fires; it has to be able to
name the files sitting in the local commit that session must now resolve.

### 5.3 The failure path and the five-field contract

`reviews/bin-land-cycle-4.md` O3 records the tension: G1's refusal requires the
output to name "the divergence and both heads", and the local head is not among
G6's five fields; G6 nonetheless presents the five as "the PRD-level contract",
so "a TRD author deriving the serialization format from G6 alone would not
leave room for it" (*observed*).

**Resolution: a sixth top-level key, `detail`, which is an object and is always
present.** The five contract keys keep their exact meanings and are never
overloaded to carry something else. `detail` holds path-specific established
facts, each an object with the same `value`/`class` shape:

| Key in `detail` | Emitted on | Meaning |
| --- | --- | --- |
| `local_head` | The divergence refusal, and any failure after step 5 | Local `HEAD` SHA at the guard |
| `branch_head` | The divergence refusal, where the local `<branch>` was the failing check (§3.2 step 5) | Local SHA of `<branch>` before step 6 would have rewritten it |
| `base` | Any failure after step 3 | The SHA resolved as the landing base |
| `stage` | Every failure | Which step of §3.2 stopped the sequence |
| `git_status` | Any failure at a git invocation | That invocation's exit status |
| `remote_head` | FM-8 | The head `ls-remote` returned for `<branch>` after the push |
| `prior_branch` | The success path, and any failure after step 6, where HEAD was on a branch other than `<branch>` when step 6 ran | The branch HEAD was on before step 6 moved it onto `<branch>` (§3.3) |

`prior_branch` is the one key in this table that can appear on a landing that
succeeded. Every other key records where the sequence stopped; this one records a
mutation of the session's own working tree, which happens on the success path
too, and which §3.3 decides the tool is permitted to make. The table carries no
"and no others" clause — unlike `stage`'s value set below, it is a definition of
the keys the design emits rather than a closed domain a reader branches on.

The "Emitted on" column is open in the same direction. It states where each key
is expected, not a ceiling on where it may appear: a key `facts` carries on a
path this column does not name is **emitted** there, not dropped. `remote_head`
is the case that arises — §3.7 has step 10 return it on every path that reaches
the `ls-remote` read, so it is carried on FM-9 and on the success path as well as
on FM-8, and on those two it equals `head` and is redundant rather than wrong.
Dropping it to match a column would be the report declining to claim a fact the
tool observed, which is the direction PRD G6 exists to rule out. A reader may
therefore not treat a key's absence from a path as a claim, and no test written
to this document may assert one.

**The permitted `detail.stage` values.** `stage` is the one field a machine
reader branches on to interpret a failure report, so its value set is closed
rather than open text. One token per step of §3.2 at which the sequence can
stop:

| Token | §3.2 step it names | Failure modes reaching it |
| --- | --- | --- |
| `fetch` | 2, fetch | FM-1 |
| `resolve` | 3, resolve the base from the remote | FM-1's class, where the remote read is what failed; and FM-11, where it succeeded and named no base |
| `base-object` | 4, confirm the base object is present locally | FM-2 |
| `guard` | 5, divergence guard | FM-3 |
| `base` | 6, establish the base | FM-4 |
| `stage` | 7, stage | FM-5 |
| `commit` | 8, commit | FM-5, FM-6 |
| `push` | 9, push | FM-7 |
| `verify` | 10, verify | FM-8, FM-9 |

Nine tokens and no others. Two readings the table is meant to foreclose: `stage`
is one value of one field, not a second step alongside `commit`, which matters
because §6's FM-5 row lists two tokens for one failure mode and because the token
`stage` and the step named "Stage" are otherwise easy to conflate; and
`base-object` is step 4's own token rather than step 3's, so a report from the
step-4 refusal no longer says `resolve` and name a step that succeeded.

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
  sequence reaches.** The enumeration is the success path and each failure mode
  in §6 **except FM-10**, which the tool does not detect and which emits nothing
  by construction, so it is not a case this criterion can be written against. The
  usage-error path is likewise outside the enumeration: it emits no report, and
  what it does emit is covered by the separate assertion below. For each case in
  the enumeration, the tool's **stdout** parses with `json.loads` without error;
  the parsed value is an object; its keys are exactly `branch`, `head`,
  `prior_head`, `files`, `verification`, `detail`; every leaf object carries a
  `class` in `{"observed", "unknown"}`; every leaf whose `class` is `"unknown"`
  has `value` of `null`, or, in a `files` entry, `match` of `null`, that being
  the one leaf shape whose established value is not named `value` (§5.2); the
  three value-domain rules of §5.2 hold; and stdout carries no text outside that
  object. On FM-7 and FM-8 — the two cases in the enumeration where a commit
  exists and no comparison result does — `files` carries one entry per path in
  the commit, each with `match` of `null` and `class` of `"unknown"`, so the
  shape §5.2 states for those two paths is tested rather than only written down.
  On every failure case, `detail.stage` is present and its value is one of the
  nine tokens §5.3 enumerates — the token §5.3 assigns to the step that stopped
  the sequence, so the set is tested rather than merely documented. Enumerating the failure modes is what makes this a real
  test rather than a test of the success path: the format's whole burden is that
  a failed landing is still machine-readable.

- **AC-LAND-T01a — the usage-error path emits no report.** Given an invocation
  `argparse` rejects, stdout is empty, stderr is non-empty, and the exit status
  is 2 (§3.2 step 11, §7). Stated as its own case rather than folded into T01
  because the property under test is the opposite one — that nothing is written
  to stdout — and a criterion asserting both shapes at once would be satisfied by
  either.

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
unestablished ones labelled `unknown`, a bracket-coded diagnostic on stderr,
and a non-zero exit.

**The last column, one rule.** Each cell names — exhaustively — the contract
fields and `detail` keys the report carries as **established** at that point: a
contract field emitted with `class: "observed"`, or a `detail` key present with
an observed value. What a cell does not name is not established there. Nothing is
thereby missing from the report: §5.2 keeps the five contract keys and `detail`
present on every path, so a contract field a cell omits is emitted
`{"value": null, "class": "unknown"}` — or, for `files`, as a list with no
entries — and a `detail` key a cell omits is simply absent. `detail.stage` is
established on every detected mode and has its own column above, so it is not
repeated cell by cell.

The cells are derived, not independent: §3.2's sequence, §3.7's step returns and
`build` rules, and §5.2's and §5.3's field semantics are what establish a fact,
and each of them is stated as a rule. Where a cell and those sections disagree,
those sections are normative and the cell is wrong.

| # | Failure mode | Detected by | `detail.stage` | Established at that point |
| --- | --- | --- | --- | --- |
| FM-1 | A remote read fails — no network, no such remote, auth refused | `git fetch` or step 3's `git ls-remote` exit status | `fetch` / `resolve` | `branch`, and no other contract field: the read that would have established them is the one that failed. `detail.git_status`. |
| FM-2 | The base object is not present locally (§3.2 step 4 names the candidate causes; the tool asserts none of them) | `git cat-file -e` | `base-object` | `branch`, `prior_head`. `detail.base`, `detail.git_status`. |
| FM-3 | **Divergence refusal, before staging** — local HEAD, or the local `<branch>` the sequence would rewrite, carries a commit the base does not | either `merge-base --is-ancestor` non-zero (§3.2 step 5) | `guard` | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.branch_head` where the local `<branch>` was the failing check. Nothing staged, no ref moved, no commit made. |
| FM-4 | Base establishment fails — a locally-modified file differs between old HEAD and base | `git checkout -B` exit status | `base` | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`. No `detail.prior_branch`: step 6 is the step that failed, so HEAD never moved. |
| FM-5 | Nothing to commit — a named path does not exist, or the staged set is empty | `git add` / `git commit` exit status | `stage` or `commit` — one field, one value (§5.3) | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. No commit exists. |
| FM-6 | A repository hook refuses the commit | `git commit` exit status | `commit` | `branch`, `prior_head`. `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. No commit exists. |
| FM-7 | Push fails | `git push` exit status | `push` | `branch`, `prior_head`, `head` — the **local** commit's SHA, `observed` — `verification`, the value `incomplete`, and `files`, carrying one entry per path in the commit with `match: null` and `class: "unknown"` (§5.2). `detail.base`, `detail.local_head`, `detail.git_status`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. |
| FM-8 | `ls-remote` disagrees with the pushed head | Comparison at step 10 | `verify` | `branch`, `prior_head`, `head`, `verification` — the value `incomplete` — and `files`, carrying one entry per path in the commit with `match: null` and `class: "unknown"` (§5.2). `detail.base`, `detail.local_head`, `detail.remote_head`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. |
| FM-9 | A per-file blob comparison mismatches | Comparison at step 10 | `verify` | `branch`, `prior_head`, `head`, `verification` — the value `incomplete` — and `files`, carrying the per-file results themselves, each `observed`, the mismatching path with `match: false`. `detail.base`, `detail.local_head`, `detail.remote_head`, and `detail.prior_branch` where HEAD was on a branch other than `<branch>` when step 6 ran. |
| FM-10 | The invocation is killed mid-sequence | Not detected by the tool | — | Nothing: no report is emitted, so there is no field for the column to be about. See §3.2 step 11's second bullet and OQ-4. |
| FM-11 | **The remote read succeeds and names no base** — neither `<branch>` nor `main` is present at the remote, so the branch-absent arm has nothing to resolve a base from | Step 3's `ls-remote` exits 0 having returned no line for either ref | `resolve` | `branch`, and `prior_head` — the literal `created`, step 3 having observed that `<branch>` is absent at the remote (§3.2 step 3). Nothing further: no base was resolved, no ref moved, nothing was staged, no commit was made. |

FM-11 is appended rather than inserted at the step it belongs to. Its stage is
step 3's, so by sequence it sits beside FM-1; the existing numbers are cited by
number in this document's review artifacts, and renumbering to restore sequence
order would strand those citations. The out-of-order row is the cheaper of the
two costs.

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
one level down: the paths are named because the tool staged and committed them,
and each `match` is `unknown` because step 10 never ran (§5.2). That is what lets
the session handed this report see which files sit in the local commit it is now
obliged to resolve, rather than reconstruct them from the invocation it made.

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
(*observed*). Exit status is the third channel. Nothing else is emitted
anywhere; there is no log file and no telemetry sink (§2).

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
| 4 | FM-8, FM-9 — the tool's own verification of its own write failed, which is exactly what `EXIT_SELF_VERIFY` already means for `bin/flip-agreed` |

Code 1's constant is named `EXIT_POLICY`, which fits this tool's use of it
poorly. Adding a code would change a cross-cutting constant every CLI's tests
read. Recorded as OQ-10.

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
stale. And B5 is **assumed**: FM-6 ships on a hook the test substrate never
installs, so either its deferred-verification path is bought or that class is
accepted knowingly — and whichever it is, the boundary audit at the implementing
change's release decision is where it is said out loud rather than inherited.

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

Eight open, and two retired. Each open question names what would resolve it; none
is settled here. A retired identifier is kept in place rather than reused, so a
reader arriving from a review artifact that cites it by number can still find
what it referred to — the precedent PRD §8 sets for its own Q1–Q4 (*observed*).
The two retirements differ in kind: OQ-8 is retired because the question had no
closing move, OQ-5 because it has been answered.

- **OQ-1 — No SLO exists for J1, J2, or J3.** §2 states this explicitly, as the
  template requires, and gives the structural reason: no production surface, no
  telemetry, no aggregate. *Resolved by*: Dave deciding whether any post-
  adoption signal about the tool is wanted at all and, if so, where it would be
  recorded — since it could not come from the tool, it would have to come from
  reading execution reports, which is PRD §5's mechanism rather than an SLO.

- **OQ-2 — Whether the PRD should govern the branch-absent diverged case.** What
  the tool does in that state is no longer what is open. §3.2 step 5's two checks
  refuse on both routes — the first where some branch other than `<branch>`
  carries the commits, the second where the local `<branch>` does — so §3.4's
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
  in the output rather than only in this document: `detail.prior_branch` names
  the branch HEAD was on where that was not `<branch>` (§5.3, §3.3). That the
  move loses no commit remains a property of §3.2 step 5's second check and never
  was one of `checkout -B`.

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
  `checkout -B`, `reset --mixed`, and `rev-parse <rev>:<path>` — is long-stable,
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

- **OQ-10 — The exit code for a failed remote write.** §7 maps FM-7 onto `1`,
  whose constant is named `EXIT_POLICY`. Adding a code would change
  `DOCUMENTED_EXIT_CODES`, which every CLI's tests read. *Resolved by*: a
  decision on the cross-cutting exit-code contract in `bin/aimeta/cli.py` —
  reuse `1` and accept the name, or add a code and update the constant and the
  documented set.
