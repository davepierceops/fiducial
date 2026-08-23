# Review: specs/bin-land.md — cycle 1

Verdict: changes-required
Reviewed: specs/bin-land.md @ 87ae153
Reviewer: Spec Reviewer Agent (execution session)
Date: 2026-08-23
Scope: Gate review of a spec at initial authorship, before Dave agrees it — all eight required PRD sections, internal consistency, traceability, NFR coverage, AC testability, risk tolerance, open questions. Plus the Depth 1 continuity scan that fires automatically on every spec revision.
Cross-checked: specs/prd-template.md, roles/spec-reviewer-agent.md, skills/review-artifact.md, docs/global-context/core.md, policies/document-metadata-policy.md, policies/remote-write-verification-policy.md, LEXICON.md, docs/global-context/review-rubric.md, skills/directive-authoring.md, docs/research/gh-write-friction-20260823T184149Z.md @ 49bd6ff4, decisions/log.md (DEC-000160, DEC-000180), .claude/settings.json, bin/aimeta/repo.py.
Not inspected: No TRD and no derived acceptance-criteria artifact exist for this spec, so the Depth 1 spine scan ran against the PRD alone and could not check PRD→TRD or AC→journey traceability. No implementation of `bin/land` exists — the spec was not checked against code, and no behaviour claimed here was executed. `specs/trd-template.md` was not read; nothing in this document is a TRD. The historical directive corpus was not re-measured; the friction figures in §1 and §5 are carried from the research findings, not independently recounted. Whether `git push` exits non-zero when it emits `fatal: failed to store: 100001` was not established — see B1's sibling finding N2.
Findings: 1 blocking, 2 non-blocking, 3 observations
Dave should inspect: (1) the branch-exists behaviour B1 names — it is the one question in this spec that no one but you can answer, and every cycle hits it; (2) whether `land` enters the methodology's vocabulary at all, given LEXICON's active retirement programme (spec §8 Q2); (3) whether the governed standing write-path document lands before this tool becomes agent-facing (spec §8 Q3), which the research findings rank as a prerequisite; (4) that this spec sits at `specs/`, which puts `bin/land` implementation under the metadata policy's build-gating rule while the spec is `draft` — see O2.

## B1 — blocking
Claim: G1 states an unconditional "branch from `origin/main` HEAD", which cannot describe the second invocation against the same branch — the sequence J1 followed by J2 produces on every cycle — and AC-LAND-01 asserts a parent commit that is false for it.
Location: specs/bin-land.md §4 G1; §6 AC-LAND-01; §3 J1 and J2; §8 Q4.
Evidence: Inferred by reading, and demonstrated by this session's own execution: this session landed a directive file on `bin-land-spec` and must land the spec and this artifact on the same branch, which is exactly the second invocation G1 does not cover. Verified by running only in the negative sense that no implementation exists to test.
Consequence: An implementer at the TRD/AC stage has three defensible behaviours to choose from — fail because the branch exists, check the branch out and require it be a descendant of `origin/main`, or re-branch and discard the earlier commit — and the spec licenses none of them. The third silently destroys landed work. AC-LAND-01 cannot be written as a passing test for the primary journey pair, so the AC set is internally inconsistent with §3.
Fix: G1 states what happens when the named branch already exists locally, at the remote, or both, and AC-LAND-01 is split so the first-invocation and subsequent-invocation cases each carry their own criterion. §8 Q4 records the gap but does not discharge it: Q4 marks a question as open while G1 continues to state an unconditional behaviour, so the document contradicts itself rather than deferring cleanly. Q1's resolution does not settle this — the "stays two invocations" answer requires the behaviour and the "becomes a mode" answer does not remove it.
Related: N1.

## N1 — non-blocking
Claim: AC-LAND-07 is not testable as written, because §4 G6 defers the output format to the TRD while the criterion requires the output to "parse mechanically into those fields".
Location: specs/bin-land.md §6 AC-LAND-07; §4 G6.
Evidence: Inferred by reading. The criterion names required fields and a parsing property but no format, and no format is named anywhere in the document.
Consequence: The Test Designer cannot derive a case from AC-LAND-07 without inventing a format, and an invented format becomes the de facto contract. The role's own gate criterion — acceptance criteria concrete enough to derive test cases from — is not met for this one criterion.
Fix: Either name the format in §4 G6, or restate AC-LAND-07 as a field-presence criterion and add a separate parsing criterion at the TRD stage, so the PRD-level criterion is testable on its own terms. Deferring a technical format to the TRD is legitimate; carrying a criterion that depends on the deferred decision is what makes this a finding.

