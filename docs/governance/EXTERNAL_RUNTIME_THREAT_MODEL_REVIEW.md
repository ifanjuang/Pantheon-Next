# External Runtime Threat Model Review

Status: active support doctrine — review method for external runtimes and privileged AI workspaces.

This document defines how Pantheon Next reviews an external runtime, AI workspace, tool host, connector host or model-serving surface before it is used around consequential professional work.

It is a review method, not an implementation.

It does not create a runtime, scanner, sandbox, firewall, installer, scheduler, queue, provider router, connector gateway, MCP host, approval engine, memory engine, OpenWebUI configuration, Hermes skill, Docker configuration or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

External AI systems increasingly combine capabilities that were previously separate:

```text
chat surface
agent execution
tool calling
file access
repository access
email / calendar access
local model serving
memory / retrieval
scheduled tasks
MCP or connector surfaces
administration settings
```

Pantheon must review that combined surface before treating it as safe to use in a professional dossier.

The review answers one question:

```text
What consequential power does this runtime expose, and which Pantheon gate must constrain it?
```

## Core rule

```text
Runtime power is not governance authority.
```

An external runtime may expose powerful capabilities. It may execute. It may observe. It may prepare candidates. It may carry a task.

It must not approve, validate, canonize, promote memory, authorize external effects, alter doctrine or silently expand scope.

## When this review is required

Run this review when a system, adapter, plugin, tool host or workspace can touch one of the following:

```text
private or client material
professional source interpretation
project files or repository content
email, calendar or messaging channels
long-lived memory, index or recall
model serving or provider selection
scheduled or background tasks
runtime installation or configuration
privileged local or host-control surfaces
MCP, gateway or connector access
```

If the system is read-only, low-risk and non-consequential, a light review is sufficient.

If the system can create a false truth, wrong memory, unapproved external effect, invalid approval, unauthorized action or scope expansion, the full review is required.

## Review record

Minimum fields:

```text
external_runtime_review:
  runtime_name:
  reviewed_ref:
  reviewed_date:
  reviewed_by:
  system_role: exposure_surface | execution_runtime | observability_layer | connector_gateway | model_runtime | mixed_workspace | other
  binding_status: unbound | candidate | sandbox | project_scoped | organization_scoped | refused
  trusted_user_assumption:
  exposure_posture:
  privileged_capabilities:
  data_access:
  external_effects:
  memory_effects:
  model_effects:
  scheduling_effects:
  host_control_surface:
  untrusted_content_paths:
  prompt_injection_posture:
  token_or_permission_granularity:
  auditability:
  reversibility_or_mitigation:
  pantheon_gate_required:
  approval_ceiling:
  evidence_expectation:
  safe_default:
  decision: accepted | refused | to_verify | to_arbitrate
  repo_state: documented_non_implemented | adapter_outside_pantheon | implemented_elsewhere | refused
```

This is a governance record. It does not authorize runtime installation by itself.

## Capability surface checklist

The review must identify whether the runtime can:

```text
read private material
write or modify durable material
send, publish or notify externally
store, index, rank or recall long-lived information
execute code or commands
alter runtime configuration
select or serve models
schedule or resume work
call connectors, MCP tools or provider gateways
alter a repository or project artifact
produce user-visible professional output
```

Each positive answer must be mapped to:

```text
risk class
scope
approval need
evidence need
safe fallback
```

## Host-control surface classification

Host-control power is a stronger concern than ordinary tool availability.

Use this vocabulary:

```text
host_control_surface:
  none
  scoped_filesystem
  broad_filesystem
  shell_user
  shell_admin
  container_host_control
  remote_host_control
  cloud_admin
```

Default classification:

```text
none -> not a host-control concern
scoped_filesystem -> review scope and minimization
broad_filesystem -> high risk
shell_user -> high risk
shell_admin -> critical risk
container_host_control -> critical risk
remote_host_control -> critical risk
cloud_admin -> critical risk
```

Critical host-control power must not be treated as a normal skill, plugin or workspace option.

It requires at minimum:

```text
explicit scope
explicit approval path
strong evidence expectation
sandbox or isolation posture where relevant
reversibility or mitigation note
human-visible gate before consequential use
```

## Untrusted content paths

External runtime review must identify untrusted content paths.

Common paths:

```text
web results
fetched pages
uploaded files
read emails
notes
runtime memory
retrieved knowledge
connector output
MCP output
model output reused as context
third-party tool output
```

Pantheon rule:

```text
Untrusted content enters as data.
It must not become instruction, proof, approval or memory by proximity.
```

Any adapter may wrap, label or isolate untrusted content. That adapter behavior lives outside Pantheon. Pantheon governs the requirement and the output status.

## Prompt-injection posture

The review must record whether the runtime distinguishes:

```text
instructions from trusted operator
instructions from system / policy
content from external source
content from retrieved memory
content from tool output
```

If the runtime cannot preserve that distinction, its outputs remain higher-risk candidates and must not be used for consequential delivery without stricter human review.

## Permission and token granularity

The review must classify permission posture:

```text
permission_granularity:
  coarse
  role_based
  capability_scoped
  task_scoped
  dossier_scoped
  unknown
```

Coarse permissions are not forbidden, but they raise the approval burden when a broad token or session can reach more capability than the Task Contract requires.

Least capability remains the default.

## Exposure posture

The review must distinguish:

```text
local_only
private_network
vpn_or_tunnel
reverse_proxy
public_internet
unknown
```

Exposure posture does not authorize use. It only informs risk.

A public or unclear exposure posture blocks professional dossier use until reviewed.

## Relationship to existing doctrine

This review applies:

```text
EXTERNAL_TOOLS_POLICY.md     -> external tools are capabilities, not authority
CAPABILITY_PLACEMENT.md      -> consequential effects pass through Pantheon
ADAPTERS_AND_BINDINGS.md     -> runnable configuration lives outside Pantheon
UNIFORM_CAPABILITY_GOVERNANCE.md -> one law, one passport, one gate
TASK_CONTRACTS.md            -> task scope and allowed outputs
EVIDENCE_PACK.md             -> reviewable evidence and limitations
APPROVALS.md                 -> approval level
MEMORY.md                    -> no automatic memory promotion
SCOPE_ISOLATION.md           -> no silent scope expansion
```

## Outcomes

Allowed review outcomes:

```text
accepted_for_reference
accepted_for_sandbox
accepted_for_adapter_design
accepted_for_project_scoped_use
needs_more_evidence
needs_sandbox
needs_adapter
needs_human_approval
blocked
refused
```

An outcome may approve documentation or adapter design. It does not approve execution unless the separate Task Contract and approval path allow it.

## Safe defaults

If the review is incomplete:

```text
no external effect
no canonical effect
no memory promotion
no privileged execution
no client-data use
candidate-only output
surface the capability gap
```

## Boundary phrase

```text
The runtime may be powerful.
The review makes the power legible.
Pantheon governs the consequence.
The human decides.
Only the validated remains.
```
