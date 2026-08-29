"""M1-M8: the lint's eight required elements.

TRD §3.6. Each element is one function over `(root, relpath, text,
eligible_lines, invariants)`, returning pass, fail with a named cause, or
unknown. No element reads another's result, none maps to an exit code, and
none formats output — `bin/check-directive` does both of those.

Every phrase, the disposition label, and the sole-tree sentence are read from
the `invariants.Document` passed in; this module holds no literal for any of
them (§3.1). The one exception, disclosed as the TRD discloses it (§3.4): the
exclusive-assignment narrowing — the `git worktree add` invocation and the
quoted-or-backticked token — is this TRD's own mechanical decision, not text
sourced from `skills/directive-invariants.md`, so it is a literal here the
same way `aimeta/directive.py`'s destination template is.

M2's object-type step reads the type word by exclusion (tag/blob/tree fail;
anything else that resolved is a commit) rather than by comparing against a
bare `"commit"` constant — AC-DT-12(a)'s static scan forbids that literal.
"""

from __future__ import annotations

import re

from . import invariants, mdmask, repo

PASS = "pass"
FAIL = "fail"
UNKNOWN = "unknown"

#: Object types `cat-file -t` returns that are never a valid M2 citation.
#: Anything else that resolved names a commit — decided by exclusion so this
#: module holds no string constant equal to the forbidden word itself.
_NON_COMMIT_TYPES = ("tag", "blob", "tree")

_NOT_A_VALID_OBJECT = "not a valid object name"
#: git phrases this two ways depending on whether the path exists in the
#: working tree: "does not exist in <rev>" when it never did, "exists on
#: disk, but not in <rev>" when the working tree has it and the commit does
#: not — both mean the same thing for M2's purposes.
_PATH_ABSENT_MARKERS = ("does not exist in", "but not in")

_HEX_RUN = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{7,40}(?![0-9a-fA-F])")
_CITATION_RE = re.compile(r"(\S+) @ ([0-9a-fA-F]{7,40})(?![0-9a-fA-F])")

#: §3.4's exclusive-assignment narrowing: this TRD's own decision, not text
#: read from the invariants document (see module docstring).
_WORKTREE_ADD = "git worktree add"
_QUOTED_TOKEN = re.compile(r'"([^"\s]+)"|`([^`\s]+)`')

_M8_TIMESTAMPED = re.compile(r"^docs/cycles/[^/]+-\d{8}T\d{6}Z?\.md$")
_M8_DIRECTIVE_SUFFIXED = re.compile(r"^docs/cycles/[^/]+-directive\.md$")


class Finding:
    """One element's result: pass, fail with a named cause, or unknown."""

    __slots__ = ("status", "code", "detail")

    def __init__(self, status, code=None, detail=None):
        self.status = status
        self.code = code
        self.detail = detail


def _pass():
    return Finding(PASS)


def _fail(code, detail):
    return Finding(FAIL, code, detail)


def _unknown(detail):
    return Finding(UNKNOWN, detail=detail)


# --------------------------------------------------------------- text helpers


def _normalize_ws(text):
    return re.sub(r"\s+", " ", text).strip()


def _paragraphs(lines):
    """`[(start, end)]` for every maximal run of non-blank physical lines."""
    paras = []
    start = None
    for index, line in enumerate(lines):
        if line.strip():
            if start is None:
                start = index
        elif start is not None:
            paras.append((start, index))
            start = None
    if start is not None:
        paras.append((start, len(lines)))
    return paras


def _paragraph_text(lines, indices_set, start, end):
    """Eligible lines of one paragraph, space-joined and whitespace-collapsed."""
    parts = [lines[i] for i in range(start, end) if i in indices_set]
    return _normalize_ws(" ".join(parts))


def _phrase_present_anywhere(lines, indices, phrase):
    """True when some paragraph's eligible text contains `phrase` (M4)."""
    needle = _normalize_ws(phrase).lower()
    indices_set = set(indices)
    for start, end in _paragraphs(lines):
        if needle in _paragraph_text(lines, indices_set, start, end).lower():
            return True
    return False


