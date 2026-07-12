# AI intervention trace — catalog validation, loader and candidate

Date: 2026-07-11
Status: validation-only trace

## Change

Added:

- JSON Schemas for Capability, Resource, Preset and InstallationCandidate;
- a read-only cross-manifest validator;
- a dedicated read-only GitHub Actions workflow;
- a static catalog projection for the Pantheon Control prototype;
- a manifest-driven Swiper page;
- local browser generation and download of an Installation Candidate JSON artifact.

## Boundary

No live registry, database, installer, provisioner, Docker or Portainer access, connector, OAuth flow, secret store, shell execution, scheduler, queue, approval engine, runtime activation or external action is implemented.

The generated Installation Candidate explicitly records:

```text
installation_authorized: false
execution_started: false
activation_authorized: false
human_approval_required: true
```

The browser download is an artefact candidate only. It is not sent to a provisioner.

## Validator invariants

The validator checks schema conformance, unique IDs, references, role coverage, admitted provisioner vocabulary, raw secret patterns, `:latest` image tags, self-approval and automatic activation.

## Preserved distinctions

```text
schema_valid != approved
manifest_valid != installed
projection_loaded != live_registry
candidate_prepared != installation_authorized
installation_authorized != execution_started
healthy != safe
trace != evidence
```
