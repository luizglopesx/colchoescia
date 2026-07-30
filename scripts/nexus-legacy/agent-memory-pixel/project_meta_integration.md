---
name: Integração Meta — Publicação e Campanhas
description: Credenciais e módulos configurados para publicação automática no Instagram/Facebook e criação de campanhas pagas via Meta Graph API
type: project
---

Integração completa com a Meta Graph API configurada em 18/05/2026.

**App Meta:** `Senhor Colchao - Publicacao` (ID configurado via `META_APP_ID` no `.env`)
Casos de uso: Gerenciar mensagens e conteúdo no Instagram + Gerenciar tudo na sua Página.

## Contas configuradas no .env

| Variável | Conta | ID |
|---|---|---|
| SOCIAL_INSTAGRAM_1 | senhor_colchao (@senhorcolchao) | 17841406065994132 |
| SOCIAL_FACEBOOK_1 | senhor_colchao (Página Senhor Colchão) | 142661446468130 |
| SOCIAL_INSTAGRAM_2 | colchoes_e_cia (@colchoesecia) | 17841400910282540 |
| SOCIAL_FACEBOOK_2 | colchoes_e_cia (Página Colchoes e Cia) | 297774650240571 |
| SOCIAL_META_ADS_1 | senhor_colchao | act_888195439518063 |
| SOCIAL_META_ADS_2 | colchoes_e_cia | act_1502183783676579 |

Tokens: Page Access Tokens permanentes (não expiram enquanto a senha não mudar).

## Módulos criados

Todos em `/workspace/.claude/skills/int-instagram/scripts/`:

- `instagram_publisher.py` — publish_photo, publish_carousel, publish_story, schedule_photo, schedule_carousel, get_scheduled_posts
- `facebook_publisher.py` — publish_post, schedule_post, get_scheduled_posts, delete_post
- `meta_ads_client.py` — create_campaign, create_ad_set, create_creative, create_ad, get_ad_insights

## Skill criada

- `social-post-scheduler` — agenda posts no Instagram e Facebook automaticamente
  - Upload de imagens locais: `.claude/skills/social-post-scheduler/scripts/upload_image.py` (via Imgur)
  - Fuso horário: America/Sao_Paulo (UTC-3) — unix_ts = local + 3*3600

**Why:** Configurado para automatizar os agendamentos da próxima campanha sem precisar acessar o Meta Business Suite manualmente.
**How to apply:** Ao planejar campanhas, usar a skill `social-post-scheduler` para agendar diretamente. Para campanhas pagas, usar `meta_ads_client.py`.
