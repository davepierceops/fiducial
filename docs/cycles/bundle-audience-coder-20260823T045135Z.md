Write this directive verbatim to docs/cycles/bundle-audience-coder-<timestamp>.md (timestamp ISO 8601 basic, generated now). Run `git checkout origin/main` then `git checkout -b bundle-audience-coder`. Commit the directive file, push the branch, open and squash-merge a PR via curl against the GitHub REST API using the credential-helper token held in an environment variable — never written to a file. Report the merged SHA. Then execute the rest on a fresh branch from origin/main, bundle-audience-coder-2, merged the same way; report that SHA too.

You are the Coder. Your job is to turn the red tests green with the minimum implementation. You do not write or alter tests, with one exception below.

Read before writing: docs/global-context/core.md; bin/tests/test_bundle_audience.py whole, including the AC docstring and the stub-banner comment; bin/bundle; bin/aimeta/repo.py; bin/bundle-methodology for output shape; bin/tests/test_bundle.py; docs/cycles/bundle-audience-tests-*.md at main.

AC amendment, dictated here (this directive is the origin): AC-BA-5 — `--list` emits every valid audience value: the basename slug of every role document under roles/ or engagements/ as repo.py discriminates, plus all-roles, all-decision-roles, human; sorted, one per line, exit 0. AC-BA-6 — a value outside that set exits non-zero with a message naming the value. Update the docstring for AC-BA-5 and AC-BA-6 and the tests that assert them, and only those; run them and confirm they fail against the stub before implementing. Touch no other test.

Replace the whole banner block in bin/bundle (STUB FOR bundle-audience-tests-2 … END STUB) with the implementation of AC-BA-1 through AC-BA-8. Remove the positional path-following closure mode entirely. Python stdlib only.

In bin/tests/test_bundle.py: delete tests that exercise the removed closure mode; keep tests that exercise shared machinery (scope, sort, dedup, output shape) and make them pass. List every deleted test by name in your report.

Run bin/tests/run. All 38 test_bundle_audience.py tests green; all retained test_bundle.py tests green; the two pre-existing test_bn10 failures unchanged; no other failure. Then run `bin/bundle --list` and `bin/bundle --audience chief-of-staff --out /tmp/bundle-check` against the live repo and report the list output and the member file count — this is the first run of the bundler against the corpus; label it observed.

Do not edit any governed document or any other file under bin/tests/. Cannot execute as written → stop and surface. Concurrent tree mutation → stop and surface. Report: both SHAs, green-run counts, deleted test names, live --list output, chief-of-staff member count, and anything needing Dave's judgment, one line each, up front.
