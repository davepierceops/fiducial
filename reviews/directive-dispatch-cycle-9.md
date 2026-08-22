# Review: skills/directive-dispatch.md — cycle 9

Verdict: changes-required
Reviewed: `skills/directive-dispatch.md` @ `5136960`
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole document, read start to finish against all eleven criteria of
the review rubric, with criterion 10 answered per section before the rest. The
document was read as a candidate for retirement, not for repair: it predates
Core's directive rule and was written for a world with tracks, sync blocks, and
chat-committed directives. Counts were taken mechanically over the file at
`5136960` and are stated in D16.
Cross-checked: `docs/global-context/core.md` (Standing; Acting; Vocabulary —
Paste block, Command block, Execution block, Directive, Directive file,
Companion document), `docs/global-context/decision-layer.md` (13, 14, 15),
`LEXICON.md` (Retired terms — Dispatch, Sync block, Track), `operating-model.md`
(Agents — must not), `skills/command-blocks.md` and the other eight files in
`skills/` for the naming convention, `skills/spec-review-cycle.md` for the
reciprocal duplication.
Not inspected: whether `bin/cycle-open` exists or behaves as described (excluded
by the directive); the eight prior review artifacts for this document beyond
cycle 8's header; whether any live directive in `docs/cycles/` still follows the
naming schema in §"Directive file naming schema"; the `reviews/expedited-log.md`
entry cited by this file's `last-reviewed`.
Findings: 17 — 13 blocking, 2 non-blocking, 2 observations
Prior cycle: `reviews/directive-dispatch-cycle-8.md`
Dave should inspect: D14 (the file asserts `status: agreed` in frontmatter and
"Nothing here is agreed" in its last line — one of the two has been wrong since
2026-08-10); D16's confirmation that no retired content survives unhomed, which
is the precondition for retiring §3 and the naming schema outright; and the
proposed filename in D1.

## Disposition — criterion 10, per section

The document as a whole does not survive. Two sections do, one of them in part.

| Section | Lines | Disposition |
| --- | --- | --- |
| Frontmatter | 1–7 | **Rewrite.** `name:` carries a retired term; `description:` carries the retired term and a vendor name. |
| Title, Purpose | 9–33 | **Retire.** Core's `Directive`, `Directive file`, and `Execution block` state the form; the rest is the argument for it. |
| Use when | 35–47 | **Retire.** Restates Core; closes with a note recording open work rather than instructing an agent. |
| The three requirements | 49–53 | **Retire.** Core's `Directive` states route, model tier, and execution block. |
| §1 Route | 55–62 | **Retire.** Core states route; nothing here is added. |
| §2 Model | 64–72 | **Retire.** Decision-layer 14 states the tiers, and this table states model names instead. |
| §3 Execution block | 74–98 | **Retire.** Mandates a sync block; LEXICON retired the term and Core states what the execution block opens with. |
| Writing the directive file | 100–119 | **Survives**, less its opening line. Five authoring constraints no foundation file states. This is the document's reason to exist. |
| Executor obligations | 121–140 | **Survives in part** — one bullet of five (concurrent tree mutation, 135–136). The rest restates Core 11, 12, and the `Directive file` definition. |
| Directive file naming schema | 142–163 | **Retire.** Contradicts Core rule 14 and current practice, and is self-labelled a proposal. |
| Status of this draft | 165–189 | **Retire.** A changelog of retired mechanics, in the register of a commit message. |

**What survives beyond what Core already states**, in full: the five authoring
constraints at 105–119 (exclusive working trees for split directives; pin STOP
conditions to the reviewed ref; mid-delta directives derive from the spec branch
and pin its SHA; no blanket constraint contradicts an explicit instruction in the
same file; scope Do-not lists to the blast radius, naming permitted exceptions),
the dictated-wording pointer rule at 117–119, and one executor obligation at
135–136. Nothing else.

The **naming schema does not survive** (D12). The **executor obligations survive
only as that one bullet** (D11).

