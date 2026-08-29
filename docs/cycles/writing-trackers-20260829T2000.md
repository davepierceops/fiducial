You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: append five decision-log entries to decisions/log.md and update OPEN-ITEMS.md, as two commits.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/writing-trackers-20260829T2000.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: writing-workstream tracker updates", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-writing-trackers", created by: git worktree add --no-track "$TMPDIR/fiducial-writing-trackers" -b writing-trackers origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named writing-trackers, stop and report. Do not touch the main tree.

BASE VERIFICATION: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/main contains commit 53f7f40728a5ae60b14e0291a6060cab43ce31b5 (git merge-base --is-ancestor 53f7f40728a5ae60b14e0291a6060cab43ce31b5 origin/main exits 0); if not, stop and report. Record origin/main's SHA in your report; branch from it wherever it stands.

EDIT 1 — decisions/log.md. Append the following five entries verbatim at the end of the file, after the last existing entry, changing nothing else:

## DEC-000220 — Writing methodology lives in fiducial; davepierceops/writing migrates in and retires
Date: 2026-08-29
Decision: All LLM methodology, prose writing included, lives in this repository; there is no separate writing-methodology repository. `davepierceops/writing` migrates into fiducial completely and is retired when the migration is confirmed complete; nothing is deleted until then. Migrated at PR #230 (`53f7f40`): the roles, the criteria, `voice-inbox.md`, and `retros/retro-20260812-201500.md`. Retired without migration: the Editor (orchestrator), Section Writer, Instruction Reviewer, and machinery-criteria documents, and `bin/session-tar`; the one-section-per-session workflow is retired as an experiment Dave did not want to keep.
Context: Owner decision (Dave), 2026-08-28. The bundle compiler selects by `audience:`, so a writing bundle costs no new machinery; a second repository would duplicate Core, the review machinery, and `bin/`. Writing rules are expected to grow into a large body with little overlap; that is a tagging cost the audience mechanism exists to carry, not a structural one. The writing repository's methodology content was audited from a snapshot at `387bde6` before this decision.

## DEC-000230 — Writing roles: Writer, Copy Editor, Critic; passes split by workload; one-word activation on an uploaded document
Date: 2026-08-29
Decision: Three writing roles. The Writer drafts whatever the author asks for, including outlines per `skills/outline.md`; it computes no piece state. The Copy Editor (`copy`) runs the checklist passes — proofread and copyedit as tracked changes, and claims-tier audit, discoverability and cold reader, justification ledger, and many-languages read as anchored comments — at solid tier, with the Google developer documentation style guide as base authority where the Voice document is silent. The Critic runs the judgment passes — Skeptic, AI-smell, voice — as anchored comments only, at frontier tier, advisory and never a gate. Each reviewing role runs every pass it knows by default and a subset on request; a `.docx` uploaded to a fresh session plus the role's word is the whole instruction. The two reviewing roles never share a session with each other or with the Writer. Output is the author's own `.docx`, returned with tracked changes and comments that Google Docs imports as suggestions and comments. Every rule is written vendor-neutral and repository-neutral: it states the outcome and the verification, never a tool, and assumes the author has a document and a chat and nothing else.
Context: Owner decisions (Dave), 2026-08-28/29, worked in the artifact pane. The tracked-changes and comments round trip through Google Docs was proven end to end on 2026-08-28 before the roles were written. The split by workload rather than by tier keeps the roles stable if tiers shift. The writing repository's Reviewer and Skeptic roles were absorbed into this catalogue; the coverage map from every criterion to the pass that checks it was recorded in the workstream's working document and every criterion is checked by a named pass, is the Writer's by design, or is a stance with nothing to check.

## DEC-000240 — prose-criteria.md splits into Public Prose Criteria and Voice; a Voice template ships with labeled examples
Date: 2026-08-29
Decision: `prose-criteria.md` is retired to `docs/history/` as superseded and replaced by two documents. `public-prose-criteria.md` holds what is true of any author's prose under this method. `voice.md` holds the author: purpose and audience, register, profanity, vocabulary, mechanics (the house-style sheet the Copy Editor applies over its base authority), repo citation, venue, disclosure wording. Roles bind to both by name, never to a person; the voice pass is reads-as-the-Voice-document. `voice-template.md` is a human-facing template a new author fills in, carrying Dave's Voice sections as labeled examples; the template states that examples are a snapshot, may lag the live Voice document, and are never a review finding — criterion 12 of the review rubric applies to rules, not examples. Voice-inbox lines default to Voice on triage; generic ones route to the Criteria. The TL;DR summary-label convention is retired; a summary section's label is per piece.
Context: Owner decisions (Dave), 2026-08-29. The split is what lets a second author use the method by replacing one file. The examples are embedded rather than pointed at so that a new author writes their own Voice rather than adopting Dave's. `policies/document-metadata-policy.md`'s in-scope set was amended in the same PR to name the three new docroot files; that policy is a gate document and its full cycle is owed.