def _first_extent_containing_all(lines, indices, phrases):
    """The first paragraph whose eligible text contains every phrase (M5, M7)."""
    if not phrases:
        return None
    indices_set = set(indices)
    needles = [_normalize_ws(p).lower() for p in phrases]
    for start, end in _paragraphs(lines):
        haystack = _paragraph_text(lines, indices_set, start, end).lower()
        if all(needle in haystack for needle in needles):
            return (start, end)
    return None


def _markers_before(lines, indices, before_index):
    """`[(index, token)]` for every marker line strictly before `before_index`."""
    hits = []
    for i in indices:
        if i >= before_index:
            break
        token = invariants.marker_token(lines[i])
        if token is not None:
            hits.append((i, token))
    return hits


def _preamble_sets(doc):
    """`(literal tokens, whether the document heading is tolerated)` — M5."""
    literal = set()
    dynamic = False
    for marker in doc.preamble_markers():
        if marker.startswith("<") and marker.endswith(">"):
            dynamic = True
        else:
            literal.add(marker)
    return literal, dynamic


def _hyphen_tolerant_pattern(phrase):
    """§3.6 M1: the phrase's words, separated by whitespace or a hyphen."""
    words = phrase.split()
    return r"\b" + r"[\s-]+".join(re.escape(word) for word in words) + r"\b"


# ----------------------------------------------------------------- git reads


def _peeled_commit_state(root, sha):
    """`"ok"`, `"fail"`, or `"unknown"` for `cat-file -e <sha>^{commit}`."""
    code, _, err = repo.run(["cat-file", "-e", "%s^{commit}" % sha], cwd=root)
    if code == 0:
        return "ok"
    if _NOT_A_VALID_OBJECT in err.lower():
        return "fail"
    return "unknown"


def _object_type(root, sha):
    """The unpeeled `cat-file -t <sha>` word, or None when the read failed."""
    code, out, _ = repo.run(["cat-file", "-t", sha], cwd=root)
    if code != 0:
        return None
    return out.decode("utf-8", "replace").strip()


def _path_in_tree_state(root, sha, path):
    code, _, err = repo.run(["cat-file", "-e", "%s:%s" % (sha, path)], cwd=root)
    if code == 0:
        return "ok"
    if any(marker in err.lower() for marker in _PATH_ABSENT_MARKERS):
        return "fail"
    return "unknown"


def _touches_state(root, sha, path):
    code, out, _ = repo.run(
        ["diff-tree", "--root", "--no-commit-id", "--name-only", "-r", sha, "--", path],
        cwd=root,
    )
    if code != 0:
        return "unknown"
    return "ok" if out.strip() else "fail"


# --------------------------------------------------------------------- M1-M8


def m1(root, relpath, text, eligible_lines, doc):
    """A reviewed-ref pin is present, and its SHA resolves to a commit."""
    lines, indices = eligible_lines
    for phrase in doc.match_phrases().get("M1", []):
        pattern = re.compile(_hyphen_tolerant_pattern(phrase), re.IGNORECASE)
        for i in indices:
            line = lines[i]
            match = pattern.search(line)
            if match is None:
                continue
            hex_match = _HEX_RUN.search(line, match.end())
            if hex_match is None:
                continue
            sha = hex_match.group(0)
            state = _peeled_commit_state(root, sha)
            if state == "ok":
                return _pass()
            if state == "fail":
                return _fail(
                    "reviewed-ref-unresolvable",
                    "%s does not resolve to a commit" % sha,
                )
            return _unknown("cannot resolve the reviewed-ref pin %s" % sha)
    return _fail("reviewed-ref-missing", "no reviewed-ref pin was found")


