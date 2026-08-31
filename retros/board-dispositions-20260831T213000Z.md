# 08-05 Board Dispositions

Board: `retros/retro-triage-board.md` (2026-08-05 retrospective, wne-crm corpus,
action items AI-1 through AI-15). Directive:
`docs/cycles/board-pass-20260831T213000Z.md`. Reviewed ref:
`6f9cc79634d6fadf1fbd64180d3658a68fa98f8f`.

One entry per action item, verified against the tree at the reviewed ref plus
`OPEN-ITEMS.md`, `retros/retro-synthesis-20260831T163000.md`, and
`decisions/log.md` DEC-000280–DEC-000300.

---

## AI-1 — SLO gate hole

Disposition: superseded — by Topic walk ruling 10, `OPEN-ITEMS.md` "Topic walk
2026-08-31 — rulings" item 10 (`policies/commit-and-change-control-policy.md`
next cycle). Ruling 10 replaces AI-1's implicit ask (define Top K journeys and
SLOs to fill the gate) with remove-and-relocate: strike the Tier 2 criterion
and the change-package SLO field, and relocate Top K/budget ownership to
`policies/project-setup-requirements.md` at project adoption.
Evidence class: observed.
Notes: pre-ruled by the decision session; verified rather than re-decided, per
directive. Tree check: `policies/commit-and-change-control-policy.md:42` still
carries the old "Top K user journey ... SLO error budget" criterion verbatim —
ruling 10's remove-and-relocate has not landed in the tree; it is a decided
direction on the "Queued next" list (`OPEN-ITEMS.md`, end of file), not yet
executed. No contradiction with the pre-ruling itself (ruling 10 does say this
is where AI-1 disposes) — only with any reading of "disposes into" as "landed."

## AI-2 — role audit result (bounded to the change flow)

