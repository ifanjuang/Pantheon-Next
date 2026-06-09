# Target Architecture — coherence compass

Status: validation-only — architecture-target and coherence map. It records a direction and orients the work; it promotes no candidate and adds no runtime.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

One compass for a coherent end-to-end system: the layers, what each external pattern fills, the gaps that keep the system from being real, and the sequence to close them. It exists so the project consolidates rather than absorbing more repositories.

## The coherent system (layers)

```text
SURFACE        OpenWebUI (cockpit) ............ displays gates, evidence, decisions
               Pantheon Control (eyes + hands)  install / update / preflight · DB + evidence-log view
                      |
LAW  (PDP)     PANTHEON NEXT ................. passport · gate · placement test ·
               Registre Probatoire · rites · roles · Uniform Capability Governance
                      |  decision: allow / block / needs-evidence / needs-approval
EXECUTION(PEP) HERMES ........................ runs capabilities under Task Contract;
               routes consequential effects to the gate · mem0 = its free memory
                      |
PROOF          Registre Probatoire  <- Evidence Packs  <- signed attestations
OBSERVABILITY  Langfuse (traces) --> Evidence Candidates
```

Coherence means a single law at the centre (the chokepoint); everything else is surface, execution or proof that connects to it. The model already exists in doctrine; what is missing is that it be real, not only documented.

Reality state per layer:

```text
LAW       documented; the chokepoint is named (UNIFORM_CAPABILITY_GOVERNANCE) but not enforced.
EXECUTION external (Hermès); routing to the gate is doctrine, not yet wired.
PROOF     Registre Probatoire is documented non-implemented (no registry, schema not hardened).
SURFACE   Pantheon Control is candidate docs; OpenWebUI integration is doctrine.
```

## The invariant

`UNIFORM_CAPABILITY_GOVERNANCE.md` is the keystone: one law, one passport per capability, no per-module rules, an unbypassable gate for consequential effects (PDP/PEP). Pantheon is master only insofar as the runtime routes consequential effects through the gate.

## Absorption map — which external pattern fills which slot

Distil the pattern and vocabulary; import no runtime.

| Slot | Pattern to distil | What is taken |
|---|---|---|
| The gate / decision | PDP/PEP (XACML) · Open Policy Agent / Gatekeeper | policy-as-data, decision-not-execution, admission required; a real implementation candidate for the policy plane |
| The proof (Registre) | in-toto / SLSA / Sigstore | signed attestation = "proof a step passed the gate"; per-step signatures |
| Control | Backstage | uniform-metadata catalogue + golden-path templates (presets) + health |
| Safe install / update | TUF | signed metadata for installing and updating the repos |
| Registre actor layer | directory-mcp | graph schema (Entities / Anchors / sourced Observations) |
| Conformance / regression | ASSERT | test that the executor honours the doctrine; keep a vertical green |
| Metacognition (rites) | self-inspect | deterministic `signal -> question` catalogue (already a candidate) |
| Skill admission | SkillsGate | admission discipline (already in CAPABILITY_REGISTRY) |
| On-the-fly composition | Case-Based Reasoning (retrieve/reuse/revise/retain) | the two gates (already in WORKFLOW_SCHEMA) |

Most of this is already distilled. The patterns still worth absorbing are the gate (OPA / PDP-PEP), the signed proof (in-toto / SLSA) and Control (Backstage). The rest is in place or candidate.

## Coherence gaps (ranked)

The system is coherent on paper but hollow in reality. The gaps that break coherence:

```text
1. The gate is not enforced. "Pantheon master" is doctrine, not mechanism:
   nothing routes Hermès' consequential effects through the policy check. (Gap #1.)
2. The Registre Probatoire does not exist (no registry; schema not hardened — E6 pending).
3. No read-only validator / Doctor checks (Phase 4): nothing verifies conformance.
4. No proven vertical end to end (the #76 example exists but is not run against schemas).
5. Unspecified links: Langfuse traces -> Evidence Candidates; attestation -> Evidence Pack.
```

## Sprawl to consolidate

```text
EVIDENCE_TOPOLOGY_*  (~8 files)  -> merge into one document with sections.
PANTHEON_CONTROL_*   family       -> one boundary document (decision D1 = keep here, slim).
reference_reviews                 -> freeze adding more; the absorption map is enough.
```

## Sequence to coherence

```text
0. Land the keystone (the named chokepoint) and its cross-references -> the LAW is clear.
1. Make the chokepoint explicit: Hermès asks the policy check before any consequential
   effect (HERMES_INTEGRATION / REQUEST_LIFECYCLE). Closes Gap #1 in doctrine.
2. Harden the spine: the E0-E4 / V0-V4 / C0-C5 scales, the passport and the Registre
   (E6) as schemas, plus a read-only validator.
3. Wire proof + observability: attestation -> Evidence Pack; Langfuse -> Evidence Candidate.
4. Prove ONE vertical: the #76 example run by the executor against the schemas, kept
   green by an ASSERT-style regression. This is what makes the system coherent AND real.
5. Consolidate the families; Control stays a minimal Backstage-like surface.
```

## The one rule of coherence

```text
The system is coherent when a single vertical really passes through the gate,
leaves a proof, and stays green.
```

Coherence will not come from more doctrine or more absorbed repositories — the model and the patterns are already right. It comes from three moves: name and enforce the chokepoint, harden the spine into something executable, and prove one vertical.

## Boundary

Direction record only. No runtime, scheduler, queue, provider router, policy engine, installer, MCP host or protected-path change inside Pantheon Next. Enforcement and execution live outside, in the runtime honouring the gate. This document maps the target; it instantiates none of it.
