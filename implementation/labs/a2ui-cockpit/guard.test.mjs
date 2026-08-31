import test from "node:test";
import assert from "node:assert/strict";
import { validateA2uiMessages } from "./guard.js";

const options = {
  protocolVersion: "v0.9.1",
  catalogId: "urn:pantheon:a2ui:research-summary:v0.1",
  surfaceId: "pantheon-research-summary",
  allowedComponents: new Set(["Column", "Row", "Text", "Card", "Divider", "Button"]),
  allowedActions: new Set(["pantheon.prepare_hermes_handoff"]),
};

function baseMessages(component) {
  return [
    {
      version: "v0.9.1",
      createSurface: {
        surfaceId: options.surfaceId,
        catalogId: options.catalogId,
        sendDataModel: false,
      },
    },
    {
      version: "v0.9.1",
      updateComponents: {
        surfaceId: options.surfaceId,
        components: [component],
      },
    },
    {
      version: "v0.9.1",
      updateDataModel: {
        surfaceId: options.surfaceId,
        path: "/",
        value: { title: "fixture" },
      },
    },
  ];
}

test("accepts the bounded qualification envelope", () => {
  const messages = baseMessages({
    id: "root",
    component: "Text",
    text: { path: "/title" },
  });
  assert.equal(validateA2uiMessages(messages, options), true);
});

test("rejects unknown components", () => {
  const messages = baseMessages({
    id: "root",
    component: "Decision",
  });
  assert.throws(
    () => validateA2uiMessages(messages, options),
    /Unknown A2UI component rejected/,
  );
});

test("rejects unknown events and client function calls", () => {
  const unknownEvent = baseMessages({
    id: "root",
    component: "Button",
    child: "label",
    action: { event: { name: "decision.validate" } },
  });
  assert.throws(
    () => validateA2uiMessages(unknownEvent, options),
    /Unknown A2UI action rejected/,
  );

  const functionCall = baseMessages({
    id: "root",
    component: "Button",
    child: "label",
    action: {
      functionCall: {
        call: "submit",
        args: {},
        returnType: "void",
      },
    },
  });
  assert.throws(
    () => validateA2uiMessages(functionCall, options),
    /functionCall is forbidden/,
  );
});

test("rejects secret-like fields and outbound data-model synchronization", () => {
  const secret = baseMessages({
    id: "root",
    component: "Text",
    text: "fixture",
  });
  secret[2].updateDataModel.value = { access_token: "do-not-render" };
  assert.throws(
    () => validateA2uiMessages(secret, options),
    /Secret-like field rejected/,
  );

  const synchronized = baseMessages({
    id: "root",
    component: "Text",
    text: "fixture",
  });
  synchronized[0].createSurface.sendDataModel = true;
  assert.throws(
    () => validateA2uiMessages(synchronized, options),
    /sendDataModel=true is forbidden/,
  );
});
