# Review: process/outline.md, process/voice.md — process-criteria-refs-read-20260910T193000Z

Verdict: ready-with-findings
Reviewed: process/outline.md, process/voice.md @ b3a8f00
Baseline: process/outline.md, process/voice.md @ c1bb437
Reviewer: frontier read, commissioned by docs/cycles/process-criteria-refs-read-20260910T193000Z.md
Date: 2026-09-10
Scope: the whole diff c1bb437..b3a8f00 over the two documents, read against R1604, R0821 and R1594; a store-wide and repo-wide scan for surviving references to the Public Prose Criteria as a document across process/, rules/, README.md and docs/ excluding docs/cycles and docs/history; and the rendered writer, copy-editor and critic bundles at the reviewed ref, generated through the same rulestore functions bin/bundle uses.
Cross-checked: process/named-queries.md (the release manifest), bin/bundle, bin/release, bin/rulestore/{store,query,terms,render}.py, rules/R1013, R1015, R1171, R0038, R0958, README.md
Not inspected: the nine non-writing bundles; docs/cycles and docs/history, excluded by the commission; the 62 docs/rule-register hits, read as a class from grep output rather than each file whole; git history before c1bb437; whether a release has been cut since b3a8f00.
Findings: 6 non-blocking, 2 observations
The human should inspect: F1 and F3 — two live rows that ship in the critic and writer bundles still instruct an agent against a document no bundle contains; F2 — the four claim tiers now reach all three writing roles as bare words with nothing in any bundle saying what earns which. None of the three is a defect in this delta, and all three want a follow-up delta before the next release cut.

The delta itself is correct and complete against its own dictated scope, and every finding below sits outside the two files it changed. That is why the verdict is `ready-with-findings` rather than `changes-required`: nothing in outline.md or voice.md needs rework, and the required changes are one row each in `rules/R1015.md` and `rules/R1171.md` and two table cells in `README.md`. Landing this delta and deferring those leaves the store in a strictly better state than refusing it; shipping a release with those three unfixed does not.

## F1 — non-blocking
Claim: R1015 still instructs the Critic against "the Criteria's list", a document no bundle contains, while its sibling R1013 was migrated to row references in the same pass.
Label: defect
Release impact: blocking at the next release cut — it renders in the critic bundle.
Location: rules/R1015.md:9 and :14; rendered at bundle-critic.md:79
Evidence: verified by running. `grep -rn -i "public prose criteria\|the Criteria" process/ rules/ README.md docs/ --exclude-dir=cycles --exclude-dir=history` returns R1015 twice, on the `condition:` key and in the body. R1015's keys are `role: [critic]`, `corpus: [writing]`, so the release manifest's `role=critic` query selects it; rendering the bundle at b3a8f00 puts the sentence at line 79. R1013 — the row for the same pass, whose register wording was "check the piece against every tell in the Criteria's list" — now reads "Check the piece against every tell in [R0853] and every structure defect in [R0835, R0844, R0846, R0849]". R1015 was left behind.
Consequence: a Critic reading only its bundle is told to report a tell "the Criteria's list does not name" and has no list of that name in front of it. The condition on the row is unevaluable, so the obligation cannot be discharged either way — and the reader has R1013 pointing at [R0853] for what is evidently the same list, which reads as two different authorities for one pass.
Fix: reword R1015's `condition:` and body to name [R0853] as R1013 already does, in a one-row delta.
Related: F3

## F2 — non-blocking
Claim: after edit 2, the four claim tiers reach the Writer, Copy Editor and Critic as four bare words, with no row in any of the three bundles stating what evidence earns which tier and no definition pulled.
Label: defect
Release impact: blocking at the next release cut — it affects all three writing bundles.
Location: process/outline.md:28–29; rules/R0821.md:14; rules/R0038.md
Evidence: verified by running. The only rows in `rules/` containing the tier names are R0821 and R0038. R0821 enumerates and requires signalling — "Signal each claim's tier in the sentence: relayed, demonstrated, grounded, or opinion" — and defines nothing. R0038 defines the term "claim strength" as "how firmly a sentence in public prose may assert — relayed, demonstrated, grounded, opinion", and stops short of per-tier criteria. R0038 is a definition row (`term: [claim strength]`, no `role`/`session`/`corpus`), so `terms.pull_definitions` pulls it only where a selected row's body contains the term; `grep -c -i "claim strength"` over the three rendered bundles returns 0, 0, 0. Neither document nor any selected row uses the term, so R0038 does not render in any writing bundle.
Consequence: outline.md's next clause tells the Writer to "give a claim the tier the author's evidence earns", and nothing in the bundle says what any tier means or what earns it. Before the delta the phrase "from the Criteria's claims taxonomy" at least told the reader the four words were a defined taxonomy with an origin to ask for; the landed text removes that acknowledgement without supplying the semantics, so the gap is now silent rather than signposted. Two agents will assign tiers differently and neither is checkable.
Fix: two candidates, both cheap. Either state the tiers in outline.md and R0821 as the governed term — "carrying its claim strength" — so R0038 is pulled into all three bundles by term and the enumeration acquires a definition; or land a row under topic `public-prose-criteria` stating what evidence earns each of the four. The first is the smaller change and uses the mechanism as designed.

