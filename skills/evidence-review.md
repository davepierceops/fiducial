---
status: agreed
last-reviewed: reviews/evidence-review-cycle-2.md @ cd7db71
audience: [reviewer-agent, skeptic-risk-agent, release-manager-agent, human]
---

# Skill: Evidence Review

This procedure runs in an execution session.

## Purpose

Evaluate whether the evidence supports the claims made by an agent or change package.

## Use when

- reviewing implementation output
- reviewing test results
- preparing release
- deciding whether Dave needs to inspect more deeply

## Inputs

- spec or intent
- implementation summary
- test evidence
- review notes
- verification boundary declarations
- known gaps

## Procedure

1. List the claims being made.
2. Match each claim to evidence.
3. Identify unsupported claims.
4. Identify overbroad interpretations of test results.
5. Identify missing evidence for material risks.
6. A recommendation is a next step, never a ship call; the ship call is the
   Release Manager's; signal no-ship by marking the gap `blocking`.

## Output

A review artifact, in the shape the review-artifact skill states. Its findings
are the unsupported claims, the overbroad interpretations of results, and the
material evidence that is missing; each carries one of LEXICON's four release
impact labels.
