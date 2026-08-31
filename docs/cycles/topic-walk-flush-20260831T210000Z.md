You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Land the 2026-08-31 topic-walk flush on OPEN-ITEMS.md and the decision-log catch-up on decisions/log.md, all wording dictated below by the decision session recording Dave's rulings. You do not flip status, do not edit any other file, and do not run bin/flip-agreed. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/topic-walk-flush-20260831T210000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: topic-walk flush and decision-log catch-up 2026-08-31", push with git push origin topic-walk-flush-20260831 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-walk-flush", created by: git worktree add --no-track "$TMPDIR/fiducial-walk-flush" -b topic-walk-flush-20260831 24dab436ba96f7cc4368f184f740636d68f4da2c
Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch topic-walk-flush-20260831, if a branch of that name already exists locally or on origin (git ls-remote origin topic-walk-flush-20260831 returns a ref), or if "$TMPDIR/fiducial-walk-flush" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. Judge every remote operation by the refs it reports and its exit status, not by credential-helper noise on stderr; an operation that exits 0 and reports no refs is not a failure. The reviewed ref 24dab436ba96f7cc4368f184f740636d68f4da2c must equal origin/main or be an ancestor of it; the worktree is created from the reviewed ref itself. In the worktree, OPEN-ITEMS.md must contain the section heading "## Retrospective session 2026-08-31 — follow-ups" exactly once; if not, stop and report.

EDITS, in order. Anchors are exact strings at the reviewed ref; where an anchor is a sentence, match it across line wraps. If an anchor is not found exactly once, stop and report.

E1 — OPEN-ITEMS.md, the section headed "## `skills/directive-authoring.md` consolidation cycle owed — adoption of `bin/directive` waits on it": strike the heading (wrap its text after "## " in ~~ ~~) and insert directly below the heading, as the section's new first paragraph:

**RESOLVED 2026-08-31.** Consolidation revision D-0 plus amendments b, c, d;
gates at cycles 4/5 (ready-with-findings, 0 blocking), 5/6
(ready-with-findings, 1 non-blocking each), and 6/7 (ready, zero findings).
Both documents `agreed` at `reviews/directive-authoring-cycle-6.md` and
`reviews/directive-invariants-cycle-7.md`, both @
afbe7df9924f0449a2f48a408c26c67399595eb8; flips landed by `bin/flip-agreed`
(one self-commit per invocation), PRs #263–#267, all merge commits, main at
24dab436. Adoption is unblocked: directives are generated with
`bin/directive` and linted with `bin/check-directive` from here on. Persisting
items and riders moved to the topic-walk section below.

E2 — OPEN-ITEMS.md, follow-up list item 15 (the line beginning "15. **Test counts carry their environment (T06).**"): append to the end of that item's text: **LANDED 2026-08-31** — the invariants Report region bullet (amendment b, refined by amendment d's arc to the tree axis with a sandbox clause), agreed at cycle 7.

E3 — OPEN-ITEMS.md, the section headed "## `bin/bundle` output format does not match DEC-000210": append as a new final paragraph of that section:

**Folded 2026-08-31 into `specs/bundle-system.md` OQ-5**, which records the
filename/header conflict as Dave's open ruling; this entry closes when OQ-5
resolves and adds nothing to it.

E4 — OPEN-ITEMS.md: append at the end of the file, after the final line of the "## Retrospective session 2026-08-31 — follow-ups" section:

---

## Topic walk 2026-08-31 — rulings

**Source:** the full 33-topic walk over
retros/retro-synthesis-20260831T163000.md, ruled by Dave one topic per turn in
the retrospective decision session, same day. Every topic now has a home; this
section is the record. The follow-up numbers below are the section above's.

**Cycles opened or re-scoped by the walk:**

