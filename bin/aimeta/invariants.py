"""The single reader of the directive-invariants document.

TRD §3.1, §3.2, §3.3, §3.4. Both binaries reach this module rather than the
file, so the disposition label, the marker grammar, the preamble tolerance and
every region's text have one definition instead of two agreeing copies. A
second definition anywhere — a regex in the lint, a string constant in the
generator — is the defect AC-DT-02 scans for.

Resolution is against **committed** content, and the tree it resolves in is
the methodology home rather than the repository the tool was invoked in
(§3.2). There is no working-tree fallback: a section whose committed body
cannot be read is a section that is not there, and refusing is what keeps
AC-DT-01 literal.
"""

from __future__ import annotations

import pathlib
import re

from . import cli, repo

#: The governed document this module is the only reader of.
RELPATH = "skills/directive-invariants.md"

#: Names §3.3's tables address sections by, held here so a caller never spells
#: a heading twice. Each is a key of the parsed mapping, never a marker.
HEADING_GENERAL = "Heading (general)"
HEADING_CYCLE = "Heading (cycle)"
ROUTE_AND_MODEL = "Route and model"
FIRST_ACT = "First act"
DISPOSITION_PROMPT = "Working-tree disposition prompt"
BASE_VERIFICATION = "Base verification"
COMPANIONS = "Companions"
TASK = "Task"
SANDBOX = "Sandbox constraints"
VERIFICATION = "Verification steps"
STOP_CONDITIONS = "Stop conditions"
REPORT_FORMAT = "Report format"
CLAIM_LABELS = "Claim labels"
DECISIONS = "Decisions"
DEFERRED = "Deferred"
EXECUTION_NOTES = "Execution notes"
SOURCE_MANIFEST = "Source manifest"
DISPOSITION_LABEL = "Disposition label"
MARKER_SYNTAX = "Marker syntax"
PREAMBLE_MARKERS = "Preamble markers"
MATCH_PHRASES = "Match phrases"

_SECTION_HEADING = re.compile(r"^## (.+?)\s*$")
_FENCE = re.compile(r"^(`{3,}|~{3,})")
_ELEMENT_LABEL = re.compile(r"^(M[1-8]):\s*$")

#: §3.3's marker grammar, compiled from the grammar `Marker syntax` states.
_ATX_MARKER = re.compile(r"^#{1,6} (.+)$")
_CAPS_MARKER = re.compile(r"^[A-Z0-9-]+(?: [A-Z0-9-]+)*")
_CAPS_MINIMUM = 3

#: §3.2's substitution syntax. The set of names is closed and fixed per region
#: by §3.3's tables; the caller supplies the subset its region admits.
_OPEN = "{" * 2
_CLOSE = "}" * 2

_FRONTMATTER_FENCE = "---"


def marker_token(line):
    """The marker token `line` carries, or None when it is not a marker."""
    heading = _ATX_MARKER.match(line)
    if heading is not None:
        return heading.group(1).strip()
    run = _CAPS_MARKER.match(line)
    if run is not None and len(run.group(0)) >= _CAPS_MINIMUM:
        return run.group(0)
    return None


