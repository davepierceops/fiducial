# Review: engagements/cartographer.md — cycle 1

Verdict: changes-required
Reviewed: engagements/cartographer.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 32 lines, against all eleven criteria of the review rubric @ 1bbd5b7.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, engagements/assistant.md, engagements/skeptic.md, policies/document-metadata-policy.md, and the full `roles/` listing at 1bbd5b7 (nine files, none named cartographer) — all @ 1bbd5b7.
Not inspected: `engagements/comfy/**` (its own cycle, per the directive); `bin/bundle`'s handling of a file with no frontmatter (not run — the consequence in CA-1 is inferred from the settled selection rule, not observed).
Findings: 7 — 3 blocking, 3 non-blocking, 1 observation
Prior cycle: none
Dave should inspect: nothing requiring his judgment beyond the shared frontmatter question (CA-1, CA-2). This is the cleanest of the four engagement files.

## Criterion 10 first

**Disposition: retain-with-changes.**

The directive's four questions:

**Role, skill, standing instruction, or history?** A **role**. A standing
posture for a whole session — read-only, answer what was asked, tag every claim
— not a procedure to run once.

**What `audience:` follows?** `[cartographer, human]`. The value already exists:
`engagements/working-with-dave.md` @ 1bbd5b7 carries `audience: [assistant,
cartographer, skeptic, human]`, and a tally of audience values across 1bbd5b7
shows `cartographer` in use on four files. The selector points at this file
already; the file does not answer.

**Does a role document already carry it?** **No.** The `roles/` directory at
1bbd5b7 contains nine files — architect, chief-of-staff, coder,
context-quality-reviewer, release-manager, reviewer, skeptic-risk,
spec-reviewer, test-designer. None is a Cartographer and none does what this
does. Unlike `engagements/skeptic.md`, this file has no counterpart to collide
with.

**Does it contribute something no other file in its bundle states?** Yes, and
this is the finding that matters: after the two criterion-4 cuts below, roughly
three quarters of the file survives. Read-only archaeology in service of what
Dave is trying to do; incremental mapping rather than read-everything-first;
naming the access or action that would answer an unanswerable question and
handing that to Dave; and not interviewing the client's people. None of the five
foundation files states any of it. Compare `engagements/assistant.md`, where six
of eight rules are Decision Layer restatements.

**Retain-with-changes.** The changes are two cuts, a frontmatter block, and one
sentence of session-kind.

## CA-1 — blocking
Claim: the file carries no frontmatter at all, so it has no `audience:` and cannot be selected into any bundle.
Location: engagements/cartographer.md:1 (the file opens with `# Role: Cartographer`; there is no `---` block)
Evidence: verified by reading the file's first line. Verified by reading engagements/working-with-dave.md @ 1bbd5b7, which carries frontmatter naming `cartographer` as an audience — so the selector exists and this file does not answer it.
Consequence: criterion 2 fails outright. Under the baton's settled rule @ 1bbd5b7 — agents receive `bin/bundle <audience>` output and never the repository — a file with no `audience:` reaches no agent. A Cartographer session bundled today receives working-with-dave.md and not the role that defines what it is. This consequence is inferred from the settled selection rule, not observed by running the compiler.
Fix: add frontmatter — `status: draft`, `last-reviewed: null`, `audience: [cartographer, human]`. No `order:` needed.
Related: AS-1, SK-1, QN-1.

## CA-2 — blocking
Claim: `engagements/**` is absent from the document-metadata policy's in-scope set, so nothing checks the frontmatter this file needs.
Location: engagements/cartographer.md (whole file), against policies/document-metadata-policy.md @ 1bbd5b7 lines 24–35
Evidence: verified by running `git show 1bbd5b7:policies/document-metadata-policy.md | sed -n '20,55p'`. The in-scope list names `policies/**`, `roles/**`, `context-sets/**`, `boundaries/**`, `skills/**`, `specs/**`, `vendors/**`, `operating-model.md`, `README.md`, `LEXICON.md`. `engagements/**` is in neither list, and the policy states "Enforcement (hooks) checks exactly the in-scope set."
Consequence: the reason CA-1 was possible. Adding frontmatter here without extending the glob fixes the instance and leaves the hole.
Fix: add `engagements/**` to the in-scope set. That edit belongs to the document-metadata-policy cycle, which the baton already schedules for a scope revision; raised here because this is where it was verified.
Related: AS-2, SK-2, QN-2.

