AMENDMENT B — prose-criteria-rows. Route: this existing session. Model tier: unchanged.

Worktree: the earlier one was removed. Holder check first — fetch origin prose-criteria-rows, run git worktree list, stop and report if any worktree holds the branch or the path exists — then re-create with the existing local branch: git worktree add "$TMPDIR/fiducial-prose-criteria-rows" prose-criteria-rows. Confirm local prose-criteria-rows equals origin/prose-criteria-rows at 8cd16fed025e264f91fcb7c8fc03cc19b2495cd8; if not, stop and report. Push with: git push origin prose-criteria-rows — no upstream.

First, write this amendment verbatim to docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md, commit it alone with the message "directive: prose-criteria-rows amendment B — intake findings F-1, F-2, F-3", push, and report the SHA.

Triage of reviews/prose-criteria-rows-read-20260909T200000Z.md @ 78b08942a2afa3ac927f11a4fd6fe555bac163da (decision session, 2026-09-09). Read it whole first.

F-1 — accept. R1013's body becomes, verbatim:
Check the piece against every tell in [R0853] and every structure defect in [R0835, R0844, R0845, R0846, R0849], and report each occurrence at its location.

F-2 — accept, modify. R0038's body becomes the body at 28dfdb0 with the phrase "the four tiers the Public Prose Criteria name" deleted along with the comma before it, so the first sentence ends "— relayed, demonstrated, grounded, opinion." The rest is byte-identical. No citation.

F-3 — accept: rows may cite rows by ID, under a constraint that is itself a row. Create R1605 (confirm absent first) in topic intake, order tail-appended, session [decision], corpus and role as the other intake-topic rows carry them (read them; if they disagree among themselves, stop and report), verb require, condition null, term null, source in the form ruled below. Body, verbatim:
A row cites another row only by its ID in square brackets, and only where every value the citing row carries on role, session, and corpus the cited row carries too, so the cited row renders in every bundle the citing one does. A citation that cannot co-render is a defect.

Observations — accept the source: form. R1604's source, and R1605's, take the exact form the two other cycle-sourced rows use — short SHA of the same length, and the line component. R1604 cites docs/cycles/prose-criteria-rows-20260909T190000Z.md @ ca9fd54; R1605 cites this amendment file at the SHA you report for it. O-3 and the trigger observation: received, no action here.

One content commit for F-1, F-2, F-3 and the source: edits, message "rules: intake findings — R1013 cites five structure rows, R0038 drops the citation, R1605 states the row-citation constraint". Push.

VERIFICATION, captured to "$TMPDIR/prose-criteria-rows-amend-b.log": bin/tests/run — expected OK; grep -rn 'R1161\|R0953\|R1001' rules/ process/ — expected no hits; for R1013's six cited rows and R1605, read each cited row's role, session, corpus keys against the citing row's and report whether the constraint holds for every citation; git diff --stat 28dfdb0..HEAD — expected 11 files: three directive files, R1604, R1605, three deletions, R0038, R1013.

Report per the directive's REPORT region, plus R1605's ID confirmation and the per-citation constraint results. Stop conditions of the directive stand. Remove the worktree after the report is composed and every push is verified landed, without force and without retry, and state the outcome as the report's final line.
