# BFL OpenAI Image Proxy Review

Status: external reference / bonus adapter candidate — documented non-implemented.

This document classifies `beecho01/bfl-openai-image-proxy` as an optional image-generation adapter candidate for the Pantheon tool cartography.

It does not install the proxy.

It does not configure Docker, OpenWebUI, Hermes, Black Forest Labs, API keys or environment variables.

It does not create a Pantheon image runtime, provider router, queue, scheduler, image-generation service, approval engine, memory engine, evidence register or OpenWebUI extension.

```text
OpenWebUI exposes.
The image proxy adapts.
Black Forest Labs executes.
Pantheon Next governs.
```

## Source

```text
repository: https://github.com/beecho01/bfl-openai-image-proxy
review_date: 2026-06-29
upstream_posture: public MIT repository
classification: optional bonus adapter candidate
```

The upstream repository describes a small OpenAI-compatible image-generation proxy for Open WebUI. It exposes an OpenAI-style image endpoint, translates requests to Black Forest Labs FLUX calls, polls BFL until the image is ready, downloads the result and returns an OpenAI-compatible response.

The reviewed scope is text-to-image generation only. Editing, inpainting, outpainting, erasure, deblur, virtual try-on, fine-tune management and FLUX Tools are outside this proxy's stated scope.

## Placement

```text
capability_type: image_generation_adapter
cartography_class: bonus_tool_candidate
exposure_layer: OpenWebUI
adapter_layer: bfl-openai-image-proxy
execution_provider: Black Forest Labs FLUX
validation_layer: Pantheon Next
status: optional_bonus_candidate
repo_state: documented_non_implemented
memory_state: non_canonical
```

This is not a Pantheon capability in the kernel.

It belongs to the adapter / binding layer because it names specific products and exists only to connect one exposure surface to one external image provider.

## Why it is useful

The adapter may be useful when OpenWebUI should expose FLUX image generation without modifying OpenWebUI itself.

Potential use cases:

```text
concept image candidate
architectural mood image candidate
visual exploration candidate
presentation-support image candidate
non-probative illustration candidate
```

Allowed output status:

```text
Result Candidate
Trace Reference
Image Candidate
Evidence Pack Candidate only if separately documented and reviewed
```

An image generated through this path must not become professional evidence by default.

## Governance classification

The placement test gives a split answer.

For simple visual exploration, failure normally produces a bad candidate image, not a canonical truth or external action. Pantheon does not need to execute the image generation.

For professional or client-facing use, the generated image may create misunderstanding, false authority, unapproved delivery, copyright / rights uncertainty, privacy exposure or scope confusion. Pantheon governs the decision around use, status, evidence and transmission.

Therefore:

```text
execution: outside Pantheon
adapter review: Pantheon documentation
output status: candidate by default
client delivery: gated when consequential
memory: none by default
canonization: refused
```

## Required boundaries

The adapter must not be treated as:

```text
Pantheon runtime
provider router
image approval engine
visual truth source
professional validation
Evidence Pack by itself
Registre Probatoire entry
memory mechanism
client-delivery authority
```

A generated image is only a candidate artifact.

It can support discussion, option exploration or visual communication after human review. It cannot validate an architectural solution, material reality, regulatory compliance, site condition, technical feasibility or client approval.

## Deployment posture if used outside Pantheon

Recommended posture for any future deployment, outside this repository:

```text
network: internal Docker network by default
public exposure: disabled unless reverse-proxy and auth are reviewed
proxy auth: required
prompt logging: disabled by default
image persistence: temporary unless explicitly approved
TTL: short by default
API keys: environment-managed outside Pantheon
provider cost: visible to the operator
```

The proxy may be treated as an operational convenience for OpenWebUI. Its existence does not authorize image generation for a Pantheon-governed case.

## Task Contract expectation

For non-consequential visual exploration, a light Task Contract may be enough:

```text
task_family: visual_candidate_generation
requested_effect: internal_state_change
allowed_output: Image Candidate
forbidden_output:
  - proof
  - validated architectural representation
  - client deliverable
  - Registre Probatoire entry
  - memory promotion
```

For client-facing, public-facing or project-decision use, the Task Contract must additionally name:

```text
project_or_case_scope
intended_recipient
visual_status
source_basis
known fictionalization
rights / licensing uncertainty
privacy minimization
approval ceiling
User Decision Gate if delivery or decision support is requested
```

## Evidence Pack Candidate expectation

If an image is used as a reviewable project artifact, the Evidence Pack Candidate should state:

```text
prompt_summary
model_or_provider
generation_date
operator_or_requester
project_or_case_scope
intended_use
visual_status
known fictionalization
source_material_used
private_material_minimized_or_excluded
rights_or_license_note
approval_required_before_delivery
```

This is not proof of the depicted condition.

## Role viewpoints

Suggested review viewpoints when image output may affect a professional file:

| Trigger | Roles |
|---|---|
| simple exploration | ATHENA + APOLLO |
| source-based visual claim | ATHENA + ARGOS + APOLLO |
| client-facing image | THEMIS + APOLLO + ZEUS |
| privacy-sensitive prompt or uploaded reference | ARGOS + THEMIS |
| memory or proof request | ARGOS + THEMIS + ZEUS |

Roles are governance viewpoints, not image agents.

## User Decision Gate trigger

Open a User Decision Gate when the generated image may be sent, published, retained as project memory, used to justify a decision, or interpreted as a faithful representation.

```text
Object of decision:
A generated image candidate may affect external communication, professional interpretation, client expectation, memory or proof status.

Default Zeus posture:
Candidate only. Do not deliver, remember or treat as evidence without explicit human decision and status.

Options:
1. Keep as internal exploration only.
2. Regenerate or revise prompt.
3. Attach limitations and use as presentation-support candidate.
4. Approve narrow delivery with explicit status.
5. Reject as misleading or out of scope.
```

## Cartography entry

```text
Bonus tool candidate:
  id: bfl_openai_image_proxy
  label: BFL OpenAI Image Proxy
  role: OpenWebUI image-generation adapter
  layer: adapter / binding
  executes: no, the provider executes
  governs: no, Pantheon governs status and use
  output: Image Candidate / Result Candidate
  memory: none by default
  authority: external reference only
```

## Decision

```text
Accepted:
  - as optional bonus adapter candidate in the tool cartography
  - as external reference / support review

Refused:
  - as Pantheon core
  - as doctrine kernel
  - as image runtime
  - as provider router
  - as proof source
  - as memory mechanism

To verify:
  - current upstream security posture before deployment
  - Black Forest Labs API terms, cost, data retention and rights posture
  - OpenWebUI image integration behavior in the target deployment

To arbitrate:
  - whether generated images should create only a trace, or also an Image Candidate card in the cockpit
```

## Boundary phrase

```text
The proxy adapts image calls.
The provider generates.
Pantheon governs the status, scope, evidence and delivery.
The human decides what the image is worth.
```
