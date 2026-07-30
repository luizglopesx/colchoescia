---
name: custom-int-receitas-manager
description: "Direct Projeto Receitas Manager API access. Use when the user asks about fluxo de caixa, cheques, contas a pagar, pro-labore, cartoes, DRE, pedidos de compra, resultado mensal, or financial summaries."
---

# Projeto Receitas Manager Integration

Use this skill to consult the Projeto Receitas Manager API.

Base URL:

```text
RECEITAS_MANAGER_URL
```

Bearer token:

```text
RECEITAS_MANAGER_TOKEN
```

Always normalize the base URL before making requests:

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
```

Always send:

```text
Authorization: Bearer $RECEITAS_MANAGER_TOKEN
Content-Type: application/json
```

Never print tokens. Never expose `.env` contents. Summarize large API responses instead of pasting raw JSON.

## Required Environment Variables

In the EvoNexus workspace `.env`:

```env
RECEITAS_MANAGER_URL=https://manager.senhorcolchao.com
RECEITAS_MANAGER_TOKEN=o-mesmo-valor-de-RECEITAS_MANAGER_API_TOKEN
```

`RECEITAS_MANAGER_TOKEN` is not a Supabase JWT and is not a Supabase service role key. It is a stable integration token validated by the Vercel endpoint `/api/nexus-manager`.

Do not put `SUPABASE_SERVICE_ROLE_KEY` in Nexus. That key belongs only to the Vercel/server environment.

## Base Endpoint

```text
GET $RECEITAS_MANAGER_URL/api/nexus-manager
```

## Health Check

Use this first when validating the integration:

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  -H "Content-Type: application/json" \
  "$BASE_URL/api/nexus-manager?resource=health"
```

Expected response:

```json
{"ok":true,"service":"receitas-manager"}
```

## Read Operations

This integration is read-only.

### Summary

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=summary&mes=2026-05"
```

Purpose: compact monthly financial summary.

### DRE

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=dre&mes=2026-04"
```

Purpose: monthly DRE using the same business rules shown in the DRE module.

Always use `resource=dre&mes=YYYY-MM` for DRE. Do not assemble DRE from unrelated endpoints.

DRE rules:

- Receita Bruta and CMV come from `estoque_fechamentos_mensais` from 2026-03 onward; before that, they come from `dre_metas`.
- CMV is not the same thing as paid suppliers in `fluxo_caixa`.
- Card fees already belong inside `Despesas Variáveis`; do not subtract them again as a separate line.
- Financial entries count only when the subcategory contains `Rendimento`; card/check anticipations are cash advances, not revenue.
- Personal pro-labore expenses from the Prolabore module do not belong in the company DRE.

### Cash Flow

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=fluxo-caixa&mes=2026-05&limit=100"
```

Purpose: monthly cash flow entries and totals.

### Checks

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=cheques&status=aberto&limit=100"
```

Status can be:

```text
aberto
compensado
todas
```

### Accounts Payable

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=contas-pagar&mes=2026-05&situacao=todas&limit=100"
```

Situacao can be:

```text
pago
aberto
cancelado
todas
```

### Pro-Labore

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=prolabore&mes=2026-05"
```

Optional person filter:

```text
&pessoa=Nome
```

### Cards

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=cartoes&mes=2026-05"
```

Purpose: card accounts, monthly card entries, and current accumulated card balance.

For current card balance, prefer:

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=saldo-cartoes"
```

Do not infer the current card balance from monthly `total_vendas`, `total_antecipado`, or `total_taxas`; those are monthly movements and may include anticipation of previous months.

### Purchase Orders

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=pedidos-compra&mes=2026-05&limit=100"
```

### Monthly Result

```bash
BASE_URL="${RECEITAS_MANAGER_URL%/}"
curl -s \
  -H "Authorization: Bearer $RECEITAS_MANAGER_TOKEN" \
  "$BASE_URL/api/nexus-manager?resource=resultado-mensal&limit=24"
```

Optional month filter:

```text
&mes=2026-05
```

## Write Operations

This integration is read-only. Do not create, update, or delete records through it.

## Response Handling

- For large lists, summarize counts, totals, dates, categories, and the top items.
- For DRE, use the `linhas`, `dre`, and `regras` fields returned by `resource=dre`.
- For card balance, use `resource=saldo-cartoes` or `saldos_atuais`.
- Never expose raw tokens, auth headers, `.env`, or private credentials.
