# Strict MCP evidence validation

Date: 2026-07-13

Status: validation-only trace — implemented read-only validation.
Boundary profile: validation_only_trace.

## Change

- Added one shared fail-closed JSON Schema validator for install,
  observability, backup and exposure evidence.
- Removed truthiness coercion for schema-defined booleans.
- Added deterministic `result: error` / `verdict: invalid` reports.
- Added adversarial tests across direct functions, CLI entry points and MCP
  tools for strings, numbers, nulls, arrays and objects supplied as booleans.
- Aligned the four schemas and the MCP policy-server doctrine with the enforced
  input contract.

## Why

Python treats the non-empty string `"false"` as true. The previous classifiers
could therefore turn malformed evidence into positive `green`, `protected`,
`guarded` or `observable` verdicts even though the governance schemas required
real booleans.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: yes — `mcp-server/`, `schemas/` and one governance
source were changed under issue #361.
Runtime impact: read-only validation becomes fail-closed before classification.
Authority impact: the existing evidence schemas become enforced input contracts
for fields that are present; missing optional evidence remains a capability gap.
Schema/test/CI impact: schema descriptions aligned; regression tests added to the
existing MCP test suite; no workflow change.
External action: none.
Memory behavior: none.

## Local distinctions

```text
missing evidence != malformed evidence
schema-valid != approved
positive verdict != authorization
invalid evidence != capability gap
```
