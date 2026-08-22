# Review: policies/project-setup-requirements.md — cycle 2

Verdict: ready-with-findings
Reviewed: policies/project-setup-requirements.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, judged against the current foundation. Confirmation pass within the Pass 1 reconciliation re-gate.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/document-metadata-policy.md, policies/commit-and-change-control-policy.md — all @ 8402c23; plus the tree at e922926 and 2a722bb.
Not inspected: whether branch protection is actually configured on the forge (the file states it cannot be verified from the repository, and it cannot); `bin/install-hooks` behaviour.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/project-setup-requirements-cycle-1.md (reviewed @ 2a722bb)
Dave should inspect: none.

## PSR-1 — non-blocking
Claim: Requirement 2 restates the frontmatter in-scope set in prose and the restatement names a document that does not exist.
Location: policies/project-setup-requirements.md:45-48 ("...and the operating model, the lexicon, and the readme at the root.")
Evidence: Verified by running — the repository-root `README.md` was deleted at e922926 (2026-08-21). This file was reviewed at 2a722bb, after the deletion, so the staleness was missed rather than introduced. The authoritative in-scope set is the glob list in policies/document-metadata-policy.md, from which `bin/aimeta/scope.py` extracts it at runtime; this file's prose is a second statement of the same rule with no mechanism keeping the two in step, which is how it drifted. Criterion 4's neighbourhood — Core is not the other home here, the metadata policy is — recorded as criterion 11, an underspecified condition an adopting repo would have to resolve by inference.
Consequence: An adopting project reads the prose list, provisions frontmatter for a root README it may not have, and has no way to tell that the glob list is the one enforcement actually reads.
Fix: Drop the enumeration and state the requirement as "the in-scope set the document metadata policy defines," which is what enforcement reads. If the enumeration stays, remove "the readme at the root."
