import { spawn, spawnSync } from "node:child_process";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";

const PAGE_URL = "http://127.0.0.1:4173/";
const DEBUG_URL = "http://127.0.0.1:9222/json/list";
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function executable(candidates) {
  for (const candidate of candidates) {
    const result = spawnSync("which", [candidate], { encoding: "utf-8" });
    if (result.status === 0 && result.stdout.trim()) return result.stdout.trim();
  }
  throw new Error(`No headless Chrome binary found (${candidates.join(", ")})`);
}

async function waitForHttp(url, attempts = 80) {
  let lastError = null;
  for (let attempt = 0; attempt < attempts; attempt += 1) {
    try {
      const response = await fetch(url);
      if (response.ok) return response;
      lastError = new Error(`${url} returned ${response.status}`);
    } catch (error) {
      lastError = error;
    }
    await sleep(100);
  }
  throw lastError || new Error(`Timed out waiting for ${url}`);
}

function collectOutput(child) {
  let output = "";
  child.stdout?.on("data", (chunk) => {
    output += chunk.toString();
  });
  child.stderr?.on("data", (chunk) => {
    output += chunk.toString();
  });
  return () => output;
}

async function stop(child) {
  if (!child || child.exitCode !== null) return;

  await new Promise((resolve) => {
    let settled = false;
    let forceTimer;
    let finishTimer;

    const finish = () => {
      if (settled) return;
      settled = true;
      clearTimeout(forceTimer);
      clearTimeout(finishTimer);
      child.removeListener("exit", finish);
      resolve();
    };

    child.once("exit", finish);
    try {
      child.kill("SIGTERM");
    } catch {
      finish();
      return;
    }

    forceTimer = setTimeout(() => {
      if (child.exitCode === null) {
        try {
          child.kill("SIGKILL");
        } catch {
          // Best-effort cleanup only.
        }
      }
      finishTimer = setTimeout(finish, 500);
    }, 750);
  });
}

async function connectCdp(webSocketUrl) {
  const socket = new WebSocket(webSocketUrl);
  await new Promise((resolve, reject) => {
    const timeout = setTimeout(() => reject(new Error("Timed out opening Chrome DevTools socket")), 5000);
    socket.addEventListener(
      "open",
      () => {
        clearTimeout(timeout);
        resolve();
      },
      { once: true },
    );
    socket.addEventListener(
      "error",
      () => {
        clearTimeout(timeout);
        reject(new Error("Chrome DevTools socket failed to open"));
      },
      { once: true },
    );
  });

  let nextId = 0;
  const pending = new Map();
  socket.addEventListener("message", (event) => {
    const message = JSON.parse(String(event.data));
    if (!message.id || !pending.has(message.id)) return;
    const { resolve, reject } = pending.get(message.id);
    pending.delete(message.id);
    if (message.error) reject(new Error(JSON.stringify(message.error)));
    else resolve(message.result);
  });

  function send(method, params = {}) {
    const id = ++nextId;
    return new Promise((resolve, reject) => {
      pending.set(id, { resolve, reject });
      socket.send(JSON.stringify({ id, method, params }));
    });
  }

  async function evaluate(expression) {
    const result = await send("Runtime.evaluate", {
      expression,
      awaitPromise: true,
      returnByValue: true,
    });
    if (result.exceptionDetails) {
      throw new Error(result.exceptionDetails.exception?.description || "Browser evaluation failed");
    }
    return result.result?.value;
  }

  return { socket, send, evaluate };
}

const profile = await mkdtemp(join(tmpdir(), "pantheon-a2ui-chrome-"));
let preview;
let chrome;
let previewOutput = () => "";
let chromeOutput = () => "";

