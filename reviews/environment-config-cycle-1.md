# Review: vendors/claude-code/environment-config.md — cycle 1

Verdict: changes-required
Reviewed: vendors/claude-code/environment-config.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 141 lines, against all eleven criteria of the review rubric @ 1bbd5b7. Includes verification of every factual claim the file makes about `.claude/settings.json`, `operating-model.md`, and `policies/document-metadata-policy.md`.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, policies/document-metadata-policy.md, vendors/README.md, docs/batons/baton-20260822T153848.md — all @ 1bbd5b7; plus the actual content of `.claude/settings.json` @ 1bbd5b7.
Not inspected: `.claude/settings.local.json` (untracked; the file's claim about it cannot be checked from the repository and is left unverified); `policies/project-setup-requirements.md` beyond confirming it is in the remaining Pass 1 scope; whether the described sandbox and allowlist settings are correct as tool configuration (that is engineering judgment about a vendor's product, ceded per the role); whether branch protection is actually configured on the remote.
Findings: 10 — 5 blocking, 4 non-blocking, 1 observation
Prior cycle: none
Dave should inspect: EC-1 (the Divergence section is now factually wrong about the committed file, and the file's whole argument rests on it) and EC-4 (the gating principle still has no home in the governed set, which the file itself admits).

## Criterion 10 first

**Disposition: retain-with-changes, `audience: [human]`.**

The directive's question for a vendor file is whether it describes an adapter's
environment or states methodology policy. This file does **both**, and the two
halves take opposite answers.

**The environment half — retained.** The settings strings are exactly what a
vendor directory is for: the shape of one tool's settings file, the exact
permission strings that tool understands, the interaction between two of its
settings. No agent reading a bundle acts on it — the baton @ 1bbd5b7 settles
that harnesses are adapters downstream of bundles and no harness reads the repo
— so its reader is Dave, configuring a clone. That is a real reader, and
`human` is a real audience with 61 files already selecting it.

**The policy half — a finding.** "Gate only on actual human judgment" is a
methodology principle, and the file says so itself: it belongs in the core doc
set and "does not currently have a home there." A vendor file that knows it is
carrying homeless policy is the vendor-tooling failure mode the operating model
names. See EC-4.

**Proposed `audience:` — `[human]`.** Not `[all-roles, human]`: no agent
receiving a bundle can act on a settings string for a runner it is not
necessarily running under, and the strings are noise in every role bundle.

## EC-1 — blocking
Claim: the "Divergence from the committed file" section describes a `.claude/settings.json` that no longer exists; it is wrong on the two points its own argument turns on.
Location: vendors/claude-code/environment-config.md:99–115
Evidence: verified by running `git show 1bbd5b7:.claude/settings.json`. The committed file at 1bbd5b7 contains a `permissions.deny` array only — five `git push --force`/`-f` patterns, `Bash(rm -rf *)`, `Read(.env)`, `Read(~/.ssh/**)`. It contains **no `defaultMode` key** and **no `ask` array**. The document asserts both: `"defaultMode": "acceptEdits"` and `"ask": ["Bash(git push *)"]`, and then states as one of its five divergence points that "`git push` is **asked, not allowed**".
Consequence: the document's central argument — the Push section at lines 68–90, which argues at length that the approval prompt on `git push` should be removed — is presented as an unimplemented target when the prompt is in fact already gone from the committed file. A reader following this document would set out to change something that has already changed, and would trust a JSON block that misrepresents the repository. Two of the five listed divergences are false; the other three (no sandbox block, no `allowUnsandboxedCommands`, no `~/.aws/credentials` deny, no notification hook) are true.
Fix: re-derive the section against the committed file, or delete it. A section whose whole content is "how the repo differs from this document today" is a standing invitation to this defect — it is state, and Decision Layer rule 9 says state is computed, not maintained. Deleting it and letting the reader diff the file is the stronger fix.

## EC-2 — blocking
Claim: the file quotes operating-model.md for a sentence operating-model.md does not contain.
Location: vendors/claude-code/environment-config.md:128–130 — "subject to `operating-model.md`'s rule that tool-specific files \"should not be the sole location of durable policy.\""
Evidence: verified by running `git show 1bbd5b7:operating-model.md | grep -nE 'Tool-specific|sole location|durable policy|vendor-specific'`. The only match is line 98: "store durable policy only in vendor-specific tooling", a bullet in the Agents "Must not" list. The quoted phrase does not appear.
Consequence: the same fabricated quotation as in vendors/README.md, in a second file — so a reader who checks one against the other finds them consistent and concludes the quotation is real. The invented wording is also weaker than the source: "should not be the sole location" reads as guidance, where the operating model states a Must-not.
Fix: delete the quotation; cite nothing and let the rule live in operating-model.md.
Related: RM-2.

## EC-3 — blocking
Claim: the file states a methodology principle — the gating principle — as its own content.
Location: vendors/claude-code/environment-config.md:16–22 ("The principle this implements: Gate only on actual human judgment… Prompts are spent on judgment; structure carries everything else.")
Evidence: verified by reading core.md, decision-layer.md, LEXICON.md, operating-model.md, and engagements/working-with-dave.md @ 1bbd5b7. None of the five states this principle or anything equivalent. The file itself confirms it at lines 132–134: "the *principle* … belongs in the core doc set and does not currently have a home there."
Consequence: a principle that governs how every gate in the methodology is designed exists only in a vendor configuration document, selected into no role bundle. That is the failure mode operating-model.md line 98 forbids — durable policy whose only location is vendor tooling — and the document is self-aware about committing it.
Fix: canonicalize the principle in a governed document, then cut lines 16–22 to a bare pointer-free sentence or nothing. This is a change to a foundation file, not to this one, so it is Dave's sequencing call; the finding stands here because this cycle is where it was verified.
Related: EC-4.

## EC-4 — blocking
Claim: the file's own scope-boundary section states an unresolved defect and leaves it unresolved with no escalation trigger and no owner.
Location: vendors/claude-code/environment-config.md:125–135 ("So: the *principle* … does not currently have a home there — see the W2 findings. … This document is not a substitute for canonicalizing the principle.")
Evidence: verified by reading. The section names a gap, names no owner, names no condition under which it is resolved, and points at "the W2 findings" — an identifier that resolves to nothing in the repository.
Consequence: criterion 11. The document knows a rule is misplaced and hands the reader no way to act on it. An agent reading this cannot tell whether canonicalizing the principle is its job, and a human reading it cannot tell what "W2" is. The gap has been standing since 2026-08-02.
Fix: raise it as a loose end with a named next step, and delete the paragraph. If the principle is canonicalized (EC-3), the section reduces to one sentence: the settings strings live here.
Related: EC-3.

## EC-5 — blocking
Claim: the file carries a second vendor's name.
Location: vendors/claude-code/environment-config.md:52, :112 (`~/.aws/credentials`)
Evidence: verified by running a vendor and model name sweep over the file. `claude-code` and "Claude Code" are the directory's own subject and are licensed; `aws` is a second vendor.
Consequence: under the cycle directive's rule for files inside `vendors/`, a second vendor name is a defect. Recorded honestly, the mitigation is real: this is a literal string in a deny list, and a deny list that does not name the file it denies cannot be executed. So the defect is not "AWS is mentioned" but "a cloud-credential deny list is stated as three examples in the vendor file for one runner" — the list is durable policy about which credentials an agent may never read, and it is filed as vendor mechanics.
Fix: state the rule in the governed set — Core rule 1 already says secret values never enter context; what is missing is that the credential *paths* are denied structurally. Keep only the concrete strings here, as an instance of that rule, and mark them as a working set rather than a policy.

## EC-6 — non-blocking
Claim: "Status of this draft" duplicates the frontmatter and dates the file.
Location: vendors/claude-code/environment-config.md:137–141
Evidence: verified by reading; the frontmatter at lines 1–5 carries `status: draft`, and "Nothing here is agreed" is what that value means under policies/document-metadata-policy.md @ 1bbd5b7.
Consequence: two statements of status, one checked by the pre-commit hook and one checked by nobody. On agreement, the prose is stale.
Fix: delete the section.
Related: RM-7.

## EC-7 — non-blocking
Claim: four path-shaped references and three opaque work-item identifiers assume a reader who holds the repository and its August 2026 session history.
Location: vendors/claude-code/environment-config.md:82 (`policies/project-setup-requirements.md`), :128 (`policies/document-metadata-policy.md`), :129 (`operating-model.md`), :140 (`docs/cycles/doc-review-2026-08-02-directive.md`); identifiers "Q1a/D1" (line 74), "W2 findings" (line 133), "Q1b" (line 141)
Evidence: verified by running a path sweep. The directive file was verified present at 1bbd5b7 by running `git cat-file -e`. Settings-file paths (`.claude/settings.json`, `~/.ssh/**`, `.env`) are excluded from this count — they are the subject matter, not cross-references.
Consequence: the paths are resolvable by Dave in a clone, which is this file's audience, so the cost is lower here than in an agent-facing file. The three identifiers are not resolvable by anyone: they name work items from one session and appear at the exact points where the document defers a decision.
Fix: keep the policy paths if the audience is `[human]`; replace the three identifiers with what they decided, or delete the clauses containing them.

## EC-8 — non-blocking
Claim: `audience: [all-roles, human]` selects one runner's settings strings into every agent's bundle.
Location: vendors/claude-code/environment-config.md:4
Evidence: verified by reading the frontmatter against the baton @ 1bbd5b7: "Harnesses are adapters downstream of bundles" and agents "receive `bin/bundle <audience>` output, never the repo."
Consequence: every role bundle carries 141 lines about configuring a tool the agent is not necessarily running under and could not reconfigure if it were.
Fix: `audience: [human]`.

## EC-9 — non-blocking
Claim: the Push and Sandbox sections argue for their rules at length where the rubric asks for the rule.
Location: vendors/claude-code/environment-config.md:32–45, :76–84
Evidence: verified by reading; criterion 6 cuts trailing justifications and "never X" restatements. Lines 76–80 are four sentences arguing that a reflex-clicked gate is not a gate, after the rule has already been stated at line 74.
Consequence: criterion 6. Lower weight than elsewhere, because the audience is `[human]` and the argument records why a security posture was chosen — which is worth keeping somewhere. But it is rationale, and it triples the length of two sections.
Fix: keep one sentence of reasoning per setting where the reasoning constrains a future change (the `autoAllowBashIfSandboxed` / `allowUnsandboxedCommands` pairing genuinely does, and should stay); cut the rest.

## EC-10 — observation
Claim: eight uses of **prompt** appear, all in the sense LEXICON carves out.
Location: vendors/claude-code/environment-config.md:21, :22, :34 (×2), :55, :76, :77, :84, :95
Evidence: verified by running a term sweep, then verified by reading LEXICON.md @ 1bbd5b7, "Retired terms": "*Not covered by this retirement:* an approval **prompt** — a tool interrupting to ask a human to authorise a step. That is a different word in a different domain, and it keeps its ordinary meaning." Every use here is that sense.
Consequence: none. Recorded because the cycle directive instructs that every use be flagged; on LEXICON's current text all eight are licensed, and this file is the clearest case for the carve-out existing at all.
Fix: none.

## Note on a directive/LEXICON tension

The directive for this cycle states that every use of *dispatch*, *sync block*,
*track*, and *prompt* is a criterion-4 finding. LEXICON @ 1bbd5b7 states two
explicit carve-outs: *track/tracking/tracker* in the ordinary record-keeping
sense, and *prompt* meaning a tool's approval interrupt. Core rule 9 says two
sources that disagree are surfaced, not resolved by picking one. Uses covered by
a carve-out are recorded here as observations, not defects, and are counted
separately in the sweep. This note appears in all eight artifacts of this cycle.

## Sweep counts

- Rules restated from the foundation: **1** (EC-2 — restated wrongly; the quotation is not in the source). Separately, one rule is stated here that the foundation does **not** carry at all (EC-3), which is the inverse defect.
- Output-shape lists with a home elsewhere: **0**
- Path-shaped references: **4** (lines 82, 128, 129, 140), plus three opaque work-item identifiers (Q1a/D1, W2, Q1b). Settings-file paths excluded as subject matter.
- Vendor and model names: **1** second vendor (AWS, lines 52 and 112). No model name. "Claude Code" is the subject and is licensed.
- Retired terms: **0 defects**, 8 carve-out uses recorded (EC-10)
- SLO / Top K copies: **0**
