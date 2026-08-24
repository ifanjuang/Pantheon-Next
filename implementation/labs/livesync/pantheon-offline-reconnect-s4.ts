import { execFileSync, spawn } from "node:child_process";
import { access, mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";

import { evalObsidianJson } from "../runner/cli.ts";
import {
    assertCouchDbReachable,
    createCouchDbDatabase,
    deleteCouchDbDatabase,
    loadCouchDbConfig,
    makeUniqueDatabaseName,
    waitForCouchDbDocs,
} from "../runner/couchdb.ts";
import { discoverObsidianCli, requireObsidianBinary } from "../runner/environment.ts";
import {
    assertEqual,
    createE2eCouchDbPluginData,
    createE2eObsidianDeviceLocalState,
    prepareRemote,
    pushLocalChanges,
    waitForLiveSyncCoreReady,
    waitForLocalDatabaseEntry,
} from "../runner/liveSyncWorkflow.ts";
import { startObsidianLiveSyncSession, type ObsidianLiveSyncSession } from "../runner/session.ts";
import { createTemporaryVault } from "../runner/vault.ts";

process.env.E2E_OBSIDIAN_CLI_TIMEOUT_MS ??= "30000";
process.env.E2E_OBSIDIAN_COUCHDB_TIMEOUT_MS ??= "30000";
process.env.E2E_OBSIDIAN_FILE_TIMEOUT_MS ??= "30000";

const liveSyncCli = resolve("src/apps/cli/dist/index.cjs");
const couchDbContainer = "couchdb-test";
const notePath = "pantheon-offline-reconnect-s4.md";
const noteContent = [
    "# Pantheon offline reconnect S4",
    "",
    "This note was created inside real Obsidian while CouchDB was stopped.",
    "A fresh LiveSync CLI consumer must retrieve the exact content after CouchDB returns.",
    "PANTHEON_LIVESYNC_OFFLINE_RECONNECT_S4",
    "",
].join("\n");
const e2eePassphrase = "pantheon-offline-reconnect-s4";

type LiveSyncCliCommand = {
    executable: string;
    prefixArgs: string[];
};

type CliResult = {
    stdout: string;
    stderr: string;
};

function resolveLiveSyncCliCommand(): LiveSyncCliCommand {
    return { executable: process.execPath, prefixArgs: [liveSyncCli] };
}

async function runLiveSyncCli(command: LiveSyncCliCommand, args: string[]): Promise<CliResult> {
    return await new Promise((resolvePromise, reject) => {
        const timeoutMs = Number(process.env.E2E_LIVESYNC_CLI_TIMEOUT_MS ?? 60000);
        const child = spawn(command.executable, [...command.prefixArgs, ...args], {
            cwd: process.cwd(),
            env: process.env,
            stdio: ["ignore", "pipe", "pipe"],
        });
        let stdout = "";
        let stderr = "";
        child.stdout.on("data", (chunk: Buffer) => {
            stdout += chunk.toString("utf-8");
        });
        child.stderr.on("data", (chunk: Buffer) => {
            stderr += chunk.toString("utf-8");
        });
        let timedOut = false;
        const timeout = setTimeout(() => {
            timedOut = true;
            child.kill("SIGTERM");
        }, timeoutMs);
        child.on("error", (error) => {
            clearTimeout(timeout);
            reject(error);
        });
        child.on("exit", (code, signal) => {
            clearTimeout(timeout);
            const result = { stdout, stderr };
            if (timedOut) {
                reject(
                    new Error(
                        `LiveSync CLI timed out after ${timeoutMs} ms\nstdout:\n${stdout}\nstderr:\n${stderr}`
                    )
                );
                return;
            }
            if (code === 0) {
                resolvePromise(result);
                return;
            }
            reject(
                new Error(
                    `LiveSync CLI failed with ${signal ? `signal ${signal}` : `exit code ${String(code)}`}\n` +
                        `stdout:\n${stdout}\nstderr:\n${stderr}`
                )
            );
        });
    });
}

async function configureLiveSyncCli(
    command: LiveSyncCliCommand,
    settingsPath: string,
    couchDb: Awaited<ReturnType<typeof loadCouchDbConfig>>,
    dbName: string
): Promise<void> {
    await runLiveSyncCli(command, ["init-settings", "--force", settingsPath]);
    const settings = JSON.parse(await readFile(settingsPath, "utf-8")) as Record<string, unknown>;
    Object.assign(settings, {
        couchDB_URI: couchDb.uri,
        couchDB_USER: couchDb.username,
        couchDB_PASSWORD: couchDb.password,
        couchDB_DBNAME: dbName,
        remoteType: "",
        liveSync: false,
        syncOnStart: false,
        syncOnSave: false,
        usePluginSync: false,
        usePluginSyncV2: true,
        useEden: false,
        customChunkSize: 60,
        sendChunksBulk: false,
        sendChunksBulkMaxSize: 1,
        chunkSplitterVersion: "v3-rabin-karp",
        readChunksOnline: true,
        disableCheckingConfigMismatch: false,
        enableCompression: false,
        hashAlg: "xxhash64",
        handleFilenameCaseSensitive: false,
        doNotUseFixedRevisionForChunks: true,
        E2EEAlgorithm: "v2",
        encrypt: true,
        passphrase: e2eePassphrase,
        usePathObfuscation: true,
        doctorProcessedVersion: "0.25.27",
        isConfigured: true,
    });
    await writeFile(settingsPath, `${JSON.stringify(settings, null, 2)}\n`, "utf-8");
}

function stopCouchDb(): void {
    execFileSync("docker", ["stop", couchDbContainer], { stdio: "inherit" });
}

function startCouchDb(): void {
    execFileSync("docker", ["start", couchDbContainer], { stdio: "inherit" });
}

async function waitForCouchDbUp(couchDb: Awaited<ReturnType<typeof loadCouchDbConfig>>): Promise<void> {
    const deadline = Date.now() + 30000;
    let lastError: unknown;
    while (Date.now() < deadline) {
        try {
            await assertCouchDbReachable(couchDb);
            return;
        } catch (error) {
            lastError = error;
            await new Promise((resolvePromise) => setTimeout(resolvePromise, 250));
        }
    }
    throw new Error(
        `CouchDB did not become reachable after restart: ${lastError instanceof Error ? lastError.message : String(lastError)}`
    );
}

async function assertCouchDbDown(couchDb: Awaited<ReturnType<typeof loadCouchDbConfig>>): Promise<void> {
    try {
        await assertCouchDbReachable(couchDb);
    } catch {
        return;
    }
    throw new Error("CouchDB remained reachable after the outage step.");
}

async function createNoteInsideRealObsidian(
    cliBinary: string,
    env: NodeJS.ProcessEnv
): Promise<void> {
    await evalObsidianJson<unknown>(
        cliBinary,
        [
            "(async()=>{",
            `const path=${JSON.stringify(notePath)};`,
            `const content=${JSON.stringify(noteContent)};`,
            "const existing=app.vault.getAbstractFileByPath(path);",
            "if(existing) await app.vault.delete(existing,true);",
            "await app.vault.create(path,content);",
            "return JSON.stringify({created:true,path});",
            "})()",
        ].join(""),
        env
    );
}

async function main(): Promise<void> {
    await access(liveSyncCli).catch(() => {
        throw new Error(`Built LiveSync CLI was not found at ${liveSyncCli}.`);
    });

    const binary = requireObsidianBinary();
    const obsidianCli = discoverObsidianCli();
    if (!obsidianCli.binary) {
        throw new Error(`Could not find obsidian-cli. Checked paths: ${obsidianCli.checked.join(", ")}`);
    }

    const couchDb = await loadCouchDbConfig();
    const dbName = makeUniqueDatabaseName(couchDb.dbPrefix, "pantheon-offline-reconnect-s4");
    const vault = await createTemporaryVault();
    const consumerState = await mkdtemp(join(tmpdir(), "livesync-offline-reconnect-consumer-"));
    const consumerDatabasePath = join(consumerState, "database");
    const consumerSettingsPath = join(consumerState, "settings.json");
    const consumerOutputPath = join(consumerState, "retrieved", notePath);
    const liveSyncCliCommand = resolveLiveSyncCliCommand();
    let session: ObsidianLiveSyncSession | undefined;
    let couchDbRunning = true;

    try {
        await assertCouchDbReachable(couchDb);
        await createCouchDbDatabase(couchDb, dbName);

        session = await startObsidianLiveSyncSession({
            binary,
            cliBinary: obsidianCli.binary,
            vault,
            startupGraceMs: Number(process.env.E2E_OBSIDIAN_STARTUP_GRACE_MS ?? 1000),
            pluginData: createE2eCouchDbPluginData(
                {
                    uri: couchDb.uri,
                    username: couchDb.username,
                    password: couchDb.password,
                    dbName,
                },
                {
                    encrypt: true,
                    passphrase: e2eePassphrase,
                    usePathObfuscation: true,
                    E2EEAlgorithm: "v2",
                }
            ),
            localStorageEntries: createE2eObsidianDeviceLocalState(vault.name),
        });
        await waitForLiveSyncCoreReady(obsidianCli.binary, session.cliEnv);
        await prepareRemote(obsidianCli.binary, session.cliEnv);
        await pushLocalChanges(obsidianCli.binary, session.cliEnv);

        stopCouchDb();
        couchDbRunning = false;
        await assertCouchDbDown(couchDb);
        console.log("Observed CouchDB outage while real Obsidian remained running.");

        await createNoteInsideRealObsidian(obsidianCli.binary, session.cliEnv);
        const localFile = await readFile(join(vault.path, notePath), "utf-8");
        assertEqual(localFile, noteContent, "Real Obsidian did not create the expected offline Markdown file.");

        const localEntry = await waitForLocalDatabaseEntry(obsidianCli.binary, session.cliEnv, notePath, {
            timeoutMs: 20000,
        });
        if (!localEntry.id || localEntry.children.length === 0) {
            throw new Error(`Offline-created note was not fully committed locally: ${JSON.stringify(localEntry)}`);
        }
        console.log("Offline-created note was committed to the real Obsidian LiveSync local database.");

        startCouchDb();
        couchDbRunning = true;
        await waitForCouchDbUp(couchDb);
        await pushLocalChanges(obsidianCli.binary, session.cliEnv);
        await waitForCouchDbDocs(couchDb, dbName, (docs) => {
            const ids = new Set(docs.map((doc) => doc._id));
            return ids.has(localEntry.id) && localEntry.children.every((childId) => ids.has(childId));
        });
        console.log("CouchDB restarted and the finite real-Obsidian replication completed.");

        await session.app.stop();
        session = undefined;

        await mkdir(consumerDatabasePath, { recursive: true });
        await configureLiveSyncCli(liveSyncCliCommand, consumerSettingsPath, couchDb, dbName);
        await runLiveSyncCli(liveSyncCliCommand, [consumerDatabasePath, "--settings", consumerSettingsPath, "sync"]);
        await mkdir(dirname(consumerOutputPath), { recursive: true });
        await runLiveSyncCli(liveSyncCliCommand, [
            consumerDatabasePath,
            "--settings",
            consumerSettingsPath,
            "pull",
            notePath,
            consumerOutputPath,
        ]);
        const retrieved = await readFile(consumerOutputPath, "utf-8");
        assertEqual(
            retrieved,
            noteContent,
            "Fresh LiveSync CLI consumer did not retrieve the offline-created note byte-for-byte."
        );
        console.log("Fresh LiveSync CLI retrieved the offline-created note with identical content after reconnection.");
    } finally {
        if (session) {
            await session.app.stop().catch(() => undefined);
        }
        if (!couchDbRunning) {
            try {
                startCouchDb();
                couchDbRunning = true;
                await waitForCouchDbUp(couchDb);
            } catch (error) {
                console.warn(error instanceof Error ? error.message : error);
            }
        }
        if (couchDbRunning) {
            await deleteCouchDbDatabase(couchDb, dbName).catch((error: unknown) => {
                console.warn(error instanceof Error ? error.message : error);
            });
        }
        await vault.dispose();
        await rm(consumerState, { recursive: true, force: true });
    }
}

main().catch((error: unknown) => {
    console.error(error instanceof Error ? error.stack : error);
    process.exit(1);
});
