# Hermes untrusted-content plugin boundary

Date: 2026-09-05  
Status: candidate implementation  
Scope: Pantheon-owned Hermes plugin only; no Hermes fork or core patch

## Objective

Extend the existing Pantheon Context Admission boundary so uploaded, downloaded,
cloned, emailed, or otherwise external file content can be used by Hermes
without acquiring instruction authority or turning a data boundary into generic
filesystem read authority.

The implementation must remain replaceable by a future native Hermes provenance
API and must not create a second document-ingestion, Evidence, approval, or
execution authority.

## Verified baselines

Pantheon work started from `main` at
`a7080fa7997f47594332db3f3c7cece265beb3fb`. Before final hardening, current
Pantheon `main` was rechecked at `305e5474e49af6842c8781355fa0cb9161dba9c9`.
The intervening main changes do not overlap the files changed by this candidate.

The canonical Pantheon qualification registry currently pins Hermes Agent
`0.21.0` at commit `29112bef099274229cadff79cdff7bf7b99c4b77`.
That exact qualified runtime exposes the extension surfaces used here:

- `pre_gateway_dispatch`, which may rewrite inbound `MessageEvent.text`;
- `pre_tool_call`, a fail-closed policy hook before dispatch;
- `post_tool_call`, emitted after normal, error, blocked, or cancelled tool
  completion with observer-grade `status` (`ok`, `error`, `blocked`,
  `cancelled`), `result`, and the original tool identity/arguments;
- `PluginContext.dispatch_tool(...)`, for native tool delegation without
  replacing Hermes built-ins;
- `PluginContext.register_skill(...)`, for the namespaced read-only guidance
  skill.

No parallel Pantheon implementation owns this boundary.

## Existing authority reused

The existing `pantheon-context-bridge` remains the only plugin artifact because
it already owns model-bound Context Admission.

```text
retrieved content != instruction
source preservation != trust
clean scan != trusted
memory != Evidence
successful execution != authorization
successful read != authorization
projection != persistence
best-effort provenance hint != governed provenance truth
```

`context_admission.py` exposes the shared `protect_untrusted_content(...)`
primitive. Existing Pantheon context tools use the same contract through
`protect_model_bound_result(...)`; there is no second delimiter or scanner.

## Inbound gateway text

`pre_gateway_dispatch` detects adapter-inlined document content marked with the
Hermes `[Content of <name>]:` form when document media is attached.

If the raw platform message exposes a caption that is provably the suffix of the
normalized event text, only the attachment prefix is wrapped as untrusted data
and the verified caption remains outside the boundary. If separation cannot be
proven, the combined text is demoted to data and fixed plugin guidance asks the
model to ask the user what action is wanted.

## File provenance compatibility layer

Intrinsic high-confidence external ingress includes:

- `$HERMES_HOME/cache/documents`;
- explicit `HERMES_DOCUMENT_CACHE_DIR`;
- sandbox-visible `/root/.hermes/cache/documents`.

Dynamic fetch recognition is intentionally narrower and split into three
states:

1. **pending candidate** — inferred from a simple supported fetch command before
   execution; may block ordinary reads but grants no guarded-read scope;
2. **eligible external root** — promoted only after `post_tool_call` reports
   `status="ok"`, the structured terminal result reports `exit_code == 0` with
   no error, and the expected destination is observably created or changed;
3. **taint-only root** — an expected destination is observably changed after an
   error/ambiguous outcome; it remains blocked from ordinary reads but still
   grants no guarded-read scope.

Supported best-effort producers are `git clone`, `gh repo clone`, `wget`, and
file-producing curl forms. Bare `curl URL` does not create provenance. Curl
short-option case is preserved and the parser recognizes `-o file`, `-ofile`,
`-o=file`, `--output file`, `--output=file`, and `-O`/`--remote-name`.

Compound shell programs (`&&`, `||`, pipes, separators, redirections and related
control syntax) are never promoted because an overall command status cannot
prove that the fetch sub-expression executed. In particular,
`false && git clone ... /` cannot turn `/` into guarded-reader scope.

For clone/tree candidates, promotion additionally requires that the destination
did not exist before and exists as a directory afterward. Existing broad paths
such as `/`, `/etc`, or `/tmp` therefore cannot become eligible merely because a
command names them. File candidates must be newly created or observably changed.

This state is bounded, process-local compatibility state. It is not governed
provenance truth.

