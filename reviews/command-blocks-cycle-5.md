# Review: skills/command-blocks.md — cycle 5

Verdict: changes-required
Reviewed: skills/command-blocks.md @ 5136960
Reviewer: Context Quality Reviewer
Date: 2026-08-22
Scope: the whole file, frontmatter and body, against all eleven criteria of docs/global-context/review-rubric.md @ 5136960; cross-read against the four foundation files and against docs/global-context/decision-layer.md rule 15.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/document-metadata-policy.md — all @ 5136960.
Not inspected: whether `bin/check-frontmatter` accepts unschemaed keys (bin/ behaviour is out of scope for this cycle); the rendering behaviour of any delivery surface's copy control — the file's claims about heredocs are taken as told, not verified; skills/directive-dispatch.md, which carries the same two frontmatter fields and was reviewed in cycle 21a.
Findings: 3 blocking, 3 non-blocking, 1 observation
Prior cycle: reviews/command-blocks-cycle-4.md
Dave should inspect: CB-1 — which file is the single home for the command-block rules. CB-3 — whether `name:`/`description:` enter the metadata schema or leave the frontmatter.

Disposition (criterion 10): **retain-with-changes.** The file states the conformance criteria, the rationale behind them, and the known-instance lists, and it is the only file carrying them that reaches an execution session. What it does not do is hold them alone — see CB-1.

## CB-1 — blocking
Claim: `docs/global-context/decision-layer.md` rule 15 restates five of this file's seven conformance criteria and one of its body rules, and the two copies have already diverged.
Location: skills/command-blocks.md:78-96 and :59-64, against docs/global-context/decision-layer.md rule 15.
Evidence: verified by running `git show 5136960:docs/global-context/decision-layer.md` and comparing bullet for bullet. Pairs: verbatim-as-pasted / no manual step in the fence (criterion 2 ↔ bullet 1); cannot terminate the shell, with the identical instance list `exit`, `exec`, `logout`, `|| { …; exit; }`, `set -e` and the identical `if…elif…else…fi` remedy (criterion 6 ↔ bullet 2); safe to re-run (criterion 3 ↔ bullet 3); a step fetching state names its source and fails loudly, nothing downstream acting on an unchecked result (criterion 7 ↔ bullet 6); copyable whole in the delivering surface, with the same heredoc instance (criterion 5 ↔ bullet 7); one block per turn when a human relays output (body :59-64 ↔ bullet 8).
Consequence: criterion 4 fails outright. A decision session receives both files and the rule twice. The divergence is not hypothetical: decision-layer rule 15 carries "one purpose per block; no placeholders — an unknown value is a question asked above the block" and "expected output stated in one line below; blast radius stated above if destructive", and neither appears among the seven criteria. So a document citing "criterion 6" by ordinal — which :98-101 says is the mechanism keeping the rule in one place — is citing a list that is not the full rule set.
Fix: pick one home. This file is the sustainable one: it is `audience: [all-roles]` and so reaches execution sessions, which never receive decision-layer. Cut rule 15's sub-bullets to a one-line statement that every command block satisfies the stated conformance criteria, and append decision-layer's two orphan bullets here as criteria 8 and 9, per this file's own append rule.

## CB-2 — blocking
Claim: the `description:` field uses the retired term "sync block" and asserts a sequencing the methodology has withdrawn.
Location: skills/command-blocks.md:6.
Evidence: verified by running `git grep -n -i "sync block" 5136960` — this line is the only hit in the file. LEXICON.md @ 5136960: "**Sync block** — retired 2026-08-21. Nothing precedes the execution block; the executor fetches as its first act."
Consequence: criterion 4. The clause reads "including the sync block preceding an execution block". It names a retired construct and states that something precedes an execution block, which is exactly what the retirement denies. `description:` is selector text — the line an agent reads to decide whether this skill applies — so the retired term sits in the most-read sentence of the file.
Fix: delete the clause "including the sync block preceding an execution block". The body's "A sync or remote command names its remote and ref" (:37) is not the retired term and stays.

## CB-3 — blocking
Claim: `name:` and `description:` are not fields the frontmatter schema defines.
Location: skills/command-blocks.md:5-6.
Evidence: verified by reading `policies/document-metadata-policy.md` @ 5136960: Required fields are `status:`, `last-reviewed:`, `audience:`; the sole conditional field is `superseded-by:`. Neither `name:` nor `description:` is named anywhere in the policy. Verified by running a per-file frontmatter scan over `skills/`, `roles/`, `policies/`, `context-sets/`, `boundaries/` @ 5136960: only this file and `skills/directive-dispatch.md` carry them.
Consequence: criteria 9 and 2. Two unschemaed keys sit in an in-scope document. The policy states enforcement "checks exactly the in-scope set" and defines no behaviour for unknown keys, so these fields are neither validated nor guaranteed to survive bundling — and `description:` is where CB-2's retired term lives, in a field no gate reviews.
Fix: either remove both fields, or add them to the metadata policy's schema with stated semantics and enforcement. This is a policy edit, not a document edit; the reviewer does not choose between them.

## CB-4 — non-blocking
Claim: a vendor name appears where the repository already has vendor-neutral wording for the same fact.
Location: skills/command-blocks.md:55.
Evidence: verified by running `git grep -n -i "Claude" 5136960 -- skills/command-blocks.md` — one hit, "in the Claude desktop client". decision-layer rule 15 states the same instance as "(known: heredocs break the desktop copy control)", with no vendor.
Consequence: criterion 8. A bundle delivered to a non-Claude harness carries an instance that does not apply to it, and the neutral phrasing already exists in the repo.
Fix: "the desktop copy control", matching decision-layer rule 15.

## CB-5 — non-blocking
Claim: three passages instruct document maintainers and adopting projects, not the agent reading the file.
Location: skills/command-blocks.md:56-57, :75-76, :98-101.
Evidence: verified by reading. ":56-57" — "adopting projects should substitute their own known cases and keep the principle"; ":75-76" — "adopting projects should add the constructs their own shells terminate on"; ":98-101" — "New criteria are appended rather than slotted into body order… so the existing numbering has to hold."
Consequence: criterion 5. An agent in a bundle cannot act on any of the three. The last also carries the file's only path-shaped citation (see CB-6).
Fix: move to the repository's instruction-writing criteria; keep the criteria themselves here.

## CB-6 — non-blocking
Claim: three path-shaped references assume the reader can open another file.
Location: skills/command-blocks.md:13, :49 (`LEXICON.md`), :101 (`decisions/log.md` `DEC-000100`).
Evidence: verified by running `git grep -n -E 'LEXICON|decisions/log' 5136960 -- skills/command-blocks.md`.
Consequence: criteria 1 and 3. Line 13's citation carries load — it is what distinguishes a command block from an execution block, and the distinction is the file's opening claim. Line 101's is the sole justification offered for the numbering rule.
Fix: state the distinguishing sentence inline at :13 and drop the citation; :49's parenthetical is redundant once :13 states it; :101 goes with the passage CB-5 removes.

## CB-7 — observation
Claim: the file never states which session kind it governs.
Location: whole file.
Evidence: verified by reading — no sentence names a decision session or an execution session.
Consequence: criterion 7. Most of the file is kind-neutral, but the one-block-per-turn rule at :59-64 is decision-session shaped; it self-bounds ("does not bind a sequence an agent runs itself with no one in the loop") rather than declaring the file's kind, which leaves the reader to infer the rest.
Fix: one line stating the file governs both session kinds.
