# Fiducial v2026.11.24

This revision publishes the batch merged since v2026.11.10: adopter and hook fixes, release-tool hardening, a gate fallback, SLO obligations that apply only where a spec declares Production SLOs, and a repeatable `probe` skill.

## What changed

- Adoption refuses, before its first write, a destination that became a directory or that it cannot write ([#412](https://github.com/davepierceops/fiducial/issues/412)). Push read-back keeps slash-containing branch names and reads Codex `cmd` payloads ([#415](https://github.com/davepierceops/fiducial/issues/415)). Emitted skills refer to other skills in each harness's own form, and emission fails on a dangling reference ([#416](https://github.com/davepierceops/fiducial/issues/416)).
- The store refuses a rule with no instruction. `bin/release` names the repository in its printed command, checks each bundle for its selected rows and for retired text, and blocks on gitignored inputs. A bundle rendered from uncommitted inputs carries a `+local` marker in its header; release assets never do.
- Where a consequential change's `human-gate` issue cannot be opened, the human's explicit go in chat releases it; the record and the issue follow.
- SLO and error-budget obligations apply only when the spec has a Production SLOs subsection. Top K journeys stay.
- New `probe` skill, emitted to Claude Code and Codex: run in a fresh session inside an adopted repository, it checks what the generated files claim. Probes of forbidden actions aim at a throwaway target. Release and adoption records cite the latest probe report.

## Verification

Candidate: `35713889a46f4defda57b705ff43a8694aadff12`.

Observed: 464 tests pass in a full-history clone, no skips reported. The twelve bundles and README were staged, names match the published list, headers name the candidate, README matches its Git blob. The new wording is present in the staged bundles and the old unconditional SLO template line is absent. Each change was read independently before merge.

Nothing live is verified. The first probe runs after adoption of this release.

## Known limitations

- Native skill loading, invocation, adherence and live hook enforcement remain unverified. Passing local tests do not establish model behavior.
- Codex deny rules written in list form may not be enforced ([#453](https://github.com/davepierceops/fiducial/issues/453)); other probe-read items are on [#454](https://github.com/davepierceops/fiducial/issues/454) and [#450](https://github.com/davepierceops/fiducial/issues/450).
- Selective citation validation remains unfinished ([#358](https://github.com/davepierceops/fiducial/issues/358)).
- The test suite requires historical Git objects; keep history when cloning for verification.

Publishing does not update existing adopted repositories. Existing users can stay pinned to v2026.11.10; upgrade through the adoption procedure, then run the probe.
