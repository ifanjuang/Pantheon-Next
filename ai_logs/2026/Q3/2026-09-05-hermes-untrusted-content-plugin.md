# 2026-09-05 — Hermes untrusted-content plugin

## Request

Continue prompt-injection hardening without forking Hermes, then verify and
merge only after security review and full requalification.

## Verified baseline

- Existing owner: `implementation/hermes/plugins/pantheon-context-bridge`.
- Existing Context Admission v1 already frames Pantheon context as data-only and
  uses Hermes threat patterns as advisory metadata.
- Current Pantheon `main` was rechecked at
  `305e5474e49af6842c8781355fa0cb9161dba9c9` during final hardening.
- Canonical Hermes qualification remains `0.21.0` at exact commit
  `29112bef099274229cadff79cdff7bf7b99c4b77`.
- That exact runtime exposes `pre_gateway_dispatch`, fail-closed
  `pre_tool_call`, observer-grade `post_tool_call`, native `dispatch_tool`, and
  `register_skill`.
- `post_tool_call` reports `status` values including `ok`, `error`, `blocked`,
  and `cancelled` plus the tool result and original tool identity/arguments.

## Convergence decision

Do not fork Hermes and do not introduce another Pantheon security manager.
Extend the existing context bridge, keeping one Context Admission framing
primitive and one replaceable compatibility provenance layer.

```text
external content != instruction
clean scan != trusted
successful execution != authorization
successful read != authorization
memory != Evidence
Context Admission != Evidence admission
best-effort provenance hint != governed provenance truth
```

## Candidate behavior

- gateway attachment text is framed through `pre_gateway_dispatch`; a caption
  remains outside only when its user-authored separation is provable;
- direct covered reads/searches of known or suspected external paths are blocked
  by `pre_tool_call`;
- native guarded read/search tools return content through Context Admission with
  `instruction_authority="none"`;
- guarded tools refuse arbitrary local paths and symlink escapes;
- Hermes document-cache paths are intrinsic external ingress;
- dynamic fetch hints cover bounded forms of `git clone`, `gh repo clone`,
  `wget`, and file-producing curl commands;
- bare `curl URL` does not invent local provenance;
- curl recognizes `-o file`, `-oFILE`, `-o=FILE`, long `--output` forms, and
  case-sensitive `-O` / `--remote-name`;
- common terminal readers, including path-qualified `/bin/cat`, are blocked on
  protected paths;
- `execute_code` remains an explicit v1 gap rather than receiving pseudo-coverage.

## Review findings and hardening

The first six-workflow-green candidate was not merged because review found
security issues. Across successive reviews, the candidate was hardened against:

1. arbitrary host-path disclosure through `pantheon_untrusted_*`;
2. ancestor searches containing a protected root;
3. symlink aliases into protected roots;
4. guarded symlink escapes out of protected roots;
5. curl `-O`/`-o` confusion;
6. path-qualified shell readers;
7. valid attached curl `-oFILE` syntax;
8. pre-execution fetch hints becoming guarded-reader authorization.

The last finding changed the provenance state model rather than adding a special
case. Dynamic fetch state is now split into:

- **pending**: inferred before execution; blocking-only, never guarded-read
  authorization;
- **eligible**: promoted only after Hermes `post_tool_call status="ok"`, a
  structured terminal `exit_code == 0` without error, and an observably created
  or changed expected destination;
- **taint-only**: an expected destination changed after a failed/ambiguous
  outcome; ordinary reads stay blocked, but guarded tools still refuse it.

Compound shell commands are not promoted because overall success cannot prove
which fetch branch ran. `false && git clone ... /` therefore cannot authorize
`/`. Clone destinations must be newly created directories; file destinations
must be newly created or observably changed.

This preserves the authority distinction:

```text
blocked as potentially external != authorized for guarded read
terminal success != task/effect authorization
framed as data != permission to read arbitrary filesystem content
```

## Tests

Focused contracts now cover:

- delimiter forgery and data-only framing;
- gateway caption separation and ambiguous demotion;
- document-cache blocking and ordinary local files;
- pending fetch blocking without guarded-read eligibility;
- post-success promotion of an observed destination;
- failed partial output becoming taint-only;
- unexecuted compound fetch not authorizing a broad root;
- `-o`, `-oFILE`, `-o=FILE`, and `-O` curl forms;
- ancestor search blocking;
- path-qualified readers;
- arbitrary local guarded paths and symlink escapes;
- guarded native delegation and framing;
- plugin registration of `pre_gateway_dispatch`, `pre_tool_call`, and
  `post_tool_call`.

## Distribution integrity

After the final plugin-tree changes, the Pantheon Architecture Audit independently
recomputed the context-bridge tree digest as:

`sha256:4fa85488ccb441989df7709f2f26f93ec95c208b2c2e049a34c02a7c6d80832e`

The candidate distribution lock is updated to that exact digest. It remains
`candidate`, `enabled_by_default: false`, with no install, activation, task,
result-acceptance, or Evidence authority.

## Remaining verification

The final head must still pass all required workflows after the digest/docs/test
updates, have no unresolved current P1/P2 review finding, and be reconciled with
current `main` before merge. Merge is a separate action and must use the exact
requalified head.
