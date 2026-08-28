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

Demonstrated active drift initially included:

- `docs/HTTP_API_CONTRACT.md`;
- protected `mcp-server/docs/HTTP_API_CONTRACT.md`;
- `docs/governance/APPROVALS.md`;
- `docs/governance/RUN_GRAPH.md`;
- `docs/governance/EVIDENCE_PACK.md`;
- `docs/governance/TASK_CONTRACTS.md`;
- `docs/governance/GOVERNANCE_COLLEGE.md`;
- `docs/intro-professionnelle.md`;
- the recently converged `AGENT_PLUGINS_INTEROPERABILITY.md`, whose generic `Hermes Web/dashboard` wording accidentally made a web surface sound selected/mandatory.

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
runtime PEP                                          = consequential-effect enforcement
Pantheon Cockpit                                     = governed projections / Cards / decisions / status
Pantheon Next                                        = governance / authority
human                                                = consequential decision
```

No capability is removed. Approval, Run Trace View, Evidence Pack, Task Contract, Governance College and deterministic HTTP policy/preflight responsibilities remain in their existing owners.

The protected HTTP contract now preserves PDP/PEP separation explicitly rather than collapsing enforcement into either Pantheon or a WebUI.

## Review-driven widening

PR review correctly identified that the original five-file regression was too narrow and that the stable HTTP pointer contradicted its protected owner.

Corrections applied:

- protected HTTP contract corrected alongside its stable pointer;
- Task Contracts and Governance College corrected because they still carried active OpenWebUI ownership;
- regression now scans active doctrine for retired ownership phrases, rather than protecting only a hand-maintained five-file list;
- PR body expanded with required Role/Rite/Space change context, overlap analysis, consumers, rollback, authority and runtime impact.

The sweep still distinguishes current ownership statements from historical provenance. The objective is not to delete the word `OpenWebUI` from Git history.

## Preserved invariants

```text
runtime display != governance authority
runtime output != Evidence
Evidence Pack Candidate != admitted Evidence
projection != persistence
projection != approval
optional client selected != authority transfer
runtime PEP enforcement != Pantheon governance authority
runtime success != Evidence
```

## Test

`tests/test_openwebui_integration_owner_retirement.py` protects core corrected surfaces and scans active doctrine for present-tense retired ownership phrases while continuing to allow historical/retirement provenance elsewhere.

## Finish criteria

- no prohibited OpenWebUI ownership phrase remains in active doctrine;
- Hermes WebUI is described as optional/proposed, not required;
- protected HTTP PDP/PEP responsibility remains explicit;
- no new client/runtime/owner introduced;
- Governance CI, Architecture Audit and Obsolete Authority green on exact PR head;
- no unresolved review finding.