## N2 — non-blocking
Claim: G4 requires the tool to know the literal string `fatal: failed to store: 100001`, and the observed evidence is that no correct implementation needs to know it.
Location: specs/bin-land.md §4 G4; §6 AC-LAND-04.
Evidence: Verified by running, in this session's sandbox: `git ls-remote origin bin-land-spec` exited 0 while writing `fatal: failed to store: 100001` to stderr; `git fetch origin main` exited 0 while writing the same line. Both are *observed*. Whether `git push` also exits 0 when it emits that line is *unknown* — this session's push did not emit it, and no failure was induced to find out.
Consequence: Two costs, in opposite directions. If git's exit code is already correct, the tool carries one sandbox's error text as a literal — the environment lore this whole effort exists to move out of prose, relocated into code where it is at least tested but still wrong the day the helper's message changes. If git's exit code is *not* correct on push, then AC-LAND-04's assertion that success "is not derived from stderr content in either direction" contradicts G4's requirement to recognise the string, and the spec does not say which signal decides.
Fix: State in G4 which signal determines that a push succeeded — git's exit status, the `ls-remote` and blob verification of G5, or both — and reduce the string to what it is: something the tool may pass through to its own output as context, never a term in the success decision. Then AC-LAND-04 tests the decision rule rather than the string.

## O1 — observation
Claim: `land` is a term new to this methodology, proposed while `LEXICON.md` is running an active retirement programme against loosely-introduced vocabulary.
Location: specs/bin-land.md §8 Q2; LEXICON.md, "Retired terms".
Evidence: Inferred by reading. `LEXICON.md` retires `prompt`, `dispatch`, `sync block`, and `track`, each with a stated replacement. `land` appears in no LEXICON entry.
Consequence: If the name is adopted by use before it is decided, the decision is made by drift — the failure mode the lexicon exists to prevent. This is not a defect in the spec, which states the name is provisional and correctly declines to edit `LEXICON.md`; it is recorded so the provisional status does not quietly expire.
Fix: None available to this role. Dave's, per Q2.

## O2 — observation
Claim: Placing this spec at `specs/` rather than at `docs/packages/`, where the repository's existing tooling specs live, changes which rules govern it — deliberately, and with consequences worth stating.
Location: specs/bin-land.md, frontmatter; policies/document-metadata-policy.md, "Scope" and "Agent behavior".
Evidence: Verified by running and by reading. `bin/check-frontmatter --all` matched 52 in-scope files at this commit, this document among them, and exited 0. `docs/packages/package-a-spec.md` states in its own text that it carries no lifecycle frontmatter because `docs/**` is out of scope. Three consequences follow from the placement: this document is frontmatter-enforced; it is gated by this role rather than the Context Quality Reviewer; and while it is `draft`, the metadata policy's build-gating rule applies, so implementing `bin/land` needs Dave's explicit per-task confirmation.
Consequence: None adverse. The placement was directed and it is the stricter of the two options. Recorded because the build-gating consequence is the kind of thing a later session discovers at the wrong moment.
Fix: None. Dave confirms per-task when implementation is directed, or agrees the spec first.

## O3 — observation
Claim: Three review-rubric criteria that a reader might apply to this document do not reach it, and one of them would misread a dictated instruction as a defect.
Location: docs/global-context/review-rubric.md, criteria 1, 3, and 4; roles/spec-reviewer-agent.md, "Gate review responsibilities".
Evidence: Inferred by reading. The rubric's own header states it is applied by the Context Quality Reviewer to the files in that role's scope; the Spec Reviewer's scope is the PRD, the TRD, and their acceptance criteria, and nothing else. Criterion 3 forbids references to other files by path, and this spec cites the research findings, the remote-write policy, and two decision-log entries by path — citation the directive that originated the spec explicitly requires. Criterion 1 assumes a bundled reader who cannot open another file, which is not how a spec spine is read. Criterion 4 forbids restating a Core rule, and §4 G6 references Core's provenance classes in order to explain why the tool emits a subset of them, which is a cross-reference rather than a restatement.
Consequence: A later reviewer applying the rubric wholesale to this document would raise three defects that are not defects. The rubric criteria that do reach it — 2 (audience selector), 9 (filename convention), 11 (escalation not left to inference), 12 (contradicts no other governed file) — were checked and pass.
Fix: None to this document.

## On the two consistency checks that matter most

Criterion 12 and the role's internal-consistency duty were the checks most likely
to fail here, because the spec makes two claims that sit close to standing rules,
and both survive inspection.

§4 G7 requires the tool never to retry, where
`policies/remote-write-verification-policy.md` sets its stop condition at two
consecutive qualifying failures. The spec states the relationship rather than
leaving it to a reader: the policy governs when an agent must stop absorbing
failures, and this tool stops at the first because it never retries at all.
Stricter, not contradictory. It also does what the policy's own "Known gap"
section asks for and does not specify — a content-expectation check alongside the
landing check — and says so.

§4 G6 has the tool emit two provenance labels where Core rule 6 names four. The
spec states this is a subset rather than a redefinition, on the ground that a
tool observes a fact or fails to and is never in a position to infer or to be
told. That reasoning holds, and the narrower set is the honest one for a
non-reasoning emitter.