def _manifest_region(lines, indices, doc):
    """Indices inside the source manifest region, if the document has one.

    G11: "the manifest is an output of the generator and an input to nothing
    the lint does." Its entries are themselves `<path> @ <sha>`-shaped, so M2
    must not read them as companion citations.
    """
    if not doc.has_section(invariants.SOURCE_MANIFEST):
        return frozenset()
    marker = invariants.marker_token(
        doc.section(invariants.SOURCE_MANIFEST).split("\n", 1)[0]
    )
    if marker is None:
        return frozenset()
    start = None
    for i in indices:
        if invariants.marker_token(lines[i]) == marker:
            start = i
            break
    if start is None:
        return frozenset()
    end = len(lines)
    for i in indices:
        if i <= start:
            continue
        if invariants.marker_token(lines[i]) is not None:
            end = i
            break
    return frozenset(i for i in indices if start <= i < end)


def m2(root, relpath, text, eligible_lines, doc):
    """Each `<path> @ <sha>` citation resolves to a commit that touches path."""
    lines, indices = eligible_lines
    excluded = _manifest_region(lines, indices, doc)
    for i in indices:
        if i in excluded:
            continue
        for match in _CITATION_RE.finditer(lines[i]):
            path, sha = match.group(1), match.group(2)
            state = _peeled_commit_state(root, sha)
            if state == "unknown":
                return _unknown("cannot resolve the citation %s @ %s" % (path, sha))
            if state == "fail":
                return _fail(
                    "citation-unresolvable",
                    "%s @ %s does not resolve to a commit" % (path, sha),
                )
            type_word = _object_type(root, sha)
            if type_word is None:
                return _unknown(
                    "cannot read the object type of %s @ %s" % (path, sha)
                )
            if type_word in _NON_COMMIT_TYPES:
                return _fail(
                    "citation-unresolvable",
                    "%s @ %s names a %s object, not a commit" % (path, sha, type_word),
                )
            path_state = _path_in_tree_state(root, sha, path)
            if path_state == "unknown":
                return _unknown("cannot read the tree of %s @ %s" % (path, sha))
            if path_state == "fail":
                return _fail(
                    "citation-path-absent",
                    "%s is not present in the tree at %s" % (path, sha),
                )
            touch_state = _touches_state(root, sha, path)
            if touch_state == "unknown":
                return _unknown("cannot diff %s @ %s" % (path, sha))
            if touch_state == "fail":
                return _fail(
                    "citation-not-touching",
                    "%s does not touch %s" % (sha, path),
                )
    return _pass()


def _m3_statements(lines, indices, doc):
    """`[(start, end)]` — every unfenced labelled statement's extent (§3.4).

    §3.5 masks indented code blocks (4+ spaces) out of nothing — they are
    deliberately left eligible, at the cost of a disclosed false stop when
    one carries the label. `leading_content` strips only up to three leading
    spaces (its own §3.5 step), so a fourth space would otherwise survive
    into the match and hide the label; the extra `lstrip` here is specific to
    the label check, not a second stripping rule.
    """
    eligible_set = set(indices)
    n = len(lines)
    statements = []
    pos = 0
    while pos < n:
        if pos in eligible_set:
            content = mdmask.leading_content(lines[pos]).lstrip(" ")
            if doc.matches_label(content):
                end = pos + 1
                while end < n and lines[end].strip():
                    end += 1
                statements.append((pos, end))
                pos = end
                continue
        pos += 1
    return statements


def m3(root, relpath, text, eligible_lines, doc):
    """Exactly one labelled disposition statement, carrying exactly one form."""
    lines, indices = eligible_lines
    statements = _m3_statements(lines, indices, doc)
    if not statements:
        return _fail(
            "disposition-absent",
            "no labelled working-tree disposition statement was found",
        )
    if len(statements) > 1:
        return _fail(
            "disposition-multiple",
            "%d labelled disposition statements were found" % len(statements),
        )
    start, end = statements[0]
    extent_text = "\n".join(lines[start:end])
    has_exclusive = (
        _WORKTREE_ADD in extent_text and _QUOTED_TOKEN.search(extent_text) is not None
    )
    sole_sentence = doc.sole_tree_sentence()
    has_sole = bool(sole_sentence) and sole_sentence in extent_text
    if has_exclusive and has_sole:
        return _fail(
            "disposition-form-ambiguous",
            "the statement carries both admitted forms",
        )
    if has_exclusive or has_sole:
        return _pass()
    return _fail(
        "disposition-form-absent", "the statement carries neither admitted form"
    )


