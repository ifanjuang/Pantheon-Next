# AI log — landing stack rewrite attempt

Date: 2026-06-04

## Scope

Requested option C: revise the landing page, comment PR #54, and add an AI log.

The intended landing update clarified:

- the sharper value proposition: status, proof, decision and memory;
- the concrete local / NAS deployment posture;
- mandatory current bindings: OpenWebUI as exposure surface and Hermes Agent as execution runtime;
- optional components: Langfuse, Langflow, LangGraph and provenance graph;
- access from browser, mobile and message-like channels when configured;
- the non-runtime boundary: Pantheon governs, it does not execute.

## Doctrine consulted

- docs/governance/STATUS.md
- docs/governance/MODULAR_DOMAIN_REORIENTATION.md
- docs/governance/CAPABILITY_PLACEMENT.md
- docs/governance/DOMAIN_PACK_SPEC.md
- docs/governance/PRODUCT_DIFFERENTIATION.md

## External docs checked

- Open WebUI documentation for self-hosting, providers and agents.
- Open WebUI Hermes Agent connection documentation.
- Langfuse documentation for observability and tracing.
- Langflow documentation for visual workflow prototyping.
- LangGraph documentation for durable, stateful, human-in-the-loop execution.

## Result

The first two full HTML replacement attempts for `docs/index.html` were blocked by the GitHub connector safety controls before writing. No landing page change was committed by those attempts.

Repo state: partial.

Implementation state: documented attempt only; no runtime, schema, test, operations, platform, Docker or environment change.
