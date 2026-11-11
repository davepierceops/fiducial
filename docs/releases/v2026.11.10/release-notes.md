# Fiducial: context consolidation

This revision consolidates the instructions already merged since v2026.11.04. It moves command-block and verification procedures into on-demand skills, prunes standing rules and definitions, and simplifies role, build and release guidance. Approved writing changes through R1167 are included; further writing-role work remains deferred.

Observed from fresh generation: each native root changes from 293 to 45 lines and from 4,171 to 585 whitespace-delimited words. Ten role bundles shrink; Architect and Writer grow slightly. These are file-size measurements, not measured improvements in model behavior, token costs or enforcement.

The source remains the rule/process store. Software adoption uses the tagged source and the reviewed adoption procedure. Downloads remain README.md and twelve standalone role bundles. Publishing a release does not update existing adopted repositories automatically.

Adoption now preserves the permissions of existing Markdown and JSON files, including the ownership manifest ([#411](https://github.com/davepierceops/fiducial/issues/411)).

## Verification

Candidate: `a8d87bc95afed9f5ac8b54fe2c8863013ce10265`.

Observed: 349 tests pass in the clean candidate clone with stable source metadata, with no skips reported. All 13 staged assets match their SHA256 manifest; bundle headers identify the candidate; README matches its Git blob. Both native layouts generate successfully, and native hooks/configuration matched v2026.11.04 byte-for-byte with unchanged modes at the previous candidate, and their sources are unchanged since. The #411 change and this refreshed candidate were each read independently (ready-with-findings; the one blocking finding in each was resolved before this text); the earlier combined review covers the previous candidate `5b2a62f` only. The inherited defects and verification gaps below remain explicit.

## Known limitations

- Native skill loading, invocation/adherence and live hook enforcement remain unverified. Generated files and passing local tests do not establish future model behavior.
- A destination changing into a directory after preparation can cause partial adoption ([#412](https://github.com/davepierceops/fiducial/issues/412)). Keep the target idle between review and apply; inspect and recover partial changes after a failure. A read-only file that needs a content write can also fail partway through.
- Some installed skill references still name source `process/` paths ([#416](https://github.com/davepierceops/fiducial/issues/416)). Use the corresponding installed skill by name; automatic recovery is untested.
- Push-readback has payload and qualified-ref limitations ([#415](https://github.com/davepierceops/fiducial/issues/415)). Verify the actual remote ref explicitly after pushing.
- Selective citation validation and empty-body refusal remain unfinished ([#358](https://github.com/davepierceops/fiducial/issues/358), [#365](https://github.com/davepierceops/fiducial/issues/365)). The current downloads were checked, without claiming those missing generator guarantees.
- The test suite requires historical Git objects; retain history when cloning for verification. Comparative effectiveness remains unestablished.

Existing users can remain pinned to v2026.11.04. Any upgrade should follow the adoption procedure rather than copying generated files over repository-specific context.
