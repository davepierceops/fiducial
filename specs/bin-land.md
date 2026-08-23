---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# PRD: `bin/land`

This is the PRD in the spec spine for the `bin/land` tool. The TRD and the
acceptance criteria derived from this document follow at the TRD/AC stage; §6
below states the criteria at the level a PRD carries them.

Its content is dictated by Dave in the decision session that directed this
authorship; the directive file `docs/cycles/bin-land-spec-20260823T190444Z.md`
@ `9be1f68a` is the origin of that wording and this document does not restate
it as if it were derived from somewhere else. Assertions about this repository
carry a provenance class: *observed*, *inferred*, *told*, *unknown*.

## 1. Problem and intent

Every execution session that lands work walks the same remote-write sequence by
hand: fetch, branch from the default branch, stage, commit, push, verify. The
sequence is not written down in one governed place, so directives carry it as
restated prose, and restated prose drifts.

The research findings at `docs/research/gh-write-friction-20260823T184149Z.md`
@ `49bd6ff4` measured the cost. Over the 90 directive files in `docs/cycles/`,
sentences containing write-path vocabulary are 16.5% of sentences and 21.8% of
characters; sentences carrying sandbox lore specifically appear in 35 of 90
directives (39%), and in the six most recent `pass2` directives write mechanics
run 13.9% to 43.3% of each file (*observed*, per that document). The same
document records that the restatements have already contradicted each other:
eight committed directives instruct one merge mechanism and the most recent
instructs its opposite, with neither superseding the other in any governed
document (*observed*, per that document).

**Purpose.** One invocation replaces the hand-run remote-write sequence in
execution sessions. All sandbox workarounds become tested implementation
detail, never agent-facing instruction (*told* — dictated).

Two standing decisions constrain this and are cited rather than re-argued:

- `DEC-000160` retired the deferred `bin/dispatch`, "whose premise was a
  chat-side commit to gate" (*observed*). `bin/land` does not revive it: it is
  an execution-session tool that lands what the executor already committed and
  reads the result back, not a decision-session tool gating a chat-side write.
  The retirement is cited here so the difference in premise is on the record.
- `policies/remote-write-verification-policy.md` names an open gap in its own
  rules: they verify that a write **landed**, not that what landed is what was
  intended (*observed*). Closing that gap is this tool's distinguishing goal;
  §4 G5 states it as a functional goal.

## 2. Users and use cases

**Primary actor — an execution session.** An LLM agent session carrying out a
directive against a working tree. It uses `bin/land` twice in a typical cycle:
once to land the directive file as its first act, and once to land the work the
directive produced. It has a local clone, whatever credentials the environment
already gave `git`, and no reliable knowledge of what its sandbox permits.

**Secondary actor — Dave, and the decision session.** Consumes the tool's
output as evidence that a landing happened and that the content landed intact.
Does not invoke the tool as part of the write path; merging is his, over the
repository connector (§4, Non-goals).

**Use cases.**

- Land a directive file and report a SHA that a decision session can cite.
- Land a change package at the end of an execution session.
- Establish, or fail to establish, that specific files landed with the exact
  content that was committed.

## 3. User journeys

Top K = 3.

### J1 — land the directive file

- **Actor**: execution session.
- **Trigger**: the session's first act under a directive.
- **Steps**: invokes `bin/land <branch> <message> <directive-path>`; the tool
  fetches, branches, stages the named file, commits, pushes, and verifies; the
  session reads the reported branch, head SHA, and per-file blob match.
- **Expected outcome**: exit 0, and a head SHA the session can report and a
  decision session can cite, established by reading remote state back rather
  than by the absence of an error.

### J2 — land the session's work

- **Actor**: execution session.
- **Trigger**: the directive's work is complete and its gates have run.
- **Steps**: invokes `bin/land` with the branch, a message, and the changed
  files, or with no files to take every change.
- **Expected outcome**: exit 0, and per-file confirmation that the content at
  the remote matches the content committed.

### J3 — a landing that cannot be verified

- **Actor**: execution session.
- **Trigger**: any step fails, or verification does not establish a match.
- **Steps**: the tool stops; it does not retry; it prints what was established
  and what was not; it exits non-zero.
- **Expected outcome**: the session stops and surfaces, holding a report that
  distinguishes what is known from what is unknown. A partial landing is
  reported as partial, never as success.

## 4. Goals and non-goals

### Functional goals

Invocation: `bin/land <branch> <message> [files...]`.

