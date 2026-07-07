# Capability Candidate Model

Status: candidate support doctrine — governed capability-candidate grammar for external repositories, tools, bindings and runtime candidates.

Runtime status: non-executable.

This document defines how Pantheon Next records and reviews a capability before it becomes a sandboxed, project-scoped or agency-scoped runtime binding.

It does not implement a runtime, installer, tool registry, connector gateway, provider router, scheduler, queue, plugin manager, MCP host, memory engine, approval engine, OpenWebUI plugin, Hermes skill, Docker service, operation, platform component or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

External repositories and tools can be useful without being safe, installed, approved or adopted.

Pantheon needs a middle object between an inspiration note and an executable adapter:

```text
External reference
-> Capability Candidate
-> Capability Slot
-> Binding Candidate
-> Runtime Status Candidate
-> Gate
-> human decision
```

The Capability Candidate Model exists to prevent this collapse:

```text
interesting repository != dependency
local runnable app != approved capability
available feature != safe professional use
health check != trust
runtime output != evidence
```

## Relationship to existing doctrine

This model composes existing doctrine. It does not replace it.

```text
COMPETENCE_MODEL.md                 -> what a competence, skill, tool, evidence, action and gate are.
CAPABILITY_PLACEMENT.md             -> where the capability belongs by primary effect.
PANTHEON_CONTROL_PLANE_BOUNDARY.md   -> how operational status may be displayed without becoming runtime.
EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md -> how privileged runtimes are reviewed.
EXTERNAL_TOOLS_POLICY.md             -> external tools are capabilities, not authority.
CARD_STACK_MODEL.md                  -> how the candidate may appear as a cockpit card.
```

## Core distinction

A Capability Candidate is not a Competence.

A Capability Candidate is a possible external or adapter-backed means of satisfying one or more abstract capabilities.

A Competence is the governed reusable ability.

A Binding Candidate is the possible execution-side attachment between the abstract capability and a specific runtime, tool, repository or service.

```text
Compétence: préparer un corpus documentaire RAG.
Capability Candidate: Chunky as possible document preparation workspace.
Binding Candidate: chunky-local-docker under Hermes.
Runtime Status Candidate: installed / healthy / version / logs reported by Hermes.
Gate: approve for sandbox indexing test.
```

## Capability Slot

A Capability Slot is the abstract function before any tool is adopted.

Minimum shape:

```yaml
capability_slot:
  id:
  title:
  abstract_function:
  professional_use_case:
  expected_inputs:
  expected_outputs:
  forbidden_outputs:
  likely_runtime_owner: hermes | openwebui | external_runtime | connector_gateway | other
  pantheon_governs:
  openwebui_exposes:
  hermes_executes:
  human_approves:
  evidence_expectation:
  approval_ceiling:
  memory_impact:
  external_effect:
  sensitive_data_classes:
  safe_default:
```

The slot is tool-agnostic.

The binding candidate is tool-specific.

## Capability Candidate

Minimum shape:

```yaml
capability_candidate:
  id:
  title:
  source:
    kind: repository | service | local_app | library | connector | model | other
    locator:
    reviewed_ref:
    reviewed_date:
  capability_slot:
  candidate_binding:
  repository_or_product_status:
  install_status:
  health_status:
  update_status:
  activation_status:
  governance_status:
  data_exposure:
  host_control_surface:
  provider_or_network_effects:
  memory_effects:
  external_effects:
  evidence_outputs:
  approval_required:
  required_gates:
  safe_default:
  decision:
  trace_refs:
```

This record is governance metadata. It does not install, run, call or authorize anything.

## Candidate lifecycle

Recommended lifecycle:

```text
observed_reference
reference_review_open
capability_slot_defined
candidate_binding_defined
risk_review_open
accepted_for_reference
accepted_for_sandbox
approved_for_sandbox
approved_for_project
approved_for_agency
suspended
blocked
refused
superseded
```

Interpretation:

| Status | Meaning |
|---|---|
| `observed_reference` | A repository, product or pattern has been noticed. |
| `reference_review_open` | Review started; no capability status yet. |
| `capability_slot_defined` | The abstract function is clear. |
| `candidate_binding_defined` | A possible execution-side binding is named. |
| `risk_review_open` | Threat / privacy / scope / evidence review is incomplete. |
| `accepted_for_reference` | Useful as inspiration, not executable. |
| `accepted_for_sandbox` | Worth testing with non-sensitive material. |
| `approved_for_sandbox` | Human-approved sandbox use under constraints. |
| `approved_for_project` | Approved for one bounded project or dossier scope. |
| `approved_for_agency` | Approved as an agency-level capability. |
| `suspended` | Temporarily blocked pending review. |
| `blocked` | Use blocked by a known risk or missing gate. |
| `refused` | Rejected for Pantheon purposes. |
| `superseded` | Replaced by a better candidate or internal method. |

Lifecycle status is not runtime state.

## Operational status

Operational status may be displayed, but it must not be confused with governance status.

Use the control-plane vocabulary where relevant:

```text
install_status
health_status
update_status
activation_status
rollback_status
governance_status
```

Mandatory non-equivalence:

```text
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
binding_selected != dependency_adopted
sandbox_enabled != production_approved
```

## Gate families

A Capability Candidate may require one or several gates.

Common gates:

```text
source_review_gate
license_review_gate
sandbox_approval_gate
external_provider_gate
data_exit_gate
client_data_gate
analytics_gate
update_authorization_gate
runtime_health_gate
rollback_gate
evidence_quality_gate
memory_promotion_gate
external_action_gate
indexation_approval_gate
recording_consent_gate
```

A gate authorizes only a status or next procedure.

A gate does not execute the tool.

## Card Stack projection

A Capability Candidate may appear in the Card Stack as one or more cards.

Recommended projection:

```text
Capability Candidate Card      -> what the candidate is.
Capability Slot Card           -> what abstract function it may satisfy.
Binding Candidate Card         -> how Hermes or another runtime could execute it.
Runtime Status Candidate Card  -> install / health / update / activation if reported.
Gate Card                      -> decision required before use.
Risk Card                      -> why use is limited or blocked.
Evidence Expectation Card      -> what outputs must carry to be reviewable.
```

These cards are display and governance objects.

They do not install, run, approve or remember anything.

## Review outputs

A capability review may produce:

```text
Capability Candidate
Capability Slot
Binding Candidate
Runtime Status Candidate
Capability Gap
Gate Recommendation
Reference Review
Sandbox Test Proposal
```

It must not produce:

```text
runtime installation
adapter implementation
approved dependency
approved production use
validated truth
automatic memory promotion
external action authorization
```

## Default posture for external repositories

Until a review is complete:

```text
install_status: unknown | absent
governance_status: candidate | to_verify
activation_status: unavailable
safe_default: no client data, no external effect, no memory promotion, no production use
```

## Human decision

A human decision is required before:

```text
installing a new runtime on agency infrastructure;
using client or confidential material;
allowing cloud or external-provider calls;
turning sandbox output into project evidence;
indexing output into RAG or memory;
allowing external actions;
authorizing updates;
changing agency-level capability status.
```

## Boundary phrase

```text
A candidate may be useful.
A binding may be runnable.
A runtime may be healthy.
Pantheon governs whether its outputs may matter.
The human decides.
Only the validated remains.
```
