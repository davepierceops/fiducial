---
project: fiducial
kind: synthesis
date: 2026-09-10
generated: 20260910T225935Z
source: claude.ai Chief of Staff session, fiducial project, 2026-09-10; no export filename
prior-synthesis: retro-synthesis-20260831T163000.md
read: 15
covers:
  - retro-20260831T220000Z.md
  - retro-20260902T185726Z.md
  - retro-20260902T233000Z.md
  - retro-20260903T070500Z.md
  - retro-20260903T175500Z.md
  - retro-20260903T221758Z.md
  - retro-20260904T180000Z.md
  - retro-20260904T183000Z.md
  - retro-20260905T001500Z.md
  - retro-20260907T173826Z.md
  - retro-20260908T042500Z.md
  - retro-20260908T160110Z.md
  - retro-20260909T171500Z.md
  - retro-20260910T032500Z.md
  - retro-20260910T223000Z.md
---

# Retro synthesis — fiducial — 2026-09-10

## Context

Input set computed per `process/retro.md`: every `retros/retro-*.md` not named
in the 2026-08-31 synthesis's `covers:` list — 15 retros, 2026-08-31 through
2026-09-10, 1,477 lines, read whole at main `d44ad52`. The period spans the
rule-store rebuild (DEC-000380 onward), so roughly half the raw candidates
target documents that AC-RS-9 retired to `docs/history/`; those are dropped
below unless the obligation is still live against the store. Everything
governed by a DEC entry at `d44ad52` is dropped and cited.

Raw material: 76 candidate methodology changes and 14 standing-preference
candidates across the 15 retros. After dedup, retirement and landed-check:
16 findings, 5 of them in the directive-verbosity cluster the human asked for
first.

## Triage method

- Dropped as landed: anything a DEC entry or a row at main already governs.
- Dropped as retired: anything whose only target is a document in
  `docs/history/` (skills/, policies/, roles/, the Decision Layer, the
  spec-review-cycle skill, the document-metadata policy, `bin/flip-agreed`).
- Clustered: several retros stating one rule become one finding; the
  recurrence count is the retro count, not the mention count.
- Rule test applied: each finding names the mistake an agent made without it,
  from the evidence cited.