## CA-3 — blocking
Claim: the claim-tagging bullet restates Core rule 6 in a second vocabulary.
Location: engagements/cartographer.md:15–17 ("Every claim tagged: **observed** (cite the file/line or query) / **inferred** (state the inference) / **told** (who, when) / **unknown** (phrased as a question worth asking)")
Evidence: verified by reading docs/global-context/core.md @ 1bbd5b7 Evidence rule 6: "**Every claim carries its class.** An assertion about state, results, verification, or completeness is a claim; label it *observed* (you saw it), *inferred* (you reasoned to it), *told* (someone said it), or *unknown*. State the class; an unlabelled assertion is treated as *unknown*."
Consequence: the same four labels defined twice in one bundle — Core is `audience: [all-roles, human]`, so both files reach a Cartographer session. The copy is lossy in one direction and additive in another: it drops Core's default ("an unlabelled assertion is treated as *unknown*") and adds a per-label obligation Core does not state (cite the file/line; name who and when). The additions are the part worth keeping; the definitions are not.
Fix: cut the label definitions. Keep the additions as one line — "Cite the location for *observed*; name the source and date for *told*; phrase *unknown* as the question worth asking" — which reads as an application of Core rule 6 rather than a second statement of it.

## CA-4 — non-blocking
Claim: the "Never guess" bullet restates Core rule 7.
Location: engagements/cartographer.md:29–30 ("Guess. 'Could not determine, here's what would determine it' beats a confident wrong answer")
Evidence: verified by reading core.md @ 1bbd5b7 Evidence rule 7: "**Say what is unverified.** Never report assumed as verified. \"Could not determine\" beats a guess."
Consequence: criterion 6 names this shape — a "Never X" restatement of a stated rule. Near-verbatim, including the phrase "Could not determine". The clause "here's what would determine it" is not in Core, but line 21–23 of this same file already states it at greater length, so it is duplicated within the file as well.
Fix: cut the bullet. Core carries the rule and line 21–23 carries the addition.

## CA-5 — non-blocking
Claim: "Load with `working-with-dave.md`" is a path-shaped reference and an instruction the bundle has already carried out.
Location: engagements/cartographer.md:3
Evidence: verified by reading, against the settled rule @ 1bbd5b7 that agents receive bundle output and never the repository.
Consequence: criterion 1 and criterion 3. A reader that has the file needs no instruction to load it; a reader that lacks it cannot comply.
Fix: cut the clause; the `audience:` values pair the two files.
Related: AS-10, SK-5.

## CA-6 — non-blocking
Claim: the session kind is not stated, and the file's own content points the opposite way from the file it says to load with.
Location: engagements/cartographer.md (whole file), against engagements/working-with-dave.md:7 @ 1bbd5b7
Evidence: verified by reading. working-with-dave.md @ 1bbd5b7 states "This file is for execution sessions within an engagement." This file describes a session that answers Dave's questions in a back-and-forth ("Dave asks; you dig; you answer with provenance"), which is the shape of a decision session under core.md's vocabulary — though it produces no directives and carries out no directive either, so it fits neither definition cleanly.
Consequence: criterion 7. Lower weight than the same defect in engagements/assistant.md, because nothing here turns on which kind it is — the Cartographer is read-only and issues no directives, so neither the Decision Layer's register nor an execution session's working-tree rules change its behaviour. It is still unstated, and a reader deciding what else to load has nothing to decide from.
Fix: state it in one line. On the content, the honest answer is that a Cartographer runs as a **decision session** — it reads freely, writes nothing to the client's systems, and hands Dave what to do next — and that working-with-dave.md's blanket "for execution sessions" needs the same correction AS-3 raises.
Related: AS-3.

## CA-7 — observation
Claim: no use of any retired term, no vendor name, and no model name appears in the file.
Location: engagements/cartographer.md (whole file)
Evidence: verified by running a term sweep for *dispatch*, *sync block*, *track*, and *prompt*, and a name sweep for vendor and model names, over the file at 1bbd5b7. Both returned no matches.
Consequence: none. Recorded because the cycle directive requires both sweeps to be reported per file, and "nothing found" is a claim rather than a default.
Fix: none.

## Note on a directive/LEXICON tension

The directive for this cycle states that every use of *dispatch*, *sync block*,
*track*, and *prompt* is a criterion-4 finding. LEXICON @ 1bbd5b7 states two
explicit carve-outs: *track/tracking/tracker* in the ordinary record-keeping
sense, and *prompt* meaning a tool's approval interrupt. Core rule 9 says two
sources that disagree are surfaced, not resolved by picking one. Uses covered by
a carve-out are recorded here as observations, not defects, and are counted
separately in the sweep. This note appears in all eight artifacts of this cycle.
No use of any retired term occurs in this file.

## Sweep counts

- Rules restated from the foundation: **2** (CA-3, Core rule 6; CA-4, Core rule 7)
- Output-shape lists with a home elsewhere: **0**
- Path-shaped references: **1** (line 3, `working-with-dave.md`)
- Vendor and model names: **0**
- Retired terms: **0**
- SLO / Top K copies: **0**
