# Fiducial

A working method for directing LLM agents and evaluating what they deliver, with roles and instructions that persist across sessions. Download a role’s Markdown bundle, load it into your agent, and put it to work.

I built Fiducial to understand the problem space: agent harnesses, context delivery, switching roles, keeping intent intact across sessions. I expect the tools here to get much better. Building something that tries to solve the problem is the best way I know to understand it.

One question I’m exploring is whether we can produce software without human code review. I think we’ll get there. I’m not comfortable relying on it for production today. I want to understand what would have to be true for me to trust it.

The most interesting part, to me, is the evidence model. What did you check? What does that establish? What remains unknown? What would close the gap? A passing test against a fixture tells you something about your parser. It tells you nothing about whether the live service accepted your credentials.

Fiducial currently supports spec-driven software development – specifications and tests before implementation – and a writing workflow with separate drafting, copy editing, and criticism. Both carry human intent through the work and its evaluation.

It’s open source. Clone it and make it your own, or send me a PR. I’ll read it. [License](https://github.com/davepierceops/fiducial/blob/main/LICENSE).

[Try it](#try-it) · [Current issues](https://github.com/davepierceops/fiducial/issues) · [Milestones](https://github.com/davepierceops/fiducial/milestones)

## Manage the proof

An agent’s report that something works is a claim. Fiducial asks it to carry the evidence with that claim, including the boundary the evidence does not cross.

For the parser example, that means reporting the fixture tested, the result observed, the live connection still unchecked, and the check needed to resolve it. The gap follows the work into review and the release decision. It should not disappear into “all tests pass.”

The software workflow separates test authorship, implementation, quality review, and skeptical review. Tests must fail on incorrect behavior; reviewers examine whether the tests establish what the implementation claims. The skeptic examines the evidence chain, including mocks, assumptions, and unverified boundaries.

Separate agents can share the same wrong assumption. These procedures give us things to examine and challenge; their existence does not settle the question of trust. Humans still own product intent, risk decisions, and consequential approval. The experiment concerns human inspection of code, not the removal of human judgment.

## Try it

### Software

Download the [chief-of-staff bundle](https://github.com/davepierceops/fiducial/releases/latest/download/fiducial-bundle-chief-of-staff.md), load it into a fresh chat project, and describe the problem you want to solve.

> Help me write a PRD for this idea. Let’s work out the users, their needs, and what success would look like.

The bundle includes a PRD template and assigns drafting it with you to the chief of staff. We’re [validating that guided starting experience](https://github.com/davepierceops/fiducial/issues/373).

The workflow proceeds through product requirements, technical design, specification/test reconciliation, implementation, review, and a release decision. This is spec-driven and test-driven development; the coding roles assume that way of working. See the [change flow](https://github.com/davepierceops/fiducial/blob/main/process/change-flow.md).

Before directing repository writes, establish the [project setup requirements](https://github.com/davepierceops/fiducial/blob/main/process/project-setup.md): default-branch protection against force-push and deletion, changes through pull requests without administrator bypass, and a runner-level force-push prohibition. Planning can begin before those controls are in place.

### Writing

Start with the [writer bundle](https://github.com/davepierceops/fiducial/releases/latest/download/fiducial-bundle-writer.md). It can develop a piece from conversation or notes, or draft from an agreed outline. Separate copy-editor and critic sessions then propose tracked edits and anchored comments; the author decides what stays.

**The released writing bundles currently contain my voice and publication preferences.** The [voice template](https://github.com/davepierceops/fiducial/blob/main/voice-template.md) is a starting aid for adapting the source; uploading it alone does not replace the embedded preferences. [Portable author profiles and optional sample-based setup](https://github.com/davepierceops/fiducial/issues/355) are planned work.

### Loading and handoffs

Have the agent read the complete bundle before starting. Your chat application or coding harness supplies sessions and tool access. You or the host starts the next role’s session and passes its instructions and artifacts along. Git work needs repository tools; tracked DOCX edits need document-editing capabilities.

For repeatable use, pin your bundle to a dated [release](https://github.com/davepierceops/fiducial/releases). In a coding project, keep a local copy and point the harness’s instruction file at it. Confirm that the harness actually reads it. Adopting a newer bundle should be deliberate.

## What we know so far

The repository contains the method’s own development record: specifications, implementations, tests, reviews, mistakes, and revisions. The [bundle-tool skeptic review](https://github.com/davepierceops/fiducial/blob/main/reviews/bundle-tool-skeptic-20260906T150000Z.md) is one example of scrutiny uncovering misleading test evidence. It describes its reviewed revision; its findings are not a current bug list.

The tool suite checks software behavior. We have not established Fiducial’s comparative effect on agent outcomes, human effort, cost, or context overhead. [Annotated examples](https://github.com/davepierceops/fiducial/issues/371) and [comparative evaluations](https://github.com/davepierceops/fiducial/issues/372) are on the roadmap.

Current adoption work also includes [resolving references inside bundles](https://github.com/davepierceops/fiducial/issues/358), [thin harness adapters](https://github.com/davepierceops/fiducial/issues/360), and [retiring obsolete entry points](https://github.com/davepierceops/fiducial/issues/361). GitHub issues and milestones carry the live status.

## Make it yours

Each rule lives in a Markdown file with selection keys such as role and topic. Shared instructions have one source; a query selects a role’s rules and process documents, with definitions added by term matching. Git carries the history.

Every rule gets its own file. Managing that is exactly as tedious as it sounds. Fortunately, I have LLMs. Thank you, LLM.

To work with the source, clone the repository. The tooling uses Python’s standard library and Git:

```sh
bin/bundle --keys
bin/bundle --where role=writer --name writer
bin/tests/run
```

Generation currently requires a successful fetch of `origin/main`, HEAD matching that ref, and no uncommitted changes under `rules/` or `process/`. Output goes to `~/Downloads` unless you supply `--out`. [Ordinary offline generation from local edits](https://github.com/davepierceops/fiducial/issues/366) is planned.

See the [named queries](https://github.com/davepierceops/fiducial/blob/main/process/named-queries.md) for the 12 distributed roles and their selection. The [rule-store design](https://github.com/davepierceops/fiducial/blob/main/specs/rule-store.md) explains the underlying model.

<details>
<summary>Repository map</summary>

| Location | Contents |
|---|---|
| `rules/` | Individual rules and definitions |
| `process/` | Workflows, templates, and bundle queries |
| `bin/` | Bundle, release, directive, and Git tools; tests |
| `specs/` | Tooling specifications |
| `decisions/log.md` | Recorded human decisions |
| `reviews/`, `retros/`, `docs/cycles/` | Development records at their stated revisions |
| `docs/history/` | Earlier forms of the methodology |

</details>
