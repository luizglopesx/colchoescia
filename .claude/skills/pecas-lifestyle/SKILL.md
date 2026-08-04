---
name: pecas-lifestyle
description: "Criação de peças de conteúdo editorial/institucional com foto de fundo estilo lifestyle para Colchões e Cia — qualquer tema (sono, atendimento, entrega, dicas, datas comemorativas, casa, rotina etc), não só sono/descanso. Use quando o usuário pedir post, story ou peça de conteúdo institucional com foto ambientada + headline, tom editorial, sem preço/oferta. Para peça de venda com produto e preço, usar a skill pecas-comerciais."
---

# Peças Lifestyle

Estilo aprovado em teste com o dono em 2026-08: foto de fundo full-bleed
com gradiente + headline + subtítulo + logo. Testado contra um layout
alternativo com cartão azul e ícones — o cartão foi rejeitado (todas as
peças nesse estilo foram descartadas). Usar sempre o padrão abaixo.

O teste original foi feito com tema sono/descanso, mas o layout e o
workflow são o padrão institucional/editorial da marca — usar como
inspiração pra **qualquer tema** de conteúdo (não só sono): dicas de
cuidado com o colchão, atendimento, entrega, datas comemorativas, rotina
de casa, o que for. Trocar a cena da foto e o texto pro tema pedido,
mantendo a estrutura visual.

## Direção visual

- Foto full-bleed (ocupa a peça inteira), gradiente escuro (`rgba(0,18,45,...)`)
  aplicado de cima (quase transparente) pra baixo (quase opaco), texto sempre
  em branco por cima da parte escura.
- Headline grande e direta (1 a 3 linhas), com uma palavra ou expressão em
  destaque na cor azul claro `#00AFEF` via `<span>`.
- Subtítulo menor, uma frase de reforço, sem negrito.
- Logo branco (`logo-oficial-white.png`) pequeno, canto inferior esquerdo.
- Sem ícones, sem cartão de cor sólida, sem CTA em bloco separado — a peça
  é institucional/editorial, não comercial. Ver `pecas-comerciais` se o
  pedido for de oferta com preço.
- Ver `identidade/design-guide.md` para paleta e tipografia oficiais.

Evitar:

- Layout com cartão de cor sólida (azul) cobrindo mais de ~15-20% da peça —
  foi testado e reprovado por ficar com "parte azul grande demais" e sem
  vida.
- Ícones genéricos em círculo (testado, reprovado nesta linha de conteúdo).
- Preço, parcelamento ou qualquer elemento de oferta comercial.
- Fotos com roupa de dormir reveladora (decote, alça fina, pele exposta
  além de braços/ombros) — a marca é popular/familiar, precisa ficar
  confortável pra qualquer público. Ver detalhe abaixo.

## Workflow

1. **Gerar a foto de fundo** com o Higgsfield CLI (ferramenta padrão do
   projeto, ver `higgsfield-imagens` na memória):
   ```
   higgsfield generate create <modelo> --prompt "..." --aspect_ratio 3:4 --resolution 2k --wait --wait-timeout 15m --json
   ```
   Baixar o `result_url` retornado com `curl` pro arquivo `bg-<tema>.png`.
2. **Misturar modelos** a cada nova leva de peças em vez de repetir sempre
   o mesmo — variedade visual importa. Modelos já testados e aprovados:
   `flux_2`, `nano_banana_2`, `seedream_v4_5`, `gpt_image_2`,
   `text2image_soul_v2`, `soul_cinematic`, `kling_omni_image`,
   `openai_hazel`, `z_image`, `marketing_studio_image`. Ver
   `higgsfield model list` pra outras opções.
3. **Montar a peça** copiando `references/template.html`, trocando
   `bg-peca-01.png` pela imagem gerada, o `id`, a headline e o subtítulo.
4. **Renderizar** com `references/render.js` (Playwright) — ajustar as
   listas `FEED_IDS`/`STORY_IDS` no topo do script antes de rodar.
   - Feed: 1080×1350 (padrão, sempre gerar)
   - Story: 1080×1920 (gerar quando o pedido for de campanha completa)
5. Conferir visualmente antes de entregar.

## Prompt de geração da foto — regras obrigatórias

Todo prompt de imagem com pessoa precisa incluir, sempre (adaptar a cena
pro tema pedido — quarto/cama é só o exemplo do teste original; pode ser
loja, sala, cozinha, entrega, qualquer cenário coerente com o tema):

- Roupa/figurino totalmente coberto e modesto, nunca decote, alça fina
  ou pele exposta além de braços/ombros: `"fully covered, modest
  clothing"`, `"family-friendly editorial photography"` — a marca é
  popular/familiar, precisa ficar confortável pra qualquer público.
- Enquadramento correto do sujeito: `"face and upper body clearly
  visible and well framed"` — sem isso o assunto pode sair cortado ou
  fora de quadro (aconteceu num teste anterior).
- Composição vertical com espaço vazio no terço inferior pro texto:
  `"vertical composition, empty space at the bottom third for text
  overlay"`.
- Tom fotográfico consistente: `"photorealistic ... warm/soft natural
  light ... editorial photography style"`.

Representatividade: a marca atende público de 25 a 65 anos (ver
`_memoria/empresa.md`) — variar entre homem sozinho, mulher sozinha,
casal jovem, casal mais velho, e cenas sem pessoas (ambiente, produto,
detalhe) pra não depender sempre de um modelo humano.

## Exemplos aprovados (tema sono — usar como referência de composição, não de conteúdo)

12 peças finais aprovadas pelo dono estão em `references/exemplos/`
(teste-02, 03, 05, 06, 09, 10, 12, 13, 14, 16, 17, 19). O tema testado
foi sono/descanso, mas o que importa reaproveitar é a **composição**:
enquadramento de foto, peso da headline, gradiente, posição do logo.
Pra um tema novo, gerar uma foto de fundo condizente com o tema e
escrever headline/subtítulo próprios — não reciclar o texto de sono.

Headlines do teste original, como referência de tom (direto, simples,
grudento — ver `_memoria/preferencias.md`):

- "O colchão certo pode transformar suas noites de sono." / "Na Colchões
  e Cia, a gente ajuda você a escolher sem enrolação."
- "Pensou colchão, pensou Colchões e Cia." / "Do jeito que você merece
  dormir."
- "Descansar bem não é luxo, é necessidade." / "Escolha o colchão certo
  aqui na Colchões e Cia."

Nunca CTA de WhatsApp em peça institucional; se precisar de contato,
usar 📞 (17) 3325-6039.

## Prompt para o usuário pedir

Quando o usuário perguntar como pedir, sugerir:

```text
Faça uma peça de conteúdo lifestyle sobre [qualquer tema], estilo
editorial: foto de fundo ambientada, gradiente escuro, headline forte
com palavra em destaque, subtítulo curto, logo branco no rodapé. Sem
preço, sem oferta.

Tema: [ex: "dor nas costas ao acordar", "entrega no mesmo dia", "dia dos pais"]
Formatos: feed 1080x1350 [+ story 1080x1920 se for campanha]
```
