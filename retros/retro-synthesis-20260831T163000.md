---
project: fiducial
kind: synthesis
date: 2026-08-31
source: Chief of Staff retrospective session, 2026-08-31 (chat; branch retros-placement-20260831)
prior-synthesis: retro-triage-board.md (2026-08-05, over wne-crm's 40 retros — a different corpus; its action items are carried below as topics)
covers:
  - 0-retro-20260831T0000-fiducial-agreeing-clusters.md
  - github-mcp-reliability-retro.md
  - retro-20260807-194436.md
  - retro-20260811-121500.md
  - retro-20260812-201500.md
  - retro-20260821T170302.md
  - retro-20260822T000000.md
  - retro-20260822T153848.md
  - retro-20260823-211500.md
  - retro-20260823T003000.md
  - retro-20260823T042000.md
  - retro-20260823T190000.md
  - retro-20260823T194500.md
  - retro-20260824T000500Z.md
  - retro-20260824T042000.md
  - retro-20260824T053100.md
  - retro-20260824T160000.md
  - retro-20260824T163000Z.md
  - retro-20260824T2010.md
  - retro-20260825T023500.md
  - retro-20260825T173910Z.md
  - retro-20260826T2130.md
  - retro-20260827T155000.md
  - retro-20260827T233500.md
  - retro-20260829T2045.md
  - retro-20260831T000000.md
  - retro-20260831T0530.md
  - retro-notes-20260824T2020.md
  - retro-triage-board.md
---

# Retro Synthesis — fiducial — 2026-08-31

Synthesis, not a retro. Never overwrites a source retro. A retro not named in
the `covers:` list of any synthesis in this directory is unsynthesized; the
next session computes its input set from that.

## Coverage

29 files read whole: 26 schema retros (`retro-*.md` and the one `0-retro-*`),
plus three non-schema files kept as data — the 2026-08-05 triage board (the
only prior retrospective session, over wne-crm's corpus), the GitHub MCP
reliability retro (2026-08-04/05), and the SRE/engagement retro notes
(2026-08-24). Session dates are the retro's `date:` field, corrected where the
file's own evidence disagreed: `0-retro-20260831T0000-…` was generated
2026-08-31 for a session whose last artifact is PR #217, merged 2026-08-26
(observed, `git log`); its `date:` is now 2026-08-26 and it carries
`generated: 2026-08-31`. All other `date:` fields agree with their cited
artifacts (observed for the 12 files citing a PR or SHA; told, from the
`source:` line, for the rest).

Retro handles used below, by session date: R01 08-04/05 (MCP reliability);
R02 08-05 (triage board); R03 08-07; R04 08-11; R05 08-12; R06 08-21;
R07 08-22 (Pass 1 cycle 26); R08 08-22 (cycles 1–15); R09 08-23 (bin/land
PRD); R10 08-23 (cycles 16–24); R11 08-23 (re-gate); R12 08-23 (Pass 2
opening); R13 08-23 (Pass 2 items 1–3); R14 08-24 (bin/land TRD hub);
R15 08-24 (directive-tooling agreement); R16 08-24 (directive-tooling spec);
R17 08-24 (bin/land cycles 3–9); R18 08-24 (bundle regen, DEC-000190);
R19 08-24 (Illuminait air-gap brief); R20 08-24 (recovery session);
R21 08-24 (SRE notes); R22 08-25 (bin/land cycle-3 triage); R23 08-26
(dedup passes); R24 08-26 (agreeing clusters); R25 08-27 (PRD rewrite
session); R26 08-27 (cycles 21–22); R27 08-28 (TRD joint flip); R28 08-29
(writing); R29 08-31 (invariants arc).

## Topics

Deduplicated across the corpus. `n` is the number of retros raising the
topic; `latest` is the most recent session date among them. `State` is
against `main` at 37c6818 as read this session: *landed* means governed text
states it, *tracked* means it is on OPEN-ITEMS or in a staged directive,
*open* means neither. Where two retros disagree the disagreement is stated,
not resolved.

| # | Topic | n | latest | raised in | State |
|---|---|---|---|---|---|
| T01 | Read the governing text and the tree before drafting; a fact in memory is the trigger to read, not to proceed. Includes: verify `bin/` flags by `--help`, never assert tooling from a decision-log entry, re-label inherited observations as *told* on receipt | 9 | 08-28 | R03 R07 R14 R18 R20 R24 R25 R27 R29 | landed (Core 6, 8); recurrence is an enforcement signal, not a text gap — the lint and generator are the fix |
| T02 | Directive self-consistency: blanket constraint vs instruction, diagnosis frozen as a constraint, sweep scope vs Do-not, a self-check that binds the directive's own dictated text; read every constraint against every instruction before sending | 6 | 08-31 | R03 R15 R16 R18 R25 R29 | landed in part (authoring skill bullet); the rest is `bin/check-directive`, adoption pending the consolidation cycle |
| T03 | Working-tree mechanics: disposition as assignment not prohibition; `$TMPDIR` worktrees; `--no-track`; holder check before creation; reuse with HEAD re-pinned; own-worktree removal as the last act with status as the report's final line | 9 | 08-31 | R09 R13 R16 R17 R18 R23 R26 R27 R29 | landed (disposition rule, invariants Report region); holder check and removal staged in the consolidation directive |
| T04 | Sandbox lore has no canonical home and is re-carried per directive: push without `-u`, keychain noise on every remote op, `gh` cannot reach the API, REST/curl fallback, scratch clones, pre-existing red sets by baseline | 10 | 08-26 | R10 R11 R12 R13 R16 R17 R18 R20 R23 R02 | landed in part (invariants Sandbox region); the rest open — every retro says "generator-encapsulation candidate" |
| T05 | One connector, many chats: a second active chat means no connector writes; route line names one session; CoS read-sequence needs a "what else is running" check; connector contention → read from a sandbox clone | 5 | 08-31 | R18 R23 R24 R29 + this session | route rule staged; the read-sequence check is open; the underlying constraint (one chat holds GitHub) is unrecorded anywhere governed |
| T06 | Every carried claim carries its class: report-derived facts in directives, expected-output lines, test counts (which are environment-specific), a baton's *observed* is the successor's *told* | 7 | 08-31 | R13 R14 R20 R25 R27 R29 R01 | landed (Core 6); directive form staged; "count carries its environment" open |
| T07 | Remote-write discipline: a timeout carries no information about landing; read state before retry; verify content not just landing (stats/size); never regenerate a large governed file over the connector; small verified diffs only; connector writes bypass the hook | 9 | 08-31 | R01 R02 R08 R12 R23 R27 R28 R29 R20 | tracked (remote-write-verification policy with a stated known gap; two OPEN-ITEMS entries); the "no whole-file regeneration" rule is open |
| T08 | The baton: one paste block, pasted as the successor's first message; carries decisions and pointers; baton before retro; directive before baton when context is loaded; the baton's next-in-order is Dave's ruling and the successor dispatches item one unasked | 7 | 08-31 | R07 R12 R13 R16 R20 R29 R11 | landed (Decision Layer 12, 13). **Disagreement:** DL 13 says a baton "carries pointers and state"; R20 says a baton carries never computed state — state is re-read from the repo. Dave's to rule. "Dispatch item one" is open in governed text |
| T09 | Review-cycle economics: state the agreement bar and gate cadence at loop start; a re-gate disposes findings and takes no new decisions; budget confirmation cycles (47→12→6→2→1→0); when findings stop shrinking in kind, change instrument; findings below the document's stage go to the next stage's questions; triage a defect class before its instances; ready-with-findings suffices | 7 | 08-28 | R09 R11 R16 R17 R22 R27 R13 | tracked in part (convergence-process canonization owed); the re-gate-takes-no-decisions rule and the stage-level routing are open |
| T10 | Spec and tests converge together and flip jointly; a spike step (time-boxed, findings-only) is missing; mutation that survives green is a coverage finding; an orchestrator role is undefined; the expedited path was stretched to a 1,400-line TRD | 3 | 08-28 | R17 R27 R19 | tracked (canonization owed); spike, mutation-in-DoD, orchestrator role, expedited reconciliation open |
| T11 | Multi-document gates over a branch: one artifact, stem names the branch, `Reviewed:` lists documents, `Baseline:` carries the pre-change ref | 3 | 08-26 | R23 R24 R11 | tracked (OPEN-ITEMS candidate); practice has run ahead of the skill four times |
| T12 | Governed documents carry substance only; findings dispositions, provenance tags, changelog prose live in review artifacts and cycle directives; cut restatement and rationale before showing a draft | 4 | 08-27 | R06 R24 R26 R25 | tracked (OPEN-ITEMS candidate) |
| T13 | Rubric and dedup discipline: criteria 3/4/6/11/12 are absence tests; the agent-instruction-not-authoring-principle test; the bundle invariant (a rule leaves file A only if home B's audience covers A's); criterion 10 applied per rule, which is the row-granular bundle model; confirm same-rule not same-text before collapsing | 6 | 08-29 | R06 R11 R20 R23 R24 R28 | tracked (three OPEN-ITEMS candidates); the per-rule criterion 10 is a bundle-system PRD input |
| T14 | Bundle staleness and format: stamp commits-behind-HEAD and generation age; regenerate after any rename touching the file set; filename and header per DEC-000210; the CoS bundle in the project is stale by construction | 6 | 08-24 | R06 R08 R15 R18 R20 R16 | bundle-system PRD input (one item already on OPEN-ITEMS) |
| T15 | "Landmine" is reserved for a consequence Dave would act on differently if unnamed; a label that fires on routine events trains the reader to skip it | 3 | 08-29 | R25 R28 R29 | landed in part (DL 3 sharpened 08-29); the test wording is an OPEN-ITEMS candidate |
| T16 | Register of triage and questions: say what the item is before the choice; conclusions first; one question, own context inline, y/n where possible; never stack questions across turns; don't offer the shortcut; surface the broad option; restate the open question after multi-report turns | 7 | 08-26 | R02 R04 R10 R11 R24 R20 R16 | landed in part (DL 1, 2, 4); "what it is before the choice" and "y/n where possible" live only in memory and the baton |
| T17 | Standing preferences repeated across sessions are invisible to the retro schema (it catches interruptions, not repetition); a spoken rule enters governed text the same turn; Dave has named the same failure across sessions more than once | 5 | 08-31 | R02 R08 R10 R29 R25 | open — the retro skill has no prompt for it; the strongest single finding of the 08-05 board (AI-15) never landed |
| T18 | Retro mechanics: retro must read nothing from and write nothing to GitHub; `date:` is the session's last interaction, not generation; a synthesis names what it covered; three triggers (Dave says retro / CoS proposes rotation / endchat) are one skill; the connector landing path was never verified end-to-end | 6 | 08-31 | R02 R10 R12 R13 R20 + this session | open — one full cycle on `skills/conversation-retro.md` (on the ineligible list), queued today |
| T19 | Command blocks: parse-atomic on paste (heredocs, multi-line strings stall an interactive shell); a paste block cannot contain a ``` fence — inner fences are `~~~`; an expected-output line is observed in the same environment or is qualitative; a block never pushes `main` | 5 | 08-27 | R03 R18 R23 R25 R04 | landed in part (copyability, one-line expected output); the fence rule, environment rule, and never-push-main are open |
| T20 | Executor stop wording: stop on any unintended mutation including the executor's own; a self-recovery is a stop; dispositions are intent — verify against the counterparty artifact and disclose deviations; carry the remedy with the ban | 5 | 08-28 | R12 R13 R24 R25 R27 | landed (invariants Stop region uses the intent wording); "disposition is intent" is open |
| T21 | Dictated wording: carry as a pointer; reviewer Fix text verbatim into the revision directive unless the record states the departure; state intent not wording for what the executor drafts; a directive that dictates wording cites its source or marks it new | 5 | 08-31 | R08 R09 R22 R29 R11 | landed in part (pointer rule); Fix-verbatim and cite-or-mark-new are open |
| T22 | Consistency sweeps: every fix names its seam and expects the sweep to catch the cycle's own edits; a Do-not names the sweep exemption; position-bearing derived artifacts get a mechanical re-check; base guards name files, not directories | 5 | 08-31 | R14 R15 R18 R23 R29 | landed in part (Core 13; base-guard rule staged); the seam-sweep and mechanical re-check rules are open |
| T23 | Session shape: narrow scope is a context-quality control; hand off before the next directory, not after; the CoS says "time to rotate" and takes an ack; the autonomous overnight run is a proven pattern with no skill | 5 | 08-24 | R04 R10 R13 R02 R20 | open — no rotation trigger and no autonomous-run skill exist |
| T24 | Decisions at their canonical level: a per-project decision log (now `decisions/log.md`); decisions logged in the session that makes them; six decisions from the 15-hour session still unlogged; state computed not maintained, and the rule register/`bin/state` as computed artifacts | 5 | 08-26 | R02 R23 R15 R25 R20 | landed (decision log exists, DL 9, 10); six decisions owed (OPEN-ITEMS); `bin/state` and a `bin/rules` open |
| T25 | The trivial-additive fast lane: an owner-approved, tool-verifiable-green change that is additive should not route through the full override/directive/PR machinery; the doc-only and expedited paths do not cover it | 2 | 08-24 | R03 R17 | open |
| T26 | Files handed to Dave go to `~/Downloads`, named to sort to the top; long documents are presented rendered and navigable, not raw in the pane | 2 | 08-27 | R20 R26 | open — lives only in memory |
| T27 | Discovery and brownfield engagements: an acquisition phase with its own evidence rules; a spike needs a definition and a coverage record; `unknown` is a deliverable; a no-repo CoS variant; what target detail may leave the corpus; a static site's search index is the whole corpus | 2 | 08-24 | R19 R21 | tracked (Illuminait retro and gap analysis, parked) |
| T28 | Skills and roles conformance: `name`/`description` on every skill; a lexicon pass; roles written before rubric criterion 5 carry a human register (writer.md was rewritten); a criterion with no reviewer is a wish; a prohibition is replaced by a per-instance test | 4 | 08-29 | R02 R28 R06 R25 | tracked in part (skills conformance pass, name/description entry); the role-register audit and criterion-5 affirmative test are open |
| T29 | The SLO gate hole: the consequential class and the change package both reference Top K journeys and SLO budgets that nothing defines or maintains, so a gate criterion cannot fire; service-practice design (N6) is invisible to this corpus by construction | 1 | 08-05 | R02 | open since 08-05; disposition of the board's AI-1 unknown |
| T30 | MCP failure epistemics: "failures" are Claude instances reporting failures — claims, not telemetry; classify before remedy (lost response / never dispatched / caller error); a dated, falsifiable tooling-facts artifact (AI-8) | 2 | 08-05 | R01 R02 | open — no tooling-facts artifact exists; the connector-failure patterns live in memory and batons |
| T31 | Adapters and reach: the portable thing is the corpus; an adapter restates no rule; how an adopting project reaches fiducial is the bundle-system PRD's question; solve distribution for the user with the fewest tools | 3 | 08-29 | R25 R28 R20 | bundle-system PRD input (CLAUDE.md deleted, PR #224) |
| T32 | `bin/land` and flips: a governed write-path usage document before the tool is agent-facing; flip from a branch containing the review artifact; flip-by-command-block as the standing remote mechanic until then | 3 | 08-31 | R09 R15 R29 | tracked (OPEN-ITEMS gate entry); the flip-from-gate-branch precondition is open |
| T33 | Rule migration: standing rules established by mid-session correction and never entered into a governed document (the 08-05 board counted ~16); the same class recurs in every later retro's "adopted in practice, unencoded" | 4 | 08-31 | R02 R08 R14 R29 | open as a class; individual rules landed piecemeal; no sweep of the 08-05 list was ever recorded |

## Prior board, 2026-08-05 — disposition unknown

`retro-triage-board.md` recorded fifteen action items (AI-1 through AI-15),
six open questions for Dave, and five decisions, over wne-crm's corpus. This
synthesis found no artifact recording which were carried out. By reading
`main` (inferred): AI-6 (decision log) landed as `decisions/log.md`; AI-9
(directive-authoring constraints) landed as the authoring skill and the
directive tooling; AI-13 (question format) landed as Decision Layer 1; AI-14
(three retro triggers) and AI-15 (standing preferences) did not land; AI-1
(SLO gate hole), AI-7 (rule migration), AI-8 (tooling-facts artifact), AI-11
(skill rubric pass) and AI-12 (lexicon pass) have no visible disposition. One
pass over that list, recording landed / superseded / still open per item, is
owed before the board can be called synthesized.

## Follow-ups — bundle-system PRD inputs

Product requirements the PRD carries, drawn from T13, T14, T31 and the
OPEN-ITEMS entries already pointing at it:

1. Every bundle states its provenance and staleness at the top: source repo,
   HEAD SHA, generation time, and — at load, if the consumer can compute it —
   commits behind the current default branch (T14; R06, R08).
2. Filename and header per DEC-000210 (`methodology-context-bundle-<stamp>.md`,
   `Source: @ <HEAD>`), closing the `bin/bundle` mismatch on OPEN-ITEMS (T14).
3. Regeneration triggers are stated: any rename touching a bundle's file set,
   any agreement flip of a member, any audience change (T14; R15, R18).
4. Selection is per rule, not per file, or the PRD states why file granularity
   is kept — criterion 10 per rule and the rule register as the seed of a
   row-granular model (T13; R20, R23).
5. Distribution through GitHub Releases, one file per audience, pinned to the
   generating SHA; new audience values need no code change; every writing
   bundle carries the Criteria, the author's Voice, and the Voice template
   (already recorded on OPEN-ITEMS, 2026-08-28).
6. How an adopting project reaches the corpus: no adapter restates a rule;
   the answer must work for a user with a document and a chat and nothing
   else (T31; R25, R28).
7. Sandbox and connector lore as a bundle member or companion document with a
   stated audience, so directives stop carrying it (T04; every retro from R10
   to R23).

## Follow-ups — methodology, for OPEN-ITEMS

New entries (not already tracked), each a candidate for a review cycle on the
named document, none decided here:

1. `skills/conversation-retro.md`, one cycle carrying four changes: reads
   nothing from and writes nothing to any remote — the file is handed in chat,
   placement is a separate command-block step; `date:` is the session's last
   interaction, derived from the last dated artifact the session touched, with
   `generated:` added; a synthesis lists the filenames it covers; a prompt for
   standing preferences repeated across sessions, held separate from
   in-session corrections (T17, T18).
2. `roles/chief-of-staff.md` read-sequence: a "what else is running" check —
   other chats holding the connector, other worktrees — before any connector
   write; and the constraint itself, one chat holds GitHub, stated where
   decision sessions read it (T05).
3. Decision Layer 13 vs R20: rule on whether a baton carries state or only
   pointers to where state is computed (T08). Dave's Core-9 ruling.
4. Decision Layer 5 or the Chief of Staff role: the baton's ordered list is
   Dave's ruling; the successor's first response dispatches item one (T08).
5. Decision Layer: "say what the item is before the choice" and "y/n where
   possible" — repeated across sessions, in no governed text (T16, T17).
6. `skills/spec-review-cycle.md`: a re-gate disposes findings and takes no new
   decisions; the agreement bar and gate cadence are stated at loop start;
   findings below the document's stage are routed to the next stage's
   question list (T09).
7. `skills/command-blocks.md`: no ``` fence inside a paste block (inner fences
   `~~~` with a fence note); an expected-output line is observed in the
   environment the block runs in, or is qualitative; a block never pushes the
   default branch (T19).
8. `skills/directive-authoring.md`, after the consolidation cycle: reviewer
   Fix text carried verbatim unless the record states the departure; every
   fix names its seam and its sweep; position-bearing derived artifacts get a
   mechanical re-check; dispositions are intent (T20, T21, T22).
9. The trivial-additive fast lane (T25): scope it or refuse it.
10. Session rotation: a stated trigger for the CoS to propose handoff, and a
    named skill for the autonomous overnight run if it is to recur (T23).
11. `~/Downloads`, sort-to-top naming, and rendered presentation of long
    documents, one line in the Decision Layer (T26).
12. A dated, falsifiable tooling-facts artifact for the connector and the
    sandbox (T30, T04) — or the decision that the bundle-system PRD's item 7
    is that artifact.
13. The SLO gate hole (T29): either define Top K journeys and SLO budgets or
    remove the criterion and the change-package field that reference them.
14. The 08-05 board pass (previous section): one disposition per action item.
15. Test counts carry the environment they were observed in (T06).

Already tracked on OPEN-ITEMS and confirmed by this corpus (no new entry):
convergence-process canonization (T09, T10); multi-document gates (T11);
substance-only governed documents (T12); rubric negation, bundle invariant,
agent-instruction test (T13); landmine test (T15); executor self-recovery
(T20); six unlogged decisions (T24); skills conformance and name/description
(T28); Illuminait retro (T27); `bin/land` usage document (T32); PRD/TRD
template audience; Critic vs review-artifact audience.
