# Hermes untrusted-content plugin boundary

Date: 2026-09-05  
Status: candidate implementation  
Scope: Pantheon-owned Hermes plugin only; no Hermes fork or core patch

## Objective

Extend the existing Pantheon Context Admission boundary so uploaded, downloaded,
cloned, emailed, or otherwise external file content can be read by Hermes without
acquiring instruction authority.

The implementation must remain replaceable by a future native Hermes provenance
API and must not create a second document-ingestion, Evidence, approval, or
execution authority.

## Verified baselines

Pantheon work started from `main` at
`a7080fa7997f47594332db3f3c7cece265beb3fb` after PR #972 and the candidate was
subsequently requalified against the newer `main` after PR #970.

Pantheon continues to qualify Hermes `0.21.0` / `v2026.8.31`. That qualified
runtime already exposes all extension surfaces used here:

- `pre_gateway_dispatch`, a directive hook that may rewrite inbound
  `MessageEvent.text` before gateway dispatch;
- `pre_tool_call`, a policy hook whose block decision is fail-closed on hook
  timeout;
- `PluginContext.dispatch_tool(...)`, which lets a plugin call native tools
  without replacing them;
- `PluginContext.register_skill(...)`, which registers a namespaced read-only
  plugin skill.

No parallel Pantheon implementation or open PR was found that already owned this
external-content boundary.

## Existing authorities reused

The existing `pantheon-context-bridge` remains the only plugin artifact because
it already owns the data-only Context Admission framing used by model-bound
Pantheon context.

The shared invariant remains:

```text
retrieved content != instruction
source preservation != trust
clean scan != trusted
memory != Evidence
successful read != authorization
projection != persistence
best-effort provenance hint != governed provenance truth
```

`context_admission.py` exposes one generic `protect_untrusted_content(...)`
primitive. The existing Pantheon context tools continue to call the same
contract through `protect_model_bound_result(...)`. There is no second delimiter
or scanner implementation.

## Plugin surface

### Inbound gateway text

`pre_gateway_dispatch` detects adapter-inlined document content marked with the
existing Hermes `[Content of <name>]:` form when document media is attached.

If the platform raw message exposes a caption that is provably the suffix of the
normalized event text, the plugin wraps only the attachment prefix as untrusted
data and leaves the verified caption outside the boundary as user-authored text.

If the caption cannot be separated without guessing, the plugin demotes the
whole combined text to data and appends fixed plugin guidance asking the model
to ask the user what action they want. It never guesses a user instruction from
document text.

### Local/extracted file reads

Known external paths include high-confidence Hermes ingress locations:

- the Hermes document cache under the active `HERMES_HOME`;
- an explicit `HERMES_DOCUMENT_CACHE_DIR`;
- the standard sandbox-visible `/root/.hermes/cache/documents` path.

The plugin also keeps bounded per-task **best-effort provenance hints** for a
small set of common terminal fetches: `git clone`, `gh repo clone`, `wget`, and
`curl` only when curl is expected to create a file (`-o` / `--output` or
`-O` / `--remote-name`). A bare `curl URL` writes to stdout and therefore does
not invent a local external-file root. Short option case is preserved so
`curl -O` cannot be confused with `curl -o`.

`pre_tool_call` blocks direct model reads of covered paths through `read_file`,
and blocks `search_files` when its search scope either lies inside a protected
root or contains one. This prevents an ancestor search such as `/work` from
returning snippets from a protected `/work/ext` tree.

Common shell content-reader commands are also blocked when they touch or contain
a protected root. Path-qualified readers such as `/bin/cat` are recognized as
well as bare command names.

Path checks consider both lexical paths and resolved symlink targets. This keeps
an outside alias pointing into a protected root from bypassing the gate while
also preventing guarded delegation from following a symlink inside a protected
tree out to an unrelated local file.

These heuristics are defense-in-depth hints, not a provenance authority and not
a complete shell parser.

`execute_code` is intentionally not claimed as mediated by this v1 plugin. A
literal-path regex would create an impression of coverage without controlling
dynamic path construction, imports, subprocesses, or copied taint. That surface
remains an explicit gap for a future native Hermes provenance mechanism.

