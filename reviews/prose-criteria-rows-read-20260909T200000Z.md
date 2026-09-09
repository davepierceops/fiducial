# Review: rules delta 28dfdb0..8cd16fe (branch prose-criteria-rows) — prose-criteria-rows-read-20260909T200000Z

Verdict: changes-required
Reviewed: prose-criteria-rows @ 8cd16fed025e264f91fcb7c8fc03cc19b2495cd8
Baseline: main @ 28dfdb0560cafcda026c70cd1c7697751b3eac26
Reviewer: Context Quality Reviewer — execution session, sandboxed, worktree `fiducial-prose-criteria-rows-read` on branch `prose-criteria-rows-read`
Date: 2026-09-09
Scope: the whole diff 28dfdb0..8cd16fe — eight files: two directive files under `docs/cycles/`, one row added (R1604), three deleted (R1161, R0953, R1001), two modified (R1013, R0038). Read by dimension, not by file. Store-wide sweeps for near-duplicates, dangling citations, key reach, ID allocation, and order collisions were run over all 454 rows at the reviewed ref and all 456 at the baseline. I did not produce this delta.
Cross-checked: process/review-artifact.md @ 8cd16fe; docs/cycles/prose-criteria-rows-20260909T190000Z.md @ ca9fd54 and its amendment A @ 69e720b; R0264, R0266, R0284, R0944, R0950 (the intake criteria); R1603 (frontmatter convention); the seventeen `public-prose-criteria` rows; the ten `voice`-topic rows; the eight other rows naming the Voice document; process/voice.md and process/outline.md @ 8cd16fe; bin/bundle and bin/rulestore/query.py @ 8cd16fe.
Not inspected: the rendered role bundles. `bin/bundle --where` refuses on any branch — observed, it exits with `refused: HEAD is not synced with origin/main` — so no bundle for writer, copy-editor, or critic is checkable before this branch merges. Reach below is established from `bin/bundle --keys` and from the rows' own frontmatter keys read against the selection rule in `bin/rulestore/query.py`, not from a rendered bundle. Also not inspected: whether Dave intends the coverage change F-1 describes; that is his ruling, not a reviewer's finding to resolve.
Findings: 1 blocking, 2 non-blocking, 6 observations
The human should inspect: F-1 — R1013's re-citation narrows the Critic's structural reporting duty from a section of criteria to a single row, and cites a row whose own second sentence withholds structure from the defect set. Amendment A ruled the ID; it did not rule that R0844, R0845, R0846, and R0849 are not structure defects. That distinction needs your word before merge.

## Pass: Continuity

Verdict (continuity): changes-required

**Near-duplicate shortlist for R1604 (observed).** Against all 454 rows at the reviewed ref, three sweeps: the nine rows whose body names the Voice document (R1171, R0959, R0958, R1168, R1017, R0982, R1016, R0960, and R1604 itself); the ten rows carrying `topic: [voice]`; and a store-wide sweep for read-first phrasing. The eight surviving Voice-document rows are all apply/flag/propose obligations that treat the Voice document as an authority at a decision point — none instructs a role to read it before starting. The nine other `voice`-topic rows are substantive register obligations. The read-first sweep returned one unrelated row, R1007 (pass ordering). R0181 ("Read the repository before asserting its state") is a different subject. **R1604 restates no surviving row** — R0264's "contributes something no rule already in its bundles does" is satisfied.

**No role loses the read-first rule it had (observed).** R1161 bound `role: [writer]`, R0953 `role: [copy-editor]`, R1001 `role: [critic]`; each was single-role. R1604 carries `role: [writer, copy-editor, critic]` — exact coverage, no role added and none dropped. `session: [decision]` and `corpus: [writing]` are unchanged from all three. Reach measured at both refs by counting rows carrying each role value in `rules/`: writer 104 → 104, copy-editor 135 → 135, critic 119 → 119. Each role loses one row and gains one. Row total 456 → 454, consistent with three deletions and one addition. Evidence class: unverified against a rendered bundle, established from frontmatter keys and the selection rule; see `Not inspected`.

**R0853 and R0835 hold what R1013 now cites them for — R0853 yes, R0835 only in part.** R0853 is the tells list: seven named AI prose-smell tells, and R1013's "every tell in [R0853]" is exact. R0835 is where the citation does not hold; see F-1.

**R0821 holds what R0038 now cites it for (observed).** R0821 reads "Signal each claim's tier in the sentence: relayed, demonstrated, grounded, or opinion." It names all four tiers, in the order R0038 names them. The substitution is accurate. Its reachability is a separate matter; see F-2.

