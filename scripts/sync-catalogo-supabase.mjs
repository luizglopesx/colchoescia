// Sincroniza "catalogo fotos transparente/" com o bucket Supabase Storage.
// Baixa arquivos novos ou alterados (compara pelo eTag/MD5); nunca apaga nada localmente.
// Uso: node --env-file=.env scripts/sync-catalogo-supabase.js

import { createHash } from "node:crypto";
import { mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_KEY = process.env.SUPABASE_SERVICE_KEY || process.env.SUPABASE_ANON_KEY;
const BUCKET = process.env.SUPABASE_BUCKET || "catalogo-fotos-transparente";
const DEST_ROOT = path.join(import.meta.dirname, "..", "catalogo fotos transparente");

if (!SUPABASE_URL || !SUPABASE_KEY) {
  console.error("Faltam envs: SUPABASE_URL e SUPABASE_SERVICE_KEY (ou SUPABASE_ANON_KEY). Confira o .env.");
  process.exit(1);
}

function apiHeaders() {
  return {
    Authorization: `Bearer ${SUPABASE_KEY}`,
    apikey: SUPABASE_KEY,
  };
}

async function listFolder(prefix) {
  const res = await fetch(`${SUPABASE_URL}/storage/v1/object/list/${BUCKET}`, {
    method: "POST",
    headers: { ...apiHeaders(), "Content-Type": "application/json" },
    body: JSON.stringify({ prefix, limit: 1000, offset: 0, sortBy: { column: "name", order: "asc" } }),
  });
  if (!res.ok) {
    throw new Error(`Falha ao listar "${prefix}": ${res.status} ${await res.text()}`);
  }
  return res.json();
}

// Percorre o bucket recursivamente e retorna a lista completa de arquivos (pastas viram entries com metadata: null).
async function walk(prefix, files) {
  const entries = await listFolder(prefix);
  for (const entry of entries) {
    const entryPath = prefix ? `${prefix}/${entry.name}` : entry.name;
    if (entry.metadata === null) {
      await walk(entryPath, files);
    } else {
      files.push({ path: entryPath, etag: entry.metadata.eTag?.replace(/"/g, "") });
    }
  }
  return files;
}

// scripts/supabase-sync-catalogo.js (upload) tira acentos dos nomes porque o Storage só aceita ASCII.
// Aqui, ao baixar, tratamos "Cabeceira California.png" (bucket) e "Cabeceira Califórnia.png" (local,
// versionado antes do bucket existir) como o mesmo arquivo — senão o download recria uma cópia duplicada.
function sanitizeAccents(name) {
  return name.normalize("NFD").replace(/[̀-ͯ]/g, "");
}

async function resolveLocalPath(destDir, remoteName) {
  const exactPath = path.join(destDir, remoteName);
  if (existsSync(exactPath) || !existsSync(destDir)) return exactPath;

  const siblings = await readdir(destDir);
  const match = siblings.find((name) => sanitizeAccents(name) === remoteName);
  return match ? path.join(destDir, match) : exactPath;
}

async function localMatches(localPath, remoteEtag) {
  if (!existsSync(localPath) || !remoteEtag) return false;
  const buf = await readFile(localPath);
  const localMd5 = createHash("md5").update(buf).digest("hex");
  return localMd5 === remoteEtag;
}

async function download(remotePath) {
  const encodedPath = remotePath.split("/").map(encodeURIComponent).join("/");
  const res = await fetch(`${SUPABASE_URL}/storage/v1/object/${BUCKET}/${encodedPath}`, {
    headers: apiHeaders(),
  });
  if (!res.ok) {
    throw new Error(`Falha ao baixar "${remotePath}": ${res.status} ${await res.text()}`);
  }
  return Buffer.from(await res.arrayBuffer());
}

async function main() {
  console.log(`Listando bucket "${BUCKET}"...`);
  const files = await walk("", []);
  console.log(`${files.length} arquivos encontrados no bucket.`);

  let novos = 0;
  let atualizados = 0;
  let semMudanca = 0;

  for (const file of files) {
    const segments = file.path.split("/");
    const remoteName = segments.pop();
    const destDir = path.join(DEST_ROOT, ...segments);
    const localPath = await resolveLocalPath(destDir, remoteName);
    const existiaAntes = existsSync(localPath);

    if (await localMatches(localPath, file.etag)) {
      semMudanca++;
      continue;
    }

    const buf = await download(file.path);
    await mkdir(path.dirname(localPath), { recursive: true });
    await writeFile(localPath, buf);

    if (existiaAntes) {
      atualizados++;
      console.log(`Atualizado: ${file.path}`);
    } else {
      novos++;
      console.log(`Novo: ${file.path}`);
    }
  }

  console.log("");
  console.log(`Sync concluído — ${novos} novo(s), ${atualizados} atualizado(s), ${semMudanca} sem mudança.`);
  if (novos + atualizados > 0) {
    console.log(`Rode /salvar (ou git add/commit/push) pra versionar as fotos novas.`);
  }
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
