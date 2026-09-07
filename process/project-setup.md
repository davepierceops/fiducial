---
order: 100
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Project Setup

An adoption precondition is something that must be true about a repository
before the methodology governs work in it. These live in the forge's
configuration and the agent runner's, outside git, where no hook can enforce
them: the human confirms them once per repository, before either session kind
begins work in it. Confirm they hold and say so; report one that does not rather
than working around it.

1. **Branch protection on the default branch**, in the forge's configuration: no
   force-push; no branch deletion; changes land only through a pull request; no
   bypass, including for administrators. The last carries the others, and it is
   what makes "agents may push and merge" safe to say.
2. **A force-push deny in the agent runner** [R0564], holding in every permission
   mode, including the modes that otherwise skip prompting.
