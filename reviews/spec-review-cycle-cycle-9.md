# Review: skills/spec-review-cycle.md — cycle 9

Verdict: changes-required
Reviewed: `skills/spec-review-cycle.md` @ `5136960`
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole document, read start to finish against all eleven criteria of
the review rubric, with criterion 10 answered first and separately for each of
its three parts — the cycle procedure, the cycle directive format, and the review
artifact schema. Counts were taken mechanically over the file at `5136960` and
are stated in S13.
Cross-checked: `docs/global-context/core.md` (Acting 11–13; Vocabulary —
Directive, Directive file, Execution block, the three layers),
`docs/global-context/decision-layer.md` (13, 14), `LEXICON.md` (Spec state —
Tranche, Spec branch, Open spec delta, Reconciliation, Claimed; Retired terms),
`operating-model.md` (Source of truth; Agents — must not; Change flow 1),
`roles/reviewer-agent.md` and `roles/spec-reviewer-agent.md` @ `5136960` for what
cycles 17 and 20 left in them, `roles/context-quality-reviewer.md` for which role
runs a rubric cycle, `skills/directive-dispatch.md` for the reciprocal
duplication.
Not inspected: whether `bin/flip-agreed`, `bin/check-frontmatter`, or
`bin/aimeta/expedited.py` exist or behave as the tool-enforcement note describes
(excluded by the directive); the content of `reviews/expedited-log.md` or of
`policies/document-metadata-policy.md`; the eight prior review artifacts for this
document beyond cycle 8's header; whether any existing artifact in `reviews/`
conforms to the schema this file states.
Findings: 14 — 10 blocking, 2 non-blocking, 2 observations
Prior cycle: `reviews/spec-review-cycle-cycle-8.md`
Dave should inspect: S1 — the artifact schema is the single home for review
output shape and the two roles that most need it cannot receive it, which this
session hit while writing this artifact; and S2, because deleting the cycle
directive format is a decision about whether a cycle directive is a class of its
own or just a directive.

## Disposition — criterion 10, by part

Three things live in this file. They have three different answers.

**1. The cycle procedure (9–147) — survives, rewritten.** The triage → directive
→ execution → verify-and-re-gate sequence, and Reconciliation's four steps, are
procedure no foundation file states, and no other file in a
spec-reviewer bundle states them. It earns its place. What must go from it is the
transport layer it was built on: uploads, the MCP prohibition, the fallback path,
and "Claude Code" as the name of the execution layer (S4, S5). The Reconciliation
argument (135–147) goes as rationale; its four numbered steps stay (S8).

**2. The cycle directive format (149–197) — retired.** Core's `Directive` is the
single home for what a directive is, and this template contradicts it (S2). One
requirement survives the deletion and belongs in the procedure instead: one
decision entry per finding, *including rejections*, because a rejection recorded
nowhere is a decision lost — Core rule 4. The defaults paragraph (182–197) goes
whole (S3).

**3. The review artifact schema (199–321) — survives, and is misfiled.** Cycle 17
made it the single home for review output shape, and that holds: verified by
reading `roles/reviewer-agent.md` @ `5136960`, which states no artifact shape at
all, and `roles/spec-reviewer-agent.md` @ `5136960`, which says only that the
role "returns a review artifact." Nothing else in the repository states the
verdict line, the header block, or the finding fields. But it is not part of this
skill's procedure, and this file's audience does not reach the roles that write
artifacts in it (S1). It should be its own file.

The file therefore does not survive as one file. Its three parts have three
homes: the procedure stays here, the directive format is deleted, and the schema
is extracted.

