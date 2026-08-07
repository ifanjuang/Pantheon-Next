# OpenTakeoff drawing/Revit adapter distillation

Date: 2026-08-07

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: `docs/domain-packs/architecture/DRAWING_TAKEOFF_LOCAL_ADAPTER.md` as the candidate local PDF/drawing takeoff binding specialization under the APU adapter contract.
- Added: `revit-plugin/docs/ENGINEERING_CONFORMANCE.md` as a supporting Revit implementation note for the single operation registry, human/agent parity, typed outcomes, provenance, conformance and fixture-corpus expectations.
- Updated: `docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md` to name Revit and drawing-takeoff as sibling source-binding specializations.
- Updated: `revit-plugin/README.md` to expose the new engineering-conformance note in the reference skeleton contract map.
- Updated: `docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md` to classify the drawing-takeoff binding as candidate support doctrine, documented non-implemented.
- Updated: `docs/governance/reference_reviews/README.md` with the strategic memory of the OpenTakeoff review and the distillation targets.
- Removed: none.

## Why

`Kentucky-ai/opentakeoff` was reviewed as a current external reference for local agent-driven PDF takeoff. The useful result was not to import its tool registry or make it a Revit dependency. The review showed two separate opportunities that needed durable placement before planning:

1. a replaceable, full-local drawing/takeoff source binding beside Revit and IFC, feeding the existing APU candidate/evidence chokepoint;
2. generic engineering patterns that strengthen the future Revit adapter without changing its governance authority.

The most relevant distilled patterns were a shared deterministic implementation behind human and agent surfaces, a closed operation registry, explicit `withheld`/refusal results, centralized provenance, preservation of original machine proposals after human correction, deterministic correction rules, parity/conformance tests, a fixed benchmark corpus and fail-closed file overwrite behavior.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none; no OpenTakeoff package, MCP server, Revit add-in, Host Agent, workflow or model was installed or executed.
Authority impact: adds one candidate source-adapter specialization and indexes it; `REVIT_LOCAL_ADAPTER.md` remains the Revit authority and `PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md` remains the generic APU adapter chokepoint.
Schema/test/CI impact: none; no protected schema/test/CI path changed.
External action: GitHub documentation branch only; no model, file publication, email, deployment or third-party runtime action.
Memory behavior: none; no capture corpus or correction record was admitted to Pantheon memory.

## Local distinctions

```text
reviewed external repo != adopted dependency
distilled pattern != imported runtime
installed != approved
MCP tool visible != Pantheon capability admitted
PDF quantity candidate != accepted project quantity
engine reviewed flag != Pantheon Decision
human/agent parity != equal authorization
transaction success != accepted result
runtime success != Evidence
```

## Source review posture

The OpenTakeoff review observed a local MCP/takeoff implementation with shared human/agent geometry, typed tool contracts, explicit provenance, deterministic rule re-application, conformance/parity tests, a scored geometry corpus, safe export overwrite checks, an optional local AI adapter and local correction-data capture.

At review time the upstream MCP package advertised `0.9.38`. That value is an audit observation only. The distillation deliberately does not pin or adopt that version.

## Decisions recorded

```text
OpenTakeoff placement -> sibling local drawing/takeoff adapter, not Revit plugin content
production posture -> exact offline package only after separate adoption review
fork posture -> no default fork; prefer thin Pantheon binding until a fundamental boundary requires one
Revit reuse -> generic engineering patterns only, no code/runtime dependency
source identity -> OpenTakeoff shape/tag/session identities remain source-local
cross-source match -> candidate under APU review, never automatic stable identity
```

## Still not done

```text
no package installation
no offline bundle or SBOM
no metric acceptance run
no real French plan benchmark
no Revit 2027 implementation
no Revit fixture corpus
no Capability Slot registry entry
no Hermes workflow
no pantheon-mvp persistence change
no Project Anatomy runtime projection
no Evidence admission
no production adoption decision
```
