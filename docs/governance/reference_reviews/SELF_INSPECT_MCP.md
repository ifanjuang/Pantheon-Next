# self-inspect-mcp Reference Review

Status: support review only — deterministic metacognition prompter, rite-operationalization distillation, and forbidden-import record.

Observed date: 2026-06-07

Reviewed sources:

- `https://github.com/ejentum/self-inspect-mcp`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review scope

This review evaluates self-inspect-mcp, an MCP server exposing one tool,
`self_inspect`, that returns a "metathought" — a clarifying question that
redirects attention to assumptions and reasoning rather than an answer.

This document does not approve installation.

This document does not add a dependency.

This document does not create a Pantheon runtime, MCP server, tool runtime,
self-correction loop, approval engine or automatic memory promotion engine.

## External project summary

self-inspect targets recurring "attention failures":

```text
commitment to the first interpretation
unnamed assumptions
goal drift
premature satisfaction with a plausible answer
unwarranted confidence
```

Mechanism:

```text
one tool: self_inspect
deterministic routing over a CSV (~50 lenses, 137 questions)
no LLM, no embeddings — heuristic scoring selects the highest lens
returns a metathought (a question) or a universal default
drift-tested: the generated code must byte-match the CSV spec
keyless, MIT, JavaScript, very early (5 stars, no releases)
```

Founding premise, quoted: *"acknowledging a trap is not escaping it"* — an agent
cannot reliably self-correct using its own reasoning.

## Why this is doctrinally aligned

That founding premise is Pantheon's own thesis. It is the reason Pantheon
externalizes truth into evidence, approval and the human rather than trusting an
agent's confidence. The project also maps almost one-to-one onto existing rites:

| self-inspect attention failure | Pantheon rite / doctrine |
|---|---|
| unnamed assumptions | `rites/PREMISSES_CACHEES.md` |
| premature satisfaction / unwarranted confidence | `rites/AUTOCRITIQUE_CONTRADICTOIRE.md` |
| goal drift | MÈTIS / the cap (`REQUEST_LIFECYCLE.md`) |
| confidence without source agreement | `rites/CONCORDANCE_DES_SOURCES.md` |
| choosing the right question | `rites/RITE_SELECTION_MATRIX.md` |

## Technical characterization

self-inspect-mcp should be classified as:

```text
deterministic_metacognition_prompter
question_catalogue_server
rite_operationalization_pattern
external_runtime_candidate
```

It is not:

```text
Pantheon governance
a Pantheon runtime
an approval
a truth or certainty authority
a self-correction loop
```

A metathought is a surfaced question for governed attention.

It is not a verdict, an approval or proof.

## Layer mapping

| Layer | Classification |
|---|---|
| Pantheon Next | owns the rite catalogue and the signal-to-question spec; governs attention, not execution |
| Hermes Agent | optional caller that surfaces a metathought during a task under Task Contract |
| self-inspect-mcp | external deterministic question prompter (pattern source) |
| OpenWebUI | cockpit exposure of the surfaced question and the rite status |

## Recommended classification

```text
name: self_inspect_mcp
classification: External Deterministic Metacognition Prompter
pantheon_status: reference_review_only
hermes_status: optional_metacognition_prompt_candidate
openwebui_status: surfaced_question_and_rite_status_surface_candidate
memory_status: non_canonical
approval_status: not_approved_for_installation
runtime_status: external_only
```

## Valuable patterns to distill

```text
a metathought is a QUESTION, never an answer or a verdict — pure "govern, not execute"
deterministic, no-LLM selection — the opposite of judge-as-authority
a compact catalogue of (signal -> question) usable as mode_light before a full rite
drift verification: the served catalogue must byte-match an owned spec
a universal default question when no signal matches
```

The strongest takeaway: it shows how to move the rites from prose to a
deterministic, drift-verified `signal -> question` catalogue that Pantheon owns
as spec and an external surface merely serves. This is captured as a candidate
in `rites/RITE_TRIGGER_CATALOGUE.md`.

## Forbidden imports

Pantheon must not import:

```text
self-inspect-mcp as an internal Pantheon runtime or MCP server
the metathought as an automatic self-correction loop (self-learning is rejected)
the metathought as an approval, a gate that blocks by itself, or proof
its CSV as Canonical Memory
any path where surfacing a question auto-triggers a rite or chains rites
```

This respects the rite rules: a signal may suggest a question; it does not
trigger a rite; ZEUS decides; anti-chaining and rite budget still apply.

## Decision

```text
Adopt the deterministic metathought pattern to operationalize the rites.
Do not adopt the tool into Pantheon; it is too young to depend on.
Keep the catalogue as Pantheon-owned spec; let an external surface (Hermès or a
  read-only MCP resource per MCP_POLICY_SERVER_CANDIDATE) serve it.
Represent every surfaced question as attention support, never as approval.
Reject any autonomous self-correction loop or auto-triggered rite chain.
```

## Final rule

```text
The catalogue may ask the question.
Hermès may surface it under contract.
OpenWebUI may show it.
Pantheon owns which question matters.
The human decides what to do with the answer.
```
