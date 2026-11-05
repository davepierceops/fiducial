"""Emission targets for `bin/bundle --emit <target>` (SPEC.md §7, DEC-001400).

The store is the source; a target turns a row set into the files one harness
loads. One module per target under this package, registered by name in
`targets()` below. This docstring and the `Target` base class are the whole
interface: a new target (the `codex` target of the subtraction plan's package
3b, say) is one module here, one line in `targets()`, one `tiers.json` column and
its tests — nothing else in `bin/` changes.

HOW `bin/bundle` CALLS A TARGET
-------------------------------

    bin/bundle --emit <target> --out DIR [--where k=v ...] [--name NAME]

The CLI builds one `EmitInputs` and calls `target.emit(inputs)`. The target
returns an `Emission` — a mapping of repo-relative paths to file text, plus
the subset to mark executable — or raises `EmitError` with one line saying
why. The CLI writes the files under DIR and prints each path written; on
`EmitError` it prints the line to stderr, exits 2, and writes nothing. No
target touches the filesystem or git: `EmitInputs` carries everything it may
read, which is what keeps a target testable with rows built in memory.

WHAT A TARGET IS GIVEN (`EmitInputs`)
-------------------------------------

- `rows`: every row of the store, rules and process documents alike, as
  `rulestore.store.Row` objects. `row.kind` is `"rule"` or `"process"`;
  `row.keys` holds the frontmatter as `{key: [values]}` (values lowercased
  except `paths`); `row.body` is the agent form, `row.human` the `## Human`
  note or `None`; `row.path` the repo-relative source path. Retired rows are
  never present.
- `sequences`: the `(topic_positions, process_positions)` pair from
  `process/named-queries.md`, for `rulestore.query.select`'s ordering.
- `where`: the parsed `--where` query as `{key: value}`, or `None` when the
  user gave none. A target declares with `takes_query` whether it needs one
  (`"required"`), tolerates one (`"optional"`) or refuses one (`"none"`);
  the CLI enforces that before calling `emit`.
- `name`: `--name`, or `None`.
- `repo`, `head`: the store repository's `owner/repo` label and HEAD SHA, for
  provenance headers. `generated` is the UTC timestamp `YYYYMMDDTHHMMSSZ`;
  use it only in the `bundle` target's header — a harness tree is committed
  into the adopting repository and must be byte-stable across runs over the
  same store, so a harness target never emits the timestamp.
- `tiers`: the parsed tier map, `tiers.json` in this package — see
  `load_tiers`. `tiers["harnesses"][<harness>][<tier>]` is the model name
  the harness loads for `frontier`, `solid` or `cheap`;
  `tiers["roles"][<role>]` is the tier a role runs at. A harness target reads
  its own column and nothing else about models (R0259, DEC-001270: rows
  speak in tiers, the emitter names models).
- `hooks`: `{name: script_text}` for every file under `bin/hooks/`, the hook
  scripts the `enforce: hook` rows' blocks invoke by `bin/hooks/<name>`. A
  harness target copies the scripts it needs into its tree and rewrites each
  block's command to point there; it must not rewrite the script.

THE ROWS A TARGET READS BY `enforce:`
-------------------------------------

A row without `enforce:` is a judgment row: its body is text the model
reads. A row with `enforce:` leaves the store by a mechanism, and its body
ends in a fenced yaml block that `blocks.parse` reads (see that module):

- `enforce: hook` — `event`, `matcher`, `command: bin/hooks/<name> [args]`,
  and `scope: agent` when the hook belongs in the agent file of the row's
  role rather than the repo's settings. Any prose before the block is the
  principle the hook enforces, emitted as text where the harness loads
  text; a block-only row has none.
- `enforce: deny` — `deny:` a list of `Tool(pattern)` entries in Claude
  Code's permission syntax. A harness with no deny rules turns each into a
  `PreToolUse` hook (DEC-001220).
- `enforce: agent` — `field: description` or `field: model`; the body is the
  field's text for the row's role (`model` is computed from `tiers`, the
  body is the principle).
- `enforce: skill` — `skill: <name>` or `skill: [<name>, ...]`; the row's
  content lives in the process document of that name and is emitted nowhere
  as a row. A role whose rows name a skill is given that skill.

Process documents (`row.kind == "process"`) are the skills: one `SKILL.md`
per document, named by its file stem, described by its first sentence; the
`gate` document carries `disable-model-invocation: true`;
`project-setup` and `named-queries` are not skills (`common.NOT_A_SKILL`; the
plan, §3a). Two further conventions a target should know: a note the target
returns starting `warning:` is printed by the CLI without the `note:` prefix;
and the spill rule (DEC, 2026-11-04) — a standing row whose first topic is a
process-document stem leaves the standing file and is appended under `## Rules`
in that document's skill — is implemented inline in `claude_code.emit`; a
harness with no skill directory keeps those rows in its standing file, and a
target that needs the grouping may lift it into `common`.

ADDING A TARGET
---------------

1. Write `bin/rulestore/emit/<name>.py` with a `Target` subclass; set
   `name`, `takes_query`, and implement `emit`. Import only the standard
   library, `rulestore.query`, `rulestore.terms`, `rulestore.render` and
   `rulestore.emit.blocks` and `rulestore.emit.common` (the standing selection,
   `Enforced`/`read_enforced`, `text_of`/`render_rows`, `first_sentence`,
   `skill_documents`, `topic_stem`, `NOT_A_SKILL`, `NO_MODEL_INVOCATION`: what
   every harness shares); take no name from `rulestore.store` but `Row`.
2. Add the class to the tuple in `targets()` below.
3. Add the harness's column to `tiers.json` — three model names.
4. Add `bin/tests/test_emit_<name>.py` with a fixture for every row carrying
   `enforce:` (`tests.emit_fixtures.emit_store_files` is the fixture store the
   claude-code tests use; reuse it) and a run of `bin/bundle --emit <name>`
   against a stand-in repository.

The `claude_code` module is the worked example; `bundle` is the smallest.
"""

