"""The `bin/land` report: its structure, its provenance labels, its JSON form.

Contract: `specs/bin-land-trd.md` §5.2 (shape, serialization, and the value
domains), §5.3 (the key table, the token table, and the one emission rule), and
§7 (the exit mapping and the diagnostic-code table).

This module knows nothing about git and starts no subprocess (§3.7). `build`
is handed facts rather than reading them, and `to_json` is a pure function of
the `Report` — together the surface §3.1's split rests on: every report shape,
failure shapes included, is constructible from synthetic facts without ever
performing a landing.

**The tables below are transcriptions, not a second voice.** §5.3's key table
is normative over every other passage of the TRD, and `_TABLE` is that table
read as data; §5.3's token table is `STAGE_TOKENS`; §7's code table is
`_CODES`. Where this module and the TRD disagree, the TRD is right and this
module is wrong.
"""

from __future__ import annotations

import json

#: §5.2: the two of Core's four provenance classes PRD G6 permits the tool to
#: emit. This is a subset of Core's set, not a redefinition of it.
OBSERVED = "observed"
UNKNOWN = "unknown"

#: §5.2: the five contract keys plus `detail`, always present on every path.
CONTRACT_FIELDS = ("branch", "head", "prior_head", "verification")

#: §5.3's token table: ten tokens and no others. Step 8 carries two —
#: `nothing-staged` for an empty staged set, `commit` for a hook refusal — which
#: is why the token, and not the step number, is what a reader keys on.
STAGE_TOKENS = (
    "fetch",
    "resolve",
    "base-object",
    "guard",
    "base",
    "stage",
    "nothing-staged",
    "commit",
    "push",
    "verify",
)

#: The terminal path's failure mode. `SUCCESS` is not a mode; it is the one
#: end state §3.2's sequence reaches by finishing.
SUCCESS = "success"

#: §7's exit mapping. The integers are `aimeta/cli.py`'s `EXIT_OK`,
#: `EXIT_POLICY`, `EXIT_PRECONDITION` and `EXIT_SELF_VERIFY`, which is where
#: they are defined for the repository; they are written out here rather than
#: imported because §3.7 gives this module no dependency to import them
#: through — `cli` reaches `repo`, and `report.py` starts no subprocess and
#: imports no `repo.py`.
_EXIT_OK = 0
_EXIT = {
    SUCCESS: _EXIT_OK,
    "FM-1": 3,   # a precondition that stopped the sequence before any write
    "FM-2": 3,
    "FM-3": 3,
    "FM-4": 3,
    "FM-5": 3,
    "FM-6": 3,
    "FM-11": 3,
    "FM-7": 1,   # a write the tool attempted and git rejected
    "FM-8": 4,   # the tool's own verification of its own write failed
}

#: §5.3's key table, as data. Per terminal mode: the contract fields
#: established there, the `detail` keys established there unconditionally, and
#: the `detail` keys whose rows carry a condition — each of those established
#: only where `facts` carries it, the condition being a state the establishing
#: step observed and recorded (§3.7).
#:
#: The "Established on" column is a **ceiling as well as a floor**. A fact the
#: accumulated `facts` happen to carry on a path no row names is not emitted
#: there, whatever `facts` holds: a contract field is present with
#: `value: null` and `class: "unknown"`, and a `detail` key is absent.
_TABLE = {
    SUCCESS: (
        ("branch", "head", "prior_head", "verification"),
        ("base", "local_head", "remote_head"),
        ("prior_branch",),
    ),
    "FM-1": (("branch",), ("stage", "git_status"), ()),
    "FM-2": (("branch", "prior_head"), ("stage", "base", "git_status"), ()),
    "FM-3": (
        ("branch", "prior_head"),
        ("stage", "base", "local_head", "git_status"),
        ("branch_head",),
    ),
    "FM-4": (
        ("branch", "prior_head"),
        ("stage", "base", "local_head", "git_status"),
        (),
    ),
    "FM-5": (
        ("branch", "prior_head"),
        ("stage", "base", "local_head", "git_status"),
        ("prior_branch",),
    ),
    "FM-6": (
        ("branch", "prior_head"),
        ("stage", "base", "local_head", "git_status"),
        ("prior_branch",),
    ),
    "FM-7": (
        ("branch", "prior_head", "head", "verification"),
        ("stage", "base", "local_head", "git_status"),
        ("prior_branch",),
    ),
    "FM-8": (
        ("branch", "prior_head", "head", "verification"),
        ("stage", "base", "local_head", "remote_head"),
        ("prior_branch",),
    ),
    "FM-11": (("branch", "prior_head"), ("stage",), ()),
}