**Both edited rows kept byte-identical frontmatter (observed).** `git diff 28dfdb0..8cd16fe -- rules/R1013.md rules/R0038.md` touches one body line in each and nothing above the closing `---`, as the producing directive's execution note required.

**ID and order allocation are clean (observed).** R1603 was the highest ID at the baseline; R1604 is highest-plus-one, and `rules/R1604.md` was absent at 28dfdb0. Order 240 is the tail of the `voice` topic (previous maximum 230, R1600) with no collision anywhere in the topic. Frontmatter key set and key order match R1603 exactly. Filename matches the `id:` field for all 454 rows.

## F-1 — blocking
Claim: R1013 cites R0835 as the container of "every structure defect", but R0835 states one defect and its second sentence withholds structure from the defect set, and the re-citation drops the structural criteria the superseded wording reached.
Location: rules/R1013.md:14, against rules/R0835.md:14
Evidence: Read both rows at 8cd16fe and R1013 at 28dfdb0. The superseded body read "against its structure defects" — plural, denoting a section of the Public Prose Criteria. The new body reads "every structure defect in [R0835]". R0835 in full: "Say each point once; cut restatements. Length and structure are the author's call per piece." That is one defect, restatement, followed by an explicit disclaimer that structure is not the reviewer's call. Enumerating the seventeen `public-prose-criteria` rows at 8cd16fe by order shows four further rows that answer to "structure defect": R0844 (land every piece clean for a cold reader), R0845 (a declared series states which part of how many), R0846 (place key terms early, keep the structure skimmable), R0849 (venue-independent prose, no platform-specific formatting dependencies). R0846 names structure in so many words. Verified by reading, not by running; no tool in the store resolves a bracketed citation.
Consequence: R0264 requires that where two rules disagree the disagreement is raised as a defect and left unresolved — R1013 calls R0835 the home of structure defects while R0835 says structure is the author's call, and a Critic following R1013 to R0835 lands on a row that partly contradicts the sentence that sent it. Concretely, the duty R1013 uniquely carries — "report each occurrence at its location" — now reaches restatement and nothing else structural. A piece that is unskimmable (R0846) or does not land for a cold reader (R0844) still violates a standing `require` the Critic holds, but no longer earns the location-level report R1013 mandates. The Critic's structural findings silently lose four criteria's worth of reach.
Fix: put the disagreement to the decision session, and do not resolve it here. It needs a ruling on which rows constitute the structure defects R1013 enumerates — R0835 alone, or R0835 with R0844, R0845, R0846, R0849 — and, separately, on whether R0835's second sentence belongs in a row cited as a defect container. Amendment A ruled "structure defects R0835" when settling step 1's IDs; it did not rule the four other rows out, and this reviewer will not read that ruling as covering them.
Related: F-3

## F-2 — non-blocking
Claim: The `[R0821]` citation added to R0038 cannot resolve in any bundle R0038 can appear in, because the two rows share no key-value pair by which one selection could return both.
Location: rules/R0038.md:11
Evidence: R0038 carries only `topic: [lexicon]`, `order`, `verb`, `condition`, `source`, `term: [claim strength]` — no `role`, `session`, or `corpus` key. R0821 carries `topic: [public-prose-criteria]`, `role: [writer, copy-editor, critic]`, `session: [decision]`, `corpus: [writing]`. `select()` in bin/rulestore/query.py returns "exactly the rows where every named key's list contains the value", and a row missing the queried key never matches, so no `--where` selection returns both rows. Read from the source at 8cd16fe; not run, because `--where` refuses on a branch. Thirty-four of the forty-eight `lexicon` rows likewise carry no `role` key, so R0038 is not anomalous — the disjunction is structural.
Consequence: R0038 remains readable and applicable on its own, because it already lists all four tiers inline — "relayed, demonstrated, grounded, opinion" — so comprehension never depends on reaching R0821. What fails is the rationale D-2 gave for the change: the old wording pointed at a document the reader could not locate in a bundle, and the new wording points at a row the reader also cannot locate in a bundle. The reference is provenance dressed as a citation, and it reads to an agent as a pointer it is expected to follow and cannot.
Fix: two options for the decision session, neither taken here — drop the bracketed ID and leave the inline list of tiers to carry the sentence, or give R0038 the keys that would co-select it with R0821. The second changes what bundles R0038 renders in and is the larger change.
Related: F-3

## Pass: Quality

Verdict (quality): ready-with-findings

Tested the three changed rows against every criterion in R0264, citing the failed criterion per R0266.

