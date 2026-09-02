# Review: specs/bundle-system.md — cycle 1

Verdict: changes-required
Reviewed: specs/bundle-system.md @ cf3b87e08cf6257ee09c7066a3a53ed2adafcd15
Reviewer: Spec Reviewer Agent (execution session; independent — authored nothing under review)
Date: 2026-09-02
Scope: full-depth gate review of the PRD against specs/prd-template.md @ 39b04d90e87267d260ee925ed3d5e3b3ccfd1f67 and the role's PRD obligations; continuity scan of every claim the PRD makes about the present tool and corpus, checked by running bin/bundle --list and bin/bundle --audience for writer, chief-of-staff, all-roles, copy-editor, and critic in the assigned worktree at 068bb00 (main 6790702 plus the directive file), and again in a snapshot of main 6e77040 extracted with git archive; the decision-log entries the PRD cites read at decisions/log.md @ 1ffe27a75428416a4bb3388cc144ad2fcc8c0276; R-1's three sites verified; the OQ-5, OQ-6, OQ-10 resolutions checked against AC-BS-2, AC-BS-4, and AC-BS-9.
Cross-checked: decisions/log.md @ 1ffe27a (DEC-000200, DEC-000210, DEC-000260, DEC-000280, DEC-000290, DEC-000320, DEC-000330, DEC-000340); bin/bundle at 6790702 (unchanged since 6e77040, observed by git diff); the frontmatter of every file AC-BS-4 and AC-BS-10 name, of skills/conversation-retro.md, and of every file under engagements/; docs/global-context/review-rubric.md criterion 10; docs/global-context/decision-layer.md rule 9; docs/global-context/core.md rule 14; OPEN-ITEMS.md (rule-register record at line 1262; the deleted-adapter entry at line 1138); retros/retro-synthesis-20260831T163000.md "Follow-ups — bundle-system PRD inputs"; reviews/directive-authoring-cycle-3.md S-1; policies/source-of-truth-policy.md "Adapter discipline"; bin/check-directive (the directive lint AC-BS-12 names).
Not inspected: no TRD exists for this PRD (observed: specs/ holds none), so the role's "consistent with the TRD" check has no object; the four writing bundles hand-built on 2026-08-30 at 40a8914 are on Dave's disk, not in the tree, so the claim that they follow the tool's header is not checked; the retros' individual asks ("two ask for the stamp; six ask for regeneration") are checked only against the synthesis and a grep, not by reading each retro; word counts are approximate (wc -w over the emitted bundle); the tool's tests under bin/tests were not run; nothing under docs/rule-register/ was re-read beyond its existence and the 878 count.
Findings: 1 blocking, 8 non-blocking, 6 observations
Dave should inspect: B-1 (which of the two `critic` role documents keeps the audience value `critic`, or whether the value splits); N-1 (whether `all-decision-roles`, which the tool already selects on, is part of the PRD's selection model or something the tagging package removes); N-3 (the header's generation-time form).