## F3 — non-blocking
Claim: R1171 still instructs the Writer to harvest rules "the Voice document or the Criteria do not yet state", naming a document no bundle contains.
Label: defect
Release impact: blocking at the next release cut — it renders in the writer bundle.
Location: rules/R1171.md:14; rendered at bundle-writer.md:71
Evidence: verified by running. The same repo-wide grep returns R1171 once. Its keys are `role: [writer]`, `corpus: [writing]`, so `role=writer` selects it; rendering the bundle at b3a8f00 puts the sentence at line 71.
Consequence: milder than F1, because the Writer can still harvest against the Voice document and against the prose-criteria rows in front of it, and the harvest is a proposal the author files rather than a gate. But the row names a second authority the session cannot see, so the Writer either treats "the Criteria" as the rows — a guess the row does not license — or under-harvests against an authority it cannot read.
Fix: reword to "the Voice document or the prose-criteria rows", matching the wording this delta put into voice.md:11.
Related: F1

## F4 — non-blocking
Claim: README.md's role table describes the Copy Editor and the Critic as working against "the public prose criteria" and "the criteria", as a standing authority, and README ships as an asset of every release.
Label: defect
Release impact: blocking at the next release cut — README.md is attached to every release alongside the bundles.
Location: README.md:44 and :45
Evidence: verified by running. The repo-wide grep returns both lines. `bin/release` builds its asset list as `assets = [readme]` plus one file per bundle, so README.md is published with every tag; `process/named-queries.md` § Releasing states the same. `git ls-tree -r b3a8f00 -- process/` confirms no `process/public-prose-criteria.md` exists at the reviewed ref, and the § Sequence block's process-document list names no such stem.
Consequence: README is the document a reader consults to choose a bundle. It promises the Copy Editor and Critic bundles govern prose against criteria that, on opening either bundle, are not there under that name — the first thing a new adopter checks is the first thing that does not hold.
Fix: reword both cells to describe the criteria as rows, in the same follow-up delta as F1 and F3. The lowercase phrasing makes this the smallest of the three edits.

## F5 — non-blocking
Claim: edit 2's re-wrap left a 50-column orphan line mid-paragraph instead of reflowing to the file's wrap width, which the directive dictated.
Label: defect
Release impact: none — the rendered text is unchanged in meaning.
Location: process/outline.md:29
Evidence: verified by running. Measured column widths across outline.md: the file wraps at 72–83 columns, and every other line of that list item runs 74–79. Line 29, "   the tier the author's evidence earns; where you", is 50. The words on line 30 would fit. The directive's TASK says "Re-wrap only the lines the edit touches, to the file's existing wrap width"; lines 28–29 were re-wrapped, line 30 onward was not reflowed, so the paragraph did not close up. voice.md's re-wrap, by contrast, is clean — lines 11 and 12 are 73 and 80 columns.
Consequence: cosmetic in the rendered bundle, and a nuisance to the next delta over this paragraph, which will produce a diff hunk wider than its own edit because the ragged line has to be absorbed.
Fix: reflow lines 28–33 to the file's width in the next delta that touches this paragraph; not worth a delta of its own.

## F6 — non-blocking
Claim: edit 3 makes "a criteria row" the left-hand side of the precedence rule, and a bundle reader has no way to tell which of the rows in front of it are criteria rows.
Label: suggestion
Release impact: deferred.
Location: process/voice.md:11–12
Evidence: verified by reading `bin/rulestore/render.py`. `render` emits `row.body` and nothing else — no id, no topic, no key of any kind — so the rows arrive as undifferentiated prose. voice.md:14, two lines below, already handles the same problem for the other direction by naming the key: "rows in the store under topic `voice`". Seventeen rows carry `topic: [public-prose-criteria]` — R0817–R0821, R0829–R0833, R0835, R0844–R0846, R0849, R0853, R0854 — and the new sentence names no such handle.
Consequence: the reader knows this document wins over a criteria row and cannot identify one, so the precedence rule cannot be applied deliberately — only by accident, when a conflict is obvious on its face. This is not the known bracketed-row-ID defect: no row is cited here, and adding one would not help; what is missing is the name of a class.
Fix: name the topic as line 14 does — "Where a row under topic `public-prose-criteria` and this document speak to the same thing, this document wins." It is strictly more informative than the landed sentence at the same length, and it uses a convention the paragraph already establishes.

