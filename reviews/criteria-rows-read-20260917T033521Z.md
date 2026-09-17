# Review: rules/R1015.md, rules/R1171.md, decisions/log.md — criteria-rows-read-20260917T033521Z

Verdict: ready-with-findings
Reviewed: rules/R1015.md, rules/R1171.md, decisions/log.md @ 9b8f599
Baseline: rules/R1015.md, rules/R1171.md, decisions/log.md @ 8127f1e
Reviewer: frontier intake read, commissioned by docs/cycles/criteria-rows-read-20260917T033521Z.md
Date: 2026-09-16
Scope: the whole diff 8127f1e..9b8f599 over the three files, read by dimension against R0264 and R1605; the three dictated texts byte-compared against the fenced blocks in docs/cycles/criteria-rows-20260917T030541Z.md @ b9a03f1; a store-wide scan for a surviving criteria-document reference over rules/, process/ and README.md; co-rendering of [R0853] from R1015 established from the rows' own keys and bin/bundle --keys; DEC-000950 against the entry form and against every entry in force, DEC-000920 and DEC-000330 read whole; DEC-000950's claims against specs/bin-land.md §3, §7 and §8, bin/land --help, and one live invocation of bin/land under a directive that misstated its base rule.
Cross-checked: process/review-artifact.md @ 38aab41, process/decision-log.md, reviews/process-criteria-refs-read-20260910T193000Z.md, rules/R1013.md, rules/R0853.md, the 17 rows under topic public-prose-criteria (keys only), bin/rulestore/render.py, bin/rulestore/store.py, bin/aimeta/land.py, reviews/bin-land-trd-cycle-8.md (header and finding ids only), docs/cycles/bin-land-spec-7-20260823T203500Z.md @ 8a77c2a (existence and its Q3 line), docs/cycles/ grepped for earlier directives instructing a bin/land invocation
Not inspected: no bundle was rendered — bin/bundle --where refuses on this branch (observed: "refused: HEAD is not synced with origin/main"), so every reach claim below is from keys, not from rendered output; specs/bin-land.md §4–§6 and specs/bin-land-trd.md were not read beyond the lines cited; the tracker was not read — gh cannot reach the API from the sandbox — so whether the four bin-land-trd finding classes are filed there is unknown; docs/cycles and docs/history were not scanned for criteria-document references, consistent with the 2026-09-10 read's exclusion; the ## Human section of R1171 is unchanged in the diff and was not re-read against DEC-000250.
Findings: 2 non-blocking, 6 observations
The human should inspect: F2 — DEC-000950 names J1 and J2 as bin/land's usage statement, and the first directive written under that entry restated the tool's base rule wrongly and stopped the executor on it; the entry's ruling stands, but the gap Q3 predicted is now observed rather than argued. F1 — R1171 now names a class of rows the bundle reader cannot pick out, which is the prior read's F6 arriving in the store; a smaller wording exists.

The delta does what the producing directive dictated, byte for byte, and the two rows no longer name a document no bundle carries. Both non-blocking findings are about what the delta lands on, not what it changed: F1 is a wording the prior read already flagged in voice.md and the directive chose to match; F2 is the usage-statement claim in DEC-000950, tested by this session's own first landing. Nothing here wants the rows or the entry reworked before merge.

## F1 — non-blocking
Claim: R1171's "the prose-criteria rows in this bundle" names a class of rows that a Writer reading only the bundle cannot identify. R0264 criterion: readable inside a bundle with no other file open, by an agent that has never seen the repository.
Location: rules/R1171.md:14
Evidence: verified by reading bin/rulestore/render.py — render emits row.body and nothing else, no id and no topic, so the rows arrive as undifferentiated prose. Verified by keys: 16 of the 17 rows under topic public-prose-criteria carry role [writer, copy-editor, critic], so they render in the writer bundle; R0845 is a term row pulled by definition. The wording matches the Fix the 2026-09-10 read gave for F3 and the wording that read's F6 then flagged in process/voice.md:11 for exactly this reason.
Consequence: the harvest's boundary — "rules the Voice document or the prose-criteria rows do not yet state" — cannot be applied deliberately against the rows half, only by the Writer's guess at which of the rows in front of it are criteria rows. Milder than the baseline, which named a document that was not there at all; the class named now exists and is present.
Fix: the same one F6 proposed for voice.md — name the topic, "the rows under topic `public-prose-criteria` in this bundle" — landed in one delta with the voice.md fix so the two stay in step. Not a reason to hold this delta: the retirement of the document reference is complete and correct as dictated.
Related: none in this delta; reviews/process-criteria-refs-read-20260910T193000Z.md F6

