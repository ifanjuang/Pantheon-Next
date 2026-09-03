# Authority topology convergence before temporal ProjectClaim work

Date: 2026-09-03

Status: implemented on candidate branch — CI/review pending.
Boundary profile: bounded_governance_support_change.

## Objective

Clarify Pantheon's existing ownership model before adding temporal ProjectClaim,
structured derivation provenance, conflict candidates or governed entity
resolution.

The change does not introduce a new authority. It makes existing responsibilities
more explicit and machine-checkable.

## Observed repository state

Base commit:

```text
Pantheon-Next/main
= 07f46ac3d3999860c123943636d03f154e7f1cba
```

This base is the merge of PR #943, which separated direct human governed effects
from delegated runtime work.

Current observations before this slice:

- `AUTHORITY_INDEX.md` already owns repository authority classes and promotion
  rules;
- `MODULES.md` already owns the governance-area navigation map, but its areas
  were presented as one flat table;
- `PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json` already separated semantic,
  implementation, runtime and projection ownership;
- that registry still named `Cockpit/OpenWebUI` as a current logical owner even
  though active doctrine had already retired/refused OpenWebUI as a target owner;
- the registry did not distinguish the implementation path that changes governed
  state from the technical owner that persists it;
- the Architecture Audit deliberately consumes an independently pinned registry
  snapshot, so a candidate registry change must not rewrite its own merge-gating
  rule in the same change.

A historical branch named `codex/close-current-authority-baseline` was checked
before work. Its only unique commit modified `check_index_coverage.py`; it did not
contain this topology convergence.

No open PR covered authority topology, ProjectClaim temporal semantics,
structured provenance, conflict detection or entity resolution at the start of
this slice.

## Scope

Changed:

- `docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json`;
- `docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP.md`;
- `docs/governance/MODULES.md`;
- `tests/test_system_ownership_registry.py`;
- this log.

Deliberately not changed:

- `AUTHORITY_INDEX.md`;
- canonical Evidence, approval, identity or scope doctrine;
- schemas or PostgreSQL migrations;
- `implementation/` runtime or persistence code;
- PDP/PEP behavior;
- the independently pinned Architecture Audit authority snapshot;
- ProjectClaim temporal semantics or derivation provenance.

## Convergence

### 1. Registry revision 4

The machine registry now separates six dimensions:

```text
semantic_owner
implementation_owner
transition_owner
persistence_owner
runtime_owner
projection_owner
```

The distinction is responsibility-based:

```text
transition owner != decision authority
persistence owner != truth authority
runtime owner != Evidence authority
projection owner != persistence owner
projection owner != authorization authority
```

`transition_owner` and `persistence_owner` are additive. The existing Architecture
Audit parser may ignore them until separately extended; current repository tests
already validate them so they cannot silently drift.

### 2. Current owner identities

The current logical owner set becomes:

```text
Pantheon governance
Pantheon implementation
Hermes/external runtime
Pantheon Cockpit
```

The composite owner identity `Cockpit/OpenWebUI` is retired from current machine
ownership. This does not erase historical OpenWebUI provenance.

### 3. Core authority envelopes

Five concept families required by the next roadmap stages now carry a common
explicit state envelope:

```text
ProjectClaim
Evidence
Document Source
Governed decision
Governed identity
```

For these concepts:

```text
semantic_owner     = Pantheon governance
implementation_owner = Pantheon implementation
transition_owner   = Pantheon implementation
persistence_owner  = Pantheon implementation
projection_owner   = Pantheon Cockpit
runtime_owner      = absent
```

The common owner identity for implementation/transition/persistence does not
collapse the dimensions. It records that the same bounded implementation zone
currently performs several distinct technical responsibilities.

### 4. MODULES navigation hierarchy

`MODULES.md` keeps every existing governance responsibility but groups the map
into five navigation families:

```text
A. Governance Kernel
B. Governed State and Professional Semantics
C. Admission and Consequential Effects
D. Execution and Integration
E. Interaction, Projection and Workspace
```

These are navigation families, not new modules or authorities.

The document also states the division of labor explicitly:

```text
AUTHORITY_INDEX
!= system ownership registry
!= module navigation map
```

## Tests

`tests/test_system_ownership_registry.py` now checks:

- revision 4 and the exact current logical owner set;
- no active `Cockpit/OpenWebUI`, repository-name or former-MVP owner identities;
- every declared owner dimension resolves to a known logical owner;
- no new `*_owner` spelling/dimension can appear without a test change;
- the five core governed-state concepts carry the required authority envelope;
- projection and persistence remain separately declared dimensions;
- core non-equivalence rules are present in the registry.

## Architecture Audit pin

The Architecture Audit currently uses an independently pinned snapshot at:

```text
5ae389d1d66791fa3523504f75a133b4b709f79a
```

This slice intentionally does not update that pin.

Expected behavior on the candidate PR:

```text
current candidate registry != pinned audit registry
-> drift reported
-> existing merge-gating rules unchanged
```

After revision 4 is accepted and merged, moving the audit pin is a separate,
reviewable micro-change.

## Boundary

```text
ownership map != authority promotion
same implementation owner != same authority dimension
stored != governed truth
projection != persistence
transition implemented != transition authorized
runtime success != authorization
folder != governed identity
```

## Next

After this topology slice is accepted, the next functional slice remains P1:
ProjectClaim temporal semantics and deterministic `known_as_of` / `valid_as_of`
reads. No universal Fact table or separate temporal authority is introduced by
this work.
