# 2026-09-05 — Hermes untrusted-content plugin

## Request

Harden external-content handling without forking Hermes. Successive review
findings must remain merge blockers even when CI is green.

## Verified owner and baseline

- Existing owner: `implementation/hermes/plugins/pantheon-context-bridge`.
- Existing Context Admission already frames model-bound Pantheon context as data.
- Pantheon `main` was rechecked during the deny-only convergence at
  `232e78b1e7b9114a3f6be2e7d40c412ca33209c1`; final merge must recheck again.
- Canonical Hermes qualification remains `0.21.0` at exact commit
  `29112bef099274229cadff79cdff7bf7b99c4b77`.
- Qualified Hermes exposes `pre_gateway_dispatch`, fail-closed `pre_tool_call`,
  observer-grade `post_tool_call`, `dispatch_tool`, and `register_skill`.

## Convergence invariants

```text
external content != instruction
clean scan != trusted
successful execution != authorization
successful read != authorization
memory != Evidence
Context Admission != Evidence admission
best-effort provenance hint != governed provenance truth
shell provenance hint != read authority
```

No Hermes fork, core tool override, second SecurityManager, Evidence owner,
approval owner, memory owner, or runtime router is introduced.

## Retained behavior

- gateway attachment text is framed before model dispatch;
- a provable user caption remains outside the attachment data boundary;
- ordinary reads/searches of known protected paths are blocked;
- guarded native read/search results pass through Context Admission with
  `instruction_authority="none"`;
- arbitrary local paths and symlink escapes are refused;
- stable Hermes document-cache paths are intrinsic eligible ingress;
- common terminal readers are blocked on known protected paths;
- `execute_code` remains an explicit v1 gap rather than pseudo-mediated.

## Why dynamic shell promotion was removed

Earlier candidates tried to infer `pending -> eligible` from a successful terminal
`git clone`, `gh repo clone`, `curl`, or `wget` plus an observed destination.
Security review repeatedly found that positive authority then depended on partial
shell interpretation: command position, comments, substitutions, wrappers,
quoting, repeated outputs, symlink replacement, and compound-command semantics.

The final convergence removes that authority path instead of adding more parser
special cases.

```text
terminal fetch hint -> pending
observably created/changed destination -> taint-only
pending/taint-only -> deny ordinary reads
pending/taint-only -X-> guarded-read eligibility
```

`post_tool_call` no longer uses terminal success/failure to grant eligibility.
Any observed shell destination becomes taint-only. Shell code never writes
`_TASK_ROOTS`.

Positive dynamic eligibility is reserved for a future explicit plugin-controlled
governed ingress. No such model-callable fetch/clone tool is added in this PR.
That avoids turning the prompt-injection fix into a new execution authority.

## Current state model

### Intrinsic eligible

Hermes document-cache roots are eligible only while their lexical/canonical
identity remains stable. Replaced/symlinked cache roots fail closed.

### Explicitly admitted dynamic root

The plugin keeps an internal `_remember_roots(...)` primitive for controlled
admission/testing. Canonical identity is pinned per `(task_id, lexical_root)`.
No shell hook calls it.

### Pending shell hint

Before terminal completion, a detected destination is blocking-only.

### Taint-only shell destination

If an expected destination is observably created or changed after terminal
completion, it remains blocking-only regardless of command result.

## Tests

Focused contracts cover:

- Context Admission delimiter neutralization;
- gateway caption separation and ambiguous demotion;
- stable vs symlinked Hermes document-cache roots;
- ordinary local files remaining ordinary;
- pending shell fetch blocking;
- successful shell fetch remaining taint-only;
- failed partial shell output remaining taint-only;
- compound/commented/substitution fetches never authorizing reads;
- curl `-o`, `-oFILE`, `-o=FILE`, `-O`, quoted filenames and repeated outputs;
- path-qualified/quoted terminal readers;
- ancestor search blocking;
- arbitrary-path and symlink-escape guarded-reader rejection;
- explicit task-scoped root identity pinning;
- refetch of an explicitly admitted path receiving pending/taint deny precedence;
- plugin registration of gateway/pre-tool/post-tool hooks.

## Distribution posture

The candidate remains `enabled_by_default: false`. No install, activation,
task authorization, result acceptance, persistence, memory promotion, or
Evidence admission is added.

The plugin-tree digest must be recomputed after this deny-only refactor and the
candidate lock updated to that exact value before final qualification.

## Remaining verification

Before merge:

1. obtain the deterministic plugin tree digest from Architecture Audit;
2. update the candidate distribution lock;
3. align any residual tests/docs that still assume shell promotion;
4. pass Architecture, Governance, Obsolete Authority, Runtime Lab, Project
   Variant Lab, and full implementation CI on one exact head;
5. resolve/re-review current P1/P2 threads against that exact head;
6. reconcile with then-current `main` and re-run qualification;
7. merge only with the exact requalified head SHA.