**R1604 passes fifteen of sixteen criteria (observed).** Readable in a bundle with no other file open — "the Voice document" is the phrase eight surviving rows already use, and process/voice.md renders in all three role bundles. Refers to no file by path. Every key value it carries already exists in the store. Names its session kind. Speaks no model name. Contributes what no surviving row does. States an obligation rather than describing. Defines no term. Is a row, not a document's form. Is not a rule a tool enforces. And, on the criterion that governs a merge — "if it merges other rows, it states the rule at its shortest, not the sum of its sources" — it is genuinely shorter than any of its three sources, having dropped the Public Prose Criteria clause rather than carrying it forward. The sixteenth criterion is O-6.

**R1013 and R0038 are edits to rows already in force**, so the intake criteria bite on the changed body only. R1013's new body satisfies "readable inside a bundle with no other file open": R1013 binds `role: [critic]`, and both cited rows carry critic in their role list, so any selection that returns R1013 returns R0853 and R0835 too. Its defect is F-1, against the "consistent with every rule in force" criterion. R0038's defect is F-2, against the same readable-in-a-bundle criterion, mitigated by the inline tier list.

**Supplementary, not a step this directive names:** `bin/tests/run` at 8cd16fe in the assigned worktree returned `OK (skipped=7)`, 511 tests, exit 0, in 130s. One `ResourceWarning` from `bin/tests/test_check_directive.py:943` (an unclosed file handle) is pre-existing test hygiene, unrelated to this delta. Reported as evidence, not as a gate.

## F-3 — non-blocking
Claim: This delta introduces bracketed row-ID citation into rule bodies, a convention with no precedent among rules rows and no tooling that validates it, and the same delta demonstrates the failure mode by hand-sweeping for the three IDs it retired.
Location: rules/R1013.md:14 and rules/R0038.md:11
Evidence: Swept every rules row at both refs for a `[Rnnnn]` citation in the body. At 28dfdb0: zero. At 8cd16fe: exactly two, R1013 and R0038, both created by this delta. The convention does exist for process documents — nine files under `process/` use it, including process/review-artifact.md, which cites [R1395a, R1396, R1408] and [R1414] — so this delta extends an established documentary convention into the rule store for the first time. No test in `bin/tests/run` resolves a bracketed ID; the producing directive's step 5 was a manual `grep` sweep for R1161, R0953, and R1001, and its step 7 relied on that sweep rather than on a check. Verified by reading the store and the test run's output; the absence of a validating test is inferred from the suite passing while no such check exists to fail.
Consequence: a row cited by ID can be retired, renumbered, or rewritten with nothing to catch the dangling reference. This delta retired three rows and had to sweep by hand to prove nothing still cited them — that sweep is clean today (zero hits across `rules/` and `process/`), but the next retirement has no such directive behind it, and a Critic's bundle would then carry R1013 pointing at an ID that resolves to nothing. The store just acquired two edges in a reference graph it does not track.
Fix: propose to the decision session that the convention be either declared and checked — a test asserting every `[Rnnnn]` in a rule body resolves to an existing row, and where the citing row carries selector keys, that the cited row is co-selectable — or confined to process documents, where the nine existing uses already live. Not resolved here; R0166 leaves the ruling to the human.
Related: F-1, F-2

## Pass: Skepticism

Verdict (skepticism): ready

No finding. What follows is the boundary on what this read could verify, stated because `Not inspected` is a claim and not a default.

**The verification claim I cannot make (observed).** `bin/bundle --where role=writer --name writer --out "$TMPDIR"` exits with `refused: HEAD is not synced with origin/main` in the assigned worktree, and will do so on any branch — bin/bundle documents the refusal at line 14 as exit 2, one line on stderr, nothing written. The producing session ran that same command before its work merged; it could only have done so from a tree synced to origin/main, which this branch is not. So the three rendered role bundles are not checkable pre-merge, and no claim in this artifact rests on one. Reach is established instead from `bin/bundle --keys` and from the rows' own frontmatter read against `select()` in bin/rulestore/query.py. That is a weaker instrument in one specific way: it confirms which rows a selection returns, not how the rendered bundle orders or presents them, which is where O-4 would show up if it matters.

**Where I looked for a reason to doubt the delta and found none (observed).** The three retirements leave no citation behind — zero hits for R1161, R0953, or R1001 across `rules/` and `process/`. No order collides in the `voice` topic. No filename disagrees with its `id:`. The ID is highest-plus-one and was absent at the baseline. Both edited rows kept frontmatter byte-identical. The file count, 8, matches the delta's shape exactly: two directive files, one addition, three deletions, two modifications. The delta does what its directive and amendment told it to do; F-1 is a defect in what it was told, not in the telling's execution.

