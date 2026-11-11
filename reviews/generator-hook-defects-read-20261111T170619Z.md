# Review: intake/generator-hook-defects — read-20261111T170619Z

Verdict: changes-required
Reviewed: intake/generator-hook-defects @ b11df95
Baseline: main @ 76a6c14
Reviewer: reviewer-agent and skeptic-risk-agent, three passes (quality, skepticism, continuity) in one session; wrote none of the delta
Date: 2026-11-11
Scope: `git diff 76a6c14..b11df95` (16 files, +1128/-27): bin/bundle, bin/release, bin/hooks/push-readback, bin/rulestore/{store.py,emit/codex.py,emit/common.py}, process/adopt.md, new and changed tests, the plan. I ran `sh bin/tests/run` (457 tests, OK, 0 failures, no skips reported); /tmp/pkg2-tests-red.log (457 run, 75 failures) and /tmp/pkg2-tests-green.log (457 OK) agree with it. All experiments ran in clones under /tmp/rvw (a bare origin with a GitHub-style URL via insteadOf); every bin/bundle and bin/release call passed an explicit --out under /tmp/rvw.
Cross-checked: plan docs/plans/generator-hook-defects-plan-20261111T161818Z.md; issue 366 body; specs/rule-store.md (G6, J4, AC-RS-6/12/14, line 216); decisions/log.md DEC-000630, DEC-000920, DEC-000940, DEC-001560; README.md; bin/release docstring; process/*.md and rules/*.md for release/bundle prose.
Not inspected: issues 365, 398, 381, 440 bodies (acceptance taken from the plan); the Context Quality read over process/adopt.md (another reviewer's); a real `gh release create` or any live GitHub call; GitHub Enterprise hosts; Windows/macOS behaviour; ACL, read-only filesystem and immutable-flag cases for E1; exhaustive proof that the C2 substring check cannot false-refuse on future stores.
Findings: 1 blocking, 5 non-blocking, 3 observations
The human should inspect: F1 (is a header change routine or consequential here; the spec says consequential).

## Quality pass

Verdict (quality): ready-with-findings

Each criterion is met by a small change. Evidence that matters:
- A: empty, whitespace-only, CRLF-empty, NBSP-only and Human-heading-first bodies all raise RowShapeError naming the file; an enforce-only body loads (run on a clone, script /tmp/rvw/a.py). The real store loads (271 rows, 223 retired) and all twelve bundles generate.
- B: a corrupted `retired:` decision target (DEC-999999) and a corrupted row target (R9999) each fail test_retired_targets naming row and target; restored, it passes on the real store.
- C: real `bin/release` against the real store (origin `https://github.com/acme/fid.git` served by a local bare repo) printed `gh release create -R acme/fid v9.9.9 --target <sha> ...` and wrote 12 bundles. A bundle path that dropped a paragraph: `refused: writer: selected row R0166 is missing from the generated bundle`, exit 2, output directory absent, no /tmp/fiducial-release-* left. A path that appended a retired row's text: `refused: writer: retired row R0125 appears in the generated bundle`, same cleanup. Reverted to the original: no false refusal on the real store. The shortest retired rendering is 23 characters, so substring matching has margin today.
- E1: with uid 65534 and a root-owned 0666 CLAUDE.md, apply exits 2 `adopt: not the owner of CLAUDE.md` and the tree is unchanged (instrumented copy of the test).
- E3: `+main`, `+refs/heads/x/y`, `+main:+refs/heads/x/y`, `+HEAD:+x/y`, `HEAD:+x/y` read back the right branch. `+a:b` with no local `a` fails loudly on the missing ref, which is correct.
- E4: emitted Codex adapter, `shell`/`exec_command`/`Bash` with `command` as a list: joined and read back, no traceback; `cmd` list still works; `deny` with a list matches.
- Test helper in test_release.py: `git diff 76a6c14..bab8a9f -- bin/tests/test_release.py` shows only added lines. The origin repoint to a GitHub-style URL is additive and every assertion that existed is unchanged. The one pre-existing fetch-failure test sets its own origin URL afterwards, so it is not masked.
- Non-additive edits to pre-existing tests, from `git diff 76a6c14..bab8a9f -- bin/tests | grep '^-[^-]'`: three lines, not one: the E6 removal in test_hooks.py, plus the `run_apply` signature and docstring lines in test_adopt.py (see F5).
- Emission on the real store, base vs head: claude-code output byte-identical; codex output differs only in `.codex/hooks/codex-hook`, as intended.

## Skepticism pass

Verdict (skepticism): ready-with-findings

Verified by running, all in clones:
- D1/D2: modified, untracked, deleted (staged and worktree), renamed (both paths named), staged-only changes under rules/ and README.md refuse and name the path. Modified SPEC.md, untracked zzz.txt, deleted LICENSE, modified bin/tests/run and bin/hooks/push-readback do not block. Paths with spaces and newlines are handled (-z).
- D3: header carries `<sha>+local.<12 hex>` for modified, deleted and renamed inputs and for modified bin/bundle; two runs on the same dirty tree give the same hex; README-only and outside-root changes keep the plain header; a malformed new rule refuses before any bundle. `--emit` output is unchanged. A clean tree's bundles are identical to base's apart from the timestamp (old bin copy vs new, same store, diffed for writer and chief-of-staff).
- Header readers: grep finds no code that parses the header; the only parser is the prose in specs/rule-store.md J4 (see F1) and the new test regex.
- E5: whole-token behaviour confirmed for `docs/process/gate.md`, `subprocess/gate.md`, a URL, `process/gate.mdx`, `process/gate.md/x`; trailing `.` and `,` still rewrite. See F3 for hyphen and `.md.bak`.
- Real store: no existing rule or process text hits any of the E5 edge forms.

Findings F2, F3, F4 below.

## Continuity pass

Verdict (continuity): changes-required

F1 is a contradiction with specs/rule-store.md and DEC-000630 that the delta did not change. DEC-001560 (bin/bundle --where renders the local tree) and DEC-000940 are consistent with the delta. DEC-000920 is consistent: release assets carry the plain SHA, and every asset states the same SHA. bin/release's docstring was updated and matches behaviour. README.md line 89 and the process documents contain no prose contradicted by the delta.

## F1 — blocking
Claim: The delta changes the bundle header (`<full HEAD>+local.<hex>`) and classifies the work routine, but the spec says the header is a public interface whose change is consequential, and the governing text still says the header names the full HEAD.
Classification: defect
Location: bin/bundle:88-101; plan line 5 ("Class: routine"); specs/rule-store.md:57 (G6), :99 (AC-RS-6), :108 (AC-RS-14), :38 (J4), :216; decisions/log.md:733 (DEC-000630)
Evidence: read specs/rule-store.md:216 "The query mechanism, the header and the render order are a public interface; changing it is consequential and takes the explicit go." G6 and DEC-000630 say "full HEAD SHA". J4 says a session "reads the header's HEAD" and "computes commits behind the default branch from that HEAD"; I ran bin/bundle on a dirty tree and the header is `...@ b11df95...+local.424ad7cb6a1d ...`, which is not a revision a consumer can pass to git. Issue 366 agrees "a compact indication of local modifications", but it is an agreed outcome, not a recorded decision or a spec edit. No decision entry or spec text in the delta supersedes DEC-000630's header clause.
Consequence: a session following J4 on a dirty-tree bundle gets an unusable HEAD; the spec and the tool disagree; and if the first user exposure is a release, the consequential-class rule requires Dave's explicit go that the plan's "routine" class does not seek.
Fix: have the human rule on classification; if consequential, record the go. Add a decision entry superseding DEC-000630's header clause (header may carry `+local.<12 hex>`; the HEAD is the part before `+`), and update G6, AC-RS-6, AC-RS-14 and J4 to say how a consumer reads it. Release bundles are unaffected (D5).

## F2 — non-blocking
Claim: A gitignored rule file inside rules/ is loaded into a release bundle, with the plain revision, and neither the release check nor the local marker sees it.
Classification: defect
Location: bin/rulestore/store.py `dirty_input_paths` (git status, ignored files not reported); plan D5 ("assets always carry the plain revision, since D2 has already refused otherwise")
Evidence: ran: added `rules/ign.md` (role: [writer]), listed in .git/info/exclude; `git status --short` clean; `bin/release` exit 0; the text appears in fiducial-bundle-writer.md whose header is the plain SHA. Base behaves the same (plain `git status --porcelain`), so this is not a regression.
Consequence: D5's stated guarantee is overstated; a release can contain a row that is in no commit.
Fix: add `--ignored` to the status call (or a `git ls-files --others --ignored` pass) over INPUT_ROOTS, or state the limit in the PR and bin/release docstring.

## F3 — non-blocking
Claim: E5's whole-token rule still rewrites a hyphen-joined prefix or a `.md` followed by `-` or `.`+word.
Classification: suggestion
Location: bin/rulestore/emit/common.py:199
Evidence: ran rewrite_process_references: `sub-process/gate.md` -> `sub-` + skill reference; `process/gate.md-old` -> skill reference + `-old`; `process/gate.md.bak` -> skill reference + `.bak`. The plan names only `.` and `,` as non-continuations.
Consequence: low; no such text exists in the real store today.
Fix: add `-` to the lookbehind class and use `(?![\w/-]|\.\w)` for the tail, with a test, or leave and note.

## F4 — non-blocking
Claim: The E1 test passes whether apply completes or refuses, so it would not catch a half-written target that still exits non-zero only if the state comparison were weak; it also never asserts which outcome the code chose.
Classification: suggestion
Location: bin/tests/test_adopt.py (test_e1_...)
Evidence: read; instrumented copy shows the actual outcome is refusal (`adopt: not the owner of CLAUDE.md`, rc 2) with the tree unchanged.
Consequence: if the implementation later switched to completing, or the refusal branch lost its state check, the test would still pass on the other branch. The documented prose (process/adopt.md step 4) now commits to the refusal.
Fix: assert returncode 2 and the message, matching the prose.

## F5 — non-blocking
Claim: The test-designer's change is not additive in test_adopt.py: `run_apply` gained a parameter and a rewritten docstring.
Classification: suggestion
Location: bin/tests/test_adopt.py:435-449
Evidence: `git diff 76a6c14..bab8a9f -- bin/tests | grep '^-[^-]'` lists the `def run_apply(self, review, approval):` line and its docstring line besides the E6 line. Default argument keeps every existing call unchanged; no assertion is weakened.
Consequence: none beyond the brief's expectation that E6 be the only non-additive edit.
Fix: say so in the PR.

## F6 — non-blocking
Claim: specs/rule-store.md's list of `bin/release` refusals does not name the two new ones (non-GitHub origin, generated-bundle body check).
Classification: suggestion
Location: specs/rule-store.md:192; AC-RS-12 (:105)
Evidence: read; "an unsynced or dirty tree and an unreachable origin". AC-RS-12 says "refuses whole on any failure", so it is not contradicted, only incomplete. The printed command also now carries `-R`, which AC-RS-12 does not mention.
Consequence: documentation lag.
Fix: add the two refusals and `-R` when F1's spec edit lands.

## O1 — observation
Claim: The emitted `.codex/hooks/codex-hook` and the push-readback hook change; adopted repositories get the fixes only on re-adoption (planned at the end of the batch, #439). `local_shell` is not in SHELL_TOOLS, so list commands for it still traceback; out of scope for E4.

## O2 — observation
Claim: `_body_problem` re-implements selection (`query.select`) and treats a retired row's rendered text as a substring; a future very short retired body could cause a false refusal. None exists now (shortest 23 characters).

## O3 — observation
Claim: A rule body of only an HTML comment or a zero-width space loads (A1 covers empty/whitespace/Human-only). The plan did not list these.
