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

## Convergence

Current split used consistently:

```text
Hermes Web/dashboard + compatible clients = runtime interaction
Hermes Agent                              = external execution
Pantheon Cockpit                          = governed projections / Cards / decisions / status
Pantheon Next                             = governance / authority
human                                     = consequential decision
```

No capability is removed. Approval, Run Trace View, Evidence Pack, deterministic HTTP policy exposure and public professional explanation remain in their existing owners.

## Preserved invariants

```text
runtime display != governance authority
runtime output != Evidence
Evidence Pack Candidate != admitted Evidence
projection != persistence
projection != approval
client selected != authority transfer
runtime success != Evidence
```

## Test

`tests/test_openwebui_integration_owner_retirement.py` now protects these five active surfaces from regaining an OpenWebUI dependency while continuing to allow historical provenance elsewhere.

## Finish criteria

- no `OpenWebUI` occurrence in the five corrected active surfaces;
- no new client/runtime/owner introduced;
- Governance CI, Architecture Audit and Obsolete Authority green on exact PR head;
- no unresolved review finding.