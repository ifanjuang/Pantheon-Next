# Template Registry

Status: non-executable template registry.

This registry lists the current declarative templates under `templates/`.

It does not install, execute, deploy or authorize any OpenWebUI Function, Tool, Pipe, Filter, Action, Pipeline, Hermes skill, Langflow flow, Langfuse trace backend, MCP server, MCP client, policy gateway or provenance graph runtime.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Current templates

| Template | Path | Owner layer | Surface | Status |
|---|---|---|---|---|
| General template scaffold | `templates/README.md` | Pantheon | template index | non-executable |
| OpenWebUI template index | `templates/openwebui/README.md` | OpenWebUI | cockpit template index | non-executable |
| Pantheon cockpit safe profile | `templates/openwebui/model_profiles/pantheon-cockpit-safe.template.yaml` | OpenWebUI | model profile candidate | non-executable |
| Request Hermes execution | `templates/openwebui/actions/request_hermes_execution.template.yaml` | OpenWebUI | thin Action candidate | non-executable |
| Candidate status banner | `templates/openwebui/filters/candidate_status_banner.template.yaml` | OpenWebUI | display Filter candidate | non-executable |
| Urgent fiche triage | `templates/openwebui/forms/urgent_fiche_triage.template.md` | OpenWebUI | form template candidate | non-executable |
| Hermes template index | `templates/hermes/README.md` | Hermes | execution template index | non-executable |
| Task Contract handoff | `templates/hermes/handoffs/task_contract_handoff.template.yaml` | Hermes | handoff candidate | non-executable |
| Evidence Pack candidate return | `templates/hermes/returns/evidence_pack_candidate.template.yaml` | Hermes | return envelope candidate | non-executable |
| Source audit skill candidate | `templates/hermes/skills/source_audit_skill_candidate.template.yaml` | Hermes | skill candidate | non-executable |
| Checkpoint manifest | `templates/hermes/run_manifests/checkpoint_manifest.template.yaml` | Hermes | run manifest candidate | non-executable |
| Context Pack preparation flow | `templates/langflow/flows/context_pack_preparation_flow.template.yaml` | Langflow | deterministic flow candidate | non-executable |
| Pantheon trace metadata | `templates/langfuse/trace_metadata/pantheon_trace_metadata.template.yaml` | Langfuse | trace metadata candidate | non-executable |
| MCP capability passport | `templates/mcp_capability_passport.yaml` | Pantheon | MCP policy template | non-executable |
| MCP external tool review | `templates/mcp_external_tool_review.md` | Pantheon | MCP policy review template | non-executable |
| Provenance links | `templates/provenance/provenance_links.template.yaml` | provenance support | provenance link candidate | non-executable |

## Boundary rules

```text
Template does not mean implementation.
Trace does not mean Evidence Pack.
Manifest does not mean scheduler.
Action template does not mean executable Action.
Skill candidate does not mean installed skill.
Flow candidate does not mean Langflow deployment.
MCP passport does not mean tool authorization.
MCP review does not mean dependency approval.
Provenance link does not mean proof.
```

## Next registry fields

If templates become more numerous, this registry should grow these columns:

```text
template_id
owner_layer
runtime_status
allowed_inputs
allowed_outputs
forbidden_outputs
approval_behavior
memory_behavior
scope_behavior
risk_level
```
