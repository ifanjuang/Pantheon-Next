# Template Registry

Status: candidate support note — non-executable template registry — documented non-implemented.

This registry lists the current declarative templates under `templates/`. It does not install, execute, deploy or authorize any runtime, client, skill, flow, MCP service, policy gateway, trace backend or prompt runtime.

```text
Hermes Web/dashboard -> selected external chat/session/runtime interaction baseline
Hermes Agent         -> external execution runtime
Pantheon             -> governance and authority
Pantheon Cockpit     -> governed Cards/navigation/decision/status projections
```

## Current templates

| Template | Path | Owner layer | Surface | Status |
|---|---|---|---|---|
| General template scaffold | `templates/README.md` | Pantheon | template index | non-executable |
| Template model | `templates/TEMPLATE_MODEL.md` | Pantheon | template discipline | documented non-implemented |
| Hermes template index | `templates/hermes/README.md` | Hermes | execution template index | non-executable |
| Task Contract handoff | `templates/hermes/handoffs/task_contract_handoff.template.yaml` | Hermes | handoff candidate | non-executable |
| Evidence Pack candidate return | `templates/hermes/returns/evidence_pack_candidate.template.yaml` | Hermes | return envelope candidate | non-executable |
| Source research skill candidate | `templates/hermes/skills/source-research/SKILL.md` | Hermes | skill candidate | non-executable |
| Checkpoint manifest | `templates/hermes/run_manifests/checkpoint_manifest.template.yaml` | Hermes | run manifest candidate | non-executable |
| Devis reprise run manifest | `templates/hermes/run_manifests/devis_reprise_run_manifest.template.yaml` | Hermes | run manifest candidate | non-executable |
| Context Pack preparation flow | `templates/langflow/flows/context_pack_preparation_flow.template.yaml` | Langflow | deterministic flow candidate | non-executable |
| Pantheon trace metadata | `templates/langfuse/trace_metadata/pantheon_trace_metadata.template.yaml` | Langfuse | trace metadata candidate | non-executable |
| MCP capability passport | `templates/mcp_capability_passport.yaml` | Pantheon | MCP policy template | non-executable |
| MCP external tool review | `templates/mcp_external_tool_review.md` | Pantheon | MCP policy review template | non-executable |
| Provenance links | `templates/provenance/provenance_links.template.yaml` | provenance support | provenance link candidate | non-executable |
| Prompt template index | `templates/prompt_templates/README.md` | Pantheon / Hermes | prompt template group | non-executable |
| Evidence extraction prompt | `templates/prompt_templates/evidence_extraction.template.md` | Pantheon / Hermes | evidence candidate extraction | non-executable |
| DCE review prompt | `templates/prompt_templates/dce_review.template.md` | Pantheon / Hermes | professional review candidate | non-executable |
| Visa review prompt | `templates/prompt_templates/visa_review.template.md` | Pantheon / Hermes | professional review candidate | non-executable |
| Client email prompt | `templates/prompt_templates/client_email.template.md` | Pantheon / Hermes | drafting candidate | non-executable |
| Decision record prompt | `templates/prompt_templates/decision_record.template.md` | Pantheon | decision record candidate | non-executable |

The former `templates/openwebui/` namespace is retired. Generic execution handoffs remain under the existing Hermes template owner; governed product projections remain under Pantheon Cockpit. No replacement client-specific template layer is introduced.

## Boundary rules

```text
Template does not mean implementation.
Trace does not mean Evidence Pack.
Manifest does not mean scheduler.
Skill candidate does not mean installed skill.
Flow candidate does not mean deployment.
MCP passport does not mean tool authorization.
Provenance link does not mean proof.
Prompt template does not mean system prompt deployment.
Draft does not mean signed position.
```
