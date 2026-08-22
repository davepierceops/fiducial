# Review: vendors/README.md — cycle 4

Verdict: changes-required
Reviewed: vendors/README.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 55 lines, against all eleven criteria of the review rubric @ 1bbd5b7. Includes verification of every factual claim the file makes about other files in the repository.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, policies/document-metadata-policy.md, vendors/claude-code/environment-config.md, docs/batons/baton-20260822T153848.md — all @ 1bbd5b7; plus the existence of README.md and docs/cycles/doc-review-2026-08-02-directive.md at 1bbd5b7, and the object type of commit `ef4438b`.
Not inspected: the pre-commit hook's actual behaviour (asserted by this file, not run here); the content of the 2026-08-02 doc-review directive beyond confirming the file exists; anything under `vendors/claude-code/` other than environment-config.md, which is reviewed separately this cycle.
Findings: 9 — 5 blocking, 3 non-blocking, 1 observation
Prior cycle: none. `reviews/README-cycle-1.md` through `-cycle-3.md` review the repository-root `README.md`, a different document, now retired. See the filename note below.
Dave should inspect: RM-1 (the disposition — this file is largely repo history and enforcement narrative, not agent context) and RM-3 (where the vendor swap test should live).

## Filename note

The artifact naming rule in skills/review-artifact.md @ 1bbd5b7 is mechanical:
`reviews/<stem>-cycle-<n>.md`, stem being the basename without extension. Two
different documents in this repository have the basename `README`. Applying the
rule unchanged gives `README-cycle-4.md` for this file, continuing a sequence
whose first three entries review a document that has since been retired. The
rule was applied as written; this note is the disambiguation, since the path
alone no longer identifies which README was reviewed. The naming rule is not in
this cycle's scope and no finding is raised against it here.

## Criterion 10 first

**Disposition: merge-into `operating-model.md` (the vendor swap test), then
retire the remainder.**

The file has four parts and only one of them survives the question.

1. **The directory convention** (one directory per vendor). Repo mechanics. No
   agent reading a bundle acts on it. The baton @ 1bbd5b7 settles that agents
   receive `bin/bundle <audience>` output and never the repository, and that
   harnesses are adapters downstream of bundles — so a file explaining how the
   repository's directories are laid out has no bundle reader.
2. **The what-belongs / what-does-not split, and the swap test.** This is
   **methodology policy**, and the directive is right to ask whether it is in
   the wrong place. It is. See RM-3.
3. **The lifecycle section.** A narrative about a policy edit made at a
   particular commit. History.
4. **"Status of this draft."** History, and duplicative of frontmatter.

So the file *states methodology policy* rather than describing an adapter's
environment — the first half of the directive's vendor question, answered
against this file: **policy, not environment.** Policy lives in governed
documents.

**Proposed `audience:`** — none, because the file does not survive. If Dave
elects to keep a bare directory-convention note for himself, it is `[human]`
and nothing else; `[all-roles, human]` is wrong under any disposition.

## RM-1 — blocking
Claim: the file states methodology policy — where operating principles must live and where vendor mechanics must live — in a location that is neither a governed policy nor a bundle any agent receives.
Location: vendors/README.md:14–32 ("What belongs here" / "What does not" / the test)
Evidence: verified by reading the baton @ 1bbd5b7, "What this session settled": "Files are sources; agents receive `bin/bundle <audience>` output, never the repo. Harnesses are adapters downstream of bundles." Verified by reading operating-model.md @ 1bbd5b7, whose Agents "Must not" list already carries the rule this section is the operative test for.
Consequence: the rule that decides whether a sentence is policy or vendor mechanics is itself stored as vendor documentation. Nothing enforces it, no agent reads it, and it is the one rule whose misplacement is self-demonstrating.
Fix: move the swap test to operating-model.md (RM-3) and retire the section here.

## RM-2 — blocking
Claim: the file quotes operating-model.md for a sentence operating-model.md does not contain.
Location: vendors/README.md:26–28 — "The split follows `operating-model.md`: \"Tool-specific files may adapt these rules but should not be the sole location of durable policy\""
Evidence: verified by running `git show 1bbd5b7:operating-model.md | grep -nE 'Tool-specific|sole location|durable policy|vendor-specific'`. The only match is line 98: "store durable policy only in vendor-specific tooling", a bullet in the Agents "Must not" list. The quoted sentence does not appear anywhere in the file.
Consequence: a quotation attributed to a governed document that does not say it. A reader who trusts the quotation carries a rule ("tool-specific files *may adapt* these rules") that the operating model does not grant — it forbids vendor tooling as the *sole* location, and says nothing about adapting. The permission is invented by the quotation.
Fix: delete the quotation. If the rule is needed, state operating-model's actual bullet, or — better — rely on it and say nothing here.
Related: EC-2, which is the same fabricated quotation in vendors/claude-code/environment-config.md.

## RM-3 — blocking
Claim: the vendor swap test is a general methodology rule stored in a vendor directory, where it governs nothing.
Location: vendors/README.md:31–32 — "The test: if swapping vendors would delete the sentence, it belongs here. If swapping vendors would leave it true, it belongs in the core doc set."
Evidence: verified by reading operating-model.md @ 1bbd5b7 line 98, which states the rule ("store durable policy only in vendor-specific tooling" — a Must-not for agents) but not the test that applies it. Verified by reading LEXICON.md and core.md @ 1bbd5b7: neither carries a placement test.
Consequence: the operating model forbids the outcome but gives no way to decide a borderline sentence. The decision procedure exists, and it is filed where only someone already inside `vendors/` will find it — which is precisely the person who has already decided.
Fix: **the test belongs in `operating-model.md`, appended to the Agents "Must not" bullet on line 98 as the one sentence that makes it operable** — "A sentence that would be deleted by swapping vendors is vendor mechanics; a sentence that would still be true is durable policy." That bullet is already in the `[all-roles, human]` bundle, which is exactly the reach the test needs, and putting it there gives the rule and its test one home. It does not belong in Core (not universal to every session), in LEXICON (a test, not a definition), or in the decision layer (execution sessions need it too).

