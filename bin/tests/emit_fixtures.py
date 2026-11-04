"""The fixture store for the emit targets (the plan, §3a acceptance).

One row per `enforce:` row of the real store as of `19f6760` — the twelve
hook/deny rows, the five agent rows, four skill rows carrying the four skill
names and the one list-valued block (R0506) — with their fenced blocks
verbatim and their prose cut short; one row carrying `paths:`; a few
judgment rows and a definition; two stub process documents (`gate`, the
skill that forbids model invocation, and `release`) beside the fixture's
`named-queries`. Built with `tests.helpers.rs_row`, so the on-disk shape is
the store's.
"""

from __future__ import annotations

from tests.helpers import rs_process, rs_row

ALL_ROLES = [
    "architect-agent", "chief-of-staff", "coder-agent", "context-quality-reviewer",
    "copy-editor", "critic", "release-manager-agent", "reviewer-agent",
    "skeptic-risk-agent", "spec-reviewer-agent", "test-designer-agent", "writer",
]
BOTH = ["decision", "execution"]
BOTH_CORPORA = ["software", "writing"]

HOOK_IDS = ("R0583", "R1408", "R0196", "R1414", "R1605", "R0934", "R0720", "R0091", "R1156")
DENY_IDS = ("R0164", "R0203", "R0564")
AGENT_IDS = ("R0259", "R0939", "R1031", "R1056", "R1141")
SKILL_IDS = ("R0486", "R0506", "R0551", "R0944")
PATHS_ID = "R0500"


def _hook(event, matcher, command, scope=None, comment=None):
    lines = ["```yaml"]
    if scope:
        lines.append("scope: %s" % scope)
    lines += ["event: %s" % event, "matcher: %s" % matcher, "command: %s" % command]
    if comment:
        lines.append("# %s" % comment)
    lines.append("```")
    return "\n".join(lines)


def _deny(*patterns):
    return "```yaml\ndeny:\n" + "".join("  - %s\n" % p for p in patterns) + "```"


