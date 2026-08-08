# Document purpose-specific currentness convergence — 2026-08-08

## Trigger

The agency collaboration/version-intake work and executable A-stream exposed a conflict in the older candidate Proof Register model:

```text
document_family.current_authoritative_version_id
```

collapsed all professional uses into one persisted version while the newer convergence requires independent purposes such as latest received, consultation, contract and execution.

## Repository findings

- `DATA_PLATFORM_ARCHITECTURE.md` already names generic candidate `doc_documents` / `doc_document_versions` implementation families.
- `PROOF_REGISTER_IMPLEMENTATION_SPEC.md` already owns architecture-specific `document_family`, `indexed_document_version` and `version_event` concepts.
- `INDEX_EFFECT_MATRIX.md` already owns the closed professional effect-class vocabulary.
- `AGENCY_COLLABORATION_AND_VERSION_INTAKE_CONVERGENCE.md` requires purpose-specific calculated currentness and forbids filename/index order as authority.
- No open Pantheon-Next PR was found implementing a competing currentness contract.

## Convergence decision

Do not create a second document identity/version model.

```text
document_family
= architecture-domain semantics projected from the logical document owner

indexed_document_version
= architecture-domain projection of one exact professional revision

version_event
= append-only effect/status/authority history attached to that revision

currentness
= calculated read projection for one declared purpose
```

Remove the candidate universal `current_authoritative_version_id` field from `document_family`.

Add a read-only currentness projection contract with explicit `resolved / unresolved / conflicting` posture and disclosed basis.

No database, runtime, approval, Evidence, Proof entry or external action is implemented by this change.

## Boundaries

```text
latest received != professional authority
highest index != current authority
projection resolved != approval created
version event != proof entry
physical table name != semantic owner
unresolved != guessed
conflicting != arbitrarily selected
```

## Follow-up

Only after this contract is validated should `pantheon-mvp` implement a bounded version-effect/event layer and purpose-specific currentness resolver over the existing logical document revision owner candidate.