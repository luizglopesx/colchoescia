# scripts/ — utilitários do MazyOS

Scripts Node.js e Python que as skills chamam quando precisam fazer coisas fora do alcance da IA pura (gerar imagem, postar em rede social, renderizar HTML em PNG).

A pasta vem **vazia** — cada skill que precisa de script tem instrução de como criar (e geralmente é um único setup por integração que você vai ativar).

## Scripts comuns

Conforme você for ativando skills, isso aqui vai sendo populado. Lista do que cada skill espera encontrar:

| Skill | Script esperado | O que faz |
|---|---|---|
| `/carrossel` (com foto IA) | `gerar-imagem.js` | Gera foto realista via OpenAI API (DALL-E 3) |
| `/carrossel` (render PNG) | `render.js` (gerado por carrossel, fica na pasta do conteúdo) | Playwright tira screenshot 1080x1350 de cada slide |
| `/aprovar-post` | `postar-instagram.js` | Publica carrossel no Instagram via Meta Graph API |
| `/aprovar-post` | `postar-facebook.js` | Publica carrossel no Facebook via Meta Graph API |
| `/anuncio-google` | (nenhum — gera CSV direto) | — |
| `/relatorio-ads` | (lê CSV exportado das plataformas) | — |

## supabase-sync-catalogo.js

Sobe fotos novas (ou alteradas) da pasta local `catalogo fotos transparente/` pro bucket Supabase Storage `catalogo-fotos-transparente`. Compara por tamanho — só envia o que for novo ou diferente.

```bash
node --env-file=.env scripts/supabase-sync-catalogo.js
```

## sync-catalogo-supabase.mjs

Traz fotos novas (ou alteradas) do bucket Supabase Storage `catalogo-fotos-transparente` pra pasta local `catalogo fotos transparente/`. Compara por eTag/MD5 — só baixa o que for novo ou diferente, nunca apaga nada local.

```bash
node --env-file=.env scripts/sync-catalogo-supabase.mjs
```

Os dois scripts usam o mesmo `.env`: `SUPABASE_URL`, `SUPABASE_BUCKET`, `SUPABASE_SERVICE_KEY` (ou `SUPABASE_ANON_KEY` se o bucket for público). Depois de rodar o de download, use `/salvar` pra commitar as fotos novas — nenhum dos dois commita ou dá push sozinho.

## Pré-requisitos comuns

A maioria dos scripts depende de:

**Node.js 20+** instalado na máquina

**.env** na raiz do projeto com as chaves de API:
```bash
OPENAI_API_KEY=sk-...               # pra gerar-imagem.js
META_PAGE_ACCESS_TOKEN=...          # pra postar-instagram.js + postar-facebook.js
META_PAGE_ID=...
META_IG_USER_ID=...
SITE_URL=https://seudominio.com.br
```

**Playwright** (pra renderizar HTML em PNG):
```bash
npm install playwright
npx playwright install chromium
```

## Como o MazyOS lida com isso

Quando você roda uma skill que precisa de script ausente, o Claude vai:

1. Detectar que falta o script
2. Te perguntar se quer configurar agora
3. Te guiar no setup das chaves de API (Meta, OpenAI, etc.)
4. Criar o script já configurado
5. Rodar a skill

Você não precisa decorar nada. Roda a skill, segue o fluxo.
