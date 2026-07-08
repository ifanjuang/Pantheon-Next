# Templates

Status: non-executable template scaffold.

This directory contains declarative templates for future OpenWebUI, Hermes, Langflow, Langfuse, MCP policy, provenance / GraphRAG-support and prompt-template integration work.

The files in this directory are not runtime configuration.

They do not install tools, skills, Functions, Pipes, Filters, Actions, Pipelines, flows, traces, graphs, MCP servers, MCP clients, gateways or deployment artifacts.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Templates make future integration surfaces explicit before implementation begins.

They help preserve capability placement, prompt placement, policy-server and bridge boundaries.

`TEMPLATE_MODEL.md` defines the common discipline for reusable templates: input contract, source hierarchy, uncertainty handling, forbidden outputs, human validation and non-executable status.

## Registry

Use `TEMPLATE_REGISTRY.md` as the local registry of current template files and their non-executable status.

## Current template groups

```text
openwebui/        cockpit templates for thin Actions, Filters and model profiles
hermes/           execution handoff, return, run-manifest and skill candidate templates
langflow/         deterministic preparation flow templates
langfuse/         trace metadata templates
mcp               MCP capability passport and external tool review templates
provenance/       provenance / GraphRAG-support link templates
prompt_templates/ reusable non-executable professional prompt templates
```

## Rule

A template is a candidate.

A template is not implementation.

A template must not be described as installed, deployed or executed.

A prompt template may be inspired by abstract prompt architecture patterns, but it must not copy, ingest, vectorize or depend on leaked, proprietary or unqualified third-party prompt text.
