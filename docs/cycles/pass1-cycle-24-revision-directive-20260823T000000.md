# Directive — Pass 1, Cycle 24: revision of specs templates, vendors, engagements (cycle 23)

Date: 2026-08-23
Route: fresh
Model: frontier
Role: Coder, executing reviewer dispositions

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Base: main @ 86ed441.
Review artifacts, all on main: reviews/prd-template-cycle-1.md, trd-template-cycle-1.md, README-cycle-4.md, environment-config-cycle-1.md, assistant-cycle-1.md, cartographer-cycle-1.md, skeptic-cycle-1.md, quiet-notes-cycle-1.md. Read each before editing its file.
Foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, docs/global-context/review-rubric.md, engagements/working-with-dave.md.

## Rules for every edit

- Every finding is applied as its artifact's Fix states unless this directive says otherwise.
- No pointers. State the rule or delete the sentence.
- Retired terms removed on touch; LEXICON carve-out senses stay and are not counted. Vendor and model names: "tracker issue", "forge", "the execution session", "a flag backend"; or deleted. Inside vendors/claude-code/, the vendor's own name is the subject; a second vendor's name is removed.
- Each retained file opens with one line naming the session kind it governs.
- The SLO / Top K requirement has one home, operating-model.md change package item 7; the Top K definition has one home, LEXICON. Delete every other copy in touched files.
- Files through Pass 1 are edited only where named below, minimally.
- Engagement files gain frontmatter: status draft, last-reviewed null, audience as stated. The frontmatter checker does not yet cover engagements/**; that is Pass 2. Write the frontmatter to the same schema regardless.

## Dispositions

### specs/prd-template.md — retain-with-changes
Apply PRD-1 through PRD-12. PRD-1: audience [chief-of-staff, spec-reviewer-agent, human]. PRD-8: the authoring checklist moves to roles/spec-reviewer-agent.md as what the Spec Reviewer inspects in a PRD, phrased as inspection items; deleted here. PRD-9: "must confirm".

### specs/trd-template.md — retain-with-changes
Apply TRD-1 through TRD-13. TRD-1: audience [architect-agent, spec-reviewer-agent, human]. TRD-6: delete blocking from the verification-class list; classes are LEXICON's evidence classes and the template names them without redefining them (TRD-7). TRD-9: the checklist moves to roles/spec-reviewer-agent.md as what the Spec Reviewer inspects in a TRD; deleted here. TRD-11: "a flag backend chosen in the TRD".

### vendors/README.md — merge the swap test into operating-model.md; retain a directory note
Apply RM-1 through RM-9. RM-3: in operating-model.md, extend the Agents must-not bullet "store durable policy only in vendor-specific tooling" with one sentence: a statement belongs in a governed document unless swapping the vendor would leave it false. What remains of the README: under ten lines, audience [human], stating that each subdirectory describes one harness's environment, that harnesses are adapters downstream of bundles, and that no harness reads the repository. RM-2, RM-4: delete the misquotation and the README principle citation.

### vendors/claude-code/environment-config.md — retain-with-changes
Apply EC-1 through EC-10. EC-1: rewrite the Divergence section to describe .claude/settings.json as committed at 86ed441 — read the file; state what it carries and nothing it does not. EC-3, EC-4: delete the gating-principle statements; the push mechanics policy is the home and this file describes settings only. EC-8: audience [human].

### engagements/assistant.md — retain-with-changes
Apply AS-1 through AS-11. AS-1: frontmatter, audience [assistant, human]. AS-3: session-kind line — the Assistant runs as a decision session; the decision layer is in its bundle; the restated rules (AS-5, AS-6, AS-7, AS-9) are deleted. AS-4: the running list is a record per decision-layer rule 9 as amended; state it as one sentence: the Assistant keeps a loose-end record in the engagement's working area. AS-8: the quiet-notes practice stays as one sentence, no fixed filename, written on first use.

### engagements/cartographer.md — retain-with-changes
Apply CA-1 through CA-7. CA-1: frontmatter, audience [cartographer, human]. CA-6: state the session kind the file's own content implies; report which.

### engagements/skeptic.md — retain-with-changes
Apply SK-1 through SK-9. SK-1: frontmatter, audience [skeptic, human]. SK-3: state in this file that an engagement has no release gate, so the verdict is input to Dave; in roles/skeptic-risk-agent.md add one sentence that inside the change flow the Skeptic/Risk review is a stage with gate force and that the engagement Skeptic is a different role. SK-4: output per skills/review-artifact.md (named, not pathed); delete the shape block. SK-8: the overlapping checklist items are deleted here; the role document keeps them.

### engagements/quiet-notes.md — retire
Apply QN-1 through QN-5. git rm.

## Verification

1. bin/check-frontmatter --all passes; bin/bundle-methodology runs clean; no file anywhere names quiet-notes.md outside docs/cycles/, reviews/, retros/, docs/batons/, and historical records — report any hit in a governed document.
2. grep all touched files for: the four retired terms in their retired sense; a second vendor's name anywhere, any vendor name outside vendors/, any model name; the Top K requirement and definition; path-shaped references — list each survivor with its reason or remove it.
3. Each retained file, in full, against rubric criteria 1, 3, 4, 6, 7, and 11 before committing.

## Output

Commit on p1-cycle-24-revision, push. Open a pull request against main titled "Pass 1 cycle 24 revision: specs templates, vendors, engagements" via the REST API with curl if gh cannot authenticate; if neither works, report the compare URL. Do not merge. PR body: per file, findings applied as written and varied, one line each for the latter.

## Report shape

One line per file: path, action, applied / varied. Then: the cartographer session kind; verification-1 hits; verification-2 survivors with reasons. Then branch, SHA, PR number or compare URL.
