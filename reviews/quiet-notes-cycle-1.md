# Review: engagements/quiet-notes.md — cycle 1

Verdict: changes-required
Reviewed: engagements/quiet-notes.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file — 205 bytes, 7 lines, of which one is a heading, three are format description, one is blank and one reads "(no entries yet)" — against all eleven criteria of the review rubric @ 1bbd5b7.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, engagements/assistant.md, policies/document-metadata-policy.md, docs/batons/baton-20260822T153848.md — all @ 1bbd5b7.
Not inspected: whether any quiet note has ever been written anywhere else (no engagement working tree was available to this session); `engagements/comfy/**` (its own cycle, per the directive); `bin/bundle`'s handling of a file with no frontmatter (not run — QN-1's consequence is inferred from the settled selection rule).
Findings: 5 — 3 blocking, 1 non-blocking, 1 observation
Prior cycle: none
Dave should inspect: QN-3 — the disposition. This is a retire recommendation, and retiring a file is a removal, not a fix.

## Criterion 10 first

**Disposition: retire.**

**What it is** — the directive asks for this explicitly. It is **none of the
four options offered.** Not a role, not a skill, not a standing instruction to a
session, not history. It is an **empty state artifact with its schema written at
the top**: an append-only record whose only content is the description of the
format entries would take if any existed, plus a parenthetical confirming none
do. Under decision-layer rule 9 @ 1bbd5b7 its class is legitimate — "A loose-end
tracker is a record, not derived state" — so the *practice* is sound. The
problem is not what it is; it is where it lives and that it is empty.

**What `audience:` follows** — **none.** There is no audience value under which
handing this file to an agent helps. An agent that receives it learns a line
format it already has (engagements/assistant.md:27–32 states the same format and
is the file whose reader performs the writing) and learns that there are no
notes, which is a fact about a repository the agent does not have. `[human]`
fails too: Dave does not need a committed empty file to know he has no quiet
notes.

**Does a role document already carry it?** Yes — engagements/assistant.md
carries the practice, the line format, and the write mechanism. Every rule this
file states is stated there.

**Criterion 10 is decisive.** "It lands in at least one bundle and contributes
something no other file in that bundle states. A file that fails this is
removed, not fixed." This lands in no bundle and states nothing another file
does not. Retire it.

The practice does not go with it. Quiet notes are a real thing the Assistant
does and should keep doing; the record belongs in the engagement's own working
area, created when the first note exists, not committed empty to the methodology
repository. That is the whole change: delete the file, keep the practice in
engagements/assistant.md.

## QN-1 — blocking
Claim: the file carries no frontmatter at all, so it has no `audience:`.
Location: engagements/quiet-notes.md:1 (the file opens with `# Quiet Notes`; there is no `---` block)
Evidence: verified by reading the file in full — all 7 lines. Verified by reading engagements/working-with-dave.md @ 1bbd5b7, which does carry frontmatter, so the absence here is not a directory-wide convention.
Consequence: criterion 2 fails. Unlike the other three engagement files, this is not a defect to fix — adding an `audience:` would be worse, because it would select a state file into a bundle. The missing frontmatter is a symptom of the criterion-10 answer: the file has no audience because it should not have one.
Fix: retire the file rather than add frontmatter.
Related: AS-1, CA-1, SK-1 — same absence, opposite fix.

## QN-2 — blocking
Claim: `engagements/**` is absent from the document-metadata policy's in-scope set.
Location: engagements/quiet-notes.md (whole file), against policies/document-metadata-policy.md @ 1bbd5b7 lines 24–35
Evidence: verified by running `git show 1bbd5b7:policies/document-metadata-policy.md | sed -n '20,55p'`. `engagements/**` appears in neither the in-scope nor the out-of-scope list; the policy states "Enforcement (hooks) checks exactly the in-scope set."
Consequence: worth recording specifically for this file, because the policy's **out-of-scope** list is where it would have belonged. That list names "State and tracker artifacts: `MANIFEST.md`, `OPEN-ITEMS.md`, `COLLAB-STATE.md`, `BACKLOG-v2.md`, review artifacts … Their status is their content." That description fits this file exactly. Had `engagements/**` been classified at all, this file would have been classified correctly and the other three would have been caught for missing frontmatter.
Fix: when `engagements/**` is added to the metadata policy's in-scope set (AS-2, CA-2, SK-2), the state-artifact carve-out should be checked against whatever remains in the directory. If this file is retired as recommended, nothing in `engagements/` is a state artifact and the carve-out is not needed.
Related: AS-2, CA-2, SK-2.

