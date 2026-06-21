# AI log — NAS installation profiles candidate

Date: 2026-06-21
Repository: `ifanjuang/Pantheon-Next`

## Request

User asked to continue development around installation facilitation, imagining a NAS with nothing installed. User added that some NAS may have integrated GPUs and that the NAS could also redirect to another machine/service.

## Search performed

```text
NAS install installation profile gpu docker setup
```

No direct equivalent document was found in the repository.

## Created

- `docs/governance/NAS_INSTALLATION_PROFILES.md`

## Decision

Decision Zeus: Accepté as candidate orientation.

The document classifies NAS deployment roles without implementing installation.

## Covered

- storage-only NAS;
- CPU service host;
- integrated media acceleration;
- NPU / AI-light appliance;
- GPU-capable NAS;
- NAS as storage with external compute;
- NAS as secure redirection / gateway point;
- private-only redirection;
- public read-only redirection;
- split subdomain pattern;
- NAS-to-compute delegation;
- capability proof checklist.

## Boundary preserved

No protected path changed.
No Docker file created.
No compose file created.
No script created.
No firewall, DNS, VPN or reverse-proxy rule created.
No GPU driver configured.
No runtime service created.
No queue, scheduler, memory engine, vector database, GraphRAG runtime, LangGraph runtime, Langflow runtime, Hermes command surface or connector was created.

## Doctrine retained

```text
Storage availability is not compute capability.
GPU presence is not LLM readiness.
Network exposure is not functional authorization.
The NAS stores by default.
The NAS may redirect when security is controlled.
Compute is earned by proof.
Acceleration is classified, not assumed.
```
