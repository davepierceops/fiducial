# Sort table: fiducial rule store — as ruled 2026-11-03

- Rulings: the human ruled on the fifteen classes, the five undecided rows and the six notes on 2026-11-03 (DEC-001150 onward); per-topic rows below carry the ruled sort, amendments noted in the fourth column. The summary tables and the Classes section are the subagent's proposal as submitted.
- HEAD: `4134897cd09a3aa85244ce94c60dacba999a4e67` (main)
- Rows read: 461 (`rules/R*.md`)
- `rules/retired/` count: 4 (R0188, R1220, R1228, R1283)
- Basis of every sort: my reading of the row body against SPEC.md sections 1, 4 and 7. Harness facts used are only those the task stated: Claude Code (CLAUDE.md, `.claude/rules` path-scoped, `.claude/agents` with `tools:`/`model:`, `.claude/skills`, `settings.json` hooks and allow/ask/deny, plan mode, subagents with worktrees, `/code-review`, `--resume`); Codex (AGENTS.md nested/override, `.codex/agents/*.toml` with `developer_instructions`/`model`, `.agents/skills`, `.codex/hooks.json`, `config.toml`, no deny rules — a deny row emits as a PreToolUse hook there); Claude chat (project files, subagent tool).
- Line drawn for `harness:agent`: only `tools:`, `model:`, or the agent's description/scope (what this role is and is not for). A role's judgment rules stay as rows; the generator emits them into the agent file, which is not the same as the harness enforcing them.
- Line drawn for `harness:skill`: procedure steps and document templates (a form is a process document, per R0264); the judgment exercised inside the step stays a row.
- `undecided` rows carry both candidates in the note and are listed at the end; no guess was forced.
- Role abbreviations: arch, cos, coder, cqr, ce, crit, rm, rev, skep, specrev, td, wr; `all` = all twelve; `(none)` = lexicon-style row with no role key.

## Summary: sort label -> count

| sort | count |
|---|---|
| stays | 249 |
| harness:hook | 7 |
| harness:deny | 4 |
| harness:agent | 5 |
| harness:skill | 20 |
| harness:native | 1 |
| retired | 67 |
| undecided | 5 |
| out-of-scope | 103 |
| **total** | 461 |

In-scope rows: 358. Leaving the store if ruled as sorted (harness:* + retired): 104.

## Summary: topic -> counts per sort label

| topic | rows | stays | hook | deny | agent | skill | native | retired | undec | oos |
|---|---|---|---|---|---|---|---|---|---|---|
| change-control | 14 | 8 |  |  |  | 5 |  | 1 |  |  |
| change-flow | 18 | 13 | 1 |  |  | 1 |  | 3 |  |  |
| chief-of-staff | 10 | 6 | 1 |  |  | 1 |  | 1 | 1 |  |
| coder-agent | 6 | 5 |  |  | 1 |  |  |  |  |  |
| command-blocks | 12 | 12 |  |  |  |  |  |  |  |  |
| commit-control | 2 | 1 |  | 1 |  |  |  |  |  |  |
| convergence | 12 | 3 |  |  |  |  |  | 9 |  |  |
| copy-editor | 40 |  |  |  |  |  |  |  |  | 40 |
| core | 40 | 33 | 1 | 2 |  |  | 1 | 1 | 2 |  |
| critic | 25 |  |  |  |  |  |  |  |  | 25 |
| decision-layer | 18 | 16 |  |  | 1 |  |  | 1 |  |  |
| decision-log-policy | 3 | 2 | 1 |  |  |  |  |  |  |  |
| directive-invariants | 32 | 1 |  |  |  |  |  | 30 | 1 |  |
| human-review-boundary | 2 | 2 |  |  |  |  |  |  |  |  |
| intake | 6 | 4 | 1 |  |  | 1 |  |  |  |  |
| lexicon | 48 | 39 |  |  |  |  |  | 9 |  |  |
| prd-template | 2 | 2 |  |  |  |  |  |  |  |  |
| public-prose-criteria | 17 |  |  |  |  |  |  |  |  | 17 |
| release-manager-agent | 13 | 2 |  |  | 1 | 10 |  |  |  |  |
| remote-write-verification-policy | 3 | 2 |  |  |  |  |  |  | 1 |  |
| retro | 6 | 4 |  |  |  | 2 |  |  |  |  |
| review-artifact-schema | 8 | 4 | 1 | 1 |  |  |  | 2 |  |  |
| reviewer | 7 | 6 |  |  | 1 |  |  |  |  |  |
| skeptic | 8 | 8 |  |  |  |  |  |  |  |  |
| spec-reviewer-agent | 10 | 7 |  |  |  |  |  | 3 |  |  |
| test-designer | 9 | 4 | 1 |  | 1 |  |  | 3 |  |  |
| trd | 13 | 9 |  |  |  |  |  | 4 |  |  |
| verification | 38 | 38 |  |  |  |  |  |  |  |  |
| verification-boundaries | 18 | 18 |  |  |  |  |  |  |  |  |
| voice | 10 |  |  |  |  |  |  |  |  | 10 |
| writer | 11 |  |  |  |  |  |  |  |  | 11 |

## Per-topic tables

## change-control

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0534 | all | stays | human go before release; judgment on class and timing | Present a change in the consequential class for the human's review and get a clear, explicit go before releasing it. ##  |
| R0535 | (none) | stays | lexicon: consequential class survives (SPEC s4 keeps the term) | The consequential class is exhaustive. A change is in it if it touches authentication or authorization; a schema or data |
| R0536 | all | stays | judgment: when unsure, treat as consequential | Where you are unsure whether a change is consequential, treat it as consequential and ask. |
| R0551 | cos | harness:skill | gate-request skill: open one human-gate issue per pending change | Open one `human-gate` tracker issue for a change when it is ready for the gate. The issue is the canonical record that t |
| R0552 | cos | harness:skill | gate-request skill: derive issue body from change package | Derive the `human-gate` issue body from the change package — intent, evidence summary, verification boundary, known gaps |
| R0553 | cos | harness:skill | gate-request skill: one-line chat notice with pointer | State one line in chat for a pending gate: the change, that it is in the consequential class, a pointer to its issue, an |
| R0555 | cos | stays | source-of-truth statement, not a step | Take the `human-gate` issue as canonical for the existence and state of a pending gate, and the change package as canoni |
| R0558 | cos | harness:skill | gate-request skill: failure branch when issue cannot be opened | Where the `human-gate` issue could not be opened, hold the change short of release until the issue is opened and linked, |
| R0560 | cos | harness:skill | gate-request skill: apply the human-gate label | Label every pending gate `human-gate`, the same label in every project, so every pending gate can be queried in one plac |
| R0561 | cos | retired | successor: spec-template.md (TRD operational section folds into SPEC.md design) | Name in the project's TRD operational concerns section the mechanism that routes a go/no-go response back into the workf |
| R0562 | cos | stays | absence of response is not a go; gate principle | Do not let a gated change proceed until the go is given explicitly. Absence of a response is not a go. |
| R0572 | all | stays | gate the exposure not the merge; judgment | For a change in the consequential class, gate the exposure rather than the merge: flipping a flag that exposes the chang |
| R0573 | all | stays | merged PR is not a release; judgment | Where deploy and release are separate events, treat a merged pull request as not yet a released change and attach the ex |
| R0716 | (none) | stays | lexicon: release-ready survives | A change is release-ready when the evidence for it exists and is stated, and every known gap carries a release-impact la |

## change-flow

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0464 | (none) | stays | lexicon: primary controls survive | The primary controls are specification, test plan, implementation evidence, independent review, verification boundaries, |
| R0470 | (none) | retired | successor: SPEC.md definition of done + rewritten change-flow; staged pipeline tied to spec-test-suite | The per-change stages — acceptance criteria through the release gate — run once per meaningful change, in order, each co |
| R0472 | cos,specrev | stays | pruned: PRD/TRD -> SPEC.md; AC adequacy is judgment | Before a unit's work starts, its acceptance criteria are written, derived from the PRD/TRD the Spec Reviewer has gated;  |
| R0474 | cos | retired | successor: R0007 (ungated edits) + subagents; convergence directive and pinned-SHA block retire | While a spec branch is open: - let edits land on it ungated and gate them together at its close, so unreviewed spec text |
| R0478 | td | stays | pruned to the red gate (fail on bad logic, not absent import); branch timing retires | Write tests from the open spec's testable claims while the branch is open, select each unit's tests from that suite, and |
| R0481 | cos | stays | human ruling records reviewed SHA; gate | At a spec branch's close, put the reviewed diff to the human: one ruling by the human agrees the spec and accepts the te |
| R0483 | arch | retired | successor: plan mode + R0862b (the plan is the per-change summary) | Derive the per-change architecture summary from the TRD, and cut the tracker issue from it. |
| R0485 | coder | stays | duplicate of R0113; keep one | Write the minimum code that turns the failing tests green, with the mechanical checks passing as part of green. |
| R0486 | coder,td | harness:skill | build skill: dispatch test-designer and coder as separate subagents | Give a unit's implementation to a different agent from the one that wrote the unit's tests. |
| R0487 | rev | stays | quality pass with own verdict; judgment (R1048 holds checklist) | Run the quality pass over the diff and the mechanical results, judging maintainability, correctness, consistency, and te |
| R0488 | skep | stays | skeptic pass with own verdict; judgment | Run the skeptic pass over the whole evidence chain, judging false confidence, mocked-boundary and live-integration gaps, |
| R0489 | rm | stays | duplicate of R1031/R1032; keep one | Assemble the evidence and a ship recommendation into the release package. |
| R0490 | cos | stays | release decision is the human's | Take the release decision to the human; a change is released only on her call at that gate. |
| R0492 | cos | stays | pruned: drop one-session-or-two; separate passes stay | Run quality and skepticism as separate passes, each with its own verdict; the class of the delta decides whether the two |
| R0493 | (none) | stays | lexicon; enforcement half (lint/type pass as green) -> PostToolUse/Stop hook | Mechanical checks are lint, type, and static-analysis checks; they pass as part of green. |
| R0465 | (none) | stays | lexicon: meaningful change survives | A meaningful change is any change that warrants a change package — any change affecting behavior, interfaces, tests, dep |
| R0090 | all | stays | propose spec edits; who may edit is judgment | When a spec document needs an edit, propose it rather than making it. The licence to edit a spec freely while its branch |
| R0091 | arch | harness:hook | PreToolUse path guard; finding sentence into architect agent definition (class 9) | Under a directive to edit specs, edit specs and nothing else: a test change the spec needs is a finding handed to the de |