## RM-4 — blocking
Claim: the file cites "README principle #7" — a numbered principle in a document that no longer exists.
Location: vendors/README.md:28–29 — "and README principle #7: \"Vendor-specific agent systems are implementation details, not the source of truth.\""
Evidence: verified by running `git cat-file -e 1bbd5b7:README.md`, which reports the path absent. Verified by reading the baton @ 1bbd5b7: "README retired; rewritten human-only in Pass 2 once `bin/bundle` exists."
Consequence: a governed document cites a deleted file for a numbered principle. The citation cannot be checked, the principle has no current home, and a Pass 2 README rewrite will not restore a principle numbered 7.
Fix: delete the citation. The rule it points at is the operating-model bullet already discussed in RM-2.

## RM-5 — blocking
Claim: five references are unresolvable by any reader who does not hold the repository and its history — four paths and a bare commit SHA, plus three opaque work-item identifiers.
Location: vendors/README.md:12 (`vendors/claude-code/`), :26 (`operating-model.md`), :36 (`policies/document-metadata-policy.md`), :37 (`ef4438b`), :54 (`docs/cycles/doc-review-2026-08-02-directive.md`, plus "W3.2"), :47 and :55 ("Q1b" twice)
Evidence: verified by running a path sweep over the file. `ef4438b` verified to be a real commit by running `git cat-file -t ef4438b`; `docs/cycles/doc-review-2026-08-02-directive.md` verified present at 1bbd5b7. The claim at line 36 that `policies/document-metadata-policy.md` lists `vendors/**` in its in-scope set was verified true at 1bbd5b7 by reading the policy's in-scope list.
Consequence: the facts are accurate and unusable. "Q1b", "W3.2", and "the W2 findings" name work items from a session in August 2026 that no reader outside that session can decode, and the SHA citation asks a bundle reader to check out a commit.
Fix: retire the sections carrying them (RM-6, RM-7). None of these references survives the disposition.

## RM-6 — non-blocking
Claim: the "Lifecycle" section is a narrative about a past policy edit, not an instruction.
Location: vendors/README.md:34–49
Evidence: verified by reading. The section reports that a policy edit happened, why it was one line rather than a migration, and which half of a question it answers.
Consequence: rationale where the rubric asks for instructions (criterion 6), and history that becomes wrong the moment the policy's in-scope list changes. It also states a rule — that documents here are enforced on the same terms as everywhere else — which the policy itself states, so the copy can go stale against its source.
Fix: delete the section. The enforceable fact (that `vendors/**` is in the frontmatter scope) lives in the metadata policy, where the hook reads it.

## RM-7 — non-blocking
Claim: "Status of this draft" duplicates the frontmatter and dates the file.
Location: vendors/README.md:51–55
Evidence: verified by reading; the frontmatter at lines 1–5 already carries `status: draft`, and "Nothing here is agreed" is what `status: draft` means under policies/document-metadata-policy.md @ 1bbd5b7.
Consequence: two statements of the same status, one of which the pre-commit hook checks and one of which nothing checks. When the document is agreed, the prose is stale and the frontmatter is right.
Fix: delete the section.
Related: EC-6.

## RM-8 — non-blocking
Claim: `audience: [all-roles, human]` selects repo-directory mechanics into every agent's bundle.
Location: vendors/README.md:4
Evidence: verified by reading the frontmatter against the baton's settled rule @ 1bbd5b7 that agents receive bundle output and never the repository.
Consequence: every agent in the methodology carries a note about how this repository's directories are laid out, which no agent can act on and which contradicts the fact that the agent is not looking at a repository.
Fix: the file does not survive criterion 10. Under any interim state, `[human]`.

## RM-9 — observation
Claim: the file names one vendor, and that vendor is the subject of the directory it documents.
Location: vendors/README.md:12 (`vendors/claude-code/`)
Evidence: verified by running a vendor and model name sweep over the file. No second vendor name and no model name appears.
Consequence: none. Recorded because the cycle directive requires the vendor-name sweep to be reported for files under `vendors/`, where the vendor's own name is licensed and a second vendor or a model name would be a defect. Neither is present.
Fix: none.

## Note on a directive/LEXICON tension

The directive for this cycle states that every use of *dispatch*, *sync block*,
*track*, and *prompt* is a criterion-4 finding. LEXICON @ 1bbd5b7 states two
explicit carve-outs: *track/tracking/tracker* in the ordinary record-keeping
sense, and *prompt* meaning a tool's approval interrupt. Core rule 9 says two
sources that disagree are surfaced, not resolved by picking one. Uses covered by
a carve-out are recorded here as observations, not defects, and are counted
separately in the sweep. This note appears in all eight artifacts of this cycle.
No use of any retired term occurs in this file.

## Sweep counts

- Rules restated from the foundation: **1** (RM-2 — and it is restated wrongly; the quotation is not in the source)
- Output-shape lists with a home elsewhere: **0**
- Path-shaped references: **4** (lines 12, 26, 36, 54), plus one bare commit SHA (line 37) and three opaque work-item identifiers (Q1b ×2, W3.2)
- Vendor and model names: **0** beyond the directory's own subject (RM-9)
- Retired terms: **0**
- SLO / Top K copies: **0**