## S1 — blocking
Claim: The review artifact schema is the single home for review output shape, and
the file it lives in is not delivered to two of the three roles that must write
one.
Location: `skills/spec-review-cycle.md:4` and `:199-321`
Evidence: verified by running `git show 5136960:roles/reviewer-agent.md` and
`git show 5136960:roles/spec-reviewer-agent.md` and grepping both for
`verdict|artifact|blocking|schema` — `roles/reviewer-agent.md` returns no match
and states no output shape; `roles/spec-reviewer-agent.md` matches only at line 9
("returns a review artifact") and line 53, neither of which describes the
artifact. Verified by reading `roles/context-quality-reviewer.md` @ `5136960`:
"The Context Quality Reviewer runs as an execution session and returns a review
artifact in the review artifact schema's shape." This file's audience is
`[spec-reviewer-agent, architect-agent, chief-of-staff, human]` — it contains
`spec-reviewer-agent` but neither `reviewer-agent` nor `context-quality-reviewer`.
Consequence: a Context Quality Reviewer bundle contains a role document that
points at "the review artifact schema's shape" and does not contain the schema;
the agent must invent the verdict vocabulary, the header block, and the finding
fields, and every artifact so produced diverges. The same holds for a Reviewer
Agent bundle. This is not hypothetical — it is the condition this session
executed under.
Fix: extract 199–321 into its own file whose audience names every role that
writes a review artifact — at minimum `context-quality-reviewer`,
`reviewer-agent`, `spec-reviewer-agent` — and leave the procedure here. Adding
the two roles to this file's audience would also close it, at the cost of
shipping the whole cycle procedure to roles that do not run the cycle.
Related: S10, S11

## S2 — blocking
Claim: The cycle directive format defines a directive as a document with seven
headed fields, which contradicts Core's definition of a directive, and it states
a model name where Core requires a tier.
Location: `skills/spec-review-cycle.md:149-180`
Evidence: verified by reading `docs/global-context/core.md` Vocabulary —
"**Directive** — the complete package handed to an execution session: one line
stating route (fresh or existing session) and model tier, then the execution
block as a paste block." The template at 151–177 makes the directive a markdown
document headed `# Cycle <n> Directive — <project>` with `Date:`, `Route:`,
`Model: <model — default Opus 5>`, `Documents in scope:`, `## Decisions`,
`## Deferred / out of scope`, and `## Execution notes`; 179–180 names the
required fields.
Consequence: an agent following this emits a directive naming a model rather than
a tier — a criterion 8 defect in every directive the class produces — and
conflates the *directive* with the *directive file*, which Core distinguishes.
The two definitions are in different files that a spec-reviewer bundle carries
together, so the conflict is live, not latent.
Fix: delete 149–180. Carry one requirement forward into the Procedure: the
directive file records one decision entry per finding, including rejections.
Related: S3, S6

## S3 — blocking
Claim: The defaults paragraph restates `skills/directive-dispatch.md` and Core at
length, in rationale register, and cites another file by path four times and by
section number twice.
Location: `skills/spec-review-cycle.md:182-197`
Evidence: verified by running `grep -n` over the paragraph —
`skills/directive-dispatch.md` at 183, 188, 197; `LEXICON.md` at 193 and 197;
`§1 Route` and `§2 Model` at 188 and 190; `Opus 5` at 182 and 189. Its operative
content ("All three requirements are stated per directive") is Core's `Directive`
sentence "All three stated every time."
Consequence: sixteen lines arguing for a rule stated in two other files in the
same bundle, pinned to section numbers in a document this artifact recommends
retiring (see `reviews/directive-dispatch-cycle-9.md`), so the citations break
either way.
Fix: delete 182–197.
Related: S2

## S4 — blocking
Claim: The document names a vendor tool as the execution layer, eight times, and
makes the whole procedure conditional on it.
Location: `skills/spec-review-cycle.md:14`, `:69`, `:71`, `:75`, `:79`, `:103`,
`:105`, `:327`
Evidence: verified by running `grep -nEo 'Claude Code|Claude'` over the file —
"Claude Code" at 14, 69, 71, 75, 79, 103, 327 and "Claude" at 105. Line 14 reads
"Chat is the decision layer. Claude Code is the execution layer," against
`docs/global-context/core.md`'s "**execution** — an LLM agent session"; 103 heads
a section "Fallback (no Claude Code available)". `operating-model.md` (Agents —
must not) forbids storing durable policy only in vendor-specific tooling.
Consequence: an agent reading this in a bundle, in any harness that is not that
product, reads a procedure addressed to something it is not, and reaches a
fallback section telling it to do something else — so the vendor name changes
which procedure the agent believes applies to it.
Fix: say "the execution session" at 14, 69, 71, 75, 79, 327. Delete 103–106 or
restate it without the vendor: the edit set is emitted for Dave to apply locally
when no execution session is available.
Related: S5

