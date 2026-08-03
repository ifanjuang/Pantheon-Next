# Cockpit loader request baseline

Date: 2026-08-04

Status: measured implementation baseline — non-authoritative.

## Scenario

The reproducible Node harness executes one representative Cockpit sequence against the real `cockpit_data_loader.js` with a deterministic fake transport:

```text
load Agency project list once
load Project schema three times for the same token
load one Project bundle once
```

The Project bundle currently reads five independent bounded resources in parallel:

```text
Information
Documents
Knowledge
Work Issues
pending Project ChangeCandidates
```

## Baseline on main

Main commit before optimization: `89d95b4d2daf0cd49902ed4797cfa9a7cfada3dd`.

```json
{
  "total_requests": 9,
  "unique_paths": 7,
  "schema_requests": 3,
  "project_bundle_requests": 5
}
```

The measurement is produced by:

```text
tools/measure_cockpit_loader_requests.js
```

and locked by:

```text
tests/test_cockpit_loader_performance_baseline.py
```

## Interpretation

The five Project-bundle requests are already parallel and each represents a distinct server-owned read. This baseline does not justify combining them into a new backend model yet.

The repeated Project-schema request is redundant within one Cockpit loader session because the schema is server-authoritative but does not vary by selected project. A bounded promise cache keyed by read token is therefore the first optimization candidate.

## Target for the next PR

```text
same scenario
schema requests: 3 -> 1
total requests: 9 -> 7
Project bundle requests remain 5
public response payloads unchanged
failed schema request remains retryable
```

## Non-equivalences

```text
fewer requests != broader authority
client cache != source of truth
cached schema != authorization
parallel request success != coherent transaction
measurement improvement != permission to create a new backend ontology
```
