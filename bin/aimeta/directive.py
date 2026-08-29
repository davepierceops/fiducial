"""Assembling a directive skeleton from committed regions.

TRD §3.3 (the region set, emission order, the markers and the manifest), §3.9
(the general-mode destination), §6 (FM-G4, FM-G5, FM-G7).

This module holds **no region text of its own**. Every region is addressed by
its section name, and every marker is taken from the first line of that
section's committed body, which is what makes AC-DT-02 satisfiable by
construction rather than by inspection: the criterion forbids a generator's
source from reproducing a line of a manifest entry's committed content, and a
marker line is such a line.
"""

from __future__ import annotations

from . import cli, invariants, mdmask

#: How a manifest entry separates a marker from its provenance.
_ENTRY_JOIN = " — "

#: What a manifest entry says where there is no committed content below the
#: marker. Two entries per mode carry it (AC-DT-18).
_AUTHOR_SOURCE = "author region"

#: Entries are indented, as §3.3 renders them. An entry opens with its
#: marker's own token, so an entry at column 0 would *be* a marker line under
#: §3.3's grammar — a second one for every region — and neither AC-DT-05's
#: uniqueness clause nor its partition could hold for any skeleton. A marker is
#: a line at column 0; indenting takes the entries out of the grammar without
#: touching the entry form the manifest states.
_ENTRY_INDENT = "    "

#: Regions are joined by one blank line, so an author region's marker is
#: followed by the blank content slot AC-DT-03 asserts on.
_REGION_JOIN = "\n\n"

#: The destination general mode computes: UTC, `Z`-suffixed (§3.9). The author
#: does not name it, so the generator cannot be driven to emit a skeleton its
#: own lint fails M8 on.
_DESTINATION = "docs/cycles/%s-%sZ.md"

#: Author slots the generator leaves for values no flag supplies.
_SLOT_ROUTE = "<route>"
_SLOT_MODEL = "<model>"
_SLOT_REVIEWED_REF = "<full sha of the reviewed ref>"
_SLOT_COMPANIONS = "- <path> @ <full sha>"


class Region:
    """One emitted region: where its text comes from, and how it is classified.

    `section` is None for the disposition author region, whose marker is the
    label rather than a section body's first line — the single-source property
    of §3.1, not a literal of this module's.
    """

    __slots__ = ("section", "placeholders", "author")

    def __init__(self, section, placeholders=(), author=False):
        self.section = section
        self.placeholders = tuple(placeholders)
        self.author = author


#: §3.3's general-mode table, in emission order. Fourteen regions: two author,
#: twelve committed.
GENERAL_REGIONS = (
    Region(invariants.HEADING_GENERAL, ("title",)),
    Region(invariants.ROUTE_AND_MODEL, ("route", "model")),
    Region(invariants.FIRST_ACT, ("directive_path",)),
    Region(invariants.DISPOSITION_PROMPT),
    Region(None, (), author=True),
    Region(invariants.BASE_VERIFICATION, ("reviewed_ref",)),
    Region(invariants.COMPANIONS, ("companion_list",)),
    Region(invariants.TASK, (), author=True),
    Region(invariants.SANDBOX),
    Region(invariants.VERIFICATION),
    Region(invariants.STOP_CONDITIONS, ("reviewed_ref",)),
    Region(invariants.REPORT_FORMAT),
    Region(invariants.CLAIM_LABELS),
    Region(invariants.SOURCE_MANIFEST, ("manifest",)),
)

#: The region whose body the manifest is substituted into, by position in the
#: order above. It is emitted last, so its own entry names a committed path and
#: AC-DT-18's "every other entry names a committed path" holds without
#: exception.
_MANIFEST_REGION = len(GENERAL_REGIONS) - 1


def destination(descriptor, timestamp):
    """General mode's one destination, computed rather than named (§3.9)."""
    return _DESTINATION % (descriptor, timestamp)


