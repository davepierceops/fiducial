# Directive — Pass 1, Cycle 22: revision of the skills (cycles 21a/21b)

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Coder, executing reviewer dispositions

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Base: main @ 017b86f.
Review artifacts, all on main: reviews/spec-review-cycle-cycle-9.md, directive-dispatch-cycle-9.md, boundary-audit-cycle-1.md, change-package-creation-cycle-1.md, command-blocks-cycle-5.md, conversation-retro-cycle-1.md, evidence-review-cycle-1.md, release-readiness-review-cycle-1.md, test-plan-review-cycle-1.md. Read each before editing its file.
Foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, docs/global-context/review-rubric.md.

## Rules for every edit

- Every finding is applied as its artifact's Fix states unless this directive says otherwise.
- No pointers. State the rule or delete the sentence. Paths that stay: filenames a skill prescribes as a convention (reviews/<stem>-cycle-<n>.md, retros/, docs/cycles/).
- Retired terms removed on touch; count them. Vendor and model names: "tracker issue", "forge", "the execution session", "frontier tier" / "standard tier"; or deleted.
- Each retained skill opens with one line naming the session kind it runs in.
- Gap labels are LEXICON's four. Agents apply blocking, deferred, or not-material; accepted-risk is applied only by Dave's go or the release process. State this once in skills/review-artifact.md and nowhere else.
- The SLO / Top K sentence has one home: operating-model.md, change package item 7. Delete every other copy in the files this cycle touches. List every copy outside this cycle's scope in the report, with path and line.
- Frontmatter carries only the fields the metadata policy defines; name: and description: are deleted wherever found.
- Files through Pass 1 (Core, decision-layer, LEXICON, operating-model, the roles) are edited only where named below, minimally.

## New file: skills/review-artifact.md
Audience: [spec-reviewer-agent, context-quality-reviewer, reviewer-agent, skeptic-risk-agent, chief-of-staff, human]. Status draft. Content: the review artifact schema moved intact from skills/spec-review-cycle.md — header, findings, prose rule, filename convention — plus the accepted-risk sentence above. Session-kind line: written by execution sessions, triaged in decision sessions. No rationale sections (S12's cuts apply here, not in the old location).

## Dispositions

### skills/spec-review-cycle.md — retain-with-changes (procedure only)
Apply S1 through S14. S1: the schema moves out per the new file above. S2: the cycle directive format section is deleted; Core's directive rule is the only form. S5: replace the transport constraints with the rule as it holds in a bundle compiler: documents are read by the execution session from the repository; full documents are never carried through the decision session; reviewed SHAs are recorded in the directive. S9: the re-gate is run by the role that gated. S10: scope is any canonical document; the Context Quality Reviewer runs rubric cycles, the Spec Reviewer runs spec cycles; state both. Target: under 120 lines.

### skills/directive-dispatch.md — rename to skills/directive-authoring.md, rewrite
Apply D1 through D17. Content of the new file: session-kind line (decision sessions); the surviving authoring constraints (D10 applied, no paths); the naming convention stated as Core rule 14's form for docs/cycles/; and from D16 nothing else. Audience: [chief-of-staff, human]. Status draft, last-reviewed null. D11: the one surviving executor obligation — if files this session did not change move, HEAD moves, or an index lock appears, stop and report rather than recover — is added to docs/global-context/core.md as one sentence in its execution-session rules, and does not appear in the skill. D12: delete the naming schema. D14: resolved by the rewrite. Use git mv so history follows.

### skills/command-blocks.md — retain-with-changes; single home for command-block rules
Apply CB-1 through CB-7. CB-1: in docs/global-context/decision-layer.md, reduce rule 15 to one sentence: command blocks conform to the command-blocks skill. Delete the restated criteria there. CB-3: delete name: and description:. CB-5: delete the maintainer-facing passages.

### skills/conversation-retro.md — retain-with-changes
Apply CR-1 through CR-8. CR-1: filename is retro-<ISO 8601 basic timestamp>.md, matching Core rule 14 and the current retros. CR-8: the trigger is the end of a decision session, or Dave directing one.

### skills/boundary-audit.md — retain-with-changes
Apply BA-1 through BA-6. BA-2 per the label rule above. BA-6: output is a review artifact per skills/review-artifact.md; delete the shape list.

### skills/evidence-review.md — retain-with-changes
Apply ER-1 through ER-6. ER-1: the Skeptic does not emit a ship recommendation (cycle 20, SK-3); the slot belongs to the Reviewer. ER-2: "risk level" is replaced by LEXICON's labels. ER-4: define "boundary ledger" in one clause or replace it with the boundary declaration the verification-boundary policy requires. ER-6: output per skills/review-artifact.md.

### skills/test-plan-review.md — retain-with-changes
Apply TP-1 through TP-6. TP-1: test-designer-agent is removed from audience:; one sentence states that the plan's author does not review it. TP-4: output per skills/review-artifact.md.

### skills/change-package-creation.md — retire
Apply CP-1 through CP-5. operating-model's change package list is the home and already carries the two items this skill dropped; nothing transfers. git rm.

### skills/release-readiness-review.md — merge into roles/release-manager-agent.md, then delete
Apply RR-1 through RR-5. Carry the assembly method into the role document as a short procedure beneath the package list, if the role does not already state it; carry nothing else. git rm.

## Verification

1. bin/check-frontmatter --all passes; bin/bundle-methodology runs clean; no audience: value or file anywhere names change-package-creation, release-readiness-review, or directive-dispatch; grep the whole tree for those three stems and report every hit outside docs/cycles/, reviews/, retros/, and docs/batons/.
2. grep all touched files for: the four retired terms; GitHub, MCP, Claude, Opus, Sonnet, Haiku; "Needs Dave decision"; name: and description: in frontmatter; path-shaped references outside prescribed filename conventions — list each survivor with its reason or remove it.
3. Each retained skill and the new file, in full, against rubric criteria 1, 3, 4, 6, 7, 9, and 11 before committing.

## Output

Commit on p1-cycle-22-revision, push. Open a pull request against main titled "Pass 1 cycle 22 revision: skills (21a/21b)" via the REST API with curl if gh cannot authenticate; if neither works, report the compare URL. Do not merge. PR body: per file, findings applied as written and varied, one line each for the latter.

## Report shape

One line per file: path, action, applied / varied. Then: retired terms removed; the SLO / Top K copies outside scope, path and line; verification-1 hits; verification-2 survivors with reasons. Then branch, SHA, PR number or compare URL.
