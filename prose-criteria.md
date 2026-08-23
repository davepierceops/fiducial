---
status: agreed
last-reviewed: reviews/corpus-regate-cycle-3.md @ edd8015
audience: [writer, human]
order: 11
---

# Public Prose Criteria

Read by the Writer role, a decision session.

## Scope

Public-facing prose published on the open internet under Dave's byline —
articles, blog posts, and similar. Nothing else: methodology documents,
operator-facing reports, and internal writing are governed elsewhere or not
yet at all.

## Trust model — every word is reviewed

Dave reads every word of a piece before it publishes.

## Purpose and audience

Readers: adopters, peers, potential clients. Goal now: establish thought
leadership. Goal later: drive adoption, expected to become primary when the
SRE-focused methodology work is public. When that shift happens, put the
register question to Dave; do not change the register on your own.

## Voice and register

- Dave's voice, singular. Not a house style, not a persona — the test is
  "reads as Dave."
- Baseline: dry, technical, wry.
- More expansive and explanatory than the methodology register — public prose
  walks the reader through reasoning the repo docs compress away.
- Persuasive, flowery, or poetic passages are permitted as occasional
  flourish, never as the constant mode.
- No clause explains the move it sits in. "It was true" over "unlike most
  such statements it was literally accurate."
- Blunt categorical claim first, then the personal instance.
- Hacker register is in-voice: grok, box.
- Claim tier is carried by verb choice and frame, never by narrated
  self-correction. "What I noticed" stays; "I should be careful with my own
  story here" is cut.
- A point is made once, flat. No contrast pair that restates it from the other
  side.

## Readers with many languages

Comprehension never depends on native-English-only cues. Speech is quoted,
not introduced by a bare colon. A line carrying irony, wordplay, or idiom
reads correctly for a reader who takes it literally; the play is bonus.
Register is never simplified to achieve this.

## Claims taxonomy

Every claim in a piece belongs to one of four tiers, and the writing makes the
tier legible to the reader:

1. **Relayed** — someone else's claim, passed along. Attributed as such.
2. **Demonstrated** — Dave's evidence constitutes proof: hypothesis, test,
   result. The piece can show the work.
3. **Grounded** — resting on experience, observation, or data below the bar
   for proof. The prose carries the tier in verb choice and frame ("what I
   noticed," "in my experience").
4. **Opinion** — clearest of all, by the same means.

This ladder is claim strength — how firmly a sentence may assert — not
provenance; provenance is stated per Core.

Tier-blurring — an opinion dressed as a grounded claim, a grounded claim
dressed as proof — is a defect.

## Terminology

Use the methodology's own governed vocabulary; define each term where it first
appears for a public reader. When an industry-standard term exists for a
concept the methodology names differently, flag the mismatch to Dave; he
decides which the piece uses.

## Profanity

Rare, and each use earns its place. Day-to-day heat comes from the rhythm and
structure of swearing without the words ("this is a terrible idea"; "no. no no
no.").

## Naming

Anonymize by default, in both directions — criticized practices are named,
companies/products/people are not; praise is likewise sparing with names.
Name only when there is a clear, articulable benefit in that instance, and
state the benefit when proposing it.

**Exception — attribution is mandatory.** When the author of a piece of work
(an idea, a technique, a phrase, a finding) is known, credit them. Always,
unless the work is literally trivial. Anonymize-by-default governs targets
and examples; it never licenses taking credit by omission.

## Structure

- Length and structure are per-piece decisions, not criteria: take them from
  Dave for the piece at hand rather than applying a standing shape.
- Standing convention: summary sections are labeled **TL;DR**.

## Length and duplication

Wordy means duplicated ideas, not duplicated words; a draft inside its word
budget can still be wordy. When Dave suspects duplication, report an audit of
the repeated ideas before cutting anything. Dave does not pick which
duplicates go: he sets a word target and the writer chooses. After a wordy
draft the target is 10% under budget, not back to budget.

## Continuity

Build across pieces is allowed, but every piece lands clean for a cold
reader. Exception: an explicitly declared series ("part 2 of N," stated
upfront) may assume its predecessors.

## Discoverability

In scope. Titles descriptive-searchable over clever; key terms appear early;
structure skimmable. **When discoverability and readability conflict,
readability wins.** The register is never altered for discoverability.

## Repo citation

When a piece discusses a methodology mechanism, link the canonical document
in the public repo (`davepierceops/fiducial`) as the authoritative artifact.

## Venue and portability

Write venue-independent prose, with no platform-specific formatting
dependencies. The canonical home is Dave's own site (pending; LinkedIn is the
interim venue); everything else is a cross-post.

## Disclosure

Site-level, stated once, in register — LLMs listed among the writing tools
alongside the dictionary and the public school education, with the closing
commitment: Dave personally reads and stands behind every published word,
including those that started in an LLM. No per-piece disclosure.

## AI prose-smell — named defect class

Defect class. The list is open: put any new tell you notice to Dave rather than
adding it yourself. Current entries:

- "load-bearing"
- em-dash cascades (a pair landing a payoff word is not a cascade)
- "it's not X, it's Y" constructions
- triadic sentence rhythm as default cadence
- hedge-then-assert patterns
- re-stating the thesis at every section opening
- summary sentences that add nothing ("This matters because...")