- **G1 — Start from the remote's current default branch.** Fetch origin and
  branch from `origin/main` HEAD, so a stale working tree cannot silently
  become the base of the work (*told* — dictated stale-tree guard).
- **G2 — Stage what was named.** Stage the named files; stage all changes if
  none are named.
- **G3 — Commit with the given message.**
- **G4 — Push, and do not read success or failure out of the transport's
  chatter.** The string `fatal: failed to store: 100001` is non-fatal noise
  from the credential helper and does not indicate that the push failed
  (*told* — dictated; *observed* in the research findings, where the fetch,
  push, and `ls-remote` all emitted it and all succeeded).
- **G5 — Verify content, not landing.** Verify by `git ls-remote` **and** by
  per-file blob-SHA comparison against the state fetched from the remote after
  the push. The comparison is what makes the claim a content claim rather than
  a landing claim; the research findings document demonstrates the technique
  and `bin/aimeta/repo.py` already exposes a `blob_at_rev` primitive for it
  (*observed*, per the research findings). This goal is what closes the gap
  `policies/remote-write-verification-policy.md` names as open.
- **G6 — Emit a machine-readable report.** Branch, head SHA, and per-file blob
  match, each claim labelled *observed* or *unknown*. The tool emits two of
  Core's four provenance classes and no others: a tool observes a fact or fails
  to, and it is never in a position to infer or to be told. This is a subset of
  Core's set, not a redefinition of it. The concrete output format is named at
  the TRD stage.
- **G7 — Exit 0 only on full verification.** On any failure, print what was
  established and what was not, and exit non-zero. Never retry a write. Never
  delete or force-push anything.

G7 is stricter than
`policies/remote-write-verification-policy.md`'s two-consecutive-failures rule
and does not conflict with it: the policy sets the point at which an agent must
stop absorbing failures, and this tool stops at the first one because it never
retries at all.

### Non-functional goals

- **Performance**: no latency target. The only performance-relevant constraint
  is negative: the tool adds no waits, backoffs, or retries of its own beyond
  the git operations it runs (*inferred* from G7).
- **Reliability**: exit 0 is a claim the tool has verified, not a claim it
  finished. Every non-verified outcome exits non-zero with the established and
  unestablished parts named separately.
- **Scalability**: N/A. One repository, one branch, one invocation; no growth
  dimension.
- **Security**: the tool never touches a token beyond what `git` does
  internally, never displays or extracts a credential, and never invokes `gh`.
  It offers no force-push and no delete, so the client-side force-push deny
  rules already in `.claude/settings.json` are not the only thing standing
  between an agent and a destructive write. Threat model: the tool must not
  become a credential surface, and must not widen what an agent can do to the
  remote beyond commit-and-push.
- **Maintainability**: every sandbox workaround is a line of code with a test,
  not a sentence in a directive. A workaround that stops being true is a
  failing test, not drifted prose.
- **Usability**: the reader is an agent. A directive names one invocation
  instead of a sequence, and the report shape is the tool's output rather than
  the session's narration of it.
- **Observability**: the tool prints the state it read back, never a success
  word standing in for it. On failure the output separates established from
  unestablished.
- **Portability / Compatibility**: depends on `git` and on nothing else
  network-facing. The tool makes no assertion about what the sandbox permits;
  it attempts the operation and reports what it observed.
- **Compliance**: N/A. No regulatory, legal, or data-residency dimension. The
  governing constraints are this repository's own policies, cited above.

### Non-goals

- **Controlling sandbox variance.** The script does not make sandbox behaviour
  uniform and does not try to; it survives variance and reports it (*told* —
  dictated). No change inside this repository can make sandbox network
  behaviour uniform across sessions, because the host allowlist is supplied by
  the runner (*observed*, per the research findings).

Out of scope, and stated here so no reader has to infer it:

- **Merging.** The decision session merges, over the repository connector. The
  tool has no merge path.
- **Invoking `gh`.** Never, for anything, including auth checks.
- **Credential extraction or display.** The script never touches a token beyond
  what `git` does internally.
- **Retries.** The tool never retries a write.

## 5. User outcomes and measurement

- **Write mechanics leave directive text.** Signal: the share of directive text
  carrying write-path vocabulary and sandbox lore. Baseline, measured over the
  90 files in `docs/cycles/` at the time of the research: 16.5% of sentences
  and 21.8% of characters carry write-path vocabulary; sandbox-lore sentences
  appear in 39% of directives (*observed*, per the research findings).
  Mechanism: recount over directives written after adoption.
