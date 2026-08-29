# Red-gate stubs — NOT an implementation

These two files exist for one purpose: to prove that the directive-tooling test
suite goes red on **wrong behaviour** rather than on an absent module.

A suite that reds because `bin/directive` does not exist proves nothing about
the suite. So each binary has a stub here that runs, exits, and produces
deliberately wrong output:

- `directive` — emits a skeleton with **no source manifest** and **two**
  unfenced labelled disposition statements, ignores `--write` (writes nothing),
  and exits 0.
- `check-directive` — **always exits 0, silently**: no report, no checked set,
  no unchecked set, no per-element result.

The suite is run once with `DIRECTIVE_TOOLING_BIN` pointing here and once
without it, and both runs are recorded in `bin/tests/red-run-*.log`.

Neither file is a head start on the implementation: neither reads the
invariants document, resolves a git object, decides an element, or emits a
manifest. `bin/tests/helpers.py:dt_bin_dir` is the only thing that can reach
them, and only when `DIRECTIVE_TOOLING_BIN` is set.
