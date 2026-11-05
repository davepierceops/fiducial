# Claim and evidence rule overlap — discussion inventory

Observed source: active rules on intake/claude-rule-pruning after PR #423. Searched active rule bodies for claims, evidence, labels, uncertainty, assertions, support, proof, reporting and verification; read the resulting candidate bodies and role selectors. The generator's --near is lexical Jaccard similarity, not semantic search; grouping below is the assistant's semantic assessment. This inventory is a discussion aid, not an approved consolidation or retirement list. R0174's labeling obligation is retained at Dave's request.

The requested three encode distinct obligations: inspectable support (R0172), provenance labels (R0174), and verification classes (R0021). The latter two are separate axes: observing a mocked test pass does not establish live behavior. Any combined row must preserve both. A merged rule must also preserve applicability: all-role core rows and narrower software verification rows currently have different selectors.

## Three requested rows

### R0172

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Support every claim with inspectable evidence.

### R0174

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Label every claim observed (you saw it), inferred (you reasoned to it), told (someone said it), or unknown.

### R0021

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Carry exactly one evidence class on every verification claim: mock-verified, contract-verified, live-verified, browser-verified, production-verified, or unverified.

## Closest claim-support, uncertainty and evidence-limit overlap

### R0177

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Say what is unverified.

### R0179

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Say "could not determine" rather than guess.

### R0110

In current installed CLAUDE.md: yes. Kind: instruction.

Role: test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent, release-manager-agent, chief-of-staff. Corpus: software. Session: decision, execution.

State the boundary of every verification claim you make — what the evidence behind it covers, and where that coverage stops.

### R0111

In current installed CLAUDE.md: yes. Kind: instruction.

Role: test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent, release-manager-agent, chief-of-staff. Corpus: software. Session: decision, execution.

Claim only what a test actually proves. A passing test, a green suite, or a small test licenses no claim wider than the scenario it executed.

### R0783

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent. Corpus: software. Session: decision, execution.

Do not let a test imply broader confidence than it actually supports.

### R0461

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Never claim live behavior from mocked evidence.

### R0161

In current installed CLAUDE.md: yes. Kind: instruction.

Role: test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent, release-manager-agent, chief-of-staff. Corpus: software. Session: decision, execution.

Judge verification by boundary analysis, never by line coverage: coverage shows that code executed, not that it was verified against production-relevant conditions.

### R0455

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

State the assumptions your work rests on.

## Related operational applications with distinct triggers

### R0181

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Read the repository before asserting its state.

### R0182

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Never claim completeness without having done the sweep.

### R0186

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Flag only what you can demonstrate, cite the location, and label each finding defect, suggestion, or accepted risk.

### R0190

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Confirm the correct content landed before reporting a write.

### R0192

In current installed CLAUDE.md: yes. Kind: instruction.

Role: architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, copy-editor, critic, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent, writer. Corpus: software, writing. Session: decision, execution.

Where you cannot read a write back, report only what the operator reported.

## Role-specific variants outside the root

### R0156

In current installed CLAUDE.md: no. Kind: instruction.

Role: test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent. Corpus: software. Session: execution.

A headless DOM is not browser rendering; never report one as the other.

### R0157

In current installed CLAUDE.md: no. Kind: instruction.

Role: test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent. Corpus: software. Session: execution.

Agent review counts as evidence only where you state what was reviewed; unstated review is not evidence.

### R0821

In current installed CLAUDE.md: no. Kind: instruction.

Role: writer, copy-editor, critic. Corpus: writing. Session: decision.

Signal each claim's tier in the sentence: relayed, demonstrated, grounded, or opinion.

### R1008

In current installed CLAUDE.md: no. Kind: instruction.

Role: critic. Corpus: writing. Session: decision.

In the Skeptic pass, enumerate every claim in the piece yourself, locate each claim's support in the piece, and test whether that support carries the claim.

### R1009

In current installed CLAUDE.md: no. Kind: instruction.

Role: critic. Corpus: writing. Session: decision.

Report only flaws you can demonstrate at their location, and say what is wrong with each: a stated support that does not carry its claim, a claim with no support, a tier the support does not earn.

### R1020

In current installed CLAUDE.md: no. Kind: instruction.

Role: critic. Corpus: writing. Session: decision.

Report nothing you cannot anchor to a passage: an observation with no passage is an impression, not a finding.

