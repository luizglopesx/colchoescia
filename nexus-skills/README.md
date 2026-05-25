# Backup de Skills Customizadas — Senhor Colchão

## Fonte oficial (versionada)

Repositório privado: `luizglopesx/cheque-manager`  
Caminho: `docs/nexus-skills/`

```
docs/nexus-skills/
├── custom-int-campaign-manager/SKILL.md
└── custom-int-receitas-manager/SKILL.md
```

O workspace do EvoNexus não tem acesso direto ao repo privado.
Este diretório (`/workspace/skill-backups/`) é o espelho local — mantido em sincronia manualmente.

## Fluxo de atualização

Sempre que uma skill for editada no EvoNexus:

1. O backup local é atualizado automaticamente em `/workspace/skill-backups/`
2. Oracle avisa para refletir a mudança no repo privado
3. Luiz Gustavo commita manualmente em `luizglopesx/cheque-manager` no caminho correspondente

## Skills disponíveis

| Skill | Descrição |
|---|---|
| `custom-int-campaign-manager` | Campaign Manager — conversas, contatos, campanhas (messenger.senhorcolchao.com) |
| `custom-int-receitas-manager` | Nexus Manager — financeiro, DRE, cheques, fluxo de caixa (manager.senhorcolchao.com) |
| `social-post-scheduler` | Agendador de posts — Instagram e Facebook via Meta Graph API |
| `meta-integration-scripts` | Módulos de publicação e campanhas pagas (instagram_publisher, facebook_publisher, meta_ads_client) |

## Como restaurar após reset do workspace

```bash
# Skills customizadas
mkdir -p /workspace/.claude/skills/custom-int-campaign-manager
cp /workspace/skill-backups/custom-int-campaign-manager/SKILL.md \
   /workspace/.claude/skills/custom-int-campaign-manager/SKILL.md

mkdir -p /workspace/.claude/skills/custom-int-receitas-manager
cp /workspace/skill-backups/custom-int-receitas-manager/SKILL.md \
   /workspace/.claude/skills/custom-int-receitas-manager/SKILL.md

# Skill de agendamento de posts
mkdir -p /workspace/.claude/skills/social-post-scheduler/scripts
cp /workspace/skill-backups/social-post-scheduler/SKILL.md \
   /workspace/.claude/skills/social-post-scheduler/SKILL.md
cp /workspace/skill-backups/social-post-scheduler/scripts/upload_image.py \
   /workspace/.claude/skills/social-post-scheduler/scripts/upload_image.py

# Scripts de publicação Meta (adicionados ao int-instagram)
cp /workspace/skill-backups/meta-integration-scripts/instagram_publisher.py \
   /workspace/.claude/skills/int-instagram/scripts/instagram_publisher.py
cp /workspace/skill-backups/meta-integration-scripts/facebook_publisher.py \
   /workspace/.claude/skills/int-instagram/scripts/facebook_publisher.py
cp /workspace/skill-backups/meta-integration-scripts/meta_ads_client.py \
   /workspace/.claude/skills/int-instagram/scripts/meta_ads_client.py
```

Se o backup local também tiver sido perdido, buscar do repo privado:
```
luizglopesx/cheque-manager → docs/nexus-skills/
```

## Variáveis de ambiente necessárias

Confirmar que `.env` contém:

```
CAMPAIGN_MANAGER_URL=https://messenger.senhorcolchao.com
CAMPAIGN_MANAGER_TOKEN=<token>

RECEITAS_MANAGER_URL=https://manager.senhorcolchao.com
RECEITAS_MANAGER_TOKEN=<token>

# Meta Integration (configurado em 18/05/2026)
META_APP_ID=1248304820712155
META_APP_SECRET=887d5065c3288934e3ce8d5d8b568f2d
SOCIAL_FACEBOOK_1_LABEL=senhor_colchao
SOCIAL_FACEBOOK_1_PAGE_ID=142661446468130
SOCIAL_FACEBOOK_1_PAGE_TOKEN=<token permanente>
SOCIAL_INSTAGRAM_1_LABEL=senhor_colchao
SOCIAL_INSTAGRAM_1_ACCOUNT_ID=17841406065994132
SOCIAL_INSTAGRAM_1_PAGE_TOKEN=<token permanente>
SOCIAL_FACEBOOK_2_LABEL=colchoes_e_cia
SOCIAL_FACEBOOK_2_PAGE_ID=297774650240571
SOCIAL_FACEBOOK_2_PAGE_TOKEN=<token permanente>
SOCIAL_INSTAGRAM_2_LABEL=colchoes_e_cia
SOCIAL_INSTAGRAM_2_ACCOUNT_ID=17841400910282540
SOCIAL_INSTAGRAM_2_PAGE_TOKEN=<token permanente>
SOCIAL_META_ADS_1_LABEL=senhor_colchao
SOCIAL_META_ADS_1_ACCOUNT_ID=act_888195439518063
SOCIAL_META_ADS_2_LABEL=colchoes_e_cia
SOCIAL_META_ADS_2_ACCOUNT_ID=act_1502183783676579
```
