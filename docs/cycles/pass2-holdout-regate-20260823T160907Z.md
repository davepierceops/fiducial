Write this directive verbatim to docs/cycles/pass2-holdout-regate-<timestamp>.md (timestamp ISO 8601 basic, generated now). Run `git checkout origin/main` then `git checkout -b pass2-holdout-regate`. Commit the directive file, push the branch, open and squash-merge a PR via curl against the GitHub REST API using the credential-helper token held in an environment variable — never written to a file. Never invoke gh for anything, including auth checks; its errors are not evidence. Report the merged SHA. Then execute the rest on a fresh branch from origin/main, pass2-holdout-regate-2, merged the same way; report that SHA too.

You are the Context Quality Reviewer. Read roles/context-quality-reviewer.md, docs/global-context/review-rubric.md, skills/review-artifact.md, docs/global-context/core.md at main before acting.

Review, each file whole against all eleven rubric criteria at main HEAD (record the SHA):

1. docs/global-context/review-rubric.md — its cycle-1 findings were closed by table only; this is its first whole re-read since.
2. docs/global-context/decision-layer.md — rule 13 added, 14–17 renumbered, post-12ecaeb.
3. policies/document-metadata-policy.md — scope globs widened, session: and order: fields added, post-12ecaeb.
4. roles/context-quality-reviewer.md — Scope section revised post-12ecaeb.

Cross-check 2 and 3 against each other and against docs/global-context/core.md for contradictions; cross-check 4's Scope against 3's in-scope set — they were made to agree by the metadata-scope cycle and should now say the same thing.

Write one review artifact per file at reviews/<stem>-cycle-<n>.md, n continuing each file's own numbering, in the review artifact schema: verdict first, Not inspected stated, findings citing criterion numbers. You review; you do not edit any of the four files, and you flip no status. Findings are claims: demonstrate, cite, classify.

Run nothing beyond git reads, bin/check-frontmatter --all, and bin/tests/run for baseline confirmation. Label every claim observed, inferred, told, or unknown. Cannot execute as written → stop and surface. Concurrent tree mutation → stop and surface. Report: both SHAs, per-file verdict one line each, findings count by severity, artifact paths, and anything needing Dave's judgment, one line each, up front.
