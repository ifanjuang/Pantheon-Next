# Page-Agent Chrome / Hermes Skill Review

Status: external reference / support review — Page-Agent Chrome extension and Hermes-side skill candidate. Repository state: documented non-implemented.

This document qualifies `alibaba/page-agent` as an external reference for a Chrome-based natural-language browser interaction skill. It does not install Page-Agent, create a Chrome extension, create a Hermes skill, create an MCP server, enable browser automation, authorize website control, send data to a model provider, approve actions, promote memory, or create any runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Source reviewed

External repository:

```text
https://github.com/alibaba/page-agent
```

Observed useful properties:

- in-page JavaScript agent for web interfaces;
- text-based DOM observation rather than screenshot-only control;
- optional Chrome extension for multi-page browser tasks;
- optional MCP server that exposes browser task execution, hub status and stop control;
- browser tools for click, input, select, scroll, wait and user question;
- optional JavaScript execution tool, disabled unless explicitly configured.

## Placement

Accepted:

- Page-Agent as an external reference for a browser interaction capability.
- A Hermes-side candidate skill may talk to Page-Agent MCP when the Chrome extension hub is connected.
- Extension presence may be used as a capability availability signal.
- The capability may support reading a page, explaining visible UI, navigating, pre-filling forms and preparing actions.
- A visible stop control is mandatory for any interactive run.

Refused:

- Page-Agent as Pantheon runtime, approval engine, memory engine, source of truth, evidence authority or professional decision-maker.
- Chrome extension connected = action authorized.
- Browser task completed = governance approved.
- UI click = human validation.
- DOM text = proof.
- Agent memory = canonical memory.
- `execute_javascript` as default capability.
- Any silent send, delete, publish, payment, filing, signature, upload, form submission or external status change.

To verify:

- exact permission set of the Chrome extension before internal use;
- security posture of the local MCP / WebSocket bridge;
- site allowlist and blocked domains;
- redaction behavior before any page content reaches an LLM provider;
- whether Page-Agent history contains sensitive client or project data;
- whether its MCP result can be normalized into `Result Candidate + Evidence Pack Candidate`;
- how stop / timeout / partial completion is surfaced to the user;
- how browser automation logs are stored, redacted and expired.

To arbitrate:

- whether first internal prototype uses upstream Page-Agent directly or a reduced internal fork / wrapper;
- whether Chrome browser control is exposed through OpenWebUI, Pantheon Control, Hermes CLI, or a dedicated cockpit panel;
- whether read-only browser inspection becomes a standard Hermes capability after sandbox testing.

## Capability activation model

The capability has separate states. They must not be collapsed.

```text
extension_installed
  = Chrome extension appears present.

hub_connected
  = Page-Agent hub is connected to local MCP / WebSocket bridge.

skill_available
  = Hermes can technically call the browser-control adapter.

task_authorized
  = a specific Task Contract permits a bounded browser task.

action_approved
  = a human has approved the specific external effect, if any.
```

Safe rule:

```text
Connected means available.
Available does not mean authorized.
Authorized does not mean approved for external effect.
```

## Candidate Hermes skill

Candidate name:

```text
hermes.skill.browser.page_agent
```

Candidate posture:

```yaml
skill_candidate:
  id: hermes.skill.browser.page_agent
  status: candidate
  repo_state: documented_non_implemented
  owner_layer: execution_runtime
  adapter_target: Page-Agent Chrome extension + Page-Agent MCP
  activation_signal:
    - chrome_extension_detected
    - page_agent_hub_connected
    - mcp_get_status_connected_true
  default_mode: read_only
  forbidden_by_default:
    - execute_javascript
    - submit_form
    - send_message
    - delete
    - publish
    - payment
    - sign
    - file_or_deposit
    - upload_without_review
    - external_status_change
  output_envelope:
    in: Task Contract
    out:
      - Result Candidate
      - Evidence Pack Candidate
      - Outcome Observation Candidate
      - Capability Gap, if blocked
```

## Modes

| Mode | Meaning | Default status |
|---|---|---|
| `browser_read` | Read current page, visible fields, buttons, tables, labels and warnings. | allowed under bounded task |
| `browser_explain` | Explain the page or a UI flow without changing it. | allowed under bounded task |
| `browser_prepare` | Prepare a navigation or form-filling plan. | candidate only |
| `browser_prefill` | Fill fields but do not submit. | gated by task scope |
| `browser_assist` | Navigate, click, filter, scroll or select in a non-external-effect path. | gated by task scope |
| `browser_execute_gated` | Submit, send, publish, delete, upload, file or validate. | requires explicit User Decision Gate |

The default mode is `browser_read`. Any escalation must be explicit and visible.

## Minimum task contract fields

Before Hermes may call the Page-Agent skill, the task must state:

```yaml
task_contract_browser_control:
  target_site:
  target_url_or_domain:
  allowed_pages:
  allowed_action_families:
  forbidden_action_families:
  requested_mode:
  data_minimization_rule:
  evidence_expectation:
  approval_ceiling:
  stop_condition:
  external_effect_possible: true | false
  user_gate_required: true | false
```

If the target site, recipient, external effect, page scope or approval ceiling is ambiguous, the adapter returns a Capability Gap instead of improvising.

## Required warning shown to user

Before any non-read-only run, the surface should show a warning equivalent to:

```text
This browser skill can interact with the current page.
It may click, type, select and navigate.
It must not send, publish, delete, file, sign, pay, upload or validate without your explicit approval.
Review the target site, visible action, data used and final effect before continuing.
```

For external-effect actions, the warning must name the exact effect:

```text
External effect detected: [send / submit / delete / publish / upload / file / status change].
The action is blocked until explicit approval.
```

## Return discipline

The adapter return must separate transport, task and governance status:

```yaml
browser_skill_result:
  handoff_delivery_status: not_sent | sent | refused | failed | timeout
  runtime_task_status: not_started | success | partial | failed | blocked | unknown
  governance_result_status: candidate | to_verify | needs_approval | approved | rejected | blocked
  acted: true | false
  external_effect: true | false
  canonical_effect: false
  changed_objects:
  unchanged_objects:
  blocked_items:
  evidence_refs:
  follow_up_needed:
```

A successful browser run is not proof, approval, professional validation, memory promotion or external-action legitimacy.

## Prototype sequence

Recommended order:

```text
P0 — read-only page inspection on allowlisted internal/test pages.
P1 — page explanation and missing-field detection.
P2 — prefill without submit.
P3 — assisted navigation and filtering.
P4 — external-effect preparation with mandatory stop before final click.
P5 — explicitly approved external effect, only after audit and policy review.
```

Do not start at P4/P5.

## Security posture

Minimum safeguards before internal production use:

- allowlist domains;
- denylist dangerous selectors and labels by default: send, submit, validate, delete, pay, sign, publish, upload, file;
- visible stop button;
- per-run timeout;
- no hidden background run;
- no `execute_javascript` by default;
- no raw client secrets in model context;
- redaction before remote LLM call;
- local log with sensitive-data minimization;
- explicit final summary before any external effect;
- separate confirmation for each external action.

## Boundary

This review creates no extension, no runtime, no Hermes skill, no MCP service, no browser control, no OpenWebUI plugin and no external action.

It records the admissible shape of a future browser-control capability:

```text
Browser extension exposes the page.
Hermes skill may execute bounded browser interaction.
Pantheon governs status, scope, evidence, memory and approval.
The human decides.
```
