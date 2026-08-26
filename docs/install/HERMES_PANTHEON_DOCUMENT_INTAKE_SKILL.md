# Hermes `pantheon-document-intake` — Historical Installation Pointer

Status: refused — former Paperless-specific Hermes skill installation path — refused.
Boundary profile: candidate_support_note.

The `pantheon-document-intake` skill is not part of the selected target architecture because its binding is Paperless-specific. This file is retained temporarily only while protected implementation/tests still reference the historical skill package.

Current candidate source still exists at:

```text
implementation/hermes/skills/pantheon-document-intake/
```

Repository presence does not mean the skill is selected, installed, enabled, approved or task-authorized.

## Historical source contract

The old installation flow pinned one Pantheon Next revision before copying the complete skill directory. The historical operator variable was:

```text
PANTHEON_NEXT_SKILL_COMMIT=<FULL_COMMIT_SHA>
```

Historical source URLs used the current repository host shape, for example:

```text
https://raw.githubusercontent.com/ifanjuang/Pantheon-Next/<PANTHEON_NEXT_SKILL_COMMIT>/implementation/hermes/skills/pantheon-document-intake/SKILL.md
```

This reference is provenance only. It is not a current installation instruction.

## Current owner

The selected baseline uses:

```text
bounded local/NAS source ingestion
existing document/source governance
separately selected extraction capabilities
Hermes runtime capabilities that are not tied to a refused DMS dependency
```

Any reusable generic capability found inside the historical skill must be extracted into an existing owner during the protected cleanup slice rather than preserving the Paperless-specific package by default.

```text
skill package present != capability needed
skill installed != capability approved
runtime success != Evidence
```

## Convergence path

Audit the package, gateway and tests together. If no distinct target consumer remains, delete the skill and this pointer in the same protected cleanup sequence; Git history remains provenance.