The plugin does not override Hermes built-ins and requests no `tools.override`
capability.

### Guarded tools

`pantheon_untrusted_read` delegates to Hermes-native `read_file` and applies
Context Admission to the complete result, but only after proving that the
requested path remains lexically and canonically inside a known external root.
An arbitrary local path is refused before native dispatch.

`pantheon_untrusted_search` applies the same root-bounded rule before delegating
to Hermes-native `search_files`, then applies Context Admission to returned
snippets.

An internal `ContextVar` marks those delegated calls so the plugin never blocks
its own already-validated guarded dispatch if host lifecycle execution invokes
`pre_tool_call` there.

### Bundled skill

The plugin registers `untrusted-content-reading` as a namespaced skill. It tells
the model when to select the guarded tools and restates the authority
invariants. The skill is guidance only; deleting or ignoring it must not remove
the executable hook/tool gates.

## Qualified tool surface

The governed Hermes profile may expose four Pantheon plugin tools:

```text
pantheon_context_manifest
pantheon_context_entity
pantheon_untrusted_read
pantheon_untrusted_search
```

For the existing synthetic context-binding acceptance, only the first two remain
required. The guarded read/search tools are allowed but not required; adding a
capability to the reviewed plugin surface must not silently turn that capability
into a mandatory execution step.

## Review hardening

The ready-for-review pass found five concrete bypasses and all were treated as
merge blockers rather than waived because the earlier CI was green:

1. guarded read/search could be used as arbitrary host filesystem readers;
2. direct `search_files` from an ancestor scope could include protected roots;
3. lexical-only containment could be bypassed with symlink aliases;
4. case-insensitive curl short-option parsing confused `-O` with `-o`;
5. path-qualified shell readers such as `/bin/cat` were not recognized.

The implementation now closes those cases and adds explicit regression tests.
This preserves the distinction:

```text
CI success != security review complete
framed-as-data != permission to read arbitrary files
known external root != arbitrary filesystem scope
```

## Failure posture

- Missing/failed Hermes threat scanner: content remains untrusted and receives
  `review_recommended`; no trust upgrade occurs.
- Forged Context Admission delimiters in source text are neutralized before
  framing.
- Missing task id: fetch provenance hints use one bounded default runtime scope
  rather than silently disabling tracking.
- Guarded path outside known external roots: refused before native dispatch.
- Guarded symlink escape from an external root: refused before native dispatch.
- Ambiguous gateway caption: combined text is demoted to data rather than
  guessing which bytes came from the user.
- Plugin disabled/not installed: this Pantheon-owned protection is absent;
  installation/activation remains an external operator action and the
  distribution lock does not claim otherwise.

## Non-goals and limits

This slice is not a filesystem sandbox, DLP system, malware scanner, approval
engine, Evidence admission path, or complete shell parser.

Known limits include arbitrary `execute_code`, shell indirection such as
`sh -c`, redirections not recognized by the bounded fetch parser, archive
extraction into a different tree, and content copied from an untrusted root into
an unrelated path. These remain explicit uncertainties rather than hidden
claims.

A future native Hermes provenance API should replace the compatibility
root-tracking portion while keeping Pantheon's authority invariant unchanged.

## Completion criteria

The candidate slice is complete when:

1. qualified Hermes `v2026.8.31` supports every plugin API used;
2. ordinary local files remain on ordinary Hermes read/search paths;
3. known external paths cannot be directly read/search-resulted to the model
   through the covered core tools, including ancestor search scopes and symlink
   aliases;
4. guarded tools refuse paths outside known external roots and symlink escapes;
5. admitted guarded results always return `instruction_authority="none"`;
6. inline attachment data is separated from a provable user caption or fully
   demoted when ambiguous;
7. the skill is bundled in the same plugin tree;
8. runtime/lab allowlists distinguish the four allowed plugin tools from the
   two context tools required by the synthetic context run;
9. focused tests, both Hermes labs, architecture/governance checks and the full
   implementation suite pass with the final distribution tree digest;
10. no installation, activation, task, Evidence, approval, or execution
    authority is added.