## F7 — observation
Claim: voice.md's Mechanics section rests on "the base authority", which resolves in the copy-editor bundle and in neither of the other two.
Label: accepted risk
Release impact: none from this delta — the text is unchanged from the baseline.
Location: process/voice.md:59–60
Evidence: verified by running. R0958 supplies the referent — "the Google developer documentation style guide is the Copy Editor's base authority where the Voice document is silent" — and carries `role: [copy-editor]`. `grep -c "Google developer documentation"` over the three rendered bundles returns 2 for copy-editor and 0 for writer and critic. The delta did not touch these lines; the diff over voice.md is confined to lines 11–12 and 55.
Consequence: a Writer or Critic reads that house-style deltas are applied "over its base authority" and that "the base authority governs" where the section is silent, without being told what that authority is. It is a pre-existing gap that the Criteria's retirement did not create and this delta did not widen, recorded here because the Skepticism pass asked what a single-bundle reader cannot resolve.

## F8 — observation
Claim: the remaining 63 repo-wide hits are records and provenance, and none of them reaches a bundle.
Label: accepted risk
Release impact: none.
Location: docs/rule-register/ (62 hits), docs/research/methodology-scan-phase2-findings.md:898 (1 hit); `source:` frontmatter on the 17 rows under topic `public-prose-criteria`
Evidence: verified by running. The repo-wide grep returns 68 hits: 3 in rules/ (F1, F3), 2 in README.md (F4), 1 in docs/research/, 62 in docs/rule-register/. The docs/rule-register hits are dated register, cluster and near-sweep artifacts quoting pre-store source text as it stood at fd54448 — the same class of record as docs/cycles and docs/history, which the commission excluded. The docs/research hit is an unrelated generic use of the word. Separately, all 17 rows under topic `public-prose-criteria` carry `source: public-prose-criteria.md:NN @ fd54448`; that is provenance pinned at a revision where the document did exist, and `render.py` emits no frontmatter, so `grep -rn "public-prose-criteria" ` over the three rendered bundles returns nothing.
Consequence: none. Recorded so the 68-hit count in the run log is not mistaken for 68 live references.

Verdict (Continuity): ready-with-findings

Each retired phrase's meaning survives into the same bundles as the two documents, verified by rendering rather than by reading keys. outline.md and voice.md both carry `role: [writer, copy-editor, critic]`, `session: [decision]`, `corpus: [writing]`; R1604, R0821 and R1594 carry byte-identical `role`, `session` and `corpus` values. The release manifest defines each bundle as `role=<slug>` "and nothing more", so identical role keys are sufficient for co-rendering, and `session` and `corpus` are not selectors here. Rendering all three bundles at b3a8f00 confirms it: R1604's "Read the Voice document before you write, edit, or read the piece, every time" at writer:193, copy-editor:255, critic:223; R0821's tier enumeration at writer:151, copy-editor:213, critic:181; R1594's "Use the methodology's own governed vocabulary, and define each term at first use" at writer:187, copy-editor:249, critic:217 — each alongside "# Process: Outline" and "# Process: Voice — Dave" in the same file. The read-first instruction survives in the half that still has a referent: R1604 carries the Voice document, and the criteria half has nothing left to read first, since rows are read as part of the bundle by construction. The precedence obligation and the define-at-first-use obligation survive whole.

What does not hold is the scan the pass also asked for. Three live places the delta did not change still name the Criteria as a document — R1015 and R1171 in the store, README.md in the release assets — and two of the three render into the very bundles the delta was making consistent. That is unfinished business from the retirement in #343 rather than a defect this delta introduced, and it is the reason this pass does not read clean.

Verdict (Quality): ready-with-findings

All four dictated edits landed, none of them altered, and nothing else in either file changed. Edit 1's sentence is gone and the paragraph rejoined with a single space and no stray break. Edit 2's replacement matches the dictation exactly once list indentation is normalized. Edits 3 and 4 match the dictated text byte for byte. `git diff --stat c1bb437..b3a8f00` names three files — the directive and the two documents — and the second commit touches only the two. Neither file carries a trailing space or an internal double space. The re-wrap is clean in voice.md and not in outline.md, which is F5. The precedence sentence still says what it said: the baseline's "where the two speak to the same thing, this document wins" becomes "Where a criteria row and this document speak to the same thing, this document wins" — the same direction, with the losing side narrowed from a document to a row, which is what the retirement requires. The clause the edit dropped, "Read with the Criteria", was dictated for deletion and is not a change of meaning, since there is no longer a document to read alongside.

Verdict (Skepticism): ready-with-findings

One thing in the two documents is genuinely worse moored than before, and it is F2: the tier names. The delta left an enumeration with no semantics anywhere in the bundle and removed the phrase that told the reader a taxonomy existed. F6 is the other side of the same coin and lighter — "a criteria row" now points at something real and present, which is an improvement on pointing at a document that does not exist, but the reader still cannot pick one out. Everything else in the two documents resolves inside a single bundle: the four tier names are at least enumerated in-document and in R0821; "the Voice document", which outline.md:41 also relies on, renders in all three bundles; "claims-tier audit" and "Skeptic pass" name work the Copy Editor's and Critic's own rows describe. "The base authority" (F7) is unresolvable for two of the three roles and was equally unresolvable before this delta.
