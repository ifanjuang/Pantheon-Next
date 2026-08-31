const SECRET_KEY_PATTERN =
  /(^|_)(authorization|api_?key|access_?token|refresh_?token|password|passwd|secret|cookie|session_?id)($|_)/i;

const MAX_MESSAGES = 8;
const MAX_COMPONENTS = 64;
const MAX_DATA_MODEL_BYTES = 128 * 1024;

function assertPlainObject(value, label) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new Error(`${label} must be an object`);
  }
}

function inspectForSecrets(value, path = "$") {
  if (Array.isArray(value)) {
    value.forEach((item, index) => inspectForSecrets(item, `${path}[${index}]`));
    return;
  }
  if (!value || typeof value !== "object") return;

  for (const [key, nested] of Object.entries(value)) {
    if (SECRET_KEY_PATTERN.test(key)) {
      throw new Error(`Secret-like field rejected from A2UI data model: ${path}.${key}`);
    }
    inspectForSecrets(nested, `${path}.${key}`);
  }
}

function validateAction(action, allowedActions, componentId) {
  if (!action) return;
  assertPlainObject(action, `action for ${componentId}`);

  if ("functionCall" in action) {
    throw new Error(`Client functionCall is forbidden in qualification surface: ${componentId}`);
  }

  const event = action.event;
  assertPlainObject(event, `event action for ${componentId}`);
  if (!allowedActions.has(event.name)) {
    throw new Error(`Unknown A2UI action rejected: ${event.name || "<missing>"}`);
  }
}

export function validateA2uiMessages(
  messages,
  {
    protocolVersion,
    catalogId,
    surfaceId,
    allowedComponents,
    allowedActions,
  },
) {
  if (!Array.isArray(messages) || messages.length === 0 || messages.length > MAX_MESSAGES) {
    throw new Error("A2UI qualification message list is empty or exceeds the bounded limit");
  }

  let createCount = 0;
  let componentCount = 0;

  for (const [index, message] of messages.entries()) {
    assertPlainObject(message, `message[${index}]`);

    if (message.version !== protocolVersion) {
      throw new Error(`Unsupported A2UI protocol version: ${message.version}`);
    }

    const updateKinds = [
      "createSurface",
      "updateComponents",
      "updateDataModel",
      "deleteSurface",
    ].filter((key) => key in message);

    if (updateKinds.length !== 1) {
      throw new Error(`Message ${index} must contain exactly one A2UI update kind`);
    }

    if (message.createSurface) {
      createCount += 1;
      const payload = message.createSurface;
      if (payload.surfaceId !== surfaceId) {
        throw new Error(`Unexpected A2UI surface id: ${payload.surfaceId}`);
      }
      if (payload.catalogId !== catalogId) {
        throw new Error(`Unapproved A2UI catalog id: ${payload.catalogId}`);
      }
      if (payload.sendDataModel === true) {
        throw new Error("sendDataModel=true is forbidden in the first qualification slice");
      }
      continue;
    }

    if (message.updateComponents) {
      const payload = message.updateComponents;
      if (payload.surfaceId !== surfaceId || !Array.isArray(payload.components)) {
        throw new Error("Invalid A2UI component update envelope");
      }
      componentCount += payload.components.length;
      if (componentCount > MAX_COMPONENTS) {
        throw new Error("A2UI component count exceeds the bounded qualification limit");
      }

      for (const component of payload.components) {
        assertPlainObject(component, "A2UI component");
        if (!component.id || !component.component) {
          throw new Error("Qualification components require explicit id and component type");
        }
        if (!allowedComponents.has(component.component)) {
          throw new Error(`Unknown A2UI component rejected: ${component.component}`);
        }
        validateAction(component.action, allowedActions, component.id);
      }
      continue;
    }

    if (message.updateDataModel) {
      const payload = message.updateDataModel;
      if (payload.surfaceId !== surfaceId) {
        throw new Error(`Unexpected data-model surface id: ${payload.surfaceId}`);
      }
      inspectForSecrets(payload.value);
      const serialized = JSON.stringify(payload.value ?? null);
      if (new TextEncoder().encode(serialized).byteLength > MAX_DATA_MODEL_BYTES) {
        throw new Error("A2UI data model exceeds the bounded qualification limit");
      }
      continue;
    }

    if (message.deleteSurface?.surfaceId !== surfaceId) {
      throw new Error(`Unexpected delete surface id: ${message.deleteSurface?.surfaceId}`);
    }
  }

  if (createCount !== 1) {
    throw new Error(`Qualification surface requires exactly one createSurface message, got ${createCount}`);
  }

  return true;
}
