---
order: 100
topic: [project-setup]
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Project Setup

An adoption precondition is something that must be true about a repository
before the methodology governs work in it. These live in the forge's
configuration and the agent runner's, outside git, where no hook can enforce
them: the human confirms them once per repository, before the decision session
begins work in it. The Chief of Staff confirms they hold, once per session, and
says so; report one that does not rather than working around it.

1. **Branch protection on the default branch**, in the forge's configuration: no
   force-push; no branch deletion; changes land only through a pull request; no
   bypass, including for administrators. The last carries the others, and it is
   what makes "agents may push and merge" safe to say. Where the forge cannot
   enforce it — a private repository under GitHub Free refuses branch
   protection — the fallback is the second precondition alone plus every
   landing by pull request, never a push to the default branch, recorded in the
   project's decision log as an accepted-risk entry naming the plan that would
   restore the forge layer; the entry is re-examined when the repository moves
   to one [R0564].
2. **A force-push deny in the agent runner** [R0564], holding in every permission
   mode, including the modes that otherwise skip prompting.
