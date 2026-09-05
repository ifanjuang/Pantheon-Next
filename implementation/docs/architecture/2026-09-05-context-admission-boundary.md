# Context Admission boundary — Pantheon / Hermes

Date: 2026-09-05  
Status: implemented candidate slice — bounded Pantheon-to-Hermes model-context transport

## Objective

Generalize prompt-injection protection one level above documents without creating
a parallel security framework.

The boundary is:

```text
model-bound context item
-> Context Admission
-> data-only transport
-> Hermes reasoning
```

It applies to context because of what the content *is*, not because a particular
tool happened to transport it.

The first implemented slice covers the existing Pantheon Context Bridge. It does
not replace Source Intake, Project Document admission, Evidence, approvals,
execution guards, or memory governance.

## Repository state verified before change

Pantheon work started from:

```text
ifanjuang/Pantheon-Next main
fd39f1d377d57eb2dc03060c0f93b21763b745b7
```

No open Pantheon PR or issue was found implementing a Context Admission or
prompt-injection boundary in parallel.

The active Pantheon distribution remains pinned to Hermes Agent `0.21.0`.

Upstream Hermes was checked both at the qualified `v2026.8.31` release and at
current `main`. The qualified release already provides:

- `tools.threat_patterns.scan_for_threats(..., scope="context")`;
- context-file scanning before system-prompt inclusion;
- `<untrusted_tool_result>` wrapping for attacker-controllable web/browser/MCP
  tool outputs;
- advisory risk findings for those tool results.

Current Hermes `main` was also rechecked and continues the same direction.

## Existing authorities reused

The implementation deliberately keeps current owners separate.

### Source Intake

`source_intake.py` preserves a Source and links it to Project scope.

```text
Source preserved != content trusted
```

It does not become a prompt-security owner.

### Project Document admission

`project_document_admission.py` reconciles a preserved Source with a professional
Document revision.

```text
professional revision admitted != model instructions authorized
```

It remains unchanged.

### Context Packs and scoped Hermes reads

`CONTEXT_PACKS.md`, `hermes_scoped_context.py`, `hermes_active_context.py` and the
bounded Hermes execution API already own scope and exact entity admission.

```text
Context Pack inclusion != Evidence
read access != write authority
scope admission != instruction authority
```

### Hermes execution security

Hermes keeps command approval, command guards, plugin/skill security and its
native threat-pattern engine.

Pantheon does not duplicate those engines.

## Observed gap

The Pantheon Context Bridge exposes two native Hermes tools:

```text
pantheon_context_manifest
pantheon_context_entity
```

Their outputs may contain source-derived Markdown, Information text, Knowledge
text, names, descriptions, notes or other model-readable strings.

Hermes `0.21.0` automatically applies its untrusted-result transport to:

```text
web_search
web_extract
browser_*
mcp_*
```

The Pantheon plugin tool names are not in that native name-based set.

Therefore a governed Pantheon read was scope-safe but could reach the model
without the same indirect-prompt-injection framing.

The problem is not professional document admission. It is the final
model-context transport boundary.

## Context Admission v1 contract

The first contract is intentionally small:

```text
contract = pantheon.context-admission.v1
content_role = data
instruction_authority = none
transport_class = untrusted_data
scanner_authority = advisory_only
scan_status = no_findings | findings | unavailable | error
disposition = admitted_untrusted | requires_review
```

Invariant:

```text
scanner clean != trusted
retrieved/context data != instruction
Context Pack inclusion != Evidence
successful tool read != authorization
```

No path in this contract can emit instruction authority.

## Runtime implementation

The existing Pantheon Context Bridge now composes Context Admission directly
into both registered Hermes tool handlers.

The handler boundary:

1. acts only on `pantheon_context_manifest` and `pantheon_context_entity`;
2. scans the raw model-bound result with Hermes'
   `tools.threat_patterns.scan_for_threats(scope="context")`;
3. neutralizes forged admission/delimiter tokens in source content;
4. wraps the complete result in the same semantic
   `<untrusted_tool_result>` boundary used by Hermes;
5. labels the result explicitly as data with `instruction_authority="none"`;
6. marks a clean scan `admitted_untrusted`, never trusted;
7. marks findings, scanner failure or scanner absence `requires_review`;
8. does not redact or mutate the preserved source or Pantheon owner record.

The scanner is defense in depth. The data-only transport boundary is the primary
invariant.

## Why the registered-handler boundary

Hermes `0.21.0` exposes `transform_tool_result`, but that transform surface uses a
first-valid-replacement rule. A security invariant should not depend on plugin
registration order or on whether another transform already returned a string.

The Pantheon plugin therefore wraps its own reviewed tool handlers before
registration. The result leaves the Pantheon plugin already framed as data-only
untrusted context. Later Hermes transforms may observe that result, but the
Pantheon boundary itself cannot be skipped by an earlier transform callback.

This is a better convergence point than:

- creating a second document ingestion pipeline;
- duplicating all Hermes threat regexes;
- modifying professional Document admission;
- teaching each Pantheon entity type its own prompt-injection behavior;
- wrapping data inside the Pantheon database projection itself.

The source remains unchanged. Only the model-bound transport representation is
framed.

## Failure posture

If Hermes' threat scanner is unavailable or raises:

```text
scan_status = unavailable | error
disposition = requires_review
instruction_authority = none
```

The boundary therefore does not silently upgrade trust because a scanner failed.

If the scanner finds an attack pattern:

```text
scan_status = findings
disposition = requires_review
instruction_authority = none
```

The content remains analyzable as quoted/source material inside the untrusted
boundary. A finding does not become a truth verdict about the document.

## Non-goals

This slice does not:

- prove that a source is authentic;
- decide whether a document is Evidence;
- reject a professional document because it contains imperative language;
- authorize or deny a Hermes tool effect;
- replace OS/container isolation;
- replace Hermes approval/Tirith/command guards;
- promote memory;
- create a new persistent trust database;
- create a generic SecurityManager;
- add Prompt Guard 2 or another model classifier before calibration demonstrates
  that the deterministic + semantic-boundary layer is insufficient.

## Remaining gap

This slice closes the Pantheon Context Bridge path.

It does **not** yet give arbitrary local files read directly by Hermes a
provenance-aware classification. Hermes already scans context files and wraps
several attacker-controllable tool families, but a future upstream improvement
could expose a public tool-output trust declaration so plugins and file readers
can request Hermes' native untrusted transport without duplicating delimiter
semantics.

That upstream/general-local-file question remains separate from this bounded
Pantheon implementation.

## Completion criteria

This slice is complete when:

- both Pantheon context tools register protected model-bound handlers;
- the transform always emits `instruction_authority=none`;
- clean scan does not imply trust;
- findings and scanner failure require review;
- forged delimiters are neutralized;
- unrelated Hermes tools are untouched;
- the pinned distribution digest includes the transform;
- focused tests cover these invariants.

The implementation remains default-off because the Pantheon Hermes distribution
itself remains candidate/default-off.
