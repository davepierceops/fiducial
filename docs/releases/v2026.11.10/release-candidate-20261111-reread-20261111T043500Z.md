## Re-read of amendment e42cbcc..428d1bd

Scope: `git diff e42cbcc..428d1bd -- docs/releases/v2026.11.10` (read-only). Delta: two log renames (tests-initial, adoption-repeat-recheck gain -5b2a62f), candidate-refresh.md (+3 lines), release-notes.md (2 lines), release-package.md (2 pointers), and the earlier read artifact added to the directory. Assets, SHA256SUMS (identical), tests-stable.log and everything outside docs/releases untouched.

- F1 resolved in substance. The stale review claim is replaced and now says the earlier combined review covers 5b2a62f only.
- F2 resolved. Both logs renamed (100% rename, content unchanged). The three pointers in release-package.md (tests-initial-5b2a62f.log, adoption-repeat-recheck-5b2a62f.log, tests-stable-5b2a62f.log, test-source-state-5b2a62f.json) all resolve to existing files; no stale unsuffixed reference remains in release-package.md, session-handoff.md or gate-request.md.
- F3 resolved. candidate-refresh.md now states the finalization tests assert the #432 batch as landed, not this candidate's process/. Accurate.
- F4 resolved. release-notes.md #412 bullet now mentions the read-only case; accurate and consistent with candidate-refresh.md.

New issue (non-blocking, deferred): the new release-notes sentence "The #411 change and this refreshed candidate were each read independently (ready-with-findings; the one blocking finding in each was resolved before this text)" is imprecise. The #411 reads were six artifacts with mixed verdicts: one changes-required (one blocking finding, resolved by the LANDED pin), others ready-with-findings or ready with no blocking finding. "Each ... the one blocking finding in each" is false for the #411 reads taken individually. For this refresh the read was ready-with-findings with one blocking finding (F1), resolved by this amendment, which is true. Fix: "The #411 change was read independently by several reads (the one blocking finding was resolved before this text) and this refreshed candidate once (its one blocking finding likewise)."

Minor: candidate-refresh.md says F1-F4 "are corrected in the commit that added it"; true at 428d1bd but this re-read, not that commit, is what confirms it. Not-material.

Verdict (amendment): ready-with-findings; the one new finding is wording only and does not change the overall verdict.
