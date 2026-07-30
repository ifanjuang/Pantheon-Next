// Cockpit live adapter.
//
// Bridges the live schema renderer (`v2_app_schema.js`) to the shared collection
// core. The renderer hands over the whole sibling collection as data; only the
// active projection and its two neighbours are ever mounted.
//
// Invariant kept for the rest of the live cockpit: exactly one interactive
// `.v2-card` exists at a time (the active projection). Neighbours are inert
// `.v2-card-preview` clones, so `#v2-stage .v2-card` still resolves to the
// active card the historical modules target. Migrating those modules to an
// explicit host registry is a separate step.

import { createCollectionController } from "./v3/collection/collection_controller.js";
import { createLiveProvider } from "./v3/providers/live_provider.js";

const stage = document.getElementById("v2-stage");

if (stage && typeof window.Swiper === "function") {
  const provider = createLiveProvider();
  let controller = null;
  let currentKey = null;
  let renderCard = null;   // provided by the live renderer on each present()
  let notifyActive = null;

  function toPreview(node) {
    node.classList.remove("v2-card");
    node.classList.add("v2-card-preview");
    node.removeAttribute("id");
    node.removeAttribute("tabindex");
    node.dataset.flipped = "false";
    node.setAttribute("aria-hidden", "true");
    node.inert = true;
    node.querySelectorAll("[id]").forEach(item => item.removeAttribute("id"));
    node.querySelectorAll("button,input,select,textarea,a,[tabindex]").forEach(item => {
      item.setAttribute("tabindex", "-1");
      if ("disabled" in item) item.disabled = true;
    });
    return node;
  }

  function renderPlaceholder() {
    const placeholder = document.createElement("div");
    placeholder.className = "v3-card-shell v3-collection-placeholder";
    placeholder.setAttribute("aria-hidden", "true");
    const dot = document.createElement("div");
    dot.className = "v3-stack-placeholder";
    placeholder.append(dot);
    return placeholder;
  }

  function renderEmpty() {
    const empty = document.createElement("p");
    empty.className = "v2-empty";
    empty.setAttribute("role", "status");
    empty.textContent = "Aucune carte dans cette collection.";
    return empty;
  }

  function ensureController() {
    if (controller) return;
    stage.replaceChildren();
    controller = createCollectionController({
      mount: stage,
      label: "Cartes sœurs",
      renderItem: (model, { active }) => {
        const node = renderCard(model);
        return active ? node : toPreview(node);
      },
      renderPlaceholder,
      renderEmpty,
      onActiveChange(model, index) {
        if (index >= 0 && model) notifyActive?.(model, index);
      },
      onMoveState(moving) {
        if (moving) {
          stage.dataset.swiperMoving = "true";
          stage.dataset.swiperNavigation = "true";
        } else {
          delete stage.dataset.swiperMoving;
          delete stage.dataset.swiperNavigation;
        }
      },
    });
  }

  function present({ key, siblings = [], index = 0, motion = "", renderCard: renderer, onActiveChange }) {
    renderCard = renderer;
    notifyActive = onActiveChange;
    if (motion) stage.dataset.motion = motion;
    ensureController();

    if (key !== currentKey || !siblings.length) {
      currentKey = key;
      controller.load(provider.toSnapshot({ key, siblings, index }));
      return;
    }
    // Same collection re-presented (e.g. project reload): reposition only.
    controller.goTo(index);
  }

  window.PantheonLiveCollection = Object.freeze({
    present,
    slide(delta) { controller?.move(delta); },
    activeElement() { return controller?.activeElement() || null; },
  });

  window.addEventListener("pagehide", () => controller?.dispose(), { once: true });
}