## DEC-000250 — Piece artifacts live with the piece; the voice inbox lives in fiducial; the roles assume no repository
Date: 2026-08-29
Decision: The record of a piece — outline, findings, drafts — travels in or beside the author's document, in the author's own storage, never in fiducial. "The repository never holds prose" stands with no exception. `voice-inbox.md` lives in fiducial because it feeds methodology; the Writer harvests into it at session close and states in one line when there is nothing to harvest, and triage is a doc-only cycle on `voice.md` or `public-prose-criteria.md` on Dave's cadence. Every writing role is written so a writer with a document and a chat and no repository can run it. A role that names a document absent from its context asks the author for it before acting on anything it governs and never proceeds from memory of it; this is written into the three writing roles and is a candidate Core line for a later cycle.
Context: Owner decisions (Dave), 2026-08-29. The constraint came from distribution: writers who are not fiducial users cannot satisfy a rule that reads a repository path. Solving for them solves the artifact question for Dave the same way.

## DEC-000260 — Writing bundles are distributed through GitHub Releases
Date: 2026-08-29
Decision: Bundles for writers who are not repository users are distributed through GitHub Releases: `bin/bundle` generates one bundle per audience, a release attaches them pinned to the repository SHA they were generated from, and a consumer downloads one file from one URL. No generated bundle is committed to the tree. Every writing bundle ships the Public Prose Criteria and the Voice document; the Outline skill is ask-on-demand; how the Voice template reaches a bundle is the bundle-system PRD's decision. New audience values `writer`, `copy-editor`, and `critic` are in use.
Context: Owner decision (Dave), 2026-08-28/29. Handed to the bundle-system PRD workstream as a requirement on 2026-08-28 and recorded in `OPEN-ITEMS.md` under the PRD entry (`docs/cycles/open-items-bundle-release-req-20260828T1900.md`). Adds a delivery surface downstream of `bin/bundle`; changes nothing in DEC-000210.

Commit decisions/log.md alone with message "decisions: DEC-000220 through DEC-000260, writing methodology". Push.

EDIT 2 — OPEN-ITEMS.md. Three changes and nothing else:

(a) Change the "Last updated:" line to 2026-08-29.

(b) In the section "## Corpus defects carried from prior batons", replace the bullet beginning "- Writing corpus:" with this bullet verbatim:
- ~~Writing corpus: the GitHub connector cannot see `davepierceops/writing` (404); `prose-criteria.md` audience tag defect.~~ RESOLVED 2026-08-29 by PR #230 (`53f7f40`): the writing repository's content was migrated from a snapshot at `387bde6`, so the connector no longer needs to see it; `prose-criteria.md` is retired to `docs/history/` and replaced by `public-prose-criteria.md` and `voice.md` (DEC-000240).

(c) Append the following section verbatim at the end of the file:

---

## Writing methodology landed — follow-ups

**Source:** writing workstream decision session, 2026-08-28/29; PR #230 (`53f7f40`); DEC-000220 through DEC-000260.

- **Full cycle owed on `policies/document-metadata-policy.md`.** Amended at `9160a86` to name `public-prose-criteria.md`, `voice.md`, and `voice-template.md` in the in-scope set and drop `prose-criteria.md`; a gate document, now `in-review` on main by Dave's decision to amend now and cycle later.
- **Doc-only agreements owed**, one each, sequential: `roles/copy-editor.md`, `roles/critic.md`, `roles/writer.md` (in-review), `skills/outline.md`, `public-prose-criteria.md`, `voice.md`, `voice-template.md`. All co-authored in the pane; none is a gate document.
- **Voice inbox triage owed**: the 2026-08-22 §4 and §5 entries in `voice-inbox.md`, against `voice.md`, as a doc-only cycle.
- **Retire `davepierceops/writing`** after the agreements above land and Dave confirms nothing is missing. Its `pieces/converging-on-intent/` directory (arc, outline, six pass reports at `387bde6`) is piece record, not methodology, and is Dave's to keep outside fiducial per DEC-000250.
- **Candidate Core line** (later cycle): a role that names a document absent from its context asks for it before acting on what it governs, and never proceeds from memory of it.
- **`voice-template.md` audience is `[human]`**; how it reaches a writing bundle is the bundle-system PRD's decision (DEC-000260).
- **`review-artifact.md` lists `critic` in its audience**; that slug now resolves to `roles/critic.md`. Whether the review-artifact skill should reach the Critic at all is open — the Critic emits comments in a document, not a review artifact.

Run bin/check-frontmatter --all from the worktree (must exit 0). Commit OPEN-ITEMS.md alone with message "OPEN-ITEMS: writing methodology landed; follow-ups". Push. Open a pull request from writing-trackers to main titled "Trackers: writing methodology decisions and follow-ups" — if gh cannot reach the API (a known sandbox failure), skip the PR, say so in the report, and the decision session opens it. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-writing-trackers" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; decisions/log.md commit SHA; OPEN-ITEMS.md commit SHA; origin/main SHA branched from; PR number or the gh failure; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
