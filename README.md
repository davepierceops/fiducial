# fiducial

Rules for getting real work out of LLM agents without losing track of what is true.

Use it for two kinds of project: software, or writing. To try either in two minutes or less:

**Software.** Download `fiducial-bundle-chief-of-staff.md` from the link below, put it in a fresh chat project, and say what you want built. It will tell you what it needs.

**Writing.** Download `fiducial-bundle-writer.md`, put it in a fresh chat project, and dump your notes. It drafts from an outline if you give it one, and from the conversation if you don't.

```
https://github.com/davepierceops/fiducial/releases/latest/download/fiducial-bundle-<slug>.md
```

That is the whole quick start. The rest of this file is the detail.

## What this is

An agent will write code, tests, specs, reviews, and essays all day, and will tell you they are done with the same confidence whether they are or not. fiducial is a set of rules that fixes that: every claim carries its evidence, every artifact lands somewhere you can inspect, and the decisions stay with you. Agents propose. You decide. The thesis, for software, is manage the proof, not the code.

The two paths:

- **Software.** A chief of staff runs the session; architect, spec reviewer, test designer, coder, reviewer, skeptic, and release manager do the work, each in its own lane, each handing back evidence rather than assurances.
- **Writing.** A writer drafts in your voice from an outline you agreed; a copy editor and a critic read it against that outline and say what moved.

Each role is one Markdown file, called a bundle. Load the bundle, and the session is that role.

## Which bundle to take

Every rule in this repository is keyed to a role. A bundle is the rules for one role, with every term it uses defined at the end. Take the bundle for the role the session is about to play.

| bundle | what the role does |
|---|---|
| `chief-of-staff` | Runs the decision session: assesses state, drafts directives, triages reports, opens and merges pull requests. Never carries out the work a directive specifies. |
| `architect-agent` | Derives a per-change architecture summary from the TRD; the tracker issue is cut from it. |
| `spec-reviewer-agent` | Gates the PRD, TRD, and acceptance criteria before agreement; runs the continuity scan. |
| `test-designer-agent` | Writes tests from acceptance criteria and confirms they fail on bad logic before any implementation. Edits tests only. |
| `coder-agent` | Writes the minimum code that turns the failing tests green, with lint, types, and static analysis passing as part of green. |
| `reviewer-agent` | The quality pass: maintainability, correctness, consistency, test adequacy, over the diff and the mechanical results. |
| `skeptic-risk-agent` | The skepticism pass: false confidence, mocked boundaries, config and deploy risk, release overclaims, over the whole evidence chain. |
| `release-manager-agent` | Assembles the change package and the ship recommendation. The human makes the release decision. |
| `context-quality-reviewer` | Runs intake: shapes a proposed rule, checks it against the store, sets its keys, lands it or refuses it with the id of the row that already says it. |
| `writer` | Drafts public prose in the author's voice from an agreed outline. |
| `copy-editor` | Edits prose for register and the public prose criteria without changing what it claims. |
| `critic` | Reads a draft against its outline and the criteria; a claim added or dropped is a finding. |

A session runs as the role its directive names. In chat, the session is the chief of staff, the writer, the copy editor, or the critic. Every other role runs as an execution session against a working tree.

## How to load one

The bundle is the first thing in context, before any task. Nothing else about loading it matters as much as that.

- **Chat** (Claude.ai or equivalent): add the file to the project, or paste it as the first message.
- **Claude Code**: commit a copy of the file to the repository and put one line in `CLAUDE.md` pointing at it, ahead of anything else.
- **Any other harness**: same idea. Get the file read, whole, before the session does anything.

## How to stay current

Bundles are release assets, and the asset name carries no timestamp, so the URL above is stable. When a release lands, replace the file. Tags are dated (`v2026.09.07`), so the tag says how old a bundle is; the header inside the file names the commit it was generated from, so a session can tell which version of the methodology it is running under.

## How to make it yours

The rules are a store, not a document: one rule per file under `rules/`, each with an id, an instruction, and free key-value pairs. A bundle is a query over that store. `bin/bundle --where role=writer` selects the rows carrying that value, the process documents the same query selects, and every definition a selected row uses. Clone the repository and run it; the store needs Python and git and nothing else. A new role is a new value on the `role` key and one line in `process/named-queries.md`; the tool does not change.

A rule enters the store through one gate, intake. Propose it in a sentence. A context-quality-reviewer session shapes it into one instruction an agent can act on, checks it against the store for a row that already says it, sets its keys, and lands one commit. There is no status field; a row in `rules/` is in force. If the vocabulary or the rules do not fit your practice, fork the store and run intake against your own. The model is in the rule-store PRD under `specs/`.

## What it asks of your repository

Agents push and merge. That is safe only because the default branch cannot be rewritten, so before the methodology governs work in a repository:

- `main` is protected: no force-push, no deletion, changes land by pull request, and the protection binds administrators too.
- The copy of the bundle the repository carries is pinned to a release tag. Bumping the tag is how a release is adopted.

Branch protection lives in the forge's settings, where nothing in the repository can check it. Confirm it by hand, once, before the first agent session.