## Covered direct read paths

`pre_tool_call` blocks ordinary `read_file` and intersecting `search_files`
access across intrinsic, eligible, pending, and taint-only roots. Ancestor
search scopes are blocked when they contain a protected root.

Common shell readers are also blocked when touching protected content,
including path-qualified forms such as `/bin/cat`.

Path checks use lexical and canonical forms. This blocks an outside symlink into
a protected root and prevents guarded delegation from following an inside
symlink out to unrelated local data.

`execute_code` is explicitly outside v1 filesystem mediation. A weak literal
regex is not treated as a security boundary.

## Guarded tools

`pantheon_untrusted_read` and `pantheon_untrusted_search` delegate to native
Hermes tools and frame returned text as data-only, but only for **eligible**
external roots:

- intrinsic document-cache roots; or
- dynamic roots promoted after the post-success observation contract above.

Pending and taint-only roots deliberately do not authorize guarded delegation.
Arbitrary local paths and symlink escapes are refused before native dispatch.
An internal `ContextVar` prevents the plugin from blocking its own validated
native delegation.

This distinction is essential:

```text
blocked as potentially external != authorized for guarded read
terminal returned success != task/effect authorization
framed as data != permission to read arbitrary files
```

## Bundled skill

`untrusted-content-reading` is namespaced guidance only. It now states that a
blocked path may be retried through a guarded tool only if the guarded tool
accepts that path. A pending/taint-only refusal must not be bypassed through
`terminal` or `execute_code`.

## Qualified tool surface

The governed profile may expose:

```text
pantheon_context_manifest
pantheon_context_entity
pantheon_untrusted_read
pantheon_untrusted_search
```

Only the first two remain required by the existing synthetic context-binding
acceptance. Guarded read/search are allowed capabilities, not mandatory steps.

## Security-review hardening

Review findings were treated as merge blockers even when CI was green. The
candidate now covers:

1. arbitrary-path disclosure through guarded readers;
2. ancestor `search_files` scopes containing external roots;
3. lexical symlink aliases into protected content;
4. guarded symlink escapes out of protected roots;
5. curl `-O` versus `-o` case semantics;
6. attached curl output syntax `-oFILE`;
7. path-qualified shell readers such as `/bin/cat`;
8. pre-execution fetch hints accidentally becoming guarded-read authorization.

The last item is resolved structurally through the qualified Hermes
`post_tool_call` lifecycle rather than by adding another security manager.

## Failure posture

- Missing/failed Hermes threat scanner: content remains untrusted and receives
  `review_recommended`; no trust upgrade occurs.
- Forged Context Admission delimiters are neutralized before framing.
- Missing task id: bounded default runtime state is used rather than silently
  disabling protection.
- Guarded path outside eligible roots: refused before native dispatch.
- Pending or failed/ambiguous fetch path: ordinary reads remain blocked, but the
  guarded tools do not gain authority from that state.
- Ambiguous gateway caption: combined text is demoted to data.
- Plugin disabled/not installed: this Pantheon protection is absent;
  installation/activation remains an external operator action.

## Non-goals and limits

This slice is not a filesystem sandbox, DLP system, malware scanner, approval
engine, Evidence admission path, or complete shell/provenance engine.

Known limits include arbitrary `execute_code`, exotic shell indirection,
unrecognized producer syntax, archive relocation, copied-content taint, and
process-lifetime loss of dynamic compatibility state. A future native Hermes
provenance API should replace the compatibility tracking rather than coexist as
a second authority.

## Completion criteria

The candidate is complete when:

1. the exact pinned Hermes runtime supports all used plugin APIs;
2. ordinary local files remain on ordinary Hermes paths;
3. covered external/pending/taint paths cannot enter model context through
   ordinary covered readers/searches;
4. guarded tools accept only eligible roots and reject arbitrary paths/symlink
   escapes;
5. dynamic eligibility requires `post_tool_call status=ok`, terminal success,
   and observable destination creation/change;
6. admitted guarded results always carry `instruction_authority="none"`;
7. gateway attachment data is separated from a provable caption or fully
   demoted when ambiguous;
8. runtime allowlists distinguish four allowed plugin tools from two required
   context tools;
9. focused tests, both Hermes labs, governance/architecture gates and the full
   implementation suite pass on the final head and exact distribution digest;
10. no installation, activation, task, Evidence, approval, persistence, memory,
    or execution authority is added.
