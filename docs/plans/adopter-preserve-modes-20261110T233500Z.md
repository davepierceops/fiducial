# Plan — adopter preserves modes on existing shared files (#411)

- Base: main `5b2a62f3b17aca1d859a43032b9ca2295c185391`. Branch: `intake/adopter-preserve-modes`.
- Told: fix #411 before publishing v2026.11.10; publication is not authorized (handoff `docs/releases/v2026.11.10/session-handoff.md` @ `7288c7a`, gate #433).
- Status: drafted by the decision session; independent plan review returned ready-with-findings, 0 blocking (see Plan review).

## Defect

- Observed (reproduced at `5b2a62f` by executing the Python fence in `process/adopt.md` against a throwaway target): an existing 0600 `.claude/settings.json` and an existing 0600 `CLAUDE.md` are both 0644 after `build_plan` + `apply`.
- Observed (same run, not in #411's text): after both are set back to 0600, a repeat run whose content is unchanged plans writes for both and widens them to 0644 again.
- Observed cause: in `build_plan`, `wanted, new_mode = desired.get(name, (None, mode))` takes the staged tree's mode for every staged path, and `if result != current or (result is not None and mode != new_mode)` plans a write on mode difference alone. `prepare` and `apply` chmod to the planned mode.

## Acceptance criteria

1. An existing shared `.json` path keeps its mode through first adoption, upgrade (staged content changes) and repeat (no change).
2. The same for an existing shared `.md` path.
3. A repeat run over unchanged content plans no writes, whatever the existing modes of shared `.md`/`.json` paths. The manifest is unchanged on a repeat because its text depends only on ownership state.
4. A new file takes its staged mode; a new executable hook lands executable.
5. Whole-file objects (scripts, TOML) keep today's behaviour: staged mode, recorded in ownership, a local mode change refused as "occupied or modified structured file".
6. A mode change on any inventoried path between plan and apply is still refused before the first write ("target changed since review").
7. The full suite passes.

## Change

- `process/adopt.md`, Python fence, `build_plan` only: for a path that exists in the target and ends `.md` or `.json`, the planned mode is the existing mode. Nothing else moves. The suffix match is case-sensitive, as the existing branch selection is. This covers fiducial-wholly-owned Markdown (agent and skill files) as well as shared files: a local mode on those is kept too.
- `process/adopt.md` prose, "Ownership and deterministic create/append": one sentence stating that an existing Markdown or JSON file keeps its permissions and a new file takes the generated ones.
- `bin/tests/test_adopt.py`: regressions for criteria 1–6.
- Regenerate the installed copies of the adopt skill through the adoption procedure so `.claude/` and `.agents/` match the source.

## Out of scope

- #412 (partial adoption after destination drift).
- The ownership manifest's hard-coded 0644 (`writes[MANIFEST]`). It is fiducial-owned, not a project-owned shared file; to be filed as its own issue, not changed here.

## Test plan

- Level: the existing `AdopterProcedure` unit tests, which execute the published fence against real temporary directories. No mocks added. Fixtures: files written by the test.
- Each regression is shown failing at `5b2a62f` before the fix, except criteria 4–6, which guard existing behaviour and are expected to pass before and after; the test designer says which is which with the run output.
- Failure cases: mode drift after plan (criterion 6); locally chmodded owned script (criterion 5).
- Unverified after this change: behaviour on filesystems without POSIX modes; native harness loading and hook enforcement (unchanged boundary from the release package). Release impact of both: `deferred`, as in the existing package.

## Regressions the plan review added

- Both a `.json` and a `.md` at 0600 across first run, upgrade and repeat; the repeat plan has no writes.
- Mode-only drift between plan and apply is refused (the existing drift test only adds a file).
- An existing 0600 file that is retired, and one that is edited only, keeps 0600 if it survives.
- A file fiducial created, then chmodded by the user: the repeat plans no writes.
- A new hook lands 0755.

## Confidence ledger

- Claim: existing `.md`/`.json` modes survive adoption. Evidence: the regressions, executing the published fence on a POSIX filesystem. Boundary: other filesystems, and a real target repository. Deferred verification: the next real adoption's diff.

## Failure analysis

- If the fix is wrong, adoption either still widens modes (visible in the adoption diff and the new tests) or fails to make a new hook executable (criterion 4 test). Neither is silent; both are reverted by reverting the adoption diff.

## Sequence

1. Independent plan review.
2. Test designer writes the regressions and records failing output.
3. A different coder makes the change and turns them green.
4. Context Quality read of the process delta; Reviewer and Skeptic/Risk passes over the diff; one review artifact per read.
5. Self-adoption refresh, PR, merge decision.
6. Refresh the v2026.11.10 candidate assets and evidence at the new main; update #433. Publication waits for explicit approval.

## Plan review

- Independent read by a subagent that did not write the plan (sonnet, read-only, traced from code, no experiments run): ready-with-findings, 0 blocking. Its findings — state the manifest and case-sensitivity positions, state that wholly-owned Markdown is covered, add the regressions listed above, add a ledger line — are folded in above.
