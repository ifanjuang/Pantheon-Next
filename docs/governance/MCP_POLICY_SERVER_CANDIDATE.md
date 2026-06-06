# MCP Policy Server Candidate

Status: candidate — to verify.

Repo state: documented non-implemented.

This document defines a candidate governance posture for using Model Context Protocol (MCP) around Pantheon Next.

It does not implement an MCP server, MCP host, MCP client, endpoint, bridge, gateway, plugin manager, tool runtime, provider router, scheduler, queue, external action, approval engine, memory engine or executable schema.

It does not approve dependency adoption or installation.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Sources reviewed

```text
https://modelcontextprotocol.io/specification/2025-11-25
https://modelcontextprotocol.io/specification/2025-11-25/server/index
https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle
https://modelcontextprotocol.io/specification/2025-11-25/changelog
```

MCP is useful to Pantheon because it standardizes how LLM-facing applications connect to context and tools.

The useful distinction is:

```text
MCP exposes capabilities.
Pantheon governs whether a capability is legitimate for a task.
```

## Decision captured

Accepted:

```text
Pantheon may speak MCP as governance vocabulary and as a future adapter target.
Pantheon may expose doctrine as MCP resources in a future external adapter.
Pantheon may expose validation-only MCP tools in a future external adapter.
Pantheon may define a passport for MCP capabilities.
```

Refused:

```text
Pantheon as MCP host.
Pantheon as MCP runtime.
Pantheon as tool executor.
Pantheon as provider router.
Pantheon as connector gateway with implicit authority.
Pantheon as automatic approval engine.
Pantheon as automatic memory promotion engine.
```

To verify:

```text
Whether a future external repository should host a Pantheon MCP policy adapter.
Whether Pantheon Control should display MCP passport and preflight status.
Whether the MCP policy server belongs behind Hermes, beside Hermes, or as a read-only governance service consumed by multiple tools.
```

To arbitrate:

```text
Whether to promote this candidate into active support doctrine after review.
Whether to create executable schemas under schemas/ later.
Whether to build an external prototype after the doctrine is validated.
```

## Core distinction

MCP gives a standard surface for capabilities.

Pantheon must distinguish:

```text
available != authorized
reachable != safe
listed != reviewed
configured != task_authorized
called != approved
returned != true
observed != evidence
remembered by a runtime != Canonical Memory
```

This is the central reason to use MCP with Pantheon.

## Layer model

```text
Exposure surface
  displays tools, statuses, warnings and User Decision Gates.

Execution runtime
  calls MCP servers, runs tools and produces candidates.

Pantheon policy plane
  defines whether a tool, result, action, memory or delivery is legitimate.

Human decision plane
  validates, rejects, limits or signs.
```

MCP should expand the execution ecosystem.

Pantheon should constrain that ecosystem through explicit status, evidence, scope and approval.

## Allowed forms

### 1. Pantheon as MCP resource server candidate

Allowed as future external adapter only.

Purpose:

```text
Expose governance documents and domain-pack rules as read-only resources.
```

Candidate resources:

```text
pantheon://doctrine/status
pantheon://doctrine/authority-index
pantheon://rules/task-contracts
pantheon://rules/context-packs
pantheon://rules/evidence-pack
pantheon://rules/approvals
pantheon://rules/memory
pantheon://rules/capability-placement
pantheon://domain-packs/architecture/source-policy
pantheon://domain-packs/architecture/evidence-expectations
pantheon://domain-packs/architecture/risk-triggers
pantheon://domain-packs/architecture/delivery-gates
pantheon://domain-packs/architecture/memory-rules
```

Boundary:

```text
Reading doctrine is not execution.
Reading doctrine is not approval.
Reading a domain pack is not professional advice.
```

### 2. Pantheon as MCP validation tool server candidate

Allowed as future external adapter only.

Purpose:

```text
Expose non-executing validation tools.
```

Candidate tools:

