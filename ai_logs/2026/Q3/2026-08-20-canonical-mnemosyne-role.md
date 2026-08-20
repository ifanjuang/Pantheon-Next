# Canonical Mnemosyne Role convergence

Date: 2026-08-20

Status: implementation complete; final log-only head awaiting exact-head CI before merge.

## Objective

Canonize `MNEMOSYNE` as a Pantheon governance Role for memory continuity without creating a memory engine, search runtime, provider binding or automatic memory-promotion path.

## Repository state before change

Base:

```text
main@adfe2bb93aedca64351633a6bb78df23e57ac3fc
```

That commit is the squash merge of PR #680, the public AI-literacy explainer.

Observed before modification:

- `docs/governance/AGENTS.md` was canonical and contained seven Roles;
- `VISUAL_LANGUAGE.md` and `NARRATIVE.md` already used Mnemosyne as a continuity/archive figure;
- candidate `docs/domain-packs/architecture/ROLE_FACETS.md` already gave Mnemosyne a distinct memory jurisdiction: history, previous decisions, duplicates, stale recall, latest-known state and memory-promotion prudence;
- `GOVERNANCE_COLLEGE.md` already distinguished being well sourced from being well remembered;
- `KNOWLEDGE_INGESTION_AND_MEMORY.md` already required scope, source, version/chronology and review before memory activation or promotion;
- the schemas repeated the seven-role enum inline, while `.github/scripts/check_schema_vocabulary.py` claimed Pantheon Roles were shared vocabulary but did not yet check that vocabulary;
- seven Hermes role-aligned profile folders existed; no dedicated Mnemosyne profile existed;
- an external memory product/provider named `Mnemosyne` also appears in candidate binding reviews and is a separate identity.

## Decision

`MNEMOSYNE` is promoted to the canonical Pantheon Role registry with this bounded responsibility:

```text
memory continuity
historical retrieval framing
current-state / index / date / version / supersession review for reuse
retention-placement proposals
```

Operational interpretation:

```text
where to search
-> relevant memory domain, dossier, corpus or governed record

how to search
-> exact terms, semantic proximity, chronology or declared relations

what state may be reused
-> duplicate / stale / index / date / version / supersession review

where a retained item may belong
-> session / Project / Agency / Sandbox / archive / Register Candidate
```

## Responsibility boundaries

`ARGOS` remains the source/evidence viewpoint:

```text
What is this source?
Where did it come from?
What does it support?
What evidence is missing?
```

`MNEMOSYNE` carries the continuity viewpoint:

```text
Where in prior context should we look?
Which historical state is being reused?
Which index/version is current for this memory question?
Is the recalled item duplicated, stale or superseded?
Where should retention be proposed?
```

The same date or version may concern both Roles for different reasons. A newer remembered record is not automatically stronger evidence.

`ZEUS` retains procedural/status arbitration.
`THEMIS` retains risk and approval-boundary review.
The human retains consequential decisions and required durable-memory approval.

## Execution boundary

Mnemosyne is a governance Role, not an executor.

The actual retrieval or tool call remains external execution under an admitted Task Contract.

This change deliberately does **not** create:

- `hermes/profiles/mnemosyne`;
- a `mnemosyne-agent`;
- a vector database;
- a memory provider;
- a retrieval engine;
- a scheduler or queue;
- an automatic archive process;
- an automatic memory promotion path.

The absence of a one-to-one Hermes profile for every Pantheon Role is documented explicitly.

## External-product name collision

The canonical Pantheon Role `MNEMOSYNE` and any third-party memory product/provider called `Mnemosyne` are separate identities.

```text
Role activation does not select a provider.
Provider availability does not activate Role authority.
```

## Schema convergence

`schemas/shared_defs.schema.yaml` now declares the canonical `pantheon_role` vocabulary alongside `scope_type`.

The canonical role values are:

```text
ATHENA
ARGOS
THEMIS
APOLLO
ZEUS
IRIS
HEPHAISTOS
MNEMOSYNE
```

The general Role enums in these schemas are aligned:

- `task_contract.schema.yaml`;
- `role_signal.schema.yaml`;
- `workflow_manifest.schema.yaml`;
- `skill_manifest.schema.yaml`.

Specialized single-responsibility fields remain specialized, notably:

```text
workflow governed_composition.forged_by = HEPHAISTOS
workflow pre_execution_eligibility.arbiter = ZEUS
```

`.github/scripts/check_schema_vocabulary.py` now treats `Pantheon Role` as canonical shared vocabulary so future copied enums cannot silently remain on an older role set.

The Role Signal example exercises a `MNEMOSYNE -> ARGOS` version-review consultation.

## Doctrine convergence

Updated owners/support include:

- `docs/governance/AGENTS.md`;
- `docs/governance/GOVERNANCE_COLLEGE.md`;
- `docs/governance/ROLE_SIGNALS.md`;
- `docs/governance/ROLE_ACTIVATION.md`;
- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`;
- `docs/governance/EDITORIAL_LANGUAGE.md`;
- `schemas/README.md`;
- Hermes adapter/profile documentation.

## Public projection

`docs/comprendre.html` and `docs/understand.html` now present the canonical eight-Role model.

The public explanation keeps the practical distinction:

```text
Argos -> value of the source
Mnemosyne -> continuity, current historical state, memory placement
executor -> performs the actual search
human -> decides consequential retention when required
```

Synthetic examples remain `LIA21`, `SOL14`, `Mme. C` only.

## Verification record

PR #682 was initially opened on head `da8d3dab8e2565ffc0a69a32104d8a2d50e1fd21`.

The first Governance CI attempt stopped before schema validation because the PR body did not yet include the repository's required semantic-change context sections. The PR body was corrected. A manual rerun still reused the original GitHub pull-request event payload, so it repeated that same documentary failure; this was not a schema or runtime failure.

A new synchronize event was then created on head:

```text
4e87ef41691c69292737391fe11e8a5e859c9cd3
```

On that exact head:

```text
Role / Rite / governed-Space change context — success
Canonical schema vocabulary consistency — success
Register instance + cascade rule validation — success
Vertical slice validation — success
Architecture project understanding referential integrity — success
mcp-server module tests — success
Packaging and release contract — success
Governance CI — success
Obsolete Authority Consistency — success
```

No missed general seven-role schema consumer was detected by the strengthened vocabulary check.

This final log-only update creates one last branch head. No doctrine, schema, runtime or public-page semantics change after the verified `4e87ef4...` head. The resulting final head must nevertheless pass the exact same PR checks before merge.

## Done criteria

The subject is complete only when:

- `MNEMOSYNE` is canonical in `AGENTS.md`;
- every general machine Role enum accepts the same eight-value set;
- CI enforces that set against future drift;
- no dedicated Hermes profile or memory runtime has been created by implication;
- public and internal doctrine no longer describe Mnemosyne as non-canonical;
- exact-head CI is green;
- PR #682 is merged and `main` is rechecked.
