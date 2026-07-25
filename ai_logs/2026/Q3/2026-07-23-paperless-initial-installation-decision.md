# AI intervention trace — Paperless initial installation decision

Date: 2026-07-23
Status: validation-only trace
Boundary profile: validation_only_trace.

## Human direction

The repository owner explicitly requested that, after framing Paperless-ngx as the document source-management candidate, the integration be implemented and documented in the initial installation.

This trace records that direction as a deployment-composition decision, not as production approval.

## Change

The stacked work package:

- adds Paperless-ngx to the reference professional installation baseline as required document source-management presence;
- keeps the Paperless-to-Hermes/Cockpit binding default-off until reviewed/configured;
- adds `docs/install/PAPERLESS_INITIAL_INSTALLATION.md`;
- extends the Phase B deployment runbook with Paperless network, storage, token, exact-version capture, fail-closed write and rollback checks;
- records that the executable adapter is implemented in an external `pantheon-mvp` candidate branch, not inside Pantheon Next.

## Placement

```text
Paperless-ngx
  external document source-management runtime
  source bytes + versions + native metadata/search + internal tasks

Hermes
  external execution/orchestration
  analysis and classification candidates
  consequential Paperless writes only behind Pantheon policy

Cockpit / OpenWebUI
  exposure and user intent

Pantheon Next
  capability placement, status, gates, Source Capture identity, Knowledge/Evidence boundaries

Human
  installation, adoption, activation and consequential decisions
```

## Preserved distinctions

```text
included_in_initial_baseline != production_adopted
installed != approved
Paperless reachable != binding activated
Paperless metadata != canonical business classification
Paperless OCR != source truth
Paperless task success != professional validation
exact_source_capture != mutable_latest_pointer
```

## Runtime status

This repository still installs nothing.

At the time of this trace:

```text
Pantheon installation code       absent by doctrine
Paperless target installation    not established
Paperless target health          not established
Paperless target activation      not authorized
real-dossier use                 not authorized
external adapter implementation  candidate work in ifanjuang/pantheon-mvp
```

The baseline change determines what an operator should provision in the initial reference deployment. It does not claim that provisioning has occurred.