1. **Decision Layer cycle (one open, several changes).** Rule 13 becomes
   pointers-only — a baton carries decisions, open questions, and pointers;
   every fact about the tree is re-read; one carve-out: a baton may name a
   state the successor would not know to check (a session left running, a
   branch mid-merge), labelled told (T08). Rule 5 gains: dispatch of ruled
   work is emitted, not offered (T08). Rule 3 gains the test: a landmine is a
   consequence Dave would act on differently if it went unnamed (T15).
   Register lines: say what the item is before the choice; y/n where
   possible; after a turn carrying a report or a block, restate the open
   question (T16). A spoken standing rule enters governed text the same turn
   (T17); a decision is logged in the session that makes it (T24); a document
   handed for reading is delivered rendered — the pane is for documents being
   edited (T26). Follow-ups 3, 4, 5, and 11 close into this cycle.
2. **Remote-write verification policy cycle** (`policies/remote-write-verification-policy.md`).
   Four rules: the content-expectation check (size and stats, closing the
   policy's own Known gap); connector writes are creates or small verified
   diffs — an existing governed document is never regenerated whole over the
   connector; any connector write of an in-scope file sets all frontmatter
   explicitly and an executor runs `bin/check-frontmatter --all` on a branch
   before merge; after a timeout on a write, read the PR or commit state
   before re-creating (T07, T11). Plus classify-before-remedy: a reported
   tool failure is classified — lost response, never dispatched, caller
   error, tool defect — before any remedy (T30). The 2026-08-03
   success-shaped-response entry and the 2026-08-06 landing-not-content entry
   fold into this cycle and close when it lands.
3. **Spec-review-cycle skill cycle** (follow-up 6 + convergence, T09, T20).
   A re-gate disposes findings and takes no new decisions — a new decision
   opens its own cycle; the agreement bar and gate cadence are stated at loop
   start, and a gate may be scoped to confirmation of named resolutions;
   findings below the reviewed document's stage route to the next stage's
   question list; a named defect class is triaged before its instances; plus
   the convergence shape — spec and tests revised together, joint flip, the
   decision session mediating, dispositions are intent (the executor verifies
   against the counterparty artifact and discloses deviation). The
   "Convergence process — canonization owed" entry closes into this cycle.
4. **Chief of Staff role cycle** (T05, T23). The one-chat-holds-the-connector
   constraint stated where decision sessions read it; a decision session
   assumes sole hold unless the baton or Dave says otherwise, and treats a
   timeout as contention first, restart second; the baton names any session
   left running, labelled told; and the rotation trigger — the Chief of Staff
   proposes handoff before the next major work item, one line, taking an ack.
   Follow-ups 2 and 10's first half close into this cycle.

**Riders recorded on existing entries and queues:**

5. **`skills/directive-authoring.md` next cycle** (follow-up 8 pile; T02,
   T03, T20, T21, walk evidence): a verification step in a directive binds
   the directive's own dictated text — read every dictated string against
   every self-check before sending; the holder check names a third case, the
   branch existing with no worktree; the reuse form — cite the prior
   directive path @ SHA as companion, `git worktree add "<path>" <branch>`
   with no -b and no --no-track, re-pin, deltas only; carry the remedy with
   the ban; a directive that dictates wording cites its source or marks it
   new; a flip directive states `bin/flip-agreed`'s self-commit behaviour —
   one commit per invocation, never a caller-authored combined commit; the
   Naming example gains the UTC `Z` per the filename decision below;
   per-file test runs use `python3 -m unittest discover -s bin/tests -t bin
   -p <file>`; a long test suite states its expected duration so an
   executor's tool timeout is raised before the run.
6. **`specs/directive-tooling-trd.md` rider queue:** M2's citation pattern
   captures an enclosing backtick or quote as part of the path (observed
   twice, 2026-08-31: backticked citation; the flip directive's quoted
   `--review` argument) — strip delimiters or the skill states citations are
   written bare; and M2 requires the cited SHA to touch the path, which a
   multi-document artifact's tip citation and a flip's artifact citation both
   trip — state the rule's intended reach.
7. **Rubric candidate entry** (T13, T28): add the collapse check — before
   collapsing two duplicate rules, confirm they state the same rule, not
   merely similar text (pass-2b evidence: the clustering over-matched); the
   criterion-with-no-reviewer-is-a-wish test and
   prohibition-becomes-per-instance-test rules cross-reference here from the
   conformance pass.
8. **Skills-conformance-pass entry** (T28): scope candidates recorded — the
   role-register audit (roles written before rubric criterion 5 carry a
   human register; writer.md's rewrite is the precedent), and the two
   test-form rules above; scope decided when the pass's rubric is drafted.
9. **`operating-model.md` next opening cycle** (T10): two riders — a spike
   step (time-boxed, throwaway, permitted before agreement, findings only,
   never shipping code), and mutation-as-coverage-finding (a mutation
   surviving a green suite is a finding; the code's author does not write
   the closing test). The orchestrator question is closed by the
   spec-review-cycle cycle; the expedited-stretch question becomes a
   one-line check at `policies/document-metadata-policy.md`'s next cycle.
10. **`policies/commit-and-change-control-policy.md` next cycle** (T29,
    follow-up 13): remove the Top K / SLO-budget criterion and the change
    package's SLO field — a criterion nothing defines cannot fire and reads
    as coverage — and relocate: a project with user-facing journeys defines
    its Top K and budgets at adoption, stated in the Project Setup
    Requirements policy. The 08-05 board's AI-1 disposes into this.
11. **`context-sets/collab-workflow.md` next opening** (T12): one rider —
    before "ship," the pane content is verified against the diff that
    actually lands; the commit derives from the pane, never from memory of
    the discussion.
12. **`docs/global-context/core.md` next opening** (filename decision): rule
    14's example gains the `Z`.
13. **Bundle-system PRD cycle 1 riders** (T26, T30): replace the three
    hard-coded `~/Downloads` paths and both "sort to the top" phrases with a
    citation of the delivery-directory decision, `--out` remaining the
    override per AC-BN-12; and the lore home (G11/AC-BS-12) is the
    tooling-facts artifact — entries are dated, falsifiable, and classified
    (lost response / never dispatched / caller error / tool defect).
    Follow-up 12 closes into this.
14. **`bin/land` usage-document entry** (T32): two added requirements — a
    flip runs from a tree that contains the review artifact it cites, and
    the document states `bin/flip-agreed`'s self-commit behaviour.
15. **By-title pointer dependency** (gate cycle-4 O-2, record only): the
    criterion-3 by-title reference between the two directive skills holds
    because both carry audience [chief-of-staff, human]; the dependency is
    recorded here and nowhere in either file — an audience change on either
    breaks criteria 1 and 3 silently. Dave weighs whether it ever needs more
    than this record.

**Refusals and deferrals, recorded:**

16. **Trivial-additive fast lane (T25, follow-up 9): refused 2026-08-31.**
    Two instances, both predating the cycle-20 metadata policy. Hitting the
    gap again is itself the trigger for a revisit — the next concrete case
    with no fitting route reopens this entry with itself as the evidence,
    and is not absorbed or worked around.
17. **Autonomous overnight-run skill (T23): deferred until the next run is
    wanted.** Two clean runs exist as evidence; when Dave next says "keep
    going, I'm off to bed," the skill is drafted first — bounds (ruled work
    only, nothing consequential, no flips), stop conditions (any question
    that would go to Dave), wake-up report shape — and that run validates it.
18. **Illuminait / discovery methodology (T27): stays parked**, one note
    added — the spike definition is landing via the operating-model rider
    above; the parked gap analysis does not re-derive it.

**Owned elsewhere, confirmed by the walk:** T01 adoption (landed above); T04
sandbox lore and T31 adapters/reach (bundle-system PRD); T14 staleness and
format (PRD; format entry folded into OQ-5); T33 closed — the class is swept
by this walk, with the same-turn encoding line and the retro skill's
standing-preferences prompt as the two structural fixes that keep it empty.

**Queued next:** the 08-05 board pass (follow-up 14) as a read-only directive
appending a per-item disposition table (AI-1 → T29; AI-8 → T30's ruling;
AI-15 → landed via T17; the rest read against main); then the retro-skill
cycle (follow-up 1, five changes), the bundle PRD cycle 1, the spec-review
cycle, the remote-write policy cycle, the Decision Layer cycle, the
command-blocks cycle (follow-up 7, three changes), and the Chief of Staff
role cycle.

E5 — decisions/log.md: append at the end of the file:

## DEC-000280 — Writing bundles: the three role file sets are ruled
Date: 2026-08-31
Decision: The Writer, Copy Editor, and Critic bundles are exactly the sets AC-BS-4 of `specs/bundle-system.md` states: writer — core, decision-layer, the role, public-prose-criteria, voice, the outline skill, in that order; copy-editor and critic — the same minus the outline skill, with their own role files. No writing bundle carries another writing role or any software-delivery file. The 22-file `--audience writer` output is retired by that criterion when the selection mechanism lands.
Context: Owner decision (Dave), 2026-08-30, writing-workstream decision session; recorded in the PRD at its landing (PR #262) and logged here at the 2026-08-31 catch-up. The log entry was owed from the 08-30 session, which ruled the sets over the hand-built bundles at 40a8914.

## DEC-000290 — Delivery naming: sort-to-top is dropped; timestamps are UTC with a required Z
Date: 2026-08-31
Decision: Supersedes DEC-000200's naming clause only; the single delivery location `~/Downloads` stands, as does everything else in that entry. Files an agent hands Dave take the standing filename convention — `<descriptor>-<timestamp>` — with no sort-to-top prefix. Repo-wide, a generated timestamp is ISO 8601 basic format, UTC, with the `Z` designator required and date and time components both present: `<YYYYMMDD>T<HHMMSS>Z`. Core rule 14's example and the directive-authoring Naming example gain the `Z` at their documents' next cycles; existing filenames are not renamed.
Context: Owner decision (Dave), 2026-08-31, topic-walk session, on seeing the `0-` prefixes the sort-to-top clause produced. UTC over local because that's what professionals do. Closes the timezone gap `reviews/directive-authoring-cycle-3.md` F-2 and `reviews/directive-authoring-cycle-4.md` O-3 recorded.
Supersedes: DEC-000200 (naming clause only)

## DEC-000300 — Trivial-additive fast lane: refused, with a hit-again revisit trigger
Date: 2026-08-31
Decision: No third sanctioned route to `agreed` is created for owner-approved, additive, tool-verifiable-green changes. The next concrete case that fits no existing route is itself the trigger for a revisit: it reopens the OPEN-ITEMS entry with itself as evidence rather than being absorbed or worked around.
Context: Owner decision (Dave), 2026-08-31, topic-walk session, T25. The two motivating instances (2026-08-24) predate the cycle-20 revision of the document-metadata policy; a route defined from stale evidence is how gate complexity accretes.

The six decisions owed from the 15-hour session are not written here: their content is not recoverable from this session and must be reconstructed from that session's records before entries can be drafted. The OPEN-ITEMS entry for them stands.

SCOPE, one commit after the directive-file commit: OPEN-ITEMS.md and decisions/log.md only. Commit message: "OPEN-ITEMS + decisions/log: topic-walk flush and catch-up 2026-08-31 (33 topics ruled; DEC-000280..300)". Push with git push origin topic-walk-flush-20260831.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-walk-flush-run.log": bin/check-frontmatter --all (state exit code and count); grep -c "^## DEC-" decisions/log.md (state before and after, expected after = before + 3); grep -c "^## Topic walk 2026-08-31" OPEN-ITEMS.md (expected 1); git diff --stat of the content commit (expected: exactly two files, insertions only apart from the E1 strike and E2/E3 appends).
Expected state, and a stop if it differs: check-frontmatter exit 0, 62 files / 14 globs. The bin/ test suite is not run by this directive; report it as not run.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin topic-walk-flush-20260831 shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-walk-flush" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 24dab436ba96f7cc4368f184f740636d68f4da2c. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any anchor not found exactly once, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the content commit SHA, and the branch it is on
- the run-log path
- per edit E1 to E5, one line stating what changed and the line numbers as landed
- the before and after DEC-entry counts, and the section-heading count
- check-frontmatter exit code and count, with the tree it was observed in; a sandboxed run says so
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