try {
  preview = spawn(
    process.execPath,
    ["./node_modules/vite/bin/vite.js", "preview", "--host", "127.0.0.1", "--port", "4173", "--strictPort"],
    { stdio: ["ignore", "pipe", "pipe"] },
  );
  previewOutput = collectOutput(preview);
  await waitForHttp(PAGE_URL);

  const chromeBin = process.env.CHROME_BIN || executable(["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]);
  chrome = spawn(
    chromeBin,
    [
      "--headless=new",
      "--no-sandbox",
      "--disable-gpu",
      "--remote-debugging-address=127.0.0.1",
      "--remote-debugging-port=9222",
      `--user-data-dir=${profile}`,
      PAGE_URL,
    ],
    { stdio: ["ignore", "pipe", "pipe"] },
  );
  chromeOutput = collectOutput(chrome);

  let target = null;
  for (let attempt = 0; attempt < 80 && !target; attempt += 1) {
    try {
      const response = await fetch(DEBUG_URL);
      if (response.ok) {
        const targets = await response.json();
        target = targets.find((candidate) => candidate.type === "page" && candidate.url.startsWith(PAGE_URL));
      }
    } catch {
      // Chrome may still be starting.
    }
    if (!target) await sleep(100);
  }
  if (!target?.webSocketDebuggerUrl) {
    throw new Error("Chrome DevTools page target was not available");
  }

  const cdp = await connectCdp(target.webSocketDebuggerUrl);
  await cdp.send("Runtime.enable");

  const rendered = await cdp.evaluate(`(async () => {
    function deepText(node) {
      let text = node.nodeType === Node.TEXT_NODE ? (node.textContent || "") : "";
      if (node instanceof Element && node.shadowRoot) text += deepText(node.shadowRoot);
      for (const child of node.childNodes || []) text += deepText(child);
      return text;
    }
    for (let attempt = 0; attempt < 100; attempt += 1) {
      const text = deepText(document);
      if (text.includes("Synthèse de recherche") && text.includes("Approfondir avec Hermès")) {
        return {
          title: text.includes("ventilation et qualité d’air intérieur"),
          action: text.includes("Approfondir avec Hermès"),
          surfaceChildren: document.querySelector("#surface-host")?.children.length || 0,
        };
      }
      await new Promise((resolve) => setTimeout(resolve, 50));
    }
    throw new Error("A2UI surface did not render the expected fixture text");
  })()`);

  if (!rendered?.title || !rendered?.action || rendered.surfaceChildren !== 1) {
    throw new Error(`Unexpected rendered A2UI surface: ${JSON.stringify(rendered)}`);
  }

  const clicked = await cdp.evaluate(`(() => {
    function deepText(node) {
      let text = node.nodeType === Node.TEXT_NODE ? (node.textContent || "") : "";
      if (node instanceof Element && node.shadowRoot) text += deepText(node.shadowRoot);
      for (const child of node.childNodes || []) text += deepText(child);
      return text;
    }
    function findButton(node) {
      if (node instanceof HTMLButtonElement && deepText(node).includes("Approfondir avec Hermès")) return node;
      if (node instanceof Element && node.shadowRoot) {
        const inShadow = findButton(node.shadowRoot);
        if (inShadow) return inShadow;
      }
      for (const child of node.children || []) {
        const found = findButton(child);
        if (found) return found;
      }
      return null;
    }
    const button = findButton(document);
    if (!button) return false;
    button.click();
    return true;
  })()`);
  if (!clicked) throw new Error("Rendered A2UI action button was not found");

  const intent = await cdp.evaluate(`(async () => {
    for (let attempt = 0; attempt < 50; attempt += 1) {
      const text = document.querySelector("#intent-output")?.textContent || "";
      if (text.includes("pantheon.prepare_hermes_handoff")) return JSON.parse(text);
      await new Promise((resolve) => setTimeout(resolve, 20));
    }
    throw new Error("Bounded A2UI intent was not captured after click");
  })()`);

  if (
    intent?.action !== "pantheon.prepare_hermes_handoff" ||
    intent?.executed !== false ||
    intent?.persisted !== false ||
    intent?.authorized !== false
  ) {
    throw new Error(`A2UI action escaped the bounded intent contract: ${JSON.stringify(intent)}`);
  }

  cdp.socket.close();
  console.log(
    JSON.stringify(
      {
        rendered: true,
        action_clicked: true,
        intent: {
          action: intent.action,
          executed: intent.executed,
          persisted: intent.persisted,
          authorized: intent.authorized,
        },
      },
      null,
      2,
    ),
  );
} catch (error) {
  console.error("A2UI browser smoke failed:", error);
  if (previewOutput()) console.error("Vite preview output:\n" + previewOutput());
  if (chromeOutput()) console.error("Chrome output:\n" + chromeOutput());
  process.exitCode = 1;
} finally {
  await stop(chrome);
  await stop(preview);
  try {
    await rm(profile, { recursive: true, force: true, maxRetries: 10, retryDelay: 100 });
  } catch (error) {
    console.warn(`A2UI browser smoke cleanup warning: ${error.message}`);
  }
}
