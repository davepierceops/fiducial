# Package 7 baseline evidence

Observed, contract-verified: `bin/tests/run` executed from the package 7 worktree at source baseline e3850f6587a242920bd04c90cb48e8f2e3ba2b62. No implementation changed during the run; only append-only decision records were being prepared.

```text
Ran 303 tests in 96.523s
OK
```

No skips or failures were reported. Full local output: `/private/tmp/fiducial-pkg7-tests-baseline.log`; SHA256 `1b88b5b623123a1131f1b7d7a1483c6989a0277b0d743052385e294313acb76a`. This committed summary records the count; the full transient log is not required to reproduce the command.

Boundary: the suite exercises local generator, hook subprocess, store, adoption and release contracts; mocked forge responses are mock-verified. It does not establish native harness enforcement, project hook trust, release publication or production behavior. Those boundaries remain separate in the package reports.

Required preparation read: SPEC.md whole; subtraction plan whole; DEC-001070 through DEC-001560; complete sort table; process/review-artifact.md, release.md and decision-log.md; every pre-existing reviews/pkg-* artifact; README.md. Later human loading evidence was additionally read in reviews/fiducial-adoption-live-check-20261105T020041Z.md.