```text
pantheon.validate_task_contract
pantheon.check_context_pack
pantheon.classify_mcp_capability
pantheon.check_tool_authorization
pantheon.classify_action_risk
pantheon.check_evidence_pack
pantheon.check_memory_candidate
pantheon.compute_approval_level
pantheon.render_user_decision_gate
```

These tools may return status and reasons.

They must not execute external actions.

### 3. Pantheon as MCP capability passport authority candidate

Allowed as doctrine and template.

Purpose:

```text
Classify MCP servers, resources, prompts and tools before they are used.
```

This is the main governance contribution.

MCP discovery says what exists.

Pantheon passporting says what may be used, where, by whom, under which scope, with which evidence and approval.

### 4. Pantheon as MCP policy gateway candidate

High-risk candidate only.

Purpose:

```text
Check whether an external runtime may call an MCP tool for a specific Task Contract.
```

Boundary:

```text
The policy gateway may allow or block by rule.
It must not run the tool.
It must not select providers silently.
It must not queue work.
It must not become a scheduler.
```

## Forbidden forms

Pantheon must not become:

```text
MCP host
MCP runtime
MCP tool executor
MCP tool registry with implicit authorization
connector gateway with automatic authority
provider router
hidden orchestrator
queue
scheduler
workflow runner
approval engine
memory promotion engine
action server
```

Forbidden tools in any Pantheon MCP adapter:

```text
pantheon.send_email
pantheon.write_file
pantheon.commit_code
pantheon.merge_pull_request
pantheon.update_notion
pantheon.call_external_api
pantheon.run_agent
pantheon.launch_workflow
pantheon.promote_memory
pantheon.approve_action
pantheon.route_model
```

These belong to external tools or runtimes.

Pantheon may govern their legitimacy.

It must not perform them.

## MCP capability passport

Every MCP capability should be evaluated through a passport before use.

Minimum passport shape:

```yaml
mcp_capability_passport:
  passport_id:
  reviewed_at:
  reviewed_by:
  mcp_server:
    server_id:
    server_name:
    canonical_uri:
    transport: stdio | http | other
    protocol_revision:
    source:
    trust_level: trusted | internal | external | unknown
  capability:
    primitive: resource | prompt | tool
    name:
    description_snapshot:
    description_hash:
    annotations_snapshot:
    icons_reviewed: yes | no | not_applicable
  operation:
    reads_private_data: true | false | unknown
    writes_external_state: true | false | unknown
    can_execute_code: true | false | unknown
    can_send_to_external_party: true | false | unknown
    can_modify_dossier: true | false | unknown
    can_change_memory: true | false | unknown
    can_commit_professional_position: none | low | medium | high | critical
  governance:
    activation_state: unavailable | detected | disabled | watch | candidate | sandbox_enabled | project_enabled | dossier_enabled | domain_enabled | organization_enabled | suspended | deprecated | rejected
    task_authorization: unauthorized | task_authorized
    allowed_scopes: []
    forbidden_scopes: []
    risk_level: low | medium | high | critical
    approval_required: C0 | C1 | C2 | C3 | C4 | C5
    memory_behavior: none | candidate_only | never_canonical
    evidence_required: []
    context_minimization_required: true | false
    user_decision_gate_required: true | false
  interface:
    allowed_inputs: []
    allowed_outputs: []
    forbidden_outputs: []
    required_envelope: task_contract_in__candidate_out__evidence_pack_out
  result_handling:
    default_output_status: draft | candidate | to_verify | blocked
    evidence_pack_required: true | false
    raw_result_never_final: true
  revocation:
    status: active | suspended | revoked
    reason:
```

The passport is not an executable schema.

If a canonical schema is later needed, it must be proposed under `schemas/` only after explicit approval.

## Policy decision result

A Pantheon policy check should return a decision object, not execute work.

Candidate shape:

```yaml
policy_decision:
  decision: allow | allow_with_gate | block | needs_revision | needs_evidence | not_applicable
  status: candidate
  reasons: []
  required_approval:
  required_user_gate:
  required_evidence: []
  required_context_changes: []
  allowed_tool_call:
    server_id:
    tool_name:
    scope:
    argument_constraints: []
  forbidden_actions: []
  memory_behavior:
  next_step:
```

