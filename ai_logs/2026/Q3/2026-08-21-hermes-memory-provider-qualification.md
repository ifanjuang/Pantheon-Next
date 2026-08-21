# 2026-08-21 — Hermes memory provider qualification

Status: validated runtime qualification — dated implementation choice, not Pantheon dependency.

Boundary profile: `external_reference_review`.

## Objective

Record the 2026-08-21 qualification of Hermes runtime-memory providers without creating a Pantheon memory runtime, provider router, vector-store policy or new governance owner.

The durable boundary already exists in `docs/governance/MEMORY.md` and `docs/governance/HERMES_INTEGRATION.md`:

```text
Hermes runtime memory -> external runtime state, no authority
Pantheon -> evidence, certainty, scope, approvals and Registre Probatoire
```

Therefore this file is a dated qualification trace. Provider choice remains replaceable and belongs to Hermes deployment/runtime configuration.

## Plan and scope

The qualification compared the currently relevant Hermes memory-provider candidates against the actual NAS deployment and the existing Hindsight MCP path.

Criteria:

- direct Hermes integration;
- local/self-hosted operation;
- persistence across Hermes sessions;
- explicit remember/recall behavior;
- operational complexity on the NAS;
- overlap with Hindsight;
- provenance and truth-status separation;
- recent defects and maintenance activity;
- rollback/replacement cost.

No external benchmark was treated as directly comparable to the local Hermes deployment. Repository reports, releases and issues were used as qualification signals, not as proof of local behavior.

## Observed target architecture

At qualification time the intended split was:

```text
Hermes
├── Mnemosyne -> fluid runtime memory and conversational continuity
└── Hindsight MCP -> separately queried knowledge / Obsidian-oriented banks

Pantheon
└── Registre Probatoire -> governed evidence, certainty, status and approval
```

The split is deliberate:

```text
remembered != true
retrieved != validated
runtime_success != Evidence
memory provider selected != Pantheon dependency adopted
```

Hermes may use Mnemosyne and Hindsight in the same task. Their provenance must remain distinguishable. Neither source gains authority merely because recall succeeded.

## Mnemosyne qualification

Observed installed versions on 2026-08-21:

```text
mnemosyne-memory: 3.15.1
mnemosyne-hermes: 0.5.0
Python wrapper: 3.12.14
```

Observed deployment:

```text
Hermes container persistent root: /opt/data
Mnemosyne wrapper venv: /opt/data/.mnemosyne/venv
Mnemosyne DB observed by CLI: /opt/data/mnemosyne/data/mnemosyne.db
Hermes memory.provider: mnemosyne
provider status: installed / available / active
```

The wrapper venv is intentionally outside Hermes' image-owned `/opt/hermes/.venv`, reducing coupling to container rebuilds.

### Local functional evidence

A controlled memory was written through the Hermes Mnemosyne tool:

```text
content: TEST-MNEMOSYNE-9381
scope: global
returned id: 5d18b47ac7826098
```

Immediate explicit `Mnemosyne Recall` returned the same memory.

A fresh Hermes session then recalled the same record with:

```text
ID: 5d18b47ac7826098
Content: TEST-MNEMOSYNE-9381
Source: user
Tier: working
Scope: global
Veracity: unknown
keyword_score: 1.0
fts_score: 1.0
```

This validates the tested path:

```text
Hermes remember
-> Mnemosyne working memory
-> persistent global scope
-> new Hermes session
-> explicit recall
```

The CLI simultaneously reported working-memory entries while episodic memory remained at zero. This was not treated as a failure: the tested records had not reached the configured auto-sleep threshold.

### Configuration correction observed during qualification

The Dashboard had serialized the optional tool configuration as:

```yaml
tools: None
```

This prevented reliable explicit-tool initialization. Removing that override and restarting Hermes restored the provider to its default tool exposure. The validated configuration therefore leaves the optional `tools` override absent unless an explicit allow-list is required.

Current relevant posture:

```text
default_scope: global
sync_roles: [user]
auto_sleep: true
sleep_threshold: 50
profile_isolation: false
shared_surface_read: false
```

These are runtime settings, not Pantheon doctrine.

## Hindsight relationship

Hindsight remains a separate MCP-accessed knowledge/memory service. The qualification demonstrated that Hermes can call Mnemosyne and Hindsight tools within the same task.

