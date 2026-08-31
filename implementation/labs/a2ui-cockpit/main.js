import { MessageProcessor } from "@a2ui/web_core/v0_9";
import { A2uiSurface } from "@a2ui/lit/v0_9";
import messages from "./fixtures/research-summary.a2ui.json";
import {
  ALLOWED_ACTION_NAMES,
  ALLOWED_COMPONENT_NAMES,
  CATALOG_ID,
  pantheonResearchCatalog,
} from "./catalog.js";
import { validateA2uiMessages } from "./guard.js";

const PROTOCOL_VERSION = "v0.9.1";
const SURFACE_ID = "pantheon-research-summary";
const allowedComponents = new Set(ALLOWED_COMPONENT_NAMES);
const allowedActions = new Set(ALLOWED_ACTION_NAMES);

validateA2uiMessages(messages, {
  protocolVersion: PROTOCOL_VERSION,
  catalogId: CATALOG_ID,
  surfaceId: SURFACE_ID,
  allowedComponents,
  allowedActions,
});

const intentOutput = document.querySelector("#intent-output");

function captureBoundedIntent(action) {
  if (!allowedActions.has(action.name)) {
    throw new Error(`Unknown A2UI action rejected at dispatch: ${action.name}`);
  }

  const boundedIntent = Object.freeze({
    kind: "cockpit_intent_candidate",
    action: action.name,
    surface_id: action.surfaceId,
    source_component_id: action.sourceComponentId,
    context: action.context,
    executed: false,
    persisted: false,
    authorized: false,
  });

  intentOutput.textContent = JSON.stringify(boundedIntent, null, 2);
  window.dispatchEvent(
    new CustomEvent("pantheon:a2ui-intent", {
      detail: boundedIntent,
    }),
  );
}

const processor = new MessageProcessor(
  [pantheonResearchCatalog],
  captureBoundedIntent,
  { version: PROTOCOL_VERSION },
);

processor.processMessages(messages);

const surface = processor.model.getSurface(SURFACE_ID);
if (!surface) {
  throw new Error(`A2UI surface was not created: ${SURFACE_ID}`);
}

const host = document.querySelector("#surface-host");
const surfaceElement = new A2uiSurface();
surfaceElement.surface = surface;
host.replaceChildren(surfaceElement);
