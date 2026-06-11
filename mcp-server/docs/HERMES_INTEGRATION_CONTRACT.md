# Hermes Integration Contract — MCP Policy Server

Status: implementation candidate — integration contract for the bounded `mcp-server/` module. Candidate until reviewed.

This contract describes how Hermes may call the Pantheon MCP Policy Server to frame work without Pantheon executing the work.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

The MCP Policy Server is read-only / validation / candidate-preparation only.

It may:

- classify a request on the K/V/C axes;
- validate a capability passport;
- prepare candidate skeletons for Task Contracts and Evidence Packs;
- run read-only doctor checks;
- return policy decisions as data.

It must not:

- execute business work;
- send externally;
- write files or state;
- approve a result;
- promote memory or write a Registre Probatoire entry;
- install, schedule, queue or route providers.

## Target sequence

```text
1. The user sends a request through OpenWebUI.
2. Hermes receives the request.
3. Hermes calls mcp.classify_request -> consequence K, verification V, ceiling C, gates.
4. Hermes calls mcp.prepare_task_contract_skeleton -> Task Contract candidate.
5. Hermes executes, outside Pantheon, only the work allowed by a reviewed contract.
6. Hermes calls mcp.prepare_evidence_pack_skeleton -> Evidence Pack candidate.
7. Hermes returns a candidate output in the expected envelope.
8. The human accepts, refuses, revises or escalates.
```

Step 5 is outside Pantheon. The MCP Policy Server does not perform it.

## Expected Hermes output envelope

```text
RESULT_CANDIDATE
EVIDENCE_PACK_CANDIDATE
STATUS                 # candidate | to_verify | blocked
SCOPE_USED
APPROVAL_NEEDED        # C0..C5
REGISTER_CANDIDATE     # proposed only, never promoted here
LIMITS_AND_UNCERTAINTIES
```

Allowed status language:

```text
candidate
requires approval
scope unclear
blocked pending evidence
human decision required
```

Forbidden status language:

```text
approved
validated truth
authorized action
safe to execute
```

## Compliance fixture

`mcp-server/fixtures/sequence_conformance.yaml` records a fictional request and the expected sequence:

```text
classify_request
prepare_task_contract_skeleton
prepare_evidence_pack_skeleton
external action refusal
```

The fixture verifies that the server prepares candidates and refusals only. It does not create a contract, approve an Evidence Pack or send anything.

## Final rule

```text
Hermes may ask the MCP server to check the frame.
Hermes performs the work outside Pantheon.
The MCP server prepares candidates.
The gate and the human decide.
```