## O-1 — observation
Claim: process/outline.md:12 carries a fourth read-first instruction, naming the Public Prose Criteria as a document to read.
Location: process/outline.md:12 — "Read the Public Prose Criteria and the Voice document in this bundle first."
Evidence: read at 8cd16fe. Told: this directive states it is known, out of this delta's scope, and belongs to a process delta already tracked.
Consequence: recorded as directed, not raised against this delta.
Fix: none here — the tracked process delta.

## O-2 — observation
Claim: process/voice.md:11 names the Criteria as a document.
Location: process/voice.md:11-12 — "The author the Public Prose Criteria in this bundle are applied to. Read with the Criteria; where the two speak to the same thing, this document wins."
Evidence: read at 8cd16fe. Told: known and out of scope, per this directive.
Consequence: recorded as directed, not raised against this delta.
Fix: none here — the tracked process delta.

## O-3 — observation
Claim: process/outline.md carries a third instance of the same pattern, at line 30, which this directive did not name.
Location: process/outline.md:30 — "carrying its tier from the Criteria's claims taxonomy — relayed, demonstrated, grounded, opinion."
Evidence: observed while reading process/outline.md whole at 8cd16fe. This directive names outline.md:12 and voice.md:11 as the known instances; line 30 is a third, and it is the one that overlaps this delta's subject most directly — it names the same four tiers R0038 and R0821 name, and attributes them to the Criteria as a document rather than to R0821.
Consequence: whoever takes the tracked process delta will find three sites in these two files, not two. Line 30 also duplicates the tier list a third time in the store, alongside R0821 and R0038.
Fix: add process/outline.md:30 to the loose-end tracker's entry for the process delta.

## O-4 — observation
Claim: the read-first instruction moves from the head of each role's own topic to the tail of the voice topic.
Location: rules/R1604.md:3-4, against rules/R1161.md:3-4, rules/R0953.md:3-4, rules/R1001.md:3-4 @ 28dfdb0
Evidence: the retired rows sat at `topic: [writer]` order 20, `topic: [copy-editor]` order 30, and `topic: [critic]` order 20 — at or near the head of each role's own topic, where a "before you do anything" rule belongs. R1604 sits at `topic: [voice]` order 240, the tail. Amendment A ruled this explicitly: "Order in the voice topic is 240 — tail append. The gap at 20 is not filled." Observed; the ruling is told.
Consequence: cannot be stated concretely, which is why this is an observation and not a finding — `sort_key` in bin/rulestore/query.py orders by band, then topic position in the sequence list, then order, then id, and the rendered bundles are not checkable pre-merge, so whether a role reads its read-first instruction near the front or near the back of its bundle is not something this read could determine. The gap at writer order 20 is now unfilled, as ruled.
Fix: none proposed; the placement is ruled. Worth a look once the branch merges and `bin/bundle --where` will run.

## O-5 — observation
Claim: R1604's `source` value uses a form only two other rows in the store use, and differs from both of those.
Location: rules/R1604.md:9
Evidence: 451 of 454 rows at 8cd16fe write `source` with a seven-character short SHA; three use a full forty-character SHA — R1601 and R1602, both `docs/cycles/store-fix-5-20260906T090000Z.md:1 @ 3e9331e…`, and R1604. R1601 and R1602 carry a `:1` line component; R1604 carries none. Amendment A dictated the exact value, full SHA and no line number, while also saying "in the same form R1603 writes its source value" — and R1603 writes a short SHA with a line number. The delta followed the dictated literal, which is the right precedence.
Consequence: three source values in the store now disagree on the form for a cycle-sourced row — short versus full SHA, and line component present versus absent. Nothing breaks; the values are all resolvable by hand.
Fix: none here. If the store wants one form for rows born from a directive, that is a convention question for the decision session.

## O-6 — observation
Claim: R1604's trigger is disjunctive across three roles, which sits awkwardly against R0264's "one trigger" and "fire together as one act" criteria.
Location: rules/R1604.md:8 and :13 — `condition: before you write, edit, or read the piece`
Evidence: R0264 requires that a row "has one trigger, stated in the body", and that it "is one checklist row where the rows fire together as one act, and separate rows where they fire independently". The Writer writing, the Copy Editor editing, and the Critic reading are three acts by three roles at three times; they do not fire together. The three superseded rows each carried a single role and a single trigger. Observed by reading R0264 against R1604.
Consequence: cannot be stated concretely — each role encounters exactly one of the three verbs as its own, so the row fires once per role per piece and reads unambiguously in practice. That is why this is an observation. It is recorded because D-1's merge is precisely the case R0264's last criterion speaks to, and a later reader may ask why the criteria did not bite.
Fix: none proposed. The merge is ruled (D-1) and the row satisfies the merge criterion that matters most — it states the rule at its shortest.
