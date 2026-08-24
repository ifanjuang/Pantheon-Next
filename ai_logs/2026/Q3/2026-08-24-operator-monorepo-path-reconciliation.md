# Operator monorepo path reconciliation

Date: 2026-08-24
Status: validation trace — no deployment, activation or authority transfer

## Objective

Reconcile Phase B, Portainer, Paperless and Hermes document-intake operator documentation with the post-import Pantheon Next monorepo without changing runtime behavior.

## Verified starting state

```text
Pantheon-Next/main = c0ff1183cfb504be66e9bcda6be0b4e21787027e
branch             = docs/reconcile-operator-monorepo-paths
```

The repository already contained and tested:

```text
compose.policy-api.yaml
implementation/compose.phase-b.yaml
implementation/compose.paperless.yaml
implementation/hermes/skills/pantheon-document-intake/
```

`implementation/tests/test_phase_b_compose.py` establishes that Paperless is not part of the core Compose file and is added through the second Compose overlay.

## Observed stale operator language

Current runbooks still contained pre-import instructions including:

- a second reviewed `pantheon-mvp` checkout/commit;
- `docker compose -f compose.phase-b.yaml --profile paperless up -d` even though the tested model uses a separate `compose.paperless.yaml` overlay;
- a Hermes skill source URL under the former `ifanjuang/pantheon-mvp` repository;
- current-owner wording that treated Pantheon adapter/gateway/observer code as an external sibling implementation.

These were current operational contradictions, not historical provenance.

## Convergence applied

The current operator model is:

```text
one reviewed Pantheon-Next revision
├── compose.policy-api.yaml
└── implementation/
    ├── compose.phase-b.yaml
    ├── compose.paperless.yaml        optional
    ├── mvp_vertical/                 candidate adapter/gateway/observer code
    └── hermes/skills/pantheon-document-intake/
```

Hermes and Paperless remain external runtimes. Pantheon governance and Pantheon implementation remain distinct responsibilities even though their source is co-located.

Historical former `pantheon-mvp` PR identifiers remain where they explain implementation lineage. They are no longer current source or owner instructions.

## Runtime-interface compatibility deliberately preserved

This tranche does not rename:

```text
MVP_*
mvp_vertical
pantheon-mvp image defaults
```

They remain active technical interfaces in current code/tests. Repository/owner convergence does not justify a runtime compatibility migration by itself.

## Regression guards

`tests/test_monorepo_placement_language.py` now verifies:

- documented Phase B/Paperless Compose files exist under `implementation/`;
- operator docs use those paths;
- deprecated `--profile paperless` does not return;
- the complete Hermes skill source exists under `implementation/hermes/skills/pantheon-document-intake/`;
- the installation URL uses a reviewed Pantheon Next commit;
- current doctrine no longer names `ifanjuang/pantheon-mvp` as the Pantheon adapter owner/source;
- historical/runtime compatibility names remain distinguishable from governed ownership.

## Separate next tranche

Hindsight/MCP/Obsidian optimization is deliberately separate and may start after this PR enters CI.

Fresh review on 2026-08-24 confirmed:

- #659 remains open for Hindsight durable-deployment hardening and single ingestion authority;
- #660 remains open for Obsidian synchronization qualification;
- the selected synchronization direction is Self-hosted LiveSync/CouchDB; Remotely Save is explicitly out of scope;
- Self-hosted LiveSync now includes an official headless CLI capable of CouchDB replication and filesystem mirroring;
- `hindsight-obsidian-sync` provides a separate headless Obsidian-vault ingestion path into Hindsight;
- #685 separately records Hermes runtime-memory provider qualification and must not be conflated with Hindsight knowledge retrieval.

Expected sequencing:

```text
#659 hardening / write-authority decision
-> revise #660 around Self-hosted LiveSync/CouchDB + headless filesystem mirror
-> qualify exactly one headless Obsidian -> Hindsight producer path
-> simplify Hermes MCP exposure to bounded read surfaces
-> only then broaden real IFJA data use
```

## Invariants

```text
repository != owner identity
folder/path != governed identity
co-location != authority transfer
compose present != deployed
installed != activated
runtime success != authorization
runtime success != Evidence
retrieved != truth
memory != Evidence
projection != persistence
```

## Done criteria

- operator and doctrine documents agree on one current monorepo source;
- commands point to existing files;
- historical provenance remains explicit;
- no runtime interface is renamed incidentally;
- repository CI passes on the final PR head;
- no review blocker remains.