def general_values(*, title, route, model, directive_path):
    """The closed placeholder set general mode binds, before the manifest."""
    return {
        "title": title,
        "route": route or _SLOT_ROUTE,
        "model": model or _SLOT_MODEL,
        "directive_path": directive_path,
        "reviewed_ref": _SLOT_REVIEWED_REF,
        "companion_list": _SLOT_COMPANIONS,
        "manifest": "",
    }


def _render_region(doc, region, values):
    if region.section is None:
        return doc.label_line()
    admitted = {name: values[name] for name in region.placeholders}
    body = invariants.substitute(doc.section(region.section), admitted, region.section)
    return body.rstrip("\n")


def _marker_of(text, region, doc):
    first = text.split("\n", 1)[0]
    token = invariants.marker_token(first)
    if token is None:
        raise cli.ToolError(
            "[skeleton-self-check-failed] observed: the region sourced from `%s` "
            "opens with a line that is not a marker: %r"
            % (region.section or invariants.DISPOSITION_LABEL, first),
            cli.EXIT_PRECONDITION,
        )
    return token


def _entry(marker, region, doc):
    if region.author:
        return "%s%s%s" % (marker, _ENTRY_JOIN, _AUTHOR_SOURCE)
    return "%s%s%s @ %s" % (marker, _ENTRY_JOIN, doc.relpath, doc.sha)


def assemble(doc, regions, values):
    """The skeleton, with its manifest, as one string.

    Two passes: the markers are taken from each region's first line, which no
    placeholder reaches, so the manifest can be built and then substituted into
    the region that carries it.
    """
    texts = [_render_region(doc, region, values) for region in regions]
    markers = [
        _marker_of(text, region, doc) for text, region in zip(texts, regions)
    ]
    entries = [
        _entry(marker, region, doc) for marker, region in zip(markers, regions)
    ]
    filled = dict(values)
    filled["manifest"] = "\n".join(_ENTRY_INDENT + entry for entry in entries)
    texts[_MANIFEST_REGION] = _render_region(
        doc, regions[_MANIFEST_REGION], filled
    )
    text = _REGION_JOIN.join(texts) + "\n"
    self_check(doc, text, markers)
    return text


def self_check(doc, text, markers):
    """FM-G7, over the mask §3.5 fixes.

    §3.2's three conditions make a failure unreachable in principle; the check
    exists because G3 is the invariant the whole design rests on, and a silent
    violation of it would hand an author a skeleton whose executor stops.
    Fenced lines are not markers here for the same reason they are not eligible
    for the lint's match: the prompt region carries both admitted forms worked
    inside a fence, and that is the Q10 decision rather than a collision.
    """
    lines, indices = mdmask.eligible(text)
    counts = {}
    statements = 0
    for index in indices:
        content = mdmask.leading_content(lines[index])
        if doc.matches_label(content):
            statements += 1
        token = invariants.marker_token(lines[index])
        if token is not None:
            counts[token] = counts.get(token, 0) + 1
    for marker in markers:
        if counts.get(marker, 0) != 1:
            raise cli.ToolError(
                "[skeleton-self-check-failed] observed: the marker %r opens %d "
                "unfenced regions of the emitted skeleton, not one"
                % (marker, counts.get(marker, 0)),
                cli.EXIT_PRECONDITION,
            )
    if statements != 1:
        raise cli.ToolError(
            "[skeleton-self-check-failed] observed: the emitted skeleton carries %d "
            "unfenced labelled disposition statements, not one" % statements,
            cli.EXIT_PRECONDITION,
        )


def refuse_existing(root, relpath):
    """FM-G5, before any write: the computed destination is never clobbered."""
    if (root / relpath).exists():
        raise cli.ToolError(
            "[directive-exists] observed: %s already exists; refusing to overwrite "
            "it" % relpath,
            cli.EXIT_PRECONDITION,
        )


def land(root, relpath, text):
    """Write the skeleton to the computed destination and nothing else."""
    path = root / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding=cli.ENCODING)
    return relpath