## D1 — blocking
Claim: The frontmatter `name:` and `description:` carry the retired term
"dispatch" and the vendor name "Claude Code".
Location: `skills/directive-dispatch.md:5-6`
Evidence: verified by running `git show 5136960:skills/directive-dispatch.md`;
`LEXICON.md` Retired terms — "**Dispatch** — retired 2026-08-21. Write 'hand the
directive to an execution session,' or 'direct.'"
Consequence: `description:` is the text a harness shows when selecting the skill,
so the retired term and the vendor name are the first thing an agent reads about
this procedure, and `name:` will not match the file once it is renamed.
Fix: rename the file to `skills/directive-authoring.md`, set `name:
directive-authoring`, and rewrite `description:` in the retired term's
replacement wording with no vendor name. The proposed filename follows the
convention the other eight files in `skills/` use — a kebab-case noun phrase
naming the procedure, matching the H1 (`change-package-creation`,
`release-readiness-review`, `spec-review-cycle`) — rather than Core rule 14's
`<descriptor>-<timestamp>`, which criterion 9 defers where a stated convention
names the file.
Related: D13, D14

## D2 — blocking
Claim: The Purpose section is the argument for a directive form that Core now
states, not an instruction to any agent.
Location: `skills/directive-dispatch.md:11-33`
Evidence: verified by reading `docs/global-context/core.md` Vocabulary against
it — `Directive`, `Directive file` ("written and committed by the executor as
its first act"), and `Execution block` ("Its first instruction is to write the
directive to a file, commit, push, and report the SHA") state every operative
fact in these 23 lines. The transport/record distinction (16–20), the post-hoc
SHA argument (24–28), and the paste-arrival-intactness paragraph (30–33) are
justification.
Consequence: 23 lines of bundle budget restating and defending a rule the reader
already loaded, in a register criterion 6 excludes.
Fix: delete 11–33.
Related: D4, D5

## D3 — blocking
Claim: "Use when" restates Core, defers to another file by path twice, and ends
by recording open work rather than instructing.
Location: `skills/directive-dispatch.md:35-47`
Evidence: verified by reading — 37 restates Core's `Directive`; 39–46 cite
`skills/spec-review-cycle.md` twice and name `Opus 5`; 46–47 reads "Where both
documents state the same requirement, this is the general statement; reconciling
the rest of the duplication is open work."
Consequence: an agent reading a bundle cannot open `skills/spec-review-cycle.md`
(criterion 1), and the closing sentence is a note between authors about
unfinished editorial work, which criterion 5 excludes from an agent instruction.
Fix: delete 35–47.
Related: D6, D15

## D4 — blocking
Claim: "The three requirements" restates Core's definition of a directive.
Location: `skills/directive-dispatch.md:49-53`
Evidence: verified by reading `docs/global-context/core.md` — "**Directive** —
the complete package handed to an execution session: one line stating route
(fresh or existing session) and model tier, then the execution block as a paste
block. All three stated every time. A class may have defaults, still stated in
full each time, the model default as a tier."
Consequence: the rule is stated twice in one bundle, and the two statements will
drift.
Fix: delete 49–53.

## D5 — blocking
Claim: §1 Route restates Core and adds only rationale.
Location: `skills/directive-dispatch.md:55-62`
Evidence: verified by reading — Core's `Directive` states route as fresh or
existing session; 57 ("A wrong route fails silently") and 58–62 are the
justification for each value.
Consequence: criterion 4 and criterion 6 both.
Fix: delete 55–62.

## D6 — blocking
Claim: §2 Model instructs the agent to select a named model, which criterion 8
forbids and decision-layer 14 already governs in tiers.
Location: `skills/directive-dispatch.md:64-72`
Evidence: verified by running `grep -Eo 'Opus 5|Sonnet 5|Haiku 4.5'` over the
file — five model-name occurrences, three of them in this table;
`docs/global-context/decision-layer.md:14` states the same three bands as
*frontier*, *solid general-purpose*, and *cheap*.
Consequence: an agent that follows this table writes a directive naming a model
rather than a tier, which is itself a criterion 8 defect in every directive
produced; and the table is wrong the day the model roster changes, silently.
Fix: delete 64–72. Decision-layer 14 is the home.
Related: D3

## D7 — blocking
Claim: §3 Execution block mandates a sync block preceding the directive, which
LEXICON retired and Core's directive rule forbids.
Location: `skills/directive-dispatch.md:74-91`
Evidence: verified by reading `LEXICON.md` Retired terms — "**Sync block** —
retired 2026-08-21. Nothing precedes the execution block; the executor fetches as
its first act." The section reads "A dispatch is two paste blocks, in order. 1. A
**sync block** … **State it every time**".
Consequence: an execution bundle containing this section instructs a two-block
form that the current rule prohibits; an executor following it waits for a block
the decision session will not send, or the decision session sends one.
Fix: delete 76–91.
Related: D8, D16

## D8 — blocking
Claim: The two bullets after the retired sync block restate Core and defend it.
Location: `skills/directive-dispatch.md:93-98`
Evidence: verified by reading `docs/global-context/core.md` — "**Companion
document** — a committed file a directive requires the executor to read before
acting. Cited with its own path and SHA" covers 93–95; "**Directive file** —
written and committed by the executor as its first act" makes 96–98 ("Do not
establish the directive's own SHA before dispatch") a restatement plus its
rationale, and it uses the retired term.
Consequence: criterion 4, criterion 6, and a retired term in an operative
sentence.
Fix: delete 93–98 with the rest of §3.
Related: D7

## D9 — non-blocking
Claim: The opening line of "Writing the directive file" restates decision-layer 13.
Location: `skills/directive-dispatch.md:102-103`
Evidence: verified by reading `docs/global-context/decision-layer.md:13` — "**A
directive is self-contained.** The executor needs the block and the repository,
nothing from this conversation."
Consequence: the section that does survive opens by restating a rule its reader
already has, which is the pattern criterion 4 exists to stop.
Fix: delete 102–103; begin the section at the first constraint at 105.

## D10 — non-blocking
Claim: Two of the five surviving authoring constraints cite another file by path
for the fact they depend on.
Location: `skills/directive-dispatch.md:110-112` and `:117-119`
Evidence: verified by reading — 110–112 states the mid-delta rule and cites
`context-sets/spec-and-change-discipline.md` for "truth-at-handoff"; 117–119
states the dictated-wording pointer rule, whose `<path>@<sha>` form is the fact
it needs.
Consequence: a bundle reader cannot follow either citation (criterion 3), and
110–112's operative content — derive from the spec branch, pin its SHA — is
complete without it.
Fix: drop both parenthetical citations; the rules stand on their own text.
Related: D3

## D11 — blocking
Claim: Four of the five executor obligations restate Core.
Location: `skills/directive-dispatch.md:122-134` and `:137-140`
Evidence: verified by reading `docs/global-context/core.md` — 122–127 ("Land the
directive first … read the SHA back from git — never report a SHA on the strength
of a write call's return") is the `Execution block` definition plus rule 12 ("A
tool's success response is a claim. Confirm the correct content landed before
reporting it … If you cannot read it back, report only what the operator
reported"); 128–134 (remote unreachable → stop and surface) is rule 11 plus rule
12's last clause applied to one case; 137–138 is rule 11 verbatim in substance.
Only 135–136 (concurrent tree mutation: files this session did not change moving,
HEAD moving, an index lock) states something no foundation file states.
Consequence: five bullets of which one carries content; the four restatements
also import a path reference to `policies/remote-write-verification-policy.md`
at 126.
Fix: keep 135–136. Delete 122–134 and 137–138. 139–140 (the report opening) is a
report-format convention, not an obligation — keep it only if the surviving file
is the home for that format, otherwise drop it.
Related: D15

## D12 — blocking
Claim: The directive file naming schema contradicts Core rule 14 and current
practice, and prescribes a date format Core does not use.
Location: `skills/directive-dispatch.md:142-163`
Evidence: verified by running `git ls-tree` and by this cycle's own directive
file — Core rule 14 requires `<descriptor>-<timestamp>` with the timestamp in ISO
8601 basic format (`20260820T161541`) where no stated convention names the file.
The schema here prescribes `docs/cycles/cycle-<n>-directive.md`, which carries no
timestamp, and `docs/cycles/<slug>-<YYYY-MM-DD>-directive.md`, whose hyphenated
date is not ISO 8601 basic. This cycle's directive landed as
`docs/cycles/pass1-cycle-21a-directive-20260822T213000.md`, matching Core rule 14
and neither form here. The section labels itself "proposed" and "the part of this
draft most likely to want revision" (162–163), and cites `bin/cycle-open` (144).
Consequence: an agent that follows this schema generates a filename that fails
criterion 9; an agent that follows Core rule 14 contradicts a file it was handed
in the same bundle.
Fix: delete 142–163. Core rule 14 governs, and the naming schema is not a stated
convention that displaces it.
Related: D16

## D13 — blocking
Claim: "Status of this draft" is a changelog of retired mechanics, written to the
authors rather than to an agent.
Location: `skills/directive-dispatch.md:165-189`
Evidence: verified by running `grep -inE 'Track B|\bTrack\b|dispatch|Downloads'`
over the section — `Track B` twice (170, 178), `Track` three times (181, 186,
187), `bin/dispatch` (182), `~/Downloads` (177); plus six `docs/cycles/` paths,
`BACKLOG-v2.md`, `LEXICON.md`, and
`policies/remote-write-verification-policy.md`. Every operative statement in it
describes an edit already made.
Consequence: 25 lines that teach an agent five retired terms and eleven
unfollowable paths, and that state, as the file's last word, a claim contradicted
by its own frontmatter (D14).
Fix: delete 165–189. Git history is the changelog.
Related: D14, D16

## D14 — blocking
Claim: The frontmatter says `status: agreed`; the document's final sentence says
"Nothing here is agreed."
Location: `skills/directive-dispatch.md:2` and `:189`
Evidence: verified by running `git show 5136960:skills/directive-dispatch.md` —
line 2 reads `status: agreed` with `last-reviewed: reviews/expedited-log.md @
c9e87ad253b5b9c2b67f4721d00e3d231c3326b3`; line 189 reads "Nothing here is
agreed." Verified by running `git log --oneline -1 5136960 --
skills/directive-dispatch.md` that the last commit touching the file is
`0dba6c9 docs(skills/directive-dispatch.md): status -> agreed`, so the flip
landed without the closing sentence being updated.
Consequence: a reader taking the frontmatter at face value treats the file as
agreed while the file denies it, and Core rule 9 ("Two sources disagree → surface
it") makes this the reviewer's to raise rather than to resolve. Core rule 13 is
the rule that was missed at the flip.
Fix: Dave's call which is true. If the retirement in this artifact is accepted
the question is moot, because 189 goes with D13 and the status is set fresh on
the renamed file.

## D15 — blocking
Claim: `audience: [all-roles, human]` puts decision-session authoring rules into
execution-session bundles.
Location: `skills/directive-dispatch.md:4`
Evidence: verified by reading the document against
`docs/global-context/decision-layer.md:1` ("Rules for decision sessions … Execution
sessions never receive this file") — "Writing the directive file" (100–119) is
addressed to whoever composes a directive, which is a decision session;
"Executor obligations" (121–140) is addressed to the execution session. The file
carries both at `all-roles`.
Consequence: every execution bundle carries five authoring constraints its reader
will never apply, and the file cannot say which session kind it is for, which
criterion 7 requires it to.
Fix: after the retirements above, what remains at 105–119 is decision-session
content and belongs at a decision-session audience; the one surviving executor
obligation (D11) belongs where execution sessions receive it. Splitting them is
the way both halves satisfy criterion 7.
Related: D11

## D16 — observation
Claim: No retired content in this file survives unhomed — with one qualification
about where its home is.
Location: `skills/directive-dispatch.md:74-98`, `:142-163`, `:165-189`
Evidence: verified by running `grep -in 'fetch'` over the four foundation files.
Every operative rule in the retired sections was checked for a home: the sync
block's substantive obligation — that the executor bring its clone current — is
stated at `LEXICON.md:113`, "Nothing precedes the execution block; the executor
fetches as its first act"; the mid-delta ref rule survives in this file's own
authoring constraints (110–112); `bin/dispatch` and the Track B on-ramp are
described in 165–189 only as things already removed; the naming schema is
displaced by Core rule 14 (D12). The counts behind this pass, taken over the file
at `5136960`: 21 path-shaped references, 5 model-name occurrences and 1 vendor
name (`Claude Code`, in `description:`), 8 word-uses of the retired term
"dispatch" plus the filename and `name:` value, 5 uses of retired "Track", 1
mandated "sync block", and 10 rules restated from Core or the decision layer.
Consequence: none — this is the confirmation the retirement depends on.
Fix: none required. One qualification worth Dave's eye: the executor's fetch
obligation is stated *only* inside LEXICON's **Retired terms** section, as part
of the entry retiring the sync block. It is homed, so nothing is lost, but a
reader looking for what an executor must do first has no reason to look under
retired terms. Whether that obligation should also be stated in Core's
`Execution block` definition is a question for the Core cycle, not a defect here.

## D17 — observation
Claim: The `bin/cycle-open` reference at 144 is the only surviving dependency
this file asserts on tooling.
Location: `skills/directive-dispatch.md:144`
Evidence: verified by reading — "Two forms, both working with `bin/cycle-open`".
Whether that tool exists or behaves as described was not inspected, by the
directive's exclusion.
Consequence: if the naming schema is deleted per D12, the assertion goes with it
and no tooling dependency remains in the file. If Dave keeps the schema instead,
the claim needs checking against `bin/`.
Fix: none if D12 is accepted.
Related: D12
