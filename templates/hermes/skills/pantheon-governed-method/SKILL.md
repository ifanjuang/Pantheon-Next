---
name: pantheon-governed-method
description: "Use for non-trivial governed work that must be framed, sourced, composed, tested and assigned an explicit readiness status. Coordinates existing Hermes skills and read-only Pantheon policy tools proportionately; it is not a workflow engine or a domain-specific procedure."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  governed_by: docs/governance/GOVERNED_METHOD_STANDARD.md
  policy_contract: mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md
  related_skills: [pantheon-request-intake, pantheon-activity-projection]
  upstream: "agentskills.io SKILL.md standard; exact Hermes runtime compatibility must be qualified before admission"
---

# Pantheon governed method

General-purpose coordination adapter for non-trivial professional work. It
supports any bounded candidate output or action without encoding the object's
business label or creating an object-specific workflow.

```text
method movement != runtime stage
viewpoint != autonomous agent
policy guidance != execution
candidate complete != approved or transmitted
technical receipt != Evidence
```

## When to use

Use when the request materially depends on scope, sources, professional risk,
several operations, a produced artifact, a delivery boundary or an observable
acceptance criterion. Keep trivial questions and harmless transformations quiet.

Never select a procedure from a client, project, object or deliverable label. Select only
from material conditions observed in the current request and task state.

## Seven movements

Apply the smallest useful form of the governed method:

```text
1. Frame / Cadrer
2. Admit / Admettre
3. Qualify / Qualifier
4. Compose / Composer
5. Produce Candidate / Produire candidat
6. Test / Éprouver
7. Status / Statuer
```

These are movements, not a mandatory linear pipeline. Skip an empty movement,
combine adjacent movements when that stays legible, and loop back only when a
material source, contradiction, scope, risk or completion condition changes.

### 1. Frame

Preserve the requested effect, audience, scope and output. Use
`pantheon-request-intake` to emit only supported conditions, coordination
relations and observable completion requirements.

### 2. Admit

Inventory what is actually available, referenced but absent, stale, partial or
contradictory. User-provided material, memory recall and retrieved results enter
as bounded working material, never as truth or Evidence by default.

### 3. Qualify

For a consequential boundary, call the exposed read-only Pantheon policy tools
instead of reproducing policy locally:

```text
classify_request
evaluate_preflight
prepare_task_contract_skeleton
prepare_evidence_pack_skeleton
plan_context_pack
validate_context_pack
```

Call only the subset justified by the returned handling. Candidate preparation
does not execute work, and validation does not authorize an effect.

Hermes currently represents deferred MCP functions as local tools. Invoke only
one such MCP function per `tool_call`; do not batch several local MCP calls in a
single call envelope. Sequence dependent policy calls. This runtime constraint
overrides the general preference to batch independent reads.

When professional factual claims require workspace sources, complete the
source-preflight receipt described below before presenting them as supported.

For Pantheon doctrine, prefer the compact progressive route:

```text
route_governed_request(request YAML or plain request text, source_limit <= 3)
-> read_doctrine(exact selected key)
-> source-preflight receipt
```

The route operation combines request classification and doctrine shortlisting
so Hermes does not batch dependent deferred MCP functions. Do not call
`classify_request`, `find_relevant_sources` or `list_sources` on the normal
answer path. Those lower-level and catalog primitives are reserved for explicit
administration, compatibility or diagnosis outside the governed runtime
profile. A shortlist is not a source consultation: only `read_doctrine` opens
the selected doctrine source.

Hermes may pass the user's request as `request_text` when a structured candidate
has not already been prepared. Do not ask the user to write YAML solely to use
this tool; the MCP adapter converts plain text into a bounded candidate.

### 4. Compose

Select the smallest set of existing capabilities. A normal task has at most:

```text
one primary method;
one guardrail method;
one verification method.
```

Examples of condition-driven selection:

| Material condition | Typical composition |
|---|---|
| source-dependent claim | source admission + assertion/probative review |
| candidate crosses an audience or system boundary | productive method + external commitment guard |
| derived quantitative claim | applicable source route + quantitative reconciliation |
| structured output must be produced | admitted production skill + output verification |
| several independent checks | parallel retrieval/checks + one synthesis |

These are selection patterns, not fixed workflows. Load specialist skills only
when their exact trigger is present. Availability is neither use nor authority.

### 5. Produce Candidate

Hermes executes admitted search, reading, comparison, calculation, drafting and
artifact production through existing skills and tools. Preserve provenance,
assumptions, contradictions and the distinction between sourced and derived
content.

### 6. Test

Test against the completion requirements returned by policy or explicitly
stated by the task. Use observable checks: source opened, components reconciled,
artifact rendered, requested sections present, tests passed, wording reviewed or
external gate opened. Do not use `looks correct` as a test.

If a material condition changes, return to Frame/Qualify. Do not rerun policy
after every routine tool call.

### 7. Status

First name the bounded result whose readiness is being judged. Close each
materially shown responsibility with one of the existing readiness decisions:

```text
ready
ready_with_limits
needs_revision
needs_user_input
blocked
```

Apply the decisions consistently:

| Decision | Meaning for the requested result |
|---|---|
| `ready` | produced and observably checked for its declared internal use |
| `ready_with_limits` | produced and usable for that use with bounded explicit limits |
| `needs_revision` | produced but an observed defect prevents declared use |
| `needs_user_input` | cannot be produced without a decision or datum unavailable to tools |
| `blocked` | cannot be produced because a required technical, access or authority dependency is unavailable |

Attach the smallest useful result, evidence/source references, limitations and
next safe action. Judge the result the user requested, not whether the method
itself ran successfully. A method explanation may be `ready_with_limits` while
the absent professional result is `needs_user_input`; name which one is being
reported. This is readiness for the bounded candidate, not whole-task approval.
A draft may be `ready` for internal review while remaining blocked for external
transmission.

## Source-preflight receipt

For a material professional factual answer, record a compact task-local receipt
using `templates/hermes/returns/source_preflight_receipt.template.yaml`.

The receipt must identify:

- each source family required by the admitted contextual adapter;
- the actual binding/tool used for each consultation;
- the exact source reference opened and, when useful, its inspected locator;
- observed source metadata and limitations without invented values;
- whether memory supplied only an unconfirmed lead;
- the Context Pack validation result when a Context Pack was required;
- the completion result for each required source family.
- an observed runtime trace reference when the active surface exposes one.

A required family is not complete when only search snippets, conversation
memory, model recall or a guessed filename were observed. If the exact source
cannot be opened, use `needs_user_input` or `blocked`; do not fabricate a
supported answer.

```text
memory lead != source consultation
search hit != exact source opened
receipt complete != source true
Context Pack valid != Evidence or approval
model-declared tool use != observed runtime trace
```

## Presentation

Use `pantheon-activity-projection` for non-trivial work. Show only materially
established Role viewpoints, actual tools and meaningful milestones. Never
expose private chain-of-thought or invent role theatre.

## Final invariant

```text
Classify by material conditions, not by object names.
Compose existing capabilities proportionately.
Produce and test an explicitly bounded candidate.
State readiness, evidence limits and the next safe action.
Pantheon governs; Hermes executes; the human decides consequential effects.
```
