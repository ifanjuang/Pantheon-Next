# Execution Minimalism

Status: active support doctrine — reliability-first execution growth and anti-overengineering rules.

This document defines how Pantheon Next should prevent agentic overengineering when integrating Hermes Agent, OpenWebUI, Langflow, LangGraph, Langfuse, GraphRAG or future external capabilities.

It does not implement workflows, agents, skills, tools, schedulers, queues, provider routers, OpenWebUI Functions, Hermes skills, Langflow flows, LangGraph runtimes or observability backends.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core principle

```text
Boring reliability before expanded authority.
```

Use the simplest viable architecture that preserves evidence, status and human decision.

An agentic loop is not the default.

It is justified only when the task cannot be reliably handled by deterministic code, a bounded LLM interpretation node or a narrow skill.

## Architecture selection

| Task property | Preferred pattern | Pantheon placement |
|---|---|---|
| Known solution | Deterministic workflow with LLM interpretation nodes only where needed | Langflow candidate, script candidate or Hermes skill candidate |
| Dynamic exploration | ReAct-style Hermes execution with strict stop conditions | Hermes under Task Contract |
| High-stakes output | Reflection / review with explicit rubric | Pantheon evidence and approval doctrine, Hermes review candidate |
| Massive scale | Deterministic sharding and routing before multi-agent decomposition | External runtime candidate only |
| Long-running work | Checkpointed execution, not open-ended autonomy | Hermes / LangGraph candidate under bridge contract |
| Human conflict | User Decision Gate | OpenWebUI exposes, Pantheon governs |

## Minimalism rules

1. Stabilize one real workflow before adding profiles, skills, tools or external runtimes.
2. Use deterministic execution before agentic execution.
3. Use LLM calls as interpretation nodes before using agent loops.
4. Use ReAct only when exploration is necessary.
5. Use Reflection only with an explicit review rubric.
6. Use multi-agent decomposition only when task scale, context size or permission boundaries require it.
7. Stop at approved checkpoints.
8. Do not run beyond approved scope.
9. Proposal is free; authority is controlled; execution is logged.
10. A returned candidate is not a validated output.

## Workflow growth discipline

Start with:

```text
one real workflow
one Task Contract shape
one Context Pack shape
one Hermes profile or skill candidate
one Evidence Pack Candidate return
one OpenWebUI display surface
one human approval path
```

Do not add a profile, skill, tool, flow, graph, dashboard or scheduler merely because the platform supports it.

A new capability must justify at least one of:

```text
different domain expertise
different permission level
different tool boundary
different memory boundary
different model requirement
different user or access boundary
different evidence requirement
different runtime requirement
```

## Checkpointed autonomy

Prefer:

```text
Work through the next approved checkpoint.
Update the run manifest.
Report status.
Continue only if the next step is already authorized and in scope.
```

Reject:

```text
Keep going until finished.
Use all available tools.
Solve the whole project autonomously.
Improve your own governance silently.
```

## Checklist Manifest posture

A manifest may preserve durable run status without bloating chat context.

It may track:

```text
task_contract_id
context_pack_id
last_completed
active_checkpoint
next_authorized_step
blockers
evidence_status
approval_status
memory_status
last_updated_at
timezone
```

A manifest is not a scheduler, queue, workflow runtime, approval engine or memory authority.

## Model hierarchy discipline

Model selection should follow output status and risk, not only cost.

```text
strongest reliable model: judgment, critique, high-stakes candidate review
cheaper cloud model: classification, summarization, first draft, bulk triage
local model: private, simple, offline or low-stakes tasks where practical
```

Provider or model routing must not become Pantheon runtime responsibility.

## Output status discipline

Every non-trivial output should preserve status:

```text
proposal
draft
result_candidate
evidence_candidate
evidence_pack_candidate
patch_candidate
memory_candidate
capability_gap
risk_escalation
approved_deliverable
canonical_memory
rejected_candidate
```

The architecture that produced an output does not determine its governance status.

Pantheon does.

## Autonomy and restraint

Govern the destination and the cliffs, not every step of the path. Dictating each
micro-step wastes the AI and bloats doctrine. The default is autonomy; control attaches
only where the consequence earns it.

### Default autonomy, gate by consequence

Apply the placement test to autonomy itself. What decides the timing of control is
reversibility, not importance alone.

```text
low / semi-consequential AND reversible
  -> the AI acts, logs, and notifies after; the human corrects via the Review Queue.
     (drafting, organizing, searching, retrieving, summarizing, proposing,
      reclassifying, internal record edits that are logged and reversible)

irreversible or hard-cliff
  -> ask before; or never automatic.
     (false truth stated as fact, unapproved external effect, sending/filing/signing,
      canonical memory promotion, scope leakage, a definitive legal/contractual claim)
```

Act-then-notify is the normal mode, because everything reversible is caught by the
append-only log and the Review Queue. Ask-before is reserved for the cliffs.

```text
Reversible and logged -> act, then review.
Irreversible or external -> review, then act.
```

### Govern outcomes, not procedures

A contract states the WHAT (a sourced result; ask if a consequential value is
uncertain), not the HOW (the exact loop, every status). Step-by-step procedures in
other documents are defaults the AI may adapt, not mandates. The AI chooses its path
and its topology; governance only checks that the proof chain and the boundaries hold.

This is why other documents may stay light: they govern the boundary and trust the
path. A workflow document that spells out every step is over-specified; it should state
what must be true of the result, and leave the method to the runtime.

### Autonomy is earned

Autonomy is not all-or-nothing. A capability climbs the lifecycle as it proves boring
reliability (`WORKFLOW_LIFECYCLE.md`): tighter at first, looser once trustworthy.

```text
new capability         -> narrow autonomy, more notification
proven capability      -> wider autonomy, lighter notification
a capability that errs  -> autonomy is stepped back, not abandoned
```

### Reusable outputs

An autonomous capability's result is a governed, scoped record — produced once, reused
by other requests. Retrieval is the clearest case: a fact fetched for one request is
saved with its source and scope and serves the next request, instead of being
re-fetched or re-asked.

```text
A capability returns a reusable result, not a throwaway answer.
A retrieved fact is saved once (with source, scope, date) and reused within its scope.
Past its review date it returns as to_reconfirm, not silently trusted.
Reuse stays scoped: a dossier fact does not become global; a general fact is not narrowed.
```

This both speeds the system and keeps it minimal: work is not repeated, and a single
retrieval skill serves many request types (`CORE_RECORDS_MODEL.md`, `MEMORY.md`).

### Artifacts scale with stakes

Not every task needs a Task Contract, an Evidence Pack and a gate. A trivial task is
just done. Reserve the full envelope for consequential work. Ceremony is proportional
to consequence, never uniform.

```text
trivial       -> do it, light log
consequential -> the full contract / evidence / gate
```

## Final rule

```text
Use less agentic architecture than the tool makes possible.
Add authority only after reliability is boring.
Preserve status, evidence, checkpoint and human decision.
```