from __future__ import annotations

import dataclasses
import json
import pathlib

#: The tier map: `{"harnesses": {<harness>: {frontier|solid|cheap: model}},
#: "roles": {<role>: tier}}`. One file, read by the emitters, never a row.
TIERS_PATH = pathlib.Path(__file__).with_name("tiers.json")

TIER_NAMES = ("frontier", "solid", "cheap")


class EmitError(Exception):
    """A refusal: one line, printed to stderr by the CLI, nothing written."""


@dataclasses.dataclass
class EmitInputs:
    rows: list
    sequences: tuple = ([], [])
    where: dict | None = None
    name: str | None = None
    repo: str = ""
    head: str | None = None
    generated: str = ""
    tiers: dict = dataclasses.field(default_factory=dict)
    hooks: dict = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class Emission:
    """`files`: repo-relative path -> text. `executable`: the paths to chmod +x.
    `notes`: lines the CLI prints to stderr after writing — gaps the human
    should know about (a skill a row names that no document provides, a
    block the harness cannot honour as written) that are not refusals."""

    files: dict = dataclasses.field(default_factory=dict)
    executable: set = dataclasses.field(default_factory=set)
    notes: list = dataclasses.field(default_factory=list)


class Target:
    """One emission target. Subclass, set the two class attributes, implement
    `emit`. `name` is the `--emit` value; `takes_query` is `"required"`,
    `"optional"` or `"none"`."""

    name = ""
    takes_query = "none"

    def emit(self, inputs: EmitInputs) -> Emission:
        raise NotImplementedError


def load_tiers(path=TIERS_PATH):
    """The tier map, validated: every harness column names all three tiers."""
    data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    for harness, column in data.get("harnesses", {}).items():
        missing = [tier for tier in TIER_NAMES if tier not in column]
        if missing:
            raise EmitError(
                "tiers.json: harness %r lacks tiers %s" % (harness, ", ".join(missing))
            )
    for role, tier in data.get("roles", {}).items():
        if tier not in TIER_NAMES:
            raise EmitError("tiers.json: role %r has tier %r, not one of %s"
                            % (role, tier, "|".join(TIER_NAMES)))
    return data


def targets():
    """`{name: Target instance}` — the registry. Import here, not at module
    top, so a broken target module fails at `--emit` time with its name."""
    from . import bundle, claude_code, codex

    registry = {}
    for cls in (bundle.BundleTarget, claude_code.ClaudeCodeTarget, codex.CodexTarget):
        registry[cls.name] = cls()
    return registry
