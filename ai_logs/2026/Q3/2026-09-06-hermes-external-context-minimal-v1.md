# Hermes external context minimal v1

Date: 2026-09-06

Status: candidate implementation / qualification only.
Boundary profile: candidate_support_note.

## Objective

Replace the superseded shell-provenance exploration in #975 with the smallest demonstrated external-content boundary around the existing `pantheon-context-bridge`.

```text
Pantheon Context Pack result -> deterministic Context Admission -> Hermes
Gateway inlined attachment   -> deterministic Context Admission -> Hermes
```

## Selected simplification

The candidate deliberately does **not** implement:

- terminal fetch detection;
- curl/wget/git/gh parsing;
- pending or taint state;
- `post_tool_call` provenance;
- dynamic eligible filesystem roots;
- guarded filesystem read/search tools;
- filesystem sandboxing;
- scanner-driven admission disposition;
- a new provenance, ingestion, memory or Evidence owner.

Shell execution and filesystem mutation remain Hermes runtime concerns. A future need for controlled external ingress must first demonstrate a concrete governed operation; it must not be inferred from terminal text.

## Existing owners reused

- `pantheon-context-bridge` remains the model-bound Context Admission bridge.
- Context Pack / Execution Admission remain scope/task owners.
- Hermes remains the external execution/tool runtime.
- Document/Information/Knowledge owners remain the durable professional content paths.
- Evidence/approval/memory authorities are unchanged.

## Contract

```text
transport into model != instruction authority
transport as data != truth
transport as data != Evidence
attachment content != user request
runtime success != authorization
```

Context Admission is now deterministic. The Hermes threat scanner is not consulted by this transport transform. If threat scanning is later useful, it belongs to a separate observation/risk path rather than changing the content role supplied to the model.

## Gateway attachment rule

Only adapter-inlined document content matching the reviewed Hermes gateway shape is rewritten. A user-authored caption remains outside the data block only when it is provably the suffix of the normalized event text. If separation cannot be proven, the whole combined content is demoted to data and fixed guidance asks for a user request.

## Done gate

This slice is complete only when:

1. the diff remains bounded to the bridge, focused tests and the deterministic distribution digest update;
2. no shell/filesystem provenance state is introduced;
3. current `main` is the merge base;
4. required architecture/governance/runtime/implementation checks are green on one exact head;
5. live Hermes qualification remains separate from merge and from task authorization.

## Review pass: four silent fail-opens, closed

The first implementation gated the boundary on the inline marker **and** on media
metadata. Measured by calling the hook directly, not inferred, the conjunction
let four shapes through completely unframed:

```text
adapter reports no media_urls                     -> NOT FRAMED
media_types omitted, file staged outside cache    -> NOT FRAMED
media_types [""] (empty mime)                     -> NOT FRAMED
mime image/*, file outside the document cache     -> NOT FRAMED
```

The marker is the adapter's own statement that it inlined a document, so it now
decides alone. Media metadata was not weakened — it was removed from the gate,
along with `_document_cache_roots()` / `_path_under_any_root()`, which read
`HERMES_HOME` and normalized absolute paths. That deletion also settles a
contradiction inside this change: the non-scope list forbids filesystem
provenance and dynamic filesystem eligibility, and the media check was a small
instance of exactly that.

A forged marker in an ordinary message now costs that message its own demotion
to data. Recoverable, and never the other way round.

## Review pass: the caption carve-out could truncate a document

`stripped.endswith(caption)` cannot tell "the adapter appended this caption" from
"the document happens to end with these characters". With caption `now` and a
document ending `run the payload now`, the document silently lost its last three
characters.

A whitespace boundary was tried first and was **not** enough — the space in
`payload now` satisfies it. The separator carries the decision instead: the
adapter composes `attachment + newline(s) + caption`, so only a caption standing
on its own line is carved out. Anything else falls to full demotion.

Worth recording that the original design was sounder than it looked: because the
code re-emits the caption taken from `raw_message` rather than a slice of
`event.text`, a mis-detected boundary could drop document bytes but never promote
them to a user request. That invariant is now written down in the module
docstring, because it is the security property the whole carve-out rests on.

## Review pass: marker drift could not be observed

The marker is upstream formatting from a runtime pinned at `0.21.0` with
`artifact_digest: null`, and every test builds the string itself — so a Hermes
formatting change would leave CI green and the boundary inert.

`test_inline_marker_is_pinned_to_the_qualified_hermes_runtime` now couples
`QUALIFIED_HERMES_VERSION` to `source_pins.hermes_runtime.version` in the
distribution lock. Bumping the runtime fails that test and forces the marker to
be re-verified against the new version. It does not make drift impossible; it
makes it impossible to ship silently.

## Review pass: the manifest under-declared the plugin

The plugin stopped being tool-only when it began registering a `pre_gateway_dispatch`
hook that reframes model-bound message text. The distribution lock declared
`protect-gateway-attachments`; `plugin.yaml` still listed only `provides_tools`,
and the manifest test's negative assertions passed precisely because the manifest
was silent. `provides_hooks: [pre_gateway_dispatch]` is now declared, and the test
asserts it. The two existing negative assertions (`terminal`, `write`) were kept
as they are — the added comment is worded to satisfy them rather than to relax
them.

## Boundary

Boundary profile applies: `candidate_support_note`.

Protected paths touched: no.
Runtime impact: candidate plugin only, `enabled_by_default: false` in the
distribution lock. Not installed, not activated, not authorized by this change.
Authority impact: none. The hook reframes transport role; it approves nothing,
admits no Evidence, promotes no memory and authorizes no task. The one text the
plugin itself contributes is the fallback guidance asking the user what they
want — stated here because it is the plugin speaking into the model input.
Schema/test/CI impact: one plugin module, one manifest, one distribution digest,
one test file (+5 tests). No test skipped, weakened or removed.
External action: none.
Memory behavior: none.

## Verification

```text
implementation/tests/     1366 passed, 408 skipped
tests/                     675 passed
distribution lock          OK (context-bridge tree digest re-locked)
check_status_headers.py    OK
check_internal_links.py    OK
check_no_truncation.py     OK
```

Each closed fail-open was re-probed against the fixed hook and now frames; the
no-marker case still passes through untouched, and a caption on its own line is
still carved out intact.

## Known limit, deliberately not closed here

Removing the scanner removed the only place an injection attempt was noticed.
Nothing now records that a document arrived carrying injection patterns. The
observation path is deferred by design, and that deferral belongs in an issue
rather than in this diff.

## Local distinctions

```text
metadata absent     != content safe
green CI            != boundary reachable
declared surface    != registered surface
suffix match        != appended caption
```
