# 2026-09-05 — Hermes untrusted-content plugin

## Request

Continue prompt-injection hardening without forking Hermes. User preference:
plugin/skill integration inside Pantheon.

## Verified baseline

- Work started from Pantheon `main` at `a7080fa7997f47594332db3f3c7cece265beb3fb` after PR #972.
- The final candidate was subsequently rebased/qualified against newer `main`
  after PR #970.
- Existing Pantheon plugin: `implementation/hermes/plugins/pantheon-context-bridge`.
- Existing Context Admission v1 already frames Pantheon context as data-only and
  reuses Hermes threat patterns as advisory metadata.
- Pantheon Hermes qualification pin remains `0.21.0` / `v2026.8.31`.
- Qualified Hermes exposes `pre_gateway_dispatch`, fail-closed `pre_tool_call`,
  `PluginContext.dispatch_tool`, and `PluginContext.register_skill`.
- No parallel Pantheon PR was found that already implemented this
  external-content boundary.

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
  - exposes root-bounded guarded read/search handler factories that delegate to
    native Hermes tools only after path validation and frame returned text as
    data-only;
- added `pantheon_untrusted_read` and `pantheon_untrusted_search` schemas;
- registered `pre_gateway_dispatch` and `pre_tool_call` hooks;
- bundled `untrusted-content-reading` via `ctx.register_skill`;
- expanded focused tests for gateway caption separation, ambiguous ingress,
  document-cache blocking, normal local reads, bounded fetch-root propagation,
  guarded tool delegation and boundary framing.

## First refinement before review

The first plugin draft overclaimed two heuristic areas. They were narrowed:

- `curl URL` no longer invents a local provenance root because curl writes to
  stdout by default; tracking occurs only for `-o` / `--output` or
  `-O` / `--remote-name`;
- `execute_code` literal-path inspection was removed. Arbitrary code execution
  is explicitly outside v1 mediation rather than represented by a weak regex
  that could be mistaken for a security boundary.

The Hermes runtime labs also revealed a useful governance check: the existing
profile allowlist correctly rejected the two newly registered guarded tools as
unexpected. Qualification policy was updated so all four plugin tools are
allowed while only `pantheon_context_manifest` and `pantheon_context_entity`
remain required for the synthetic context-binding run.

## Ready-for-review security findings

After the first complete six-workflow green run and marking PR #975 ready, the
automated code review identified five additional path-boundary issues. Two were
P1 and three P2, so the PR was not merged despite green CI.

Observed problems:

1. `pantheon_untrusted_read` / `pantheon_untrusted_search` could dispatch an
   arbitrary host-readable path because framing prevented instruction authority
   but did not constrain filesystem disclosure;
2. direct `search_files` rooted above a protected directory could still return
   snippets from the protected tree;
3. lexical-only containment could be bypassed by symlink aliases;
4. case-insensitive curl option parsing could treat `-O` as `-o` and remember
   the URL as a destination path;
5. path-qualified readers such as `/bin/cat` were not recognized by the shell
   reader gate.

## Hardening applied

- guarded read/search now refuse any path that is not both lexically and
  canonically contained in one known external root;
- this also refuses a symlink inside an external tree that resolves to an
  unrelated local file, preventing guarded tools from becoming generic host
  filesystem readers;
- direct path detection checks both lexical and resolved forms, so an outside
  symlink alias into a protected root is still blocked;
- direct `search_files` is blocked when its scope is inside a protected root or
  contains one;
- common shell content readers are recognized by basename even when invoked via
  a path such as `/bin/cat`;
- `curl -o` and `curl -O` parsing is case-sensitive and separate;
- path-qualified common fetch commands are still treated only as best-effort
  provenance hints, not governed truth;
- focused regression tests cover every review finding plus symlink escape from
  a protected root.

The resulting invariant is stronger and clearer:

```text
framed-as-data != permission to read arbitrary filesystem content
known external path != arbitrary local path
CI success != security review complete
```

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

## Current verification state

- first review-ready head `f185132ed04c8cac7367199a3309c522bf230578` had all six workflows green;
- post-review hardening changed the plugin tree and therefore intentionally
  invalidated the previous digest;
- Architecture Audit recomputed the hardened plugin digest as
  `sha256:752cccdf182fe47ea643ee4a398df97b604384eb8aa6611840a7fd5d1d34cc3d`;
- the distribution lock was updated to that exact digest;
- final merge remains blocked until the hardened head again passes the complete
  workflow set and the review threads are reconciled.
