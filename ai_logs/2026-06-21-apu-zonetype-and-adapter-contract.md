# 2026-06-21 APU zone_type requirement + adapter contract

Status: documented non-implemented (small schema patch + governance doc).

Two APU usability pieces:

1. zone_type-when-zone (#169 residual): spatial_node now requires `zone_type`
   when `node_kind` is `zone` (allOf if/then), so transversal zones are typed
   groupings, not bare containers.

2. Adapter contract: `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md`
   defines the binding an external APU adapter (PDF/IFC/image/Revit reader, runtime
   outside Pantheon) must respect: Task Contract in -> Result Candidate + Evidence
   Pack Candidate out; candidate-only; per-attribute provenance; E0-E4 certainty
   band across the boundary; observed/proposed modality only; no canonization; no
   regulatory_claim; no source mutation; one-way dependency (adapter imports
   Pantheon schemas, never the reverse). Specializes BRIDGE_CONTRACT /
   ADAPTERS_AND_BINDINGS; points to the #168 template and the #170 conformant
   dossier as reference shapes. Indexed in AUTHORITY_INDEX.md.

This closes the open #169 items; the runtime itself remains a separate repo
(ifj-project-understanding-runtime), out of scope for this governance repo.

Verified: pytest 9/9; referential-integrity 16/16; doctor scripts green; mcp-server 29/29.

Boundary: schema constraint + governance doc only. No runtime, no new object.