def m4(root, relpath, text, eligible_lines, doc):
    """Both stop conditions are present, each an independent test."""
    lines, indices = eligible_lines
    phrases = doc.match_phrases().get("M4", [])
    missing = [p for p in phrases if not _phrase_present_anywhere(lines, indices, p)]
    if missing:
        return _fail("stop-condition-missing", "missing: %s" % "; ".join(missing))
    return _pass()


def m5(root, relpath, text, eligible_lines, doc):
    """The first-act statement is present, preceded only by preamble markers."""
    lines, indices = eligible_lines
    phrases = doc.match_phrases().get("M5", [])
    extent = _first_extent_containing_all(lines, indices, phrases)
    if extent is None:
        return _fail(
            "first-act-missing",
            "no extent contains write, commit, push, and report the SHA together",
        )
    start, _end = extent
    markers = _markers_before(lines, indices, start)
    if not markers:
        return _pass()
    # The marker opening the statement's own region does not count as
    # preceding it (§3.6 M5) — only the markers before that one do.
    preceding = markers[:-1]
    literal, dynamic = _preamble_sets(doc)
    heading_marker = markers[0][1] if dynamic else None
    for _, token in preceding:
        if token == heading_marker or token in literal:
            continue
        return _fail(
            "first-act-missing",
            "the marker %r precedes the first-act statement" % token,
        )
    return _pass()


def m6(root, relpath, text, eligible_lines, doc):
    """A report marker is present and its region enumerates >= 2 fields."""
    lines, indices = eligible_lines
    phrases = doc.match_phrases().get("M6", [])
    if not phrases:
        return _fail("report-section-missing", "no match phrase is compiled for M6")
    target = phrases[0].strip().lower()
    marker_index = None
    for i in indices:
        token = invariants.marker_token(lines[i])
        if token is not None and token.strip().lower() == target:
            marker_index = i
            break
    if marker_index is None:
        return _fail(
            "report-section-missing",
            "no marker line's token case-folds to %r" % target,
        )
    end = len(lines)
    for i in indices:
        if i <= marker_index:
            continue
        if invariants.marker_token(lines[i]) is not None:
            end = i
            break
    count = sum(
        1
        for i in indices
        if marker_index < i < end and mdmask.is_list_item(lines[i])
    )
    if count < 2:
        return _fail(
            "report-section-missing",
            "the report region enumerates fewer than two fields",
        )
    return _pass()


def m7(root, relpath, text, eligible_lines, doc):
    """The claim-label instruction — all four classes in one extent."""
    lines, indices = eligible_lines
    phrases = doc.match_phrases().get("M7", [])
    extent = _first_extent_containing_all(lines, indices, phrases)
    if extent is None:
        return _fail(
            "claim-labels-missing",
            "no extent names all four claim classes together",
        )
    return _pass()


def m8(root, relpath, text, eligible_lines, doc):
    """The resolved path matches exactly one of the three filename patterns."""
    if _M8_TIMESTAMPED.match(relpath) or _M8_DIRECTIVE_SUFFIXED.match(relpath):
        return _pass()
    return _fail(
        "filename-unmatched", "%s matches none of M8's three patterns" % relpath
    )


FUNCTIONS = {
    "M1": m1,
    "M2": m2,
    "M3": m3,
    "M4": m4,
    "M5": m5,
    "M6": m6,
    "M7": m7,
    "M8": m8,
}


def decide(root, relpath, text, doc):
    """`{element: Finding}` for all eight elements, over one shared mask."""
    eligible_lines = mdmask.eligible(text)
    return {
        name: func(root, relpath, text, eligible_lines, doc)
        for name, func in FUNCTIONS.items()
    }
