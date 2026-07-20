---
tags:
  - qa
  - agente
---
# Agente: Auto-organização da Daily

Classificar e rotear os registros crus da daily (anotações e bugs ainda não estruturados) pras referências corretas do vault, nos dois modos possíveis: pedido manual numa sessão, ou tarefa agendada rodando sozinha. Design completo em [[../Specs/2026-07-14-inbox-auto-organizacao-design.md|Spec]].

## Princípio: um lugar de escrita, um lugar de leitura

Rafael **escreve tudo na daily do dia** — anotação crua em `## Anotações`, bug visto em `## Bugs encontrados`, ideia de melhoria em `## Melhorias propostas`, lembrete em `## Pendente para amanhã`. A **Dashboard é só leitura** (KPIs, pendências, melhorias em aberto). O `00 Inbox/` **não é lugar de escrita** — guarda apenas o backlog de melhorias do próprio vault/ferramenta.

## Gatilhos

Três gatilhos, mesma lógica — o que muda é quem executa e o que cobre:

| Gatilho | Executor | Cobre | Ambiguidade |
|---|---|---|---|
| **Botão 🔄 Atualizar** (Dashboard) | Script determinístico (`.obsidian/scripts/qa-atualiza.py`, sem IA, offline, instantâneo) | Só a parte **mecânica**: cria a daily de hoje, carry-over sem duplicar, continuação de pendências concluídas **com resultado anotado**, reconciliação de Atividades, fila viva (invariante), marca ` → `, bloco de registro | Não existe: o que não casa com os padrões vira `⏳ aguardando resultado` ou fica intocado |
| **Sessão interativa** (Rafael pede "organiza a daily") | IA | Tudo: parte mecânica **+ classificação de registros crus** (Anotações/Bugs encontrados) | Pergunta antes de decidir |
| **Agendado 7h** (tarefa cron, opcional) | IA | Tudo | Palpite mais provável com marca `(auto)`; na dúvida entre "registro do dia" e processável, deixa como está |

O botão é o gatilho principal do dia a dia e **não depende de IA nem de internet**.

## Fonte (o que é processado)

Na daily mais recente até hoje (na execução agendada das 7h, isso normalmente significa a daily de ontem; no modo manual, a de hoje):

- **`## Anotações`**: linhas cruas ainda sem a marca de organizado
- **`## Bugs encontrados`**: itens em texto puro que ainda não têm card (sem wikilink pra card em `02 Demandas/`)
- **Checkboxes concluídos sem continuação**: itens marcados `[x]` em "A fazer hoje"/"Pendente para amanhã" cujo desfecho ainda não foi aplicado no resto do vault

Itens **não marcados** de `## Melhorias propostas` e `## Pendente para amanhã` não são processados — já são o destino certo dessas coisas; a Dashboard agrega de lá.

## Continuação de pendências concluídas

Quando Rafael marca uma pendência como feita, ele anota o **resultado curto entre parênteses** no fim da linha — essa anotação é o insumo do organizador pra completar o processo definido, sem inventar nada.