#: §5.3's `files` row. Observed entries on the success path; one `match: null`
#: entry per committed path on FM-7 and FM-8, where a commit exists and step 10
#: produced no comparison; no entries on every other path.
_FILES_UNKNOWN = ("FM-7", "FM-8")

#: The modes each token names. `resolve` is the one token two modes reach, and
#: `stop.git_status` separates them: FM-1's stop is a failed subprocess and
#: carries that invocation's exit status, FM-11's is a read that exited 0 and
#: carries none (§3.7).
_MODE_BY_TOKEN = {
    "fetch": "FM-1",
    "base-object": "FM-2",
    "guard": "FM-3",
    "base": "FM-4",
    "stage": "FM-5",
    "nothing-staged": "FM-5",
    "commit": "FM-6",
    "push": "FM-7",
    "verify": "FM-8",
}

#: §7's diagnostic-code table, keyed by the refusal it names. Twelve codes and
#: no others. FM-3's two rows are separated by `detail.branch_head`, which is
#: the fact §5.3 puts on the second check's path and on no other, so the key
#: carries that condition rather than a token that cannot express it.
_CODES = {
    ("FM-1", "fetch"): "fetch-failed",
    ("FM-1", "resolve"): "remote-read-failed",
    ("FM-11", "resolve"): "no-base-at-remote",
    ("FM-2", "base-object"): "base-object-missing",
    ("FM-3", "guard", False): "head-diverged",
    ("FM-3", "guard", True): "branch-diverged",
    ("FM-4", "base"): "base-checkout-failed",
    ("FM-5", "stage"): "path-not-found",
    ("FM-5", "nothing-staged"): "nothing-staged",
    ("FM-6", "commit"): "commit-refused",
    ("FM-7", "push"): "push-rejected",
    ("FM-8", "verify"): "remote-head-mismatch",
}

#: The human-readable half of each diagnostic. §7 fixes the code; the wording
#: is this module's, and the suite asserts on codes and never on English
#: (`bin/tests/helpers.py`).
_MESSAGES = {
    "fetch-failed": "git fetch origin did not complete",
    "remote-read-failed": "could not read the branch heads at origin",
    "no-base-at-remote": (
        "origin carries neither the named branch nor main, so there is no "
        "base to land on"
    ),
    "base-object-missing": (
        "the base commit origin names is not in the local object database; "
        "refusing to fetch again"
    ),
    "head-diverged": "local HEAD carries a commit the landing base does not",
    "branch-diverged": (
        "the local branch carries a commit the landing base does not, and it "
        "is the ref this landing would rewrite"
    ),
    "base-checkout-failed": "could not put the branch at the base",
    "path-not-found": "a named path does not exist",
    "nothing-staged": "the staged set is empty; there is nothing to commit",
    "commit-refused": "a repository hook refused the commit",
    "push-rejected": "the push was rejected; the commit is left in place locally",
    "remote-head-mismatch": (
        "the head at origin is not the commit that was pushed; the landing is "
        "unverified"
    ),
}


def _leaf(value, established):
    """§5.2: a leaf carries exactly `value` and `class`, and nothing else.

    `value` is `null` wherever `class` is `"unknown"`. An unestablished fact is
    never rendered as an empty string or a plausible placeholder.
    """
    if not established:
        return {"class": UNKNOWN, "value": None}
    return {"class": OBSERVED, "value": value}


def mode_of(stop):
    """The terminal path's mode, from the stop alone (§3.7).

    `stop is None` is the success path; the sequence has no other way to
    finish. Otherwise the token names the mode outright on every token but
    `resolve`, which FM-1 and FM-11 both reach.
    """
    if stop is None:
        return SUCCESS
    if stop.stage == "resolve":
        return "FM-1" if stop.git_status is not None else "FM-11"
    return _MODE_BY_TOKEN[stop.stage]


def verification_of(facts):
    """§5.2's biconditional, read off the facts and from nothing else.

    `"complete"` if and only if `ls-remote` confirmed the head SHA and every
    per-file comparison matched. §7's exit mapping reads the same biconditional
    through `exit_code`, which is what stops the report and the exit status
    from drifting apart (AC-LAND-T02).
    """
    head = facts.get("head")
    if head is None:
        return None
    if facts.get("remote_head") != head:
        return "incomplete"
    matches = facts.get("matches")
    if matches is None or not all(matches.values()):
        return "incomplete"
    return "complete"


