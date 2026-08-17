// Cockpit live collection adapter.
//
// Owns the boundary between the active schema projection and the shared
// collection core. Card DOM is produced by the canonical renderer; this module
// only coordinates presentation state around that renderer.

import { createCollectionController } from "./collection/collection_controller.js";
import { canExpandCollection } from "./collection/motion_adapter.js";
import { createLiveProvider } from "./providers/live_provider.js";
import { renderCanonicalCard } from "./rendering/card_renderer.js";

const stage = document.getElementById("v2-stage");

if (stage && typeof window.Swiper === "function") {
  const provider = createLiveProvider();
  const flippedByEntity = new Map();
  let controller = null;
  let currentKey = null;
  let notifyActive = null;
  let primaryHost = null;
  let childHost = null;
  let presentation = "compact";
  let expandedEntityId = null;

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

  function childModelsFor(entityId) {
    if (!entityId) return [];
    const graph = window.PantheonCockpitGraph;
    if (!graph?.children?.get || !graph?.cards?.get) return [];
    return (graph.children.get(entityId) || [])
      .map(id => graph.cards.get(id))
      .filter(Boolean)
      .map(projectModelViewState);
  }

  function stageWidth() {
    return Number(stage.getBoundingClientRect?.().width || stage.clientWidth || window.innerWidth || 0);
  }

  function contextualChildrenFor(entityId) {
    const children = childModelsFor(entityId);
    if (children.length === 1) return children;
    return canExpandCollection({ width: stageWidth(), count: children.length }) ? children : [];
  }

  function syncPresentationAttributes() {
    stage.dataset.collectionPresentation = presentation;
    if (presentation === "expanded" && expandedEntityId) {
      stage.dataset.collectionExpanded = "true";
    } else {
      delete stage.dataset.collectionExpanded;
    }
  }

  function renderExpandedChildren() {
    if (!childHost) return;
    childHost.replaceChildren();
    const children = presentation === "expanded" ? contextualChildrenFor(expandedEntityId) : [];
    if (!children.length) {
      childHost.hidden = true;
      syncPresentationAttributes();
      return;
    }

    const section = document.createElement("section");
    section.className = "v3-expanded-children";
    const parent = window.PantheonCockpitGraph?.cards?.get?.(expandedEntityId);
    section.setAttribute("aria-label", parent?.title ? `Sous-cartes de ${parent.title}` : "Sous-cartes");

    const grid = document.createElement("div");
    grid.className = "v3-expanded-child-grid";
    for (const model of children) {
      const cell = document.createElement("div");
      cell.className = "v3-expanded-child-cell";
      cell.append(renderProjectedCard(model));
      grid.append(cell);
    }
    section.append(grid);
    childHost.append(section);
    childHost.hidden = false;
    syncPresentationAttributes();
  }

  function loadSnapshot(models, activeIndex) {
    const snapshot = provider.toSnapshot(projectSnapshotInput(models), activeIndex);
    if (currentKey && currentKey !== snapshot.collection_id) expandedEntityId = null;
    currentKey = snapshot.collection_id;
    controller.load(snapshot);
    renderExpandedChildren();
  }

  function ensureHosts() {
    if (primaryHost && childHost) return;
    stage.replaceChildren();
    primaryHost = document.createElement("div");
    primaryHost.className = "v3-primary-collection-host";
    childHost = document.createElement("div");
    childHost.className = "v3-expanded-children-host";
    childHost.hidden = true;
    stage.append(primaryHost, childHost);
  }

  function ensureController() {
    if (controller) return;
    ensureHosts();
    controller = createCollectionController({
      mount: primaryHost,
      label: "Cartes sœurs",
      renderItem: (model, { active, presentation: itemPresentation }) => {
        const node = renderProjectedCard(model);
        if (itemPresentation === "expanded") {
          node.dataset.collectionActive = active ? "true" : "false";
          return node;
        }
        return active ? node : toPreview(node);
      },
      renderPlaceholder,
      renderEmpty,
      onActiveChange(model, index, meta = {}) {
        if (meta.presentation === "compact") expandedEntityId = null;
        if (index >= 0 && model) notifyActive?.(model, index);
        if (expandedEntityId && model?.entity_id !== expandedEntityId) expandedEntityId = null;
        renderExpandedChildren();
      },
      onItemActivate(model, _index, meta = {}) {
        if (meta.presentation !== "expanded" || !model?.entity_id) return;
        const children = contextualChildrenFor(model.entity_id);
        if (!children.length) {
          expandedEntityId = null;
        } else if (meta.reselected && expandedEntityId === model.entity_id) {
          expandedEntityId = null;
        } else {
          expandedEntityId = model.entity_id;
        }
        renderExpandedChildren();
      },
      onPresentationChange(nextPresentation) {
        presentation = nextPresentation;
        if (presentation !== "expanded") expandedEntityId = null;
        syncPresentationAttributes();
        renderExpandedChildren();
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
      primaryHost = null;
      childHost = null;
      presentation = "compact";
      expandedEntityId = null;
      delete stage.dataset.collectionPresentation;
      delete stage.dataset.collectionExpanded;
      flippedByEntity.clear();
    },
  };
}
