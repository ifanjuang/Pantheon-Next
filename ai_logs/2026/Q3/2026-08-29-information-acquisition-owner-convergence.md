# Information acquisition owner convergence

Date: 2026-08-29
Issue: #787
Base `main`: `dc2951fd341ecb85d1fcd4db149abef5ae1be95a`
Branch: `codex/converge-information-access-selection`

## Objective

Clarify how a request selects direct source access, documentary retrieval, an operational query, or runtime memory without creating a Pantheon information router, a new schema, a new runtime service, or another governance owner.

## Observed owners

- `REQUEST_LIFECYCLE.md` already owns proportional request activation and explicitly forbids turning it into a hidden router.
- `SOURCE_NEED_AND_REGISTRY.md` already owns source needs, source families and permitted routes.
- `ADAPTERS_AND_BINDINGS.md` already owns the blueprint/adapter boundary and conformance-without-duplication rule.
- `HERMES_EXECUTION_TRACE_SUMMARY.md` already owns bounded technical tool/refusal observations; no new telemetry owner is required.

## Change

- `REQUEST_LIFECYCLE.md`: add one acquisition-selection rule using the least indirect admitted route.
- `SOURCE_NEED_AND_REGISTRY.md`: add operational-owner query as an acquisition route, explicitly not a source family, and generalize the existing acquisition-to-Evidence chain.
- `ADAPTERS_AND_BINDINGS.md`: require tool/query adapters to reuse an existing operational owner instead of creating AI-specific shadow state or duplicated business logic.
- `tests/test_source_document_owner_convergence.py`: extend the existing convergence guard rather than add a new test file.

## Boundary preserved

```text
acquisition route != authority
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
```

No new current-authority Markdown document, schema, capability family, store, router, scheduler, provider path or runtime owner was introduced.

## Validation

Repository diff is intentionally limited to the three existing owners, one existing convergence test, and this required intervention log. Pull-request CI remains the execution validation path for the exact branch head.
