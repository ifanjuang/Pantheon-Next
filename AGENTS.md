# Pantheon Next — Agents

## Overview

Pantheon Next uses a structured set of agents inspired by Greek mythology.

Each agent has:

- a clear role
- defined responsibilities
- explicit limits

Agents must remain focused. No agent should become a monolithic general-purpose component.

---

# Control Agents

## ZEUS

Role: orchestration and arbitration.

Responsibilities:

- supervise workflow execution
- arbitrate between conflicting outputs
- trigger replanning when needed

Limits:

- does not execute tools
- does not produce domain content

---

## ATHENA

Role: planning and decomposition.

Responsibilities:

- classify user intent
- break tasks into subtasks
- propose execution plan

Limits:

- does not execute tools
- does not produce final output

---

## METIS

Role: deliberation.

Responsibilities:

- identify hypotheses
- surface uncertainty
- highlight conflicts
- recommend checks

Limits:

- does not produce final answers

---

## PROMETHEUS

Role: challenge and contradiction.

Responsibilities:

- detect weak reasoning
- identify unsupported claims
- preserve divergent views

Limits:

- should not block valid reasoning excessively

---

## THEMIS

Role: rules and compliance.

Responsibilities:

- enforce workflow rules
- validate policy constraints

Limits:

- does not evaluate factual correctness

---

## APOLLO

Role: validation and confidence.

Responsibilities:

- score confidence
- validate structure and coherence
- approve or reject output

Limits:

- depends on upstream quality

---

## HECATE

Role: uncertainty detection.

Responsibilities:

- detect missing information
- trigger clarification

Limits:

- does not produce answers

---

# Research Agents

## HERMES

Role: routing research.

Responsibilities:

- select data sources
- route queries to tools

---

## DEMETER

Role: data ingestion.

Responsibilities:

- fetch and normalize data

---

## ARGOS

Role: extraction.

Responsibilities:

- extract facts
- extract citations
- extract entities

Limits:

- no interpretation

---

## ARTEMIS

Role: filtering.

Responsibilities:

- remove irrelevant information

---

# Memory Agents

## HESTIA

Role: session memory.

---

## MNEMOSYNE

Role: knowledge memory.

---

## HADES

Role: deep memory.

---

# Output Agents

## KAIROS

Role: synthesis.

---

## DAEDALUS

Role: document construction.

---

## IRIS

Role: communication.

---

## HEPHAESTUS

Role: diagrams.

---

## APHRODITE

Role: presentation polish.

---

# System Agents

## ARES

Role: fast execution.

---

## POSEIDON

Role: flow control.

---

# Design Rules

- one role per agent
- no hidden responsibilities
- no agent should bypass policy checks
- no direct tool execution without runtime validation

---

# Goal

Agents must behave like a coordinated expert team where each role is explicit, controlled and testable.
