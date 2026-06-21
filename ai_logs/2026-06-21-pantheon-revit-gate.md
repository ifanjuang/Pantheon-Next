# 2026-06-21 Pantheon Revit Gate framing dossier

Status: documented non-implemented (governance dossier; issue #175).

Documentation-only PR requested on issue #175 (owner/ChatGPT). Adds a framing
dossier for a local, Pantheon-governed Revit plugin. No runtime, plugin, add-in,
MCP server, schema, test, Docker or operations change.

Added:

- docs/governance/PANTHEON_REVIT_GATE.md:
  - Control Band (B0 read-only .. B4 destructive, forbidden at MVP) and Control
    Matrix (capability x mode -> approval ceiling), documentation tables only;
  - action modes (dry-run / preview / temporary / persist) and a governed
    decision queue (a human-decision review surface, not a runtime queue or
    scheduler);
  - Warning Broker (surfaces warnings/conflicts/doubts, decides nothing;
    explainable refusals);
  - Revit 2027 MCP/API read-first notes (.NET 10; external-reference only);
  - spatial understanding notes mapping Revit reads to the APU vocabulary
    (Architectonics / Revit Dialect), bound by the APU adapter contract;
  - installable packs: four distinct states (documented catalogue / real
    installation / technical verification / local execution), never conflated;
  - Missing operational safeguards: worksharing/central file, backup/restore,
    idempotence, units/tolerances, phases/variants, linked models,
    coordinates/project north, selection scope, user roles, family/parameter
    audit, temp cleanup, log confidentiality, doctor checks, Revit 2026/2027
    compatibility, fictional test sets, explainable refusals, safe-subset
    execution, before/after diff, project-data vs graphic-projection, and
    Architectonics compatibility.
- docs/governance/AUTHORITY_INDEX.md: index row.

Boundary: read-first, candidate-only, human-gated; the plugin is a separate ifj-*
runtime repo outside Pantheon. Documented non-implemented; the plugin is not
claimed to exist.