- Every claim below is labelled observed (the retro's evidence, or the tree at
  `d44ad52`) or told (the retro's interpretation, or memory).

## Findings, in priority order

Each phrased as a finding for the delta that would carry it, not a decision.
`[R]` = rules delta (intake). `[P]` = process delta (one frontier read, human
sign-off). `[T]` = tracker, not methodology.

### Cluster 1 — directive verbosity and executor stops (human's priority)

Measured (observed, main `d44ad52`): `prose-criteria-rows-20260909T190000Z.md`
is 136 lines; its TASK region is 12; FIRST ACT, BASE VERIFICATION, SANDBOX,
STOP CONDITIONS, REPORT, CLAIM LABELS and SOURCE MANIFEST — text every
directive inherits — are 67. The AC-RS-8/9 chain ran 239/144/161/180 lines.
The diagnosis two retros converge on (09-09 E4–E10, 09-10a E5–E10): the stops
were caused by dictated tree facts in author regions, not by the boilerplate;
length correlates because more specification commits to more unread facts.

1. **[R] The decision session dictates intent, acceptance criteria, and any
   prose body the human agreed; it dictates no tree facts** — IDs, key values,
   orders, which rows hold what, tool names, expected counts. The executor
   derives each and reports the derivation with its evidence. Recurrence: 6
   retros (09-03a told-fact stop; 09-03c report-and-compare; 09-04a count
   rule; 09-07 E6; 09-09 #1/#2; 09-10a). Applied in 09-10b: three directives
   dictating rulings only, zero stops (observed). Mistake without it: every
   stop of 2026-09-09.
2. **[R] A precondition the executor can satisfy by reading the tree, with no
   judgment call and no change of intent, is resolved and reported, not
   stopped on.** Recurrence: 2 (09-09 #3 as an R0458 amendment; 09-10a).
   Evidence: four stops on 09-09 whose resolution the executor wrote into its
   report and then waited for (observed).
3. **[R] Route every directive to a fresh session**; retire the "existing
   session" route form, or restrict it to a session identified by a worktree it
   still holds. Recurrence: 2 (09-10a, 09-10b applied). R1283/R1312 still admit
   the existing-session form (observed). Mistake without it: the self-review
   of 09-09 (09-10a E10).
4. **[P] `process/directive-invariants.md`: carry invariant regions by pointer
   or drop the ones that restate executor-bundle rows.** Two shapes proposed:
   emit each region as one pointer line — path, SHA, section — with the lint
   checking the pointer resolves (09-09 #4, per R1291); or drop SANDBOX, CLAIM
   LABELS and REPORT where every executor bundle already carries the rows
   (09-10a). Either collapses the manifest to author regions. Recurrence: 2.
   This is the verbosity finding proper; smaller in stop-cost than 1–3.
5. **[P] `process/directive-invariants.md`: three inherited defects.** (a)
   FIRST ACT says "before touching any other file" above a disposition that
   creates the worktree it pushes from — still in the document at `d44ad52`
   (observed); recurrence 3 (09-03a, 09-07 #5, 09-09 #5). (b) No Cleanup
   region: worktree removal after push verified is author-region memory;
   recurrence 2 (09-02b, 09-03a). (c) A directive's verification capture path
   lives outside the worktree it assigns, so the non-force removal holds
   (09-10b; observed refusal on `flush-20260910`).

### Cluster 2 — the decision session's own claims

6. **[R] Command-blocks: a block is tested end-to-end against a local
   stand-in for the remote, guard and re-run paths included, and a block
   carrying a substituted value is run with the value bound before it is
   handed over.** Recurrence: 3 (09-07 E10; 09-08a E11 `printf %s` landed
   "agreed at  as"; memory). R1228 says valid and re-runnable, not tested
   (observed; no row matches "stand-in").
7. **[R] Dictated text is verified byte-for-byte against the landed file —
   a `diff` against the directive's own fenced block — never by a proxy
   count or heading grep.** Recurrence: 3 (09-04a #314 truncation; 09-04b
   applied; 09-08a fence-character failure). Survives finding 1 because
   agreed prose bodies are still dictated.
8. **[R] Before directing against a spec, read the spec whole — PRD, TRD and
   the DEC entries that agree it; a question the human is asked that the
   spec answers is a defect in the read.** Recurrence: 2 (09-09 #2 and its
   standing-preference candidate; 09-04a "read the file, not the baton").
   R0180/R0181 name governed text and the repository, not the spec spine
   (observed).
9. **[R] "I'll change X" is a defect unless X is changed in the same turn;
   the write precedes the statement.** Recurrence: 1 (09-05 E7), but the
   human caught it verbatim ("Did you though?"). Core-12 class.

### Cluster 3 — asking the human

10. **[R] Amend R0225 or add a row: a ruling question defines the corpus
    term it turns on in one sentence, restates the situation from the ground
    floor when the question arrives without its context, and names which
    option matches his prior rulings, offering the reversible one.**
    Recurrence: 3 (09-04b E4/E13; 09-05 "supply the ordinary word";
    09-10a E18 "I came into the middle of a conversation"). Also: triage
    items go one per turn, never as a list (09-07 E14, two of four rulings
    reversed).
11. **[R] A question the Chief of Staff could answer itself once the human
    declines it was never his; ask the naming or judgment question beneath
    it.** Recurrence: 1 (09-05 E3). Merges with 10 if the human prefers one
    row.

### Cluster 4 — spec close and boundaries

12. **[P] `process/change-flow.md` or `spec-test-suite.md`: at a close that
    claims to state what was built, the read checks each AC against the
    tree at the reviewed SHA and names each built or not-built.**
    Recurrence: 1 (09-09 E5/E7: a PRD "revised to state what was built"
    agreed with two unbuilt ACs). R1489 and the reconciliation definition
    state the outcome, not the check (observed).
13. **[R] Boundary topic: a package that retires a tool which installs
    per-clone state — a hook, a config, a credential helper — names the
    operator step that removes it and where that step is published; the
    suite cannot see it.** Recurrence: 1 (09-09 E11; 09-10a E1 the same
    hook stopped the next executor). R0148's boundary-sensitive list omits
    per-clone state (observed).

### Cluster 5 — small process and writing findings

14. **[R] Writing corpus, writer and copy-editor: in a document whose
    audience includes readers outside software, use the plain phrase for a
    software term or define it in the sentence that first uses it.**
    Recurrence: 1 (09-08b E7 "vendor"). Named-audience row; passes the rule
    test on that evidence alone.
15. **[P] `process/review-artifact.md`: a filename form for a delta over more
    than one reviewed document** (descriptor or branch slug). Recurrence: 1
    (09-10b E10). **[P] `process/retro.md`: state which of `date:` or the
    session's opening day names a retro in conversation, or that both do**
    (09-10b E12). Two one-line process edits; bundle into one delta.
16. **[T] Tooling, no methodology text:** `bin/release` prints its `gh` line
    with `-R`; the rendered-bundle body check goes between `bin/release` and
    `gh release create` (09-10a); `bin/bundle` branch-render mode (three
    reads stated its absence as their boundary); `bin/directive` emits `~~~`
    inner fences and stops appending " Directive" to a title that carries it
    (09-03b, 09-03a); `bin/check-directive` M2's three known false-positive
    phrasings (09-05, 09-10b — cleared by per-file companion SHAs).

## Standing-preference candidates not already rows

Named in the retros as stated in more than one session; each a candidate row
unless the human says it is already carried:

- Non-blocking findings are tracked, never fixed inline — now DEC-000700;
  the row proposed in 09-10a is owed to intake (told: not yet a row).
- A block whose value is substituted is run with the value bound — finding 6.
- Restate the ground floor before a choice — finding 10.
- Land every artifact left untracked on the clone as its own pull request
  (09-10b E12; applied 09-09 in #347). One statement located, one applied.
- A governing document stands alone and carries rationale where a human is
  the reader (09-08a E12/E13) — told: already applied to the PRD template;
  no row found (observed, grep "stand alone" in `rules/`: none).
- When the same class of failure repeats, change the method, not the
  instance (09-09 E14). First statement located; the retro on 09-09 is its
  evidence.

## Dropped, with reason

- **Landed:** non-blocking-never-reopens (DEC-000700); row citations
  co-render (DEC-000710); "every commit on the default branch is releasable"
  (rows, 09-07); prose-criteria retirement (DEC-000720/730); R1605.
- **Retired with the lifecycle (AC-RS-8/9):** pre-ruled dispositions in a
  read-only pass (08-31); path-exists and M5 lint rules, remote-write
  precomputed-blob policy, `skills/directive-authoring.md` cycle-number rule,
  Decision Layer rule 13/6/10 amendments, spec-review-cycle re-gate scope,
  document-metadata `review-scope` axis, `bin/flip-agreed` diagnostics,
  retro-trigger coupling, `roles/chief-of-staff.md` cycle items, the
  convergence-suite interface source (09-02 through 09-04). Where the
  obligation survived, it appears above as a store finding (6, 7, 8, 10).
- **Done by the rebuild:** dedup method, shortlist thresholds, compound-row
  clustering (09-05).
- **Already on the human's plate, not new:** `[R####]` citations in process
  documents; the claim-tier semantics (read F2); R1015/R1171/README "the
  Criteria" before the next release cut; `named-queries.md` naming
  `lexicon` nowhere and two roles with no rows (09-08a #4).
- **One-off, no recurrence, no incident cost:** cut a fix branch from the
  read branch (09-08a #5); decision entry stated once inside a directive
  (09-08a #3) — subsumed by finding 1; baton items carry a plain clause
  (09-03c) — subsumed by R0252's form; sub-session spawning by an execution
  session (09-04a) — no incident since.

## Open question surfaced by the triage, not a finding

The rule test — "what would an agent do wrong without this row; if nothing,
refuse" — is the working intake filter (09-07 E13, memory) and is not a row
at `d44ad52` (observed). Whether it belongs in the store or stays the human's
own instrument is his call.
