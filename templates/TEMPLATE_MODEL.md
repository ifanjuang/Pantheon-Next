# Template Model

Status: support template discipline / documented non-implemented.

This document defines the common structure for Pantheon / Hermes prompt and execution templates.

It is not a runtime configuration.
It does not install, execute, deploy, approve, send, schedule, route providers, promote memory or create an autonomous workflow.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A template is a reusable execution contract.

It frames how an assistant, external runtime, cockpit surface or human reviewer should read, qualify, transform, compare, draft or return information.

A template may standardize:

- role framing;
- required inputs;
- source hierarchy;
- allowed outputs;
- forbidden outputs;
- uncertainty discipline;
- evidence expectations;
- human validation points;
- final answer or return format.

A template must not be treated as implementation.

## Authority boundary

Templates instantiate existing doctrine.
They do not create doctrine by themselves.

A template must remain compatible with:

- repository status rules;
- authority classes;
- task contracts;
- evidence rules;
- approval rules;
- memory rules;
- external action boundaries;
- runtime placement boundaries.

If a template conflicts with active doctrine, the template is wrong.

## Template anatomy

Each reusable template should define:

```text
name
status
owner_layer
surface
intent
target_user
phase_or_context
required_inputs
optional_inputs
source_hierarchy
operating_rules
forbidden_behaviors
output_structure
uncertainty_handling
evidence_requirements
approval_or_human_validation_points
memory_behavior
external_action_behavior
examples_or_notes
```

## Required distinctions

Every template that handles consequential professional work must distinguish:

```text
fact
assumption
interpretation
recommendation
uncertainty
missing_information
decision_required
```

A template must not convert an assumption into a fact.
A template must not hide uncertainty.
A template must not cite, imply or fabricate a source that was not actually consulted.

## Source hierarchy

A template should explicitly state the source hierarchy it expects.

Default order for professional project work:

```text
1. validated project documents
2. latest indexed drawings or written pieces
3. contract / mission scope
4. applicable regulations or professional references
5. meeting minutes and correspondence
6. domain knowledge
7. model inference
```

Model inference is never evidence by itself.

## Output status

Template output should be labelled when appropriate:

```text
candidate
partial / to verify
documented non-implemented
ready for human review
requires source check
requires approval
refused / out of scope
```

## Forbidden pattern

A template must not:

- claim implementation;
- claim installation;
- self-approve;
- promote memory;
- authorize an external action;
- create a hidden workflow;
- create a scheduler or queue;
- turn a runtime success into evidence;
- treat a tool response as validated truth;
- bypass a human decision gate;
- import raw prompt leaks, proprietary prompts or unqualified third-party instructions into Pantheon doctrine.

## External inspiration rule

External prompt collections, tool prompts, leaked system prompts, public examples and third-party assistants may inspire abstract structure only.

Allowed:

- prompt architecture patterns;
- input / output contract patterns;
- uncertainty discipline;
- source hierarchy patterns;
- refusal and stop-condition patterns;
- trace and evidence framing patterns.

Forbidden:

- raw ingestion;
- verbatim reuse;
- vectorization as knowledge;
- skill derivation from proprietary prompts;
- dependency adoption;
- automatic update;
- treating external prompts as authority.

## Layer placement

```text
Pantheon governs template status, boundary and consequence.
Hermes may execute from a template under Task Contract.
OpenWebUI may expose a template form, card or prompt surface.
The human validates consequential output.
```

A template is useful only when its boundary is visible.