`allow` does not mean validated truth.

`allow` means only that the external runtime may proceed under the stated contract.

## Invocation lifecycle

```text
1. User request is captured by the exposure surface.
2. A Task Contract is drafted.
3. Pantheon policy check validates the Task Contract.
4. The execution runtime proposes a capability to call.
5. Pantheon checks the MCP capability passport and task authorization.
6. If allowed, the execution runtime calls the MCP tool.
7. The MCP tool returns a raw result.
8. Raw result is downgraded to Result Candidate.
9. Evidence Pack Candidate is assembled.
10. Pantheon checks evidence, memory and approval implications.
11. The exposure surface displays the User Decision Gate.
12. The human decides.
```

## Security stance

MCP tool descriptions, annotations, icons and metadata are not governance truth.

They must be treated as untrusted until reviewed.

Minimum controls:

```text
description snapshot
description hash
source URI
server trust level
transport class
OAuth or token boundary
scope minimization
allowed arguments
forbidden arguments
read/write classification
external-effect classification
review date
revocation status
```

Important MCP-specific risks:

```text
tool poisoning
tool shadowing
rug pull after review
excessive scopes
token passthrough
resource exfiltration
description injection
cross-server trust leakage
silent write capability
implicit tool authorization
```

Pantheon mitigation:

```text
deny by default
passport before use
Task Contract before invocation
approval ceiling before action
Evidence Pack Candidate after result
Memory Candidate only unless approved
human decision for consequential action
```

## Relationship to Pantheon Control

Pantheon Control may display MCP capability posture.

Allowed display:

```text
MCP server reachable
MCP tools listed
passport status
activation state
task authorization state
risk level
required approval
last preflight
revocation status
```

Forbidden dashboard collapse:

```text
reachable MCP server = authorized capability
listed tool = safe tool
green health check = approval
preflight pass = final truth
```

Pantheon Control, if built, should show eligible execution surfaces and risks.

It must not become automatic routing, scheduling, hidden orchestration or implicit authorization.

## Relationship to domain packs

A domain pack may be exposed as read-only MCP resources through a future external adapter.

The domain pack still does not advise, approve, execute, send or remember by itself.

Example for architecture:

```text
pantheon://domain-packs/architecture/source-policy
pantheon://domain-packs/architecture/evidence-expectations
pantheon://domain-packs/architecture/risk-triggers
pantheon://domain-packs/architecture/delivery-gates
pantheon://domain-packs/architecture/memory-rules
```

This allows external tools to consult the professional method without copying it into each prompt.

## Adoption phases

### Phase 0 — current document

```text
candidate doctrine only
no implementation
no schema
no runtime
```

### Phase 1 — templates

```text
non-executable MCP capability passport template
non-executable MCP external tool review template
```

### Phase 2 — external adapter prototype

Only after review.

```text
external repository
read-only resources first
validation-only tools second
no external action tools
```

### Phase 3 — Hermes consumption

Only after adapter prototype review.

```text
Hermes asks Pantheon policy check before calling consequential MCP tools.
Hermes still executes.
Pantheon still governs.
```

### Phase 4 — exposure surface display

Only after Phase 3.

```text
OpenWebUI or Pantheon Control displays policy decisions, passports, evidence needs and User Decision Gates.
```

## Review questions

Before promotion, answer:

```text
1. Is MCP policy checking part of Pantheon doctrine or only an adapter profile?
2. Should the passport become a schema later?
3. Which MCP primitives are allowed first: resources only, or tools too?
4. Which tools must always be blocked without human approval?
5. Where should the future external adapter live?
6. Should Pantheon Control display passport status as first-class dashboard information?
7. What counts as sufficient descriptor review before task authorization?
8. How are descriptor changes detected and revoked?
```

## Boundary phrase

```text
Pantheon may speak MCP.
Pantheon must not become the MCP runtime.
MCP exposes capabilities.
Pantheon governs eligibility, proof, scope, memory, approval and status.
The execution runtime acts only under contract.
The human decides.
```
