# AI intervention trace — provisioner handoff contracts

Date: 2026-07-12
Status: validation-only trace

## Change

Added non-executable contracts for the transition from an `InstallationCandidate` to an external provisioner and back:

```text
InstallationCandidate
-> ProvisionerHandoffCandidate
-> ExecutionResultCandidate
-> HealthObservation
```

Added:

- three JSON Schemas;
- one Docling fixture chain;
- one read-only validator;
- one dedicated CI workflow;
- one static review surface.

## Boundary

No Portainer API, Docker socket, Compose execution, SSH, shell runner, OAuth connector, secret retrieval, runtime installation, approval engine or activation path is implemented.

The fixture reports a success only to exercise the contract. It explicitly states that no real execution occurred.

The static review surface can download candidate JSON objects locally. It does not persist, transmit, approve or execute them.

## Preserved distinctions

```text
handoff_prepared != handoff_authorized
handoff_authorized != execution_authorized
execution_reported_success != installation_verified
runtime_success != evidence
healthy != safe
healthy != admitted
installed != activated
receipt != professional_evidence
```

## Responsibility split

```text
Pantheon governs the contracts, status, gates and review surface.
An external provisioner would execute after separate human approval.
Hermes may later submit or consume authorized contracts, but does not gain implicit authority here.
OpenWebUI may expose the review surface.
The human decides handoff, execution acceptance and activation.
```