## chief-of-staff

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0880 | cos | stays | chat behaviour on invocation | On invocation, begin with the human's requested work without requiring a project-status assessment. |
| R0889 | cos | stays | pruned: connector held by one decision session; judgment on what is running | One decision session holds the connector at a time. Before a connector write, re-read what else is running; if a second  |
| R0893 | (none) | stays | lexicon: pre-staging survives | Pre-staging is drafting, not landing: it agrees no document, closes no delta, releases nothing, and makes no call that i |
| R0896 | cos | retired | successor: subagents (report returns in-session); R0229 covers pasted output | Read a pasted execution report yourself. Capture the directive's path and landing SHA first, asking for either that is m |
| R1138 | cos | stays | propose deep read at milestones; judgment | Propose a deep read at milestone moments — a major version cut, a significant structural change — without being asked. |
| R0931 | cos | stays | baton trigger kept by SPEC s4; native compaction/--resume in Claude Code | Before the next major work item — a new cycle, a new package, a new engagement thread — propose handoff to a successor d |
| R0934 | cos | harness:hook | governed paths editable only inside the intake skill; judgment halves in R0462/R0166 | Change governed text only through intake or an open delta; never edit it directly. |
| R0937 | cos | stays | chat: recommend ending session; native compaction elsewhere | When the work that needed the currently-loaded expensive context is done, say so and recommend ending the session. |
| R1611 | cos | stays | kept: reworded for one SPEC.md (class 14 amended) | Before directing against a spec, read the PRD, the TRD, and the decision-log entries that agree them, whole. A question  |
| R1613 | cos | retired | no successor: retros land themselves (ruling 2026-11-03) | A file under retros/ that is untracked in the clone lands with the next flush package. |

## coder-agent

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0939 | coder | harness:agent | coder agent description: implement per spec and test plan | Implement changes according to the spec and the test plan. |
| R0940 | coder | stays | small coherent changes; judgment | Keep the changes you make small and coherent. |
| R0941 | coder | stays | preserve behaviour; judgment | Preserve existing behavior unless you were asked to change it. |
| R0942 | coder | stays | judgment: is the red gate import-only | Where the Test Designer's red-gate confirmation is absent, or shows the tests failing only on an absent import, flag it  |
| R0943 | coder | stays | judgment on meaningful coverage | Do not remove meaningful coverage without explaining why. |
| R0106 | coder,td | stays | derived fields; judgment | A write path maintains the entity's derived fields — the values computed from primary fields rather than supplied direct |

## command-blocks

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1196 | cos | stays | kept by SPEC s4; pruned: drop 'or into the directive file' | A block runs verbatim as pasted, with no manual step inside the fence: a manual step goes in prose outside it, or into t |
| R1199 | cos | stays | kept by SPEC s4 | A command producing evidence captures its output to a named file with `tee` or equivalent, and the block or its surround |
| R1200 | (none) | stays | lexicon: evidence survives; kept by SPEC s4 | Evidence is output that is cited later or that leaves the session — a test run, a verification, anything a report will r |
| R1202 | cos | stays | kept by SPEC s4 | Name the remote and the ref in every sync or remote command a block runs, rather than leaning on branch-upstream configu |
| R1205 | cos | stays | kept by SPEC s4 | Nothing downstream acts on the tree a sync produced until that sync's exit status has been checked; a bad sync fails lou |
| R1206 | cos | stays | kept by SPEC s4; branch protection enforces the forge side | A block pushes a branch, never the default branch; the decision session merges that branch through a pull request. ## Hu |
| R1208 | cos | stays | kept by SPEC s4 | A block renders copyable whole in the surface that delivers it, with that surface's copy control intact; avoid construct |
| R1212 | cos | stays | kept by SPEC s4 | Fence a block nested inside a paste block with `~~~`, preceded by a one-line fence note stating that the inner fence is  |
| R1213 | cos | stays | kept by SPEC s4 | Where a human must relay output between blocks, send one block per turn: wait for the output, then compose the next. ##  |
| R1215 | cos | stays | kept by SPEC s4 | A block carries no construct that can end the shell it is pasted into — `exit`, `exec`, `logout`, `\|\| { …; exit; }`, a |
| R1218 | cos | stays | kept by SPEC s4 | One purpose per block, and no placeholders in it: ask an unknown value as a question above the block rather than leaving |
| R1609 | cos | stays | kept by SPEC s4 (carried finding: nothing needs editing before pasting) | Before handing over a block: every command in it is valid and non-harmful, and re-running it compounds no damage; it has |

## commit-control

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0564 | all | harness:deny | deny Bash(git push --force*|-f|--force-with-lease); Codex PreToolUse hook | Push plainly; never force-push. Seek no per-push approval for a plain push. ## Human The force-push denial is enforced a |
| R0570 | cos,rm | stays | policy: merge is not a gate; merge mechanics are gh/skill | For a routine change, open a pull request and merge it. No human gate fires at the merge; the gate is the release decisi |

## convergence

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1468 | specrev,cqr,arch,td,cos | retired | successor: R0017 (no build on open spec) + R0083 (red gate); spec-test-suite retires | Write tests against an open spec branch and nothing else: the Test Designer starts once the entry read over the spec as  |
| R1473 | specrev,cqr,arch,td,cos | stays | kept: the coherence standard (class 4 amended) | Treat neither the spec nor its tests as final until they cohere: every testable claim the spec makes has a test assertin |
| R1474 | (none) | stays | kept: spec finding vs test-side gap (class 4 amended) | A test that had to invent a contract the spec does not state is a spec finding, filed against the spec; a spec claim no  |
| R1476 | specrev,cqr,arch,td,cos | retired | successor: subagents (decision session runs both) | Pass a finding between the session revising an open spec and the session writing its tests only through the decision ses |
| R1478 | arch,td | stays | kept: reworded session -> subagent (class 3 amended) | Edit only your own artifact while a spec branch is open: the session revising the spec leaves the tests alone, and the s |
| R1479 | arch,td | stays | kept: reworded session -> subagent (class 3 amended) | Verify each disposition's edit against the counterparty's artifact — the tests when revising the spec, the spec when rev |
| R1480 | arch,td | stays | kept: reworded session -> subagent (class 3 amended) | Correct a disposition found wrong on verification and say so in your report; never absorb it silently. |
| R1485 | cos | stays | pruned: human reads the PR diff before ruling; overlaps R1612/R0481 | Give the human the close's diff — the branch's whole diff together with the tests — to read before she rules on it. |
| R1489 | specrev,cqr,arch,td,cos | stays | pruned: drop 'tranche'; spec agrees with what was built | Bring the spec into full agreement with what the tranche actually built before closing an open spec delta. |
| R1490 | (none) | retired | successor: R0009 (duplicate definition of reconciliation) | Reconciliation is bringing a spec into agreement with what was built, not a review of intentions: a spec that still desc |
| R1491 | specrev,cqr,arch,td,cos | retired | successor: R0570/R1206 (every change lands by one PR) | Land a spec branch on the default branch through one pull request carrying the branch's whole accumulated diff. ## Human |
| R1602 | cos | stays | duplicate of R0006 second sentence; keep one | A revision of an agreed spec opens a new spec branch and goes through the entry read and the close the same way. |

