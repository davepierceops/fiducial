---
order: 10
role: [architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: Change Flow

A delta is the accumulated difference between a thing as it stands and the thing
as it will stand when the work is done. Review is charged once per delta, at its
close — never per document, never per edit — and the delta's size and reach set
the depth of the read. Close a delta early at will; the tranche boundary is a
deadline, not a target [R0008].

## Four kinds of thing change

| What changes | The delta | Closed by | Who reads |
|---|---|---|---|
| **Rules** — rows in `rules/` | the proposed rows | **intake**: one commit | Context Quality Reviewer |
| **Process** — prose in `process/` | the edited document | **one frontier read** against the rows it cites, then the human's sign-off, recorded in the decision log naming the SHA | a frontier session that did not draft it, then the human |
| **Specs** — a project's PRD, TRD, acceptance criteria | a spec branch with commits on it | **reconciliation**: one read, one ruling recorded in the decision log naming the SHA, one pull request | Spec Reviewer, then the human |
| **Code** — a project's implementation | a unit of work's branch, landing as one pull request | **change package**: one read over the package; every pull request gets a code review by an agent | Reviewer and Skeptic/Risk, then the human at the release gate |

## The one read

At close, a session that did not produce the delta [R0462] reads it whole — the
diff from where it opened to the revision under review, plus what it produced:
tests, evidence, a change package — organised by dimension, not by document.

- **Continuity** — does the delta contradict anything it did not change? For a
  spec delta, the continuity scan [R1104, R1105, R1137]; for a rules delta, the
  near-duplicate shortlist plus judgment; for a code delta, the architecture
  summary against the TRD.
- **Quality** — [R0487]. For a code delta this dimension is a code review: every
  pull request gets one, by an agent, with no trivial-change exemption and no
  human diff-read by default.
- **Skepticism** — [R0488].

Continuity carries its own verdict line, as quality and skepticism do; the
delta's class decides whether those two run in one session or two [R0492, R0534,
R0535, R0536]. The **size call** is the second trigger for two: the reader finds
the delta exceeds what one session can read whole and says so in the verdict; it
sets the session count only.

The human, or the Chief of Staff on his behalf, may call for a deep read of
anything at any time, delta or not: every dimension, two sessions, continuity at
its widest reach, over the whole thing rather than a diff [R1137, R1138].

The read emits a review artifact with one overall verdict and one per pass
[R1414]; the decision session triages its findings [R1395b]. A blocking finding
reopens the delta, which closes again on one more read over the diff since then.

## The spec lifecycle

A spec branch is **open** — it has commits the default branch does not — or
**closed**, agreed, the default branch being the version of record.

1. **Open** from the commit that cuts `spec/<tranche-slug>` [R0004]; edits land
   ungated and are gated together at the close [R0474]. The Test Designer starts
   once the entry read has run and the human has said to proceed [R1101, R1468],
   then writes the spec's suite and runs the red gate while the branch is open
   [R0478, R1158]. At most two tranches run at once [R0012, R0013].
2. **Close** when spec and tests cohere: the Spec Reviewer reads the branch's
   whole diff, from the branch point, with the tests [R1106, R1126]; the human
   then reads that diff and makes one ruling [R0481, R1485]. The reconciliation
   pull request lands the branch [R1491]; agreement attaches to the version of
   record at that SHA [R0011].
3. **Reopen**: a revision of an agreed spec opens a new delta on a new branch and
   runs the same way, entry read included [R1602].

## The per-change stages

Once a spec is closed, each meaningful change [R0465] runs the per-change stages
in order [R0470]: acceptance criteria [R0472]; an architecture summary from the
TRD [R0483]; the unit's tests confirmed red [R0478]; implement to green with the
mechanical checks passing [R0485, R0493]; the one read above; the release package
[R0489]; the human's release gate [R0490]. A change is done when the definition
of done holds [R0509].
