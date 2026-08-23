Write this directive verbatim to docs/cycles/bundle-audience-tests-<timestamp>.md (timestamp ISO 8601 basic, generated now). Run `git checkout origin/main` then `git checkout -b bundle-audience-tests`. Commit the directive file, push the branch, open and squash-merge a PR via curl against the GitHub REST API using the credential-helper token held in an environment variable — never written to a file. Report the merged SHA. Then execute the rest on a fresh branch from origin/main, bundle-audience-tests-2, merged the same way; report that SHA too.

You are the Test Designer. You write acceptance criteria and tests. You do not implement bin/bundle; a separate session does.

Read before writing: docs/global-context/core.md; bin/bundle, bin/bundle-methodology, bin/aimeta/repo.py, bin/aimeta/expedited.py and the ACs and tests that shipped with expedited.py (find them; follow their location and layout exactly); bin/tests/run; bin/check-frontmatter and its glob configuration; policies/document-metadata-policy.md §Scope and §Required fields (audience).

Write acceptance criteria for `bin/bundle --audience <value>`, alongside expedited.py's ACs, covering exactly these:
1. Governed file set = every file matched by bin/check-frontmatter's configured globs, plus docs/global-context/**, engagements/**, and prose-criteria.md. Nothing under docs/history, docs/batons, docs/cycles, reviews, retros, decisions, or adapters.
2. Membership: a file is in bundle <value> when its `audience:` contains <value>, or contains all-roles, or contains all-decision-roles and <value> is the basename slug of a role document whose frontmatter has `session: decision`. Role document = first heading `# Role:` under roles/ or engagements/, as repo.py discriminates.
3. Order: ascending `order:` where present, files without `order:` after them, ties by path.
4. Output: one self-contained file; header stamp names davepierceops/fiducial, the HEAD SHA, generation timestamp, and the file list with per-file blob SHAs; each file preceded by a separator naming path and blob SHA, in the same shape bin/bundle-methodology emits today. `--out <dir>` writes <dir>/bundle-<value>-<timestamp>.md; absent `--out`, stdout.
5. `--list` emits every audience value present in any governed file, one per line, sorted, plus the three reserved values, and exits 0.
6. An audience value not in the set from AC 5 exits non-zero with a message naming the value.
7. The positional path-following closure mode is removed; invoking it exits non-zero with a message pointing at --audience.
8. Python stdlib only; same interpreter version check as the existing bin/ scripts.

Write tests for every AC in the existing test layout, runnable by bin/tests/run, against fixture trees you create under the tests directory — not against the live repo, so AC 2's `session: decision` case is tested now. Include a stub bin/bundle behaviour with deliberately wrong ordering and membership so the red run fails on assertions, not on a missing module; remove the stub before committing, or mark it so the Coder knows to replace it — say which. Run bin/tests/run; every new test must fail; the two pre-existing test_bn10 failures stay unchanged; report the counts.

Label every claim observed, inferred, told, or unknown. Do not edit bin/bundle beyond the stub, and do not edit any governed document. Cannot execute as written → stop and surface. Concurrent tree mutation → stop and surface. Report: both SHAs, AC file path, test file paths, red-run counts, and anything needing Dave's judgment, one line each, up front.
