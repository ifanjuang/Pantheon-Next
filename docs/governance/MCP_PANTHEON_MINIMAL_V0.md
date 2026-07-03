# MCP Pantheon Minimal V0

Status: candidate support doctrine — bounded minimal profile for Pantheon MCP use.

Repo state: documented non-implemented for this profile. Existing `mcp-server/` artifacts may already provide partial read-only validation surfaces, but this document does not change their runtime status.

This document defines the smallest acceptable Pantheon MCP posture for integration with OpenWebUI and Hermes.

It does not implement an MCP server, MCP client, endpoint, host, bridge, gateway, provider router, scheduler, queue, approval engine, memory engine, connector runtime, OpenWebUI Function, Hermes skill or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon may use MCP to expose governance context and validation reports. It must not use MCP to become the execution system.

Minimal V0 answers:

```text
What is the smallest MCP posture that is useful to Hermes and OpenWebUI without creating governance drift?
```

## Position

Accepted:

```text
MCP Pantheon may expose read-only resources.
MCP Pantheon may expose validation-only tools.
MCP Pantheon may prepare candidates and reports.
MCP Pantheon may help Hermes frame work under a Task Contract.
MCP Pantheon may help OpenWebUI display status, gates and gaps.
```

Refused:

```text
MCP Pantheon as host.
MCP Pantheon as runtime.
MCP Pantheon as connector gateway.
MCP Pantheon as provider router.
MCP Pantheon as scheduler or queue.
MCP Pantheon as approval engine.
MCP Pantheon as memory promotion engine.
MCP Pantheon as external-action server.
MCP Pantheon as hidden enforcement proxy by default.
```

To verify:

```text
Whether V0 should be implemented only in the existing read-only mcp-server/ surface.
Whether OpenWebUI should consume MCP results directly or only through Hermes.
Whether a separate hard enforcement proxy is useful later.
```

To arbitrate:

```text
Whether the term Policy Server remains acceptable or should be narrowed to Governance Resource Server / Eligibility Server.
Whether this document supersedes parts of older MCP candidate wording.
```

## Minimal V0 layers

```text
OpenWebUI        displays MCP posture and gates.
Hermes           consumes MCP governance resources and validation reports.
MCP Pantheon     returns doctrine, reports, skeletons and gaps as data.
Pantheon docs    remain the source of truth.
Human            decides consequential outcomes.
```

## V0 allowed resources

V0 may expose only read-only governance resources.

Candidate resource families:

```text
pantheon://status
pantheon://authority-index
pantheon://module-map
pantheon://capability-placement
pantheon://task-contracts
pantheon://context-packs
pantheon://evidence-pack
pantheon://approvals
pantheon://registre-probatoire
pantheon://domain-pack-spec
pantheon://architecture-domain-pack
pantheon://mcp-boundary
pantheon://tripartite-interface
pantheon://refusal-fixtures
```

Each resource response must include:

```yaml
resource:
  uri:
  source_file:
  repo_ref:
  authority:
  status:
  summary:
  relevant_rules:
  open_questions:
```

Rules:

```text
A resource may quote doctrine.
A resource may summarize doctrine.
A resource must not invent doctrine.
A candidate document remains candidate when exposed.
Reading a resource is not approval.
```

## V0 allowed tools

V0 tools must be side-effect-free.

Allowed tool families:

```text
pantheon.list_sources
pantheon.read_doctrine
pantheon.validate_task_contract
pantheon.classify_request
pantheon.check_scope
pantheon.check_external_action
pantheon.check_evidence_pack_candidate
pantheon.check_register_candidate
pantheon.validate_capability_passport
pantheon.prepare_evidence_pack_skeleton
pantheon.prepare_result_candidate_format
pantheon.report_capability_gap
```

Every tool response must state:

```yaml
response:
  status: candidate | report | blocked | not_applicable
  scope:
  reasons: []
  required_evidence: []
  required_approval:
  required_user_gate:
  blocked_actions: []
  uncertainties: []
  next_human_decision:
```

Rules:

```text
Validation report != authorization.
Classification report != approval.
Evidence skeleton != Evidence Pack.
Register candidate check != Registre Probatoire entry.
External-action check must default to block unless a Task Contract and approval path exist.
```

## V0 forbidden tools

The following tool names or effects are forbidden in any Pantheon MCP V0 surface:

```text
pantheon.send_email
pantheon.write_file
pantheon.delete_file
pantheon.commit_code
pantheon.merge_pull_request
pantheon.update_notion
pantheon.call_external_api
pantheon.run_agent
pantheon.launch_workflow
pantheon.schedule_job
pantheon.route_provider
pantheon.install_skill
pantheon.approve_action
pantheon.promote_memory
pantheon.create_registre_probatoire_entry
pantheon.validate_professional_truth
```