## F2 — non-blocking
Claim: DEC-000950 makes specs/bin-land.md's J1 and J2 the tool's usage statement, and neither an executor's --help nor the directive form routes their content to the executor; the first directive written under the entry restated J1's base rule wrongly and the tool stopped the executor on it.
Location: decisions/log.md:895; specs/bin-land.md:85–108; bin/land --help
Evidence: verified by running. bin/land --help states the argument form and one sentence ("Commit and push onto a branch at origin, then verify the landing by reading remote state back") — nothing on base resolution, exit codes, or the report's field and stage vocabulary. J1 states the base for a first landing: "finds the named branch absent at the remote and creates it from origin/main HEAD"; bin/aimeta/land.py:145–167 implements exactly that, with no way to name another base. The commissioning directive for this read told its executor bin/land "creates criteria-rows-read at origin on the first landing" from a worktree on origin/criteria-rows; the invocation exited 3, stage guard, "[head-diverged] local HEAD carries a commit the landing base does not", with detail.base reporting origin/main's SHA 8127f1e. The executor could not tell from --help whether the directive or the tool was right and read bin/aimeta/land.py to find out. The decision session resolved it by creating origin/criteria-rows-read by hand at 9b8f599 so J2's branch-present arm applied. grep over docs/cycles confirms the two 2026-09-17 directives are the first to instruct an invocation; the two August hits describe the spec.
Consequence: DEC-000950 says "the directive that invokes it says what its report and exit status mean", which places the usage statement in each directive author's restatement. The first such restatement was wrong on the one fact J1 is explicit about, and the cost was a stop, a hand-made remote write by the decision session, and an amendment. J1 and J2 are a sufficient statement of what the tool does on its two journeys; they are not a sufficient usage statement for an executor holding only the directive and --help, because that executor holds neither of them, and --help carries none of the three things a stopped executor needs — the base rule, the exit-code map, and the stage names.
Fix: the owed process delta the producing directive defers — process/directive-invariants.md making bin/land the generated skeleton's landing step — states G1's two arms in the skeleton text so an author cannot restate them, and states that non-zero is a stop with the stage name as the diagnostic. Alternatively or additionally, a --help epilog carrying the same three facts, which is a tool change on the bin-land spec. The entry's ruling — the tool is agent-facing — is not in question; this finding is about where its usage lives.
Related: F3, F7

## F3 — observation
Claim: DEC-000950's third sentence — the four untriaged finding classes against specs/bin-land-trd.md are filed on the tracker as deferred — is unverifiable from the sandbox.
Location: decisions/log.md:895
Evidence: reviews/bin-land-trd-cycle-8.md carries B1, N1, N2 and N3 (observed, its heading list), which is four, consistent with the entry's count. Whether they are filed on GitHub Issues is unknown: gh cannot reach the API from here.
Consequence: none for the delta; recorded so the entry's claim is labelled unknown rather than passed.
Fix: the decision session confirms the issue number in the pull request.

## F4 — observation
Claim: R1015's [R0853] renders in the critic bundle as a literal bracketed ID with no row labelled R0853 to resolve it, today.
Location: rules/R1015.md:9 and :14
Evidence: verified by reading bin/rulestore/render.py — no id is emitted for any row. R1013:14 in the same bundle already cites [R0853] and [R0835, R0844, R0846, R0849] the same way, so the delta adds one instance to a class already in the critic bundle. DEC-000930 rules the fix under #358: the bundler labels the targets of citations the author marks as necessary instruction and refuses to render when a retained target is absent.
Consequence: none beyond the standing class. When #358 lands, this citation must be marked as necessary instruction rather than provenance — R1015's condition cannot be evaluated without R0853 in view.
Fix: none in this delta.

## F5 — observation
Claim: the third commit, 9b8f599, edits R1015's condition key, which the producing directive told its executor to leave unchanged and whose Decisions section limited the package to the three dictated texts; the ruling that produced it is recorded in the commit message and in this read's commissioning directive, nowhere else.
Location: rules/R1015.md:9; docs/cycles/criteria-rows-20260917T030541Z.md TASK ("changing nothing in either row's frontmatter") and Decisions
Evidence: observed from the diff and the directive at b9a03f1. The condition key is a selector, lowercased by bin/rulestore/store.py:147 and never rendered, so the bundle is unaffected either way; the 2026-09-10 read's F1 named the condition line as one of the two places to fix, and the fix is right.
Consequence: the directive at its committed SHA now disagrees with the delta it produced, and a reader reconstructing the package from the directive alone would expect two row-body edits and find a third change. No effect on the store.
Fix: none needed; noted for the decision session's practice of recording post-hoc rulings only in commit messages.

## F6 — observation
Claim: DEC-000950's Decision runs three sentences where process/decision-log.md's form says one or two.
Location: decisions/log.md:895
Evidence: observed. DEC-000920, in force, runs longer still, so the bound is not one the log enforces.
Consequence: none.
Fix: none.

## F7 — observation
Claim: specs/bin-land.md §8 still records Q3 as closed by the sequencing decision DEC-000950 withdraws.
Location: specs/bin-land.md:363–372
Evidence: observed. The producing directive's Deferred section names the one-line closure as a spec edit on a spec branch.
Consequence: none for the delta; known and deferred.
Fix: the deferred spec edit.
Related: F2

