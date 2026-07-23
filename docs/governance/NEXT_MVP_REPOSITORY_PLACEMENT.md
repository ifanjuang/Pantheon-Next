# Pantheon Next / Pantheon MVP — repository placement boundary

Status: **candidate support decision — human direction recorded 2026-07-23**.

This document clarifies where artifacts belong after the executable MVP and cockpit moved to the sibling repository `ifanjuang/pantheon-mvp`.

It does not install, activate, execute, approve, migrate professional data or create a deployment runtime.

## Core split

```text
Pantheon Next defines what must be true and how it is checked.
pantheon-mvp implements and demonstrates one external candidate binding.
A private deployment layer configures one real environment.
Private governed storage holds real professional data.
```

## External consumption contract

An external candidate may consume a small, explicit subset of Pantheon Next governance artifacts as a read-only vendored snapshot.

```text
source of governance      = Pantheon Next
external consumer         = pantheon-mvp or another reviewed candidate
allowed direction         = consumer -> Pantheon Next
reverse dependency        = forbidden
consumed artifacts        = explicit manifest
source revision           = exact pinned commit
conflict or divergence    = Pantheon Next source prevails
drift detection owner     = external consumer
correction                = reviewed re-vendoring change
silent or automatic sync  = forbidden
```

The consumer may detect and report drift, but it must not silently rewrite its copy or treat a green comparison as adoption, activation or professional authorization. Pantheon Next does not monitor, update or operate the external consumer.

## Pantheon Next retains

Pantheon Next retains artifacts whose primary purpose is governance or conformance:

- doctrine, vocabulary, roles, rites, gates and status rules;
- schemas and validation contracts;
- read-only validators and policy/preflight projections;
- positive and negative conformance fixtures;
- expected validation reports;
- capability passports, Task Contract templates and handoff contracts;
- declarative Hermes and OpenWebUI templates without executable adapter code;
- governance-only Card Stack visual grammar prototypes;
- authority indexes, status maps and intervention traces.

A fixture remains in Pantheon Next when its purpose is to prove that a contract accepts or refuses a bounded structure.

## pantheon-mvp receives

`pantheon-mvp` owns artifacts whose primary purpose is execution, product demonstration or runtime integration:

- cockpit HTML, CSS, JavaScript and renderer code;
- synthetic projects, documents, Knowledge Items and Work Issues displayed by the cockpit;
- fictional dossier corpora used by ingestion or retrieval;
- executable scenario runners and runtime adapters;
- OpenWebUI functions, tools, pipes or actions implemented as code;
- Hermes-side executable adapters;
- runtime-return fixtures and integration recordings;
- browser, API, database and end-to-end integration tests;
- local demo configuration and product screenshots.

A fixture belongs in `pantheon-mvp` when it feeds an executable flow, a product screen or an integration test.

## Delete instead of migrate

An artifact is removed from the working tree, rather than migrated, when it is:

- superseded by the current cockpit or Card Stack grammar;
- an abandoned intermediate mockup;
- unused by active documentation, conformance or tests;
- a duplicate renderer or duplicate data fixture;
- useful only as historical context already preserved by Git and `ai_logs/`.

```text
contract value -> keep in Next
product or runtime value -> move to MVP
historical value only -> remove; Git history remains
```

## Data boundary

Real client documents, plans, contractual files, standards corpora and professional Knowledge do not belong in either public repository.

```text
public repositories -> code, contracts, synthetic fixtures, qualified metadata
private deployment   -> environment-specific configuration and secret references
private storage      -> real sources, derived representations and governed records
secret manager       -> credentials and keys
```

Copyrighted standards or contractual corpora may be represented by synthetic metadata and source manifests. Their full content remains outside Git unless licence and disclosure are explicitly qualified.

## Deployment separation

A future private deployment repository or equivalent operator-controlled configuration layer may contain:

- pinned repository revisions;
- Compose or Portainer configuration;
- reverse-proxy and network configuration;
- storage mount declarations;
- backup, health and rollback procedures;
- references to secrets stored elsewhere.

That layer remains configuration, not an automatic installer, scheduler, provider router, approval engine or Pantheon runtime.

## Non-equivalences

```text
copied != adopted
installed != approved
healthy != safe
runtime fixture != Evidence
public demo != production deployment
binding selected != dependency adopted
update available != update authorized
drift detected != drift corrected
green comparison != professional authorization
```

## Migration rule

Every cross-repository migration records:

- source repository and path;
- destination repository and path;
- exact source and destination revisions;
- whether the artifact was copied, transformed or deleted;
- whether incoming references were updated;
- whether adoption or activation remains absent.

Pantheon governs the classification. The external repository carries the implementation. OpenWebUI exposes the operational surface. Hermes performs authorized work. The human approves consequential migration, adoption and activation.
