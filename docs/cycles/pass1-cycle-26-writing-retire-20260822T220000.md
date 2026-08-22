# Directive — Pass 1, Cycle 26: retire the writing pipeline

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Implementer (execution session). Not a review cycle; edits are dictated below.

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Starting state: main @ eaee794. Read docs/global-context/core.md, LEXICON.md, engagements/working-with-dave.md, writing/prose-criteria.md, writing/voice-inbox.md in full before editing.

## Decision

The writing pipeline (arc, outline, per-section bundles, five review passes, voice inbox, Editor/Section Writer/Reviewer/Skeptic/Instruction Reviewer) was a one-time experiment. Its yield is prose-criteria.md. Everything else retires. Writing becomes one role over the common foundation; baton hand-off, interaction rules, and escalation are inherited from Core and are not restated.

## Instructions

1. Archive, unedited, with history preserved by `git mv`: writing/pieces/ → docs/history/writing/pieces/; writing/retros/ → docs/history/writing/retros/; writing/voice-inbox.md → docs/history/writing/voice-inbox.md.
2. Delete: writing/roles/editor.md, writing/roles/section-writer.md, writing/roles/reviewer.md, writing/roles/skeptic.md, writing/roles/instruction-reviewer.md, writing/machinery-criteria.md, writing/README.md, writing/bin/ (entire directory).
3. `git mv writing/prose-criteria.md prose-criteria.md` (repo root; writing/ is then empty and gone). Edit it as follows. Everything not named is unchanged.
   a. Frontmatter → `status: draft`, `last-reviewed: null`, `audience: [writer, human]`. Delete `purpose:`.
   b. Claims taxonomy, last paragraph: delete the sentence beginning "This is the public-facing translation". Keep the tier-blurring sentence.
   c. Terminology: replace both bullets with: "Use the methodology's own governed vocabulary; define each term where it first appears for a public reader. When an industry-standard term exists for a concept the methodology names differently, flag the mismatch to Dave; he decides which the piece uses."
   d. Profanity: delete "Enforced by the justification-ledger pass (`roles/reviewer.md`)."
   e. Repo citation: replace `davepierceops/ai` with `davepierceops/fiducial`.
   f. AI prose-smell, first paragraph: replace with "Defect class. The tell list is open; add tells as they are noticed. Current entries:". Delete the closing paragraph ("A tell appearing in a draft…").
   g. Voice and register: append two bullets:
      - "Tier is carried by verb choice and frame, never by narrated self-correction. 'What I noticed' stays; 'I should be careful with my own story here' is cut."
      - "A point is made once, flat. No contrast pair that restates it from the other side."
   h. New section after Structure, titled "Length and duplication":
      "Wordy means duplicated ideas, not duplicated words; a draft inside its word budget can still be wordy. When Dave suspects duplication, report an audit of the repeated ideas before cutting anything. Dave does not pick which duplicates go: he sets a word target and the writer chooses. After a wordy draft the target is 10% under budget, not back to budget."
   i. Scan the whole file for any remaining path-shaped reference, role name from the retired set, or the words pipeline, pass, section, bundle, ledger, inbox. Report each; remove it only if its sentence still stands without it, else report and leave.
4. Create roles/writer.md with exactly this content:

---
status: draft
last-reviewed: null
audience: [writer, human]
---

# Role: Writer

Drafts public prose in Dave's voice. Governed by the Public Prose Criteria in this bundle; read them on every invocation.

- The draft is a document in the document pane. Discussion is in chat. Never paste the draft into chat.
- Dave edits the draft directly. Treat his edits as the current text and as voice evidence; propose a criteria line when an edit shows a rule the criteria do not state.
- The published text lives in Dave's own document, owned by Dave. The repository never holds prose.
- Nothing publishes on agent judgment. Dave reads every word before anything publishes.
- When Dave says the piece is done, state that a Skeptic and a Context Quality Reviewer are available for it, and stop. Do not start either.

5. Run `bin/check-frontmatter --all` and `bin/bundle writer`; confirm the writer bundle contains roles/writer.md, prose-criteria.md, and the all-roles set. Report the `bin/bundle --list` output.
6. Scan the repository outside the edited files for references to writing/, any retired writing role, machinery-criteria, or voice-inbox; report each with path and line. Do not edit them.
7. Commit on branch p1-cycle-26-writing-retire, push, open a pull request against main titled "Pass 1 cycle 26: retire writing pipeline, add Writer role". Do not merge. Report the SHA read back from git.

## Report shape

PR number and SHA. Then: bin/bundle --list output; the files in the writer bundle; every item from instructions 3i and 6, one line each; anything that could not be executed as written.
