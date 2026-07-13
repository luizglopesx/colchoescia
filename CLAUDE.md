# Colchões e Cia — MazyOS

Empresa de varejo de colchões e produtos de dormitório, posicionada para o público B, C e D. Equipe de 3 pessoas: dono (administração), Otávio (marketing) e Joaquim (vendas). Gargalo atual: criação de conteúdo e marketing.

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é a Colchões e Cia, o que vende, equipe, público
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, o que tá segurando o crescimento
4. `_memoria/meta_integration.md` — contexto técnico da integração Meta, quando a tarefa envolver Instagram/Facebook

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Pra qualquer tarefa visual (carrossel, post, landing page), consultar `identidade/design-guide.md` como referência de estilo — cores `#0064A6` e `#00AFEF`, fonte Arial Rounded MT Bold.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## O que é esse workspace

Operação da Colchões e Cia. Marketing, vendas, conteúdo e administração num só lugar.

**Estrutura de pastas:**
- `_memoria/` — quem é a empresa, como falamos, foco atual, integração Meta
- `identidade/` — marca aplicada em tudo que o sistema gera
- `marketing/` — campanhas, conteúdo gerado, mídia paga
- `marketing/conteudo/` — posts gerados (HTML, PNGs, legendas, scripts de publicação) organizados em séries (ex: `posts-conteudo-sono/`, `sono-semana-2/`)
- `marketing/campanhas/` — campanhas com roteiro, legendas e assets
- `.github/workflows/` — automação de publicação via GitHub Actions cron
- `.claude/skills/int-instagram/scripts/` — scripts de integração Meta (instagram_publisher.py, facebook_publisher.py)
- `saidas/` — documentos pontuais gerados
- `dados/` — arquivos a analisar (CSV, XLSX, PDF)
- `scripts/` — automações e utilitários

---

## Sobre a empresa

Colchões e Cia é uma empresa de varejo de produtos para dormitório. Atua no segmento popular (público B, C, D), com foco em acessibilidade e volume. Vende colchões de espuma, colchões de molas, cama box, cabeceiras e box baú. Faz parte de um grupo com outras unidades voltadas a públicos de maior poder aquisitivo.

**Equipe:**
- Dono — administração geral
- Otávio — marketing
- Joaquim — vendas

---

## Tom de voz

Direto, simples, grudento. Referência real: "Pensou Colchão Colchões e Cia!" — curto, sem enrolação, fácil de gravar. Comunicação honesta, sem promessa vazia, sem jargão de guru.

Evitar: incoerência, falta de transparência, brincadeiras fora de contexto, promessas vazias, "alavancar", "sinergia", tom formal demais.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante em `.claude/skills/`. Se encontrar, seguir as instruções da skill. Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível, perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

---

## Aprender com correções

Quando o usuário corrigir algo ou dar instrução permanente ("na verdade é assim", "não faça mais isso", "prefiro assim", "sempre que...", "evita..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde salvar:
- **Sobre o negócio** → `_memoria/empresa.md`
- **Sobre preferências e estilo** → `_memoria/preferencias.md`
- **Sobre prioridades e foco** → `_memoria/estrategia.md`
- **Regra de comportamento nessa pasta** → próprio `CLAUDE.md`

---

## Manter contexto atualizado

Ao terminar tarefa que mudou algo relevante, perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

**Quando NÃO perguntar:** tarefas pontuais sem impacto no contexto, perguntas simples, mudanças já salvas.

---

## Criação de skills

Quando o usuário pedir skill nova:

1. Verificar se existe template relevante em `templates/skills/`
2. Perguntar se é específica desse projeto ou útil em qualquer contexto
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` pra calibrar ao contexto da Colchões e Cia
4. Seguir o fluxo da skill-creator nativa do Claude Code
