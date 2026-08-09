# Project Anatomy V0.2 match-application continuity

Date: 2026-08-09

## Objective

Restore the governed H2 write path after the executable Project Anatomy owner
migrated to V0.2, without reopening `stable_object.matches`, fabricating
historical provenance or creating another match authority.

## Repository state checked

- `pantheon-mvp` H1, H3 and H4 are merged; H4 is on `main` at `12f8da0`.
- the H2 `add_match_to_existing_object` chain remains executable for V0.1 owners.
- V0.2 migration deliberately closes that legacy carrier.
- `source_representation` and `relation_claim(identity.represents)` are the active
  canonical V0.2 carriers.
- no open PR, issue or active branch already implements this continuity.
- the executable Observation Bundle contract remains documented non-implemented.

## Decision

Retain the existing operation and authorization chain. A newly prepared command
records `target_model_version` and, for V0.2, carries the exact canonical effect:

```text
source_representation(proof_status = candidate)
-- relation_claim(identity.represents, proof_status = candidate) -->
existing stable_object
```

The server must build the source representation only from exact available source
provenance. For the first document-fragment path this means the persisted Document
Structure compilation, fragment, digests, locator, compiler version and observed
time. Missing exact provenance is a refusal, not a synthetic placeholder.

The target stable-object revision is checked but not incremented by V0.2
application because the canonical relation is a separate append-only claim. The
project owner revision and append-only application event do advance.

## Compatibility

Historical commands without `target_model_version` remain contract-readable.
V0.1 projects may continue to use the historical inline carrier until explicitly
migrated. Migration still creates no source representation or claim from old
inline matches.

## Boundaries

```text
new exact source provenance != historical provenance reconstructed
write authorized != write applied
relation candidate appended != identity professionally validated
relation candidate appended != source considered mapped
source representation stored != Evidence admitted
```

## Non-effects

- no new operation family;
- no fifth project-world primitive;
- no automatic stable-object creation;
- no Evidence, Decision, WorkIssue or ProjectClaim mutation;
- no direct Hermes or adapter write;
- no H5 adapter/runtime validation.