## S5 — blocking
Claim: The Hard constraints mandate a chat-and-upload transport, and prohibit a
tool class, that a bundle reader can neither perform nor verify.
Location: `skills/spec-review-cycle.md:29-42`
Evidence: verified by reading — 33–34 requires documents to "enter chat as
uploads … as attachments on the first message"; 35–38 states "Full documents
never leave chat. No full-file pushes through MCP tools during a cycle," citing
`skills/directive-dispatch.md` and
`policies/remote-write-verification-policy.md`; 36–37 restates that the directive
leaves as a paste block, which Core's `Execution block` states.
Consequence: three of the four hard constraints govern a decision session's chat
mechanics, in a file whose audience is four execution-side and human roles; the
executor that receives them cannot act on any of them, and the one constraint it
can act on — reviewed SHAs recorded — is fourth.
Fix: keep 29–32 (one conversation per cycle) and 39–42 (reviewed SHAs recorded,
and the mid-delta note). Delete 33–38.
Related: S4, S9

## S6 — blocking
Claim: Procedure steps 6 and 8 restate Core rules the executor already has.
Location: `skills/spec-review-cycle.md:71-74` and `:79-80`
Evidence: verified by reading `docs/global-context/core.md` — step 6 ("writes the
pasted directive verbatim to the named path, commits it, and reads the SHA back
from git") is the `Execution block` definition plus rule 12 ("A tool's success
response is a claim … Read current state before retrying a write that appeared to
fail"); step 8 ("If a directive item cannot be executed as written, Claude Code
stops and surfaces it") is rule 11 verbatim in substance.
Consequence: criterion 4, and the restatement is where the vendor name enters the
procedure twice (S4).
Fix: delete step 8. Reduce step 6 to what is specific to a cycle — that the SHA
the executor reports is what the decision record cites.
Related: S4

## S7 — blocking
Claim: The tool-enforcement note is a dated implementation changelog carrying six
path references and one tool-internals citation.
Location: `skills/spec-review-cycle.md:91-101`
Evidence: verified by reading — "**Precondition on the agreement flip — enforced
by tool since 2026-08-02.**" followed by `policies/document-metadata-policy.md`,
`reviews/expedited-log.md`, `bin/flip-agreed`, `bin/check-frontmatter`,
`bin/aimeta/expedited.py`, and `OPEN-ITEMS.md` — "see the resolved entry in
`OPEN-ITEMS.md` for what the check does and does not cover."
Consequence: eleven lines explaining why a check exists, to a reader who cannot
open any of the six files and does not run the check; the one operative sentence
for an agent — the cited SHA must resolve to an entry in the log — is buried in
the middle of the argument.
Fix: delete 91–101. If the agent needs the precondition, state it in one sentence
naming no path and no tool.

## S8 — blocking
Claim: Reconciliation restates LEXICON's definitions and then argues for them
across three paragraphs.
Location: `skills/spec-review-cycle.md:110-118` and `:135-147`
Evidence: verified by reading `LEXICON.md` Spec state — **Open spec delta**
("During it Dave edits spec documents freely, with no reviewer gate and no
per-edit ceremony"), **Reconciliation** ("the whole accumulated diff goes through
the reviewer gate **once** — once per delta, not once per edit"), **Spec branch**,
**Claimed**. Lines 110–113 restate the first two; 135–141 ("Why this holds
`agreed` honest") and 143–147 ("A reconciliation may be invoked early") are
argument; 115–117 defends the word "once" that LEXICON already qualifies.
Consequence: the definitional weight is carried twice in one bundle, and the
39-line section contains 15 lines of procedure.
Fix: keep the four numbered steps at 119–133 — they are the procedure LEXICON
does not state, and step 4's ordering constraint is load-bearing. Delete 110–118
and 135–147.
Related: S5

## S9 — blocking
Claim: Which role performs the re-gate at step 10 is left to inference, and for a
rubric cycle two roles can both claim it.
Location: `skills/spec-review-cycle.md:85-86`
Evidence: verified by reading — step 10 reads "Hand the revised documents back to
the reviewer for the gate re-check," naming no role. Verified by reading
`roles/spec-reviewer-agent.md` @ `5136960`: "Review of governed instruction
documents against the review rubric belongs to the Context Quality Reviewer, not
to this role; Depth 3 looks for contradictions across the corpus and cedes the
rubric review to it." Verified by reading `roles/context-quality-reviewer.md` @
`5136960`: its scope is "Every governed instruction document," and it cedes only
the PRD, TRD, and derived acceptance criteria.
Consequence: the boundary is stated correctly in the two role documents and
erased here by the bare word "the reviewer" — and this file, which governs the
cycle, is delivered to `spec-reviewer-agent` and not to
`context-quality-reviewer`, so the role that runs a rubric cycle never sees the
procedure and the role that does see it is the one that cedes the work.
Criterion 11.
Fix: name the role at step 10 by cycle class — the Spec Reviewer for a spec
cycle, the Context Quality Reviewer for a rubric cycle — and fix the audience per
S1.
Related: S1, S10

## S10 — blocking
Claim: The Purpose scopes the skill to spec documents while the schema it
contains governs artifacts for every reviewed document.
Location: `skills/spec-review-cycle.md:11-15` against `:199-249`
Evidence: verified by reading — Purpose reads "Execute one external-gate review
cycle over spec documents (PRD, TRD, or any canonical document)"; the schema
section governs artifacts in `reviews/` generally, gives
`policies/document-metadata-policy.md` as its worked filename example, and states
that this skill's own artifacts are `reviews/spec-review-cycle-cycle-<n>.md`.
Consequence: a reader deciding whether this file applies to a rubric cycle over a
skill document gets "spec documents" from the Purpose and a policy document from
the schema's example; the file does not answer its own scope question.
Fix: resolved by S1's extraction — the procedure keeps the Purpose it has, and
the schema states its own scope, which is every review cycle.
Related: S1, S9

## S11 — non-blocking
Claim: The Output section restates the procedure and reintroduces the vendor name.
Location: `skills/spec-review-cycle.md:323-328`
Evidence: verified by reading — its three bullets restate step 4 (directive
landed by the executor, cited by SHA), step 7 (revised documents committed), and
step 10 (queued for re-gate); the second reads "committed by Claude Code."
Consequence: criterion 4 within the file itself, and the eighth vendor-name
occurrence.
Fix: delete 323–328.
Related: S4, S6

## S12 — non-blocking
Claim: The verdict-vocabulary rationale and the why-verdict-first section are
argument for rules the schema already states.
Location: `skills/spec-review-cycle.md:275-278` and `:316-321`
Evidence: verified by reading — 275–278 explains why `Verdict` avoids the word
`agreed`, citing `policies/document-metadata-policy.md` and
`roles/spec-reviewer-agent.md`; 316–321 argues why the verdict comes first,
having already stated it at 204–205 and 253.
Consequence: criterion 6, and two more path references in the part of the file
that survives.
Fix: keep the operative sentence at 278 ("`ready` means ready for Dave's
agreement") and delete the rest of both.

## S13 — observation
Claim: The mechanical counts behind this pass.
Location: `skills/spec-review-cycle.md`
Evidence: verified by running `grep -noE` over the file at `5136960` — 32
path-shaped references (the highest in `skills/`), of which 6 are to
`skills/directive-dispatch.md` and 4 to `policies/document-metadata-policy.md`; 8
vendor-name occurrences (`Claude Code` ×7, `Claude` ×1) plus 2 uses of `MCP`; 3
model-name occurrences, all `Opus 5`; 2 word-uses of the retired term "dispatch"
(183, 185) beyond the 6 that are part of a filename; 8 rules restated from Core,
the decision layer, or LEXICON. No use of retired "Track" or "sync block"
survives — cycle 8's C1 edits removed them, and that holds at `5136960`.
Consequence: none — these are the counts the findings above are drawn from.
Fix: none required.

## S14 — observation
Claim: The review artifact filename convention survives criterion 9 unchanged and
is the stated convention Core rule 14 defers to.
Location: `skills/spec-review-cycle.md:226-235`
Evidence: verified by reading `docs/global-context/core.md:14` — "**A filename you
generate is `<descriptor>-<timestamp>`** … Where a convention names it, follow the
convention." The section states `reviews/<stem>-cycle-<n>.md`, derives it
mechanically from the reviewed document's path, and resolves the `-cycle` stem
collision explicitly ("this document's own artifacts are
`reviews/spec-review-cycle-cycle-1.md`"). This artifact and its companion were
named by it.
Consequence: none — recorded because S1 moves this text to a new file, and the
convention must move with the schema rather than stay with the procedure.
Fix: none. Carry 226–240 with the extracted schema.
Related: S1
