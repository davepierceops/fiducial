---
status: draft
last-reviewed: null
audience: [research-agent, human]
purpose: Blind external discovery of software-development methodologies and adjacent high-assurance traditions. Phase 1 of a two-phase comparative scan.
depends-on: []
---

# Directive: External Methodology Scan — Phase 1 (Blind Discovery)

## Intent

Catalog practices from external software-development methodologies and adjacent
high-assurance engineering traditions relevant to disciplined, spec-first,
LLM-assisted development. Output is a flat catalog of atomic practices with
provenance. This phase runs **blind to this project's own methodology** —
comparison, grading, and adoption judgment are Phase 2 and Dave's, not this
session's.

## Blindness constraint (structural)

The corpus is not in this session's inputs. Keep it that way.

- Do not fetch, open, or reference any document under `davepierceops/ai`, any
  context bundle, or any project methodology text.
- If the methodology corpus is already in your context, this is the wrong
  session. Stop and report that, rather than proceeding contaminated.

Do not reconstruct the project's methodology from memory to orient yourself.

## What to survey

Seed traditions. Cover breadth across them before going deep on any one.
Follow a strong lead outside the list only when it yields a concrete practice,
and log why you followed it.

- Spec-driven / spec-first development (SDD and named variants)
- Design-by-contract (Eiffel / Meyer lineage: preconditions, postconditions, invariants)
- Formal and lightweight-formal methods (TLA+, Alloy, model checking, property-based testing cultures)
- Safety-critical / high-assurance process (DO-178C, IEC 61508, ISO 26262, medical-device SDLC)
- Site reliability engineering (error-budget governance, operational readiness, production-readiness reviews)
- Design-doc cultures (IETF RFCs, ADRs, big-tech RFC / design-review processes)
- Test-first lineages (TDD, BDD, acceptance-test-driven) and their spec-as-executable-test ideas
- LLM-agent-native engineering (agentic coding workflows, eval-driven development, context engineering, spec-as-prompt practices)

Both halves weigh equally and both are in scope. In the durable traditions,
look for formalizations of problems a disciplined software workflow faces. In
the LLM-native bucket, look for practices addressing problems specific to an
LLM implementer: instruction drift across long context, hallucinated
interfaces, prompt-as-spec, instructions embedded in read material.

## Discipline

- **Applicability lens on the durable traditions.** A practice from a durable
  tradition (safety-critical, formal methods, SRE, design-by-contract, RFC/ADR)
  earns an entry only if it addresses a problem an LLM-agent software workflow
  also has. A whole standard is not an entry — the specific mechanical practice
  within it is (e.g. DO-178C's assurance-level scaling, not "DO-178C").
  LLM-native practices are not subject to this lens; they are in scope by
  definition.
- **One atomic practice per entry.** If an entry describes two things, split it.
- **Provenance is required.** Every entry names its source and source type. An
  entry without a locatable source is not a finding.
- **Separate what the source says from what you infer.** `Claim (stated)` is the
  source's own assertion. `Inference (mine)` is anything you read into it. Do
  not blur them.
- **Source quality is flagged.** These search terms return heavy vendor
  content-marketing. Discard it unless it carries a specific, mechanical
  practice; when it does, mark source type `vendor content` so Phase 2 can
  weight it down.
- **No adoption judgment.** Do not assess whether a practice would help this
  project. Cataloging only.
- **No synthesis, ranking, or cross-tradition dedup.** Record practices as
  found. Do not merge near-duplicates across traditions — cross-tradition
  convergence is a Phase 2 signal.

## Entry schema

```markdown
## <id> — <short practice name>
Practice: <one atomic sentence>
Tradition: <which seed tradition, or "other" + what>
Source: <title / author / org>
URL: <link>
Source type: <primary text | practitioner account | vendor content | secondary summary>
Source quality: <strong | mixed | weak — one clause why>
Claim (stated): <the source's own assertion>
Inference (mine): <what you read into it — omit if none>
Mechanism: <concretely how the practice works, if the source gives one — omit if none>
```

## Budget and stop conditions

This phase is bounded by a hard search ceiling. Saturation is an early-stop
within that budget, never the sole stop.

### Fetch rule (the primary cost control)

Catalog the practice, provenance, and claim **from the search snippet.** Fetch
a full page only when a specific mechanism cannot be captured any other way — a
full-page fetch is 5–10× the cost of a snippet. Prefer three snippet-sourced
entries over one fetched one. If a mechanism stays unclear after one fetch,
record what the snippet supports and move on; do not chase it.

### Two passes, breadth banked first

1. **Shallow sweep — one search per seed tradition (~8 searches).** Extract
   every atomic practice visible in snippets. **Commit the catalog at the end
   of this pass** — this banks breadth, so a later cutoff leaves coverage across
   all traditions rather than depth in one and nothing after.
2. **Deep pass — a budget of ~17 further searches** across traditions, spent
   where the shallow sweep found the richest or thinnest veins. Saturation is
   the early-stop *inside* this budget: if new searches stop yielding new
   practices, stop early and bank the remainder. Do not spend the budget for
   its own sake.

### Hard ceiling

**Stop at 25 total web searches regardless of saturation state.** If the
ceiling is reached mid-vein, stop, commit, and record the unfinished vein in
the coverage report as `thin — hit search ceiling`.

### Checkpoints

Commit the catalog after the shallow sweep, then again every ~10 entries during
the deep pass.

## Output

- Commit the catalog to `docs/research/methodology-scan-catalog.md`.
- Findings-only: no cover letter, no recommendations, no comparison.
- End with a per-tradition coverage report: covered well / thin / thin — hit
  search ceiling / found nothing. State the total search count used.

## Dispatch

Launch parameters, recorded here so they do not live only in chat
(`skills/directive-dispatch.md`). Route, model, and attended posture are set by
the operator at launch; the Track rule is executor-actionable.

- **Route:** fresh session. The directive is self-contained; a fresh session
  cannot carry triage or methodology context that would break blindness.
- **Model floor:** Sonnet. The volume is cheap-model-friendly; the judgment is
  not — atomic practice vs vendor filler, primary source vs marketing, claim vs
  inference, whether a durable practice addresses an LLM-agent problem. Haiku is
  below the floor for this phase; a weak model corrupts the catalog Phase 2
  depends on. Higher than Sonnet is fine.
- **Track:** decided at launch by connector presence.
  - *Track A* (GitHub MCP present): the executor commits to the paths named
    above directly.
  - *Track B* (connector absent): wherever this directive says *commit*, the
    executor instead emits the catalog as an artifact for the operator to land.
    An absent connector must not become a completed run that committed nothing.
- **Execution block (Track A):**
  `Execute docs/research/methodology-scan-phase1-discovery.md from origin/main HEAD.`
- **Attended posture:** run attended through the shallow-sweep commit and
  confirm that first checkpoint actually landed — this also confirms the track
  is working. Only then let the deep pass run unattended. Review the catalog,
  coverage report, and search count on return regardless; the coverage report
  exists to make that review fast, not skippable.
