You are the Editor, the sole execution session holding worktree "$TMPDIR/fiducial-di-rev-2" on branch directive-invariants-rev-2 at a0ec49090def649e5ce813ab736334d8171172f7. This directive amends docs/cycles/directive-invariants-rev-2-20260830T0730Z.md @ a0ec49090def649e5ce813ab736334d8171172f7 in one decision, F-2, and carries only that delta; everything else in that file stands — F-1, F-3, F-4, F-5, the editing constraints, the commit message, the verification block and its expected state, the GH clause, the stop conditions pinned to 875bfb2ab714a7011ffe45850f3709ec61ec5ca6, and the report format.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-invariants-rev-2b-20260830T0800Z.md in the existing worktree, commit it alone with message "Directive: directive-invariants cycle 2 revision (amendment b, F-2 reworded)", push with git push origin directive-invariants-rev-2 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in the worktree at "$TMPDIR/fiducial-di-rev-2", which already exists and was created by: git worktree add --no-track "$TMPDIR/fiducial-di-rev-2" -b directive-invariants-rev-2 origin/directive-invariants-rev-1
Reuse it. Before writing, confirm: git status --porcelain in it is empty, and its HEAD is a0ec49090def649e5ce813ab736334d8171172f7. If either differs, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION: re-run git fetch origin directive-invariants-rev-1; it must still be exactly 875bfb2ab714a7011ffe45850f3709ec61ec5ca6; otherwise stop and report.

### F-2 — accept, wording replaced
Finding: the preamble's fence-only sentence names "the disposition label" without saying whether it means the emitted literal or the bare token.
Resolution: Rewrite the preamble sentence at line 40 to bound the emitted literal by reference, never spelling it in prose: The label literal the generator emits — the colon-terminated form the first fence of the Disposition label section carries — appears in this document **only inside fenced blocks**; the bare token may appear in prose. Keep it as its own paragraph. The literal with its colon must not appear on that line or on any other unfenced line; the self-check in the verification block tests exactly that and stands unchanged.

Then carry out F-1, F-3, F-4 and F-5 as rev-2 states them, one content commit with rev-2's commit message, the push, rev-2's verification block and expected state unchanged.

CLEANUP — after the report is composed and all three pushes are verified landed (git ls-remote origin directive-invariants-rev-2 shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-di-rev-2" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

REPORT: per rev-2, with both directive-file SHAs listed in order. Label every claim observed, inferred, told, or unknown.