## B-1 — blocking
Claim: The audience value `critic` names two governed role documents — roles/critic.md (the writing Critic, `session: decision`) and engagements/critic.md (the SRE engagement's critic, `session: execution`) — and six further engagement files plus skills/review-artifact.md carry `critic` in their `audience:`, so AC-BS-4's five-file critic set is not reachable by tagging under G5, and the PRD neither states the collision nor names who resolves it.
Location: specs/bundle-system.md:336-343 (AC-BS-4 critic set and "no other file"); :160-164 (G5); :421-423 (OQ-3, "The tool already reads `engagements/`").
Evidence: verified by running. bin/bundle --list at 068bb00 emits `critic` once (observed). bin/bundle --audience critic emits 28 files at 068bb00 and 28 at the 6e77040 snapshot (observed), against copy-editor's 21; the seven extra members are engagements/working-with-dave.md, engagements/critic.md, engagements/sre/README.md, engagements/sre/engagement-change-package.md, engagements/sre/override-log-policy.md, engagements/sre/speed-audit.md, and skills/review-artifact.md, every one tagged `critic` (observed by reading their frontmatter). bin/bundle's local_role_slugs takes the slug from both roles/ and engagements/, and _role_document_path resolves `critic` to roles/critic.md first, so the writing Critic's `session: decision` is what the value inherits (observed by reading bin/bundle:136-169). The PRD's only mention of engagements/ is OQ-3's note that the tool reads it (observed).
Consequence: Delivery step 2 (Tag) cannot make step 3's "exactly the ruled writing sets" true for `critic` by tagging alone: removing `critic` from the seven files strips the SRE engagement's own critic of its bundle, and leaving them makes the first release (G8, AC-BS-9, the "first exposure" §7 gates) ship a writer-facing Critic bundle carrying SRE engagement policy and a review-artifact schema the writing Critic never uses. Either way a decision is taken in a package that the PRD says takes none, and the TRD (OQ-7) cannot choose a selection mechanism without knowing whether audience values are unique per role.
Fix: State the collision in §5's baseline (the corpus holds two `critic` role documents; the value is shared) and add an OQ, or a ruling, naming the resolution and its resolver — one role's audience value renamed (the engagement's value namespaced, or the writing Critic's changed), or audience values scoped by directory — and note in AC-BS-4 that "no other file" is met only once that resolution lands. A proposal, clearly labelled as one: rename the engagement's value, since DEC-000230 fixed `critic` as the writing role's one-word activation.
Related: N-1 (the same file, roles/critic.md, is the decision role whose session kind pulls `all-decision-roles` files into the writing bundles).

## N-1 — non-blocking
Claim: The PRD describes present selection as "by `audience:` alone" and never names `all-decision-roles`, a reserved audience value the tool already selects on through the role document's `session:` field; that mechanism, not the `all-roles` floor, is what carries the Decision Layer and the retro skill into every writing bundle at main today.
Location: specs/bundle-system.md:21-22 (§1), :243-252 (§5 "Selection by `audience:` alone over-selects"), :339-343 (AC-BS-4 exclusion of "the retro skill"), :413-417 (OQ-1, "Session kind is already a role property").
Evidence: verified by running and by reading. bin/bundle:32 reserves `all-roles`, `all-decision-roles`, `human`; is_member (bin/bundle:183-192) admits a file tagged `all-decision-roles` when the audience value names a role whose `session:` is `decision` (observed). roles/writer.md, roles/copy-editor.md, and roles/critic.md are all `session: decision` (observed). docs/global-context/decision-layer.md is `[all-decision-roles, human]` and skills/conversation-retro.md is `[all-decision-roles, human]` at 6790702, having been `[all-roles, human]` at 6e77040 (observed by git diff 6e77040 6790702); the writer bundle is 22 files at both revisions while the `all-roles` set fell from 17 to 16, the difference being exactly conversation-retro's re-tag (observed in the bundle log).
Consequence: The tagging package cannot drop the retro skill from the writing bundles by retagging that one file to an explicit role list without also deciding the fate of the reserved value for every other decision role; and OQ-8's "in, by ruling" for the Decision Layer is today enforced by the same mechanism, so a change to it silently changes a ruled set. OQ-1 asks whether audience is roles or conditions as if session kind were not yet a selection input, when it already is.
Fix: §5's baseline names the two selection inputs the tool has (literal audience values and `all-decision-roles` via `session:`), OQ-1 states that the second exists and asks whether it stays, and AC-BS-3/AC-BS-4 say whether the writing sets are reached with or without it.
Related: B-1.

## N-2 — non-blocking
Claim: The measurement mechanism §5 names for bundle size, `bin/bundle --audience <value> --list`, does not exist: `--list` takes precedence over `--audience` and prints the audience-value list, exit 0.
Location: specs/bundle-system.md:284-285.
Evidence: verified by running. bin/bundle --audience writer --list at 068bb00 printed the eighteen audience values and exited 0 (bundle log, last region); bin/bundle:306-310 dispatches on `--list` before `--audience` (observed). No goal or AC asks for a member-listing mode.
Consequence: The stated observation for the headline outcome, run at a package's landing, succeeds and returns the wrong thing; a verifier following the PRD literally records a count that was never produced. The file count is in fact observable today from the header's numbered list, which the PRD does not say.
Fix: Either name the header's numbered member list as the observation, or add the member-listing mode as a requirement (G1 or AC-BS-1) and keep the sentence.

## N-3 — non-blocking
Claim: The generation time the header carries is unspecified in form; the present tool writes local wall-clock time with no zone, and the PRD applies DEC-000290 (UTC, `Z` required) to the filename only.
Location: specs/bundle-system.md:316-323 (AC-BS-2, "keeps the tool's present fields"); :351-354 (AC-BS-7, "the generation time bounds the claim"); :69-72 (J2).
Evidence: verified by running. The writer bundle at 068bb00 opens `- Generated: 2026-09-02 05:27` (observed; the sandbox's local time), produced by datetime.now() with no timezone at bin/bundle:226 (observed). DEC-000290 makes a generated timestamp repo-wide `<YYYYMMDD>T<HHMMSS>Z` (observed in the log).
Consequence: A consumer without repository access, which J2 and AC-BS-7 say bounds its knowledge by the generation time, cannot compare that bound to anything without knowing the generating machine's zone; two bundles generated on Dave's Mac and in a sandbox state times that are not comparable. AC-BS-7's "nothing a consumer would have to recompute to trust" is not met by the field it inherits.
Fix: AC-BS-2 states the Generated value's form — per DEC-000290 is the ruled repo-wide form — or states why the header keeps a different one.

## N-4 — non-blocking
Claim: J1 says the tool "syncs or refuses on an unsynced tree"; G1 and AC-BS-1 say it refuses.
Location: specs/bundle-system.md:54-55 (J1); :150 (G1); :314-315 (AC-BS-1).
Evidence: inferred by reading. The three sentences are quoted above; the present tool does neither — bin/bundle makes no fetch or status check before rendering (observed by reading bin/bundle whole).
Consequence: A test derived from AC-BS-1 (non-zero exit, nothing written, on an unsynced tree) is contradicted by a tool that syncs first and then emits; the Test Designer cannot tell which the PRD wants, and §7's "refusal over emission" argues for one.
Fix: J1 reads "refuses on an unsynced tree" — or, if syncing is wanted, G1 and AC-BS-1 admit it and say what "unsynced" then means.

## N-5 — non-blocking
Claim: OQ-5 says the filename and delivery directory are stated in "§2, §4, and §6"; §2 states neither — the first site is J1 in §3.
Location: specs/bundle-system.md:428-429.
Evidence: verified by reading. grep for DEC-000200 and the filename form in the PRD hits lines 56-57 (§3 J1), 149-150 (§4 G1), and 312-313 (§6 AC-BS-1) and nothing in §2 (lines 28-45) (observed).
Consequence: The one sentence written to point at the three sites points a reader verifying R-1 at the wrong section.
Fix: "§3, §4, and §6".

## N-6 — non-blocking
Claim: OQ-5 says a log entry superseding DEC-000210's naming clause is "owed to the decision log at the next flush"; that entry, DEC-000320, landed the same evening, and OQ-6 and OQ-10 likewise carry no reference to their entries DEC-000330 and DEC-000340.
Location: specs/bundle-system.md:433-434 (OQ-5); :435-449 (OQ-6); :466-468 (OQ-10).
Evidence: verified by reading. decisions/log.md @ 1ffe27a carries DEC-000320, DEC-000330, DEC-000340, each dated 2026-09-01 and each citing the PRD's OQ by number (observed); commit 1ffe27a is dated 2026-09-01 21:08 -0700, three hours after cf3b87e (observed by git log). The PRD's only DEC citations are DEC-000200, DEC-000210, DEC-000290 (observed by grep).
Consequence: The PRD states as owed a thing that exists, and the three resolutions trace to the log only in the log's direction; a reader of the PRD alone cannot find the entries that make the resolutions decisions rather than notes.
Fix: OQ-5, OQ-6, OQ-10 each cite their entry; the "owed" sentence goes.

## N-7 — non-blocking
Claim: AC-BS-9's first sentence, "one bundle per audience the release carries", admits a release carrying a subset of audiences; its third sentence, the OQ-6 resolution, requires every audience.
Location: specs/bundle-system.md:359-364.
Evidence: inferred by reading. OQ-6 (lines 435-438) and DEC-000330 both say "every audience's bundle, regenerated whole" (observed).
Consequence: A test derived from sentence one accepts a partial release that sentence three and DEC-000330 forbid; the phrase is a residue of the pre-resolution wording.
Fix: Drop "the release carries", or fold the two sentences into one.

## N-8 — non-blocking
Claim: The "Regeneration cost" outcome gives as its baseline "a hand procedure with a heredoc-free block, run from a clone root", which DEC-000210 retired on 2026-08-25, six days before the baseline revision 6e77040; the same section says the tool emits 22 files at that revision.
Location: specs/bundle-system.md:292-294.
Evidence: verified by reading. DEC-000210 (dated 2026-08-25) states "There is no hand-maintained spine and no hand-run generation procedure" (observed); bin/bundle at 6e77040 accepts --audience and --out DIR and writes `bundle-<audience>-<stamp>.md` there (observed in the snapshot run and by reading bin/bundle:281-297).
Consequence: Baseline and target measure different things: "one command, one directory" is already true of the present tool, which takes any directory; the real gap — the ruled name and directory, and the refusal on an unsynced tree — is not what this outcome observes, and "the retros that stop mentioning it" cannot observe a procedure that already stopped.
Fix: Baseline: `bin/bundle --audience <v> --out <dir>`, writing `bundle-<v>-<stamp>.md` to whatever directory is named, with no sync check. Target: the ruled name in the ruled directory, refused when unsynced.

## O-1 — observation
Claim: The functional goals run G10, G12, G11 in that order.
Location: specs/bundle-system.md:182-196.
Evidence: verified by reading.
Consequence: None concrete; AC-BS-11 and AC-BS-12 pair with G10 and G11 correctly.
Fix: Renumber or reorder.

## O-2 — observation
Claim: AC-BS-14 cites G9 for a clause covering adopting projects; G9 is writer completeness, and adopting-project reach is G10.
Location: specs/bundle-system.md:384-386.
Evidence: verified by reading.
Consequence: A wrong pointer in a criterion the audit will read closely.
Fix: "(G9, G10)".

## O-3 — observation
Claim: Two historical figures in §5 are looser than the record: "the one adapter that existed" was two files (CLAUDE.md and AGENTS.md, deleted together in PR #224; the ten-rules finding was against CLAUDE.md), and the stale bundle behind reviews/directive-authoring-cycle-3.md S-1 was generated 2026-08-09 and cited 2026-08-24, fifteen days, not "three weeks".
Location: specs/bundle-system.md:257-258, :275-276.
Evidence: verified by reading OPEN-ITEMS.md:1138-1145, the merge commit ed46f40 and its two parents, DEC-000190's context, and S-1.
Consequence: None to the requirements; both figures support the same conclusion. The 878-rule count and the "about 70 lines" net (OPEN-ITEMS.md:1262) and the 22 / 33 / 17 / about 15,000-word baselines all check exactly at 6e77040 (observed in the snapshot: writer 22 files, 15,205 words; chief-of-staff 33; `all-roles` 17); the six-file writer set is 3,704 words at 6e77040 (observed by wc -w), and OQ-8's "about 570" for the Decision Layer is 574 there (observed).
Fix: "two adapters" and "two weeks", or leave as is.

## O-4 — observation
Claim: AC-BS-4's ordering (role document third) is not what the present tags produce for copy-editor and critic: roles/copy-editor.md and roles/critic.md carry no `order:`, so they sort after the Criteria (order 11) and Voice (order 12).
Location: specs/bundle-system.md:328-338.
Evidence: verified by running. The copy-editor bundle at 068bb00 places roles/copy-editor.md at position 19 of 21, after public-prose-criteria.md (8) and voice.md (9); roles/writer.md carries `order: 10` and sorts third (observed).
Consequence: None for the PRD; the tagging package must add `order:` to both role files, which J4's "where load position matters, `order:`" already implies.
Fix: None required; noted so the tagging package's directive carries it.

## O-5 — observation
Claim: The PRD's frontmatter audience is `[human]`, matching every other spec in specs/ and its own AC-BS-5 (no spec in the floor), while the template's skeleton says `[all-roles, human]`.
Location: specs/bundle-system.md:4; specs/prd-template.md:98.
Evidence: verified by reading the frontmatter of the five other files in specs/.
Consequence: None for this document; a PRD that copied the skeleton literally would join every bundle, which AC-BS-5 forbids. The template is not under review here.
Fix: None here; a template cycle could align the skeleton.

## O-6 — observation
Claim: §5's "Two conventions" paragraph ends "the conflict is a decision this document must record", which OQ-5 and DEC-000320 have now done.
Location: specs/bundle-system.md:267-268.
Evidence: verified by reading.
Consequence: None; the paragraph is framed as the baseline at 6e77040. A reader may take "must record" as still pending.
Fix: "recorded at OQ-5 (DEC-000320)".

## Pre-ruled

### R-1 — delivery form: verified, no site missed
Result: all three sites state the ruled form — specs/bundle-system.md:55-58 (§3 J1), :148-150 (§4 G1), :311-313 (§6 AC-BS-1) — each naming the delivery directory DEC-000200 defines and `fiducial-bundle-<audience>-<timestamp>` per DEC-000290 (observed). No residual `~/Downloads`, sort-to-top, or `0-` prefix text remains anywhere in the PRD (observed by grep). AC-BS-2 (:320) refers to the filename by pointer, "the filename §4 states", which is consistent. DEC-000320 in the log states the same form (observed). One note, not a finding: J1 restates DEC-000290's content inline ("ISO 8601 basic, UTC, `Z` required") where G1 and AC-BS-1 cite the entry by identity only; under the PRD's own G2 principle the citation form is the safer one. OQ-5's pointer to the three sites is wrong by one section (N-5).

### R-2 — lore home: pre-ruled, not yet applied
Recorded, nothing filed. The lore home for G11 (specs/bundle-system.md:194-196) and AC-BS-12 (:372-375) is ruled (topic-walk ruling 13 T30, told): the tooling-facts artifact; entries dated, falsifiable, classified as lost response, never dispatched, caller error, or tool defect. The PRD does not yet state it; G11 and AC-BS-12 absorb it at the revision. The directive lint AC-BS-12 names exists as bin/check-directive (observed), so "once the directive lint learns the file" has a subject.

### OQ-5, OQ-6, OQ-10 — resolutions checked against the criteria that cite them
OQ-5 against AC-BS-2: consistent — same fields, same filename pointer, same retirement of DEC-000210's carried form; DEC-000320 says the same (observed). The header's generation-time form is unstated in both (N-3); the section pointer is off by one (N-5).
OQ-6 against AC-BS-9: consistent in substance; the first sentence of AC-BS-9 carries a pre-resolution residue (N-7). Cadence and ownership are held in OQ-6 pending the header package, as OQ-6 itself says; DEC-000330 records them whole (observed).
OQ-10 against AC-BS-4: consistent — skills/outline.md is in the writer set and in neither other set; its frontmatter at 6790702 is still `[writer, human]`, as OQ-10 says it will be until the tagging package (observed); DEC-000340 says the same (observed).

## OQ dependencies

Open questions with named resolvers, and where the PRD depends on them; none resolved here.

- OQ-1 (audience as roles or conditions) — resolver: the audit's first pass. Depended on by §4's row definition (`audience`), AC-BS-3, and OQ-2. N-1 bears on it: session kind is already a selection input through `all-decision-roles`.
- OQ-2 (one agent form per row) — resolver: the same audit pass. Depended on by G4, AC-BS-13, and the dual-form evidence in §5.
- OQ-3 (project-specific rows) — resolver: the first adopting project under AC-BS-11. Depended on by J5, G10, AC-BS-11. B-1 lives in the engagements/ tree OQ-3 mentions.
- OQ-4 (canonical corpus for shared rules) — resolver: AC-BS-14's first instance, Dave ruling. Depended on by AC-BS-14 and G2.
- OQ-7 (selection mechanism) — resolver: the TRD, within G5. Depended on by G3, G5, AC-BS-3, AC-BS-4, AC-BS-5, and delivery step 3. B-1 and N-1 both constrain the answer.
- OQ-8 (Decision Layer in writing bundles) — resolver: an experiment Dave directs. Depended on by AC-BS-4's three sets (the Decision Layer is member two of each). N-1 notes the present mechanism carrying it.
- OQ-9 (writing bundle as a kind) — resolver: with OQ-7. Depended on by the same sites as OQ-7.
- OQ-11 (the store) — resolver: the row count and dual-form evidence after the audit. Depended on by §4's end-state constraint, the scalability NFR, and §7's accepted risk.
