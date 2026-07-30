# Colchoes e Cia - MazyOS no Claude Code

Este projeto usa o MazyOS como sistema operacional de trabalho da Colchoes e Cia.
A memoria oficial e compartilhada do projeto fica nos arquivos Markdown da pasta
`_memoria/`. Nao duplicar aqui fatos do negocio, preferencias, campanhas ou contexto
tecnico.

## Contexto obrigatorio

No inicio de qualquer trabalho neste projeto, ler e usar naturalmente, quando existirem:

1. `_memoria/empresa.md` - empresa, produtos, equipe, contatos e operacao
2. `_memoria/preferencias.md` - tom de voz, estilo e coisas a evitar
3. `_memoria/estrategia.md` - prioridades, metas e campanhas
4. `_memoria/meta_integration.md` - integracoes Instagram/Facebook, quando aplicavel

Para tarefas visuais, consultar tambem `identidade/design-guide.md`.

Esses arquivos sao a fonte principal. Se houver conflito entre uma informacao deles e
uma referencia antiga em outro arquivo, usar `_memoria/` e sinalizar a divergencia.
Nao precisa listar o que foi lido nem confirmar a leitura.

## Estrutura do workspace

- `_memoria/` - memoria oficial e compartilhada
- `identidade/` - identidade visual da marca
- `marketing/` - campanhas, conteudo e midia paga
- `saidas/` - documentos pontuais gerados
- `dados/` - arquivos para analise
- `scripts/` - automacoes e utilitarios
- `.claude/skills/` - instrucoes e fluxos reutilizaveis do Claude Code
- `.github/workflows/` - automacoes do GitHub Actions

## Skills

Antes de executar uma tarefa, verificar se existe skill relevante em
`.claude/skills/`. Se existir, seguir o `SKILL.md` correspondente quando fizer sentido.

Ao concluir uma tarefa repetivel que nao tenha skill, perguntar:

> "Isso pode virar uma skill pra proxima vez. Quer que eu crie?"

Quando o usuario pedir uma skill nova:

1. Verificar se existe template relevante em `templates/skills/`
2. Perguntar se ela e especifica deste projeto ou util em qualquer contexto
3. Usar `_memoria/empresa.md` e `_memoria/preferencias.md` para calibrar a skill
4. Seguir o fluxo da skill-creator disponivel no Claude Code

## Atualizacao da memoria

Quando o usuario pedir para lembrar, guardar ou salvar uma informacao permanente,
confirmar a permanencia quando necessario e editar somente o arquivo adequado:

- Negocio, produtos, equipe, contatos ou operacao: `_memoria/empresa.md`
- Tom, linguagem, preferencias ou coisas a evitar: `_memoria/preferencias.md`
- Prioridades, metas, campanhas, prazos ou foco: `_memoria/estrategia.md`
- Instagram, Facebook, tokens, workflows ou Meta: `_memoria/meta_integration.md`
- Regras exclusivas do Claude Code neste projeto: `CLAUDE.md`
- Regras exclusivas do Codex neste projeto: `AGENTS.md`

Quando o usuario fizer uma correcao com intencao permanente, perguntar:

> "Quer que eu salve isso pra nao precisar repetir?"

Editar com cirurgia, sem reformatar toda a memoria nem apagar contexto historico.
