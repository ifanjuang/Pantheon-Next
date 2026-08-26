# Platform Phase B — Historical Deployment Handoff

Status: refused — superseded operator handoff retained temporarily for compatibility — refused.
Boundary profile: candidate_support_note.

This former Phase B runbook is no longer a deployment authority. The current operator path is `COMMON_BASELINE_RUNBOOK.md`, aligned with `COMMON_INSTALLATION_BASELINE.md`.

The historical handoff bundled responsibilities that the current architecture now separates:

```text
runtime interaction -> Hermes Web/dashboard or reviewed compatible Hermes client
governed projections -> Pantheon Cockpit
execution -> Hermes Agent
professional source intake -> bounded local/NAS source path + existing source owners
workspace -> Obsidian
```

OpenWebUI and Paperless are not target architecture dependencies.

## Historical implementation provenance

Protected implementation artifacts still exist and are audited separately:

```text
implementation/compose.phase-b.yaml
implementation/compose.paperless.yaml
implementation/mvp_vertical/
implementation/hermes/skills/pantheon-document-intake/
```

Their presence is historical implementation provenance only. In particular, `implementation/compose.paperless.yaml` does not make Paperless selected, preferred, installed or authorized.

```text
repository presence != architecture dependency
compose file present != deployment selected
implementation merged != production adopted
```

The former `pantheon-mvp` repository/PR lineage remains Git provenance. Current Pantheon implementation placement is under `implementation/`.

## Current owner

Use:

```text
docs/install/COMMON_BASELINE_RUNBOOK.md
```

for current bootstrap, Hermes configuration, bounded Pantheon policy connection, source-path setup, acceptance and rollback guidance.

Product-specific Paperless/OpenWebUI deployment instructions from this former handoff must not be followed for the selected architecture.

## Convergence path

This file remains only because protected tests still exercise historical monorepo placement assumptions. When the related OpenWebUI/Paperless implementation/tests are removed or generalized, delete this pointer and retain provenance in Git history.

```text
runtime success != Evidence
projection != persistence
historical compatibility != current authority
```
