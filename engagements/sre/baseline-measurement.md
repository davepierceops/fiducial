---
status: draft
last-reviewed: null
audience: [cartographer, implementer, assistant, human]
---

# Skill: Baseline Measurement

Steps 1-5 run in a decision session by the Assistant; step 6 runs in an
execution session by whichever of the Cartographer or Implementer re-measures.
All three read the whole file.

The baseline-gate procedure.

## Procedure

1. **Enumerate the stages** from the System Map: trigger delivery, queue,
   runner boot, checkout, auth, init, plan, apply, image build, image push,
   image pull, boot, data hydration, health-to-ready — whatever the actual
   pipeline's stages are.
2. **Instrument read-only first.** Extract stage timings from existing logs and
   CI APIs before proposing any pipeline change. Instrumentation that requires
   a change ships as a pull request like anything else.
3. **Capture a distribution, not an anecdote.** Enough runs to state p50 and
   p95 per stage.
4. **Publish the baseline** — the Measurement Baseline, in the shape and place
   the Artifacts list states.
5. **Gate improvements on an expected-delta statement**: "this change attacks
   stage X, currently p50 A / p95 B; expected result: p50 → A′" — stated
   before implementation, recorded in the change package.
6. **Re-measure after the change** with the same stopwatch, same method. The
   delta claim in the change package cites both measurements (delta-verified).

## Override

An override of this gate names the measurement debt in the change package.

## Failure modes to avoid

- optimizing the stage that is easiest to see instead of the stage the
  distribution indicts
- changing the stopwatch and the pipeline in the same change
- reporting means; report p50 and p95
- measuring spin-up but not teardown
