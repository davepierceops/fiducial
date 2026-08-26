---
status: in-review
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Release Readiness

This policy governs both session kinds: decision sessions and execution
sessions.

A change is **release-ready** when the evidence for it exists and is stated,
and every known gap carries a release-impact label of `deferred`,
`accepted-risk`, or `not-material`. A gap labelled `blocking` means the change
is not release-ready.

The release decision itself is gated by the commit and change control policy.
