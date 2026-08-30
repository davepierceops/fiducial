SYNC FIRST: from the main tree, git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/main contains commit d5778195970015e9b65e81f8b3ba4152ab113c3c (git merge-base --is-ancestor d5778195970015e9b65e81f8b3ba4152ab113c3c origin/main exits 0); if not, stop and report. Record origin/main's SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-voice-triage", created after the fetch above by: git worktree add --no-track "$TMPDIR/fiducial-voice-triage" -b voice-inbox-triage-1 origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named voice-inbox-triage-1, stop and report. Do not touch the main tree's checkout. All pushes go to origin voice-inbox-triage-1.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/voice-inbox-triage-20260829T2330.md in the worktree, commit it alone with message "Directive: voice-inbox §4/§5 triage into voice.md and the Criteria", push, and report the SHA.

PRECONDITIONS: voice.md reads status: agreed with last-reviewed: reviews/expedited-log.md @ a7e21331070ed5e554d7482b72a4bc50d57e5437; public-prose-criteria.md reads status: agreed with last-reviewed: reviews/expedited-log.md @ dcb64275d2c69eac7623d3969acf2881343ac4e9; voice-inbox.md's last two sections are headed "## 2026-08-22 — §4 session" and "## §5 harvest — 2026-08-22 (accepted, 262 words)". If any differs, stop and report.

EDIT 1 — voice.md. In the "## Register" section, after the last existing bullet ("- Hacker register is in voice: grok, box."), append these five bullets verbatim, same bullet form and wrap width as the section:

- When a draft reads thick, the fix is a terse pass that moves the story forward, not line-level trimming; the target after a wordy draft is about 10% under budget.
- Sentence fragments are in voice when they land a point; a fragment opener is a baton-turn device, one per section, never the default cadence.
- Mirrored two-sentence pairs and a closing contrast pair are structure, not restatement — flag, do not cut; a second closing pair in a piece needs a reason.
- The flat absolute over the hedged quantifier; hedging a claim Dave can stand behind reads as weaker, not more careful.
- Rising-specificity repetition — the same claim three times, each more concrete — is his rhythm; when cutting for budget keep the first and last, the middle is the candidate.

In the frontmatter, set status: in-review and last-reviewed: null. Change nothing else. Commit voice.md alone with message "voice: Register gains five lines from the §4/§5 harvest (content edit; in-review, doc-only cycle owed)". Read the full SHA with git rev-parse HEAD; call it VOICE_SHA. Push.

EDIT 2 — public-prose-criteria.md. Read the "## Structure and length" section first. Append to it, as its last line in the section's own form (a bullet if the section uses bullets, a sentence if it uses prose), this text verbatim: Cut scene-setting clauses ("when I sit down to build," "from where I sit"); stance carries on the verb. In the frontmatter, set status: in-review and last-reviewed: null. Change nothing else. Commit public-prose-criteria.md alone with message "criteria: cut scene-setting clauses (content edit; in-review, doc-only cycle owed)". Read the full SHA; call it CRITERIA_SHA. Push.

EDIT 3 — voice-inbox.md. Retitle the two sections "## 2026-08-22 — §4 session — triaged 2026-08-29" and "## §5 harvest — 2026-08-22 (accepted, 262 words) — triaged 2026-08-29". Prefix each accepted line with a bracketed target in the file's existing form: §4 lines 1–3 and §5 lines 1, 2, 3, 5 get "[accepted → voice.md] "; §4 line 4 gets "[accepted → public-prose-criteria.md] ". Strike §5 line 4 (the "Accepted unflagged" line) with the file's ~~strike~~ convention and append " (rejected: prose, not criterion)". Change nothing else. Commit voice-inbox.md alone with message "voice-inbox: §4/§5 triaged". Push.

Run bin/check-frontmatter --all from the worktree (must exit 0 — the two documents are in-review with last-reviewed: null, which is the in-review state the policy permits). Do not open a pull request. Never merge anything. Never flip a status.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-voice-triage" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not rebase, do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; VOICE_SHA and CRITERIA_SHA with stats; the inbox commit SHA and stat; the Criteria line as it now reads with its surrounding two lines; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