| Pendência marcada `[x]` | O que o organizador completa |
|---|---|
| `Cadastrar melhoria MEL-NNNN no Notion (SGV-XXXX)` | Preenche `task` e Link no card, renomeia o arquivo pra `<SGV> - <título>`, marca o checkbox da proposta na daily original, linha `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)` em Atividades, item no Histórico do card |
| `Retestar/revalidar SGV-XXXX (aprovada)` | Linha `✅`/`🔁` com a frase padrão em Atividades do ambiente; card: `status`/`ambiente` atualizados, movido de pasta conforme a esteira (ex.: `HML/` → `Concluídas/`, com `data_fim`), item no Histórico |
| `Retestar/revalidar SGV-XXXX (reprovada)` | Linha `🔴` em Atividades, `status: aberto` no card, nova pendência de revalidação (regra de reabertura), item no Histórico |
| `Testar/validar SGV-XXXX (reprovada, bug SGV-YYYY aberto)` | Tudo da linha de reprovada acima **+** card novo pro bug em `02 Demandas/<ambiente testado>/` (via [[../Skills/SKILL_BUGS\|SKILL_BUGS]]), linha `🐛 SGV-YYYY - Bug cadastrado` em Atividades, entrada em **Bugs encontrados**, e **duas** pendências na fila: `SGV-YYYY - Acompanhar (<título>)` e `SGV-XXXX - Revalidar (reaberta em <ambiente>, aguardando correção do SGV-YYYY)`. Evidência compartilhada: ver [[../../QA Workspace/Evidências/README\|Evidências/README]] |
| `Retestar SGV-XXXX (não reproduzido)` | Linha `⚪` em Atividades, item no Histórico |
| `Cadastrar bug ... no Notion (SGV-XXXX)` | Preenche `task` no card (e renomeia se ainda estava sem número), linha `🐛 SGV-XXXX - Bug cadastrado` em Atividades |
| `Revisar cenários de teste do SGV-XXXX (<resultado>)` | Linha em Atividades com o resultado anotado, item no Histórico do card |
| `Atualizar/levar análise do SGV-XXXX pro Notion (feito)` | Linha `📤 SGV-XXXX - <Tipo> atualizado(a) no Notion (...)` em Atividades, item no Histórico do card |
| `Investigar suspeita: <título> (descartada: <motivo>)` | Linha `🗑️ Suspeita descartada: <título> (não é bug: <motivo>)` em Atividades |
| `Investigar suspeita: <título> (confirmada)` | **Botão**: cria pendência "Criar card do bug: <título> (via SKILL_BUGS)" na fila — o card em si exige IA/sessão, que o cria e registra |
| Marcada **sem anotação de resultado** | **Manual**: pergunta o desfecho antes de agir. **Agendado**: não inventa — lista como `⏳ aguardando resultado` e não altera nada |

A linha do checkbox processado ganha a mesma marca ` → <resultado>` de sempre — o organizador nunca reprocessa.

**Resultado múltiplo**: uma anotação pode carregar o desfecho de **mais de uma demanda**. O organizador processa **cada desfecho pela linha correspondente da tabela**, como se fossem checkboxes separados.

**Anotação longa vira resumo**: o parêntese do checkbox é pra resultado **curto**. Quando vier material bruto ali, o organizador extrai esse material pro destino certo (card) e **reescreve o checkbox na forma curta padrão**.

**SGV sem card e sem contexto**: quando a pendência cita uma demanda que não tem card no vault e não veio material pra criar um, a citação fica em texto puro (Regra de links) e a pendência de acompanhamento é criada normalmente — **não criar card sem material suficiente**.

## Roteamento de registros crus

| Tipo detectado | Destino | Marca no registro original |
|---|---|---|
| Bug (comportamento errado observado, reproduzível) | Card novo em `02 Demandas/<ambiente testado>/` (DEV quando o ambiente não é conhecido), template [[../Templates/Bug Report.md\|Bug Report.md]] | linha ganha ` → card criado: [[card]]` |
| Melhoria de produto (ideia sobre o sistema, não é erro) | Checkbox em `## Melhorias propostas` da mesma daily | linha ganha ` → movido pra Melhorias propostas` |
| Tarefa/lembrete pontual (não é bug nem melhoria) | Item em `## Pendente para amanhã` da mesma daily | linha ganha ` → movido pra Pendente para amanhã` |
| Ideia sobre o próprio vault/ferramenta | Item novo no checklist "Próximos passos" de `00 Inbox/README.md` | linha ganha ` → backlog do vault` |
| Anotação de contexto/registro do dia | Fica onde está | nenhuma |
| Sanidade / Conhecimento / não classificável | Fica onde está | ` → aguardando estrutura` |

## Marca de processado

Uma linha já processada carrega o sufixo ` → ...` (seta + resultado). O organizador nunca reprocessa linha que já tem essa marca.

## Reconciliação de Atividades (o fim implica os passos anteriores)

Rafael pode trabalhar direto pelas **Atividades**: escrever a frase padrão à mão sem passar por pendência nenhuma. O botão reconcilia os cards com o que a daily de hoje declara — pra cada linha `✅ 🔁 🔴 ⚪ 📤 🗑️` com SGV cujo card não reflete o estado, ele aplica a esteira completa.

