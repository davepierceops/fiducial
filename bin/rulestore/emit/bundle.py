"""The `bundle` target: today's bundle document, for the writing roles and
Claude chat (SPEC.md §7). One file, `fiducial-bundle-<name>-<generated>.md`,
rendered exactly as `bin/bundle --where` renders it — the two share
`rulestore.render`, and a test holds them byte-identical.
"""

from __future__ import annotations

from rulestore import query, render, terms

from . import EmitError, Emission, Target


def bundle_filename(where, name, generated):
    bundle_name = name or "-".join("%s-%s" % (k, v) for k, v in where.items())
    return "fiducial-bundle-%s-%s.md" % (bundle_name, generated)


class BundleTarget(Target):
    name = "bundle"
    takes_query = "required"

    def emit(self, inputs):
        selected = query.select(inputs.rows, inputs.where, inputs.sequences)
        if not selected:
            raise EmitError("refused: the query selected no rows")
        definitions = terms.pull_definitions(selected, inputs.rows)
        text = render.render(
            selected, definitions,
            repo=inputs.repo, head=inputs.head, generated=inputs.generated,
        )
        path = bundle_filename(inputs.where, inputs.name, inputs.generated)
        return Emission(files={path: text})
