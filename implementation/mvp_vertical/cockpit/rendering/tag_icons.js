const REGISTRY_SOURCES = Object.freeze({
  type: new URL("../registries/type_tags.json", import.meta.url),
  subject: new URL("../registries/subject_tags.json", import.meta.url),
});

const registries = { type: new Map(), subject: new Map() };
const FALLBACK_PRESENTATION = Object.freeze({
  title: "Tag",
  description: "Tag hors registre de présentation.",
  icon_provider: "material-symbols",
  icon_key: "label",
  color: "slate",
});
let loadPromise = null;

function slug(value) {
  return String(value || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

async function fetchRegistry(kind) {
  const response = await fetch(REGISTRY_SOURCES[kind], { cache: "no-store" });
  if (!response.ok) throw new Error(`Tag registry unavailable: ${kind} (${response.status})`);
  const payload = await response.json();
  registries[kind].clear();
  for (const entry of payload.tags || []) registries[kind].set(slug(entry.slug || entry.title), entry);
}

export function loadTagIconRegistries() {
  if (!loadPromise) {
    loadPromise = Promise.all(Object.keys(REGISTRY_SOURCES).map(fetchRegistry))
      .catch(error => console.warn("Tag icon registries unavailable; using visible fallback icons", error));
  }
  return loadPromise;
}

export function tagPresentation(value, kind = "subject") {
  const label = String(value?.title ?? value?.label ?? value?.name ?? value?.slug ?? value ?? "Tag").trim() || "Tag";
  const registry = kind === "type" ? registries.type : registries.subject;
  const registered = registry.get(slug(value?.slug ?? value)) || null;
  return { ...FALLBACK_PRESENTATION, ...(registered || {}), title: registered?.title || label };
}

export function createTagIcon(presentation) {
  const icon = document.createElement("span");
  icon.className = "tag-icon";
  icon.setAttribute("aria-hidden", "true");
  if (presentation.icon_provider === "radix") {
    icon.classList.add("radix-icon");
    icon.dataset.icon = presentation.icon_key;
  } else {
    icon.classList.add("material-symbols-rounded");
    icon.textContent = presentation.icon_key || FALLBACK_PRESENTATION.icon_key;
  }
  return icon;
}

export function createTagToken(value, kind, { className, legacyClassName = "", labelled = false } = {}) {
  const presentation = tagPresentation(value, kind);
  const node = document.createElement("span");
  node.className = [className, legacyClassName].filter(Boolean).join(" ");
  node.title = presentation.description || presentation.title;
  node.setAttribute("aria-label", presentation.title);
  node.dataset.iconProvider = presentation.icon_provider;
  node.dataset.iconKey = presentation.icon_key;
  if (presentation.color) node.dataset.tokenColor = presentation.color;
  node.append(createTagIcon(presentation));
  if (labelled) {
    const label = document.createElement("span");
    label.className = "tag-label";
    label.textContent = presentation.title;
    node.append(label);
  }
  return node;
}

const API = Object.freeze({ loadTagIconRegistries, tagPresentation, createTagIcon, createTagToken });
if (typeof window !== "undefined") window.PantheonTagIcons = API;
