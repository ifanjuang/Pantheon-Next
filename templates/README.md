# Templates

Status: non-executable template scaffold.

This directory contains declarative templates for future OpenWebUI, Hermes, Langflow, Langfuse and GraphRAG integration work.

The files in this directory are not runtime configuration.

They do not install tools, skills, Functions, Pipes, Filters, Actions, Pipelines, flows, traces, graphs or deployment artifacts.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Templates make future integration surfaces explicit before implementation begins.

They help preserve capability placement, prompt placement and bridge boundaries.

## Current template groups

```text
openwebui/   cockpit templates for thin Actions, Filters and model profiles
hermes/      execution handoff and skill candidate templates
langflow/    deterministic preparation flow templates
langfuse/    trace metadata templates
graphrag/    provenance graph templates
```

## Rule

A template is a candidate.

A template is not implementation.

A template must not be described as installed, deployed or executed.
