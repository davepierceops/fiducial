# Retro Triage Board — 2026-08-05

Working artifact. Derived from `wne-crm/retros/index-2026-08-05.md` (canonical;
not duplicated here). Handles are assigned in index order and are local to this
session.

**Corpus verified:** 40 retros, 119 index pointers, all resolving. 38 of 40
retros cited (`193001`, `193024` carry zero findings — thin sessions, not
omissions). Archive matches `origin/main`.

**Status key:** ` ` open · `A` action item · `D` discussion item (needs own
thread) · `M` merged into another handle · `X` closed, no action

---

## crosses — persist across the 2026-08-02 boundary

| # | Claim (short) | Ptrs | St |
|---|---|---|---|
| C1 | **Split — see below.** Original: recommendation rests on unchecked fact or contradicts settled precedent | 10 | M |
| C1a | General heuristic applied without checking whether its preconditions hold in this case | 6 **+1** | A |
| C2 | **Split — see below.** Original: decision agreed in one artifact never propagated | 6 | M |
| C2a | Derived artifacts (Issues, ACs, tracker) hand-maintained in parallel with specs, and drift | 4 | A |
| C2b | Decision recorded below its canonical level — product intent living only in the TRD | 1 | A |
| C3 | Stale session/memory state narrated or acted on without a repo read-sequence | 6 | |
| C4 | Tool timeout carries no information about whether the write landed | 6 | |
| C5 | Decisions presented batched, buried, or as bare identifiers | 5 **+1** | |
| C6 | Execution handoff requires human to interpret or intervene mid-run | 4 | |
| C7 | Environment lacks an assumed capability; each session improvises a workaround | 7 | |
| C8 | Claim stated as established without verification | 4 | |
| C9 | Standing expectation enforced by repeated correction before it exists in a document | 4 | |
| C10 | Pass anchored to a derived artifact misses what the canonical source would expose | 4 **+2** | |
| C11 | Local clone lags origin; its negative report treated as evidence | 3 | |
| C12 | Work existing only locally or in a chat log is invisible to the layer that must act | 3 | |
| C13 | Scoped edit changes one instance, leaves siblings stale | 3 | |
| C14 | Directive carries internal contradiction or self-invalidating constraint | 3 | |
| C15 | Two surfaces write the same artifact without seeing each other | 3 | |
| C16 | Control artifacts carry unreviewed defects and are acted on as authoritative | 3 | |
| C17 | Tracked defect deferred rather than root-caused, recurs | 2 | |

## stops-at — ended at the boundary

| # | Claim (short) | Surface activity | St |
|---|---|---|---|
| S1 | Structural duplication inside specs generates contradictions | reduced | |
| S2 | Spec claim about dependency/vendor/data-model asserted unchecked | active | |
| S3 | One conversation carrying a whole lifecycle exhausts context + payload | active | |
| S4 | Full-document round-trip corrupts the file; verification checks landing not content | active | |
| S5 | MCP writes fail above a payload ceiling | work active, path abandoned | |
| S6 | Coverage claimed from a sample rather than exhaustive check | active | |
| S7 | Finding not converted to tracked work at the moment of finding | active | |
| S8 | ACs written in unassertable form; spec consistent yet behaviorally wrong | active | |

## starts-after — new since the boundary

| # | Claim (short) | Ptrs | St |
|---|---|---|---|
| A1 | Tool/API reports a state that is not the true state | 2 | |
| A2 | Standing note encodes a tooling claim, goes stale, believed because it reads settled | 1 | |
| A3 | Tool call fails on agent's own malformed argument; indistinguishable from transport failure | 1 | |
| A4 | Restating a committed source's wording introduces transcription defects | 2 | |
| A5 | Red-before-green evidence produced by a mechanism that doesn't demonstrate it | 1 | |

## Class D — candidate methodology changes (19)

D1–D19 carried in the index with targets and status. Triaged after the claim
blocks, since several are already answered by decisions made above them.

---

## Named by Dave — contemporaneous, not corpus-derived

Distinct evidence class from C/S/A above. Corpus corroboration noted where it
exists; N6 has none and cannot have any (see below).

