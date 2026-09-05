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
`a7080fa7997f47594332db3f3c7cece265beb3fb` after PR #972.

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

Current upstream Hermes was also rechecked during this work and had advanced to
`9dd6634c5635321cf38840cc30e9b51226689128`. No Pantheon implementation or open
Pantheon PR already covered this plugin-only boundary.

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
```

`context_admission.py` now exposes one generic
`protect_untrusted_content(...)` primitive. The existing Pantheon context tools
continue to call the same contract through `protect_model_bound_result(...)`.
There is no second delimiter or scanner implementation.

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

Known external paths include:

- the Hermes document cache under the active `HERMES_HOME`;
- an explicit `HERMES_DOCUMENT_CACHE_DIR`;
- the standard sandbox-visible `/root/.hermes/cache/documents` path;
- bounded per-task roots learned from common `git clone`, `gh repo clone`,
  `curl`, and `wget` terminal commands.

`pre_tool_call` blocks direct model reads/searches of those paths through
`read_file`, `search_files`, and common shell content-reader commands. Literal
known-root references in `execute_code` receive bounded defense-in-depth, but
this is not claimed as complete filesystem mediation.

The plugin does not override Hermes built-ins and requests no `tools.override`
capability.

### Guarded tools

`pantheon_untrusted_read` delegates to Hermes-native `read_file` and applies
Context Admission to the complete result.

`pantheon_untrusted_search` delegates to Hermes-native `search_files` and
applies Context Admission to returned snippets.

An internal `ContextVar` marks those delegated calls so the plugin never blocks
its own guarded path if host lifecycle dispatch invokes `pre_tool_call` there.

### Bundled skill

The plugin registers `untrusted-content-reading` as a namespaced skill. It tells
the model when to select the guarded tools and restates the authority
invariants. The skill is guidance only; deleting or ignoring it must not remove
the executable hook/tool gates.

## Failure posture

- Missing/failed Hermes threat scanner: content remains untrusted and receives
  `review_recommended`; no trust upgrade occurs.
- Forged Context Admission delimiters in source text are neutralized before
  framing.
- Missing task id: fetch provenance uses one bounded default runtime scope
  rather than silently disabling tracking.
- Ambiguous gateway caption: combined text is demoted to data rather than
  guessing which bytes came from the user.
- Plugin disabled/not installed: this Pantheon-owned protection is absent;
  installation/activation remains an external operator action and the
  distribution lock does not claim otherwise.

## Non-goals and limits

This slice is not a filesystem sandbox, DLP system, malware scanner, approval
engine, Evidence admission path, or complete shell parser.

Known limits include dynamically constructed paths inside arbitrary
`execute_code`, shell indirection such as `sh -c`, redirections not recognized by
the bounded fetch parser, archive extraction into a different tree, and content
copied from an untrusted root into an unrelated path. These remain explicit
uncertainties rather than hidden claims.

A future native Hermes provenance API should replace the compatibility
root-tracking portion while keeping Pantheon's authority invariant unchanged.

## Completion criteria

The candidate slice is complete when:

1. qualified Hermes `v2026.8.31` supports every plugin API used;
2. ordinary local files remain on ordinary Hermes read/search paths;
3. known external paths cannot be directly read/search-resulted to the model
   through the covered core tools;
4. guarded tools always return `instruction_authority="none"`;
5. inline attachment data is separated from a provable user caption or fully
   demoted when ambiguous;
6. the skill is bundled in the same plugin tree;
7. focused tests pass and the distribution tree digest is updated;
8. no installation, activation, task, Evidence, approval, or execution
   authority is added.