## F8 — observation
Claim: bin/bundle --keys reports R1015's condition as "you find a prose tell [r0853] does not name", lowercased.
Location: bin/rulestore/store.py:141 and :147
Evidence: observed. Every key value is lowercased on parse; R1015 is the only row carrying a bracketed citation in its condition, so it is the first time the normalization has touched a row ID.
Consequence: none — the key is a selector, not rendered, and no query selects on it by ID.
Fix: none.

Verdict (Continuity): ready-with-findings

R1015 answers F1 of the 2026-09-10 read: both the body and the condition line name [R0853] where they named "the Criteria's list", matching R1013's form for the same list (observed). R1171 answers F3: the body names "the Voice document or the prose-criteria rows in this bundle", which is F3's dictated Fix with "in this bundle" added (observed). grep -rn -i "the Criteria" over rules/, process/ and README.md at the reviewed ref returns nothing — count 0, observed in the assigned worktree; README.md carries no occurrence of "criteria" at all, so the prior read's F4 is also closed on this base. The [R0853] citation co-renders under R1605: R1015 carries role [critic], session [decision], corpus [writing], and R0853 carries role [writer, copy-editor, critic], session [decision], corpus [writing] — every value R1015 carries, R0853 carries — so R0853 reaches every bundle R1015 reaches (observed from the two files' frontmatter; bin/bundle --keys confirms critic, decision and writing are values those keys hold). Established by keys, not by rendering: bin/bundle --where refuses on this branch, and DEC-000940's removal of that refusal under #366 has not landed at this ref. DEC-000950 contradicts no entry in force: DEC-000920 and the DEC-000330 rulings it restates govern releases — regeneration whole at one SHA, event-driven cadence, the go being the human's — and bin/land lands commits on branches and is not on the release path; DEC-000940 governs bin/bundle's inputs; DEC-000690's "agent-facing corpus" is a different sense of the word. F1 is the one continuity cost: the phrase R1171 now carries reproduces the class the prior read's F6 named in voice.md.

Verdict (Quality): ready-with-findings

All three dictated texts landed byte-identical to their fenced blocks at b9a03f1 (verified by running a script that extracts the blocks and compares). R1015 and R1171 against R0264, criterion by criterion: each refers to no file by path; each carries keys unchanged from the baseline with every value in the vocabulary --keys reports; each names session [decision] and says nothing an execution session needs; neither names a model; R1015 contributes what R1013 does not — R1013 checks against R0853's list, R1015 reports what the list lacks and proposes the line; each is consistent with every rule in force and R1015's citation takes R1605's form; each states an obligation; each has one trigger stated in the body, and R1015's condition key now matches its body's trigger; neither is a negation, a ban, a form, or a merge; neither defines a term; neither states a rule a tool enforces; each is one act. The one criterion not cleanly met is the first, readability inside the bundle alone, and that is F1 for R1171 and the standing F4 class for R1015. DEC-000950 takes the form process/decision-log.md states — heading with em dash and short title, Date, Decision, Context, no Supersedes — and is numbered DEC-000950 from DEC-000940, the last entry on the base (observed). Its Context correctly says there is no entry to supersede: the withdrawn precondition lives in docs/cycles/bin-land-spec-7-20260823T203500Z.md, which exists at 8a77c2a and states it (observed), and in §8 Q3. Its claim that the producing directive is the first to invoke bin/land holds (observed by grep over docs/cycles). Its claim about the tracker is F3, unknown. F6 is the form's sentence bound, not enforced.

Verdict (Skepticism): ready-with-findings

The pre-merge boundary: bin/bundle --where refuses on a branch, so no bundle was rendered and every reach claim here is from the rows' own keys and bin/bundle --keys; DEC-000940 rules that refusal onto the release path but the change has not landed at this ref, so the boundary stands for this read. What a single-bundle reader cannot resolve after this delta: the Writer cannot pick out the prose-criteria rows R1171 names (F1), and the Critic sees [R0853] with no row so labelled (F4, the standing class). Neither is worse than the baseline, where both rows named a document that was not there. The question the directive put — whether J1 and J2 are a sufficient usage statement for an executor holding only the directive and the tool's --help — has an observed answer rather than an argued one, and it is F2: no. J1 states the base rule plainly and the directive author restated it wrongly; --help carries nothing an executor could check it against; the executor stopped correctly, as the directive's stop conditions and the tool's §7 posture both intend, and the cost was borne by the decision session, which created the branch at origin by hand — a remote write outside the tool by the session that had just ruled the tool agent-facing. That is the gap Q3 predicted and DEC-000950 withdrew the guard for, and it is a finding for triage, not a reason to hold the entry: the ruling that the tool is agent-facing survived its first use, and the tool did what its spec says.