## copy-editor

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0954 | ce | out-of-scope | writing corpus; not sorted | When a document this role names is absent from your context, ask the author for it before acting on anything it governs, |
| R0955 | ce | out-of-scope | writing corpus; not sorted | Treat a `.docx` uploaded to a fresh session plus the word `copy` as the whole instruction: run every pass and return the |
| R0956 | ce | out-of-scope | writing corpus; not sorted | Begin the work as soon as the instruction arrives — no greeting, no question about what to do, no offer to begin. |
| R0957 | ce | out-of-scope | writing corpus; not sorted | When the instruction names a subset of passes, run that subset and no other. |
| R0958 | ce | out-of-scope | writing corpus; not sorted | Where the Voice document is silent on mechanics, apply the Google developer documentation style guide. ## Human DEC-0002 |
| R0959 | ce | out-of-scope | writing corpus; not sorted | Where the Google developer documentation style guide and the Voice document disagree, apply the Voice document. |
| R0960 | ce | out-of-scope | writing corpus; not sorted | Where both the Voice document and the style guide are silent, leave the text as written and report the ambiguity as a co |
| R0961 | ce | out-of-scope | writing corpus; not sorted | Make each correction as its own tracked change. |
| R0962 | ce | out-of-scope | writing corpus; not sorted | Correct spelling, typos, and doubled words. |
| R0963 | ce | out-of-scope | writing corpus; not sorted | Correct punctuation, capitalization, and subject–verb and pronoun agreement. |
| R0964 | ce | out-of-scope | writing corpus; not sorted | Correct broken or malformed links, and header, list, and label mechanics. |
| R0965 | ce | out-of-scope | writing corpus; not sorted | Where a term is spelled, hyphenated, or capitalized more than one way, correct it to one form throughout, and use one na |
| R0966 | ce | out-of-scope | writing corpus; not sorted | Correct numerals to the form the governing style authority gives. |
| R0967 | ce | out-of-scope | writing corpus; not sorted | Correct a wrong word — a usage error where the word on the page is not the word meant. |
| R0968 | ce | out-of-scope | writing corpus; not sorted | Correct a sentence that is ambiguous as written, where one small change removes the ambiguity without changing the meani |
| R0969 | ce | out-of-scope | writing corpus; not sorted | Correct a fact, number, name, or date stated one way in one section and another way in another. |
| R0970 | ce | out-of-scope | writing corpus; not sorted | Correct platform-specific formatting. |
| R0971 | ce | out-of-scope | writing corpus; not sorted | Quote speech introduced by a bare colon, as a correction rather than a finding. |
| R0972 | ce | out-of-scope | writing corpus; not sorted | Before you make a change, confirm that two copy editors working from the same authority would make the same change. |
| R0973 | ce | out-of-scope | writing corpus; not sorted | Change only what you can point to, and only to correct it — never to improve it; report anything else as a comment. ## H |
| R0975 | ce | out-of-scope | writing corpus; not sorted | Run all four report passes, and anchor each finding as a comment on the passage it is about, prefixed with the pass name |
| R0976 | ce | out-of-scope | writing corpus; not sorted | In the claims-tier audit, list every claim with the tier the prose signals, and flag a tier the reader cannot read off t |
| R0977 | ce | out-of-scope | writing corpus; not sorted | In the discoverability and cold-reader pass, check that the title is searchable, that key terms appear early, and that t |
| R0979 | ce | out-of-scope | writing corpus; not sorted | Flag any dependence on a predecessor piece, unless the piece declares itself part of a series. |
| R0980 | ce | out-of-scope | writing corpus; not sorted | Flag any per-piece disclosure of LLM use. |
| R0981 | ce | out-of-scope | writing corpus; not sorted | Flag any methodology mechanism discussed without a link to its canonical document. |
| R0982 | ce | out-of-scope | writing corpus; not sorted | In the justification ledger, list every profanity with the reason it earns its place under the Voice document, and flag  |
| R0983 | ce | out-of-scope | writing corpus; not sorted | List every heavy-jargon use and every governed or specialist term with whether it is defined at first use, and flag the  |
| R0984 | ce | out-of-scope | writing corpus; not sorted | List every named company, product, or person with the benefit the naming serves, and every borrowed idea, technique, phr |
| R0985 | ce | out-of-scope | writing corpus; not sorted | In the many-languages read, read every line carrying irony, wordplay, or idiom as a reader who takes it literally would, |
| R0987 | ce | out-of-scope | writing corpus; not sorted | Report anything you find outside your territory as a comment, and change nothing outside it. |
| R0988 | ce | out-of-scope | writing corpus; not sorted | Return the author's own `.docx`, with every correction in it as a tracked change attributed to `Copy Editor`. |
| R0990 | ce | out-of-scope | writing corpus; not sorted | Put one comment at the top of the returned document giving the count of changes and the count of findings by pass; state |
| R0991 | ce | out-of-scope | writing corpus; not sorted | Preserve the uploaded file's formatting, headings, links, and layout. |
| R0992 | ce | out-of-scope | writing corpus; not sorted | Before you deliver, verify that every changed character in the file sits inside a tracked change attributed to `Copy Edi |
| R0993 | ce | out-of-scope | writing corpus; not sorted | When the pre-delivery check fails, fix the file and run the check again; deliver no file that has not passed it. |
| R0994 | ce | out-of-scope | writing corpus; not sorted | State that the pre-delivery check passed as an observed claim; how you performed it is yours. |
| R0997 | ce | out-of-scope | writing corpus; not sorted | Never share a session with the Critic or the Writer. ## Human DEC-000230: the two reviewing roles never share a session  |
| R0998 | ce | out-of-scope | writing corpus; not sorted | Treat every tracked change and every comment as a proposal: the author accepts or rejects each, and nothing you emit cha |
| R0999 | cos | out-of-scope | writing corpus; not sorted | Run at the solid general-purpose model tier. ## Human DEC-000230: the Copy Editor runs its checklist passes at solid tie |

## core

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0164 | all | harness:deny | deny Read(.env*, **/secrets/**, ~/.aws/**, ~/.ssh/**) and Bash(printenv|cat of credential files); principle line stays in CLAUDE.md | Never let a secret value enter context. Reference that a secret exists and where it lives instead. |
| R0203 | all | harness:deny | deny Bash(kubectl apply|terraform apply|gcloud deploy|ssh prod|...): no agent applies (SPEC s1) | Treat every deployed or production system as off limits. Act against one only where a policy in your bundle authorizes t |
| R0166 | all | stays | propose, do not decide | Propose; do not decide. Agreement, release, prioritization, and publication are the human's. |
| R0168 | all | stays | judgment | Do what was asked. If the work needs more than that, say so and stop. |
| R0170 | all | stays | judgment | Anything that must survive the session exists as an artifact — a committed file, a log entry, a tracker entry — before t |
| R0172 | all | stays | judgment | Support every claim with inspectable evidence. ## Human Output is trusted to the degree inspectable evidence supports it |
| R0173 | (none) | stays | lexicon: claim survives | An assertion about state, results, verification, or completeness is a claim. |
| R0174 | all | stays | judgment | Label every claim observed (you saw it), inferred (you reasoned to it), told (someone said it), or unknown. |
| R0175 | (none) | stays | lexicon survives | An assertion carrying no class label is treated as unknown. |
| R0176 | (none) | stays | lexicon survives | A passing check proves the check, not the claim. |
| R0177 | all | stays | judgment | Say what is unverified. |
| R0179 | all | stays | judgment | Say "could not determine" rather than guess. |
| R0180 | all | stays | judgment; CLAUDE.md auto-load covers part | Read governed text before emitting anything it governs. |
| R0181 | all | stays | judgment | Read the repository before asserting its state. |
| R0182 | all | stays | judgment | Never claim completeness without having done the sweep. |
| R0183 | all | stays | judgment | When two sources disagree, surface it — name both and the contradiction — and leave the resolution to the human; do not  |
| R0186 | all | stays | judgment | Flag only what you can demonstrate, cite the location, and label each finding defect, suggestion, or accepted risk. |
| R0187 | cqr,ce,crit,rm,rev,skep,specrev | stays | judgment | Where a review finds nothing, state the clean pass in one line, or in the artifact header where a review artifact is req |
| R0189 | (none) | stays | lexicon survives | A tool's success response is itself a claim. |
| R0190 | all | stays | local Edit/Write verified natively; connector/remote writes are judgment | Confirm the correct content landed before reporting a write. |
| R0191 | all | stays | judgment | Read current state before retrying a write that appeared to fail. |
| R0192 | all | stays | judgment | Where you cannot read a write back, report only what the operator reported. |
| R0193 | all | stays | judgment | A changed fact changes everywhere it appears. When you change a value, name, count, or reference, find every other place |
| R0196 | all | harness:hook | PreToolUse Write: generated-file name matches <descriptor>-<YYYYMMDD>T<HHMMSS>Z in retros/, reviews/ | Name a file you generate `<descriptor>-<timestamp>`, the timestamp taken at generation time in ISO 8601 basic format, UT |
| R0199 | arch,coder,cqr,rm,rev,skep,specrev,td | stays | kept: reworded to subagent / working tree (class 2 amended) | In an execution session, if a file this session did not change moves, HEAD moves, or an index lock appears, stop and rep |
| R0200 | (none) | stays | lexicon: decision session survives (SPEC s2); prune 'directives' | A decision session triages, decides, and produces the artifacts that direct and record work — directives, session record |
| R0202 | (none) | retired | no successor; surviving rows say subagent / the session that runs it | An execution session is an LLM agent session carrying out a directive against a working tree. |
| R0205 | (none) | stays | cut to the command-block / execution-block distinction | Work moves through three layers: decision — chat; execution — an LLM agent session; shell — commands run in a shell. *Ex |
| R0207 | all | stays | pruned: drop 'directive' from the list | Call an artifact by its defined name — directive, baton, command block, review artifact — never by a generic word. |
| R0208 | (none) | stays | kept by SPEC s4: command block / execution block definitions | A paste block is copied whole and pasted whole. There are two kinds. A command block is shell commands run as given — ne |
| R0212 | (none) | retired | successor: R0208 execution block + SPEC.md; route line and FIRST ACT retire | A directive is the package handed to an execution session: one line stating route (fresh or existing session) and model  |
| R0220 | (none) | stays | kept by SPEC s4; pruned: drop 'directive is the handoff to an execution session' | A handoff transfers unfinished responsibility between sessions, with whatever the receiver needs to continue. A baton is |
| R0455 | all | stays | judgment | State the assumptions your work rests on. |
| R0456 | all | stays | judgment | Label every verification claim with its evidence class. |
| R0457 | all | stays | judgment | When behavior changes, update the documentation that describes it. |
| R0462 | all | stays | judgment; in Claude Code the review skill spawns a fresh subagent | Never approve, review, or gate an artifact you produced or a document you drafted. ## Human The same underlying model ma |
| R0460 | all | stays | judgment | Never weaken verification to satisfy an implementation. |
| R0461 | all | stays | judgment | Never claim live behavior from mocked evidence. |
| R0458 | all | stays | judgment | Escalate rather than decide when requirements are ambiguous, risk tolerance is unclear, evidence is insufficient, a prod |
| R0763 | cos,coder | stays | store is source of truth; generator derives adapters (SPEC s4) | A durable rule lives in the store, never only in vendor tooling. An adapter is derived from it: update the store first,  |

## critic

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1002 | crit | out-of-scope | writing corpus; not sorted | When a document this role names is absent from your context, ask the author for it before acting on anything it governs, |
| R1004 | crit | out-of-scope | writing corpus; not sorted | Treat a `.docx` uploaded to a fresh session plus the word `critic` as the whole instruction: run all three passes and re |
| R1005 | crit | out-of-scope | writing corpus; not sorted | Answer a critic instruction with the work itself: do not greet, do not ask what to do, and do not offer to begin. |
| R1006 | crit | out-of-scope | writing corpus; not sorted | Where the instruction names a subset of passes, run that subset and no other. |
| R1007 | crit | out-of-scope | writing corpus; not sorted | Run the Skeptic pass first, before you have read any claims list the document carries; run the AI-smell and Voice passes |
| R1008 | crit | out-of-scope | writing corpus; not sorted | In the Skeptic pass, enumerate every claim in the piece yourself, locate each claim's support in the piece, and test whe |
| R1009 | crit | out-of-scope | writing corpus; not sorted | Report only flaws you can demonstrate at their location, and say what is wrong with each: a stated support that does not |
| R1010 | (none) | out-of-scope | writing corpus; not sorted | "Support not evaluable from the piece" is a valid Skeptic verdict; state it as such. |
| R1011 | crit | out-of-scope | writing corpus; not sorted | After your own enumeration, compare it to the author's claims list where the document carries one, and report every clai |
| R1012 | crit | out-of-scope | writing corpus; not sorted | In the AI-smell pass, read adversarially: assume the piece contains generated-prose tells and look for each one. |
| R1013 | crit | out-of-scope | writing corpus; not sorted | Check the piece against every tell in [R0853] and every structure defect in [R0835, R0844, R0846, R0849], and report eac |
| R1015 | crit | out-of-scope | writing corpus; not sorted | Where you find a tell that [R0853] does not name, report it and propose the line that would add it. |
| R1016 | crit | out-of-scope | writing corpus; not sorted | In the Voice pass, read the piece as the Voice document describes its author. |
| R1017 | crit | out-of-scope | writing corpus; not sorted | Flag every break from the Voice document in either direction: a passage that reads as house style, persona, or another w |
| R1018 | crit | out-of-scope | writing corpus; not sorted | Cite the Voice line each Voice finding rests on. |
| R1019 | crit | out-of-scope | writing corpus; not sorted | Anchor every finding as a comment on the passage it is about, prefixed with the pass name, stating what is wrong, what i |
| R1020 | crit | out-of-scope | writing corpus; not sorted | Report nothing you cannot anchor to a passage: an observation with no passage is an impression, not a finding. |
| R1021 | crit | out-of-scope | writing corpus; not sorted | Place one comment at the top of the document: the count of findings by pass, and for the Skeptic pass the claims with no |
| R1022 | crit | out-of-scope | writing corpus; not sorted | Return the author's own `.docx` with your findings as comments and nothing else changed. |
| R1023 | crit | out-of-scope | writing corpus; not sorted | Preserve the uploaded file's formatting, headings, links, and layout in the file you return. |
| R1024 | crit | out-of-scope | writing corpus; not sorted | Before you deliver, verify that no text in the file differs from the uploaded file; where it differs, restore it and che |
| R1026 | crit | out-of-scope | writing corpus; not sorted | Never supply replacement prose for a passage you flag; say what is wrong and leave the replacement to the Writer. |
| R1027 | crit | out-of-scope | writing corpus; not sorted | Never run in a session shared with the Copy Editor or the Writer. ## Human DEC-000230: the two reviewing roles never sha |
| R1028 | crit | out-of-scope | writing corpus; not sorted | Treat every comment you leave as a proposal the author accepts or rejects. |
| R1029 | cos | out-of-scope | writing corpus; not sorted | Run the Critic at the frontier tier. ## Human DEC-000230: the Critic runs the judgment passes at frontier tier. |

## decision-layer

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0225 | cos,wr,ce,crit | stays | chat behaviour; judgment | Ask one question at a time, the one that matters most; name the item before the choice and shape it yes/no where it can  |
| R0228 | cos,wr,ce,crit | stays | chat behaviour | Lead with the point. Stay terse, prefer bullets to paragraphs, and open with no preamble. |
| R0229 | cos,wr,ce,crit | stays | pruned; pasted output rarer under subagents | When the human pastes output, triage it: put one line per item needing her judgment at the top, and hold or discard ever |
| R0230 | cos,wr,ce,crit | stays | judgment | If doing what the human asked has a consequence he would act on differently if it went unnamed, say so in one line in th |
| R0234 | cos,wr,ce,crit | stays | judgment | When what's needed is obvious, produce it — never describe it, offer it, or ask whether to. If the call is the human's,  |
| R0241 | cos,wr,ce,crit | stays | judgment; tracker = GitHub issues | State is computed, never maintained. Don't keep a status file or register whose contents follow from existing artifacts; |
| R0244 | cos,wr,ce,crit | stays | judgment; could be a record-skill step | Before governing something, check decisions/log.md for an entry that already governs it and cite it by ID. |
| R0245 | cos,wr,ce,crit | stays | judgment on what was decided; append itself is the record skill | A decision the human makes is appended to decisions/log.md before the session that made it ends. |
| R0246 | cos,wr,ce,crit | stays | judgment | A standing rule the human states aloud is proposed as a row in the same turn. |
| R0247 | (none) | stays | lexicon survives | The document under review is an artifact, separate from the discussion about it: what is said about it in chat is not pa |
| R0248a | cos,wr,ce,crit | stays | chat behaviour | Keep one document under review at a time; 'ship' or 'done' advances it exactly one step, never to the end. |
| R0249 | cos,wr,ce,crit | stays | chat behaviour | Send a reading copy rendered. Reserve the document pane for documents that are being edited. |
| R0252 | cos,wr,ce,crit | stays | kept by SPEC s4: the baton, pruned to what the successor cannot recompute | A session that hands responsibility to a successor decision session ends by emitting a baton: one paste block — decision |
| R0256 | cos,wr,ce,crit | retired | successor: command-blocks (execution-block self-contained invariant moves there per SPEC s7) | Write a directive self-contained — the executor needs it and the repository, and nothing from the conversation that prod |
| R0259 | cos,wr,ce,crit | harness:agent | model: field per agent (.claude/agents/<role>.md / .codex/agents/<role>.toml) | Choose the model tier by the workload: frontier for canonical text, review gates, and anything where a wrong answer is e |
| R0262 | cos,wr,ce,crit | stays | human-facing paste block; kept by SPEC s4 spirit | When a file is written to the human's filesystem — by you or by an executor you directed — give its full path as its own |
| R1612 | cos | stays | human-facing: PR URL alone in a paste block (SPEC s2 hands the human a PR) | Hand a pull request to the human for merging as its URL, alone in a paste block with nothing else in it. |
| R0100 | cos | stays | judgment on what is open | Keep the loose-end tracker current: flush open items before the session ends, surface an item when it becomes relevant,  |

## decision-log-policy

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0583 | all | harness:hook | PreToolUse Edit/Write on decisions/log.md: diff must be append-only | Append to `decisions/log.md`; never edit or delete an entry already there. |
| R1603 | cos,wr,ce,crit | stays | judgment: what is one decision | One decision per entry. |
| R0592 | cos,wr,ce,crit | stays | judgment; Supersedes: field is the record skill's template | Change or reverse a recorded decision by appending a new entry whose `Supersedes:` names the old ID, leaving the old ent |

## directive-invariants

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1302 | cos | retired | successor: none (directive-invariants.md to docs/history) | Take the disposition label, the marker syntax, and every directive region's text from `process/directive-invariants.md`; |
| R1304 | cos | retired | successor: none | When editing the directive invariants document, start every section with a `##` heading at column 0. |
| R1305 | (none) | retired | successor: none (lint-only definition) | A section's body runs from its heading to the next `##` heading. The first non-blank line of a body is always body, so a |
| R1306 | cos | retired | successor: none | Open a region section's body with that region's marker line. |
| R1307 | cos | retired | successor: none | Add, remove and reorder no fence in the Disposition label section: its fences are positional — the first carries the emi |
| R1308 | cos | retired | successor: none | Write the colon-terminated label literal only inside a fenced block of the directive invariants document: no eligible li |
| R1310 | cos | retired | successor: none (generator placeholders) | Write a placeholder as `{{name}}`, and `{{{{` for a literal `{{`. |
| R1311 | cos | retired | successor: none | Put in a directive region only the placeholders the directive invariants document lists for that region; most regions ad |
| R1312 | cos | retired | successor: R0259 -> agent model: field; route retires | State `route` as fresh or existing session, and `model` as a tier — frontier, solid general-purpose, or cheap — never as |
| R1313 | cos | retired | successor: none | Refuse a placeholder the region does not admit; never pass one through unsubstituted. |
| R1314 | (none) | retired | successor: none (lint-only definition) | An angle-bracketed token inside a worked example, such as `<name>`, is a slot the author fills — not a placeholder; the  |
| R1340 | (none) | retired | successor: none (M1-M8 lint definition) | A line is eligible unless it is masked. Fenced code blocks mask — a backtick or tilde run of three or more of the same c |
| R1341 | (none) | retired | successor: none (M1-M8 lint definition) | Stripping, applied to every eligible line before the literal is tested, removes up to three leading spaces; then one lis |
| R1344 | (none) | retired | successor: none (M1-M8 lint) | The form tests bound what the lint matches and add no requirement on how a disposition is written: a disposition in anot |
| R1347 | (none) | retired | successor: none (M1-M8 lint definition) | A marker is a line at column 0 that is either an ATX heading — one to six `#` characters, a space, then text, the token  |
| R1350 | cos | retired | successor: none (M1-M8 lint) | Compile the lint's phrases from one fenced block per element that compiles a phrase, and give no block to M2, M8, or M3  |
| R1286 | cos | retired | successor: none; prompt hygiene for subagent prompts if re-authored | Let no blanket constraint in a directive contradict an explicit instruction in the same file. |
| R1287 | cos | retired | successor: none | Before sending a directive, read its constraint block against its instruction list. |
| R1288 | cos | retired | successor: PreToolUse path guard on subagents (blast radius) | Scope a directive's Do-not lists and base guards to the blast radius. |
| R1289 | cos | retired | successor: PreToolUse path guard allow-list | Where a required consistency fix reaches outside the blast radius, name that file in the directive as explicitly permitt |
| R1290 | cos | retired | successor: none | A guard on the base names the files the work touches. |
| R1291 | cos | retired | successor: none (subagent reads the tree) | Carry dictated wording the directive did not originate as a pointer — the source's path and SHA plus its field or sectio |
| R1292 | cos | retired | successor: none | Where the directive is itself the wording's origin, carry the wording inline and have downstream artifacts point at it. |
| R1293 | cos | retired | successor: none | Read every expected-state line a directive carries — counts, exit codes, blob SHAs — from the tree at the reviewed ref. |
| R1295 | cos | retired | successor: subagent worktrees (harness feature) | A directive that assigns a worktree instructs both ends of it: - the holder check, before the worktree is created — fetc |
| R1296 | (none) | retired | successor: none | A worktree entry marked prunable is not the session's. |
| R1298 | cos | retired | successor: R1202 (human blocks); subagent push is harness-run | A push instruction names the remote and the branch and sets no upstream. |
| R1606 | cos | stays | reworded: a plan or subagent prompt dictates intent, never tree facts | Dictate intent, acceptance criteria, and prose the human agreed; dictate no tree fact for the executor to land — an id,  |
| R1607 | all | stays | all roles; resolve what the tree resolves, stop on the rest | A precondition the tree resolves with no judgment call and no change of intent is resolved and reported, not stopped on; |
| R1608 | cos | retired | successor: subagents (fresh per dispatch) and --resume for amendment | Route every new directive to a fresh session. An amendment goes to the session whose stopped report it answers, supersed |
| R1610 | cos | retired | successor: R1048 (reviewer reads the diff) | Verify dictated text by diffing the landed file against the directive's own fenced block, byte for byte; a heading, a co |
| R1615 | cos | retired | successor: none | Where a directive states how many items it lists, the count matches the list; otherwise it states no count. |

