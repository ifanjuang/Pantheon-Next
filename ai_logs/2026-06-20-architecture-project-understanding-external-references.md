# 2026-06-20 architecture project understanding external references

Status: documented non-implemented (external reference register, candidate-only).

Added an external reference register for the Architecture Project Understanding
work, as a documentation-only sister PR (branch `docs/apu-external-references`,
based on `main`), separate from PR #163.

Added:

- `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md`:
  consolidated register of openBIM standards (IFC / IDS / BCF), IFC/BIM libraries
  and viewers (IfcOpenShell / IfcDiff / Bonsai, xBIM, web-ifc, Autodesk revit-ifc),
  AEC object-model and adapter inspirations (BHoM, BHoM Adapter, Speckle), spatial
  graph / topology references (TopologicPy, IfcLLM, ifc-bench v2), Revit/MCP bridge
  candidates (official Revit MCP 2027, mcp-servers-for-revit, REVIT_MCP_study, AEC
  Model Bridge, Nonica, BIBIM), vector-PDF / OCR extraction (PyMuPDF, pdfplumber,
  OpenCV, LayoutParser, PaddleOCR), floorplan AI / raster-to-graph (CubiCasa5K,
  DeepFloorPlan, FloorPlanCAD, Raster2Seq, FloorplanVLM), future performance
  analysis (Ladybug / Honeybee, EnergyPlus / Radiance / OpenStudio) and IDS
  assisted generation (Ishigaki-IDS);
- `docs/governance/AUTHORITY_INDEX.md`: index row for the new register
  (required by the read-only index-coverage check).

Doctrine encoded:

- a placement rule: external repositories may inspire adapters/examples/benchmarks
  but must not define doctrine, become core dependencies, auto-canonize, mutate
  Revit/IFC/PDF/project memory without approval, or replace Pantheon evidence /
  decision / approval registers;
- every adapter outputs Task Contract in -> Result Candidate + Evidence Pack
  Candidate out, through the chokepoint;
- external identifiers (IFC GlobalId, Revit ElementId, source labels) are
  sources/evidence, never the internal stable_id;
- repo state documented-not-implemented; authority external-reference /
  candidate-only; proposed Zeus decision "to verify" pending audit.

No runtime, schema, dependency or canonical adoption of any external tool was
added. All factual claims about external repositories are recorded as
candidate / to verify, not as verified facts.