Disposition: still-open.
Evidence class: observed.
Notes: `roles/orchestrator-agent.md` no longer exists in the tree (role
removed, consistent with the board's "superseded/frozen" note), but
`roles/context-quality-reviewer.md` still exists with no `stage`/`Activation`
tie into `operating-model.md`'s nine-stage list, and no "standing function"
role class appears anywhere in `operating-model.md` or `roles/*.md`. AI-2's own
question — is a standing-function role class named, or folded into CoS — has
no recorded ruling in `OPEN-ITEMS.md` or `decisions/log.md` DEC-000280–300.

## AI-3 — C1a: recommendations must state and check their preconditions

Disposition: still-open.
Evidence class: observed.
Notes: no rule of this shape exists in `docs/global-context/core.md` (the
successor to the board's cited target, `context-sets/base.md`, which no longer
exists at that path — the corpus was restructured into
`docs/global-context/{core,decision-layer,review-rubric}.md` and
`context-sets/{production-grade-software,spec-and-change-discipline,
testing-and-verification}.md` since the board was written). Grepped
"precondition" across `roles/`, `context-sets/`, `docs/global-context/`,
`policies/`, `skills/`, `operating-model.md`: no hits state a general
recommendation-must-check-its-conditions rule. Neither `OPEN-ITEMS.md` nor the
2026-08-31 synthesis/topic-walk carries this item under any name (C1a is
absent from both). Not superseded, not refused — simply never picked up.

## AI-4 — C2a: derived artifacts are hand-maintained, so they drift

Disposition: still-open.
Evidence class: observed.
Notes: `policies/source-of-truth-policy.md` has no "regenerat*" language, and
no mechanism regenerating Issues/ACs from specs exists in the tree. Decision
Layer rule 9 ("State is computed, never maintained") is the same principle
applied to decision-session artifacts, not to the Issues/AC drift AI-4 names.
Absent from `OPEN-ITEMS.md` and the 2026-08-31 synthesis/topic-walk under any
name.

## AI-5 — C2b: a decision recorded below its canonical level

Disposition: still-open.
Evidence class: observed.
Notes: no "record at canonical level before anything encodes it" routing rule
found in `docs/global-context/*.md`, `policies/*.md`, or
`skills/spec-review-cycle.md`. Decision Layer rule 10 ("check the decision log
... before you govern something it already governs") is adjacent — a consult
obligation — but is not the routing-order rule AI-5 asks for (PRD before TRD
before ACs). Absent from `OPEN-ITEMS.md` and the synthesis/topic-walk.

## AI-6 — decision log is the shared remedy

Disposition: landed.
Evidence class: observed.
Notes: `decisions/log.md` exists (append-only, `DEC-NNNNNN` entries, "never
edited or deleted; a reversal is a new entry whose `Supersedes:` names the old
ID" — matches the inbox sketch's "immutable entries" requirement exactly), and
`ACCEPTED-RISKS.md` exists as the `accepted-risk` type sibling. The consult
obligation ("read the decision log and cite the governing entry by ID") is
Decision Layer rule 10 in `docs/global-context/decision-layer.md`.
`OPEN-ITEMS.md`'s "`bundle base` red" entry independently states "under the
AI-6 landing," confirming the same conclusion from a different angle. The
retro-synthesis document's own inferred read agrees: "AI-6 (decision log)
landed as `decisions/log.md`."

## AI-7 — rule migration (C9; largest item in the corpus)

Disposition: still-open.
Evidence class: observed.
Notes: this is the item `retros/retro-synthesis-20260831T163000.md` topic T33
names directly ("the 08-05 board counted ~16" rules) with status "open as a
class; individual rules landed piecemeal; no sweep of the 08-05 list was ever
recorded." Confirmed piecemeal landing on spot-check: "never bypass the
pre-commit hook" is now a stated rule at `skills/directive-authoring.md:49`;
several other named rules (sync-block-first, one-directive-per-session,
verbatim command blocks) are covered by `skills/directive-dispatch.md` and
`skills/command-blocks.md`. No single artifact ties the ~16 back to AI-7 as a
migration unit, and the board's own list was never swept item-by-item.

## AI-8 — tooling-facts artifact, dated and falsifiable

Disposition: superseded — by Topic walk ruling 13, `OPEN-ITEMS.md` "Topic walk
2026-08-31 — rulings" item 13 ("the lore home ... is the tooling-facts
artifact — entries are dated, falsifiable, and classified"), which folds AI-8's
ask into the Bundle-system PRD cycle 1 rider set rather than a standalone
artifact built now.
Evidence class: observed.
Notes: pre-ruled by the decision session; verified rather than re-decided, per
directive. No file matching `*tooling-fact*` exists anywhere in the tree —
the artifact itself has not been built; ruling 13 settles what it will be and
where it will live (a Bundle-system PRD rider), not that it exists yet. The
synthesis document's own status line for the matching topic (T30) reads "open
— no tooling-facts artifact exists," consistent with this reading.

## AI-9 — directive-authoring constraints

Disposition: landed.
Evidence class: observed.
Notes: all five named constraints are now in governed text. Exclusive working
trees for split directives: `skills/directive-invariants.md:85-99` ("Every
directive states its working-tree disposition ... exclusive assignment").
STOP conditions pin to the reviewed ref: `skills/directive-invariants.md:150`
("Pinned to the reviewed ref {{reviewed_ref}}"). Concurrent tree mutation
stops: same block, line 151. Blanket constraints must not contradict explicit
instructions: `skills/directive-authoring.md:29` ("No blanket constraint may
contradict an explicit instruction in the same [directive]"). Do-not lists
scoped to blast radius: `skills/directive-authoring.md:31` ("Scope Do-not
lists and base guards to the blast radius"). The retro-synthesis document's
inferred read agrees ("AI-9 ... landed as the authoring skill and the
directive tooling").

## AI-10 — no action required, recorded so effort is not re-spent

Disposition: landed.
Evidence class: observed.
Notes: the item is self-disposing — it asserts three sub-claims (C3's
read-sequence working as designed; S1 ended 2026-07-22; S5's MCP path already
abandoned) as already true when written, requiring no further action. Nothing
in the tree, `OPEN-ITEMS.md`, or the decision log contradicts any of the three.
Treated as landed in the sense that its own claim — nothing to do — stands
unchallenged.

## AI-11 — skill evaluation pass against a rubric (findings only)

Disposition: still-open.
Evidence class: observed.
Notes: maps to `OPEN-ITEMS.md`'s "Skills conformance pass — rubric first,
scope undecided" entry, which states the sequencing question (committed rubric
first vs. criteria in the directive) is still unresolved. Topic walk item 8
("Skills-conformance-pass entry (T28)") records scope candidates but defers
the decision to when the rubric is drafted — not yet done. The synthesis
document lists AI-11 among items with "no visible disposition" as of
2026-08-31T163000; the subsequent topic walk gave it a home (a queued pass)
but not a landing.

## AI-12 — lexicon conformance pass

Disposition: still-open.
Evidence class: observed.
Notes: same underlying open item as AI-11 — `OPEN-ITEMS.md`'s "Skills
conformance pass" entry explicitly targets "Anthropic's skill-authoring
guidance, `LEXICON.md`, and this repo's frontmatter policy" together, and AI-12's
own touch-rule conflict ("a full-suite conformance run *is* a migration
project") is restated there. Not run; scope and rubric still undecided.

## AI-13 — CoS must not assume Dave has read a relayed report

Disposition: landed.
Evidence class: observed.
Notes: the core behavior landed in `docs/global-context/decision-layer.md`
Register: rule 1 ("One question at a time. Ask the one that matters most,
wait, then the next.") and rule 2 ("When he pastes output, triage it: one line
per item that needs his judgment, up front; hold or discard the rest.") cover
the brief-summary-before-approval shape AI-13 asks for. The retro-synthesis
document's inferred read agrees ("AI-13 (question format) landed as Decision
Layer 1"). One named sub-clause has not landed: "ending in a y/n question
wherever possible" is absent from `decision-layer.md`'s Register as written —
confirmed by `OPEN-ITEMS.md` follow-up 5 and Topic walk item 1 (T16), which
still list "y/n where possible" as living "only in memory and the baton,"
queued into the (unlanded) Decision Layer cycle.

## AI-14 — `endchat` is a third trigger, not a fourth mechanism

Disposition: still-open.
Evidence class: observed.
Notes: matches retro-synthesis topic T18 exactly ("three triggers (Dave says
retro / CoS proposes rotation / endchat) are one skill"), status "open — one
full cycle on `skills/conversation-retro.md` (on the ineligible list), queued
today." `skills/conversation-retro.md` contains no `endchat` trigger language
at the reviewed ref. `OPEN-ITEMS.md` follow-up 1 and the "Queued next" line
both list the conversation-retro cycle as still to run.

## AI-15 — retro skill must capture standing preferences

Disposition: landed — via T17 (the same-turn encoding line) and the retro
skill's standing-preferences prompt.
Evidence class: observed.
Notes: pre-ruled by the decision session; verified rather than re-decided, per
directive. **Contradiction found:** `skills/conversation-retro.md` contains no
standing-preferences prompt at the reviewed ref (grepped "standing" — one
unrelated hit at line 37); `docs/global-context/decision-layer.md` contains no
same-turn-encoding rule (its Register runs 1–17 with no such line); and
`decisions/log.md` DEC-000280–DEC-000300 (the full range this directive
requires reading) contains no entry stating either rule. The retro-synthesis
document itself states the opposite at its own timestamp: topic T17's status
reads "open — the retro skill has no prompt for it; the strongest single
finding of the 08-05 board (AI-15) never landed," and the "Prior board"
section says outright "AI-15 (standing preferences) did not land." The
`OPEN-ITEMS.md` line the pre-ruling draws on — "T33 closed — the class is
swept by this walk, with the same-turn encoding line and the retro skill's
standing-preferences prompt as the two structural fixes that keep it empty" —
reads, on this session's tree check, as a decision that these two fixes *will*
close the class, not as a record that they have shipped; both are listed on
the still-pending "Queued next" line at the end of `OPEN-ITEMS.md` (the
Decision Layer cycle and the retro-skill cycle). Recorded per directive
instruction: the pre-ruled disposition (landed) is kept; this is the
contradiction for the decision session to triage.

---

Synthesized: yes. Every item AI-1 through AI-15 carries a disposition (15 of
15) — landed (AI-6, AI-9, AI-10, AI-13, AI-15), superseded (AI-1, AI-8), or
still-open (AI-2, AI-3, AI-4, AI-5, AI-7, AI-11, AI-12, AI-14) — per the
directive's own criterion that synthesized means every item carries a
disposition, not that every item has landed. One disposition (AI-15) is
recorded as pre-ruled `landed` despite a tree contradiction noted above, per
directive instruction to keep the pre-ruled disposition and let the decision
session triage it; that contradiction does not unmake the disposition as
recorded.