A controlled Mnemosyne test record was not returned by Hindsight Agency recall, which is the desired non-duplication behavior for that test.

A search for `Pantheon` against the Hindsight `Agency` bank returned no results during the qualification. This establishes only that the queried bank/path did not return Pantheon material at that time. It does not establish that Hindsight as a whole lacks Pantheon knowledge; bank selection and indexed sources remain separate deployment concerns.

Hindsight must not be silently collapsed into Mnemosyne. The useful boundary is:

```text
Mnemosyne -> ambient/fluid Hermes runtime memory
Hindsight -> explicit knowledge retrieval from its configured banks/sources
```

## Mem0 comparison

Mem0 remains the primary fallback/reference alternative rather than an additional concurrent memory layer.

The Hermes provider supports hosted, self-hosted-server and OSS modes. OSS can introduce an LLM/embedder plus Qdrant or pgvector, while self-hosted server mode introduces a separate service. This is useful when a more independent or scalable memory service is required, but it adds moving parts relative to the validated Mnemosyne SQLite path.

Qualification result:

```text
maturity / ecosystem breadth -> Mem0 advantage
local Hermes simplicity -> Mnemosyne advantage
fit beside existing Hindsight -> Mnemosyne advantage
provider independence / scale-out -> Mem0 advantage
```

No Mem0 runtime was added because the current responsibility is already covered. Adding Mem0 beside Mnemosyne and Hindsight would create overlapping memory authorities and synchronization questions without a demonstrated need.

Mem0 is the first replacement candidate if Mnemosyne fails sustained reliability qualification or if requirements materially change toward an independent/scaled memory service.

## TencentDB Agent Memory comparison

TencentDB Agent Memory was not retained as the primary Hermes memory provider at this checkpoint.

Recent upstream reports reviewed during qualification included defects around capture completeness, retrieval thresholds/ranking and operational log growth. The project also exposes a broader architecture than required for the current Hermes runtime-memory responsibility.

Qualification result:

```text
capability breadth -> high
current required responsibility -> narrower
operational complexity -> higher than Mnemosyne
recent reliability signals -> require requalification before adoption
```

Tencent remains a candidate technology, not a Pantheon dependency and not a concurrent memory layer.

## iai-pme / IAI Personal Memory Engine

`iai-pme 3.0.6` was installed in an isolated Python 3.12 environment during exploration, but its doctor reported that the NAS host lacks AVX2 and therefore the native memory store cannot load on that host.

The Hermes capture hooks were not adopted as the active memory path. The candidate is rejected for this NAS target unless the hardware/runtime constraint changes.

```text
installed package != usable store
hook installed != memory provider adopted
```

## Decision

For the observed NAS/Hermes deployment on 2026-08-21:

```text
primary Hermes fluid memory -> Mnemosyne
knowledge / Obsidian retrieval -> Hindsight MCP
fallback/reference provider -> Mem0
TencentDB Agent Memory -> not retained; requalify if upstream/runtime conditions change
iai-pme -> unsuitable on current NAS because native store requires AVX2
```

Do not add Mem0 or Tencent concurrently merely because Hermes exposes those providers.

The convergence rule is one runtime-memory responsibility per active path, with Hindsight remaining a distinct explicit knowledge-retrieval path.

## Re-evaluation triggers

Re-run this qualification rather than relying on the dated provider choice when:

- Mnemosyne loses inter-session persistence or recall reliability in sustained use;
- Hermes materially changes its memory-provider contract;
- Mnemosyne changes storage/runtime requirements;
- Hindsight takes over the same ambient-memory responsibility, creating duplication;
- Mem0 materially simplifies its local Hermes deployment or becomes necessary for scale-out;
- Tencent resolves the reviewed reliability/operational issues and offers a demonstrated advantage for the actual requirement;
- the NAS hardware changes, especially AVX2 availability;
- a requirement appears for profile isolation, shared surfaces, multi-user tenancy or cross-host memory service.

## Result

```text
new Pantheon memory subsystem -> no
new provider router -> no
new canonical-memory concept -> no
Hermes runtime provider qualification -> Mnemosyne retained
Hindsight replacement -> no
Mem0/Tencent concurrent deployment -> no demonstrated need
Pantheon authority change -> none
```

The subject is closed for the 2026-08-21 checkpoint. Future provider changes are runtime qualification events unless they reveal a missing provider-agnostic governance distinction.