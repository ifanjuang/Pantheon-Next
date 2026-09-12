# Governed Hermes runtime-efficiency qualification

Status: qualification lab for Pantheon issue #1047. Not installed, activated, adopted or wired into any product/runtime path.

## Purpose

Measure whether the exact governed Hermes runtime used by Pantheon has a demonstrated efficiency problem before prototyping any SoL-inspired mechanism.

```text
recorded governed Hermes observation
            +
recorded candidate observation
            ↓
provider-neutral comparison
            ↓
quality/provenance gate first
            ↓
operational cost comparison second
            ↓
qualification decision only
```

This lab does not execute Hermes, install SoL-Pi, change Hermes configuration, select a model/provider, persist runtime state or create Pantheon authority.

## Current baseline

Opened from:

```text
Pantheon-Next main: 836219b7e9c271d64a4850bd2484d3767c56a38f
Pantheon deployment target: nousresearch/hermes-agent:v2026.8.31
reference project: NVlabs/SoL-Pi
issue: #1047
```

Revalidate those identities before a live qualification run. Repository state here is provenance, not proof of what is currently installed on the Linux node.

## Existing owners remain unchanged

```text
Pantheon Context Pack / scoped context = admitted working perimeter
Hermes                         = runtime execution mechanics
Hermes native compression     = runtime context hygiene
Pantheon Evidence owners      = Evidence semantics/admission
Pantheon Memory doctrine      = Registre boundary
human / existing gates        = consequential decision
```

No `efficiency engine`, `ObservationPack`, `DistilledContext`, reducer owner, memory owner, Evidence owner or Capability Slot is introduced.

## Comparison envelope

Each observation is a local JSON object consumed by `compare.py`.

Required identity fields:

```text
case_id
variant
runtime_identity
result_status
```

Identity fields to record when observable:

```text
model_identity
profile_identity
settings_digest
```

Operational metrics are optional; missing values are `null`, never zero by inference:

```text
input_tokens
output_tokens
llm_turns
tool_calls
elapsed_seconds
max_context_tokens
repeated_context_tokens
large_tool_result_count
large_tool_result_chars
```

Quality/provenance fields:

```text
source_recall_checks
source_recall_passes
required_quality_checks: {name: boolean}
retrieved_refs
admitted_refs
used_refs
notes
```

Opaque task-local refs are preferred. Do not commit client content or sensitive document locators merely to populate a lab fixture.

When lineage refs are recorded, all three sets must be present and the harness enforces:

```text
used ⊆ admitted ⊆ retrieved
```

## Result status

Accepted observation statuses are deliberately operational only:

```text
complete
partial
blocked
failed
unknown
```

They do not create Pantheon result validity, Evidence status or approval.

## Quality-first rule

The candidate cannot be preferred merely because it uses fewer tokens or fewer calls.

The harness rejects a candidate when it:

- fails required source-recall checks;
- fails an explicitly required quality/provenance check;
- returns `blocked` or `failed`;
- regresses a baseline source-recall perimeter that is directly comparable.

Unknown quality remains `unknown` and yields an inconclusive decision rather than a token-saving claim.

```text
fewer tokens != better result
summary != source
reduced context != Evidence
runtime success != result validity
```

## Comparability

An A/B pair must use the exact same `case_id` and different variant names.

A runtime identity mismatch blocks causal comparison. Known model/profile/settings mismatches also block comparison. Missing model/profile/settings identity is preserved as a warning rather than silently treated as equal.

This lets the first live qualification expose incomplete observability without fabricating parity.

## Cost comparison

For each known metric the harness reports:

```text
baseline
candidate
delta = candidate - baseline
percent_change when baseline != 0
```

Lower is treated as operationally cheaper for the listed cost metrics. There is deliberately no universal score or arbitrary token threshold.

Possible lab decisions:

```text
candidate_for_further_qualification
mixed_cost_tradeoff
no_measured_gain
reject_candidate
inconclusive
```

None means `adopted`.

## Representative live cases

Use the same model/profile/settings per A/B pair whenever technically possible.

### C1 — large admitted representation

Exercise a large admitted document/Knowledge representation, including the current scoped-context pressure/oversize boundary where relevant.

Goal: determine whether native Hermes/scoped-context handling is already sufficient before considering handle-based recall.

### C2 — large diagnostic/tool output

Use a long terminal, test or diagnostic result whose raw source remains locally recoverable.

Goal: measure whether repeated large observations materially dominate model context.

### C3 — edit/validate loop

Exercise several deterministic edit → validation cycles on disposable code/text fixtures.

Goal: measure whether LLM-turn overhead is material enough to justify an Action-Fusion-like runtime experiment.

### C4 — long IFJA source task

Use synthetic/non-sensitive IFJA-style material requiring project context, bounded memory/workspace retrieval, source checking and synthesis/calculation.

Goal: measure real professional-work context pressure rather than coding-only performance.

## Decision order after measurement

```text
native Hermes sufficient
→ stop; no new mechanism

large/repeated observation cost dominates
→ only then consider a bounded handle/exact-recall prototype

edit/validation turn cost dominates
→ only then consider Action-Fusion-like behavior

long diagnostic-log cost dominates
→ only then consider local provenance-preserving reduction

completed-step history dominates
→ only then consider additional compaction trigger logic
```

Prefer configuration or reuse of an existing Hermes mechanism before new runtime code.

## SoL-Pi boundary

SoL-Pi is reference material only. This lab does not depend on Pi or SoL-Pi packages.

If one mechanism is later justified, reimplement only the smallest required behavior through an exact, verified Hermes extension surface. Do not copy Pi's extension architecture into Pantheon.

Remote reducer/model use is outside this slice. Local-only is the default posture for any future diagnostic-log reduction experiment.

## Run locally

Prepare two JSON observations, then:

```bash
python implementation/labs/hermes_runtime_efficiency/compare.py baseline.json candidate.json
```

The output is a qualification report, not persisted governed state.

## Removal test

Removing these files restores prior behavior completely:

```text
implementation/labs/hermes_runtime_efficiency/
implementation/tests/test_hermes_runtime_efficiency_lab.py
.github/workflows/implementation-hermes-runtime-efficiency-qualification.yml
```

No product module imports this lab.

## Current status

Implemented in this slice:

- provider-neutral observation parser;
- `used ⊆ admitted ⊆ retrieved` validation when lineage is observed;
- identity/comparability checks;
- quality-before-cost comparison;
- unknown-metric preservation;
- regression tests and isolated CI lane.

Not yet performed:

- real Linux-node Hermes A/B runs;
- dominant-cost classification from real traces;
- any SoL-inspired prototype;
- any runtime/deployment change.

The lab remains open until issue #1047 records measured runs or closes with `native_sufficient` / `inconclusive` without adding architecture.