## QN-3 — blocking
Claim: every rule the file states is stated in engagements/assistant.md, and the file's only other content is a statement that it is empty.
Location: engagements/quiet-notes.md:3–7 (the whole body)
Evidence: verified by reading both files at 1bbd5b7 side by side. This file states: append-only; one line per note as `date | note | where seen`; written by the Assistant at session end; not today's problems — smells, risks, cleanup. engagements/assistant.md:27–32 states: "A quiet-notes list: things you noticed that aren't today's problem (smells, risks, cleanup). Accumulate; surface only when asked or when one becomes today's problem… At session end, write the new notes to the `quiet-notes.md` tracker (one line each: date, note, where you saw it) — append directly if you have write access, otherwise render an append-ready block for Dave to paste." Every element matches. Line 7 of this file reads "(no entries yet)".
Consequence: criterion 10. Two statements of one format, and the second one is in the file the Assistant is not reading when it decides how to write a note — it reads its role document. Worse, the duplication is the drift hazard: if the format changes in one place, notes written from the other are malformed, and nothing checks a file outside the enforcement glob (QN-2).
Fix: delete the file. Keep the format statement in engagements/assistant.md, which AS-8 already edits, and have the Assistant create the record in the engagement's working area on first use. If Dave wants the file to exist in advance, it is an untracked working file, not a committed methodology document.
Related: AS-8.

## QN-4 — non-blocking
Claim: the fixed filename `quiet-notes.md` is a single global name for a per-engagement record.
Location: engagements/quiet-notes.md (the filename itself), against engagements/assistant.md:30 @ 1bbd5b7
Evidence: verified by reading core.md @ 1bbd5b7 Standing/Acting rule 14: "**A filename you generate is `<descriptor>-<timestamp>`** … when no stated convention names the file. Where a convention names it, follow the convention." engagements/assistant.md:30 names it, so the convention exists and criterion 9 is technically satisfied.
Consequence: one name, one file, for a practice that runs across multiple client engagements. Notes from two engagements land in the same record with nothing but the "where seen" column separating them, and there is no rule that they should not. The rubric's criterion 9 is satisfied on its letter; the underlying purpose — that a reader can tell what a file holds from its name — is not, once there is a second client.
Fix: subsumed by QN-3. A record created in the engagement's own working area is scoped by its location and needs no timestamp or client name.

## QN-5 — observation
Claim: no use of any retired term, no vendor name, no model name, no path-shaped reference, and no restatement of a foundation rule appears in the file.
Location: engagements/quiet-notes.md (whole file)
Evidence: verified by running a term sweep for *dispatch*, *sync block*, *track*, and *prompt*, a name sweep for vendor and model names, and a path sweep, over the file at 1bbd5b7. All three returned no matches. The file duplicates engagements/assistant.md (QN-3), which is not a foundation file, so the foundation-restatement count is genuinely zero.
Consequence: none. Recorded because the cycle directive requires the sweeps to be reported per file, and because a clean sweep on a file recommended for retirement is worth stating plainly: the file is not retired for containing anything wrong. It is retired for containing nothing.
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

- Rules restated from the foundation: **0** (the duplication in QN-3 is against engagements/assistant.md, which is not a foundation file)
- Output-shape lists with a home elsewhere: **0** — though the whole file is arguably one: a line format whose home is engagements/assistant.md (QN-3)
- Path-shaped references: **0**
- Vendor and model names: **0**
- Retired terms: **0**
- SLO / Top K copies: **0**
