(function () {
  "use strict";

  const SDK = window.__HERMES_PLUGIN_SDK__;
  const registry = window.__HERMES_PLUGINS__;
  if (!SDK || !registry) return;

  const React = SDK.React;
  const hooks = SDK.hooks;
  const C = SDK.components;

  const POLICY = Object.freeze({
    mem0: {
      label: "Mem0",
      category: "Memory",
      risk: "high",
      governance: "candidate",
      scope: "project",
      reason:
        "Optional long-term memory provider. Hermes owns the runtime; Pantheon only governs what may become durable memory.",
      constraints: [
        "Only one external Hermes memory provider can be selected at a time.",
        "Provider selection does not promote content into Pantheon canonical memory.",
        "Configuration and dependencies must be ready before selection.",
      ],
    },
    n8n: {
      label: "n8n",
      category: "Automation",
      risk: "high",
      governance: "candidate",
      scope: "sandbox",
      reason:
        "Useful for deterministic integrations and recurring workflows. It complements Hermes execution; it must not become a second reasoning or approval layer.",
      constraints: [
        "The official Hermes catalog enables eight read-mostly tools by default.",
        "activate_workflow, deactivate_workflow, and container_logs are excluded by default.",
        "Installation or Hermes enablement never authorizes a workflow for a task.",
      ],
    },
    "pantheon-policy": {
      label: "Pantheon policy wiki",
      category: "Governance MCP",
      risk: "low",
      governance: "active_support",
      scope: "read_only",
      reason:
        "Gives Hermes on-demand, source-aware explanations of Pantheon structure and the reasons behind it.",
      constraints: [
        "Only list_sources, read_doctrine, and explain_governance_structure should be exposed.",
        "The Pantheon checkout must be mounted read-only.",
        "MCP sampling, prompts, and resources stay disabled.",
      ],
    },
    langgraph: {
      label: "LangGraph",
      category: "External runtime",
      risk: "critical",
      governance: "candidate",
      scope: "sandbox",
      reason:
        "A possible Hermes-side runtime for interruptible graphs. It is not the Pantheon workflow engine.",
      constraints: [
        "A native Hermes adapter and a scoped Task Contract are required before use.",
        "Graph state is runtime state, not evidence or canonical memory.",
        "No automatic install or activation is offered here.",
      ],
    },
    memvid: {
      label: "Memvid",
      category: "External memory candidate",
      risk: "high",
      governance: "watch",
      scope: "none",
      reason:
        "Interesting external memory technology, but no native Hermes memory-provider adapter is visible in the audited APIs.",
      constraints: [
        "No activation action is available until a reviewed Hermes adapter exists.",
        "Detection would not imply adoption or memory authority.",
      ],
    },
  });

  const N8N_DEFAULT_TOOLS = Object.freeze([
    "health",
    "list_workflows",
    "get_workflow",
    "find_workflows",
    "list_executions",
    "get_execution",
    "recent_failures",
    "export_workflow",
  ]);
  const N8N_WITHHELD_TOOLS = Object.freeze([
    "activate_workflow",
    "deactivate_workflow",
    "container_logs",
  ]);

  const EXTERNAL_CANDIDATES = Object.freeze([
    { id: "langgraph", aliases: ["langgraph", "langgraph-agent-stack"] },
    { id: "memvid", aliases: ["memvid"] },
  ]);

  function asArray(value) {
    return Array.isArray(value) ? value : [];
  }

  function cleanId(value) {
    return String(value || "").trim().toLowerCase();
  }

  function defaultPolicy(item) {
    return {
      label: item.name || item.id,
      category: item.kind === "mcp" ? "MCP" : item.kind === "plugin" ? "Plugin" : "Module",
      risk: "unassessed",
      governance: "detected",
      scope: "none",
      reason:
        "Observed through Hermes. No Pantheon-specific activation policy is encoded for this capability yet.",
      constraints: ["Hermes enablement does not establish task authorization."],
    };
  }

  function policyFor(item) {
    return POLICY[cleanId(item.id)] || defaultPolicy(item);
  }

  function normalizeMemory(payload) {
    const active = cleanId(payload && payload.active);
    return asArray(payload && payload.providers).map(function (provider) {
      const id = cleanId(provider.name);
      const status = String(provider.status || "unknown");
      const item = {
        id: id,
        name: provider.name || id,
        kind: "memory",
        description: provider.description || "Hermes memory provider.",
        source: "Hermes memory registry",
        listed: true,
        detected: status !== "missing",
        installed: status !== "missing",
        configured: typeof provider.configured === "boolean" ? provider.configured : null,
        enabled: active === id,
        reachable: null,
        health: "unknown",
        nativeStatus: status,
        setup: provider.setup || {},
      };
      item.policy = policyFor(item);
      return item;
    });
  }

  function normalizeMcps(catalogPayload, serverPayload, probes) {
    const catalog = asArray(catalogPayload && catalogPayload.entries);
    const servers = asArray(serverPayload && serverPayload.servers);
    const serverByName = new Map();
    servers.forEach(function (server) {
      serverByName.set(cleanId(server.name), server);
    });

    const rows = [];
    catalog.forEach(function (entry) {
      const id = cleanId(entry.name);
      const server = serverByName.get(id);
      const requiredEnv = asArray(entry.required_env);
      const probe = probes && probes[id];
      const installed = Boolean(entry.installed || server);
      const item = {
        id: id,
        name: entry.name || id,
        kind: "mcp",
        description: entry.description || "Hermes MCP catalog entry.",
        source: entry.source || "Hermes MCP catalog",
        listed: true,
        detected: installed,
        installed: installed,
        configured: requiredEnv.length ? null : installed ? true : null,
        enabled: server ? server.enabled !== false : Boolean(entry.enabled),
        reachable: probe ? Boolean(probe.ok) : null,
        health: probe ? (probe.ok ? "healthy" : "unhealthy") : "unknown",
        nativeStatus: installed ? "installed" : "catalog_only",
        requiredEnv: requiredEnv,
        needsInstall: Boolean(entry.needs_install),
        command: entry.command || (server && server.command) || null,
        args: asArray(entry.args || (server && server.args)),
        url: entry.url || (server && server.url) || null,
        installUrl: entry.install_url || null,
        installRef: entry.install_ref || null,
        bootstrap: asArray(entry.bootstrap),
        defaultEnabled: asArray(entry.default_enabled),
        selectedTools: server && Array.isArray(server.tools) ? server.tools : null,
        postInstall: entry.post_install || "",
        probe: probe || null,
        catalogEntry: true,
      };
      item.policy = policyFor(item);
      rows.push(item);
      serverByName.delete(id);
    });

    serverByName.forEach(function (server, id) {
      const probe = probes && probes[id];
      const item = {
        id: id,
        name: server.name || id,
        kind: "mcp",
        description: "MCP server configured directly in Hermes.",
        source: server.url || server.command || "Hermes configuration",
        listed: true,
        detected: true,
        installed: true,
        configured: null,
        enabled: server.enabled !== false,
        reachable: probe ? Boolean(probe.ok) : null,
        health: probe ? (probe.ok ? "healthy" : "unhealthy") : "unknown",
        nativeStatus: "configured",
        requiredEnv: [],
        needsInstall: false,
        command: server.command || null,
        args: asArray(server.args),
        url: server.url || null,
        installUrl: null,
        installRef: null,
        bootstrap: [],
        defaultEnabled: [],
        selectedTools: Array.isArray(server.tools) ? server.tools : null,
        postInstall: "",
        probe: probe || null,
        catalogEntry: false,
      };
      item.policy = policyFor(item);
      rows.push(item);
    });

    return rows.sort(function (a, b) {
      return a.name.localeCompare(b.name);
    });
  }

  function normalizePlugins(hubPayload, memoryNames) {
    return asArray(hubPayload && hubPayload.plugins)
      .filter(function (plugin) {
        const id = cleanId(plugin.name);
        return id !== "pantheon-modules" && !memoryNames.has(id);
      })
      .map(function (plugin) {
        const item = {
          id: cleanId(plugin.name),
          name: plugin.name,
          kind: "plugin",
          description: plugin.description || "Hermes plugin.",
          source: plugin.source || "Hermes plugin registry",
          listed: true,
          detected: true,
          installed: true,
          configured: null,
          enabled: plugin.runtime_status === "enabled",
          reachable: null,
          health: "unknown",
          nativeStatus: plugin.runtime_status || "unknown",
          version: plugin.version || "",
          authRequired: Boolean(plugin.auth_required),
        };
        item.policy = policyFor(item);
        return item;
      })
      .sort(function (a, b) {
        return a.name.localeCompare(b.name);
      });
  }

  function normalizeExternal(observedItems) {
    return EXTERNAL_CANDIDATES.map(function (candidate) {
      const matches = observedItems.filter(function (item) {
        const haystack = cleanId(item.id + " " + item.name + " " + item.description);
        return candidate.aliases.some(function (alias) {
          return haystack.indexOf(alias) !== -1;
        });
      });
      const policy = POLICY[candidate.id];
      return {
        id: candidate.id,
        name: policy.label,
        kind: "candidate",
        description: policy.reason,
        source: matches.length ? "Observed through Hermes APIs" : "Pantheon candidate registry",
        listed: true,
        detected: matches.length > 0,
        installed: matches.length ? matches.some(function (item) { return item.installed; }) : false,
        configured: null,
        enabled: matches.length ? matches.some(function (item) { return item.enabled; }) : false,
        reachable: null,
        health: "unknown",
        nativeStatus: matches.length ? "observed" : "no_native_adapter_observed",
        policy: policy,
      };
    });
  }

  function normalizeInventory(payloads, probes) {
    const memory = normalizeMemory(payloads.memory || {});
    const memoryNames = new Set(memory.map(function (item) { return item.id; }));
    const mcps = normalizeMcps(payloads.catalog || {}, payloads.servers || {}, probes || {});
    const plugins = normalizePlugins(payloads.hub || {}, memoryNames);
    const candidates = normalizeExternal(memory.concat(mcps, plugins));
    return { memory: memory, mcps: mcps, plugins: plugins, candidates: candidates };
  }

  function isSecretEnv(name) {
    return /(KEY|TOKEN|SECRET|PASSWORD|PASSCODE|CREDENTIAL)/i.test(String(name || ""));
  }

  function triLabel(value) {
    if (value === true) return "yes";
    if (value === false) return "no";
    return "unknown";
  }

  function triTone(value) {
    if (value === true) return "good";
    if (value === false) return "muted";
    return "unknown";
  }

  window.__PANTHEON_MODULES_TEST__ = Object.freeze({
    normalizeInventory: normalizeInventory,
    normalizeMemory: normalizeMemory,
    normalizeMcps: normalizeMcps,
    normalizePlugins: normalizePlugins,
    isSecretEnv: isSecretEnv,
    policy: POLICY,
    n8nDefaultTools: N8N_DEFAULT_TOOLS,
    n8nWithheldTools: N8N_WITHHELD_TOOLS,
  });

  function StateCell(props) {
    return React.createElement(
      "div",
      { className: "pm-state" },
      React.createElement("span", { className: "pm-state-label" }, props.label),
      React.createElement(
        "span",
        { className: "pm-state-value pm-tone-" + (props.tone || "unknown") },
        props.value,
      ),
    );
  }

  function StateGrid(props) {
    const item = props.item;
    const healthTone = item.health === "healthy" ? "good" : item.health === "unhealthy" ? "danger" : "unknown";
    return React.createElement(
      "div",
      { className: "pm-states", "aria-label": "Module states" },
      React.createElement(StateCell, { label: "Listed", value: triLabel(item.listed), tone: triTone(item.listed) }),
      React.createElement(StateCell, { label: "Detected", value: triLabel(item.detected), tone: triTone(item.detected) }),
      React.createElement(StateCell, { label: "Installed", value: triLabel(item.installed), tone: triTone(item.installed) }),
      React.createElement(StateCell, { label: "Configured", value: triLabel(item.configured), tone: triTone(item.configured) }),
      React.createElement(StateCell, { label: "Hermes enabled", value: triLabel(item.enabled), tone: triTone(item.enabled) }),
      React.createElement(StateCell, { label: "Reachable", value: triLabel(item.reachable), tone: triTone(item.reachable) }),
      React.createElement(StateCell, { label: "Health", value: item.health, tone: healthTone }),
      React.createElement(StateCell, { label: "Governance", value: item.policy.governance, tone: "policy" }),
      React.createElement(StateCell, { label: "Task use", value: "not established", tone: "danger" }),
    );
  }

  function PolicyBlock(props) {
    const policy = props.item.policy;
    return React.createElement(
      "details",
      { className: "pm-policy" },
      React.createElement("summary", null, "Why this placement"),
      React.createElement("p", null, policy.reason),
      React.createElement(
        "ul",
        null,
        policy.constraints.map(function (constraint) {
          return React.createElement("li", { key: constraint }, constraint);
        }),
      ),
    );
  }

  function McpTechnicalDetails(props) {
    const item = props.item;
    if (item.kind !== "mcp") return null;
    const defaults = item.id === "n8n" ? N8N_DEFAULT_TOOLS : item.defaultEnabled;
    return React.createElement(
      "details",
      { className: "pm-technical" },
      React.createElement("summary", null, "Hermes connection details"),
      React.createElement(
        "dl",
        null,
        React.createElement("dt", null, "Source"),
        React.createElement("dd", null, item.source || "unknown"),
        item.installRef && React.createElement("dt", null, "Pinned ref"),
        item.installRef && React.createElement("dd", { className: "pm-mono" }, item.installRef),
        item.command && React.createElement("dt", null, "Command"),
        item.command && React.createElement("dd", { className: "pm-mono" }, item.command),
        item.url && React.createElement("dt", null, "URL"),
        item.url && React.createElement("dd", { className: "pm-mono" }, item.url),
        defaults.length > 0 && React.createElement("dt", null, "Default tools"),
        defaults.length > 0 && React.createElement("dd", { className: "pm-mono" }, defaults.join(", ")),
        item.id === "n8n" && React.createElement("dt", null, "Excluded by default"),
        item.id === "n8n" && React.createElement("dd", { className: "pm-mono" }, N8N_WITHHELD_TOOLS.join(", ")),
      ),
      item.bootstrap.length > 0 && React.createElement(
        "div",
        { className: "pm-bootstrap" },
        React.createElement("strong", null, "Bootstrap to review"),
        item.bootstrap.map(function (command) {
          return React.createElement("code", { key: command }, command);
        }),
      ),
    );
  }

  function InstallForm(props) {
    const item = props.item;
    const values = props.values || {};
    return React.createElement(
      "div",
      { className: "pm-install-form" },
      React.createElement("strong", null, "Explicit Hermes install request"),
      item.requiredEnv.length === 0 && React.createElement(
        "p",
        null,
        "This catalog entry declares no required environment values.",
      ),
      item.requiredEnv.map(function (field) {
        return React.createElement(
          "label",
          { key: field.name, className: "pm-field" },
          React.createElement(
            "span",
            null,
            field.prompt || field.name,
            field.required === false ? " (optional)" : "",
          ),
          React.createElement(C.Input, {
            type: isSecretEnv(field.name) ? "password" : "text",
            autoComplete: "off",
            value: values[field.name] || "",
            placeholder: field.name,
            onChange: function (event) {
              props.onChange(field.name, event.target.value);
            },
          }),
        );
      }),
      React.createElement(
        "p",
        { className: "pm-secret-note" },
        "Values remain only in this form until submission. The plugin keeps no browser copy. Hermes persists submitted values through its native API.",
      ),
      React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(C.Button, { onClick: props.onSubmit, disabled: props.busy }, props.busy ? "Submitting…" : "Install via Hermes"),
        React.createElement(C.Button, { variant: "outline", onClick: props.onCancel, disabled: props.busy }, "Cancel"),
      ),
    );
  }

  function ModuleActions(props) {
    const item = props.item;
    const busy = props.busy === item.kind + ":" + item.id;

    if (item.kind === "candidate") {
      return React.createElement("p", { className: "pm-no-action" }, "No native activation action is exposed for this candidate.");
    }

    if (item.kind === "memory") {
      if (item.nativeStatus !== "ready") {
        return React.createElement(
          "div",
          { className: "pm-actions" },
          React.createElement(C.Button, { variant: "outline", onClick: props.onOpenNativePlugins }, "Open native setup"),
        );
      }
      return React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(
          C.Button,
          { onClick: function () { props.onMemory(item); }, disabled: busy },
          busy ? "Applying…" : item.enabled ? "Use built-in memory" : "Select in Hermes",
        ),
      );
    }

    if (item.kind === "plugin") {
      return React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(
          C.Button,
          { variant: item.enabled ? "outline" : "default", onClick: function () { props.onPlugin(item); }, disabled: busy },
          busy ? "Applying…" : item.enabled ? "Disable in Hermes" : "Enable in Hermes",
        ),
      );
    }

    if (item.kind === "mcp") {
      if (!item.installed && item.catalogEntry) {
        return React.createElement(
          "div",
          { className: "pm-actions" },
          React.createElement(
            C.Button,
            { onClick: function () { props.onPrepareInstall(item); } },
            props.installTarget === item.id ? "Install form open" : "Prepare install",
          ),
        );
      }
      return React.createElement(
        "div",
        { className: "pm-actions" },
        React.createElement(C.Button, { variant: "outline", onClick: function () { props.onProbe(item); }, disabled: busy }, "Test connection"),
        React.createElement(
          C.Button,
          { variant: item.enabled ? "outline" : "default", onClick: function () { props.onMcpToggle(item); }, disabled: busy },
          busy ? "Applying…" : item.enabled ? "Disable in Hermes" : "Enable in Hermes",
        ),
      );
    }

    return null;
  }

  function ModuleCard(props) {
    const item = props.item;
    return React.createElement(
      C.Card,
      { className: "pm-card" },
      React.createElement(
        C.CardHeader,
        { className: "pm-card-header" },
        React.createElement(
          "div",
          { className: "pm-card-title-row" },
          React.createElement(
            "div",
            null,
            React.createElement(C.CardTitle, null, item.policy.label || item.name),
            React.createElement("p", { className: "pm-native-name" }, item.name !== item.policy.label ? item.name : item.source),
          ),
          React.createElement(
            "div",
            { className: "pm-badges" },
            React.createElement(C.Badge, { variant: "outline" }, item.policy.category),
            React.createElement(C.Badge, { variant: item.policy.risk === "low" ? "secondary" : "outline", className: "pm-risk-" + item.policy.risk }, "risk: " + item.policy.risk),
          ),
        ),
      ),
      React.createElement(
        C.CardContent,
        { className: "pm-card-content" },
        React.createElement("p", { className: "pm-description" }, item.description),
        React.createElement(StateGrid, { item: item }),
        React.createElement(
          "div",
          { className: "pm-native-status" },
          React.createElement("span", null, "Native status"),
          React.createElement("code", null, item.nativeStatus),
          React.createElement("span", null, "Policy scope"),
          React.createElement("code", null, item.policy.scope),
        ),
        item.authRequired && React.createElement("p", { className: "pm-warning" }, "Hermes reports that authentication is still required."),
        item.probe && !item.probe.ok && React.createElement("p", { className: "pm-warning" }, item.probe.error || "Connection test failed."),
        item.probe && item.probe.ok && React.createElement("p", { className: "pm-success" }, "Observed " + asArray(item.probe.tools).length + " MCP tools during the latest test."),
        React.createElement(PolicyBlock, { item: item }),
        React.createElement(McpTechnicalDetails, { item: item }),
        React.createElement(ModuleActions, Object.assign({}, props, { item: item })),
        props.installTarget === item.id && React.createElement(InstallForm, {
          item: item,
          values: props.envValues[item.id] || {},
          busy: props.busy === "mcp:" + item.id,
          onChange: function (name, value) { props.onEnvChange(item.id, name, value); },
          onSubmit: function () { props.onInstall(item); },
          onCancel: props.onCancelInstall,
        }),
      ),
    );
  }

  function callApi(name) {
    const fn = SDK.api && SDK.api[name];
    if (typeof fn !== "function") {
      return Promise.reject(new Error("Hermes API method unavailable: " + name));
    }
    const args = Array.prototype.slice.call(arguments, 1);
    return Promise.resolve(fn.apply(SDK.api, args));
  }

  function PantheonModulesPage() {
    const useState = hooks.useState;
    const useEffect = hooks.useEffect;
    const useCallback = hooks.useCallback;
    const useMemo = hooks.useMemo;
    const [payloads, setPayloads] = useState({ memory: {}, catalog: {}, servers: {}, hub: {} });
    const [probes, setProbes] = useState({});
    const [loading, setLoading] = useState(true);
    const [errors, setErrors] = useState([]);
    const [message, setMessage] = useState(null);
    const [busy, setBusy] = useState("");
    const [filter, setFilter] = useState("all");
    const [query, setQuery] = useState("");
    const [installTarget, setInstallTarget] = useState("");
    const [envValues, setEnvValues] = useState({});

    const refresh = useCallback(function () {
      setLoading(true);
      const calls = [
        ["memory", "getMemory"],
        ["catalog", "getMcpCatalog"],
        ["servers", "getMcpServers"],
        ["hub", "getPluginsHub"],
      ];
      return Promise.allSettled(calls.map(function (entry) { return callApi(entry[1]); }))
        .then(function (results) {
          const next = { memory: {}, catalog: {}, servers: {}, hub: {} };
          const nextErrors = [];
          results.forEach(function (result, index) {
            const key = calls[index][0];
            if (result.status === "fulfilled") next[key] = result.value || {};
            else nextErrors.push(key + ": " + String(result.reason && result.reason.message ? result.reason.message : result.reason));
          });
          setPayloads(next);
          setErrors(nextErrors);
        })
        .finally(function () { setLoading(false); });
    }, []);

    useEffect(function () { refresh(); }, [refresh]);

    const inventory = useMemo(function () {
      return normalizeInventory(payloads, probes);
    }, [payloads, probes]);

    const sections = [
      { id: "memory", label: "Memory", items: inventory.memory },
      { id: "mcp", label: "MCP & automation", items: inventory.mcps },
      { id: "plugins", label: "Hermes plugins", items: inventory.plugins },
      { id: "candidates", label: "External candidates", items: inventory.candidates },
    ];

    const visibleSections = sections.map(function (section) {
      const needle = cleanId(query);
      const items = section.items.filter(function (item) {
        if (filter !== "all" && filter !== section.id) return false;
        if (!needle) return true;
        const haystack = cleanId(item.name + " " + item.description + " " + item.policy.category + " " + item.policy.reason);
        return haystack.indexOf(needle) !== -1;
      });
      return { id: section.id, label: section.label, items: items };
    }).filter(function (section) { return section.items.length > 0; });

    function runMutation(key, successText, action) {
      setBusy(key);
      setMessage(null);
      return Promise.resolve()
        .then(action)
        .then(function (result) {
          setMessage({ tone: "success", text: typeof successText === "function" ? successText(result) : successText });
          return refresh().then(function () { return result; });
        })
        .catch(function (error) {
          setMessage({ tone: "error", text: String(error && error.message ? error.message : error) });
          return null;
        })
        .finally(function () { setBusy(""); });
    }

    function handleMemory(item) {
      const next = item.enabled ? "" : item.id;
      const action = item.enabled ? "return to Hermes built-in memory" : "select " + item.name + " as the exclusive external memory provider";
      if (!window.confirm("Confirm: " + action + ". This changes Hermes configuration but does not promote or authorize Pantheon memory.")) return;
      runMutation("memory:" + item.id, "Hermes memory provider updated. Start a fresh session before relying on the change.", function () {
        return callApi("setMemoryProvider", next);
      });
    }

    function handlePlugin(item) {
      const verb = item.enabled ? "disable" : "enable";
      if (!window.confirm("Confirm: " + verb + " Hermes plugin '" + item.name + "'. Runtime enablement does not establish Pantheon governance activation or task authorization.")) return;
      runMutation("plugin:" + item.id, "Hermes plugin state updated. A fresh session may be required.", function () {
        return callApi(item.enabled ? "disableAgentPlugin" : "enableAgentPlugin", item.name);
      });
    }

    function handleMcpToggle(item) {
      const next = !item.enabled;
      if (!window.confirm("Confirm: " + (next ? "enable" : "disable") + " MCP server '" + item.name + "' in Hermes. This takes effect for new sessions and does not authorize its tools for a task.")) return;
      runMutation("mcp:" + item.id, "Hermes MCP state updated. Start a fresh session to load the new tool surface.", function () {
        return callApi("setMcpServerEnabled", item.name, next);
      });
    }

    function handleProbe(item) {
      if (!window.confirm("Run a Hermes connectivity test for '" + item.name + "'? The probe may start the MCP process and contact its configured service.")) return;
      setBusy("mcp:" + item.id);
      setMessage(null);
      callApi("testMcpServer", item.name)
        .then(function (result) {
          setProbes(function (current) {
            return Object.assign({}, current, { [item.id]: result || { ok: false, error: "Empty response", tools: [] } });
          });
          setMessage({ tone: result && result.ok ? "success" : "error", text: result && result.ok ? "Connection observed. This is liveness evidence, not task authorization." : (result && result.error) || "Connection test failed." });
        })
        .catch(function (error) {
          setProbes(function (current) {
            return Object.assign({}, current, { [item.id]: { ok: false, error: String(error.message || error), tools: [] } });
          });
          setMessage({ tone: "error", text: String(error.message || error) });
        })
        .finally(function () { setBusy(""); });
    }

    function handleEnvChange(id, name, value) {
      setEnvValues(function (current) {
        const nextForItem = Object.assign({}, current[id] || {}, { [name]: value });
        return Object.assign({}, current, { [id]: nextForItem });
      });
    }

    function handleInstall(item) {
      const values = envValues[item.id] || {};
      const missing = item.requiredEnv.filter(function (field) {
        return field.required !== false && !String(values[field.name] || "").trim();
      });
      if (missing.length) {
        setMessage({ tone: "error", text: "Missing required values: " + missing.map(function (field) { return field.name; }).join(", ") });
        return;
      }
      const installEffect = item.needsInstall
        ? "Hermes will clone the pinned source, run the displayed bootstrap commands, persist supplied environment values, and enable the MCP when installation completes."
        : "Hermes will persist supplied environment values and add this MCP to its configuration.";
      if (!window.confirm("Confirm installation of '" + item.name + "'. " + installEffect + " This is a privileged configuration action, not task authorization.")) return;
      runMutation(
        "mcp:" + item.id,
        function (result) {
          return result && result.background
            ? "Hermes started the background install. Refresh after the native action completes, then test the connection."
            : "Hermes installed the MCP. Test it before relying on the connection.";
        },
        function () { return callApi("installMcpCatalogEntry", item.name, values, true); },
      ).then(function (result) {
        if (!result) return;
        setEnvValues(function (current) {
          const next = Object.assign({}, current);
          delete next[item.id];
          return next;
        });
        setInstallTarget("");
      });
    }

    const actionProps = {
      busy: busy,
      installTarget: installTarget,
      envValues: envValues,
      onMemory: handleMemory,
      onPlugin: handlePlugin,
      onMcpToggle: handleMcpToggle,
      onProbe: handleProbe,
      onPrepareInstall: function (item) { setInstallTarget(item.id); setMessage(null); },
      onCancelInstall: function () { setInstallTarget(""); },
      onEnvChange: handleEnvChange,
      onInstall: handleInstall,
      onOpenNativePlugins: function () {
        const current = window.location.pathname;
        const target = current.replace(/\/pantheon-modules\/?$/, "/plugins");
        window.location.assign(target === current ? "/plugins" : target);
      },
    };

    return React.createElement(
      "div",
      { className: "pm-page" },
      React.createElement(
        "section",
        { className: "pm-hero" },
        React.createElement(
          "div",
          null,
          React.createElement("div", { className: "pm-kicker" }, "Governed module inventory"),
          React.createElement("h1", null, "Pantheon Modules"),
          React.createElement("p", null, "Hermes observes and executes. Pantheon governs. The human decides."),
        ),
        React.createElement(C.Button, { variant: "outline", onClick: refresh, disabled: loading }, loading ? "Refreshing…" : "Refresh observations"),
      ),
      React.createElement(
        "section",
        { className: "pm-boundary", role: "note" },
        React.createElement("strong", null, "State boundary"),
        React.createElement("span", null, "listed ≠ installed ≠ configured ≠ enabled ≠ reachable ≠ healthy"),
        React.createElement("span", null, "Hermes enabled ≠ Pantheon governance activation ≠ task authorization"),
      ),
      message && React.createElement("div", { className: "pm-message pm-message-" + message.tone, role: "status" }, message.text),
      errors.length > 0 && React.createElement(
        "div",
        { className: "pm-message pm-message-error", role: "alert" },
        "Partial inventory — " + errors.join(" | "),
      ),
      React.createElement(
        "div",
        { className: "pm-toolbar" },
        React.createElement(C.Input, {
          value: query,
          onChange: function (event) { setQuery(event.target.value); },
          placeholder: "Search modules, risks, or reasons",
          "aria-label": "Search modules",
        }),
        React.createElement(
          "div",
          { className: "pm-filters", "aria-label": "Module type filters" },
          [
            ["all", "All"],
            ["memory", "Memory"],
            ["mcp", "MCP"],
            ["plugins", "Plugins"],
            ["candidates", "Candidates"],
          ].map(function (entry) {
            return React.createElement(
              "button",
              { key: entry[0], className: filter === entry[0] ? "active" : "", onClick: function () { setFilter(entry[0]); } },
              entry[1],
            );
          }),
        ),
      ),
      loading && React.createElement("div", { className: "pm-loading" }, "Reading native Hermes inventories…"),
      !loading && visibleSections.length === 0 && React.createElement("div", { className: "pm-empty" }, "No modules match this view."),
      !loading && visibleSections.map(function (section) {
        return React.createElement(
          "section",
          { key: section.id, className: "pm-section" },
          React.createElement(
            "div",
            { className: "pm-section-heading" },
            React.createElement("h2", null, section.label),
            React.createElement("span", null, section.items.length + " observed/listed"),
          ),
          React.createElement(
            "div",
            { className: "pm-grid" },
            section.items.map(function (item) {
              return React.createElement(ModuleCard, Object.assign({ key: item.kind + ":" + item.id, item: item }, actionProps));
            }),
          ),
        );
      }),
    );
  }

  registry.register("pantheon-modules", PantheonModulesPage);
})();
