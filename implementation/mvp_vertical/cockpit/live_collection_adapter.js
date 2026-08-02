// Cockpit live collection adapter.
//
// Owns the boundary between the active schema projection and the shared
// collection core. Card DOM is produced by the canonical renderer; this module
// does not translate class vocabularies and never owns visual decoration.

import { createCollectionController } from "./collection/collection_controller.js";
import { createLiveProvider } from "./providers/live_provider.js";
import { renderCanonicalCard } from "./rendering/card_renderer.js";

const stage = document.getElementById("v2-stage");

if (stage && typeof window.Swiper === "function") {
  const provider = createLiveProvider();
  const flippedByEntity = new Map();
  let controller = null;
  let currentKey = null;
  let notifyActive = null;

  function projectModelViewState(model) {
    if (!model || typeof model !== "object") return model;
    const entityId = model.entity_id || model.id;
    const remembered = entityId ? flippedByEntity.get(entityId) : undefined;
    const flipped = remembered ?? model.view_state?.flipped === true;
    return {
      ...model,
      view_state: {
        ...(model.view_state || {}),
        flipped: Boolean(flipped),
      },
    };
  }

  function projectSnapshotInput(input) {
    if (Array.isArray(input)) return input.map(projectModelViewState);
    if (!input || typeof input !== "object") return input;
    if (Array.isArray(input.siblings)) {
      return { ...input, siblings: input.siblings.map(projectModelViewState) };
    }
    if (Array.isArray(input.models)) {
      return { ...input, models: input.models.map(projectModelViewState) };
    }
    return input;
  }

  function toPreview(node) {
    node.classList.remove("card");
    node.classList.add("card-preview");
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

  function renderProjectedCard(model) {
    return renderCanonicalCard(model, { flipped: model?.view_state?.flipped === true });
  }

  function renderPlaceholder() {
    const placeholder = document.createElement("div");
    placeholder.className = "card-shell collection-placeholder";
    placeholder.setAttribute("aria-hidden", "true");
    const dot = document.createElement("div");
    dot.className = "stack-placeholder";
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

  function loadSnapshot(models, activeIndex) {
    const snapshot = provider.toSnapshot(projectSnapshotInput(models), activeIndex);
    currentKey = snapshot.collection_id;
    controller.load(snapshot);
  }

  function ensureController() {
    if (controller) return;
    stage.replaceChildren();
    controller = createCollectionController({
      mount: stage,
      label: "Cartes sœurs",
      renderItem: (model, { active }) => {
        const node = renderProjectedCard(model);
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

  stage.addEventListener("pantheon:card-flip", event => {
    const entityId = event.detail?.entity_id;
    if (!entityId) return;
    flippedByEntity.set(entityId, event.detail?.flipped === true);
  });

  window.PANTHEON_COCKPIT_SWIPER = {
    mount({ models, activeIndex = 0, onActiveChange }) {
      notifyActive = onActiveChange;
      ensureController();
      loadSnapshot(models, activeIndex);
    },
    update({ models, activeIndex = 0 }) {
      if (!controller) return;
      loadSnapshot(models, activeIndex);
    },
    previous() {
      controller?.move(-1);
    },
    next() {
      controller?.move(1);
    },
    activeElement() {
      return controller?.activeElement?.() || null;
    },
    destroy() {
      controller?.dispose();
      controller = null;
      currentKey = null;
      notifyActive = null;
      flippedByEntity.clear();
    },
  };
}
