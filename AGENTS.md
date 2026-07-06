# Colchoes e Cia - MazyOS no Codex

Este projeto usa o MazyOS como sistema operacional de trabalho da Colchoes e Cia.
No Codex, a memoria oficial e portatil do projeto fica nos arquivos Markdown da pasta
`_memoria/`. Trate esses arquivos como fonte principal de contexto do negocio.

## Contexto obrigatorio

No inicio de qualquer trabalho neste projeto, ler e usar naturalmente, quando existirem:

1. `_memoria/empresa.md` - quem e a Colchoes e Cia, o que vende, equipe, publico
2. `_memoria/preferencias.md` - tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` - foco atual, prioridades e campanhas ativas
4. `_memoria/meta_integration.md` - contexto tecnico da integracao Meta, quando a tarefa envolver Instagram/Facebook

Para tarefas visuais, consultar tambem `identidade/design-guide.md`.

Nao precisa listar o que foi lido nem confirmar a leitura. Use o contexto de forma natural.

## Como responder pela marca

- Tom direto, simples, popular e honesto.
- Referencia de frase da marca: "Pensou Colchao Colchoes e Cia!"
- Evitar promessa vazia, formalidade excessiva e jargoes de marketing.
- Considerar que o publico principal e B, C e D, com foco em preco justo, acessibilidade e volume.

## Memoria no Codex

O Codex nao usa a memoria automatica interna do Claude Code. Portanto:

- Quando o usuario pedir "salva isso na memoria", "guarda isso", "lembra disso" ou algo equivalente, salvar nos arquivos `_memoria/*.md`, depois de confirmar quando a mudanca for permanente.
- Quando o usuario corrigir algo com intencao permanente, perguntar: "Quer que eu salve isso pra nao precisar repetir?"
- Se o usuario responder sim, escolher o arquivo correto:
  - Sobre o negocio, produtos, equipe, contatos ou operacao: `_memoria/empresa.md`
  - Sobre tom, estilo, linguagem, preferencias ou coisas a evitar: `_memoria/preferencias.md`
  - Sobre prioridades, metas, campanhas, prazos ou foco atual: `_memoria/estrategia.md`
  - Sobre Instagram, Facebook, tokens, workflows ou integracoes Meta: `_memoria/meta_integration.md`
  - Sobre regras de comportamento do Codex neste projeto: `AGENTS.md`

Editar com cirurgia: adicionar ou ajustar somente o trecho relevante, sem reformatar o documento inteiro.

## Comando equivalente a /atualizar

Quando o usuario disser "/atualizar", "atualiza a memoria", "varre o projeto",
"reconcilia o contexto" ou pedir uma atualizacao geral da memoria:

1. Levantar o estado real do workspace:
   - Pastas na raiz
   - Arquivos recentes nas areas de trabalho
   - Skills em `.claude/skills/`
   - Campanhas, conteudos e workflows recentes
2. Comparar com:
   - `_memoria/empresa.md`
   - `_memoria/preferencias.md`
   - `_memoria/estrategia.md`
   - `_memoria/meta_integration.md`
   - `CLAUDE.md`
   - `AGENTS.md`
   - `identidade/design-guide.md`
3. Apresentar uma lista curta do que parece desatualizado, sempre com evidencia do workspace.
4. Perguntar antes de aplicar mudancas, a menos que o usuario tenha pedido explicitamente para aplicar.
5. Se aprovado, editar os arquivos relevantes sem apagar contexto antigo.

Regras:

- Nao inventar fatos.
- Se a evidencia for ambigua, perguntar antes.
- Nao apagar conteudo historico dos arquivos de memoria.
- Se nada precisar mudar, responder: "Ta tudo coerente, nada pra atualizar."

## Skills do Claude neste projeto

As skills em `.claude/skills/` nao sao executadas nativamente pelo Codex como comandos slash.
Mesmo assim, elas sao arquivos de instrucao uteis. Quando a tarefa bater com uma skill existente,
ler o `SKILL.md` correspondente e seguir o fluxo quando fizer sentido.

Exemplos:

- Pedido de `/atualizar`: ler `.claude/skills/atualizar/SKILL.md`
- Pedido de `/salvar`, "salvar no GitHub", "commit" ou "push": ler `.claude/skills/salvar/SKILL.md`
- Pedido de carrossel: ler `.claude/skills/carrossel/SKILL.md`
- Pedido de publicacao ou agendamento: procurar skills relacionadas em `.claude/skills/`

Se uma tarefa repetivel nao tiver skill correspondente, ao concluir perguntar:
"Isso pode virar uma skill pra proxima vez. Quer que eu crie?"

## Fluxo de GitHub

Quando o usuario pedir "salvar", "salva no GitHub", "commit", "push" ou "/salvar":

1. Verificar `git status`.
2. Mostrar um resumo curto do que vai entrar.
3. Pedir ou sugerir uma mensagem de commit.
4. Fazer `git add`, `git commit` e `git push` se o usuario aprovar.

Nunca usar `--force`, `git reset --hard` ou comandos destrutivos sem pedido claro do usuario.

