# Review: specs/bin-land.md — cycle 2

Verdict: ready-with-findings
Reviewed: specs/bin-land.md @ 7801f36
Reviewer: Spec Reviewer Agent (execution session)
Date: 2026-08-23
Scope: Gate review of the cycle-2 revision, before Dave agrees it — confirmation that cycle 1's B1, N1, and N2 are discharged as Dave dispositioned them, plus a full re-run of the gate over all eight PRD sections: internal consistency, traceability, NFR coverage, AC testability, risk tolerance, open questions. Plus the Depth 1 continuity scan that fires automatically on every spec revision.
Cross-checked: reviews/bin-land-cycle-1.md, docs/cycles/bin-land-spec-2-20260823T192131Z.md @ 4145d1bd, specs/prd-template.md, roles/spec-reviewer-agent.md, skills/review-artifact.md, docs/global-context/core.md, policies/document-metadata-policy.md, policies/remote-write-verification-policy.md, LEXICON.md.
Not inspected: No TRD and no derived acceptance-criteria artifact for `bin/land` exists — `specs/` holds this PRD and the two templates and nothing else (*observed*) — so the Depth 1 spine scan ran against the PRD alone and could not check PRD→TRD or AC→journey traceability across artifacts. No implementation of `bin/land` exists; no behaviour claimed in the spec was executed. The historical directive corpus was not re-measured; the friction figures in §1 and §5 are carried unchanged from the research findings. A scratch-repository demonstration of the divergence case in F1 was attempted and not permitted in this session's sandbox, so that finding's evidence is inferred by reading, not verified by running. `docs/global-context/review-rubric.md` was not re-applied; cycle 1's O3 established it does not reach this document, and nothing in this revision changes that.
Findings: 0 blocking, 2 non-blocking, 2 observations
Prior cycle: reviews/bin-land-cycle-1.md
Dave should inspect: (1) Q2, whether `land` enters the methodology's vocabulary at all — you held it open and it is still the naming decision no one else can make; (2) Q3, whether the governed standing write-path document lands before this tool becomes agent-facing; (3) F1, the one case G1's second arm leaves to the TRD — the local tree not being at the branch's remote head — and whether you want it stated at PRD level or left where it is; (4) that `last-reviewed:` is still `null`, so your agreement commit is where this artifact's path and SHA get recorded.

## Cycle-1 findings: disposition confirmed

**B1 — discharged.** G1 is now conditional and states both arms: branch absent at origin creates from `origin/main` HEAD with the report's prior-head field reading `created`; branch present lands on top of that branch's current head with the prior head printed before the landing. AC-LAND-01 is split into AC-LAND-01a and AC-LAND-01b, one per arm, and each is derivable as a test case. The contradiction cycle 1 named — an unconditional G1 against a journey pair that produces the second invocation on every cycle — is gone: §3 J1 now describes the create arm and §3 J2 the land-on-top arm, and both trace to their own criterion. The "no flags and no modes" clause is stated in G1 and echoed in §2, so the resolution is carried in the goals rather than left in the journeys.

**N1 — discharged.** G6 names five output fields — branch, head SHA, prior head, per-file blob match, verification outcome — and AC-LAND-07 tests presence and labelling only, saying in its own text that mechanical parsing is a property of the serialization format and belongs to the TRD. The criterion no longer depends on a decision the document defers, which was the defect.

**N2 — discharged, and the residue is the correct one.** G4 no longer requires the tool to recognise `fatal: failed to store: 100001`. It states the decision rule — git's exit status plus the G5 verification, and nothing else — and relegates the string to a note explicitly marked as context for the reader rather than a requirement on the tool. The string does still appear in AC-LAND-04, and that is not a relapse: there it is an *input* to a test fixture, describing a stderr condition the tool must be shown to be indifferent to, not a literal the implementation matches. G4 and AC-LAND-04 now agree on which signal decides, where cycle 1 found them asserting opposite things.

**O1 — unchanged, by Dave's disposition.** `land` still appears in no `LEXICON.md` entry (*observed*), and Q2 still records the name as provisional. Nothing in this revision adopts it by use.

**O3 — unchanged.** Nothing in this revision brings the review rubric's criteria into scope for this document.

## F1 — non-blocking
Claim: G1's second arm states which commit the new commit must sit on, and the document nowhere states what the tool does when the local working tree is not already at that commit — the case where the branch's remote head moved after this session last fetched it.
Location: specs/bin-land.md §4 G1, second arm; §4 G2; §6 AC-LAND-01b.
Evidence: Inferred by reading. G1 fixes the base at the branch's remote head as of this invocation's own fetch. G2 stages from the local working tree. The document does not connect the two: it does not say whether the tool moves the tree to that head, refuses when the tree is elsewhere, or requires the caller to have arrived there. A scratch-repository demonstration was attempted and not permitted in this sandbox, so no case was run.
Consequence: Two starting states are unspecified. Where local HEAD is an ancestor of the remote head and uncommitted changes exist, the tool must carry those changes onto a tree it is not currently at, and git will refuse that move on any path the changes touch. Where local HEAD carries commits the remote does not, basing on the remote head puts those commits outside the new history. An implementer choosing for themselves at the TRD stage could land the second case in a way that leaves local work unreachable.
Fix: One sentence in G1 stating the tool's posture when the local tree is not at the resolved base — most plainly, that it establishes the base or stops, and never resolves the mismatch by discarding a commit. Alternatively, an explicit deferral naming the case as the TRD's, which is materially different from the current silence.
Why this is not blocking: the spec already bounds the outcome from two directions. §7 lists any destructive operation among what is not accepted, so the history-losing resolution is out of tolerance rather than merely undesirable; and G7 with J3 requires the tool to stop, report what was established, and exit non-zero on any failure, which is a licensed answer for this case. The primary journey pair — J1 then J2 in one session, where local HEAD is the head that invocation put there — is fully specified. What is missing is a statement, not a decision.
Related: F2.

