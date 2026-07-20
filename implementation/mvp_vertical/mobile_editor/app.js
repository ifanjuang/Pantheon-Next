const $ = id => document.getElementById(id);
const state = { items: [], current: null, baseMarkdown: "", token: "" };
const instructionLabels = {
  rewrite: "Reformuler la sélection sans en changer le sens.",
  expand: "Détailler la sélection avec les précisions utiles.",
  simplify: "Simplifier la sélection sans perdre les exigences.",
  verify: "Vérifier la sélection et signaler les points à confirmer.",
  move_to_lot: "Proposer le déplacement de la sélection dans un autre lot."
};

function uuid(prefix) { return `${prefix}-${crypto.randomUUID()}`; }
function headers() { return {Authorization:`Bearer ${state.token}`, "Content-Type":"application/json"}; }
function key(id) { return `pantheon-knowledge:${id}`; }
function queueKey() { return "pantheon-knowledge:queue"; }
function queue() { return JSON.parse(localStorage.getItem(queueKey()) || "[]"); }
function setQueue(value) { localStorage.setItem(queueKey(), JSON.stringify(value)); }
function message(text) { $("message").textContent = text; }
function setNetwork() { $("network").textContent = navigator.onLine ? "en ligne" : "hors ligne"; }

async function api(path, options={}) {
  const response = await fetch(path, {...options, headers:{...headers(), ...(options.headers||{})}});
  if (!response.ok) throw new Error((await response.json().catch(()=>({detail:response.statusText}))).detail);
  return response;
}

function renderItems() {
  $("items").innerHTML = "";
  for (const item of state.items) {
    const button = document.createElement("button");
    button.className = `item ${state.current?.knowledge_id === item.knowledge_id ? "active" : ""}`;
    button.append(document.createTextNode(item.title));
    const detail = document.createElement("small");
    detail.textContent = `${item.family} · v${item.version} · ${item.review_status}`;
    button.append(detail);
    button.onclick = () => openItem(item);
    $("items").append(button);
  }
  if (!state.items.length) $("items").innerHTML = '<p class="muted">Aucun sujet Knowledge.</p>';
}

async function loadProject() {
  state.token = $("token").value;
  const project = $("project").value.trim();
  if (!project) return message("Indiquez le projet.");
  try {
    const response = await api(`../v1/projects/${encodeURIComponent(project)}/knowledge`);
    state.items = (await response.json()).knowledge;
    localStorage.setItem(`pantheon-project:${project}`, JSON.stringify(state.items));
    renderItems(); message(`${state.items.length} sujet(s) chargé(s).`); await syncQueue();
  } catch (error) {
    state.items = JSON.parse(localStorage.getItem(`pantheon-project:${project}`) || "[]");
    renderItems(); message(`Mode hors ligne : ${error.message}`);
  }
}

async function openItem(item) {
  state.current = item; renderItems();
  let markdown, loadedRemote = false;
  try {
    markdown = await (await api(`../v1/knowledge/${encodeURIComponent(item.knowledge_id)}/markdown`)).text();
    loadedRemote = true;
    localStorage.setItem(key(item.knowledge_id), JSON.stringify({item, markdown, baseMarkdown:markdown}));
  } catch {
    const cached = JSON.parse(localStorage.getItem(key(item.knowledge_id)) || "null");
    if (!cached) return message("Ce sujet n’est pas encore disponible hors ligne.");
    markdown = cached.markdown; item = cached.item; state.current = item;
    state.baseMarkdown = cached.baseMarkdown || markdown;
  }
  if (loadedRemote) state.baseMarkdown = markdown;
  $("title").textContent = item.title;
  $("status").textContent = `${item.family} · version ${item.version} · ${item.review_status}`;
  $("markdown").value = markdown; $("markdown").disabled = false; $("save").disabled = false;
  document.querySelectorAll("[data-action]").forEach(button => button.disabled = false);
  message("Le brouillon reste local jusqu’à synchronisation.");
}

function storeDraft() {
  if (!state.current) return;
  localStorage.setItem(key(state.current.knowledge_id), JSON.stringify({item:state.current, markdown:$("markdown").value, baseMarkdown:state.baseMarkdown}));
}

async function saveRevision() {
  if (!state.current) return;
  storeDraft();
  const operation = {
    type:"revision", knowledge_id:state.current.knowledge_id,
    body:{markdown:$("markdown").value, expected_version:state.current.version, actor:"mobile-user", actor_kind:"human", idempotency_key:uuid("mobile-revision")}
  };
  setQueue([...queue(), operation]);
  message("Révision ajoutée à la file hors ligne.");
  await syncQueue();
}

async function requestEdit(kind) {
  if (!state.current) return;
  const textarea = $("markdown"), start = textarea.selectionStart, end = textarea.selectionEnd;
  if (textarea.value !== state.baseMarkdown) return message("Synchronisez d’abord le brouillon avant une demande intelligente.");
  if (start === end) return message("Sélectionnez d’abord une zone du texte.");
  const operation = {
    type:"edit_request", knowledge_id:state.current.knowledge_id,
    body:{request_id:uuid("edit"), instruction_kind:kind, instruction:instructionLabels[kind], base_version:state.current.version, selection_start:start, selection_end:end, selected_text:textarea.value.slice(start,end), requested_by:"mobile-user", idempotency_key:uuid("mobile-edit")}
  };
  setQueue([...queue(), operation]);
  message("Demande intelligente mise en file pour Hermes. Le texte n’est pas modifié tant qu’une proposition n’est pas appliquée.");
  await syncQueue();
}

async function syncQueue() {
  if (!navigator.onLine || !state.token) return;
  const pending = queue(), remaining = [];
  for (const operation of pending) {
    try {
      const path = operation.type === "revision"
        ? `../v1/knowledge/${encodeURIComponent(operation.knowledge_id)}`
        : `../v1/knowledge/${encodeURIComponent(operation.knowledge_id)}/edit-requests`;
      const response = await api(path, {method: operation.type === "revision" ? "PUT" : "POST", body:JSON.stringify(operation.body)});
      const result = await response.json();
      if (operation.type === "revision" && state.current?.knowledge_id === operation.knowledge_id) {
        state.current = result; state.baseMarkdown = operation.body.markdown;
        $("status").textContent = `${result.family} · version ${result.version} · ${result.review_status}`;
        localStorage.setItem(key(result.knowledge_id), JSON.stringify({item:result, markdown:operation.body.markdown, baseMarkdown:operation.body.markdown}));
      }
    } catch (error) {
      remaining.push({...operation, conflict:String(error.message)});
    }
  }
  setQueue(remaining);
  message(remaining.length ? `${remaining.length} opération(s) en attente ou en conflit ; aucune version récente n’a été écrasée.` : "Synchronisation terminée.");
}

$("load").onclick = loadProject; $("save").onclick = saveRevision;
$("markdown").addEventListener("input", storeDraft);
document.querySelectorAll("[data-action]").forEach(button => button.onclick = () => requestEdit(button.dataset.action));
window.addEventListener("online", () => { setNetwork(); syncQueue(); });
window.addEventListener("offline", setNetwork); setNetwork();
if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js");
