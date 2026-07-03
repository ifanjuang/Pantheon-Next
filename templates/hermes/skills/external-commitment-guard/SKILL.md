---
name: external-commitment-guard
description: Use before any draft (e.g. a MOA email) could leave the cockpit, to detect wording or actions that would imply agency approval, a client instruction or an external send, and to open the User Decision Gate. Authorizes nothing by itself.
metadata:
  owner_layer: hermes
  status: candidate_template_only
  pantheon_capability_id: external-commitment-guard
  governed_by: docs/examples/vertical_devis_reprise/workflow_manifest.devis-reprise.yaml
  upstream: agentskills.io SKILL.md standard; loadable by Hermes Agent (NousResearch) >= 0.18
---

# External commitment guard (governed candidate)

Non-executable candidate skill in the `agentskills.io` / `SKILL.md` standard. It opens
a gate; it never sends. Pantheon governs; Hermes executes outside the repo.

## When to use
Before a draft opinion or email could become an external effect.

## Governed boundary
- Allowed outputs: open the User Decision Gate; risky-wording note; safer-wording
  candidate; capability gap.
- Forbidden: external send; sign; enterprise instruction; final approval; promoting a
  Registre Probatoire entry.
- The guard opens the gate; the human decides. The draft is the system's; the signature
  and the send remain the human's.
