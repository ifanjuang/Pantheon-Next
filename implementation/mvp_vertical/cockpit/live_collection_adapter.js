// Cockpit live collection adapter.
//
// Owns the boundary between the active schema projection and the shared
// collection core. Card DOM is produced by the canonical renderer; this module
// does not translate class vocabularies and never owns visual decoration.

import { createCollectionController } from "./v3/collection/collection_controller.js";
import { createLiveProvider } from "./v3/providers/live_provider.js";
import { renderCanonicalCard } from "./rendering/card_renderer.js";

const stage = document.getElementById("v2-stage");

if (stage && typeof window.Swiper === "function") {
  const provider = createLiveProvider();
  let controller = null;
  let currentKey = null;
  let projectLegacyState = null;
  let notifyActive = null;

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
    // Flipped state still belongs to the active application renderer until the
    // state projection is moved into the collection snapshot. No legacy DOM is
    // mounted or normalized; only the state bit is read during this transition.
    const legacyProjection = projectLegacyState?.(model);
    const flipped = legacyProjection?.dataset?.flipped === "true";
    return renderCanonicalCard(model, { flipped });
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

  window.PANTHEON_COCKPIT_SWIPER = {
    mount({ models, activeIndex = 0, renderCard, onActiveChange }) {
      projectLegacyState = renderCard;
      notifyActive = onActiveChange;
      ensureController();
      const snapshot = provider.toSnapshot(models, activeIndex);
      currentKey = snapshot.collection_id;
      controller.load(snapshot);
    },
    update({ models, activeIndex = 0 }) {
      if (!controller) return;
      const snapshot = provider.toSnapshot(models, activeIndex);
      if (snapshot.collection_id !== currentKey) currentKey = snapshot.collection_id;
      controller.load(snapshot);
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
      projectLegacyState = null;
      notifyActive = null;
    },
  };
}
