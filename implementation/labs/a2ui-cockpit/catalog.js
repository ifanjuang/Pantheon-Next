import { Catalog } from "@a2ui/web_core/v0_9";
import { basicCatalog } from "@a2ui/lit/v0_9";

export const CATALOG_ID = "urn:pantheon:a2ui:research-summary:v0.1";

export const ALLOWED_COMPONENT_NAMES = Object.freeze([
  "Column",
  "Row",
  "Text",
  "Card",
  "Divider",
  "Button",
]);

export const ALLOWED_ACTION_NAMES = Object.freeze([
  "pantheon.prepare_hermes_handoff",
]);

const allowed = new Set(ALLOWED_COMPONENT_NAMES);
const selectedComponents = [...basicCatalog.components.values()].filter((component) =>
  allowed.has(component.name),
);

if (selectedComponents.length !== ALLOWED_COMPONENT_NAMES.length) {
  const selectedNames = new Set(selectedComponents.map((component) => component.name));
  const missing = ALLOWED_COMPONENT_NAMES.filter((name) => !selectedNames.has(name));
  throw new Error(`A2UI qualification catalog missing expected components: ${missing.join(", ")}`);
}

// No catalog functions are admitted in the first qualification slice.
// In particular, generated functionCall actions cannot execute client-side code.
export const pantheonResearchCatalog = new Catalog(
  CATALOG_ID,
  selectedComponents,
  [],
);
