# Residual OpenWebUI active-document convergence — 2026-08-28

## Objective

Audit remaining active repository documents after #666/#780/#781/#783 and remove residual OpenWebUI ownership only where it still described current architecture. Preserve historical ai_logs and dated implementation provenance.

## Revalidated base

Pantheon-Next `main`: `f6fda6f20b31e35447a28ddd8ad45e79a2c5f812`.

Open issue search found no active issue assigning `OpenWebUI exposes`. Broad repository search still returned many historical ai_logs plus a small set of active documents.

## Classification

Left unchanged:

- `ai_logs/**`: historical provenance;
- dated implementation history such as `implementation/docs/architecture/2026-08-03-stable-openwebui-projection-routes.md`: historical implementation provenance unless a current owner points to it as authority;
- `templates/README.md`: already client-agnostic and explicitly protects retirement of `templates/openwebui/`.

Demonstrated active drift:

- `docs/HTTP_API_CONTRACT.md` still said `OpenWebUI exposes`;
- `docs/governance/APPROVALS.md` assigned approval display to OpenWebUI;
- `docs/governance/RUN_GRAPH.md` assigned Run Trace display to OpenWebUI;
- `docs/governance/EVIDENCE_PACK.md` assigned Evidence Pack exposure/review to OpenWebUI;
- `docs/intro-professionnelle.md` still publicly described an OpenWebUI cockpit as the visible Pantheon surface.

## Hermes WebUI clarification

During the slice, `nesquena/hermes-webui` was explicitly identified as an available Hermes web/mobile surface that should remain proposed/optional rather than mandatory.

Upstream revalidation on 2026-08-28 observed:

- public repository `nesquena/hermes-webui`;
- MIT licence;
- active upstream development;
- near-CLI web/mobile interaction positioning;
- chat runs Hermes Agent in-process by default, with an optional Gateway-backed chat mode documented separately.

Therefore Hermes WebUI must not be collapsed into a generic mandatory `Hermes Web/dashboard` owner. If selected, it is a replaceable external runtime/client surface requiring its own deployment/security qualification.

```text
Hermes WebUI available != Hermes WebUI selected
Hermes WebUI selected != Pantheon authority transferred
Hermes WebUI runtime approval card != Pantheon human approval
web interaction success != Evidence
```

## Convergence

Current split used consistently:

```text
Hermes WebUI (optional/proposed) or compatible clients = possible runtime interaction
Hermes Agent                                         = external execution
Pantheon Cockpit                                     = governed projections / Cards / decisions / status
Pantheon Next                                        = governance / authority
human                                                = consequential decision
```

No capability is removed. Approval, Run Trace View, Evidence Pack, deterministic HTTP policy exposure and public professional explanation remain in their existing owners.

`docs/governance/AGENT_PLUGINS_INTEROPERABILITY.md` is also corrected in this slice so its prior merged `Hermes Web/dashboard` wording does not accidentally make Hermes WebUI mandatory.

## Preserved invariants

```text
runtime display != governance authority
runtime output != Evidence
Evidence Pack Candidate != admitted Evidence
projection != persistence
projection != approval
optional client selected != authority transfer
runtime success != Evidence
```

## Test

`tests/test_openwebui_integration_owner_retirement.py` protects the corrected active surfaces from regaining an OpenWebUI dependency and now also protects the explicit optional Hermes WebUI posture, while continuing to allow historical provenance elsewhere.

## Finish criteria

- no `OpenWebUI` occurrence in the corrected active surfaces;
- Hermes WebUI is described as optional/proposed, not required;
- no new client/runtime/owner introduced;
- Governance CI, Architecture Audit and Obsolete Authority green on exact PR head;
- no unresolved review finding.