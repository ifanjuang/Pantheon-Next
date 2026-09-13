(() => {
  "use strict";

  const ACTIVE_ADMISSION_KEY = "pantheon-active-hermes-admission";
  const ROLE_ICONS = Object.freeze({
    Athena: "🦉", Argos: "🔎", Themis: "⚖", Apollo: "☀",
    Hephaistos: "🛠", Iris: "📨", Zeus: "⚡", Mnemosyne: "🧠", Hermes: "⚙",
  });
  const DETAIL_LABELS = Object.freeze({
    action: "Action", raison: "Raison", but: "But", sources: "Sources",
    method: "Méthode", skill: "Skill", outil: "Outil", result: "Résultat",
    limite: "Limite", next_action: "Prochaine action", gate: "Gate", handoff: "Relais",
  });

  const $ = id => document.getElementById(id);
  const token = () => $("v2-token")?.value || "";
  const dockOpen = () => !$("v2-hermes-dock")?.hidden;
  let currentRun = "";
  let lastCursor = 0;
  let streamController = null;
  let admissionTimer = null;
  let reconnectTimer = null;
  let reconnects = 0;
  const stages = new Map();

  function setState(message) {
    const node = $("v2-role-dialogue-state");
    if (node) node.textContent = message;
  }

  function stop() {
    streamController?.abort();
    streamController = null;
    window.clearTimeout(admissionTimer);
    window.clearTimeout(reconnectTimer);
    admissionTimer = reconnectTimer = null;
  }

  function resetForRun(runId) {
    if (runId === currentRun) return;
    stop();
    currentRun = runId;
    lastCursor = 0;
    reconnects = 0;
    stages.clear();
    $("v2-role-dialogue-events")?.replaceChildren();
  }

  function stageDetails(host, values) {
    const entries = Object.entries(values || {}).filter(([, value]) => value != null && value !== "");
    if (!entries.length) return;
    const details = document.createElement("details");
    const summary = document.createElement("summary");
    summary.textContent = "Détails observables";
    const list = document.createElement("dl");
    for (const [key, value] of entries) {
      const dt = document.createElement("dt");
      const dd = document.createElement("dd");
      dt.textContent = DETAIL_LABELS[key] || key.replaceAll("_", " ");
      dd.textContent = String(value);
      list.append(dt, dd);
    }
    details.append(summary, list);
    host.append(details);
  }

  function renderStage(event) {
    if (!event?.stage_id || !event?.visible_role) return;
    let item = stages.get(event.stage_id);
    if (!item) {
      item = document.createElement("li");
      item.className = "v2-role-stage";
      stages.set(event.stage_id, item);
      $("v2-role-dialogue-events")?.append(item);
    }
    const completed = event.phase === "completed";
    item.classList.toggle("is-running", !completed);
    item.replaceChildren();

    const icon = document.createElement("span");
    icon.className = "v2-role-stage-icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = ROLE_ICONS[event.visible_role] || "•";
    const title = document.createElement("strong");
    title.className = "v2-role-stage-title";
    title.textContent = `${event.visible_role} — ${event.semantic_function || event.role_family || "Jalon"}`;
    const status = document.createElement("span");
    status.className = "v2-role-stage-status";
    status.textContent = completed ? "terminé" : "en cours";
    const summary = document.createElement("p");
    summary.className = "v2-role-stage-summary";
    summary.textContent = event.summary || "Jalon public observé.";
    const origin = document.createElement("span");
    origin.className = "v2-role-stage-origin";
    origin.textContent = event.projection === "derived_transient" ? "dérivé" : "natif";
    origin.title = event.projection === "derived_transient"
      ? "Projection transitoire dérivée du flux public Hermes"
      : "Événement structuré émis par le runtime";
    item.append(icon, title, status, origin, summary);
    stageDetails(item, event.details);
  }

  function consumeBlock(block) {
    let kind = "message";
    let id = null;
    const data = [];
    for (const line of block.split("\n")) {
      if (line.startsWith("event:")) kind = line.slice(6).trim();
      else if (line.startsWith("id:")) id = Number(line.slice(3).trim());
      else if (line.startsWith("data:")) data.push(line.slice(5).trimStart());
    }
    if (!data.length) return;
    const payload = JSON.parse(data.join("\n"));
    if (Number.isSafeInteger(id) && id > lastCursor) lastCursor = id;
    if (kind === "role.stage") renderStage(payload);
    else if (kind === "role.trace.error") setState("Rejeu incomplet");
  }

  async function traceStatus(runId) {
    const response = await fetch(`../cockpit/role-traces/${encodeURIComponent(runId)}`, {
      headers: { Authorization: `Bearer ${token()}` }, cache: "no-store",
    });
    if (!response.ok) return null;
    return response.json();
  }

  function retryStream(runId) {
    if (!dockOpen() || runId !== currentRun || reconnects >= 5) return;
    reconnects += 1;
    reconnectTimer = window.setTimeout(() => void connect(runId), Math.min(1000 * reconnects, 5000));
  }

  async function connect(runId) {
    if (!runId || !token() || !dockOpen()) return;
    resetForRun(runId);
    streamController?.abort();
    streamController = new AbortController();
    setState(lastCursor ? "Reconnexion…" : "Connexion…");
    try {
      const headers = { Authorization: `Bearer ${token()}` };
      if (lastCursor) headers["Last-Event-ID"] = String(lastCursor);
      const response = await fetch(`../cockpit/role-traces/${encodeURIComponent(runId)}/events`, {
        headers, cache: "no-store", signal: streamController.signal,
      });
      if (!response.ok || !response.body) {
        setState(response.status === 404 ? "Trace en attente" : "Trace indisponible");
        retryStream(runId);
        return;
      }
      reconnects = 0;
      setState("En direct");
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      while (true) {
        const { value, done } = await reader.read();
        buffer += decoder.decode(value || new Uint8Array(), { stream: !done }).replaceAll("\r\n", "\n");
        let boundary;
        while ((boundary = buffer.indexOf("\n\n")) >= 0) {
          const block = buffer.slice(0, boundary);
          buffer = buffer.slice(boundary + 2);
          if (block.trim()) consumeBlock(block);
        }
        if (done) break;
      }
      const status = await traceStatus(runId);
      setState(status?.diagnostic ? "Trace incomplète" : status?.terminal ? "Terminé" : "Interrompu");
      if (!status?.terminal) retryStream(runId);
    } catch (error) {
      if (error?.name !== "AbortError") {
        setState("Connexion interrompue");
        retryStream(runId);
      }
    }
  }

  function scheduleAdmissionRead(delay = 3000) {
    window.clearTimeout(admissionTimer);
    if (!dockOpen() || currentRun) return;
    admissionTimer = window.setTimeout(() => void readActiveAdmission(), delay);
  }

  async function readActiveAdmission() {
    const admissionId = sessionStorage.getItem(ACTIVE_ADMISSION_KEY);
    if (!admissionId || !token() || !dockOpen()) {
      setState("Aucune exécution");
      return;
    }
    try {
      const response = await fetch(`../cockpit/hermes-execution-admissions/${encodeURIComponent(admissionId)}`, {
        headers: { Authorization: `Bearer ${token()}` }, cache: "no-store",
      });
      const admission = await response.json();
      if (!response.ok) throw new Error(admission.detail || response.statusText);
      const runId = String(admission.consumed_by_run_id || "");
      if (runId) void connect(runId);
      else {
        resetForRun("");
        setState(admission.admission_state === "admitted" ? "En attente d’Hermes" : "Aucune exécution");
        scheduleAdmissionRead();
      }
    } catch (_error) {
      setState("Admission indisponible");
      scheduleAdmissionRead(5000);
    }
  }

  document.addEventListener("pantheon:hermes-admission", event => {
    const runId = String(event.detail?.admission?.consumed_by_run_id || "");
    if (runId) void connect(runId);
    else {
      resetForRun("");
      scheduleAdmissionRead();
    }
  });
  document.addEventListener("pantheon:hermes-dock-open", () => void readActiveAdmission());
  document.addEventListener("pantheon:hermes-dock-close", stop);
  $("v2-token")?.addEventListener("change", () => {
    resetForRun("");
    if (dockOpen()) void readActiveAdmission();
  });
})();
