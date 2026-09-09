AMENDMENT A — prose-criteria-rows. Route: this existing session, in the retained worktree at "$TMPDIR/fiducial-prose-criteria-rows" on branch prose-criteria-rows. Model tier: unchanged.

First, write this amendment verbatim to docs/cycles/prose-criteria-rows-20260909T190000Z-amend-a.md, commit it alone with the message "directive: prose-criteria-rows amendment A — ID, order, source rulings", push origin prose-criteria-rows, and report the SHA.

Rulings on your three open items (decision session, 2026-09-09):

1. The new row's ID is R1604. bin/next-id does not exist; step 2's reference to it is withdrawn. Allocate by hand: highest ID in the store plus one, and confirm rules/R1604.md is absent before writing it.
2. Order in the voice topic is 240 — tail append. The gap at 20 is not filled.
3. The row carries source: docs/cycles/prose-criteria-rows-20260909T190000Z.md @ ca9fd54dd8a3bb0f84ec7943eb9717ccc870785c, in the same form R1603 writes its source value. Every other key exactly as step 2 lists.

Step 1's IDs stand: tells R0853, structure defects R0835, tiers R0821. Fill D-2 and D-3 with them.

Then resume at step 2 and run through step 7 and VERIFICATION as the directive states, one content commit. Step 6's three observations are received and need no further action from you. Include in the report the post-change bin/tests/run result, the three bundle grep counts, and the diff-stat — expected 7 files now: directive, amendment, new row, three deletions, two edits. Remove the worktree after the report is composed and every push is verified landed, as R1295 states.
