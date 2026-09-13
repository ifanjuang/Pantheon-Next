(() => {
  "use strict";

  const $ = id => document.getElementById(id);
  const nodes = new Map();
  let currentRun = "";
  let selectedId = "";
  let d3Promise = null;

  function setState(message) {
    const node = $("v2-runtime-topology-state");
    if (node) node.textContent = message;
  }

  function reset(runId = "") {
    currentRun = String(runId || "");
    selectedId = "";
    nodes.clear();
    $("v2-runtime-topology-tree")?.replaceChildren();
    $("v2-runtime-topology-detail")?.replaceChildren();
    setState("Aucun worker observé");
  }

  function mergeEvent(event) {
    if (!event?.subagent_id || event.governed_identity !== false) return;
    if (currentRun && event.run_id && event.run_id !== currentRun) return;
    if (!currentRun && event.run_id) currentRun = String(event.run_id);
    const previous = nodes.get(event.subagent_id) || {};
    nodes.set(event.subagent_id, { ...previous, ...event });
    setState(`${nodes.size} worker${nodes.size > 1 ? "s" : ""} observé${nodes.size > 1 ? "s" : ""}`);
    void render();
  }

  async function d3Ready() {
    if (window.d3?.hierarchy && window.d3?.tree && window.d3?.select) return true;
    if (!window.PantheonD3Loader?.ensureD3) return false;
    if (!d3Promise) d3Promise = window.PantheonD3Loader.ensureD3();
    return Boolean(await d3Promise);
  }

  function relationModel() {
    const byParent = new Map();
    const roots = [];
    const known = new Set(nodes.keys());
    for (const event of nodes.values()) {
      const parent = event.parent_id && known.has(event.parent_id) ? event.parent_id : null;
      if (!parent) {
        roots.push(event);
        continue;
      }
      if (!byParent.has(parent)) byParent.set(parent, []);
      byParent.get(parent).push(event);
    }

    let cycleDetected = false;
    const materialize = (event, path = new Set()) => {
      if (path.has(event.subagent_id)) {
        cycleDetected = true;
        return { event, children: [], cycleCut: true };
      }
      const nextPath = new Set(path);
      nextPath.add(event.subagent_id);
      return {
        event,
        children: (byParent.get(event.subagent_id) || []).map(child => materialize(child, nextPath)),
      };
    };

    return {
      data: {
        event: {
          subagent_id: currentRun || "hermes-run",
          synthetic_root: true,
          status: "run",
        },
        children: roots.map(event => materialize(event)),
      },
      cycleDetected,
    };
  }

  function renderFallback(host) {
    host.replaceChildren();
    const list = document.createElement("ul");
    list.className = "v2-runtime-topology-fallback";
    for (const event of nodes.values()) {
      const item = document.createElement("li");
      item.textContent = `${event.subagent_id}${event.parent_id ? ` ← ${event.parent_id}` : " · racine du run"}`;
      list.append(item);
    }
    host.append(list);
    setState(`${nodes.size} worker${nodes.size > 1 ? "s" : ""} · D3 indisponible`);
  }

  function renderDetail(event) {
    const host = $("v2-runtime-topology-detail");
    if (!host) return;
    host.replaceChildren();
    if (!event || event.synthetic_root) return;

    const head = document.createElement("div");
    head.className = "v2-runtime-topology-detail-head";
    const title = document.createElement("strong");
    title.textContent = event.subagent_id;
    const status = document.createElement("span");
    status.textContent = event.status || (event.phase === "completed" ? "completed" : "running");
    head.append(title, status);

    const summary = document.createElement("p");
    summary.className = "v2-runtime-topology-detail-summary";
    summary.textContent = event.summary || event.goal || "Worker Hermes observé.";
    host.append(head, summary);

    const rows = [
      ["Parent runtime", event.parent_id],
      ["Délégation", event.delegation_id],
      ["Session enfant", event.child_session_id],
      ["Modèle", event.model],
      ["Profondeur", event.metrics?.depth],
      ["Durée", event.metrics?.duration_seconds != null ? `${event.metrics.duration_seconds}s` : null],
      ["Tokens entrée", event.metrics?.input_tokens],
      ["Tokens sortie", event.metrics?.output_tokens],
      ["Coût", event.metrics?.cost_usd != null ? String(event.metrics.cost_usd) : null],
      ["Fichiers lus", event.files?.read?.join(", ")],
      ["Fichiers écrits", event.files?.written?.join(", ")],
    ].filter(([, value]) => value != null && value !== "");
    if (rows.length) {
      const list = document.createElement("dl");
      for (const [label, value] of rows) {
        const dt = document.createElement("dt");
        const dd = document.createElement("dd");
        dt.textContent = label;
        dd.textContent = String(value);
        list.append(dt, dd);
      }
      host.append(list);
    }
  }

  async function render() {
    const host = $("v2-runtime-topology-tree");
    if (!host) return;
    if (!nodes.size) {
      host.replaceChildren();
      renderDetail(null);
      return;
    }
    if (!await d3Ready()) {
      renderFallback(host);
      return;
    }

    const { data, cycleDetected } = relationModel();
    const d3 = window.d3;
    const root = d3.hierarchy(data, item => item.children);
    const layout = d3.tree().nodeSize([46, 150]);
    layout(root);
    const descendants = root.descendants();
    const minX = Math.min(...descendants.map(item => item.x));
    const maxX = Math.max(...descendants.map(item => item.x));
    const maxY = Math.max(...descendants.map(item => item.y));
    const width = Math.max(320, maxY + 190);
    const height = Math.max(120, maxX - minX + 80);
    const offsetX = 40 - minX;

    host.replaceChildren();
    const svg = d3.select(host)
      .append("svg")
      .attr("class", "v2-runtime-topology-svg")
      .attr("viewBox", `0 0 ${width} ${height}`)
      .attr("role", "tree")
      .attr("aria-label", "Topologie des workers Hermes observés");
    const graph = svg.append("g").attr("transform", `translate(28 ${offsetX})`);

    graph.selectAll("path")
      .data(root.links())
      .join("path")
      .attr("class", link => link.source.data.event.synthetic_root
        ? "v2-runtime-topology-link v2-runtime-topology-link--run"
        : "v2-runtime-topology-link")
      .attr("d", link => {
        const middle = (link.source.y + link.target.y) / 2;
        return `M${link.source.y},${link.source.x} C${middle},${link.source.x} ${middle},${link.target.x} ${link.target.y},${link.target.x}`;
      });

    const groups = graph.selectAll("g.v2-runtime-topology-node")
      .data(descendants)
      .join("g")
      .attr("class", item => item.data.event.synthetic_root
        ? "v2-runtime-topology-node v2-runtime-topology-node--root"
        : "v2-runtime-topology-node")
      .attr("transform", item => `translate(${item.y} ${item.x})`)
      .attr("role", item => item.data.event.synthetic_root ? "presentation" : "treeitem")
      .attr("tabindex", item => item.data.event.synthetic_root ? null : 0)
      .attr("aria-label", item => item.data.event.synthetic_root
        ? null
        : `${item.data.event.subagent_id}, ${item.data.event.status || item.data.event.phase || "observé"}`)
      .on("click", (_event, item) => {
        if (item.data.event.synthetic_root) return;
        selectedId = item.data.event.subagent_id;
        renderDetail(item.data.event);
        void render();
      })
      .on("keydown", (event, item) => {
        if (item.data.event.synthetic_root || (event.key !== "Enter" && event.key !== " ")) return;
        event.preventDefault();
        selectedId = item.data.event.subagent_id;
        renderDetail(item.data.event);
        void render();
      });

    groups.append("circle")
      .attr("r", item => item.data.event.synthetic_root ? 8 : 10)
      .attr("data-phase", item => item.data.event.phase || "observed")
      .attr("data-selected", item => item.data.event.subagent_id === selectedId ? "true" : "false");

    groups.append("text")
      .attr("x", 16)
      .attr("y", 4)
      .text(item => item.data.event.synthetic_root ? "Hermes run" : item.data.event.subagent_id);

    if (selectedId && nodes.has(selectedId)) renderDetail(nodes.get(selectedId));
    else renderDetail(null);
    if (cycleDetected) setState(`${nodes.size} workers · relation cyclique coupée`);
  }

  window.PantheonRuntimeTopology = Object.freeze({ reset, consume: mergeEvent });
  reset("");
})();