### R1077

In current installed CLAUDE.md: no. Kind: instruction.

Role: skeptic-risk-agent. Corpus: software, writing. Session: execution.

Flag any statement equivalent to one of these: coverage proves correctness; the fixture matches reality because it worked before; the agent says it works; no test failed so there is no issue; not tested means not risky; local dev success proves production config; type checks prove runtime behavior; unit tests prove background-worker or installed-app behavior; an SLO target is defined but no mechanism exists to verify it in production.

### R1073

In current installed CLAUDE.md: no. Kind: instruction.

Role: reviewer-agent, skeptic-risk-agent, release-manager-agent. Corpus: software, writing. Session: execution.

When reviewing implementation output, reviewing test results, preparing a release, or deciding whether the human needs to inspect something more deeply, run the pass over the evidence chain:

- inspect the request or spec, the acceptance criteria, the test plan, the implementation summary, the test results, the mocks and fixtures, the verification boundary declarations, the live and browser test evidence, the release-readiness claims, and the operational notes — and, where the change is consequential, whether a `human-gate` tracker issue is open and linked to it;
- list the claims being made;
- match each claim to the evidence for it;
- report the unsupported claims, the overbroad interpretations of test results, and the evidence missing for material risks, each carrying one of the four release-impact labels.

### R0151

In current installed CLAUDE.md: no. Kind: instruction.

Role: test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent. Corpus: software. Session: execution.

When you write or review tests, state what is verified, what is not, what is mocked, what assumptions the fixtures encode, whether live, browser, or production verification is still needed, where the verification boundary is recorded, and whether any gap blocks release.

### R0114

In current installed CLAUDE.md: no. Kind: instruction.

Role: test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent. Corpus: software. Session: execution.

Make every mock's boundary visible: what production behavior it represents, what the test verifies, what it does not verify, where the missing side is verified, and — where it is not verified — the release-impact label the gap carries and who owns the follow-up.

### R0284

In current installed CLAUDE.md: no. Kind: instruction.

Role: context-quality-reviewer. Corpus: software, writing. Session: execution.

Name what you cross-checked when you report the review.

### R1044

In current installed CLAUDE.md: no. Kind: instruction.

Role: release-manager-agent. Corpus: software, writing. Session: execution.

Where a required item of the release readiness review has no source at all, say so rather than filling the slot, and carry the missing item as a known gap.

```yaml
skill: release
```

## Definitions that clarify the overlap

### R0173

In current installed CLAUDE.md: yes. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

An assertion about state, results, verification, or completeness is a claim.

### R0175

In current installed CLAUDE.md: no. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

An assertion carrying no class label is treated as unknown.

### R0176

In current installed CLAUDE.md: no. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

A passing check proves the check, not the claim.

### R0040

In current installed CLAUDE.md: no. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

Provenance class is where an assertion came from — observed, inferred, told, unknown, the four classes Core names.

### R0038

In current installed CLAUDE.md: no. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

Claim strength is how firmly a sentence in public prose may assert — relayed, demonstrated, grounded, opinion. It is a property of the assertion, not of where the knowledge came from: claim strength and provenance class are independent axes.

### R0027

In current installed CLAUDE.md: yes. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

Unverified means known but not yet checked.

### R0189

In current installed CLAUDE.md: no. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

A tool's success response is itself a claim.

### R0780

In current installed CLAUDE.md: yes. Kind: definition.

Role: definition; pulled when referenced. Corpus: definition. Session: definition.

A verification boundary is the point where evidence stops — the line between what has been checked and what is merely assumed, mocked, deferred, or accepted as risk.

## Existing retirement and moved procedures

R0456, “Label every verification claim with its evidence class.”, was already retired into R0021 by PR #423. It is not another live candidate. Detailed verification checklists now live in process/verification-checklists.md; their confidence ledger and reporting fields apply the same principles in procedural form and are outside this root-row consolidation proposal.

## Assessment for the human

The clearest repetition is among R0111, R0783, R0461 and R0161: each limits what evidence can establish. R0110 makes the boundary explicit. R0177 and R0179 require disclosure of gaps. R0172/R0174/R0021 can be expressed together as requirements on a claim, while preserving the two labeling systems. Operational checks (read repository, inspect writes, sweep before completeness) and public-writing claim-strength labels have additional scope and should not disappear merely because the general principle is combined. No change is authorized by this assessment.
