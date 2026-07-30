# Estratégia

> O que importa agora. Prioridades, metas, prazos.
> O Claude usa isso pra decidir o que sugerir primeiro e o que adiar.
> Atualize sempre que as prioridades mudarem.

## Fase

Posicionamento e crescimento de presença — consolidar a Colchões e Cia como referência de preço justo e qualidade para o público B, C e D na região.

## Prioridade principal

Criar presença digital consistente e produzir conteúdo de marketing de forma regular. O gargalo de criação está sendo endereçado — pipeline de conteúdo automatizado funcionando desde 03/06/2026.

## O que está funcionando

- **Meta Graph API integrada** (18/05/2026) — publica e agenda posts no Instagram e Facebook via script Python
- **GitHub Actions ativo** — 30 workflows: 3 institucionais, 3 educativos, 5 Dia dos Namorados, 7 da série Sono, 3 da campanha Anúncio Geral Julho 2026, 3 da campanha Preço e Acesso Julho 2026, 3 da campanha Espuma ou Mola e 3 da campanha Facilidade de Pagamento
- **Agendamento Facebook local** — `facebook_publisher.py schedule_post` funcionando direto do terminal (sem depender de cron)
- **Série de conteúdo do Sono** — 7 posts educativos sobre qualidade do sono (2 semanas: 24/06–03/07 e 06–10/07/2026). Posts: acorda cansado, dor nas costas, casais brigam, acorda de madrugada, colchão afundando, alergia/espirros, tempo de trocar
- **Anúncio Geral Julho 2026** — campanha com 3 posts comerciais gerais (06, 08 e 10/07/2026), usando feed + story, agendamento Facebook e workflow Instagram
- **Higgsfield integrado** (26/06/2026) — geração de imagens de fundo via `higgsfield generate create flux_2` (CLI), substituindo dependência de bancos de imagem
- **Ciclo semanal consolidado** — 3 posts por semana (seg-qua-sex às 12h), com feed + story + legenda + agendamento Facebook + workflow Instagram

## Campanhas ativas

- **Facilidade de Pagamento** (29/07–03/08/2026) — 3 posts em `marketing/conteudo/facilidade-pagamento-2026-07/`, com publicação no Instagram via GitHub Actions em 29/07, 31/07 e 03/08. Workflows: `facilidade-pagamento-post1-2026-07-29.yml`, `facilidade-pagamento-post2-2026-07-31.yml`, `facilidade-pagamento-post3-2026-08-03.yml`

## Em desenvolvimento

- **Festa do Peão — Quarto de Visitas** (agosto/2026) — piloto em `marketing/conteudo/festa-peao-visitas-2026-08-piloto/`, com feed, legenda, fundo gerado por IA, prompt e renderizador. Ainda sem evidência de workflow ou agendamento.

## Campanhas encerradas

- **Espuma ou Mola Julho 2026** (22–27/07/2026) — 3 posts sobre a diferença entre espuma firme/densa e molas macias com pillow-top; arquivos em `marketing/conteudo/espuma-ou-mola-2026-07/`
- **Preço e Acesso Julho 2026** (15–20/07/2026) — 3 posts em `marketing/conteudo/preco-acesso-2026-07/`
- **Anúncio Geral Julho 2026** (06–10/07/2026) — 3 posts em `marketing/conteudo/anuncio-geral-2026-07/`
- **Série Sono — Semana 2** (06–10/07/2026) — 3 posts em `marketing/conteudo/sono-semana-2/`
- **Série Sono — Semana 1** (24/06–03/07/2026) — posts em `marketing/conteudo/posts-conteudo-sono/`
- **Dia dos Namorados** (01–13/06/2026)
- **Seleção de Ofertas** (15/06–01/07/2026) — campanha Meta Ads pausada em 01/07/2026; gerou 40 conversas com investimento de R$ 944,91, segundo `marketing/campanhas/relatorios/2026-07-01-comparativo-namorados-selecao-ofertas.md`
- **Posts institucionais** (04–07/06/2026)
- **Posts educativos** (08–12/06/2026)

## O que pode esperar

- Expansão para novos produtos
- Processos administrativos internos
- Próximas semanas da série Sono