These effects belong to external tools, external runtimes, human approval paths or governed validation paths. Pantheon may classify their legitimacy. It must not perform them.

## V0 invocation lifecycle

```text
1. OpenWebUI captures the request and displays the initial intent.
2. Hermes or OpenWebUI drafts an Intent Candidate.
3. Hermes calls MCP Pantheon to classify the request.
4. If needed, Hermes calls MCP Pantheon to prepare or validate a Task Contract skeleton.
5. MCP Pantheon returns a report, not authorization.
6. Hermes executes only effects allowed under a valid Task Contract.
7. Hermes returns Result Candidate + Evidence Pack Candidate.
8. MCP Pantheon may validate the candidate shape and report gaps.
9. OpenWebUI displays result, evidence, gaps and User Decision Gate.
10. The human decides.
```

## Minimum capability passport before external MCP use

Any external MCP resource, prompt or tool should be passported before use.

Minimal V0 passport:

```yaml
mcp_capability_passport:
  server_id:
  server_name:
  transport:
  trust_level: trusted | internal | external | unknown
  primitive: resource | prompt | tool
  name:
  description_snapshot:
  description_hash:
  reads_private_data: true | false | unknown
  writes_external_state: true | false | unknown
  can_execute_code: true | false | unknown
  can_send_to_external_party: true | false | unknown
  can_modify_dossier: true | false | unknown
  can_change_runtime_memory: true | false | unknown
  can_create_register_candidate: true | false | unknown
  activation_state: detected | candidate | sandbox_enabled | project_enabled | suspended | rejected
  task_authorization: unauthorized | task_authorized
  allowed_scopes: []
  forbidden_scopes: []
  risk_level: low | medium | high | critical
  approval_required: C0 | C1 | C2 | C3 | C4 | C5
  required_envelope: task_contract_in__candidate_out__evidence_pack_out
```

Rules:

```text
Discovered != passported.
Passported != task_authorized.
Task authorized != approved.
Approved for one scope != approved for another scope.
```

## Relation to Hermes

Hermes may consume V0 in three ways:

```text
read doctrine resources
request validation reports
request candidate skeletons
```

Hermes must not treat V0 as:

```text
a command source
a hidden planner
a provider selector
a scheduler
a permission oracle
a replacement for human approval
```

Expected Hermes envelope:

```text
Task Contract in
-> Hermes execution
-> Result Candidate + Evidence Pack Candidate out
```

## Relation to OpenWebUI

OpenWebUI may display:

```text
MCP server reachable
resources listed
passport status
activation state
task authorization state
risk level
required approval
last preflight
capability gaps
user decision gate
```

OpenWebUI must not display:

```text
reachable = authorized
listed = safe
green = approved
validation report = truth
```

## Relation to Registre Probatoire

V0 must use Registre-oriented wording for retained governance claims.

Allowed:

```text
register candidate
Evidence Pack Candidate
candidate finding
scope-bound note
to verify
blocked pending evidence
```

Forbidden:

```text
canonical memory
memory authority
promote memory
memory approved by MCP
automatic Registre entry
```

Runtime memory remains runtime territory. Pantheon governs Registre Probatoire posture, evidence linkage, scope, approval and final status.

## Minimum refusal posture

V0 must refuse any request whose requested effect includes:

```text
send
write
delete
merge
approve
promote
canonize
install
schedule
route
execute
file externally
notify externally
```

The refusal must return a legitimization path, not a silent failure:

```yaml
refusal_report:
  decision: block
  refused_effect:
  reason:
  required_task_contract:
  required_approval:
  required_evidence:
  next_safe_step:
```

## V0 exit criteria

V0 is acceptable only if:

```text
all tools are side-effect-free;
all external actions are blocked by default;
all outputs are candidates or reports;
all memory language is Registre/Evidence-oriented;
all resources disclose source file, status and authority;
Hermes remains the runtime;
OpenWebUI remains the exposure surface;
Pantheon remains governance.
```

## Explicit non-goals

```text
No runtime.
No workflow engine.
No connector gateway.
No hidden action dispatcher.
No provider routing.
No implicit authorization.
No canonical memory.
No automatic approval.
No external send.
```

## Status summary

```text
Accepted: V0 as read-only resources plus validation-only reports.
Refused: V0 as runtime, host, action tool, approval engine or memory engine.
To verify: mapping to existing mcp-server/ artifacts and OpenWebUI/Hermes adapters.
To arbitrate: final naming and promotion from candidate support doctrine.
Repo state: documented non-implemented for this profile.
```