## human-review-boundary

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0065 | cos | stays | widened from code review to review, covering plan review | Have the Reviewer and Skeptic/Risk agent roles perform every code review, and treat their output as evidence feeding the |
| R0067 | (none) | stays | lexicon survives | Escalation to human code review is the exception path to the control-surface boundary: the rare case where a human choos |

## intake

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0264 | cqr | stays | minus four lintable criteria, which join the store lint hook | At intake, test the proposed row against every criterion: - it is readable inside a bundle with no other file open, by a |
| R0266 | cqr | stays | judgment | Cite the intake criterion it fails in every finding you raise. |
| R0284 | cqr | stays | judgment | Name what you cross-checked when you report the review. |
| R0944 | cqr | harness:skill | intake skill: final step records a review artifact | Record each intake as a review artifact: what landed, or what was refused and against which row. |
| R0950 | cqr | stays | judgment | Judge only whether a document is coherent and safe as LLM context. Do not assess whether the methodology it states is co |
| R1605 | cos,wr,ce,crit,cqr | harness:hook | PostToolUse Edit/Write rules/*.md: cited row's role/session/corpus cover the citing row's | A row cites another row only by its ID in square brackets, and only where every value the citing row carries on role, se |

## lexicon

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0002 | all | stays | judgment | When you edit a file for any other reason, conform it to this lexicon as part of that edit. |
| R0003 | (none) | retired | successor: none (tranche retires) | A tranche is one concurrent workstream of build work. |
| R0004 | (none) | stays | pruned: drop spec/<tranche-slug> naming | A spec branch is the branch a tranche's spec edits land on, named `spec/<tranche-slug>`. The branch existing, with commi |
| R0006 | (none) | stays | pruned: drop 'tranche' | An open spec delta is the interval during which a tranche's spec branch carries edits the default branch does not; the b |
| R0007 | all | stays | human edits spec freely while delta open | While a spec delta is open, the human edits its spec documents freely — no reviewer gate, no per-edit ceremony. ## Human |
| R0008 | cos | retired | successor: none (tranche retires) | Bound every spec delta to its tranche; a delta never spans two. |
| R0009 | (none) | stays | lexicon: reconciliation survives (R1490 is the duplicate) | Reconciliation is the close of an open spec delta: the spec is brought to full agreement with what was actually built. |
| R0011 | all | stays | agreement attaches at reconciliation | Attach agreement at reconciliation, to the version of record on the default branch; never to a revision the spec branch  |
| R0012 | (none) | retired | successor: none (only R0013 uses 'claimed') | A spec document is claimed when it appears in an open delta's diff. |
| R0013 | cos | retired | successor: none (one SPEC.md; no concurrent spec territory) | A document claimed by one open delta is not claimed by a second; keep concurrent deltas over disjoint spec territory. |
| R0017 | cos,coder | stays | no build against an unapproved spec; gate | Implement nothing against an open spec; implementation waits on the spec closing agreed. |
| R0021 | all | stays | evidence classes survive (SPEC s4) | Carry exactly one evidence class on every verification claim: mock-verified, contract-verified, live-verified, browser-v |
| R0022 | (none) | stays | duplicate of R0131; keep one | Mock-verified means checked against controlled or simulated inputs. |
| R0023 | (none) | stays | duplicate of R0133; keep one | Contract-verified means checked against a documented or encoded interface contract. |
| R0024 | (none) | stays | duplicate of R0135; keep one | Live-verified means checked against a real external system or deploy-like service. |
| R0025 | (none) | stays | duplicate of R0137; keep one | Browser-verified means checked in a real browser environment. |
| R0026 | (none) | stays | duplicate of R0139; keep one | Production-verified means checked through deployed telemetry, monitoring, synthetic checks, logs, or other real producti |
| R0027 | (none) | stays | lexicon survives | Unverified means known but not yet checked. |
| R0028 | (none) | stays | lexicon survives | Deferred means intentionally postponed with a named future mechanism — as an evidence class, deferred verification; as a |
| R0029 | (none) | stays | lexicon survives | Accepted risk is an explicit decision — the human's, or the release process's — to proceed despite a known gap. |
| R0030 | all | stays | judgment | Mark every known, unresolved boundary gap with one of the four release-impact labels — `blocking`, `deferred`, `accepted |
| R0031 | (none) | stays | lexicon survives | A `blocking` gap is one the governing policies prohibit releasing with. |
| R0032 | all | stays | judgment | Resolve a gap labelled `blocking` before release. |
| R0033 | all | stays | judgment | A gap awaiting the human's judgment is not blocking by that fact alone: label it by its release impact, and let it reach |
| R0037 | (none) | stays | lexicon survives | A `not-material` gap is known but not relevant to the release decision. |
| R0038 | (none) | stays | writing-corpus term in lexicon; untouched | Claim strength is how firmly a sentence in public prose may assert — relayed, demonstrated, grounded, opinion. It is a p |
| R0040 | (none) | stays | lexicon survives | Provenance class is where an assertion came from — observed, inferred, told, unknown, the four classes Core names. |
| R0043 | (none) | stays | pruned: model tier -> agent model: field; claim tier is writing | A model tier is frontier, solid general-purpose, or cheap. A claim tier is one of the four claim-strength tiers. The wor |
| R0044 | all | stays | pruned with R0043 | When you write "tier", say which axis you mean — model tier or claim tier. |
| R0045 | (none) | stays | pruned: 'as the PRD lists them' -> SPEC.md | Top K is the K most important user journeys of a product, as the PRD lists them; a requirement stated for "Top K journey |
| R0046 | arch,cos,specrev | retired | successor: SPEC.md (one document; no PRD/TRD split) | Define the Top K list once, in the PRD; the TRD sets SLO targets against that list and does not redefine it. |
| R0054 | (none) | retired | no successor; skill takes the harness meaning | What a session loads as standing context is a context set, a role document, a skill document, a policy, or a boundary do |
| R0055 | (none) | stays | pruned: drop decomposition doc; spec = SPEC.md | What a session derives work from is the decomposition doc, a change package, the acceptance criteria, or the spec — the  |
| R0057 | (none) | stays | lexicon survives | An approval prompt is a tool interrupting to ask a human to authorise a step; in that domain the word keeps its ordinary |
| R0058 | all | retired | successor: none (directive vocabulary) | For the act of giving a directive to an execution session, write "hand the directive to an execution session", or "direc |
| R0060 | cos | retired | successor: command-blocks (nothing-before-the-block invariant moves there per SPEC s7) | Nothing precedes the execution block in a directive: the executor fetches as its first act. |
| R0064 | (none) | stays | lexicon survives | Track, tracking and tracker keep their ordinary meaning where they mean keeping or consulting a record — a loose-end tra |
| R0604 | (none) | stays | lexicon survives | A document's version, at the moment it is referenced, is the SHA of the last commit that touched the file. |
| R0611 | (none) | stays | reworded: the verb is approved; swap applied store-wide | Something is agreed when the human has agreed it. Agreed is the repo's standing verb for that act; no other word carries |
| R0757 | (none) | retired | successor: SPEC.md / spec-template.md | The PRD is the standing product specification: canonical for what is being built and why, at the top of the spec spine a |
| R0758 | (none) | retired | successor: SPEC.md / spec-template.md | The TRD states technical design and is canonical for how. |
| R0759 | (none) | stays | pruned: derived from the spec | Acceptance criteria are derived from the PRD and owned by the human. |
| R0760 | (none) | stays | pruned: the plan; drop 'derived from the TRD' | An architecture summary is scoped to one unit of work, derived from the TRD, and produced by the Architect Agent; it is  |
| R0761 | (none) | stays | lexicon survives | A tracker issue is a derived PM artifact that tracks and organizes work — a view onto the specs, never an independent so |
| R1601 | (none) | stays | lexicon survives | A known gap is a place where the evidence for a change stops short of what the release claims: an unverified behavior, a |
| R0083 | (none) | stays | red gate survives (SPEC s7) | A red-gate is a test run that fails on wrong behavior. A run that fails only because the module under test does not exis |
| R0580 | (none) | stays | lexicon survives | A DEC ID is a decision's resolvable handle: searching it in `decisions/log.md` lands on the entry that records the decis |
| R0594 | (none) | stays | lexicon survives | A recorded decision is live until a later entry's `Supersedes:` names its ID. |

## prd-template

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1513 | cos,specrev | stays | pruned: merge with R1542 into one row on an unapproved SPEC.md | Never act on a PRD the human has not agreed: the PRD owns product intent, it is his document, and it is not in force unt |
| R1533 | cos,specrev | stays | duplicate of R0472/R0759; keep one | Derive per-unit acceptance criteria from the PRD, whether they live in the PRD itself or in the unit's own artifact. |

## public-prose-criteria

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0817 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Write so that comprehension never depends on native-English-only cues. |
| R0818 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Quote speech rather than introducing it with a bare colon. |
| R0819 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Make every line carrying irony, wordplay, or idiom read correctly for a reader who takes it literally. ## Human The play |
| R0820 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Never simplify or alter the register — not to make a line read literally, and not for discoverability. |
| R0821 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Signal each claim's tier in the sentence: relayed, demonstrated, grounded, or opinion. |
| R0829 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Define each governed or specialist term where it first appears, for a public reader; where the audience includes readers |
| R0830 | wr,ce,crit | out-of-scope | writing corpus; not sorted | When an industry-standard term exists for a concept the piece names differently, flag the mismatch to the author, who de |
| R0831 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Anonymize by default, in both directions: name criticized practices, not the companies, products, or people, and be as s |
| R0832 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Name a party only where there is a clear benefit in that instance, and state the benefit when proposing it. |
| R0833 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Credit the known author of an idea, technique, phrase, or finding unless the work is trivial; anonymizing targets and ex |
| R0835 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Say each point once; cut restatements. Length and structure are the author's call per piece. |
| R0844 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Land every piece clean for a cold reader; build across pieces is allowed. |
| R0845 | (none) | out-of-scope | writing corpus; not sorted | An explicitly declared series says up front which part of how many a piece is, and may assume its predecessors. |
| R0846 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Prefer descriptive, searchable titles over clever ones, place key terms early, and keep the structure skimmable. |
| R0849 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Write venue-independent prose, with no platform-specific formatting dependencies. |
| R0853 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Treat each of these AI prose-smell tells as a defect wherever it appears: "load-bearing"; em-dash cascades, though a pai |
| R0854 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Propose any new AI prose-smell tell to the author; never add one to the list yourself. |

## release-manager-agent

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1031 | rm | harness:agent | release-manager description: recommendation only, decision is the human's | From the assembled release evidence, produce a ship/no-ship release recommendation. The recommendation is what you produ |
| R1032 | rm | harness:skill | release skill: package assembly template | When assembling a release package, collect the change summary, the test evidence, and the review evidence; check the ver |
| R1039 | rm | harness:skill | gate-request skill: check human-gate issue open and linked | Before presenting a consequential change to the human, confirm its `human-gate` tracker issue is open and linked. |
| R1041 | rm | harness:skill | release skill: readiness-review template (eleven items) | A release readiness review states eleven items: the change summary; user-visible behavior; test evidence; review finding |
| R1042 | rm | harness:skill | release skill: assemble from change package | Assemble each item of the release readiness review from the change package wherever the change package states it; do not |
| R1044 | rm | harness:skill | release skill: missing item -> known gap | Where a required item of the release readiness review has no source at all, say so rather than filling the slot, and car |
| R1045 | rm | harness:skill | release skill: recommendation enum | State the release recommendation as exactly one of: ship; ship with accepted risks; do not ship; needs the human decisio |
| R0502 | rm | harness:skill | release skill: change-package template | A meaningful change produces a change package: intent, acceptance criteria, test plan, implementation summary, test resu |
| R0503 | rm | harness:skill | release skill: test plan / test results fields | In a change package, the test plan is the unit's tests selected from the spec's suite, together with the review artifact |
| R0505 | rm | harness:skill | gate-request skill: reference the issue in the package | Where the change is consequential, reference its `human-gate` tracker issue in the change package. |
| R0506 | rm,rev,skep | harness:skill | review/release skill: report shape (role, intent, evidence, boundary, gaps, rec, decisions) | Reporting substantial implementation, review, or release work, state role, intent, evidence, boundary, gaps, recommendat |
| R0509 | rm | stays | definition of done for a change; judgment | Call a change done only when all of this holds: the intended behavior is implemented; the mechanical checks pass; the re |
| R0527 | rm,cos | stays | judgment | Escalate for human code inspection when the change is security-sensitive, the system handles private data, release risk  |

## remote-write-verification-policy

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0720 | arch,cos,coder,cqr,rm,rev,skep,specrev,td | harness:hook | PostToolUse on git push: fetch and print the remote SHA; successor R0172 | The repository's log is the record of what landed. After any remote write, read it back from the fetched remote before r |
| R0730 | cos | stays | connector write recovery; judgment | After a write that timed out or came back unconfirmable, read state before anything else: landed — continue from it; not |
| R0725 | cos | stays | judgment | A second consecutive failure of that kind is a signal, not a retry: stop and establish state. Auth errors, not-found, an |

## retro

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1237 | cos,wr,ce,crit | stays | judgment | Ground every retro in concrete evidence from the conversation it covers. ## Human The retros form a per-project corpus f |
| R1241 | cos,wr,ce,crit | stays | judgment | Carry into a retro what is durable and new: the techniques, workflows, belief changes, and engineering practices that tr |
| R1244 | cos,wr,ce,crit | stays | narrowed to its input half; the write prohibition drops (ruling 2026-11-03) | While producing a retro, read nothing from and write nothing to any remote, GitHub included; every input is the conversa |
| R1246 | cos,wr,ce,crit | retired | successor: the retro skill lands the retro (ruling 2026-11-03) | Hand the finished retro to the human as one Markdown file in the chat that produced it — a downloadable artifact where t |
| R1249 | cos,wr,ce,crit | stays | judgment | Answer in every retro, explicitly, which preferences the human stated this session that he has also stated in earlier se |
| R1270 | cos,wr,ce,crit | stays | judgment | Phrase a methodology change a retro or synthesis proposes as a finding for the delta it feeds — intake for a rules delta |

## review-artifact-schema

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1395a | specrev,cqr,rev,skep,rm,cos | retired | successor: subagents (reviewer subagent writes the artifact); R1396 | Write the review artifact in the execution session that runs the review. |
| R1395b | specrev,cqr,rev,skep,rm,cos | retired | successor: subagents (decision session triages in-session); R1614 | Triage a review artifact's findings in a decision session. ## Human The two halves bind opposite sides of the flow: the  |
| R1396 | specrev,cqr,rev,skep,rm,cos | stays | one artifact per review; judgment on scope | Emit exactly one artifact in this schema per review — one read over one delta, one artifact — whatever the review proced |
| R1414 | arch,cos,cqr,ce,crit,rm,rev,skep,specrev | harness:hook | PostToolUse Write reviews/*.md: Verdict lines present, enum-valued, overall = most severe | Carry one overall `Verdict:` line in a review artifact's header and one `Verdict (<pass>):` line at the head of each pas |
| R1408 | specrev,cqr,rev,skep,rm,cos | harness:deny | deny Edit/Write on existing review artifacts (reviews/** path); records are immutable | Never rewrite an existing review artifact to match a later version of this schema; the schema binds artifacts written af |
| R1448 | cos,wr,ce,crit | stays | rule by class; judgment | Where a review artifact names a defect class and lists its instances, rule on the class once and dispose the instances u |
| R1450 | cos,wr,ce,crit | stays | judgment | Route a finding below the reviewed document's stage — a PRD read raising a TRD question, a spec read raising an implemen |
| R1614 | specrev,cqr,rev,skep,rm,cos | stays | judgment; file-and-land default | A non-blocking finding's disposition at triage is file-and-land by default: it goes to the loose-end tracker and the del |

## reviewer

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1047 | rev | stays | judgment; /code-review candidate when a standard is adopted | Review a change in one pass over the whole of it — all files, the test plan, the diff and the boundary updates together  |
| R1048 | rev | stays | judgment checklist | In the review pass over a change, check: - correctness; - the change against the spec it implements, reporting where the |
| R1054 | rev | stays | judgment | State in the review what was checked and what was not checked. ## Human A review is only useful if its scope is legible: |
| R1055 | rev | stays | judgment | Do not submit a review whose whole content is a bare verdict — looks good, tests pass, implementation matches spec, no i |
| R1056 | rev | harness:agent | reviewer description: scope excludes spec documents | Do not review spec documents; they are the Spec Reviewer's. Your review covers implementation quality and consistency. # |
| R1496 | rev | stays | judgment | When reviewing a test plan, take as inputs the spec, its acceptance criteria, the proposed test plan, the affected bound |
| R1497 | rev | stays | judgment | Review the test plan when tests are written before implementation, when a spec-first or TDD plan is under review, and wh |

## skeptic

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1058 | skep | stays | judgment | Ask what confidence is being inferred that the evidence does not actually support, assuming the evidence you are given c |
| R1068 | skep | stays | judgment | Raise a risk as a finding and leave the weighing to the release decision: reserve `blocking` for a gap the governing pol |
| R1073 | rev,skep,rm | stays | judgment | When reviewing implementation output, reviewing test results, preparing a release, or deciding whether the human needs t |
| R1077 | skep | stays | judgment | Flag any statement equivalent to one of these: coverage proves correctness; the fixture matches reality because it worke |
| R1088 | skep | stays | judgment | Judge a gap's severity against the change's declared verification boundary, not against any list of examples. |
| R1090 | skep | stays | judgment | Raise as a finding manual verification standing in where the spec or test plan specified automation, and monitoring belo |
| R1091 | skep | stays | judgment | Do not raise as a finding work that conforms to the minimum acceptable practice the testing and verification context set |
| R1094 | rev,skep,rm | stays | judgment | Output your findings with their labels and a recommended next step, never a ship call: the ship call is the Release Mana |

## spec-reviewer-agent

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1101 | specrev | retired | successor: R1107 (one read before the human approves SPEC.md); two-point timing retires | Read a spec at exactly two points: the entry read, when the branch opens and before the Test Designer starts, and the cl |
| R1104 | specrev | stays | pruned: one document, internal consistency scan | At a spec delta's close, run a Depth 1 continuity scan over the spine — PRD, TRD, acceptance criteria: does the TRD answ |
| R1105 | specrev | stays | judgment | Widen the continuity scan to the delta's reach: where the delta's diff touches a boundary or policy document, run Depth  |
| R1106 | specrev | retired | successor: subagents (decision session spawns the reviewer); R1107 | Run the close's read when an open spec branch's text and tests cohere, on the decision session's directive, before the h |
| R1107 | specrev | stays | reworded for SPEC.md sections | In the entry read, confirm: - every required section is present and substantively answered; - the document is internally |
| R1116 | specrev | stays | pruned: PRD sections -> SPEC.md sections | In the entry read, confirm, of a PRD: - its functional goals are concrete outcomes rather than feature lists; - every NF |
| R1122 | specrev | stays | pruned: TRD sections -> SPEC.md design section | In the entry read, confirm, of a TRD: - every component has a named responsibility and lists its interfaces; - every ext |
| R1126 | specrev,cos | retired | successor: SPEC.md definition of done + R0083 red gate + R1396 | At the close, in one read by the role that gated the spec: - read the spec branch's whole diff, from the branch point to |
| R1133 | specrev | stays | judgment | In a continuity scan report only inconsistencies and contradictions, flagged for the human to resolve; where a fix for o |
| R1137 | specrev | stays | judgment | Run a Depth 3 sweep over everything — the spec spine and the rules store — asking only whether anything contradicts anyt |

## test-designer

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1141 | td | harness:agent | test-designer description | Define how correctness will be evaluated, and what evidence it requires, before implementation begins. |
| R1143 | td | stays | judgment | When designing the test plan: - derive the test cases from the acceptance criteria and from the spec's testable claims;  |
| R1151 | td | stays | judgment | Mark each gap the test plan leaves open with its release-impact label. |
| R1153 | td | stays | duplicate of R0017; keep one | Implement nothing against an open spec; while its branch is open it takes tests and nothing else. |
| R1155 | td | stays | pruned: 'through the decision session' -> 'as a finding' | Where a test cannot be derived — the spec leaves a contract unstated, or a claim untestable — file a spec finding throug |
| R1156 | td | harness:hook | PreToolUse path guard; finding sentence into test-designer agent definition (class 9) | A Test Designer edits tests and nothing else; a spec change it needs is a finding to the decision session. |
| R1158 | td | retired | successor: R0083 (red gate result is evidence); suite-at-close retires | Hand the red-gate result to the spec delta's close as its evidence for the tests. |
| R0085 | td | retired | successor: SPEC.md design section (stage 3 / TRD retire) | Take the interface contract for a spec's test suite, written at stage 3 while the spec branch is open, from the TRD's st |
| R0086 | td | retired | successor: plan (R0862b); stage numbering retires | Take the interface contract for a unit's tests at stage 7 from the architecture summary produced at stage 6. ## Human DE |

## trd

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1541 | arch | retired | successor: SPEC.md written by interview (SPEC s3) | As the Architect Agent, draft the project's TRD. |
| R1542 | arch,specrev | stays | pruned: merge with R1513 into one row on SPEC.md | Never act on a TRD the human has not agreed: it is in force only from her ruling, recorded in the decision log naming th |
| R1543 | arch | stays | pruned: update SPEC.md design section; duplicate of R0876 | When a change you hold the Architect role for alters standing architecture, update the TRD as part of that change. |
| R1573 | arch,specrev | stays | judgment | Prefer boring, understandable designs. |
| R0862b | arch,cos | stays | pruned: the plan; drop 'in an execution session' (plan mode) | For a meaningful change, produce a per-change architecture summary in an execution session, naming affected components,  |
| R0863 | arch | stays | kept: reworded to the spec design section (class 6 amended) | When drafting or updating the TRD, design the system's technical structure and define its important boundaries: - propos |
| R0871 | (none) | retired | successor: SPEC.md design section | The standing TRD is the durable, slow-moving technical specification the Architect drafts and the human agrees; it chang |
| R0872 | arch | retired | successor: none (drafting by interview) | Take responsibility for every section of the TRD you draft. |
| R0876 | arch | stays | duplicate of R1543; keep one | When a change alters standing architecture, update the TRD and keep it consistent across every affected section. |
| R0497 | (none) | stays | lexicon survives | Deploy is code on prod; release is functionality exposed to users. The two may be separate events. |
| R0499 | arch | stays | judgment | Where deploy and release are separate events, separate them with feature flags or canaries. |
| R0500 | arch | stays | judgment | When a feature flag is introduced, depend on a vendor-neutral flag interface — so the flag backend stays a swappable per |
| R0501b | arch | stays | judgment | Track a stale flag as debt and clean it up. |

## verification

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0108 | (none) | stays | judgment | A test executes a controlled scenario; verification is the confidence claim drawn from that evidence. Testing and verifi |
| R0110 | td,coder,rev,skep,rm,cos | stays | judgment | State the boundary of every verification claim you make — what the evidence behind it covers, and where that coverage st |
| R0111 | td,coder,rev,skep,rm,cos | stays | judgment | Claim only what a test actually proves. A passing test, a green suite, or a small test licenses no claim wider than the  |
| R0112 | td,coder,rev,skep,rm,cos | stays | judgment | Never treat a test that passes before the implementation it covers exists as a head start: it is a broken test, and fixi |
| R0113 | td,coder,rev,skep | stays | duplicate of R0485; keep one | Once the tests are confirmed failing, implement only as far as needed to turn them green. |
| R0114 | td,coder,rev,skep | stays | judgment | Make every mock's boundary visible: what production behavior it represents, what the test verifies, what it does not ver |
| R0121 | td,coder,rev,skep | stays | judgment | Choose the smallest test that produces the evidence the claim needs. |
| R0123 | td,coder,rev,skep | stays | judgment | Test deterministic logic with unit tests. |
| R0124 | td,coder,rev,skep | stays | judgment | Test UI behavior with component tests. |
| R0125 | td,coder,rev,skep | stays | judgment | Test combined local components with integration tests. |
| R0126 | td,coder,rev,skep | stays | judgment | Test external assumptions with contract tests; what they produce is a contract-verified claim. |
| R0127 | td,coder,rev,skep | stays | judgment | Test real external services with live smoke tests; what they produce is a live-verified claim. |
| R0128 | td,coder,rev,skep | stays | judgment | Test browser-only behavior with browser or E2E smoke tests; what they produce is a browser-verified claim. |
| R0129 | td,coder,rev,skep | stays | judgment | Check ongoing health with production synthetic checks or monitoring; what they produce is a production-verified claim, a |
| R0130 | td,coder,rev,skep | stays | judgment | Make error budget consumption observable from the production checks. |
| R0131 | (none) | stays | duplicate of R0022; keep one | Mock-verified evidence supports application logic, parsing, error handling, UI state, edge cases, retry behavior, and fa |
| R0133 | (none) | stays | duplicate of R0023; keep one | Contract-verified evidence supports fixture shape, schema expectations, required fields, API assumptions, and compatibil |
| R0135 | (none) | stays | duplicate of R0024; keep one | Live-verified evidence supports credentials, provider availability, auth shape, live response shape, real status codes,  |
| R0137 | (none) | stays | duplicate of R0025; keep one | Browser-verified evidence supports rendering, layout, map and tile loading, service worker and PWA behavior, browser-onl |
| R0139 | (none) | stays | duplicate of R0026; keep one | Production-verified evidence supports ongoing dependency health, real-world failure modes, regressions after deploy, ava |
| R0140 | td,coder,rev,skep,rm,cos | stays | judgment | Treat a verification claim made against an exhausted or critical error budget as materially weaker than the same claim m |
| R0141 | td,coder,rev,skep,rm,cos | stays | judgment | A production-verified claim states which SLO was checked and its current status — healthy, degraded, or exhausted — the  |
| R0144 | td,coder,rev,skep,rm,cos | stays | judgment | A production-verified claim never stands in for pre-deploy checks on a known high-risk path; run those checks as well. |
| R0145 | td,coder,rev,skep,rm,cos | stays | judgment | For a meaningful change, be able to produce a confidence ledger — for each claim, the evidence, the boundary that eviden |
| R0147 | td,coder,rev,skep,rm,cos | stays | judgment | A test plan for a meaningful change states acceptance criteria, behaviors under test, test levels used, mocked dependenc |
| R0148 | td,coder,rev,skep,rm,cos | stays | judgment | Treat these areas as boundary-sensitive by default: external APIs; auth and authorization; environment variables; per-cl |
| R0150 | (none) | stays | judgment | Boundary-sensitive means do not overclaim here. It does not mean the area must be overtested. |
| R0151 | td,coder,rev,skep | stays | judgment | When you write or review tests, state what is verified, what is not, what is mocked, what assumptions the fixtures encod |
| R0152 | td,coder,rev,skep | stays | judgment | On a small project or early-stage feature, keep: - fast mocked and unit tests; - at least one live or browser smoke test |
| R0156 | td,coder,rev,skep | stays | judgment | A headless DOM is not browser rendering; never report one as the other. |
| R0157 | td,coder,rev,skep | stays | judgment | Agent review counts as evidence only where you state what was reviewed; unstated review is not evidence. |
| R0158 | td,coder,rev,skep | stays | judgment | Know what assumptions a fixture encodes before you rely on it. |
| R0159 | td,coder,rev,skep | stays | judgment | Keep live tests out of the unit run; run them deliberately instead. |
| R0161 | td,coder,rev,skep,rm,cos | stays | judgment | Judge verification by boundary analysis, never by line coverage: coverage shows that code executed, not that it was veri |
| R0070 | td,coder,rev,skep | stays | judgment | For a change meant to be production-grade, decide explicitly which of these attributes are relevant to the change in han |
| R0073 | td,coder,rev,skep | stays | judgment | Support a production-grade claim with evidence: passing unit and integration tests, live and browser smoke tests, contra |
| R0074 | td,coder,rev,skep,rm,cos | stays | judgment | Every meaningful change answers: what happens if it fails; how the failure would be known, including whether it hits a T |
| R0531 | (none) | stays | judgment | Production-grade software is intentionally specified, verified to declared boundaries, operationally supportable, observ |

## verification-boundaries

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R0780 | (none) | stays | judgment | A verification boundary is the point where evidence stops — the line between what has been checked and what is merely as |
| R0781 | arch,cos,coder,rm,rev,skep,specrev,td | stays | judgment | Give every meaningful mock, stub, fake, fixture, simulated service, generated response, assumed external behavior, brows |
| R0782 | (none) | stays | judgment | A mock is a claim about our side of the contract, with the other side verified elsewhere or explicitly accepted as unver |
| R0783 | arch,cos,coder,rm,rev,skep,specrev,td | stays | judgment | Do not let a test imply broader confidence than it actually supports. |
| R0784 | arch,cos,coder,rm,rev,skep,specrev,td | stays | judgment | State in a boundary declaration its boundary name, production surface, representation mechanism, verification class, ver |
| R0785 | (none) | stays | judgment | Common boundary types are mocked HTTP APIs, browser APIs, storage, authentication, authorization, time, geolocation, ser |
| R0789 | arch,cos,coder,rm,rev,skep,specrev,td | stays | judgment | Create or update a boundary declaration when you add a mock, change a fixture for external data, add or change an extern |
| R0798 | arch,cos,coder,rm,rev,skep,specrev,td | stays | pruned: TRD section -> SPEC.md design section | Put boundary information in one of these: the project TRD's standing verification boundary section, a feature-specific v |
| R0799 | arch,cos,coder,rm,rev,skep,specrev,td | stays | pruned: TRD section -> SPEC.md design section | Declare durable or repeated boundaries in the project TRD's standing verification boundary section or verification ledge |
| R0800 | coder,td | stays | judgment | Keep the default unit suite fast and deterministic, with live and browser checks outside it. |
| R0802 | arch,cos,coder,rm,rev,skep,specrev,td | stays | judgment | Choose when a boundary's verification runs — manually before release, in a dedicated CI job, on a schedule, or after dep |
| R0803 | arch,cos,coder,rm,rev,skep,specrev,td | stays | judgment | Verify a boundary material to user-visible behavior or release risk before release. |
| R0804 | arch,cos,coder,rm,rev,skep,specrev,td | stays | judgment | Verify a boundary that can drift after deployment by production monitoring. |
| R0807 | rev | stays | judgment | When reviewing a change, check whether its verification boundaries are named and documented. |
| R0809 | rm | stays | judgment | Before release, put every material verification boundary in one of four states: verified by an appropriate mechanism, ex |
| R1178 | rev,skep,rm | stays | judgment | In a boundary audit, identify where the system's tests, mocks, tools, or assumptions stop proving production behavior: - |
| R1179 | rev,skep,rm | stays | judgment | Run a boundary audit when you add or change a mock or an external integration, when you change auth, config, or deployme |
| R1183 | rev,skep,rm | stays | judgment | Run a boundary audit when you investigate a surprise production or manual failure, and when you verify that the SLO targ |

## voice

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1577 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Write for adopters, peers, and potential clients, toward establishing thought leadership; when the goal shifts toward dr |
| R1579 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Write in one voice, Dave's — not a house style, not a persona. The test is whether it reads as Dave. |
| R1585 | wr,ce,crit | out-of-scope | writing corpus; not sorted | When a draft reads thick, fix it with a terse pass that moves the story forward rather than with line-level trimming, an |
| R1587 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Flag, rather than cut, mirrored two-sentence pairs and a closing contrast pair: they are structure, not restatement. |
| R1588 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Give a reason for a second closing contrast pair in a piece. |
| R1591 | wr,ce,crit | out-of-scope | writing corpus; not sorted | When cutting for budget, keep the first and last statements of a rising-specificity repetition and cut the middle one. |
| R1594 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Use the methodology's own governed vocabulary, and define each term at first use. |
| R1598 | wr,ce,crit | out-of-scope | writing corpus; not sorted | When a piece discusses a methodology mechanism, link the canonical document in the public repository `davepierceops/fidu |
| R1600 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Disclose LLM use once, at site level: list LLMs among the writing tools alongside the dictionary and the public school e |
| R1604 | wr,ce,crit | out-of-scope | writing corpus; not sorted | Read the Voice document before you write, edit, or read the piece, every time. |

## writer

| id | role(s) | sort | replacement / note | body (first 120 chars) |
|---|---|---|---|---|
| R1162 | wr | out-of-scope | writing corpus; not sorted | When a document this role names is absent from your context, ask the author for it before acting on anything it governs, |
| R1163 | wr | out-of-scope | writing corpus; not sorted | Draft what the author asks for — a braindump capture, an arc, an outline, a section, a whole piece, a rewrite of any of  |
| R1164 | wr | out-of-scope | writing corpus; not sorted | When the author asks for an outline, produce it in the shape the bundle's Outline skill sets. |
| R1165 | wr | out-of-scope | writing corpus; not sorted | Put the draft in the document pane and keep the discussion in chat. |
| R1167 | wr | out-of-scope | writing corpus; not sorted | Treat the author's edits to the draft as the current text. |
| R1168 | wr | out-of-scope | writing corpus; not sorted | When an author's edit shows a rule the Voice document does not state, propose the line that would state it, in chat, and |
| R1169 | wr | out-of-scope | writing corpus; not sorted | When the author says the piece, section, or outline is done, state that a Copy Editor pass and a Critic pass are availab |
| R1171 | wr | out-of-scope | writing corpus; not sorted | When the author says the work is done, emit the voice harvest — one paste block, one line per rule this session showed t |
| R1173 | wr | out-of-scope | writing corpus; not sorted | Leave the piece to the author: keep the record in the author's own document rather than in anything you write, and leave |
| R1174 | wr | out-of-scope | writing corpus; not sorted | Never share a session with the Copy Editor or the Critic, and never run their passes on your own draft. ## Human DEC-000 |
| R1176 | cos | out-of-scope | writing corpus; not sorted | Run the Writer at the frontier tier. |

## Classes for ruling

The human rules by class (R1448). Each class names its rows and the one-sentence rule that disposes of all of them. Rows not in any class are `stays` (judgment) or `out-of-scope`.

### 1. Directive-package rows -> retired, successor none (docs/history)

- Rows: R1302 R1304 R1305 R1306 R1307 R1308 R1310 R1311 R1312 R1313 R1314 R1340 R1341 R1344 R1347 R1350 R1286 R1287 R1288 R1289 R1290 R1291 R1292 R1293 R1298 R1608 R1610 R1615 R0212 R0058 R0256 R0060
- Rule: Every row that exists to shape, lint, route, or verify a directive retires with the package; the two execution-block invariants (self-contained, nothing before the block) are restated once under command-blocks, and the route/model line becomes the agent `model:` field (R0259).

### 2. Worktree choreography -> retired, successor subagent worktrees

- Rows: R1295 R1296 R0199
- Rule: Subagents run in harness-managed worktrees, so holder checks, removal steps, and the shared-clone mutation stop are the harness's; R0199 is already redundant (harness:native).

### 3. Execution-session courier rows -> retired, successor subagents

- Rows: R0896 R0474 R1476 R1478 R1479 R1480 R1395a R1395b R1106
- Rule: Where a row exists only because the human carried reports, findings, or dispositions between a decision session and an execution session, it retires: the decision session spawns the subagent and reads its report in-session.

### 4. Spec-test-suite / convergence rows -> retired, successor SPEC.md definition of done + red gate

- Rows: R1468 R1473 R1474 R1126 R1158 R0470 R1101 R0085 R0086 R0483
- Rule: The spec-branch test suite, its coherence check, its entry/close choreography, and its stage numbering fold into SPEC.md's definition of done, the red gate (R0083, R0112, R0478), and plan mode; the judgment rubrics (R1107, R1116, R1122, R1143) stay reworded for one document.

### 5. Tranche-bound spec-delta terms -> retired, successor none

- Rows: R0003 R0008 R0012 R0013 R1490 R1491
- Rule: With one SPEC.md per project there is no tranche and no concurrent spec territory; the open-delta model itself (R0004, R0006, R0007, R0009, R0011, R0017) stays, pruned of the word.

### 6. PRD/TRD two-document rows -> retired, successor SPEC.md / spec-template.md

- Rows: R0757 R0758 R0871 R1541 R0872 R0863 R0046 R0561
- Rule: A row that names the PRD or TRD as a document, or who drafts it, retires into spec-template.md; a row that names what the spec must say or who may act on it stays, reworded to SPEC.md (R1513, R1542, R1543/R0876, R0798, R0799, R0045, R0759).

### 7. Secret and production handling -> deny rules

- Rows: R0164 R0203
- Rule: No agent reads a credential file or runs an apply/deploy/production command: `settings.json` permissions deny (Claude Code) and a PreToolUse hook (Codex); the one-line principle stays in CLAUDE.md.

### 8. Git and record immutability -> deny rules / PreToolUse hooks

- Rows: R0564 R0583 R1408
- Rule: Force-push is denied; edits to `decisions/log.md` must be append-only; existing review artifacts are not writable — each is a byte-level check on the tool call.

### 9. Path-scoped subagent write guards -> PreToolUse hooks

- Rows: R0091 R1156
- Rule: A role that may edit only one artifact class (spec-revision: specs/; test-designer: tests) gets a PreToolUse Edit/Write hook keyed on the agent, replacing the 'edit X and nothing else' prose.

### 10. Store and artifact lint -> PostToolUse/Stop hooks

- Rows: R1605 R0196 R1414 R1613
- Rule: A format or consistency check that a script can decide (citation co-render, generated-file timestamp name, Verdict line enum, untracked retros/) becomes a hook; the rows carry `enforce: hook` per SPEC s7.

### 11. Agent-definition fields -> harness:agent

- Rows: R0259 R0939 R1031 R1056 R1141
- Rule: The model tier becomes `model:` per agent; a row that only states what a role is for, or is not for, becomes the agent's description.

### 12. Gate-request procedure -> harness:skill

- Rows: R0551 R0552 R0553 R0558 R0560 R1039 R0505
- Rule: Opening, labelling, deriving, announcing, and checking the human-gate issue is one skill; the judgment of whether a change is consequential (R0535, R0536) stays a row.

### 13. Release-package and report templates -> harness:skill

- Rows: R1032 R1041 R1042 R1044 R1045 R0502 R0503 R0506
- Rule: A row that enumerates a document's or report's required fields is a form, not a rule, and lives in the release (or review) skill's template; the definition of done for a change (R0509) stays.

### 14. Build, intake, and retro procedure steps -> harness:skill

- Rows: R0486 R1611 R0944 R1244 R1246
- Rule: A step the session runs in a fixed order (read SPEC.md first, spawn separate test-designer and coder subagents, record the intake artifact, keep a retro offline, hand it over as one file) becomes a step of that skill.

### 15. Duplicate pairs -> prune to one row (all `stays`; listed so the ruling covers them)

- Rows: R0485/R0113 R0489/R1031-R1032 R1602/R0006 R0022/R0131 R0023/R0133 R0024/R0135 R0025/R0137 R0026/R0139 R1153/R0017 R1533/R0472-R0759 R1543/R0876 R1513/R1542 R0009/R1490
- Rule: Where two rows define or require the same thing, one source of truth survives (SPEC s4 non-functional goal); which one is the human's call, except R1490 which is already sorted retired to R0009.

### Undecided rows (no guess forced)

| id | candidate A | candidate B | why |
|---|---|---|---|
| R0934 | stays | harness:hook | 'change governed text only through intake or an open delta' is deterministic if 'through intake' means 'on an intake branch' (PreToolUse Edit on rules/** off such a branch); it is judgment if intake is a review, not a branch. Depends on how the intake skill is shaped. |
| R0202 | stays (pruned) | retired | 'Execution session' as a courier concept retires, but SPEC s4 keeps the execution block as a secondary path, and R0208 needs a name for the session that carries one out. Whether the pruned term or a new word ('executor') survives is a vocabulary ruling. |
| R0205 | stays (pruned) | retired | The three-layer vocabulary (decision/execution/shell) still distinguishes a command block from an execution block, but under subagents 'execution layer' may be no more than 'subagent'. Same ruling as R0202. |
| R1606 | stays (pruned) | retired | The rule (dictate intent and acceptance criteria, never a tree fact the executor should derive) is sound judgment for any subagent prompt or plan; its wording is directive-specific. Retire with the package, or keep reworded to 'a plan or subagent prompt'. |
| R0720 | harness:hook | stays | For Claude Code, a PostToolUse hook on `git push` can fetch and compare the remote ref deterministically. For Claude chat connector writes (the incident the row cites) no hook exists and the read-back is judgment. One row may need to split by harness, which SPEC s4 says a row must not do. |

Undecided count: 5.

### Notes for the ruling that are not a class

- R0611 (`agreed`): SPEC s4 adopts Anthropic's 'approve'; the row says no other word carries the act. Reword, do not retire.
- R0054 (`skill document`): collides with the harness word 'skill'; prune or rename when the vocabulary row lands.
- R0038 (`claim strength`): a writing-corpus term that lives in `lexicon`; marked stays and untouched.
- R0493 (`mechanical checks`): the definition stays; 'they pass as part of green' is a natural PostToolUse/Stop hook once an adopting repo names its lint/type commands.
- R0264 (intake criteria): the rubric is judgment, but three criteria (no file path references, keys from existing values, session kind named) are lint-able on rules/*.md and could join class 10.
- R0462, R0065, R0487, R0488: the separation of author and reviewer is achieved in Claude Code by the review skill spawning a fresh subagent and in Claude chat by the subagent tool; the rows stay because the obligation to do so is not something the harness checks.
