// Cockpit live adapter.
//
// Bridges the live schema renderer (`v2_app_schema.js`) to the shared collection
// core. The renderer still exposes a legacy DOM vocabulary internally; this
// adapter normalizes every mounted card to the neutral design-system contract.

import { createCollectionController } from "./v3/collection/collection_controller.js";
import { createLiveProvider } from "./v3/providers/live_provider.js";

const stage = document.getElementById("v2-stage");

const CLASS_MAP = Object.freeze({
  "v2-card": "card",
  "v2-card-inner": "card-inner",
  "v2-card-face": "card-face",
  "v2-card-front": "card-front",
  "v2-card-back": "card-back",
  "v2-card-top": "card-top",
  "v2-card-body": "card-body",
  "v2-back-body": "card-back-body",
  "v2-card-title": "card-title",
  "v2-back-title": "card-back-title",
  "v2-card-summary": "card-summary",
  "v2-card-identity": "card-identity",
  "v2-card-identity-line": "card-identity-line",
  "v2-family-mark": "family-mark",
  "v2-state-icon": "state-icon",
  "v2-card-category": "card-category",
  "v2-card-meta": "card-meta",
  "v2-card-states": "card-states",
  "v2-card-type-tags": "card-type-tags",
  "v2-type-tag": "type-tag",
  "v2-subject-tag-icon": "subject-tag-icon",
  "v2-card-footer": "card-footer",
  "v2-indicator-rail": "indicator-rail",
  "v2-card-actions": "card-actions",
  "v2-back-tag-labels": "card-back-tags",
  "v2-back-tag-label": "card-back-tag",
  "v2-back-section": "card-back-section",
  "v2-back-multiline": "card-back-multiline",
  "v2-card-kicker": "card-kicker",
  "v2-entity-id": "card-entity-id",
});

function stableVariant(value) {
  const input = String(value || "card");
  let hash = 0;
  for (let index = 0; index < input.length; index += 1) {
    hash = ((hash << 5) - hash + input.charCodeAt(index)) | 0;
  }
  return String((Math.abs(hash) % 3) + 1);
}

function presentationAxes(model) {
  const presentation = model?.presentation_family || model?.family || "information";
  const entityType = model?.entity_type || "information";
  const isPack = entityType === "cockpit_space";

  let family = presentation;
  if (["project", "work", "contact"].includes(presentation)) family = "affaires";
  if (presentation === "tool") family = "tools";

  let kind = entityType;
  if (entityType === "legacy_document" || entityType === "document") kind = "folder";
  if (presentation === "project") kind = "project";
  if (presentation === "work") kind = "work";

  return {
    family,
    level: isPack ? "pack" : entityType === "project" ? "booster" : "card",
    kind,
  };
}

function normalizeClasses(root) {
  for (const [legacy, neutral] of Object.entries(CLASS_MAP)) {
    if (root.classList.contains(legacy)) {
      root.classList.remove(legacy);
      root.classList.add(neutral);
    }
    root.querySelectorAll(`.${legacy}`).forEach(node => {
      node.classList.remove(legacy);
      node.classList.add(neutral);
    });
  }
}

function normalizeCard(node, model) {
  normalizeClasses(node);
  node.classList.add("card");

  const axes = presentationAxes(model);
  node.dataset.family = axes.family;
  node.dataset.level = axes.level;
  node.dataset.kind = axes.kind;
  node.dataset.status = model?.status || node.dataset.status || "neutral";
  node.dataset.variant = stableVariant(model?.entity_id);

  const identityAccent = node.style.getPropertyValue("--identity-accent");
  if (identityAccent) node.style.setProperty("--project-accent", identityAccent);

  return node;
}

if (stage && typeof window.Swiper === "function") {
  const provider = createLiveProvider();
  let controller = null;
  let currentKey = null;
  let renderCard = null;
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
        const node = normalizeCard(renderCard(model), model);
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
    mount({ models, activeIndex = 0, renderCard: render, onActiveChange }) {
      renderCard = render;
      notifyActive = onActiveChange;
      ensureController();
      const snapshot = provider.toSnapshot(models, activeIndex);
      const key = snapshot.collection_id;
      currentKey = key;
      controller.render(snapshot);
    },
    update({ models, activeIndex = 0 }) {
      if (!controller || !renderCard) return;
      const snapshot = provider.toSnapshot(models, activeIndex);
      if (snapshot.collection_id !== currentKey) currentKey = snapshot.collection_id;
      controller.render(snapshot);
    },
    slidePrev() {
      controller?.slidePrev();
    },
    slideNext() {
      controller?.slideNext();
    },
    activeElement() {
      return controller?.activeElement?.() || null;
    },
    destroy() {
      controller?.destroy();
      controller = null;
      currentKey = null;
      renderCard = null;
      notifyActive = null;
    },
  };
}
