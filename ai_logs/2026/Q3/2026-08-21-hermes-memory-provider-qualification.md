# 2026-08-21 — Hermes runtime-memory provider qualification

Status: dated runtime qualification trace — reconciled with current Pantheon Next doctrine on 2026-08-24.

Boundary profile: `external_reference_review`.

## Objective

Record the observed Hermes runtime-memory qualification without creating a Pantheon memory subsystem, changing a Capability Slot binding, or collapsing conversational memory and workspace retrieval into one responsibility.

Current doctrine remains authoritative:

- `docs/governance/MEMORY.md` owns the distinction between Hermès runtime state and the Registre Probatoire;
- `docs/governance/HERMES_INTEGRATION.md` owns the Hermes/Pantheon execution boundary;
- `docs/governance/HERMES_CAPABILITY_BINDINGS.md` owns candidate binding posture;
- #659 owns Hindsight durable-ingestion hardening;
- #660 owns Obsidian/LiveSync/CouchDB/NAS-mirror synchronization qualification.

This file is therefore an implementation observation, not a new doctrine or provider registry.

## Observed runtime result

The tested Hermes deployment used Mnemosyne for fluid runtime memory.

Observed package/runtime identities recorded during the qualification:

```text
mnemosyne-memory = 3.15.1
mnemosyne-hermes = 0.5.0
Python wrapper   = 3.12.14
```

Observed placement:

```text
Hermes
  -> memory.provider: mnemosyne
  -> persistent Mnemosyne data under /opt/data
```

The qualification branch recorded the Mnemosyne database at:

```text
/opt/data/mnemosyne/data/mnemosyne.db
```

and the wrapper environment under:

```text
/opt/data/.mnemosyne/venv
```

These paths are deployment observations. They are not Pantheon-governed identities and may change with a future Hermes deployment.

## Functional observation

A controlled record was written through the Hermes/Mnemosyne memory path:

```text
content: TEST-MNEMOSYNE-9381
scope: global
returned id: 5d18b47ac7826098
```

The same record was returned by explicit recall and was recalled from a fresh Hermes session.

The observed path was therefore:

```text
Hermes remember
-> Mnemosyne runtime memory
-> persistent storage
-> new Hermes session
-> explicit recall
```

This demonstrates cross-session runtime recall for that tested configuration only.

It does not establish truth, Evidence, professional validity, Pantheon persistence, or a governed memory binding.

```text
remembered != true
recalled != validated
runtime persistence != Registre Probatoire
runtime success != Evidence
```

## Configuration finding

During qualification, an optional Hermes provider setting had been serialized as:

```yaml
tools: None
```

That prevented reliable explicit-tool initialization. Removing the unnecessary override and allowing the provider defaults restored the explicit memory-tool surface in the tested configuration.

Relevant observed settings at that checkpoint included:

```text
default_scope: global
sync_roles: [user]
auto_sleep: true
sleep_threshold: 50
profile_isolation: false
shared_surface_read: false
```

These remain runtime configuration observations, not Pantheon doctrine.

## Relationship to Hindsight

Hindsight is not collapsed into Mnemosyne.

The current converged responsibility split is:

```text
Mnemosyne
= fluid Hermes runtime / conversational memory

Hindsight
= derived workspace/document retrieval from intentional sources

Pantheon
= governance, provenance, authorization, Evidence and Registre Probatoire
```

Hindsight remains separately queried through bounded retrieval surfaces. Current #659 further constrains the durable topology so that Obsidian-derived Hindsight banks are produced through the qualified file-ingestion path and consumed through bounded read/recall surfaces.

The tested Mnemosyne record was not expected to appear in Hindsight. Lack of duplication across those paths is desirable because they serve different responsibilities.

```text
Mnemosyne recall != Hindsight retrieval
Hindsight retrieval != fluid conversation memory
memory != Evidence
```

## Relationship to `external_runtime_memory`

This observed Hermes configuration does **not** bind Pantheon's `external_runtime_memory` Capability Slot.

The current registry remains authoritative and keeps that slot `unbound` for Pantheon. Candidate ordering, sandbox posture and future provider comparisons belong in `HERMES_CAPABILITY_BINDINGS.md`, not in this dated trace.

Therefore:

```text
Hermes memory.provider = mnemosyne
!= Pantheon CapabilityBinding activation
!= Pantheon dependency adoption
!= provider authority
```

## Provider comparisons

The original qualification work also explored alternatives including Mem0, TencentDB Agent Memory and iai-pme.

Those comparisons are intentionally not promoted here into a second provider registry. Current candidate posture and the results of the broader #655 campaign belong to `HERMES_CAPABILITY_BINDINGS.md` and the relevant qualification issues.

The durable conclusion from this trace is narrower:

```text
observed Hermes fluid-memory path -> Mnemosyne worked across sessions
Hindsight replacement             -> no
second concurrent fluid provider  -> no demonstrated need
Pantheon memory subsystem         -> no
Pantheon authority change         -> none
```

## Re-evaluation triggers

Re-run runtime qualification when any of the following materially changes:

- Hermes changes its memory-provider contract;
- Mnemosyne changes storage or runtime requirements;
- cross-session recall or persistence becomes unreliable;
- a different provider is actually selected for the Hermes deployment;
- Hindsight begins to overlap the same fluid conversational-memory responsibility;
- multi-user/profile isolation becomes a demonstrated requirement;
- the host/runtime topology materially changes.

A provider change is an external runtime qualification event by default. It requires a Pantheon kernel change only if it exposes a genuinely missing provider-agnostic governance distinction.

## Final classification

```text
Observed on 2026-08-21:
  Hermes fluid runtime memory -> Mnemosyne functional in tested deployment

Current governance interpretation:
  Pantheon runtime-memory owner -> none
  external_runtime_memory slot  -> unbound
  Hindsight role                -> separate derived workspace/document retrieval
  Registre Probatoire           -> governed evidence path, unchanged
```

This checkpoint is closed as a dated runtime observation. #659 remains the active Hindsight hardening/ingestion qualification, and provider selection may be requalified without changing Pantheon doctrine.