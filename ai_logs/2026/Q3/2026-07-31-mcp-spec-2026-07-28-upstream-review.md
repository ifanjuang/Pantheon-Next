# 2026-07-31 — MCP specification 2026-07-28 upstream review

Status: validation-only trace (external reference review).
Boundary profile: validation_only_trace.

## Trigger

Review of the upstream release
`https://blog.modelcontextprotocol.io/posts/2026-07-28/` (Model Context Protocol
specification revision `2026-07-28`) against the bounded `mcp-server/` module.

## Repository recheck (before writing)

Read the current implementation and the governance home for external reviews:

```text
mcp-server/pantheon_mcp/server.py        stdio transport via MCPServer (mcp>=2,<3)
mcp-server/pantheon_mcp/http_api.py      SEPARATE bounded REST adapter, static bearer key
mcp-server/pantheon_mcp/http_middleware.py   correlation-only request_id; no session state
mcp-server/pyproject.toml                version 0.1.64, mcp>=2,<3
docs/governance/reference_reviews/       established distill-before-adopt home
docs/governance/WATCHLIST.md             watch-record format
docs/governance/authority/EXTERNAL_REFERENCES_AUTHORITY_INDEX.md   grouped-row coverage
```

## Change

Documentation only. No runtime, dependency, schema or pin change.

```text
docs/governance/reference_reviews/MCP_SPEC_2026_07_28_REVIEW.md   new one-shot review
```

The review classifies each headline change of the release on the governed axes:

```text
stateless core        SDK surface migrated in PR #495; no Pantheon state migrated
MRTR / input_required not applicable — already compliant; forbidden as an exec loop
header routing        to verify at gateway/SDK; no core change
cacheable lists       optional inventory-only enhancement; verdicts never cacheable
auth hardening (9207) not applicable to the bearer-key adapter; watch if OAuth added
Tasks extension       FORBIDDEN import (recreates scheduler / mandatory queue)
Roots/Sampling/Logging unused; sampling/routing prohibition stands; verify logging
HTTP+SSE deprecation  not an MCP transport here; no offramp needed
Python mcp SDK        migrated to mcp>=2,<3 in PR #495; full suite passed
```

## Distillates recorded (not yet distilled into target doctrine)

```text
1. Three naming-collision clarifications:
     MCP Tasks        != Pantheon Task Contract
     OAuth issuer     != Pantheon decision issuer (HMAC signer)
     MCP session id   != Context-Pack ID / x-pantheon-request-id
2. "Cacheable inventory, never cacheable verdict" caching boundary rule.
3. "MRTR is not a consultation loop" and "Tasks extension is Hermes-side only".
```

## Boundary

```text
spec_released != spec_adopted
deprecated_upstream != in_use_here
formalized_extension != approved_import
SDK_update_available != update_authorized
runtime_success != evidence
```

This trace itself performs no upgrade. The separately reviewed PR #495 has since
completed the pinned `mcp` SDK 2.x migration with a full suite re-run.
`mcp-server/` remains a read-only, side-effect-free surface: stdio transport
delegated to the SDK, a separate bounded REST adapter, no scheduler, no queue,
no sampling and no roots. The migration created no new runtime authority.