def _without_frontmatter(text):
    """Drop a leading YAML frontmatter block; the fixture document carries none."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != _FRONTMATTER_FENCE:
        return text
    for index in range(1, len(lines)):
        if lines[index].strip() == _FRONTMATTER_FENCE:
            return "\n".join(lines[index + 1:])
    return text


def parse_sections(text):
    """`{name: body}` for every section, per §3.3's schema.

    A section's body runs from its heading to the next `##` heading, under the
    rule that the first non-blank line of a body is always body: three region
    sections carry an ATX marker as their first body line, and a parse that
    ended a section at the first `##` inside it would read all three as empty
    and invent three sections that are not there.
    """
    sections = {}
    name = None
    body = []
    started = False
    for line in _without_frontmatter(text).split("\n"):
        heading = _SECTION_HEADING.match(line)
        if heading is not None and (name is None or started):
            if name is not None:
                sections[name] = _trimmed(body)
            name = heading.group(1)
            body = []
            started = False
            continue
        if name is None:
            continue
        if line.strip():
            started = True
        body.append(line)
    if name is not None:
        sections[name] = _trimmed(body)
    return sections


def _trimmed(body):
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return "\n".join(body) + "\n" if body else ""


def fenced_blocks(body):
    """Each fenced block's content lines, in order of appearance."""
    blocks = []
    current = None
    char = None
    length = 0
    for line in body.split("\n"):
        opening = _FENCE.match(line)
        if current is None:
            if opening is not None:
                current = []
                char = opening.group(1)[0]
                length = len(opening.group(1))
            continue
        if (
            opening is not None
            and opening.group(1)[0] == char
            and len(opening.group(1)) >= length
            and line[len(opening.group(1)):].strip() == ""
        ):
            blocks.append(current)
            current = None
            continue
        current.append(line)
    if current is not None:
        blocks.append(current)
    return blocks


def _content_lines(block):
    return [line for line in block if line.strip()]


class Document:
    """The invariants document at one committed revision of the home."""

    def __init__(self, home, sha, text):
        self.home = home
        self.relpath = RELPATH
        self.sha = sha
        self.text = text
        self._sections = parse_sections(text)

    def section(self, name):
        """One section's body, or FM-G2's refusal naming it."""
        body = self._sections.get(name)
        if not body:
            raise cli.ToolError(
                "[invariants-section-missing] observed: %s carries no `%s` section, "
                "so the region it sources cannot be assembled" % (self.relpath, name),
                cli.EXIT_PRECONDITION,
            )
        return body

    def has_section(self, name):
        return bool(self._sections.get(name))

    # -- §3.4's three parts, all read from the one `Disposition label` section.

    def label_literal(self):
        """The literal the generator emits, as the section's first fence holds it."""
        blocks = fenced_blocks(self.section(DISPOSITION_LABEL))
        for block in blocks:
            content = _content_lines(block)
            if content:
                return content[0].strip()
        raise cli.ToolError(
            "[invariants-section-missing] observed: %s fences no disposition label"
            % self.relpath,
            cli.EXIT_PRECONDITION,
        )

    def label(self):
        """The label without its trailing colon — the token a marker carries."""
        return self.label_literal().rstrip(":").rstrip()

    def label_line(self):
        """The label as the generator emits it: at column 0, one colon, no text."""
        return "%s:" % self.label()

    def sole_tree_sentence(self):
        """The canonical sole-tree form, from the same section's last fence."""
        blocks = fenced_blocks(self.section(DISPOSITION_LABEL))
        for block in reversed(blocks):
            content = _content_lines(block)
            if content:
                return content[0].strip()
        return ""

    def matches_label(self, line):
        """§3.4's match rule, applied to one line's leading content.

        Case-sensitive, exact in the leading literal, with any text permitted
        between the literal and the first colon on the line.
        """
        label = self.label()
        if not line.startswith(label):
            return False
        return ":" in line[len(label):]

    # -- the lint's other compiled strings.

    def preamble_markers(self):
        """Markers admitted before the first-act statement (M5's tolerance)."""
        blocks = fenced_blocks(self.section(PREAMBLE_MARKERS))
        markers = []
        for block in blocks:
            markers.extend(line.strip() for line in block if line.strip())
        return markers

    def match_phrases(self):
        """`{element: [phrase]}` — §3.6's phrases, one fenced block per element.

        M2, M3 and M8 have no block, and their absence is not an omission: M2
        and M8 match no phrase at all, and M3's strings are the label
        section's.
        """
        phrases = {}
        element = None
        collecting = None
        for line in self.section(MATCH_PHRASES).split("\n"):
            label = _ELEMENT_LABEL.match(line.strip())
            if label is not None and collecting is None:
                element = label.group(1)
                continue
            if _FENCE.match(line) is not None:
                if collecting is None:
                    collecting = []
                    continue
                if element is not None:
                    phrases[element] = collecting
                element = None
                collecting = None
                continue
            if collecting is not None and line.strip():
                collecting.append(line.strip())
        return phrases

    def marker_syntax(self):
        """The grammar's own statement, for a report that cites its source."""
        return self.section(MARKER_SYNTAX)


