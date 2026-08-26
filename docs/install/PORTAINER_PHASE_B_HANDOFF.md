# Portainer Phase B — Historical Operator Handoff

Status: refused — superseded Portainer specialization retained temporarily for compatibility — refused.
Boundary profile: candidate_support_note.

This former Portainer specialization is no longer an installation authority. The current operator guidance is `COMMON_BASELINE_RUNBOOK.md`; Portainer is merely one possible operator tool.

OpenWebUI and Paperless are not target architecture dependencies.

## Historical implementation provenance

The old specialization referenced the co-located candidate composition:

```text
compose.policy-api.yaml
implementation/compose.phase-b.yaml
implementation/compose.paperless.yaml
```

`implementation/compose.paperless.yaml` remains a protected historical compatibility artifact pending the implementation cleanup slice. Its presence does not select or prefer Paperless.

The `MVP_*` names remain active runtime interfaces where protected implementation/tests still consume them. They are compatibility identifiers, not repository owners, architectural authorities or evidence that the old stack remains selected.

```text
implementation path != governed identity
compose file present != service selected
runtime interface name != authority owner
```

## Current owner

Use `docs/install/COMMON_BASELINE_RUNBOOK.md` for the selected Hermes-centered baseline, regardless of whether the human operator applies it through CLI tooling, Portainer or another infrastructure surface.

Current responsibility split:

```text
Hermes Web/dashboard -> runtime interaction
Hermes Agent         -> execution
Pantheon Cockpit     -> governed projections
Pantheon Next        -> governance/admission semantics
Obsidian             -> human Markdown workspace
operator             -> infrastructure deployment and secrets
```

No Portainer-specific layer acquires Pantheon authority.

## Convergence path

This file remains only until protected placement/route tests and the residual OpenWebUI/Paperless implementation are generalized or removed. Then delete this pointer; Git history is sufficient provenance.
