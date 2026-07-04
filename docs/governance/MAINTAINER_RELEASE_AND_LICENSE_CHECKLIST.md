# Maintainer release and licence checklist

Status: validation-only / maintainer checklist.

Related issues:

```text
#261 — post-consolidation git tags
#262 — PDF licence qualification and optional history purge
#264 — out-of-repo handoff
```

This document records maintainer actions that are outside the assistant connector and outside Pantheon runtime scope.

It does not implement a runtime, release system, legal decision, history rewrite, approval engine, memory engine, scheduler, queue, provider router or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## 1. Version tag checklist

The repository version marker should remain coherent:

```text
VERSION
CHANGELOG.md head
pyproject.toml project.version
mcp-server/pyproject.toml project.version
git tag
```

The current maintainer issue records at least one missing tag:

```text
v0.1.59 -> e45f37276f0ee2153909efd660ac4d4fa1720001
```

The handoff issue also mentions:

```text
v0.1.60 -> the #218 merge / VERSION 0.1.60 line
```

Before creating a tag, verify the target commit manually:

```bash
git fetch origin --tags
git checkout main
git pull --ff-only

git show --stat e45f37276f0ee2153909efd660ac4d4fa1720001
git show --stat <commit-for-v0.1.60>
```

Create tags only after confirming the version files agree at the target commit:

```bash
git tag -a v0.1.59 e45f37276f0ee2153909efd660ac4d4fa1720001 -m "v0.1.59"
git push origin v0.1.59

# Only after resolving the exact target commit:
git tag -a v0.1.60 <commit-for-v0.1.60> -m "v0.1.60"
git push origin v0.1.60
```

Do not use the latest `main` commit as a version tag target unless the version files intentionally describe that exact commit.

## 2. PDF licence qualification checklist

Current stance:

```text
base_metier/architecte/ = external professional corpus / to verify
not authority
not proof
not vertical-slice grounding material
source PDFs out of current git tree
manifest retained for provenance/integrity only
```

Decision required for each source family:

```text
source name:
source owner:
original URL or acquisition path:
licence / terms found:
redistribution allowed: yes / no / unclear
private internal use allowed: yes / no / unclear
derivative text extraction allowed: yes / no / unclear
can remain referenced in manifest: yes / no / unclear
can ground examples or vertical slices: yes / no
maintainer decision:
decision date:
```

Default until cleared:

```text
MAF professional material: treat as not redistributable without written authorization.
Ordre des Architectes publications: verify terms before redistribution.
Official legal texts: lower risk, but reproduction conditions still need verification.
Unknown-origin PDFs: do not redistribute and do not ground examples.
```

## 3. Optional history purge decision

A current-tree deletion is not a history purge.

Run a history rewrite only after maintainer/legal decision and team coordination.

Decision options:

```text
A. No purge: accept history risk and keep repo as-is.
B. Purge PDFs only: remove base_metier/**/*.pdf from all history.
C. New clean repository: archive old repo and continue in a clean successor.
```

If purge is required:

```bash
# Fresh mirror clone.
git clone --mirror git@github.com:ifanjuang/Pantheon-Next.git Pantheon-Next.git
cd Pantheon-Next.git

git filter-repo \
  --path-glob 'base_metier/**/*.pdf' \
  --invert-paths

git push --force --mirror
```

Operational warnings:

```text
Do not run during active PR work.
Notify collaborators before and after rewrite.
Existing clones should be recloned or carefully reset.
Old PR references and tags may require attention.
CI caches may need clearing.
GitHub Pages may need rebuild verification.
```

## 4. Closure criteria

Issue #261 can close when:

```text
required tags exist on origin
version files and tag targets are verified
```

Issue #262 can close when:

```text
licence decision is recorded
history purge decision is recorded
any chosen purge is completed or explicitly refused
base_metier remains excluded from vertical-slice grounding until cleared
```

Issue #264 can close when:

```text
#261 is closed
#262 is closed
#273 has either completed the first external run or recorded why it is deferred
```

The validated remains.
