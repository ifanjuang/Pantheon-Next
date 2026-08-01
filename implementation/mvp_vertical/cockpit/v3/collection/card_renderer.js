// Cockpit renderer — semantic DOM projection only, no Swiper or stylesheet knowledge.
//
// The renderer projects stable visual axes. CSS alone decides how combinations look:
//   level, family, kind, status, context variables.

const PACK_IDS = new Set(["space:pantheon", "space:affaires", "space:connaissances", "space:outils"]);

function stableVariant(value) {
  let hash = 0;
  for (const character of String(value || "")) hash = ((hash << 5) - hash + character.charCodeAt(0)) | 0;
  return String((Math.abs(hash) % 3) + 1);
}

function visualLevel(item) {
  if (item.level) return item.level;
  if (PACK_IDS.has(item.id)) return "pack";
  if (item.family === "project") return "booster";
  return "card";
}

function visualKind(item) {
  if (item.kind) return item.kind;
  if (item.family === "project") return "project";
  if (item.family === "work") return "work";
  if (String(item.id || "").startsWith("document:")) return "folder";
  return item.family || "information";
}

function faceElement(className, item, { hydrated }) {
  const face = document.createElement("div");
  face.className = `card-face ${className}`;
  const back = className.includes("back");

  const top = document.createElement("header");
  top.className = "card-top";
  const identity = document.createElement("div");
  identity.className = "card-identity";
  const line = document.createElement("div");
  line.className = "card-identity-line";
  const mark = document.createElement("span");
  mark.className = "family-mark";
  mark.textContent = String(item.family || "i").slice(0, 1).toUpperCase();
  const category = document.createElement("span");
  category.className = "card-category";
  category.textContent = item.category || "";
  line.append(mark, category);
  identity.append(line);
  const stateIcon = document.createElement("span");
  stateIcon.className = "state-icon";
  stateIcon.textContent = String(item.status || "").slice(0, 2).toUpperCase();
  top.append(identity, stateIcon);

  const body = document.createElement("div");
  body.className = back ? "card-back-body" : "card-body";
  const title = document.createElement("h2");
  title.className = back ? "card-back-title" : "card-title";
  title.textContent = item.title || "";
  const copy = document.createElement("p");
  copy.className = back ? "card-back-copy" : "card-summary";
  copy.textContent = hydrated
    ? (back ? item.details || item.summary || "" : item.summary || "")
    : "Chargement des informations…";
  body.append(title, copy);

  face.append(top, body);
  return face;
}

export function renderCard(item, { hydrated = true, interactive = true } = {}) {
  const article = document.createElement("article");
  article.className = "card";
  article.dataset.entityId = item.id ?? "";
  article.dataset.family = item.family ?? "";
  article.dataset.level = visualLevel(item);
  article.dataset.kind = visualKind(item);
  article.dataset.status = item.status ?? "";
  article.dataset.flipped = "false";
  article.dataset.variant = stableVariant(item.id);
  article.tabIndex = interactive ? 0 : -1;
  if (!interactive) {
    article.setAttribute("aria-hidden", "true");
    article.inert = true;
  }

  const inner = document.createElement("div");
  inner.className = "card-inner";
  inner.append(
    faceElement("card-front", item, { hydrated }),
    faceElement("card-back", item, { hydrated }),
  );
  article.append(inner);
  return article;
}

export function renderPlaceholder() {
  const placeholder = document.createElement("div");
  placeholder.className = "collection-placeholder";
  placeholder.dataset.placeholder = "true";
  placeholder.setAttribute("aria-hidden", "true");
  const dot = document.createElement("div");
  dot.className = "stack-placeholder";
  const copy = document.createElement("p");
  copy.className = "card-summary";
  copy.textContent = "Chargement de la collection…";
  placeholder.append(dot, copy);
  return placeholder;
}

export function renderNewSlide(collection, onCreate) {
  const card = document.createElement("div");
  card.className = "create-card";
  card.setAttribute("role", "button");
  card.tabIndex = 0;
  card.setAttribute("aria-label", `Créer dans ${collection?.title || "la collection"}`);

  const mark = document.createElement("span");
  mark.className = "create-mark";
  mark.textContent = "+";
  const copy = document.createElement("span");
  copy.className = "create-copy";
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
  preview.className = "level-preview";
  preview.setAttribute("aria-hidden", "true");
  preview.inert = true;
  if (item) preview.append(renderCard(item, { hydrated: true, interactive: false }));
  return preview;
}
