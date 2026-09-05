# 2026-09-05 — Context Admission boundary

## Objective

Implement the agreed generalized prompt-injection boundary as a Context Admission
primitive without creating a competing document-security or execution-security
owner.

## Verified baseline

Pantheon `main` was rechecked immediately before the branch was created:

```text
fd39f1d377d57eb2dc03060c0f93b21763b745b7
```

No open Pantheon PR or issue was found implementing Context Admission,
prompt-injection admission, or untrusted-context transport in parallel.

Hermes was rechecked:

- Pantheon qualification pin: Hermes Agent `0.21.0`;
- qualified release `v2026.8.31` contains `tools.threat_patterns` and native
  untrusted tool-result wrapping for web/browser/MCP results;
- current upstream `main` observed during the review:
  `deaebd9b1713745e35164f8673bd2d4c38d99e5f`.

## Existing paths retained

Unchanged:

- Source Intake remains source preservation/project-link authority;
- `project_document_admission` remains professional Source-to-revision admission;
- Context Pack / scoped context remains scope authority;
- Evidence remains separate;
- approval remains separate;
- Hermes command/tool execution guards remain separate.

## Gap

`pantheon_context_manifest` and `pantheon_context_entity` are native plugin tool
names. Hermes 0.21.0's built-in high-risk tool-name classifier does not
automatically classify those names as untrusted, even though entity output can
contain source-derived or user-controlled text.

## Change

Composed Context Admission directly into both registered model-bound handlers
of the existing `pantheon-context-bridge`.

The handler boundary:

```text
Pantheon bounded context result
-> Hermes context threat scan
-> reserved delimiter neutralization
-> <untrusted_tool_result>
-> content_role=data
-> instruction_authority=none
-> admitted_untrusted | review_recommended
```

The Hermes scanner is reused, not copied.

No findings never upgrades the content to trusted.

Scanner absence/failure produces `review_recommended` while instruction authority
remains `none`. This is advisory classification only; no human gate is claimed or
executed by this slice.

The direct handler composition was chosen after verifying that Hermes'
`transform_tool_result` surface uses a first-valid-replacement rule. The security
boundary therefore does not depend on transform-plugin registration order.

## Semantic correction before merge

The initial candidate used `requires_review` for findings or scanner failure.
That wording overstated runtime authority because the v1 boundary still transports
the content to the model and does not enforce quarantine or a human decision.

The contract therefore uses:

```text
review_recommended
```

and reserves a future `requires_review` state for a concrete consumer that
actually blocks or requires human review before the relevant effect proceeds.

Focused tests explicitly refuse `disposition="requires_review"` on this advisory
path so the semantic ceiling cannot silently regress.

## Tests

Focused tests cover:

- protected handler registration;
- clean scan remains untrusted data;
- prompt-injection finding recommends review;
- scanner unavailable recommends review;
- advisory paths do not claim `requires_review`;
- delimiter forgery neutralization;
- unrelated tools remain outside the Pantheon admission helper;
- the adapter calls Hermes' scanner with `scope="context"`.

## Distribution

Because the context bridge tree is digest-pinned, the candidate distribution lock
moves to the new exact tree digest. The distribution remains default-off and
does not gain task, Evidence, approval or execution authority.

## Open

Arbitrary local files read directly by Hermes remain an upstream/general
provenance question. This change closes the existing Pantheon Context Bridge path
only.

No model classifier such as Prompt Guard 2 is added in this slice. That remains a
possible calibrated second detector, not a prerequisite for the authority
boundary.
