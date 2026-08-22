# Review: policies/document-metadata-policy.md — cycle 14

Verdict: changes-required
Reviewed: policies/document-metadata-policy.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, judged against the current foundation. Confirmation pass within the Pass 1 reconciliation re-gate. Every factual claim the file makes about other paths in the repository was checked against the tree at 8402c23.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/project-setup-requirements.md, policies/commit-and-change-control-policy.md, skills/conversation-retro.md, skills/spec-review-cycle.md, bin/aimeta/scope.py, bin/check-frontmatter — all @ 8402c23; plus the tree at e922926 and 2a722bb.
Not inspected: `bin/` behaviour beyond reading how `bin/aimeta/scope.py` extracts the in-scope globs from this file's Scope section; the two pre-existing `bin/tests` failures; whether the expedited and doc-only conditions are the right conditions.
Findings: 3 — 2 blocking, 1 non-blocking
Prior cycle: reviews/document-metadata-policy-cycle-13.md (reviewed @ 2a722bb)
Dave should inspect: DMP-1 — closing it means either creating nine `roles/` files for the engagement roles or widening the audience rule, and that is a structural decision about whether engagement roles are roles.

## DMP-1 — blocking
Claim: The `audience:` rule states a value set that eleven files in the corpus violate.
Location: policies/document-metadata-policy.md:91-93 ("Values are `roles/` file slugs plus two reserved values: `all-roles` and `human`. Any other value fails enforcement.")
Evidence: Verified by running — `roles/*.md` at 8402c23 yields exactly ten slugs: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Eleven files carry `audience:` values outside that set plus the two reserved ones — `assistant` (9 files), `cartographer` (7), `skeptic` (6), `implementer` (6) — across engagements/assistant.md, engagements/cartographer.md, engagements/skeptic.md, engagements/working-with-dave.md, and all seven files under engagements/sre/. The `implementer` slug was introduced at 0e07753 (cycle 25); this file was last reviewed at 2a722bb, before it. Criterion 11.
Consequence: The rule reads as enforced and is not. It is not enforced only because `engagements/**` is outside the in-scope globs — the known scope gap — so the moment that gap is closed, eleven files fail the check the policy says they fail today. Meanwhile a reader of this policy cannot tell that four widely-used audience values are illegal by its own text.
Fix: Either name the engagement role documents as a second source of valid slugs, or state the rule as "the basename of a role document anywhere in the corpus." Do not close the `engagements/**` scope gap before this is settled.

## DMP-2 — blocking
Claim: The gate-document class — a normative list — names a document that does not exist at 8402c23.
Location: policies/document-metadata-policy.md:152 (`README.md`, last entry of the expedited path's condition-3 list)
Evidence: Verified by running — the repository-root `README.md` was deleted at e922926 (2026-08-21, cycle 6 revision); `git cat-file -e 8402c23:README.md` fails. The same dead path appears at policies/document-metadata-policy.md:34 in the in-scope glob list, where `bin/check-frontmatter --all` reports it as `WARN [unmatched-glob]`; that warning is a known and excluded item, but the gate-class entry is a separate statement and is not. The file was reviewed at 2a722bb, which is *after* the deletion, so no foundation change caused this — it was missed. Criterion 11.
Consequence: The list is described as "normative where it names a document." A normative list naming a deleted file is unfollowable at that entry, and its presence implies the list is current when it has not been reconciled since the deletion.
Fix: Remove the `README.md` entry from the gate-document class. Decide separately whether the in-scope glob for it goes too.

## DMP-3 — non-blocking
Claim: The file uses a retired role name.
Location: policies/document-metadata-policy.md:280 ("Orchestrators may select context by `audience`.")
Evidence: Verified by running — no `roles/orchestrator*.md` exists at 8402c23; `reviews/orchestrator-agent-cycle-1.md` is the record of its review, and the role document is gone. `orchestrator` appears nowhere else in the corpus as a live term. Criterion 8's neighbourhood; more precisely criterion 11, since the sentence grants a selection permission to a role that does not exist.
Consequence: The one line describing who may select context by audience names nobody. No live role reads it as addressed to itself, so the permission is inert.
Fix: Restate as the bundler's behaviour, or name the role that actually selects context, or delete the line — bundle membership is declared by the document, not chosen by a reader.
