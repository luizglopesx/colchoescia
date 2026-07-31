const { createClient } = require('@supabase/supabase-js');

/**
 * Cliente Supabase reutilizavel.
 * useServiceKey: true -> acesso admin (bypassa RLS), pra scripts de automacao.
 * useServiceKey: false -> acesso publico (anon key), pra leitura respeitando RLS.
 */
function getSupabaseClient({ useServiceKey = true } = {}) {
  const url = process.env.SUPABASE_URL;
  const key = useServiceKey
    ? process.env.SUPABASE_SERVICE_KEY
    : process.env.SUPABASE_ANON_KEY;

  if (!url || !key) {
    throw new Error(
      'Faltam variaveis do Supabase no .env (SUPABASE_URL e SUPABASE_SERVICE_KEY/SUPABASE_ANON_KEY).'
    );
  }

  return createClient(url, key, {
    auth: { persistSession: false },
  });
}

module.exports = { getSupabaseClient };
