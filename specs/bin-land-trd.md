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
failure shape — without performing a landing.

### 3.2 The sequence

One invocation runs these steps in order, and stops at the first that fails.

1. **Parse.** `<branch>`, `<message>`, zero or more paths. No flags and no
   modes (*observed*, PRD G1). `--help` exits 0, as AC-X-3 requires of every
   CLI (*observed*).
2. **Fetch.** `git fetch origin`. Its exit status is the only thing read;
   stderr is captured for diagnostics and never inspected for a decision (G4).
3. **Resolve the base, from the remote rather than from a cached ref.**
   `git ls-remote --heads origin <branch>` answers presence and, where present,
   the head SHA. Presence decides which of G1's two arms applies; the base SHA
   comes from this read, not from `refs/remotes/origin/<branch>`.

   This is a deliberate technical decision, not a restatement of environment
   lore. `policies/remote-write-verification-policy.md` rule 1 makes the
   repository's own log against the **fetched** remote the authority on what
   landed (*observed*); a remote-tracking ref is a cache of a previous fetch,
   and the failure it produces — a base cut from a stale ref — has been
   observed in this repository's own sessions (*observed*, recorded in
   `docs/cycles/bin-land-flip-20260823T210300Z.md`). Reading the remote
   directly removes the class rather than warning about it.

   Where the branch is absent, the same read is performed for `main` and its
   SHA is the base; the report's prior-head field reads `created` (PRD G1,
   first arm).
4. **Confirm the base object is present locally.** `git cat-file -e <base>^{commit}`.
   If the object is absent, the remote moved between step 2 and step 3 and the
   tool refuses rather than fetching again — a second fetch would race the same
   way, and the tool does not loop (§6, FM-2).
5. **Divergence guard, before anything is staged.** `git merge-base --is-ancestor HEAD <base>`.
   Exit 0 means local HEAD is at or behind the base and the sequence continues.
   Non-zero means the local tree carries at least one commit the base does not,
   and the tool refuses: it names the divergence, the base SHA, and the local
   HEAD SHA, and exits non-zero (PRD G1, AC-LAND-01c).

   The guard runs **before** step 6 because step 6 moves a ref. Ordering is
   load-bearing: AC-LAND-01c requires every local-only commit to remain
   reachable from local HEAD afterwards, and that holds precisely because the
   tool has touched no ref by the time it refuses.
6. **Establish the base.** `git checkout -B <branch> <base>`. See §3.3.
7. **Stage.** `git add -- <paths>` for named paths; `git add -A` when none are
   named (PRD G2). Paths are always separated by `--`.
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
    path, including every failure path (§5).

Steps 2, 9, and 10 are the only network operations, and there is exactly one of
each write: one push per invocation, on every path. §8 states how that is
enforced.

### 3.3 Base establishment for the at-or-behind case

PRD G1 fixes the base at remote state and PRD G2 stages from the local tree,
and the operation joining them is not stated at PRD level — recorded as
`reviews/bin-land-cycle-4.md` O1, which names three candidates: fetch-and-reset,
`commit-tree` against the fetched base, and checkout-then-stage (*observed*).

**Decision: `git checkout -B <branch> <base>`.** One command. It creates or
resets the local branch `<branch>` to the fetched base, checks it out, and
carries uncommitted working-tree changes across.

What the working tree holds afterwards, stated because O1 records that the
three candidates "differ only in what they leave in the tree afterwards"
(*observed*):

- **Immediately after step 6**: the tracked content of the fetched base, plus
  every uncommitted modification and untracked file the session had before the
  invocation. Nothing the session produced is discarded; that is the property
  that rules out `git reset --hard`, which would destroy exactly the work the
  tool exists to land.
- **After a successful invocation**: HEAD on `<branch>`, at the new commit,
  which is also the branch's head at the remote. Paths that were landed are
  clean. Where paths were named and other changes existed, those other changes
  are still present and uncommitted.

Two consequences are stated rather than left to be discovered:

- **The J1→J2 sequence works without the session doing anything between
  invocations.** After J1 the local branch is at the landed head, so J2's
  divergence guard sees a tree at the base and proceeds. A design that left
  local HEAD where it was — `commit-tree` against the fetched base, writing the
  ref directly — would leave the session's second invocation staging the same
  file again against a base that already contains it.
- **HEAD moves.** If the checkout was on some branch other than `<branch>`,
  `checkout -B` moves HEAD off it. The prior branch's ref is not touched and no
  commit becomes unreachable, because step 5 has already established that local
  HEAD is an ancestor of the base. Whether the tool should nonetheless refuse
  rather than move HEAD off an unrelated branch is OQ-5.

`checkout -B` fails when a locally-modified file's content differs between the
old HEAD and the base. That is a real and reachable state, it is caught before
any commit or push, and the tool stops there (§6, FM-4). A false stop is cheap
(*observed*, PRD §7).

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
  step 8's `git commit`.

