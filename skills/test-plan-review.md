---
status: draft
last-reviewed: null
audience: [reviewer-agent, human]
---

# Skill: Test Plan Review

This procedure runs in an execution session.

## Purpose

Evaluate whether a test plan is sufficient for the intended change and risk.
The plan's author does not review it.

## Use when

- writing tests before implementation
- reviewing a spec-first/TDD plan
- adding external dependencies
- adding browser/PWA behavior
- adding or changing mocks

## Inputs

- spec
- acceptance criteria
- proposed test plan
- affected boundaries
- known risks

## Procedure

1. Map acceptance criteria to tests.
2. Identify untested criteria.
3. Identify mocks and fixtures.
4. Identify live/browser verification needs.
5. Check that the plan includes a red-gate step; flag if absent.
6. Check negative/failure cases.
7. Identify over-testing or unnecessary complexity.
8. Recommend changes.

## Output

A review artifact, in the shape the review-artifact skill states.
