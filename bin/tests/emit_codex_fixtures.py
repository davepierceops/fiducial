"""Package 3b's fixture: all 34 enforce rows at 3f6fc8c, short prose.

Extends 3a's common fixture with the remaining procedure rows and the full
credential/production deny blocks. Blocks are literal snapshots, so a store
change requires a deliberate fixture update (checked by test_emit_codex).
"""
from tests.emit_fixtures import ALL_ROLES, BOTH, BOTH_CORPORA, emit_store_files
from tests.helpers import rs_row

EXTRA_SKILLS = {
    "R0502": ("release", "release-manager-agent"),
    "R0503": ("release", "release-manager-agent"),
    "R0505": ("gate", "release-manager-agent"),
    "R0552": ("gate", "chief-of-staff"),
    "R0553": ("gate", "chief-of-staff"),
    "R0558": ("gate", "chief-of-staff"),
    "R0560": ("gate", "chief-of-staff"),
    "R1032": ("release", "release-manager-agent"),
    "R1039": ("gate", "release-manager-agent"),
    "R1041": ("release", "release-manager-agent"),
    "R1042": ("release", "release-manager-agent"),
    "R1044": ("release", "release-manager-agent"),
    "R1045": ("release", "release-manager-agent"),
}
DENIES = {
    "R0164": ["Read(./.env)", "Read(./.env.*)", "Read(./**/.env)", "Read(./**/.env.*)",
              "Read(./**/secrets/**)", "Read(~/.aws/**)", "Read(~/.ssh/**)",
              "Bash(printenv*)", "Bash(cat *.env*)", "Bash(cat ~/.aws/*)", "Bash(cat ~/.ssh/*)"],
    "R0203": ["Bash(kubectl apply*)", "Bash(kubectl delete*)", "Bash(terraform apply*)",
              "Bash(terraform destroy*)", "Bash(tofu apply*)", "Bash(tofu destroy*)",
              "Bash(pulumi up*)", "Bash(pulumi destroy*)", "Bash(gcloud * deploy*)",
              "Bash(gcloud run deploy*)", "Bash(aws * deploy*)", "Bash(helm install*)",
              "Bash(helm upgrade*)", "Bash(ssh *prod*)"],
    "R0564": ["Bash(git push --force*)", "Bash(git push -f*)",
              "Bash(git push --force-with-lease*)", "Bash(git push * --force*)",
              "Bash(git push * -f*)", "Bash(git push * --force-with-lease*)",
              "Bash(git push origin +*)", "Bash(git push * +*)"],
}


def codex_store_files():
    files = emit_store_files()
    for row_id, (skill, role) in EXTRA_SKILLS.items():
        files["rules/%s.md" % row_id] = rs_row(
            row_id, "Procedure %s.\n\n```yaml\nskill: %s\n```" % (row_id, skill),
            order=100, topic=["change-control" if role == "chief-of-staff" else role],
            role=[role], session=BOTH, corpus=BOTH_CORPORA, verb="require", term=None,
            enforce="skill")
    for row_id, patterns in DENIES.items():
        files["rules/%s.md" % row_id] = rs_row(
            row_id, "Deny principle %s.\n\n```yaml\ndeny:\n%s```" % (
                row_id, "".join("  - %s\n" % pattern for pattern in patterns)),
            order=10, topic=["core" if row_id != "R0564" else "commit-control"],
            role=ALL_ROLES, session=BOTH, corpus=BOTH_CORPORA,
            verb="forbid", term=None, enforce="deny")
    return files
