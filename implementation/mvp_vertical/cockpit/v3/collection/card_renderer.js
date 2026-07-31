// Cockpit V3 — Renderer (DOM only, no Swiper knowledge).
//
// Produces the HTMLElements the CollectionController puts into slides. Every
// function here is a pure projection of a demo item model:
//   { id, title, category, family, summary, status, details }

const BLOB_FAMILIES = new Set(["pantheon", "affaires", "project"]);

function stableVariant(value) {
  let hash = 0;
  for (const character of String(value || "")) hash = ((hash << 5) - hash + character.charCodeAt(0)) | 0;
  return String((Math.abs(hash) % 3) + 1);
}

function blobPrimitive() {
  const container = document.createElement("div");
  container.className = "v3-card-blobs";
  container.setAttribute("aria-hidden", "true");
  for (let index = 1; index <= 3; index += 1) {
    const blob = document.createElement("span");
    blob.className = `v3-card-blob v3-card-blob--${index}`;
    container.append(blob);
  }
  return container;
}

function faceElement(className, item, { hydrated }) {
  const face = document.createElement("div");
  face.className = `v2-card-face ${className}`;
  const back = className.includes("back");

  if (!back) face.append(blobPrimitive());

  const top = document.createElement("header");
  top.className = "v2-card-top";
  const identity = document.createElement("div");
  identity.className = "v2-card-identity";
  const line = document.createElement("div");
  line.className = "v2-card-identity-line";
  const mark = document.createElement("span");
  mark.className = "v2-family-mark";
  mark.textContent = String(item.family || "i").slice(0, 1).toUpperCase();
  const category = document.createElement("span");
  category.className = "v2-card-category";
  category.textContent = item.category || "";
  line.append(mark, category);
  identity.append(line);
  const stateIcon = document.createElement("span");
  stateIcon.className = "v2-state-icon";
  stateIcon.textContent = String(item.status || "").slice(0, 2).toUpperCase();
  top.append(identity, stateIcon);

  const body = document.createElement("div");
  body.className = back ? "v2-back-body" : "v2-card-body";
  const title = document.createElement("h2");
  title.className = back ? "v2-back-title" : "v2-card-title";
  title.textContent = item.title || "";
  const copy = document.createElement("p");
  copy.className = back ? "v2-back-multiline" : "v2-card-summary";
  copy.textContent = hydrated
    ? (back ? item.details || item.summary || "" : item.summary || "")
    : "Chargement des informations…";
  body.append(title, copy);

  face.append(top, body);
  return face;
}

// Interactive recto/verso card for the active slide.
export function renderCard(item, { hydrated = true, interactive = true } = {}) {
  const article = document.createElement("article");
  article.className = "v2-card";
  article.dataset.entityId = item.id ?? "";
  article.dataset.family = item.family ?? "";
  article.dataset.status = item.status ?? "";
  article.dataset.cockpitV3 = "living-card";
  article.dataset.flipped = "false";
  article.dataset.blobVariant = stableVariant(item.id);
  article.dataset.blobSignature = BLOB_FAMILIES.has(item.family) ? "true" : "false";
  article.tabIndex = interactive ? 0 : -1;
  if (!interactive) {
    article.setAttribute("aria-hidden", "true");
    article.inert = true;
  }
  const inner = document.createElement("div");
  inner.className = "v2-card-inner";
  inner.append(faceElement("v2-card-front", item, { hydrated }), faceElement("v2-card-back", item, { hydrated }));
  article.append(inner);
  return article;
}

// The placeholder slide content, shown before the first item lands.
export function renderPlaceholder() {
  const placeholder = document.createElement("div");
  placeholder.className = "v3-card-shell v3-collection-placeholder";
  placeholder.dataset.v3Placeholder = "true";
  placeholder.setAttribute("aria-hidden", "true");
  const dot = document.createElement("div");
  dot.className = "v3-stack-placeholder";
  const copy = document.createElement("p");
  copy.className = "v2-card-summary";
  copy.textContent = "Chargement de la collection…";
  placeholder.append(dot, copy);
  return placeholder;
}

// The synthetic `New` slide, offered only for creatable collections.
export function renderNewSlide(collection, onCreate) {
  const card = document.createElement("div");
  card.className = "v2-swiper-create-card";
  card.setAttribute("role", "button");
  card.tabIndex = 0;
  card.setAttribute("aria-label", `Créer dans ${collection?.title || "la collection"}`);

  const mark = document.createElement("span");
  mark.className = "v2-swiper-create-mark";
  mark.textContent = "+";
  const copy = document.createElement("span");
  copy.className = "v2-swiper-create-copy";
  const strong = document.createElement("strong");
  strong.textContent = "Nouveau";
  const small = document.createElement("small");
  small.textContent = `Créer dans ${collection?.title || "la collection"}`;
  copy.append(strong, small);
  card.append(mark, copy);

  let pointerId = null;
  let startX = 0;
  let startY = 0;
  let dragged = false;

  card.addEventListener("pointerdown", event => {
    pointerId = event.pointerId;
    startX = event.clientX;
    startY = event.clientY;
    dragged = false;
  }, { passive: true });

  card.addEventListener("pointermove", event => {
    if (event.pointerId !== pointerId) return;
    if (Math.hypot(event.clientX - startX, event.clientY - startY) > 8) dragged = true;
  }, { passive: true });

  card.addEventListener("pointercancel", () => {
    pointerId = null;
    dragged = true;
  }, { passive: true });

  card.addEventListener("click", () => {
    pointerId = null;
    if (dragged) {
      dragged = false;
      return;
    }
    onCreate?.(collection);
  });

  card.addEventListener("keydown", event => {
    if (event.key !== "Enter" && event.key !== " ") return;
    event.preventDefault();
    onCreate?.(collection);
  });

  return card;
}

export function renderPreview(item) {
  const preview = document.createElement("div");
  preview.className = "v3-level-preview";
  preview.setAttribute("aria-hidden", "true");
  preview.inert = true;
  if (item) preview.append(renderCard(item, { hydrated: true, interactive: false }));
  return preview;
}
