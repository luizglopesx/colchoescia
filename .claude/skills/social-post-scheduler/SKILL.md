---
name: social-post-scheduler
description: "Agenda posts no Instagram e Facebook automaticamente via Meta Graph API. Use quando o usuário quiser agendar um post, programar publicação, agendar para uma data específica, ou quando mencionar 'agendar post', 'programar publicação', 'postar no dia X'. Suporta foto, carrossel, story e posts no Facebook. Suporta múltiplas contas (senhor_colchao, colchoes_e_cia)."
---

# Social Post Scheduler

Agenda publicações no Instagram e Facebook via Meta Graph API — sem precisar abrir o Meta Business Suite.

## Contas disponíveis

- `senhor_colchao` — Instagram @senhorcolchao + Página Senhor Colchão
- `colchoes_e_cia` — Instagram @colchoesecia + Página Colchoes e Cia

## Como usar esta skill

Quando o usuário quiser agendar um post:

1. **Colete as informações** necessárias (veja Input Gathering abaixo)
2. **Converta a data/hora** para Unix timestamp (fuso: America/Sao_Paulo = UTC-3)
3. **Execute o scheduler** via script Python
4. **Confirme** com os IDs retornados

## Input Gathering

Pergunte apenas o que o usuário não forneceu:

- **Arte**: caminho do arquivo PNG/JPG ou URL pública da imagem
- **Legenda**: texto do post (se não fornecida, peça ou gere)
- **Data e hora**: ex: "19/05 às 10h" → converta para Unix timestamp
- **Plataforma(s)**: Instagram, Facebook ou ambos (padrão: ambos)
- **Tipo**: feed, carrossel ou story (padrão: feed)
- **Conta(s)**: senhor_colchao, colchoes_e_cia ou ambas (padrão: senhor_colchao)

Se o usuário fornecer tudo, execute direto sem perguntar.

## Conversão de data para Unix timestamp

Fuso horário: America/Sao_Paulo (UTC-3)
Fórmula: timestamp_utc = timestamp_local + 3*3600

Exemplos:
- "19/05/2026 às 10h" → 2026-05-19 10:00 BRT → 2026-05-19 13:00 UTC → unix: 1747656000
- "26/05/2026 às 09h" → unix: 1748257200

## Execução

```bash
# Agendar foto no Instagram
python3 {project-root}/.claude/skills/int-instagram/scripts/instagram_publisher.py schedule_photo <image_url> "<caption>" <unix_ts> [account]

# Agendar foto no Facebook
python3 {project-root}/.claude/skills/int-instagram/scripts/facebook_publisher.py schedule_post "<message>" <unix_ts> [image_url] [account]

# Agendar carrossel no Instagram
python3 {project-root}/.claude/skills/int-instagram/scripts/instagram_publisher.py schedule_carousel <img1,img2,img3> "<caption>" <unix_ts> [account]

# Listar posts agendados
python3 {project-root}/.claude/skills/int-instagram/scripts/instagram_publisher.py scheduled [account]
python3 {project-root}/.claude/skills/int-instagram/scripts/facebook_publisher.py scheduled [account]
```

## Importante: imagens precisam de URL pública

A Meta Graph API exige URLs públicas para as imagens (não aceita caminhos locais).

Se o usuário fornecer um arquivo local (ex: `workspace/marketing/arte.png`), use o script de upload:

```bash
python3 {project-root}/.claude/skills/social-post-scheduler/scripts/upload_image.py <caminho_local>
```

Ele retorna uma URL pública temporária via Imgur ou similar.

## Output esperado

Após agendar, confirme com:
- ✅ Plataforma + conta
- 📅 Data/hora agendada (no fuso BRT)
- 🆔 ID do post agendado
- 🖼️ Tipo de conteúdo (foto/carrossel/story)

## Notas
- Posts agendados ficam visíveis no Meta Business Suite em "Ferramentas de publicação → Posts agendados"
- A Meta exige que o agendamento seja com no mínimo 10 minutos de antecedência e no máximo 29 dias
- Stories não suportam agendamento via API — apenas feed e carrossel