## F2 — non-blocking
Claim: AC-LAND-04 forbids more than G4 requires — the criterion says no code path *reads* stderr content, where the goal says only that no behaviour *keys on* it.
Location: specs/bin-land.md §6 AC-LAND-04; §4 G4.
Evidence: Inferred by reading, comparing the two texts at this SHA. G4: "No behaviour keys on the content of stderr, in either direction." AC-LAND-04: "No code path in the source reads, matches, or branches on stderr content."
Consequence: A tool that captures git's stderr in order to pass it through into its own report — which keys no decision on the content and which the G4 note's spirit suggests is useful — satisfies the goal and fails the criterion as written. A Test Designer deriving from AC-LAND-04 would write a static check that rejects a conforming implementation, and the criterion would become the de facto contract over the goal it was derived from. This is the smaller sibling of the cycle-1 N2 mismatch, in the opposite direction.
Fix: Drop "reads" from AC-LAND-04, leaving "matches, or branches on", so the criterion tests the decision rule G4 states. If passthrough is meant to be forbidden as well, G4 says so instead, and the two agree again.
Related: F1.

## O1 — observation
Claim: The split of AC-LAND-01 into AC-LAND-01a and AC-LAND-01b retires an identifier that a prior artifact cites, and the document notes the equivalent retirement for the open questions but not for this one.
Location: specs/bin-land.md §6; §8, closing paragraph; reviews/bin-land-cycle-1.md, B1.
Evidence: Inferred by reading. §8's closing paragraph states that Q1's and Q4's identifiers are retired rather than reused and says what each referred to. §6 carries no equivalent note, and cycle 1's B1 refers to "AC-LAND-01", which now names nothing on its own.
Consequence: Nothing adverse yet — no TRD, no test suite, and no other document references the AC identifiers. Recorded because the asymmetry is the kind of thing that reads as an oversight later, and because once test cases carry these identifiers a silent renumbering stops being free.
Fix: Optional, and Dave's call whether it is worth the line: a parenthetical in §6 noting that AC-LAND-01 was split at cycle 2. The review-artifact schema forbids retrofitting cycle 1, so the stale reference there stays as the record of what was reviewed.

## O2 — observation
Claim: Two consequences of this document's placement and status, established at cycle 1, are unchanged by this revision and remain live.
Location: specs/bin-land.md, frontmatter; policies/document-metadata-policy.md, "Agent behavior" and "Expedited return to `agreed`".
Evidence: Verified by running and by reading. `bin/check-frontmatter --all` matched 52 in-scope files at this commit and exited 0 (*observed*). The frontmatter reads `status: draft`, `last-reviewed: null`, which is what the cycle-2 directive instructed — content edits keep it draft. Two rules follow: while the spec is `draft`, implementing `bin/land` needs Dave's explicit per-task confirmation; and the metadata policy excludes `specs/` from both the expedited and doc-only paths, so this document reaches `agreed` only through this gate.
Consequence: None adverse. Recorded so the `last-reviewed` pointer is not forgotten at agreement — `agreed` requires it non-null and naming an artifact that states in its own scope that it reviewed this document at the cited SHA, which this artifact does for `7801f36`.
Fix: None to the document. At agreement, `last-reviewed: reviews/bin-land-cycle-2.md @ <sha>`.

## Depth 1 continuity scan

The spine is PRD-only, so the scan reduced to traceability within this document and found it complete. Every criterion in §6 traces to a goal in §4: AC-LAND-01a and AC-LAND-01b to G1's two arms, 02 to G2, 03 to G3, 04 to G4, 05 and 06 to G5, 07 to G6, 08 and 09 to G7, and 10 to the §4 non-goals together with the Security NFR. Every journey in §3 has a criterion that exercises it: J1 at AC-LAND-01a, J2 at AC-LAND-01b and AC-LAND-06, J3 at AC-LAND-09. All eight template sections are present and substantively answered, and every NFR dimension is addressed or marked N/A with a reason.

Two claims that sit against standing rules were re-checked at this revision and both still hold. G7's never-retry is stricter than `policies/remote-write-verification-policy.md`'s two-consecutive-failures stop condition rather than in conflict with it, and G5 does what that policy's "Known gap — landing is verified, content is not" section asks for and does not itself specify (*observed*, that section exists at the cited policy). G6's two provenance labels remain a subset of Core rule 6's four, stated as a subset, and the revision's new prior-head field is labelled on the same terms as the rest.

## On what the revision did to the document's centre of gravity

Worth stating because it is a change in kind, not only in wording. Before this revision the spec tried to prevent a stale base and could not describe its own second invocation. It now does something narrower and more defensible: it fixes the base to remote state, and it makes the base *legible* — the prior head is printed before the landing, so an executor's report carries what the landing extended whether or not the landing completed. Staleness moves from something the tool was implicitly claiming to prevent to something the evidence trail exposes, which is the posture the rest of this methodology takes everywhere else. F1 is the one place that posture is not yet written down completely.
