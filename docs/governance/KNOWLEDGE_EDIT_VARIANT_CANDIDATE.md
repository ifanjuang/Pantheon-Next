# Knowledge Edit Variant Candidate

A Knowledge Edit Variant Candidate is an immutable proposed replacement for one exact text selection in one exact Knowledge revision.

It is transported as a typed `knowledge_edit_variant` item inside the canonical `Execution Result` envelope.

## Required scope

```text
request_ref
request_scope_digest
knowledge_ref
base_version
selection_start / selection_end
selected_text_digest
variant_label A or B
replacement_markdown + digest
```

The consumer must verify the complete scope against the retained edit request before projecting the candidate. A mismatch is a conflict; it is not silently adapted.

## Lifecycle boundary

```text
Execution Result stored
!= variant projected into a Knowledge edit request
!= variant selected
!= edit applied
!= Knowledge professionally validated
```

Hermes may produce the candidate. It cannot select, reject or apply it. Human selection remains distinct from the existing optimistic Knowledge revision transaction.

## Provenance

Optional source references and rationale remain candidate provenance. They do not become Evidence merely because they are attached to a proposal.

## Non-authority

A candidate cannot:

- authorize another task;
- mutate Knowledge;
- select itself;
- validate professional content;
- admit Evidence;
- promote memory.

The schema owner is `schemas/knowledge_edit_variant_candidate.schema.yaml`. The implementation candidate belongs in `pantheon-mvp`; Hermes remains the external producer of an admitted execution result.