def substitute(body, values, where):
    """Replace `{{name}}` from a closed set; `{{{{` is a literal brace pair.

    An unrecognised placeholder is FM-G4's refusal, never a silent
    pass-through: the set is small and enumerable on purpose, and a name the
    generator cannot bind is a section it cannot render honestly.
    """
    out = []
    index = 0
    doubled = _OPEN + _OPEN
    while index < len(body):
        if body.startswith(doubled, index):
            out.append(_OPEN)
            index += len(doubled)
            continue
        if body.startswith(_OPEN, index):
            end = body.find(_CLOSE, index + len(_OPEN))
            if end != -1:
                name = body[index + len(_OPEN):end]
                if name not in values:
                    raise cli.ToolError(
                        "[invariants-placeholder-unknown] observed: the `%s` section "
                        "carries a placeholder this generator does not bind: %s"
                        % (where, name),
                        cli.EXIT_PRECONDITION,
                    )
                out.append(values[name])
                index = end + len(_CLOSE)
                continue
        out.append(body[index])
        index += 1
    return "".join(out)


def load(root, allow_dirty=False):
    """The document at its last commit in the methodology home (§3.2).

    FM-G1: an absent document, an unreadable one, or a home carrying no
    committed revision of it is a refusal before anything is written.
    FM-G3: an uncommitted modification is a refusal, downgraded to a `WARN` by
    `--allow-dirty` — AC-CO-5's shape applied to a second class of input.
    """
    try:
        home = repo.methodology_home(root)
    except LookupError as exc:
        raise cli.ToolError(str(exc), cli.EXIT_USAGE)

    # §3.6 step 4: "a document that is not there is still invariants-missing
    # rather than invariants-dirty." An uncommitted deletion still has a
    # commit touching the path (`last_commit_sha` looks at history, not the
    # working tree), so absence from the working tree is checked first and
    # separately from the dirty check below.
    if not (pathlib.Path(home) / RELPATH).is_file():
        raise cli.ToolError(
            "[invariants-missing] observed: %s is not present in the methodology "
            "home at %s; there is no working-tree fallback" % (RELPATH, home),
            cli.EXIT_PRECONDITION,
        )

    sha = repo.last_commit_sha(home, RELPATH)
    if sha is None:
        raise cli.ToolError(
            "[invariants-missing] observed: %s has no committed revision in the "
            "methodology home at %s; there is no working-tree fallback"
            % (RELPATH, home),
            cli.EXIT_PRECONDITION,
        )
    try:
        text = repo.file_at_rev(home, sha, RELPATH)
    except UnicodeDecodeError:
        text = None
    if text is None:
        raise cli.ToolError(
            "[invariants-missing] observed: cannot read %s at %s" % (RELPATH, sha),
            cli.EXIT_PRECONDITION,
        )

    code, out, _ = repo.run(["status", "--porcelain", "--", RELPATH], cwd=home)
    if code == 0 and out.strip():
        if not allow_dirty:
            raise cli.ToolError(
                "[invariants-dirty] observed: %s has uncommitted modifications in "
                "the methodology home, so the skeleton would not match the revision "
                "its manifest names" % RELPATH,
                cli.EXIT_PRECONDITION,
            )
        cli.diagnostic(
            "WARN",
            RELPATH,
            "invariants-dirty",
            "observed: uncommitted modifications; the skeleton carries the "
            "committed revision",
        )
    return Document(home, sha, text)
