# Hermes untrusted-content plugin boundary

Date: 2026-09-05  
Status: candidate implementation  
Scope: Pantheon-owned Hermes plugin only; no Hermes fork or core patch

## Objective

Extend the existing Pantheon Context Admission boundary so external content can
be used by Hermes without acquiring instruction authority and without turning a
data boundary into generic filesystem-read authority.

The implementation must remain replaceable by a future native Hermes provenance
API. It must not create a second document-ingestion, Evidence, approval,
execution, memory, or provenance authority.

## Verified baseline

Pantheon `main` was rechecked during the deny-only convergence at
`232e78b1e7b9114a3f6be2e7d40c412ca33209c1`. Final merge qualification must
recheck the then-current `main` again.

The canonical Pantheon qualification registry continues to pin Hermes Agent
`0.21.0` at exact commit `29112bef099274229cadff79cdff7bf7b99c4b77`.
The qualified runtime exposes the extension surfaces used here:

- `pre_gateway_dispatch`;
- fail-closed `pre_tool_call`;
- observer-grade `post_tool_call`;
- `PluginContext.dispatch_tool(...)`;
- `PluginContext.register_skill(...)`.

No Hermes fork, core patch, built-in tool override, or second SecurityManager is
introduced.

## Reused authority

`pantheon-context-bridge` remains the single Pantheon owner because it already
owns model-bound Context Admission.

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

`context_admission.py` provides the shared `protect_untrusted_content(...)`
primitive. Existing Pantheon context tools and guarded file tools use that same
contract.

## Gateway attachment boundary

`pre_gateway_dispatch` recognizes adapter-inlined document content using Hermes'
`[Content of <name>]:` form when document media is attached.

If a user-authored caption is provably separable from the attachment body, only
the attachment content is wrapped as untrusted data. If separation cannot be
proven, the whole combined text is demoted to data and fixed guidance asks the
model to obtain a user request rather than execute content directives.

## External path states

There are deliberately only two authority classes.

### Positive eligibility

Guarded read/search can operate only on:

1. intrinsic Hermes document-cache roots whose lexical/canonical identity is
   still stable; or
2. roots explicitly admitted by a plugin-controlled governed operation.

The current candidate exposes no model-callable operation that can arbitrarily
create such positive eligibility.

### Deny-only shell provenance

Common shell producers (`git clone`, `gh repo clone`, `curl`, `wget`) are parsed
only as compatibility hints for blocking.

Before terminal completion, an inferred destination is `pending`. After terminal
completion, any expected destination that is observably created or changed
becomes `taint-only`, regardless of terminal success/failure status.

Neither state can ever become positive guarded-read eligibility.

```text
shell fetch observed != guarded-read authorization
terminal success != authorization
pending != eligible
taint-only != eligible
```

This removes shell parsing from the positive authority path. Shell quoting,
multiple curl outputs, command substitution, comments, pipelines, wrappers, or
other syntax can at worst influence conservative deny state; they cannot widen
filesystem read authority.

## Why shell promotion was removed

Earlier candidates tried to promote a successfully observed shell destination to
`eligible`. Successive security reviews demonstrated that doing so required
reconstructing too much shell semantics: comments, substitutions, wrappers,
multiple outputs, symlink replacement, command position, and related edge cases.

The convergence decision is therefore structural rather than another regex fix:

```text
shell heuristics -> blocking/taint only
shell heuristics -X-> positive read authority
```

A future need for controlled download/clone should be implemented as a separate,
explicit plugin ingress with its own execution and authorization contract rather
than inferred from arbitrary terminal text.

## Covered read paths

`pre_tool_call` blocks ordinary `read_file` and intersecting `search_files`
access across intrinsic, explicitly eligible, pending, and taint-only roots.
Ancestor search scopes are blocked when they contain protected material.

Common shell readers are blocked when they touch protected content, including
path-qualified and quoted forms. Path checks use lexical and canonical forms to
cover symlink aliases and prevent guarded delegation from escaping an eligible
root.

`execute_code` remains explicitly outside v1 filesystem mediation. This candidate
is not a filesystem sandbox.

## Guarded tools

`pantheon_untrusted_read` and `pantheon_untrusted_search` delegate to native
Hermes tools only after `_require_guarded_path(...)` confirms positive
eligibility and rejects pending/taint state.

Returned text is framed through Context Admission with
`instruction_authority="none"`.

Arbitrary local paths, pending shell destinations, taint-only shell destinations,
and symlink escapes are refused before native dispatch.

## Intrinsic cache identity

Hermes document-cache roots are positive ingress only while their configured
lexical root is not a symlink and resolves canonically to itself. A replaced or
symlinked cache root fails closed instead of being lazily redefined as trusted at
first guarded access.

## Bundled skill

`untrusted-content-reading` is guidance only. It states explicitly that a shell
fetch cannot be made eligible by retrying it, changing quoting, or using another
reader. A refusal must not be bypassed through `terminal` or `execute_code`.

## Qualified tool surface

The governed candidate profile may expose:

```text
pantheon_context_manifest
pantheon_context_entity
pantheon_untrusted_read
pantheon_untrusted_search
```

Only the first two remain required by the existing synthetic context-binding
acceptance. Guarded read/search are allowed capabilities, not mandatory steps.

## Failure posture

- Missing/failed Hermes threat scanner: content remains untrusted; no trust
  upgrade occurs.
- Forged Context Admission delimiters are neutralized before framing.
- Missing task id: bounded default runtime state is used.
- Guarded path outside positive eligibility: refused before native dispatch.
- Shell fetch destination: pending then taint-only if observably changed; never
  promoted from success.
- Ambiguous gateway caption: combined text is demoted to data.
- Plugin disabled/not installed: this Pantheon boundary is absent; installation
  and activation remain external operator actions.

## Non-goals

This slice is not a filesystem sandbox, DLP system, malware scanner, approval
engine, Evidence admission path, or complete shell/provenance engine.

Known limits include arbitrary `execute_code`, unrecognized producer syntax,
archive relocation, copied-content taint, and process-lifetime loss of dynamic
deny state. A future native Hermes provenance API should replace compatibility
tracking rather than coexist as a second authority.

## Completion criteria

The candidate is complete when:

1. the exact pinned Hermes runtime supports all used plugin APIs;
2. ordinary local files remain on ordinary Hermes paths;
3. covered external/pending/taint paths cannot enter model context through
   covered ordinary readers/searches;
4. guarded tools accept only intrinsic stable or explicitly admitted roots;
5. no terminal command or result can create guarded-read eligibility;
6. guarded results always carry `instruction_authority="none"`;
7. gateway attachment data is separated from a provable caption or fully
   demoted when ambiguous;
8. four plugin tools remain allowed while only two context tools are required;
9. architecture/governance gates, both Hermes labs and the full implementation
   suite pass on a head reconciled with current `main` and the exact plugin tree
   digest;
10. no install, activation, task, Evidence, approval, persistence, memory, or
    execution authority is added.