**O fim implica os passos anteriores**: registrar direto o estágio final (card ainda em DEV, atividade diz "aprovada em homologação") não trava nada — o card avança até o estado declarado e o Histórico registra `(etapas anteriores concluídas implicitamente)`. Idempotente: estado já refletido não é reaplicado.

## Invariante da fila viva

**Todo card em aberto (`02 Demandas/` fora de `Concluídas/`) tem um item ativo em "A fazer hoje"** — em qualquer estágio: a refinar, refinada, cadastrada no Notion, em validação, reaberta, aguardando dev. Vale pra bug, melhoria, funcionalidade, POC — tudo.

Na prática:
- Pendência que nasce durante o dia entra em **A fazer hoje**
- O botão 🔄 Atualizar **garante o invariante sozinho**: varre os cards abertos e, pra cada um sem item ativo na fila, move a pendência correspondente do "Pendente para amanhã" pra cima — ou cria o próximo passo padrão
- A demanda só sai da fila quando o card sai da esteira (Concluídas ou 99 Arquivo)

## Invariante da Triagem confiável

**Toda entrada de uma Triagem de sprint (`05 Refinar/Triagem - <sprint>.md`) marcada "já refinado"/"critérios no card" **sem wikilink** pro card precisa ter a pendência de confirmação rastreada** — não necessariamente um card no vault. "Card" aqui pode ser a **task do Notion**, não o arquivo local — Rafael confirmou isso em 2026-07-20. Não presumir inconsistência automaticamente; presumir **pendência de confirmação**.

Gap encontrado em 2026-07-20: SGV-8977 e SGV-9036 estavam marcadas `✅ → já refinado, critérios no card` desde 17/07, sem wikilink. A SGV-8977 de fato não tinha card local (confirmado ao revisar o MR — [[../Skills/SKILL_REVISAO_ESCOPO_MR|SKILL_REVISAO_ESCOPO_MR]] — e resolvido criando o card). A SGV-9036 pode estar correta como está (critérios só no Notion) — **sem material/MR em mãos pra confirmar, não se cria card no escuro.**

Verificação (varredura de `05 Refinar/Triagem - *.md`):
- Linha com `✅` e "já refinado"/"critérios no card"/"card criado" **sem wikilink** → checar se existe card em `02 Demandas/` pelo SGV.
  - Existe → só faltava o link; adicionar.
  - Não existe **e** há material/MR disponível pra confirmar → seguir [[../Skills/SKILL_REVISAO_ESCOPO_MR|SKILL_REVISAO_ESCOPO_MR]] (card direto ou revisão).
  - Não existe **e não há** material/MR em mãos → **não inventar nem criar card sem conteúdo**. Garantir que existe pendência na fila (`SGV-XXXX - Confirmar critérios (Notion) e revisar MR quando disponível`) — é isso que fecha o invariante, não a criação forçada de um card.

Quando disparar: no botão 🔄 Atualizar (parte mecânica: só reporta a ausência de pendência, não decide o desfecho) e nas sessões interativas de revisão de MR ou de bater a Triagem — é o momento natural de já cruzar a informação.

## Pendência até o cadastro externo

Criar o card/checkbox no vault não fecha o ciclo — Bug e Melhoria ainda precisam ser registrados na ferramenta externa (Notion ou equivalente). Todo item roteado como Bug ou Melhoria também gera uma linha em **A fazer hoje** da daily do dia.

## Copy padronizada (obrigatória pro organizador)

Tudo que o organizador escreve segue a copy já padronizada do vault — nunca inventar redação própria. As frases oficiais estão no [[../../QA Workspace/01 Daily/README\|01 Daily/README]] (catálogo completo: bug, melhoria, planejamento).

## Registro na daily

Todo processamento (manual ou agendado) grava um bloco novo na daily processada:

```markdown
### Auto-organização
- <resumo do item> → <destino/resultado>
```

Itens resolvidos por palpite automático (modo agendado) levam a marca `(auto)` no fim da linha.