- **The content-verification gap closes.** Signal: a landing whose remote
  content differs from what was committed is detected by the tool rather than
  by a human noticing a file got smaller. Mechanism: a test that mutates the
  pushed content and asserts the tool exits non-zero; and, after adoption,
  the absence of any content-loss incident of the class
  `policies/remote-write-verification-policy.md` records.
- **Landings stop being narrated.** Signal: execution reports cite the tool's
  output rather than a session's account of which commands were run. Mechanism:
  reading execution reports and retros.

Not measured, and stated so the list is not read as exhaustive: whether
executor refusals decrease. The research findings record two candidate causes
for refusals of the same shape and does not resolve between them (*observed*),
so no baseline for that signal exists.

## 6. Acceptance criteria

Derived from §4. Each is concrete enough to derive a test case from; the test
substrate is expected to be a bare repository served over `file://`, which makes
the remote half testable offline (*inferred*, per the research findings).

- **AC-LAND-01** — Given a working tree whose checked-out branch is behind the
  remote default branch, an invocation produces a commit whose parent is
  `origin/main` HEAD as of the invocation's own fetch.
- **AC-LAND-02** — Given named files, only those paths appear in the resulting
  commit. Given no named files, every change present in the tree appears in it.
- **AC-LAND-03** — The commit message is exactly the message argument.
- **AC-LAND-04** — Given a push that emits `fatal: failed to store: 100001` on
  stderr and otherwise succeeds, the invocation exits 0. The tool's success
  determination is not derived from stderr content in either direction.
- **AC-LAND-05** — After a successful push, `git ls-remote` for the branch
  returns the same SHA the tool reports as head.
- **AC-LAND-06** — For each file in the commit, the blob SHA at the
  post-push fetched remote branch equals the blob SHA committed locally. Where
  any file differs, the invocation exits non-zero and names that file.
- **AC-LAND-07** — The output carries the branch, the head SHA, and one
  per-file blob-match result, each labelled *observed* or *unknown*, and parses
  mechanically into those fields by the format the TRD names.
- **AC-LAND-08** — Exit status is 0 if and only if `ls-remote` confirmed the
  head SHA and every per-file blob comparison matched.
- **AC-LAND-09** — On any failure the output names what was established and
  what was not, as separate statements, and no failure path issues a second
  write of any kind.
- **AC-LAND-10** — No code path invokes `gh`, force-pushes, deletes a ref, or
  merges. Verifiable statically over the source.

## 7. Risk tolerance

The tool is on the write path of every execution session, so its risk posture
is deliberately conservative and asymmetric: it will fail loudly far more
readily than it will act.

**Accepted.** An invocation that stops with work committed locally but not
verified at the remote. The session is then obliged to stop and surface, and a
human or a later session resolves it. This costs a stall; the alternative — a
retry — risks a second write against unknown state, which is the failure class
`policies/remote-write-verification-policy.md` exists to prevent.

**Accepted.** An invocation that refuses to proceed on a condition that turns
out to be benign. A false stop is cheap; a false success is not.

**Not accepted.** Any write the tool does not read back. Any destructive
operation: force-push, ref deletion, merge. Any handling, display, or logging
of a credential. Any output that reports a landing the tool did not observe.

**Escalation.** Anything the tool cannot establish is reported as unknown and
handed to the session, which stops and surfaces it. The tool never decides that
an unverified landing is acceptable; that judgment is Dave's.

## 8. Open product questions

- **Q1 (dictated; must remain open at this stage).** Whether directive-file-
  first landing becomes a mode of `bin/land` or stays two invocations. Resolved
  by: Dave's decision at the TRD/AC stage.
- **Q2 (dictated).** The binary name `land` is provisional, pending Dave's
  `LEXICON.md` check. `LEXICON.md` carries an active retirement programme, and
  a term new to the methodology is a vocabulary decision. This document does
  not add `land` to `LEXICON.md`. Resolved by: Dave.
- **Q3 (raised by the author).** Whether a governed standing write-path
  document lands before this tool becomes agent-facing. The research findings
  rank that document first and name it a prerequisite: the tool encapsulates
  the mechanics, but something governed still has to say when to invoke it and
  what its output means (*observed*, per that document). Resolved by: Dave's
  sequencing decision.
- **Q4 (raised by the author).** What `bin/land` does when the named branch
  already exists at the remote — the case J1 followed by J2 produces on every
  cycle. G1 states the branch is taken from `origin/main` HEAD and does not
  say what happens on the second invocation. Resolved by: a stated behaviour at
  the TRD/AC stage; Q1's resolution does not settle it, because the
  "two invocations" answer requires it and the "mode" answer does not remove it.
