# Review: engagements/sre/implementer.md — cycle 1

Verdict: changes-required
Reviewed: engagements/sre/implementer.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 37 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — produced by directive at 0e07753 (cycle 25), never rubric-reviewed. One of the seven-file `engagements/sre/` set.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, roles/coder-agent.md, and the other six files of the `engagements/sre/` set — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether "Terraform or equivalent" is the right technology framing — the baton records it as a deliberate engagement-shape retention and this review does not re-open it.
Findings: 2 — 2 blocking
Prior cycle: none
Dave should inspect: SRE-IMP-1. It is the sharpest thing this re-gate found, and closing it is an `audience:` decision.

## SRE-IMP-1 — blocking
Claim: The `implementer` bundle contains the rule that everything is overridable and does not contain the rule that says what is not.
Location: engagements/sre/implementer.md:4 (`audience: [implementer, assistant, human]`) — the defect is what the bundle this file anchors does not contain. Colliding text: engagements/sre/override-log-policy.md:13-15 against engagements/working-with-dave.md:33-36.
Evidence: Verified by running — the `implementer` bundle resolves to 23 files at 8402c23. It contains engagements/sre/override-log-policy.md, which states "Every ceremonial element of this engagement pack — the baseline-gate, the change-package shape, any procedural step — is trivially overridable by Dave" and whose Exclusions section bounds that only with "An agent does not waive its own stop-and-ask by its own judgment." It does not contain engagements/working-with-dave.md, whose `audience:` is `[assistant, cartographer, skeptic, human]` and which carries the corpus's only rule marked "not negotiable, not overridable": "You have zero write access to the client's cloud and systems." The `implementer` role was created at 0e07753; working-with-dave.md was last reviewed at cb3e75a, before it existed. Criterion 11, criterion 1.
Consequence: The Implementer is the engagement role that writes code and lands changes. Its bundle tells it that every procedural element of the pack is trivially overridable on Dave's word, and never tells it that write access to the client's systems is outside the overridable set. This file's own constraint — "applies are executed by humans or the client's own CI" — is a statement about who runs applies, not a prohibition on the agent acquiring write access, and it sits under a "Constraints" heading in a pack whose override policy declares constraints overridable.
Fix: Add `implementer` to engagements/working-with-dave.md's `audience:`. Whichever way the guardrail reaches the bundle, engagements/sre/override-log-policy.md should name it as outside the overridable set, since that file is where the override protocol is read.
Related: WD-1, SRE-OLP-1

## SRE-IMP-2 — blocking
Claim: Two of the three preconditions and one responsibility turn on the System Map, which is defined in a file absent from this file's bundle.
Location: engagements/sre/implementer.md:29-31 ("surface anything discovered mid-implementation that contradicts the System Map — that is a map correction; escalate before proceeding")
Evidence: Verified by running — "System Map" is defined only in engagements/sre/system-discovery.md (its Procedure and Output sections), whose `audience:` is `[cartographer, assistant, human]`. That file is absent from the 23-file `implementer` bundle. engagements/sre/README.md, which is in the bundle, names the System Map in the artifact chain but does not say what it is, where it lives, or what form a correction takes. Criterion 1.
Consequence: The Implementer is given an escalation trigger — contradiction with the System Map — for an artifact its bundle never describes. Criterion 11 makes an escalation trigger the agent must resolve by inference a defect, and this one cannot be resolved at all: the agent cannot know what would count as a contradiction.
Fix: Add `implementer` to engagements/sre/system-discovery.md's `audience:`, or state the map's shape and location in engagements/sre/README.md, which every engagement bundle receives.
Related: SRE-SD-2
