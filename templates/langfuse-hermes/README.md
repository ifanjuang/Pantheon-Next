# Langfuse / Hermes template pack

Status: template candidate — not installed, not production-ready, not authoritative.

This folder contains copy-and-adapt templates for a future Langfuse installation beside Hermes.

It does not deploy anything.

It does not contain secrets.

It does not create `operations/`, `platform/`, `.env`, schemas, tests, Dashboard runtime code or Hermes runtime code.

## Files

```text
docker-compose.langfuse.example.yml
langfuse.env.example
dashboard-module.langfuse.example.yaml
hermes-trace-metadata.example.yaml
```

## Intended first use

```text
1. copy these templates outside Pantheon or into an approved runtime repository;
2. check the current official Langfuse Docker Compose documentation;
3. replace all CHANGEME values with generated secrets outside Git;
4. run with synthetic traces only;
5. expose Dashboard link/status only;
6. do not emit client dossier traces before redaction and retention are reviewed.
```

## Boundary

```text
Langfuse observes.
Hermes executes.
Dashboard exposes.
Pantheon governs.
```

A Langfuse trace is not an Evidence Pack, approval, memory, proof or professional validation.