def emit_store_files():
    files = {
        # ---------------------------------------------------- judgment rows
        "rules/R0001.md": rs_row(
            "R0001", "Propose; do not decide. Approval is the human's.",
            order=10, topic=["core"], role=ALL_ROLES, session=BOTH,
            corpus=BOTH_CORPORA, verb="require", term=None,
            human="DEC-000001: the human decides.",
        ),
        "rules/R0002.md": rs_row(
            "R0002", "State the obligation at its shortest, in one tranche.",
            order=20, topic=["chief-of-staff"], role=["chief-of-staff"],
            session=["decision"], corpus=["software"], verb="require", term=None,
        ),
        "rules/R0003.md": rs_row(
            "R0003", "Run the red gate before any implementation.",
            order=40, topic=["coder-agent"], role=["coder-agent"],
            session=["execution"], corpus=["software"], verb="require", term=None,
        ),
        "rules/R0004.md": rs_row(
            "R0004", "Read the whole delta before the first finding.",
            order=10, topic=["reviewer"], role=["reviewer-agent", "skeptic-risk-agent"],
            session=["execution"], corpus=["software"], verb="require", term=None,
        ),
        "rules/R0100.md": rs_row(
            "R0100", "A tranche is one concurrent workstream of build work.",
            order=20, topic=["lexicon"], verb="define", term=["tranche", "tranches"],
        ),
        # ------------------------------------------------------- paths: row
        "rules/%s.md" % PATHS_ID: rs_row(
            PATHS_ID, "A test asserts one behaviour and names it.",
            order=10, topic=["verification"], role=["coder-agent", "test-designer-agent"],
            session=["execution"], corpus=["software"], verb="require", term=None,
            paths=["tests/**", "SPEC.md"],
        ),
        # ------------------------------------------------------- deny rows
        "rules/R0164.md": rs_row(
            "R0164",
            "Never let a secret value enter context.\n\n"
            + _deny("Read(./.env)", "Read(./**/.env)", "Read(~/.ssh/**)", "Bash(printenv*)"),
            order=10, topic=["core"], role=ALL_ROLES, session=BOTH, corpus=BOTH_CORPORA,
            verb="forbid", term=None, enforce="deny",
            human="A deny matches tool calls, not intent.",
        ),
        "rules/R0203.md": rs_row(
            "R0203",
            "Treat every deployed or production system as off limits.\n\n"
            + _deny("Bash(kubectl apply*)", "Bash(terraform apply*)", "Bash(ssh *prod*)"),
            order=20, topic=["core"], role=ALL_ROLES, session=BOTH, corpus=BOTH_CORPORA,
            verb="require", term=None, enforce="deny",
        ),
        "rules/R0564.md": rs_row(
            "R0564",
            "Push plainly; never force-push.\n\n"
            + _deny("Bash(git push --force*)", "Bash(git push -f*)", "Bash(git push * +*)"),
            order=10, topic=["commit-control"], role=ALL_ROLES, session=BOTH,
            corpus=BOTH_CORPORA, verb="require", term=None, enforce="deny",
        ),
        # ------------------------------------------------------- hook rows
        "rules/R0583.md": rs_row(
            "R0583",
            "Append to `decisions/log.md`; never edit or delete an entry already there.\n\n"
            + _hook("PreToolUse", "Edit|Write", "bin/hooks/decision-log-append-only"),
            order=30, topic=["decision-log-policy"], role=ALL_ROLES, session=BOTH,
            corpus=BOTH_CORPORA, verb="require", term=None, enforce="hook",
        ),
        "rules/R1408.md": rs_row(
            "R1408",
            "Never rewrite an existing review artifact to match a later schema.\n\n"
            + _hook("PreToolUse", "Edit|Write", "bin/hooks/review-artifact-immutable",
                    comment="refuses a write to a reviews/ file tracked at HEAD"),
            order=110, topic=["review-artifact-schema"],
            role=["reviewer-agent", "chief-of-staff"], session=BOTH, corpus=BOTH_CORPORA,
            verb="forbid", term=None, enforce="hook",
        ),
        "rules/R0196.md": rs_row(
            "R0196",
            "Name a file you generate `<descriptor>-<timestamp>`.\n\n"
            + _hook("PostToolUse", "Edit|Write", "bin/hooks/store-lint --check generated-filename"),
            order=260, topic=["core"], role=ALL_ROLES, session=BOTH, corpus=BOTH_CORPORA,
            verb="require", term=None, enforce="hook",
        ),
        "rules/R1414.md": rs_row(
            "R1414",
            "Carry one overall `Verdict:` line and one `Verdict (<pass>):` line per pass.\n\n"
            + _hook("PostToolUse", "Edit|Write", "bin/hooks/store-lint --check verdict-lines"),
            order=40, topic=["review-artifact-schema"],
            role=["reviewer-agent", "chief-of-staff"], session=BOTH, corpus=BOTH_CORPORA,
            verb="require", term=None, enforce="hook",
        ),
        "rules/R1605.md": rs_row(
            "R1605",
            "A row cites another row only by its ID in square brackets.\n\n"
            + _hook("PostToolUse", "Edit|Write", "bin/hooks/store-lint --check citations",
                    comment="store-lint also carries R0264's four criteria"),
            order=60, topic=["intake"], role=["chief-of-staff", "context-quality-reviewer"],
            session=BOTH, corpus=BOTH_CORPORA, verb="require", term=None, enforce="hook",
        ),
        "rules/R0934.md": rs_row(
            "R0934",
            _hook("PreToolUse", "Edit|Write", "bin/hooks/intake-branch-guard"),
            order=470, topic=["chief-of-staff"], role=["chief-of-staff"],
            session=["decision"], corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="hook",
            human="The hook matches the tool call, not intent: an edit under `rules/` "
                  "or `process/` passes only on a branch named `intake/*`.",
        ),
        "rules/R0720.md": rs_row(
            "R0720",
            _hook("PostToolUse", "Bash", "bin/hooks/push-readback"),
            order=10, topic=["remote-write-verification-policy"],
            role=["chief-of-staff", "coder-agent", "writer"], session=BOTH,
            corpus=BOTH_CORPORA, verb="require", term=None, enforce="hook",
            human="After a `git push` it fetches the remote and prints the ref's SHA.",
        ),
        "rules/R0091.md": rs_row(
            "R0091",
            "Edit specs and nothing else; a change you need outside your lane is a "
            "finding, not an edit.\n\n"
            + _hook("PreToolUse", "Edit|Write", "bin/hooks/lane-guard --lane specs",
                    scope="agent"),
            order=270, topic=["change-flow"], role=["architect-agent"],
            session=["execution"], corpus=["software"], verb="require", term=None,
            enforce="hook",
        ),
        "rules/R1156.md": rs_row(
            "R1156",
            "Edit tests and nothing else; a change you need outside your lane is a "
            "finding, not an edit.\n\n"
            + _hook("PreToolUse", "Edit|Write", "bin/hooks/lane-guard --lane tests",
                    scope="agent"),
            order=150, topic=["test-designer"], role=["test-designer-agent"],
            session=["execution"], corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="hook",
        ),
        # ------------------------------------------------------ agent rows
        "rules/R0259.md": rs_row(
            "R0259",
            "Choose the model tier by the workload: frontier, solid, cheap.\n\n"
            "```yaml\nfield: model\n```",
            order=190, topic=["decision-layer"],
            role=["chief-of-staff", "writer", "copy-editor", "critic"],
            session=["decision"], corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="agent",
        ),
        "rules/R0939.md": rs_row(
            "R0939",
            "Implement changes according to the spec and the test plan.\n\n"
            "```yaml\nfield: description\n```",
            order=20, topic=["coder-agent"], role=["coder-agent"], session=["execution"],
            corpus=BOTH_CORPORA, verb="require", term=None, enforce="agent",
        ),
        "rules/R1031.md": rs_row(
            "R1031",
            "Produce a ship/no-ship release recommendation.\n\n"
            "```yaml\nfield: description\n```",
            order=20, topic=["release-manager-agent"], role=["release-manager-agent"],
            session=["execution"], corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="agent",
        ),
        "rules/R1056.md": rs_row(
            "R1056",
            "Do not review spec documents; they are the Spec Reviewer's.\n\n"
            "```yaml\nfield: description\n```",
            order=110, topic=["reviewer"], role=["reviewer-agent"], session=["execution"],
            corpus=BOTH_CORPORA, verb="forbid", term=None, enforce="agent",
            human="In force until a published code-review standard replaces it.",
        ),
        "rules/R1141.md": rs_row(
            "R1141",
            "Define how correctness will be evaluated before implementation begins.\n\n"
            "```yaml\nfield: description\n```",
            order=20, topic=["test-designer"], role=["test-designer-agent"],
            session=["execution"], corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="agent",
        ),
        # ------------------------------------------------------ skill rows
        "rules/R0486.md": rs_row(
            "R0486",
            "Give a unit's implementation to a different agent from the one that "
            "wrote the unit's tests.\n\n```yaml\nskill: build\n```",
            order=180, topic=["change-flow"], role=["coder-agent", "test-designer-agent"],
            session=["execution"], corpus=["software"], verb="require", term=None,
            enforce="skill",
        ),
        "rules/R0506.md": rs_row(
            "R0506",
            "Reporting substantial work, state role, intent, evidence, boundary, gaps, "
            "recommendation.\n\n```yaml\nskill: [release, review]\n```",
            order=200, topic=["release-manager-agent"],
            role=["release-manager-agent", "reviewer-agent", "skeptic-risk-agent"],
            session=["execution"], corpus=["software"], verb="require", term=None,
            enforce="skill",
        ),
        "rules/R0551.md": rs_row(
            "R0551",
            "Open one `human-gate` tracker issue for a change when it is ready for the "
            "gate.\n\n```yaml\nskill: gate\n```",
            order=40, topic=["change-control"], role=["chief-of-staff"],
            session=["decision"], corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="skill",
        ),
        "rules/R0944.md": rs_row(
            "R0944",
            "Record each intake as a review artifact.\n\n```yaml\nskill: intake\n```",
            order=40, topic=["intake"], role=["context-quality-reviewer"],
            session=["execution"], corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="skill",
        ),
        # --------------------------------------------------- retired: never
        "rules/retired/R0900.md": rs_row(
            "R0900", "A retired row is never emitted.",
            order=5, topic=["core"], role=["chief-of-staff"], session=["decision"],
            corpus=["software"], verb="require", term=None,
        ),
        # ---------------------------------------------- process documents
        "process/gate.md": rs_process(
            "# Process: Gate\n\nRequest the human's go/no-go for a consequential "
            "change. Open the issue first.\n\n## Steps\n\n1. Open the issue.\n",
            order=10, topic=["gate"], role=["chief-of-staff"], session=["decision"],
            corpus=["software"],
        ),
        "process/release.md": rs_process(
            "# Process: Release\n\nAssemble the change package! Then recommend.\n",
            order=20, topic=["release"], role=["release-manager-agent"],
            session=["execution"], corpus=["software"],
        ),
        "process/project-setup.md": rs_process(
            "# Process: Project Setup\n\nCreate the labels.\n",
            order=100, topic=["project-setup"], session=["decision"], corpus=["software"],
        ),
        "process/named-queries.md": rs_process(
            "# Named Queries (fixture)\n\n## The list\n\n```text\n"
            "chief-of-staff role=chief-of-staff\n```\n\n## Sequence\n\n```text\n"
            "core\nchief-of-staff coder-agent reviewer test-designer\n"
            "decision-layer\nintake\nchange-flow change-control commit-control\n```\n\n"
            "```text\ngate\nrelease\n```\n",
            order=120, topic=["named-queries"], role=["chief-of-staff"],
            session=["decision"], corpus=["software"],
        ),
    }
    return files
