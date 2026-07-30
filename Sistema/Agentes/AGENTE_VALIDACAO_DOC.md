---
tags:
  - qa
  - agente
---
# Agente: Validação contra Documentação

Rede de segurança do **gate de verificação contra doc** ([[../Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]]). Varre cards aprovados ou movidos pra `Concluídas/` que ainda não passaram pelo cruzamento contra a documentação do módulo, e levanta pendências visíveis — pra não repetir o caso da SGV-9464 (aprovada em HML e só depois descoberta a divergência com a doc de Rastrear Documento). Precedente real: comportamento validado e aprovado contradizia o que a doc especificava havia 4 meses.

Não faz integração externa nem roda por conta própria em background: dispara no gatilho **já existente** de organização da daily.

## Por que existe

O gate de doc é obrigatório em dois momentos ([[../Skills/SKILL_VERIFICACAO_DOC#Gate obrigatório — antes de ✅ aprovar e antes de destilar o card|SKILL_VERIFICACAO_DOC]]):

- **Ao destilar o card** no refinamento (antes de fechar resultado esperado + critérios)
- **Antes de marcar `✅ aprovado`** numa validação DEV/HML

Mas é um passo humano, sujeito a ser pulado na pressa do dia. Este agente é a **rede de segurança**: detecta o gap depois do fato e sinaliza — não pune, não bloqueia, só garante que a pendência não morra silenciosa. O SKILL_VERIFICACAO_DOC já cobre o **como** cruzar; este agente cobre o **garantir que foi cruzado**.

## Gatilho

| Gatilho | Executor | O que acontece |
|---|---|---|
| **🔄 Atualizar** (Dashboard) | — | **Nada.** O `qa-atualiza.py` não faz gate de doc: não há uma linha sequer sobre `04 Conhecimento/` ou módulo no script. Este agente **não roda** pelo botão |
| **Sessão de IA** | Este agente | Varredura da daily, detecção de aprovação sem gate registrado e sugestão de módulo. É o **único** caminho de execução hoje |

> [!warning] Corrigido em 30/07 — a tabela anterior era falsa
> Ela dizia que "no modo 🔄 (script)" este agente fazia "a parte mecânica — varredura e detecção de ausência". **O script não faz nada disso** — verificado por busca direta: zero ocorrências de gate, módulo ou `04 Conhecimento` no `qa-atualiza.py`.
>
> Uma sessão nova lia isso e assumia que o gate de doc já tinha sido conferido pelo botão. Como este agente é justamente a **rede de segurança** contra o gate ser pulado, a rede não existia — e ninguém sabia.

## Pipeline

### 1. Varrer cards candidatos

Fontes de cards que podem ter passado pelo gate sem registro:

| Fonte | O que procura |
|---|---|
| Daily de hoje — Atividades | Linhas `✅` / `🔁` com SGV (aprovações do dia) |
| Daily de hoje — A fazer hoje | Checkboxes `[x]` com resultado de aprovação (`aprovada em <ambiente>`, `retestada e aprovada`) |
| `02 Demandas/Concluídas/` | Cards movidos recentemente (data de modificação do arquivo ≤ 2 dias) que não têm registro de gate |
| `02 Demandas/HML/` | Cards com `status: em_validacao` ou `resolvido` sem registro de gate |

**Excluir da varredura**: cards com `status: descartado`, cards em `99 Arquivo/`, cards de POC (validação exploratória), cards só de API (fluxo 3f — verificação de doc não se aplica da mesma forma).

### 2. Detectar o módulo

A detecção segue uma cascata de 3 níveis:

| Nível | Fonte | Confiança |
|---|---|---|
| **Explícito** | Campo `módulo` no frontmatter do card ou da mesa de refinamento | Alta |
| **Inferido** | Título do card, descrição do problema, nome do arquivo (ex.: "Novo rastreio de documentos" → `Rastrear Documento`; "Campo 'Para' não preenche" → depende do contexto do módulo de despacho/trâmite) | Média — sempre marcar como `(módulo inferido)` |
| **Não identificado** | Nenhuma pista clara | Baixa — tratar como caso especial |

**Regra de inferência**: buscar no título e na descrição do card por nomes de módulos conhecidos. Os módulos existentes estão listados em `04 Conhecimento/Módulos/` — a lista de arquivos `.md` nessa pasta é o catálogo de módulos disponíveis. Cruzar palavras-chave do título (substantivos próprios do domínio: "Assinatura", "Rastrear", "Workflow", "Despacho", "Trâmite", "Documento", "Processo", "Setor", "Usuário") contra os nomes dos arquivos.

### 3. Buscar a doc e classificar o gap

Para cada card candidato, verificar se **já existe** registro do gate em algum destes lugares:

- **No card**: seção Observações ou Histórico com menção a `SKILL_VERIFICACAO_DOC`, `gate de doc`, `verificado contra doc`, ou citação de um arquivo em `04 Conhecimento/Módulos/`
- **Na doc do módulo**: seção `## Comportamentos observados em teste (QA)` com o SGV
- **Na daily**: anotação `[IA]` mencionando verificação contra doc

**Se já existe registro** → pular. Card conforme.

**Se não existe registro** → classificar o gap:

| Situação | Pendência gerada | Trava? |
|---|---|---|
| Módulo explícito, doc existe | `⚠️ SGV-XXXX × doc [[<Módulo>]] — cruzar contra a doc (gate pendente)` | Sim |
| Módulo inferido, doc existe | `⚠️ SGV-XXXX × doc [[<Módulo>]] — cruzar contra a doc (gate pendente, módulo inferido)` | Sim |
| Módulo identificado, doc **não existe** | `📚 Importar doc de <Módulo> — não existe em 04 Conhecimento/Módulos/ (fluxo 8)` | Não — mas entra em Foco |
| Módulo **não identificado** | `⚠️ SGV-XXXX — gate de doc pendente (módulo não identificado — verificar card)` | Sim |
| Card de melhoria/funcionalidade nova (não é bug) sem módulo óbvio | `⚠️ SGV-XXXX — verificar se há doc de módulo relacionada (melhoria/funcionalidade nova)` | Não — entra em Foco |

### 4. Registrar pendências e Travas

**Na fila (A fazer hoje)**:
- Cada card com gate pendente ganha um item com `⏳` no início
- Formato: `⏳ SGV-XXXX — gate de doc pendente × <Módulo ou "módulo não identificado">`
- Se já existir pendência idêntica de execução anterior → não duplicar

**Nas Travas do Status — reunião**:
- Cards com módulo identificado (explícito ou inferido) **sem** gate → `⚠️ SGV-XXXX sem gate de doc ([[<Módulo>]])`
- Cards sem módulo identificado → `⚠️ SGV-XXXX sem gate de doc (módulo pendente)`
- O [[AGENTE_STATUS_REUNIAO]] detecta essas pendências com `⚠️ gate de doc` e as inclui em Travas

**No bloco de Auto-organização**:
```markdown
> [!organizacao]- Auto-organização
> - 🔍 Gate de doc: <n> cards aprovados sem verificação — SGV-XXXX ([[<Módulo>]]), SGV-YYYY (módulo pendente)
> - 📚 Doc ausente: <n> módulos sem documentação — <MóduloA>, <MóduloB>
```

### 5. Fechamento do ciclo

Quando o gate é resolvido (a verificação foi feita e registrada):

- O [[AGENTE_ORGANIZADOR]] detecta a resolução ao encontrar o registro na daily (`🔎 SGV-XXXX - Verificado contra doc`) e fecha a pendência automaticamente
- Se a verificação resultou em divergência `⚠️`, a pendência não fecha — é substituída por `⏳ SGV-XXXX × doc <Módulo> — divergência em aberto (decisão de Produto)`
- Travas que eram de gate pendente são removidas na próxima regeneração do Status

### 6. Priorização

Quando há múltiplos cards com gate pendente:

| Prioridade | Critério |
|---|---|
| 🔴 Alta | Card **movido pra Concluídas** sem gate — aprovado e arquivado sem verificação |
| 🟡 Média | Card aprovado hoje em HML (ambiente mais próximo de produção) |
| 🟢 Baixa | Card aprovado hoje em DEV (ainda vai passar por HML, onde o gate será repetido) |

A prioridade é indicada na pendência com o emoji correspondente e influencia a ordem na fila (itens de alta sobem).

## O que NÃO faz

- **Não executa** a verificação — apenas sinaliza. Quem faz o cruzamento é o [[../Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]].
- **Não edita** a doc do módulo sob nenhuma circunstância.
- **Não bloqueia** movimentação de card — a pendência é informativa, o card segue seu ciclo.
- **Não decide** se a doc ou o bug estão certos — QA sinaliza, Produto decide.

## Relação com outros agentes

| Agente | Interação |
|---|---|
| **AGENTE_ORGANIZADOR** | Dispara este agente; recebe as pendências de gate e as fecha quando resolvidas |
| **AGENTE_STATUS_REUNIAO** | Lê as pendências `⚠️ gate de doc` e as inclui em Travas |
| **AGENTE_FILA** | Pendências de gate são agrupadas em 👁️ Acompanhamento com marcador `⏳` |

## Resultado

- Cards aprovados sem gate de doc: pendência `⏳` na fila + item em Travas no Status — reunião
- Módulos sem documentação: pendência `📚 Importar doc` na fila
- Relatório consolidado no bloco `[!organizacao]- Auto-organização` da daily
- Nenhum card aprovado some na Concluídas com gate de doc esquecido
