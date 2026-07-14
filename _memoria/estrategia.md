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
- **GitHub Actions ativo** — 24 workflows: 3 institucionais, 3 educativos, 5 Dia dos Namorados, 7 da série Sono (24/06 a 10/07), 3 da campanha Anúncio Geral Julho 2026 e 3 da campanha Preço e Acesso Julho 2026
- **Agendamento Facebook local** — `facebook_publisher.py schedule_post` funcionando direto do terminal (sem depender de cron)
- **Série de conteúdo do Sono** — 7 posts educativos sobre qualidade do sono (2 semanas: 24/06–03/07 e 06–10/07/2026). Posts: acorda cansado, dor nas costas, casais brigam, acorda de madrugada, colchão afundando, alergia/espirros, tempo de trocar
- **Anúncio Geral Julho 2026** — campanha com 3 posts comerciais gerais (06, 08 e 10/07/2026), usando feed + story, agendamento Facebook e workflow Instagram
- **Higgsfield integrado** (26/06/2026) — geração de imagens de fundo via `higgsfield generate create flux_2` (CLI), substituindo dependência de bancos de imagem
- **Ciclo semanal consolidado** — 3 posts por semana (seg-qua-sex às 12h), com feed + story + legenda + agendamento Facebook + workflow Instagram

## Campanhas ativas

- **Série Sono — Semana 2** (06–10/07/2026) — posts em `marketing/conteudo/sono-semana-2/`: colchão afundando (06/07), alergia/espirros (08/07), tempo de trocar (10/07). Workflows: `sono-post5-2026-07-06.yml`, `sono-post6-2026-07-08.yml`, `sono-post7-2026-07-10.yml`
- **Anúncio Geral Julho 2026** (06–10/07/2026) — posts em `marketing/conteudo/anuncio-geral-2026-07/`: dormir bem (06/07), preço de vizinho (08/07), seu sono merece (10/07). Workflows: `anuncio-geral-post1-2026-07-06.yml`, `anuncio-geral-post2-2026-07-08.yml`, `anuncio-geral-post3-2026-07-10.yml`
- **Preço e Acesso Julho 2026** (15–20/07/2026) — posts em `marketing/conteudo/preco-acesso-2026-07/`: colchão bom não precisa ser caro (15/07), parcela que cabe no bolso (17/07), colchão pra cada bolso (20/07). Workflows: `preco-acesso-post1-2026-07-15.yml`, `preco-acesso-post2-2026-07-17.yml`, `preco-acesso-post3-2026-07-20.yml`. Agendamento Facebook ainda pendente (arquivo `agendar-facebook.py` pronto, aguardando o usuário rodar)

## Campanhas encerradas

- **Série Sono — Semana 1** (24/06–03/07/2026) — posts em `marketing/conteudo/posts-conteudo-sono/`
- **Dia dos Namorados** (01–13/06/2026)
- **Seleção de Ofertas** (15/06–01/07/2026) — campanha Meta Ads pausada em 01/07/2026; gerou 40 conversas com investimento de R$ 944,91, segundo `marketing/campanhas/relatorios/2026-07-01-comparativo-namorados-selecao-ofertas.md`
- **Posts institucionais** (04–07/06/2026)
- **Posts educativos** (08–12/06/2026)

## O que pode esperar

- Expansão para novos produtos
- Processos administrativos internos
- Próximas semanas da série Sono