| # | Item | Corpus support | St |
|---|---|---|---|
| N1 | Skill for generating directives that enforce what we want | C14, C6, D3, D4, D9, D14 — strong | D |
| N2 | Skill for writing to GitHub | C4, C15, S4, S5, A1, A3, D18 — strong | D |
| N3 | Ticket system | S7, C17 — corroborated under another name; inbox entry 5 | D |
| N4 | Retro skill + habit of saying "do the retro" each session | skill exists at `draft`; habit is the gap (= S7 shape) | D |
| N5 | CoS says "time to rotate", takes ack, then runs the retro | D8, D13, C3 | D |
| N6 | Service artifacts: catalog, golden signals, SLOs, journey SLOs, logging, metrics, tracing | **zero** — invisible to this corpus by construction | D |

**On N6's zero.** Every session in the corpus is spec authoring, review cycles,
or methodology work. Nothing has run in production, so no retro could have
surfaced this. The absence is a scope property of the corpus, not a defect in
it — and it is the reason N6 had to be named rather than discovered.

**N4 + N5 likely collapse.** Both are "CoS notices the moment and asks Dave."
One mechanism, two triggers — not two mechanisms.

---

## Action items

- **AI-3 — C1a: recommendations must state and check their preconditions.**
  Six findings (`193011#3`, `193032#1`, `193027#4`, `180500#4`, `193029#2`,
  `193032#6`) share one defect: a correct general heuristic applied without
  testing whether the conditions that make it correct hold in this case —
  annotate-don't-remove where no migration cost existed; accept-a-sentinel
  where nullable was cheap; "some flakiness is inherent" in an all-mocked,
  local-Postgres architecture; a partial unique index against an implausible
  race using an ORM that can't express it, while the decisive precedent (the
  primary-email invariant, also inexpressible in Prisma, also settled as
  app-level) sat unweighed in the spec. Two were caught only by measurement or
  challenge. Candidate remedy: a recommendation must name the conditions under
  which it holds and confirm they obtain here. Broader than D17, which covers
  precedent search only. Target doc TBD — likely `context-sets/base.md`
  required behavior, since it is cross-role.
  **Severity note:** the original claim line ends "and the human catches it."
  In all ten findings, Dave did. The control that held is his attention — the
  control this methodology exists to stop depending on.

- **AI-4 — C2a: derived artifacts are hand-maintained, so they drift.**
  (`193004#1`, `193006#4`, `193010#2`, and weakly `214500#7`.) Multi-user model
  confirmed but never propagated to the integration layer; AC #7's
  merge-reversibility claim contradicting locked decisions; Issue #15 ACs still
  encoding retry behavior B6 forbids; a repoint list omitting Drip and
  `referralSourceId`; a tracker tag reading "Issue 13 partial" against zero
  criteria. Structural fix available from the repo's own principle — CoS holds
  that *state is computed, never maintained*. Issues and ACs are derived
  artifacts (`policies/source-of-truth-policy.md`) being edited in parallel
  with the specs rather than regenerated from them. Regeneration removes most
  of this class rather than policing it.

- **AI-5 — C2b: a decision recorded below its canonical level.** (`193012#3`.)
  The HouseAnniversary Purchase-only rule existed in the TRD and was never
  backfilled to the PRD — product intent living only in the technical spec.
  The canonical order is PRD → TRD → ACs → architecture summary → Issues, so
  this is not downstream drift; the decision entered the chain beneath where it
  belonged. Remedy is routing, not propagation: a decision must be recorded at
  its canonical level before anything encodes it.

- **AI-6 — decision log is the shared remedy under three claim blocks.**
  Findings refer to decisions by bare identifier — "decision B4", "B6",
  "cycle-6 agreed direction" — so decisions *are* recorded, scattered across
  cycle documents, with no index. Consulting one requires already knowing which
  cycle to open. This is why `180500#4` missed the primary-email precedent
  (C1a), why `193015#4` diverged from cycle-6 (C1a), and what C2b's routing
  problem needs a home for. Global retro inbox entry 1 already sketches the
  artifact (per-project `decisions/`, immutable entries, `decision` and
  `accepted-risk` types) and already flags the missing *consult* obligation.
  Promote from inbox sketch to drafted proposal. Also intersects C5 — bare
  identifiers are exactly what C5 names as a presentation defect.

