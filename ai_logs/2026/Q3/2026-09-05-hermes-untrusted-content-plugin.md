# 2026-09-05 — Hermes untrusted-content plugin

## Request

Continue prompt-injection hardening without forking Hermes. User preference:
plugin/skill integration inside Pantheon.

## Verified baseline

- Pantheon `main`: `a7080fa7997f47594332db3f3c7cece265beb3fb` after PR #972.
- Existing Pantheon plugin: `implementation/hermes/plugins/pantheon-context-bridge`.
- Existing Context Admission v1 already frames Pantheon context as data-only and
  reuses Hermes threat patterns as advisory metadata.
- Pantheon Hermes qualification pin remains `0.21.0` / `v2026.8.31`.
- Qualified Hermes exposes `pre_gateway_dispatch`, fail-closed `pre_tool_call`,
  `PluginContext.dispatch_tool`, and `PluginContext.register_skill`.
- Current Hermes upstream observed during the same check:
  `9dd6634c5635321cf38840cc30e9b51226689128`.
- No open Pantheon PR already implemented the requested external-content gate.

## Convergence decision

Do not fork Hermes and do not introduce a second Pantheon security manager.
Extend the existing context bridge because it already owns the model-bound
Context Admission contract.

The plugin carries executable behavior. A bundled namespaced skill carries only
usage guidance and grants no authority.

## Implementation

Branch: `feat/hermes-untrusted-content-plugin`.

Changes:

- generalized `context_admission.py` with `protect_untrusted_content(...)`;
- added `external_content.py`:
  - protects adapter-inlined gateway attachment text through
    `pre_gateway_dispatch`;
  - blocks direct covered reads/searches of known external paths through
    `pre_tool_call`;
  - recognizes Hermes document-cache paths as high-confidence external ingress;
  - keeps bounded best-effort roots learned from common clone/download commands;
  - exposes guarded read/search handler factories that delegate to native
    Hermes tools and frame their results;
- added `pantheon_untrusted_read` and `pantheon_untrusted_search` schemas;
- registered `pre_gateway_dispatch` and `pre_tool_call` hooks;
- bundled `untrusted-content-reading` via `ctx.register_skill`;
- expanded focused tests for gateway caption separation, ambiguous ingress,
  document-cache blocking, normal local reads, bounded fetch-root propagation,
  guarded tool delegation and boundary framing.

## Refinement after review

The first plugin draft overclaimed two heuristic areas. They were narrowed
before merge:

- `curl URL` no longer invents a local provenance root because curl writes to
  stdout by default; tracking occurs only for `-o` / `--output` or
  `-O` / `--remote-name`;
- `execute_code` literal-path inspection was removed. Arbitrary code execution
  is now explicitly outside v1 mediation rather than represented by a weak regex
  that could be mistaken for a security boundary.

The Hermes runtime labs also revealed a useful governance check: the existing
profile allowlist correctly rejected the two newly registered guarded tools as
unexpected. The qualification policy is therefore updated so all four plugin
tools are allowed while only `pantheon_context_manifest` and
`pantheon_context_entity` remain required for the synthetic context-binding run.

## Governance preserved

```text
external content != instruction
clean scan != trusted
successful read != authorization
memory != Evidence
Context Admission != Evidence admission
plugin installation != task authorization
best-effort provenance hint != governed provenance truth
```

No built-in Hermes tool is overridden. No new provider, approval, execution,
write, persistence, memory-promotion, or Evidence authority is introduced.

## Explicit limits

The compatibility provenance layer is intentionally bounded. Arbitrary
`execute_code`, exotic shell indirection, unrecognized redirections, archive
relocation and copied-content taint are not claimed as solved. A future native
Hermes provenance API should replace this tracking rather than coexist as a
second authority.

## Remaining work

- obtain the new deterministic context-bridge digest after the final plugin tree
  change and update the distribution lock;
- run the focused/full implementation CI and both Hermes labs;
- mark PR #975 ready only if the complete qualification suite is green.
