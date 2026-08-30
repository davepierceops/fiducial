You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial, filling the Context Quality Reviewer role. One task: gate re-check, cycle 20, of policies/document-metadata-policy.md — a confirmation pass over cycle 19's fixes, returned as one review artifact.

SYNC FIRST: from the main tree, git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/main contains commit f74e0899d9694d43014ff0e185e6f400da5edfd3 (git merge-base --is-ancestor f74e0899d9694d43014ff0e185e6f400da5edfd3 origin/main exits 0); if not, stop and report. Record origin/main's SHA for your report.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dmp-cycle-20", created after the fetch above by: git worktree add --no-track "$TMPDIR/fiducial-dmp-cycle-20" -b document-metadata-policy-cycle-20 origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named document-metadata-policy-cycle-20, stop and report. Do not touch the main tree's checkout.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/document-metadata-policy-cycle-20-directive.md in the worktree, commit it alone with message "Directive: document-metadata-policy cycle 20 confirmation gate", push with git push origin document-metadata-policy-cycle-20, and report the SHA.

REVIEWED REVISION: policies/document-metadata-policy.md at content commit 9160a865fc7070775fc17e9b50c55bc5610318df, unchanged since cycle 19. Confirm with git log -1 --format=%H -- policies/document-metadata-policy.md that this is still the last commit touching the file; if not, stop and report.

READ FIRST, from the worktree: roles/context-quality-reviewer.md; docs/global-context/review-rubric.md; skills/review-artifact.md; reviews/document-metadata-policy-cycle-19.md (the prior cycle, whole); docs/cycles/document-metadata-policy-cycle-19-fix-directive.md (the decision record: DMP19-1 accepted, DMP19-2 accepted, DMP19-3 rejected as a finding on this document and recorded as a rubric-cycle candidate in OPEN-ITEMS.md). Then the document under review, whole.

CONFIRM EACH CYCLE-19 FINDING against origin/main, verified by running:
- DMP19-1: bin/tests/test_scope.py and bin/tests/test_check_frontmatter.py no longer anchor on prose-criteria.md (git grep -n "prose-criteria.md" -- bin/ returns no hit that is not a substring of public-prose-criteria.md); run bin/tests/run with tee to "$TMPDIR/fiducial-dmp-cycle-20/suite-cycle-20.txt" (not committed) and confirm exactly seven failures, all cycle-mode-unavailable landing-state failures in tests.test_directive and tests.test_directive_trd, none from test_scope, test_check_frontmatter or test_bundle_audience. Report the count and names.
- DMP19-2: bin/bundle GOVERNED_EXTRA_FILES names public-prose-criteria.md, voice.md, voice-template.md and not prose-criteria.md; bin/bundle --audience writer lists public-prose-criteria.md and voice.md. voice-template.md is expected absent — its audience is [human] by DEC-000240 and its bundle delivery is the bundle-system PRD's question (DEC-000260); its absence is not a finding.
- DMP19-3: OPEN-ITEMS.md's review-rubric candidate item carries the DMP19-3 sentence. Confirm presence; the rejection stands and is not re-raised here.
Run bin/check-frontmatter --all (must exit 0); report exit code and file count.

Re-apply the twelve criteria to the document's whole text only where a cycle-19 fix could have changed a criterion's answer; otherwise cycle 19's pass stands and you say so in Scope. Do not edit the document under review or any other governed file.

ARTIFACT: write reviews/document-metadata-policy-cycle-20.md in the review artifact schema's shape. Reviewed: policies/document-metadata-policy.md @ 9160a865fc7070775fc17e9b50c55bc5610318df. Reviewer: Context Quality Reviewer. Prior cycle: reviews/document-metadata-policy-cycle-19.md @ fd16aa7758407c86561318c59a713319c18c486a. Cross-checked names everything you ran or read for the confirmations above. Not inspected is stated explicitly. A confirmation pass that finds nothing is the header and nothing else, Verdict: ready. Any new finding follows the schema's entry shape and cites its criterion.

Commit reviews/document-metadata-policy-cycle-20.md alone with message "Review: document-metadata-policy cycle 20 (confirmation)". git push origin document-metadata-policy-cycle-20. Do not open a pull request. Never merge anything. Never flip a status.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dmp-cycle-20" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not rebase, do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; artifact commit SHA; the artifact's header block verbatim; suite failure count and names; check-frontmatter exit code and count; origin/main SHA verified; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