### 3.6 Boundaries

The points where the tool meets something it does not control:

- **B1 — the remote git service.** The receive-pack that accepts the push and
  the upload-pack that answers `ls-remote` and `fetch`.
- **B2 — the credential path.** Whatever `git` does to authenticate, including
  the helper whose stderr output PRD G4 exists to be indifferent to.
- **B3 — the sandbox network policy.** Whether the remote is reachable at all.
- **B4 — `git` itself.** The plumbing this design relies on:
  `ls-remote --heads`, `merge-base --is-ancestor`, `cat-file -e <rev>^{commit}`,
  `checkout -B`, `rev-parse <rev>:<path>`.

Each is declared in §4 with its representation and evidence class.

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
- Does not prove: behaviour on another version. No minimum version is asserted
  today; OQ-8 asks whether one should be pinned and tested.

### 4.3 A note on what the per-file comparison proves

Stated plainly because it bears on how much B1's contract-verified class
carries. Under git's content addressing, a commit SHA determines its tree, so
once `ls-remote` returns the same commit SHA the tool pushed, the per-file blob
SHAs necessarily agree (*inferred*). AC-LAND-06's comparison is therefore not
independent evidence *for a git-transport write*.

It is not redundant in two other senses, and both are why PRD G5 asks for it:
the report must carry a per-file result (G6), and the check is the one that
would catch the failure class `policies/remote-write-verification-policy.md`
records — a write path carrying content as a request parameter, where a
placeholder replaced a ~64KB file with 19 bytes and landing-verification
confirmed the destruction as a success (*observed*, that policy's Known gap).

A strictly stronger check exists — comparing the bytes fetched back from the
remote against the bytes of the named file on disk, rather than against the
blob SHA in the local commit — which would additionally catch a mis-staged
file. It is not adopted here because AC-LAND-06 states the comparison as
"equals the blob SHA committed locally" (*observed*), and changing what an
agreed criterion asserts is Dave's. Recorded as OQ-6.

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
| The index | Reset by step 6's checkout; written by step 7 | Local |
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
  never rendered as an empty string or a plausible placeholder.
- `prior_head.value` is either a 40-character SHA or the literal string
  `"created"` (PRD G1, first arm).
- `files` is a list, possibly empty. `match` is `true`, `false`, or `null`;
  `null` only with `class: "unknown"`.
- `verification.value` is `"complete"` or `"incomplete"`. `"complete"` if and
  only if `ls-remote` confirmed the head SHA and every per-file comparison
  matched — the same biconditional as AC-LAND-08's exit status, so the two can
  never disagree.

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
| `base` | Any failure after step 3 | The SHA resolved as the landing base |
| `stage` | Every failure | Which step of §3.2 stopped the sequence |
| `git_status` | Any failure at a git invocation | That invocation's exit status |

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

Named here as AC-LAND-07 defers it. This is a TRD-stage criterion; it is
proposed for the derived acceptance-criteria artifact and is not an amendment
to PRD §6.

- **AC-LAND-T01 — the report parses mechanically, on every terminal path.**
  For each terminal state of §3.2 — the success path and each failure mode
  enumerated in §6 — the tool's **stdout** parses with `json.loads` without
  error; the parsed value is an object; its keys are exactly `branch`, `head`,
  `prior_head`, `files`, `verification`, `detail`; every leaf object carries a
  `class` in `{"observed", "unknown"}`; every leaf whose `class` is
  `"unknown"` has `value` of `null`; and stdout carries no text outside that
  object. Enumerating the failure modes is what makes this a real test rather
  than a test of the success path: the format's whole burden is that a failed
  landing is still machine-readable.

- **AC-LAND-T02 — `verification` and exit status agree.** Across the same
  enumeration, exit status is 0 if and only if `verification.value` is
  `"complete"`. This is AC-LAND-08 read through the serialization, and it is
  what stops the report and the exit code from drifting apart.

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

| # | Failure mode | Detected by | `detail.stage` | Established at that point |
| --- | --- | --- | --- | --- |
| FM-1 | Fetch fails — no network, no such remote, auth refused | `git fetch` exit status | `fetch` | Nothing. All five contract fields `unknown` except `branch`. |
| FM-2 | The remote moved between fetch and resolve; the base object is not present locally | `git cat-file -e` | `resolve` | `branch`; `detail.base`. |
| FM-3 | **Divergence refusal, before staging** | `merge-base --is-ancestor` non-zero | `guard` | `branch`; `prior_head` where the branch existed; `detail.base`, `detail.local_head`. Nothing staged, no ref moved, no commit made. |
| FM-4 | Base establishment fails — a locally-modified file differs between old HEAD and base | `git checkout -B` exit status | `base` | As FM-3. |
| FM-5 | Nothing to commit — a named path does not exist, or the staged set is empty | `git add` / `git commit` exit status | `stage` / `commit` | As FM-4, plus the base established. |
| FM-6 | A repository hook refuses the commit | `git commit` exit status | `commit` | As FM-5. No commit exists. |
| FM-7 | Push fails | `git push` exit status | `push` | Everything up to and including a **local** commit, whose SHA is reported as `head` with `class: "observed"`; `verification` is `incomplete`. |
| FM-8 | `ls-remote` disagrees with the pushed head | Comparison at step 10 | `verify` | The push's exit status and the local head; the remote's head as `detail`. |
| FM-9 | A per-file blob comparison mismatches | Comparison at step 10 | `verify` | The head; the branch; the prior head; per-file results with the mismatching file named `match: false`. |
| FM-10 | The invocation is killed mid-sequence | Not detected by the tool | — | Nothing is emitted. See §5.2's note and OQ-4. |

Two of these need more than a row.

**FM-3 is the pre-staging refusal path, and it is a first-class failure mode
here.** `reviews/bin-land-cycle-4.md` O2 records that PRD §3's J3 trigger —
"any step fails, or verification does not establish a match" — does not reach
it, because no step failed and verification was never attempted (*observed*).
That is a PRD-side documentation gap, held out of scope by Dave; this section
does not depend on it. FM-3 is detected, reported, and tested regardless, and
AC-LAND-01c already states the behaviour directly (*observed*). Whether J3's
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
commit was observed, the landing was not.

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
| 3 | FM-1 through FM-6 — every precondition that stops the sequence before a write |
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
  stop being true and a real gate would be needed.

**Operating it responsibly.** Two standing obligations follow from §4: B1's
contract-verified class means the change package for the implementing change
should record whether a live landing was performed (OQ-7); and B2's mock
representation means the static no-stderr-branching scan is the part that must
never be deleted, because it is the only half of AC-LAND-04 that cannot go
stale.

## 8. Constraints, NFRs, and non-goals

The technical instantiation of PRD §4's non-functional goals, dimension by
dimension.

**Performance.** No latency target, per the PRD. The concrete constraint is
negative and enforceable: one invocation performs exactly one `fetch` for
objects, one `ls-remote` before the write, one `push`, and one `ls-remote` plus
one targeted `fetch` after it. No sleep, no backoff, no retry loop, and no
second write on any path. Enforced by a test that records the git argv sequence
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
assume. No minimum `git` version is asserted; the plumbing used is long-stable,
and OQ-8 asks whether to pin and test a floor. The tool makes no assertion
about what the sandbox permits (*observed*, PRD §4).

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

Ten. Each names what would resolve it. None is settled here.

- **OQ-1 — No SLO exists for J1, J2, or J3.** §2 states this explicitly, as the
  template requires, and gives the structural reason: no production surface, no
  telemetry, no aggregate. *Resolved by*: Dave deciding whether any post-
  adoption signal about the tool is wanted at all and, if so, where it would be
  recorded — since it could not come from the tool, it would have to come from
  reading execution reports, which is PRD §5's mechanism rather than an SLO.

- **OQ-2 — The branch-absent diverged case.** §3.4 proposes uniform refusal and
  gives the reason. No PRD goal or acceptance criterion decides it, and both
  behaviours satisfy every stated goal (*observed*,
  `reviews/bin-land-cycle-5.md` O1). *Resolved by*: Dave's disposition of
  cycle-5 O1 — either lifting G1's refusal sentence into its "In both arms"
  paragraph, or widening AC-LAND-01c's given.

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

- **OQ-5 — Whether the tool should refuse when the checkout is on a branch
  other than the named one.** §3.3 has `checkout -B` move HEAD, losing no
  commit but changing which branch the session is on. *Resolved by*: a decision
  on what the tool is permitted to do to the session's working tree — which is
  a contract with the executor rather than a purely internal choice.

- **OQ-6 — Whether the per-file comparison should compare fetched bytes against
  the file on disk rather than blob SHAs against the local commit.** §4.3 gives
  the argument: the stronger form additionally catches a mis-staged file, and
  it is the form that is independent of commit-SHA equality. It is not adopted
  because AC-LAND-06 states the weaker one. *Resolved by*: Dave deciding
  whether AC-LAND-06 changes.

- **OQ-7 — Whether a live landing against the real `origin` is required before
  release, and on what cadence B1's deferred verification re-runs.** §4.2
  proposes one, recorded in the implementing change's package.
  *Resolved by*: the boundary audit at that change's release decision, under
  `policies/verification-boundary-policy.md`.

- **OQ-8 — Whether a minimum `git` version is pinned and tested.** §3.2 relies
  on `ls-remote --heads`, `merge-base --is-ancestor`, `cat-file -e <rev>^{commit}`,
  `checkout -B`, and `rev-parse <rev>:<path>`. No floor is asserted today.
  *Resolved by*: establishing the oldest `git` any target environment supplies
  — which is *unknown* here, since the sandbox runner is not this repository's
  to inspect.

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
