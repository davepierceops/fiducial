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

from . import cli, closure, invariants, mdmask, repo

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

#: Cycle mode's bundle directory default, unchanged from `bin/cycle-open`
#: (AC-CO-7).
BUNDLE_DIR_DEFAULT = ".cycle-bundles"

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

#: §3.3's cycle-mode table, in emission order. Sixteen regions: two author,
#: fourteen committed. Row 1's two marker forms (one per selector) are one
#: region either way: the marker is whatever text `directive_identity` puts on
#: the emitted heading line, taken from the rendered text like every other
#: region rather than named here.
CYCLE_REGIONS = (
    Region(invariants.HEADING_CYCLE, ("heading", "date", "scope_list")),
    Region(invariants.ROUTE_AND_MODEL, ("route", "model")),
    Region(invariants.FIRST_ACT, ("directive_path",)),
    Region(invariants.DISPOSITION_PROMPT),
    Region(None, (), author=True),
    Region(invariants.DECISIONS),
    Region(invariants.DEFERRED),
    Region(invariants.EXECUTION_NOTES, (), author=True),
    Region(invariants.BASE_VERIFICATION, ("reviewed_ref",)),
    Region(invariants.COMPANIONS, ("companion_list",)),
    Region(invariants.SANDBOX),
    Region(invariants.VERIFICATION),
    Region(invariants.STOP_CONDITIONS, ("reviewed_ref",)),
    Region(invariants.REPORT_FORMAT),
    Region(invariants.CLAIM_LABELS),
    Region(invariants.SOURCE_MANIFEST, ("manifest",)),
)


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


def cycle_values(*, heading, date, scope_list, route, model, directive_path):
    """The closed placeholder set cycle mode binds, before the manifest.

    `{{reviewed_ref}}` and `{{companion_list}}` carry the same author slots
    general mode emits (§3.9): cycle mode's own reviewed ref and companions are
    a session-level concern the flags here do not supply.
    """
    return {
        "heading": heading,
        "date": date,
        "scope_list": scope_list,
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
    the region that carries it. The manifest is always the last region in
    emission order (§3.3, both tables), in either mode.
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
    manifest_index = len(regions) - 1
    texts[manifest_index] = _render_region(
        doc, regions[manifest_index], filled
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


# ---------------------------------------------------------------------------
# Cycle mode, migrated from `bin/cycle-open` (TRD §3.9 step 3), behaviour
# unchanged: the identity, document-set, revision-resolution and
# reviewed-revision-bundle code that is cycle-mode-only. `bin/cycle-open`
# keeps its own copies until step 4 replaces its body with a forwarder.


def directive_identity(root, args):
    """(relpath, heading) for the directive, per AC-CO-1 and D4."""
    if args.cycle:
        title = args.title or root.name
        return (
            "docs/cycles/cycle-%s-directive.md" % args.cycle,
            "# Cycle %s Directive — %s" % (args.cycle, title),
        )
    title = args.title or args.name.replace("-", " ")
    return "docs/cycles/%s-directive.md" % args.name, "# %s Directive" % title


def collect_documents(root, args):
    """Closure expansion of `--bundle` entries, unioned with explicit paths."""
    documents = []
    if args.bundle:
        entries = [closure.resolve_entry(root, entry) for entry in args.bundle]
        for item in closure.walk(root, entries):
            documents.append(item["path"])
    for path in args.paths:
        documents.append(cli.relpath_of(root, path))
    ordered = []
    for relpath in documents:
        if relpath not in ordered:
            ordered.append(relpath)
    return ordered


def resolve_revisions(root, documents, allow_dirty):
    """`[(relpath, sha)]`, refusing untracked, missing, or dirty documents."""
    revisions = []
    for relpath in documents:
        if not (root / relpath).is_file():
            raise cli.ToolError("%s does not exist" % relpath, cli.EXIT_POLICY)
        sha = repo.last_commit_sha(root, relpath)
        if sha is None:
            raise cli.ToolError(
                "%s is untracked, so it has no reviewed revision" % relpath,
                cli.EXIT_POLICY,
            )
        if repo.git("status", "--porcelain", "--", relpath, cwd=root):
            if not allow_dirty:
                raise cli.ToolError(
                    "%s has uncommitted modifications; its recorded SHA would not "
                    "describe the uploaded content" % relpath,
                    cli.EXIT_PRECONDITION,
                )
            cli.diagnostic(
                "WARN",
                relpath,
                "dirty-document",
                "uncommitted modifications; the bundle carries the committed revision",
            )
        revisions.append((relpath, sha))
    return revisions


def write_bundle(root, outdir, revisions, directive_relpath):
    """AC-CO-7: the reviewed-revision bundle, plus its `BUNDLE.txt` manifest."""
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for relpath, sha in revisions:
        content = repo.file_at_rev(root, sha, relpath)
        if content is None:
            raise cli.ToolError(
                "cannot read %s at %s" % (relpath, sha), cli.EXIT_PRECONDITION
            )
        (outdir / relpath.replace("/", "__")).write_text(content, encoding=cli.ENCODING)
        manifest.append("%s @ %s" % (relpath, sha))
    manifest.append(directive_relpath)
    (outdir / "BUNDLE.txt").write_text(
        "\n".join(manifest) + "\n", encoding=cli.ENCODING
    )


def warn_if_bundle_not_ignored(root, out_rel):
    """AC-CO-8: a bundle directory git does not ignore gets a WARN, still writes."""
    code, _, _ = repo.run(["check-ignore", "-q", "--", out_rel + "/"], cwd=root)
    if code != 0:
        cli.diagnostic(
            "WARN",
            out_rel,
            "bundle-not-ignored",
            "the bundle directory is not gitignored; uploads risk becoming tracked files",
        )
