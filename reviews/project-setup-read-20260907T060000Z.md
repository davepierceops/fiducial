# Review: process/project-setup.md — process-sweep-read-20260907T060000Z

Verdict: ready-with-findings
Reviewed: process/project-setup.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/project-setup.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names, over all 22 lines, with the one bracketed id — R0564 — resolved to its file under rules/ at the base ref, including its Human note, and both checklist items compared item by item against the baseline.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md; rules/R0564.md's Human note, which carries the two-layer reasoning the sweep cut from the body.
Not inspected: whether the preconditions actually hold on this repository — they live in the forge's configuration and the agent runner's, outside git, and confirming them is the act this document describes, not part of reviewing it. The sweep session's report is not committed on this branch, so the LOSS test's "listed in the sweep report's six intake candidates" limb could not be applied.
Findings: 1 — 0 blocking, 1 non-blocking
The human should inspect: PS-01, which asks who performs the confirmation the document's third sentence orders. The answer is in the role key rather than the text.

## Verdict (citations): ready

The one id resolves and sits on the clause that relies on it. `[R0564]` annotates "A force-push deny in the agent runner", and R0564's body is "Push plainly; never force-push", with a Human note stating the exact arrangement the item describes: "The force-push denial is enforced at two layers — the agent runner's configuration and the forge's branch protection — so that neither a permissive mode nor a credential no local configuration has seen escapes it." That note is also what carries the baseline's cut two-layers paragraph, so the id is doing both jobs — supporting the clause it sits on and standing in for the sentences the sweep cut nearby.

## Verdict (loss): ready-with-findings

See PS-01, which is an attribution thinning rather than a cut obligation. Everything else survives. The precondition definition keeps what it is and when it must be true. Both checklist items keep every sub-item: no force-push, no branch deletion, changes land only through a pull request, no bypass including for administrators, and the last-carries-the-others observation with the "agents may push and merge" clause it licenses. Item 2 keeps the runner deny and the every-permission-mode condition including the modes that skip prompting, which is the baseline's "A deny a permissive mode waives is not a deny" in positive form — the sweep's sixth criterion applied. The three cut passages were checked and are covered: the "Git cannot record them and no hook can enforce them" reasoning survives as "outside git, where no hook can enforce them"; the branch-protection-lives-in-the-forge sentence survives as "in the forge's configuration" on item 1 plus the intro; and the two-layers paragraph is R0564's Human note, cited.

## Verdict (residue): ready

Every sentence is a definition an agent needs to recognize the condition, an act, or an item of the checklist. "The principle" and its bolded thesis are gone, as is the "What this does not decide" section, whose one substantive half — confirm and say so, report rather than work around — was promoted into the intro as an instruction.

## Verdict (keys): ready

`[chief-of-staff]`, unchanged, with `session: [decision]`. The confirming act the intro orders is the Chief of Staff's, which is what the baseline said in the sentence the sweep cut, and no act in the document names another performer. The two preconditions are conditions on a repository rather than acts of a second role.

## Verdict (loadable): ready

The sweep removed both headings and kept both checklist items, so nothing points at a heading that is gone. The document reads as one paragraph and a two-item list, and the list's items are the two things the paragraph says must be true.

## PS-01 — non-blocking
Claim: The sweep merged the human's once-per-repository confirmation and the Chief of Staff's per-session confirmation into consecutive sentences without naming either performer, so the imperative's addressee is no longer stated.
Location: process/project-setup.md:12-15 — "the human confirms them once per repository, before either session kind begins work in it. Confirm they hold and say so; report one that does not rather than working around it."
Evidence: Read by inspection against the diff. The baseline kept the two apart and named both. The human's act was in the framing paragraph: "Confirming them is the human's, once per repository, before either session kind begins work in it." The Chief of Staff's was a separate item under "What this does not decide": "**Whether the repository is ready for work.** The Chief of Staff confirms the preconditions hold and says so; a precondition that does not hold is reported, not worked around." The sweep cut the section that held the second and moved its instruction into the sentence immediately after the first, where the nearest stated subject is the human.
Consequence: An agent reading the two sentences in order is told the human confirms the preconditions, then told to confirm them. The reasonable reading of an unattributed imperative in a governed document is that it addresses the loading agent, which is right; but the alternative reading — that the sentence restates the human's act — is available, and under it a session skips its own check on the ground that the human already did it once. The obligation is not lost, only its subject; `role: [chief-of-staff]` and `session: [decision]` resolve it for a reader who consults the frontmatter.
Fix: Name the subject once — "The Chief of Staff confirms they hold and says so" — or split the two, keeping the human's adoption-time confirmation in its own sentence away from the imperative.