class Report:
    """The five contract fields, the `detail` object, and their serialization."""

    def __init__(self, branch, mode, facts, stop):
        self.branch = branch
        self.mode = mode
        self.facts = facts
        self.stop = stop

    # -- construction ------------------------------------------------------

    @classmethod
    def build(cls, branch, facts, stop):
        """Assemble the report from the accumulated `facts` and nothing else.

        What `facts` holds is not what decides emission: §5.3's "Established
        on" column decides it, for the terminal path the sequence reached.
        Accumulation and emission are two questions, and only the second is
        this method's.
        """
        return cls(branch, mode_of(stop), dict(facts), stop)

    # -- the derived facts -------------------------------------------------

    @property
    def stage(self):
        """§5.3's token for the stop this report is about, or None on success."""
        return None if self.stop is None else self.stop.stage

    def verification(self):
        return verification_of(self.facts)

    def diagnostic_code(self):
        """§7's code for this refusal, or None on the two success paths.

        A successful landing emits no diagnostic and therefore no code: §7's
        table is the seventeen refusal paths', and gives a landing that worked
        no row, there being no situation to answer.
        """
        if self.stop is None:
            return None
        if self.mode == "FM-3":
            return _CODES[("FM-3", "guard", "branch_head" in self.facts)]
        return _CODES[(self.mode, self.stop.stage)]

    def diagnostic_message(self):
        """The English half of the diagnostic. Never a bracketed token."""
        code = self.diagnostic_code()
        if code is None:
            return None
        message = _MESSAGES[code]
        note = getattr(self.stop, "note", None)
        return "%s: %s" % (message, note) if note else message

    def exit_code(self):
        """§7's exit mapping, read through §5.2's biconditional.

        0 if and only if the verification is complete (AC-LAND-08); otherwise
        the code §7 assigns this mode. Both directions come from one place, so
        an exit status can never claim a landing the report does not.
        """
        if self.verification() == "complete":
            return _EXIT_OK
        code = _EXIT[self.mode]
        # A mode §7 maps to 0 that did not verify would be exactly the
        # inversion PRD §7 puts under "Not accepted". It cannot arise from the
        # table above; the guard is here so that it never could.
        return code if code != _EXIT_OK else _EXIT["FM-8"]

    # -- emission, under §5.3's one rule -----------------------------------

    def _established(self):
        """The exact sets §5.3's table establishes on this terminal path."""
        contract, unconditional, conditional = _TABLE[self.mode]
        detail = list(unconditional)
        detail += [key for key in conditional if key in self.facts]
        return set(contract), detail

    def _detail_value(self, key):
        if key == "stage":
            return self.stage
        if key == "git_status":
            return self.stop.git_status
        return self.facts[key]

    def _files(self):
        """§5.3's `files` row: three shapes and no fourth."""
        paths = sorted(self.facts.get("files", ()))
        if self.mode in _FILES_UNKNOWN:
            return [
                {"class": UNKNOWN, "match": None, "path": path} for path in paths
            ]
        if self.mode != SUCCESS:
            # No commit was made, so there are no per-file entries. The empty
            # list is the absence of entries, not a claim that the commit
            # carried no files — `detail.stage` is what says which it is.
            return []
        matches = self.facts.get("matches", {})
        return [
            {"class": OBSERVED, "match": matches[path], "path": path}
            for path in paths
        ]

    def to_dict(self):
        """The report as a plain object, under §5.2's shape and §5.3's rule."""
        established, detail_keys = self._established()
        values = {
            "branch": self.branch,
            "head": self.facts.get("head"),
            "prior_head": self.facts.get("prior_head"),
            "verification": self.verification(),
        }
        report = {
            name: _leaf(values[name], name in established)
            for name in CONTRACT_FIELDS
        }
        report["files"] = self._files()
        report["detail"] = {
            key: _leaf(self._detail_value(key), True) for key in detail_keys
        }
        return report

    def to_json(self):
        """§5.2's format: two-space indent, sorted keys, ASCII, one newline.

        `ensure_ascii=True` is the decision that retired OQ-11: a script's
        stdout must not depend on the ambient locale being UTF-8, and the
        escaped and raw forms parse to the identical string, so nothing is
        given up for it.
        """
        return json.dumps(
            self.to_dict(), indent=2, sort_keys=True, ensure_ascii=True
        ) + "\n"
