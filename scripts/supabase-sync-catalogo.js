const fs = require('fs');
const path = require('path');
const { getSupabaseClient } = require('./supabase-client.js');

// Sincroniza a pasta local "catalogo fotos transparente" com o bucket do Supabase.
// Sobe apenas arquivos novos ou com tamanho diferente do que ja esta no bucket.
const LOCAL_DIR = path.join(__dirname, '..', 'catalogo fotos transparente');
const BUCKET = process.env.SUPABASE_STORAGE_BUCKET || 'catalogo-fotos-transparente';

// Supabase Storage nao aceita chaves com acentos/caracteres nao-ASCII.
function sanitizeKey(name) {
  return name.normalize('NFD').replace(/[̀-ͯ]/g, '');
}

function listLocalFiles(dir, base = '') {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  let files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    const remoteName = sanitizeKey(entry.name);
    const remotePath = base ? `${base}/${remoteName}` : remoteName;
    if (entry.isDirectory()) {
      files = files.concat(listLocalFiles(fullPath, remotePath));
    } else if (/\.(png|jpe?g|webp)$/i.test(entry.name)) {
      files.push({ fullPath, remotePath: remotePath.replace(/\\/g, '/') });
    }
  }
  return files;
}

async function listRemoteFiles(supabase, prefix = '') {
  const { data, error } = await supabase.storage.from(BUCKET).list(prefix, { limit: 1000 });
  if (error) throw new Error(`Erro listando "${prefix}": ${error.message}`);

  let files = {};
  for (const item of data) {
    const itemPath = prefix ? `${prefix}/${item.name}` : item.name;
    if (item.id === null && item.metadata === null) {
      // pasta
      const nested = await listRemoteFiles(supabase, itemPath);
      files = { ...files, ...nested };
    } else {
      files[itemPath] = item.metadata?.size ?? null;
    }
  }
  return files;
}

async function main() {
  if (!fs.existsSync(LOCAL_DIR)) {
    console.error(`Pasta local nao encontrada: ${LOCAL_DIR}`);
    process.exit(1);
  }

  const supabase = getSupabaseClient();
  const localFiles = listLocalFiles(LOCAL_DIR);
  const remoteFiles = await listRemoteFiles(supabase);

  console.log(`Arquivos locais: ${localFiles.length}`);
  console.log(`Arquivos no bucket: ${Object.keys(remoteFiles).length}`);

  let uploaded = 0;
  let skipped = 0;
  let failed = 0;

  for (const { fullPath, remotePath } of localFiles) {
    const localSize = fs.statSync(fullPath).size;
    const remoteSize = remoteFiles[remotePath];

    if (remoteSize === localSize) {
      skipped++;
      continue;
    }

    const fileBuffer = fs.readFileSync(fullPath);
    const contentType = remotePath.toLowerCase().endsWith('.png')
      ? 'image/png'
      : remotePath.toLowerCase().endsWith('.webp')
      ? 'image/webp'
      : 'image/jpeg';

    const { error } = await supabase.storage
      .from(BUCKET)
      .upload(remotePath, fileBuffer, { contentType, upsert: true });

    if (error) {
      console.error(`FALHOU: ${remotePath} — ${error.message}`);
      failed++;
    } else {
      console.log(`OK: ${remotePath}`);
      uploaded++;
    }
  }

  console.log(`\nResumo: ${uploaded} enviados, ${skipped} ja atualizados, ${failed} falhas.`);
  if (failed > 0) process.exit(1);
}

main();