- **AI-1 — SLO gate hole (from N6).** `operating-model.md` change package
  item 7 requires "SLO status and error budget consumption for affected Top K user
  journeys," and `policies/commit-and-change-control-policy.md` Tier 2 makes
  "any change to a code path for a Top K user journey whose SLO error budget is
  at or below 20% remaining" a consequential-class criterion. Neither *Top K
  user journey* nor any SLO is defined in the methodology, and no artifact
  creates or maintains them. Consequence: a Tier 2 criterion that cannot be
  evaluated cannot fire, so a class of change the policy calls consequential
  cannot be identified as such; and a required change-package field has no
  source. This is a hole in an active gate, distinct from the broader
  service-practice design. Enters via normal spec-review cycle.

- **AI-2 — role audit result (bounded to the change flow).** All nine stages in
  `operating-model.md` have role documents (`pm-em-owner`, `architect-agent`,
  `spec-reviewer-agent`, `test-designer-agent`, `coder-agent`, `reviewer-agent`,
  `skeptic-risk-agent`, `release-manager-agent`). **No stage gaps.** Three role
  docs do not map to a stage: `chief-of-staff` (deliberate), `orchestrator-agent`
  (superseded/frozen), `context-quality-reviewer` (**not inspected** — unplaced).
  Finding: the stage model has no slot for *standing functions*, which is why
  both known gaps went unnoticed — retro facilitator and operational readiness
  are ongoing functions, not stages. Decide whether standing functions are a
  distinct role class or get folded into CoS.

**AI-1 is also an ownership gap, not only an artifact gap.** No stage in the
nine-stage flow is operational readiness. Release Manager assembles evidence;
Skeptic/Risk assesses it; neither *produces* SLOs or journey definitions. The
gate therefore depends on an artifact no role is responsible for creating.

- **AI-7 — rule migration (C9; largest item in the corpus).** ~16 standing
  operating rules were established by mid-session correction and never entered
  a governed document. Some landed in OPEN-ITEMS #30; most did not. Enumerated:
  never auto-retry an MCP timeout (stop, ask for client restart); every Claude
  Code prompt opens with sync-from-origin; prompts are exactly two steps (sync,
  then execute a named committed directive file); every handed block runs
  verbatim, no manual steps inside a fence; tee on handed blocks; handover
  contents (fresh-or-reuse, model, two-step prompt — #30 r4); sync block targets
  the explicit HTTPS remote (#30 r5); failure-reporting protocol (verbatim tool
  name and args, exact error text or its absence, attempt number, read-back
  before retry, never retry silently, missing tool reported as configuration);
  re-fetch a tracker immediately before editing when another agent may write it;
  C-2 checkout-demonstrated red acceptable only when disclosed in the red-run
  section; Reviewer and Skeptic outputs persist to `reviews/` before the PR
  opens; dictated wording carried as a pointer, never restated; one
  self-contained directive file per Claude Code session, pasted as path + SHA;
  scoping questions asked in chat *before* the prompt file is written; each
  one-at-a-time question carries its own context rather than bare document
  references. **Migration, not design** — each rule already exists and is
  already agreed in practice. Route each to a target document through the normal
  spec-review cycle. Sources: `193028#2`, `193032#4`, `041500#6`, `192900#6`,
  `180500#9`, `193027#5`, `214500#4`, `214500#6`, `193019#3`, `193025#3`,
  `193025#5`, `041500#5`, `193027#2`, `180500#2`.

- **AI-8 — tooling-facts artifact, dated and falsifiable (N2).** Empirical MCP
  knowledge scattered across retros plus one falsified handoff note. Known:
  writes fail above ~40KB (`193009#3`); `push_files` at ~110KB hangs 4+ min
  while single-file `create_or_update_file` lands both (`193014#3`);
  `get_file_contents` strips the trailing newline, so full-file round-trips must
  re-append it (`193026#1`); a base64 `content` parameter writes the literal
  base64 string and truncates the file (`193022#5`); client-side result-delivery
  drops can present as 4-minute timeouts while server round-trips complete in
  ~1s (`041500#9`); **and yet** two timed-out writes genuinely did not land
  (`180500#8`), falsifying the standing note that a timeout implies the write
  landed. Add this session: two consecutive 4-minute read timeouts under
  concurrent Desktop sessions, clean read once contention cleared — session
  contention as a mechanism distinct from GitHub MCP unreliability. Per A2,
  every claim carries a date, provenance, and a falsification record; a note
  that reads settled gets believed. **Resolves global retro inbox entry 4** —
  the answer is *not simply fixed*; relax no existing verification directive.

- **AI-9 — directive-authoring constraints (N1).** Discovered, not codified:
  split directives require exclusive working trees; STOP conditions pin to the
  ref the reviewer actually reviewed, never the branch head the directive lands
  on; blanket constraints must not contradict explicit instructions in the same
  file; a Do-not list must not block a required consistency fix; executors
  detecting concurrent tree mutation STOP. (`193025#5`, `192900#1`, `192900#7`.)

- **AI-10 — no action required, recorded so effort is not re-spent.** C3 is
  predominantly the read-sequence working as designed (3 of 4 stale-memory
  findings show the control catching it). S1 (spec structural duplication) ended
  when both specs were agreed 2026-07-22. S5's MCP payload path was already
  abandoned in favour of dictated-edit directives (`192900#8`).

- **AI-11 — skill evaluation pass against a rubric (findings only).** Take
  `/mnt/skills/examples/skill-creator/` as context; evaluate every document in
  `skills/` (and decide whether `roles/` is in scope) and produce findings for
  improvement. Findings only — no rewrites — so output enters the normal gate
  rather than presenting an unreviewable diff.
  **Format mismatch, verified by reading the source:** skill-creator targets
  runtime-loaded skills (directory + `SKILL.md`, `name`/`description`
  frontmatter, description-as-trigger). Repo skills are flat `.md` methodology
  documents with `status`/`last-reviewed`/`audience`, hand-loaded via context
  bundles. Its trigger-optimization (`improve_description.py`) and eval harness
  (`run_eval.py`, with-skill vs baseline subagent comparison, `grader.md`,
  `comparator.md`) optimise an event these skills do not have.
  **Transfers:** <500 lines then add hierarchy; reference files with explicit
  when-to-read pointers; TOC past 300 lines; imperative form; exact output
  templates; worked examples; and *explain why rather than heavy-handed MUSTs*.
  **Does not transfer:** description-triggering, the eval harness, the
  scripts/references/assets anatomy.
  **Risk and mitigation:** without the harness the pass is qualitative, and
  "make it excellent" reliably yields longer and more confident — the failure
  mode this corpus documents, and the shape of three defects introduced during
  AI-9 itself. Every finding must cite a rubric line, and the rubric must carry
  an explicit *reduction* criterion so cutting is a valid recommendation.

- **AI-12 — lexicon conformance pass.** Run the full skill/role suite against a
  second LLM checking conformance to `LEXICON.md`. **Conflict to resolve
  first:** `LEXICON.md` carries a touch rule — files edited for other reasons
  get conformed, no migration project. A full-suite conformance run *is* a
  migration project. Either the pass produces findings that queue against
  future edits rather than landing, or the touch rule is revised in the same
  cycle. Otherwise the first operation performed under the document
  contradicts it. Lowest-risk of the current batch (read-only, findings out);
  run first regardless of the others.

- **AI-13 — CoS must not assume Dave has read a relayed report.** Directives to
  coding agents end in reports Dave pastes to the CoS; the CoS replies as
  though he has read them. He has not and does not intend to. Required
  behaviour: a very brief summary of what he needs to care about, then, where
  approval is needed, the standing question format — one question at a time,
  adequate context carried in the question itself, a recommendation, tradeoffs
  where significant, ending in a y/n question wherever possible. Same principle
  as `180500#2` (*imagine me as an LLM without context*), now applied to
  relayed output rather than document references. The y/n-where-possible
  ending is new and appears in no current document. Target:
  `roles/chief-of-staff.md`. Small surface, no known conflicts.

- **AI-14 — `endchat` is a third trigger, not a fourth mechanism.** Run
  `conversation-retro`, then close with a stop signal. This is the same
  retro-and-stop as N4 (human says "do the retro") and N5 (CoS proposes
  rotation, takes ack, runs it). Three triggers, one skill — build once.
  Note: chat cannot render "large text" reliably; a markdown H1 is the honest
  form.

- **AI-15 — retro skill must capture standing preferences, not only in-session
  corrections.** The retro schema reliably captures corrections that arrive as
  a visible interruption; it drops preferences Dave has repeated across many
  sessions without a single dramatic correction. Evidence: the "end with a y/n
  question wherever possible" preference was requested many times and appears
  in no document, no OPEN-ITEMS entry, and no retro finding across all 40
  retros — while adjacent framing corrections (one at a time, carry context,
  don't bury the decision point) were captured repeatedly. Repetition across
  sessions is *stronger* evidence a rule is load-bearing and unenforced than a
  single in-session correction, and the schema is structurally blind to it.
  Add an explicit prompt to `skills/conversation-retro.md` for standing
  preferences repeated across sessions, held separate from in-session
  corrections. This is why C9 persisted: the mechanism meant to surface it
  could not see its most common form.

## Open questions for Dave — closed set, answer in any order

Recorded so they are not re-asked or regenerated. Nothing else is pending.

1. **AI-11 rubric criterion.** Use "keep the why when removing it changes an
   agent's decision at a boundary; cut the why that only defends the decision"
   as the primary reduction criterion?
2. **AI-11 scope.** Is `roles/` in scope alongside `skills/`?
3. **Six skills' `name`/`description` (OPEN-ITEMS).** Intended to make skills
   runtime-loadable, or metadata hygiene? Affects one rubric line (whether
   description-triggering is worth evaluating). Does **not** gate AI-11's
   shape — an earlier claim on this board that it did was wrong and is
   corrected here.
4. **`endchat` lock.** Engage on Dave's acceptance of the retro rather than on
   emission, with one named unlock phrase?
5. **AI-1.** Minimal marker fix inside Trivium (Tier 2 SLO criterion marked as
   dependent on definitions that do not yet exist), substantive SLO and journey
   work deferred to Quadrivium?
6. **AI-7 routing.** Read the five documents at `f66dd20` and rebuild the
   routing against what exists? The out-of-scope nine was predicted under the
   greenfield assumption that proved wrong.

**Process defect, this session.** Questions were asked one per turn but stacked
across turns — a new question issued before the prior was answered, so the queue
grew faster than Dave could drain it. Same defect as batching within a turn
(C5). Occurred while recording AI-13, which governs question format. Remedy:
maintain the queue here; ask strictly serially; do not issue a new question
while one is outstanding. Second instance the same turn: a question was
referred to as "question 3" — a bare identifier resolvable only by scrolling
to a prior message (C5), attached to an unverified importance claim (C8).
Questions carry their own context inline when asked.

## Discussion items — need their own thread

- **N6 — service practice design.** Large design space; own kickoff doc.
  Constraint carried from this session: whatever it produces must bind back
  into the change flow (change package / release gate), not run as a parallel
  track. The org-chart separation that makes it a distinct discipline is also
  the mechanism by which observability rots.
- N1, N2, N3, N4+N5 — scoped after the C/S/A blocks are triaged, since several
  claim-block outcomes will constrain them.

## Decisions made this session

- Hold the index's separation of C1/C3/C10/C11 rather than collapsing them.
  (Dave, this session.)
- Split N6: gate hole handled as an action item now; service-practice design
  spun into its own thread. (Dave, this session.)
- Split C1 three ways on evidence: C1a (6 findings, preconditions-unchecked)
  carries the claim; `180500#5` and `180500#6` reassigned to C10 (unflagged
  propagation from a source doc); `193022#4` reassigned to C5 (decision
  presentation — offering a methodology-forbidden option, plus false binaries).
  (Dave, this session.) Note: this is the opposite operation from the merge
  proposed earlier in the session, which the evidence did not support.
- Split C2: C2a (derived-artifact drift, 4) and C2b (decision recorded below
  its canonical level, 1); `193015#4` reassigned to C1a as a consult failure
  rather than artifact drift. (Dave, this session.)
- Board is a triage board, not a copy of the index — index stays canonical to
  avoid a drift pair.
