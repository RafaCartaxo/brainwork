---
tags:
  - qa
  - skill
---
# Skill: Auto-organização da Daily

Classificar e rotear os registros crus da daily (anotações e bugs ainda não estruturados) pras referências corretas do vault, nos dois modos possíveis: pedido manual numa sessão, ou tarefa agendada rodando sozinha. Design completo em [[../Specs/2026-07-14-inbox-auto-organizacao-design.md|2026-07-14-inbox-auto-organizacao-design.md]].

## Princípio: um lugar de escrita, um lugar de leitura

Rafael **escreve tudo na daily do dia** — anotação crua em `## Anotações`, bug visto em `## Bugs encontrados`, ideia de melhoria em `## Melhorias propostas`, lembrete em `## Pendente para amanhã`. A **Dashboard é só leitura** (KPIs, pendências, melhorias em aberto). O `00 Inbox/` **não é lugar de escrita** — guarda apenas o backlog de melhorias do próprio vault/ferramenta. O fluxograma didático desse fluxo fica na [[../../Dashboard/Dashboard|Dashboard]].

## Objetivos

- Deixar Rafael escrever tudo num lugar só (a daily), sem decidir na hora o destino de cada coisa
- Rotear cada registro cru pro lugar certo do vault, no formato certo
- Nunca inventar destino pra tipo sem estrutura própria ainda (Sanidade, Conhecimento)
- Manter rastreável o que ainda falta cadastrar externamente (Notion ou equivalente)

## Fonte (o que é processado)

Na daily mais recente até hoje (na execução agendada das 7h, isso normalmente significa a daily de ontem; no modo manual, a de hoje):

- **`## Anotações`**: linhas cruas ainda sem a marca de organizado (ver "Marca de processado" abaixo)
- **`## Bugs encontrados`**: itens em texto puro que ainda não têm card (sem wikilink pra card em `02 Demandas/`)
- **Checkboxes concluídos sem continuação**: itens marcados `[x]` em "A fazer hoje"/"Pendente para amanhã" cujo desfecho ainda não foi aplicado no resto do vault (sem linha correspondente em Atividades, card não atualizado/movido) — ver "Continuação de pendências concluídas" abaixo

Itens **não marcados** de `## Melhorias propostas` e `## Pendente para amanhã` não são processados — já são o destino certo dessas coisas; a Dashboard agrega de lá.

## Continuação de pendências concluídas

Quando Rafael marca uma pendência como feita, ele anota o **resultado curto entre parênteses** no fim da linha — essa anotação é o insumo do organizador pra completar o processo definido, sem inventar nada. (A coluna da esquerda mostra **ação + anotação**; na fila real o formato é número primeiro — `SGV-XXXX - <ação> (<resultado>)` — e o organizador reconhece a ação em qualquer posição da linha.)

| Pendência marcada `[x]` | O que o organizador completa |
|---|---|
| `Cadastrar melhoria MEL-NNNN no Notion (SGV-XXXX)` | Preenche `task` e Link no card, renomeia o arquivo pra `<SGV> - <título>`, marca o checkbox da proposta na daily original, linha `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)` em Atividades, item no Histórico do card |
| `Retestar/revalidar SGV-XXXX (aprovada)` | Linha `✅`/`🔁` com a frase padrão em Atividades do ambiente; card: `status`/`ambiente` atualizados, movido de pasta conforme a esteira (ex.: `HML/` → `Concluídas/`, com `data_fim`), item no Histórico |
| `Retestar/revalidar SGV-XXXX (reprovada)` | Linha `🔴` em Atividades, `status: aberto` no card, nova pendência de revalidação (regra de reabertura), item no Histórico |
| `Testar/validar SGV-XXXX (reprovada, bug SGV-YYYY aberto)` | Tudo da linha de reprovada acima **+** card novo pro bug em `02 Demandas/<ambiente testado>/` (passos extraídos da anotação, via [[SKILL_BUGS.md\|SKILL_BUGS]]), linha `🐛 SGV-YYYY - Bug cadastrado` em Atividades, entrada em **Bugs encontrados**, e **duas** pendências na fila: `SGV-YYYY - Acompanhar (<título>)` e `SGV-XXXX - Revalidar (reaberta em <ambiente>, aguardando correção do SGV-YYYY)`. Evidência compartilhada entre os dois casos: ver [[SKILL_BUGS.md#Evidências\|SKILL_BUGS]] |
| `Retestar SGV-XXXX (não reproduzido)` | Linha `⚪` em Atividades, item no Histórico |
| `Cadastrar bug ... no Notion (SGV-XXXX)` | Preenche `task` no card (e renomeia se ainda estava sem número), linha `🐛 SGV-XXXX - Bug cadastrado` em Atividades |
| `Revisar cenários de teste do SGV-XXXX (<resultado>)` | Linha em Atividades com o resultado anotado (ex.: cenários ok / faltou cenário X, devolvido pro dev), item no Histórico do card |
| `Atualizar/levar análise do SGV-XXXX pro Notion (feito)` | Linha `📤 SGV-XXXX - <Tipo> atualizado(a) no Notion (...)` em Atividades, item no Histórico do card |
| `Investigar suspeita: <título> (descartada: <motivo>)` | Linha `🗑️ Suspeita descartada: <título> (não é bug: <motivo>)` em Atividades — sem card, nada mais a fazer |
| `Investigar suspeita: <título> (confirmada)` | **Botão**: cria pendência "Criar card do bug: <título> (via SKILL_BUGS)" na fila — o card em si exige IA/sessão, que o cria e registra `🐛 Bug confirmado (card criado)` |
| Marcada **sem anotação de resultado** | **Manual**: pergunta o desfecho antes de agir. **Agendado**: não inventa — lista no bloco `### Auto-organização` como `⏳ aguardando resultado` e não altera nada |

A linha do checkbox processado ganha a mesma marca ` → <resultado>` de sempre — o organizador nunca reprocessa.

**Resultado múltiplo**: uma anotação pode carregar o desfecho de **mais de uma demanda** (ex.: `Revalidar SGV-XXXX (aprovada; bug SGV-YYYY também aprovado)` — testei as duas na mesma sessão). O organizador processa **cada desfecho pela linha correspondente da tabela**, como se fossem checkboxes separados: cada demanda ganha a própria linha em Atividades, o próprio item de Histórico e a própria movimentação de card.

**Anotação longa vira resumo**: o parêntese do checkbox é pra resultado **curto** (com o ambiente, quando a ação envolve validação — evita o organizador ter que perguntar). Quando vier material bruto ali (passo a passo, contexto extenso), o organizador extrai esse material pro destino certo (card) e **reescreve o checkbox na forma curta padrão** — ex.: `- [x] Testar melhoria SGV-XXXX (reprovada em homologação, bug SGV-YYYY aberto — passos no card)` — mantendo a marca ` → ...` com o link do card. É a única exceção à regra de "a linha original fica": a fidelidade do texto bruto fica preservada no card; a fila é ledger, não repositório de detalhe.

**SGV sem card e sem contexto**: quando a pendência cita uma demanda que não tem card no vault e não veio material pra criar um, a citação fica em texto puro (Regra de links) e a pendência de acompanhamento/revalidação é criada normalmente — **não criar card sem material suficiente pra preencher sem inventar**; o card nasce quando houver contexto.

**Legado**: arquivos de captura antigos em `00 Inbox/*.md` com `status: pendente` continuam sendo processados pela mesma tabela abaixo, até zerarem. O fluxo novo não cria mais capturas soltas.

## Roteamento

| Tipo detectado | Destino | Marca no registro original |
|---|---|---|
| Bug (comportamento errado observado, reproduzível) | Card novo em `02 Demandas/<ambiente testado>/` (DEV quando o ambiente não é conhecido — regra do PADROES_QA: a pasta segue o último ambiente testado), no template [[../Templates/Bug Report.md\|Bug Report.md]] | linha ganha ` → card criado: [[card]]` |
| Melhoria de produto (ideia sobre o sistema Sogov, não é erro) | Checkbox em `## Melhorias propostas` da mesma daily | linha ganha ` → movido pra Melhorias propostas` |
| Tarefa/lembrete pontual (não é bug nem melhoria) | Item em `## Pendente para amanhã` da mesma daily | linha ganha ` → movido pra Pendente para amanhã` |
| Ideia sobre o próprio vault/ferramenta (não é sobre o Sogov) | Item novo no checklist "Próximos passos" de `00 Inbox/README.md` | linha ganha ` → backlog do vault` |
| Anotação de contexto/registro do dia (não precisa de ação) | Fica onde está | nenhuma (não é processável, é diário mesmo) |
| Sanidade / Conhecimento / não classificável | Fica onde está | ` → aguardando estrutura` |

Nas capturas legadas do Inbox, "marca no registro" vale pro frontmatter (`status`) e o arquivo é apagado depois de roteado com sucesso, como no design original.

Bug e Melhoria são a mesma coisa por baixo — um card numerado em `02 Demandas/`, só muda o `tipo` — a diferença é de **momento**: bug já nasce card porque a estrutura de reprodução já é objetiva; melhoria fica no checkbox até Rafael refinar (regras de negócio, escopo) e formalizar com [[../Templates/Demanda.md|Demanda.md]].

`03 Sanidades/` e `04 Conhecimento/` estão vazias, sem template — não rotear com confiança pra lá até essas pastas ganharem estrutura própria.

## Marca de processado

Uma linha já processada carrega o sufixo ` → ...` (seta + resultado). O organizador nunca reprocessa linha que já tem essa marca. Isso mantém a daily legível como diário (a linha original fica, com o desfecho ao lado) sem precisar de frontmatter por item — com uma única exceção: anotação longa é resumida pra forma curta padrão depois de extraída pro card (ver "Anotação longa vira resumo" acima).

## Gatilhos e ambiguidade

Três gatilhos, mesma lógica — o que muda é quem executa e o que cobre:

| Gatilho | Executor | Cobre | Ambiguidade |
|---|---|---|---|
| **Botão 🔄 Atualizar** (Dashboard) | Script determinístico (`.obsidian/scripts/qa-atualiza.py`, sem IA, offline, instantâneo) | Só a parte **mecânica**: cria a daily de hoje, carry-over sem duplicar, continuação de pendências concluídas **com resultado anotado**, **reconciliação de Atividades** (abaixo), **fila viva** (invariante abaixo), marca ` → `, bloco de registro | Não existe: o que não casa com os padrões vira `⏳ aguardando resultado` ou fica intocado |
| **Sessão interativa** (Rafael pede "organiza a daily") | IA | Tudo: parte mecânica **+ classificação de registros crus** (Anotações/Bugs encontrados) | Pergunta antes de decidir |
| **Agendado 7h** (tarefa cron, opcional/complementar) | IA | Tudo | Palpite mais provável com marca `(auto)`; na dúvida entre "registro do dia" e processável, deixa como está |

O botão é o gatilho principal do dia a dia e **não depende de IA nem de internet**. Classificar anotação crua (decidir se é bug/melhoria/lembrete e escrever o card) é o único trabalho que exige IA.

## Copy padronizada (obrigatória pro organizador)

Tudo que o organizador escreve segue a copy já padronizada do vault — nunca inventar redação própria:

- Linha em `## Atividades`: frase padrão **com emoji de status na frente** (tabela em [[../../01 Daily/README|01 Daily/README]]), ex.: `🐛 SGV-XXXX - Bug cadastrado`.
- Checkbox em `## Melhorias propostas`: formato `- [ ] **MEL-NNNN · <Título curto e acionável>** — <contexto em 1 frase>. (origem: [[card|SGV-XXXX]])`. O número é o próximo MEL livre do vault (maior `MEL-\d{4}` existente em qualquer daily ou campo `mel` de card Demanda, + 1) — a Dashboard exibe esse próximo número. Nunca reaproveitar número (regra completa no mesmo README).
- Item de Histórico em card: `- YYYY-MM-DD - <frase padrão com emoji>`.
- **Estágio executado = linha registrada na hora**: quando o trabalho acontece numa sessão (proposta, refinamento, atualização no Notion, cadastro), cada estágio concluído gera imediatamente a própria linha em Atividades **e** o item marcado correspondente em **A fazer hoje** (`- [x] <ação> (<o que foi feito>) → registrado`) — a fila é o ledger completo do dia, e a daily mostra o caminho (`💭 → 📝 → 📤 → 💡`), não só o estado final. O botão 🔄 Atualizar faz o backfill do ledger sozinho a partir das Atividades.
- Pendência: **número/card primeiro, ação depois** — `- [ ] [[card|SGV-XXXX]] - Cadastrar no Notion` — espelhando as listas de Atividades e de bugs: a coluna de numerações vira leitura instantânea da fila. Numeração **linkada pro card quando ele existe**; item **sem número** (suspeita, captura) fica com a ação na frente, como sempre. Autocontida em qualquer caso. O botão linkifica sozinho o que estiver em texto puro. **Card mudou depois?** Quando o conteúdo de um card é revisado (critérios, escopo), conferir e atualizar as pendências abertas que o citam — detalhe defasado na fila induz erro na hora de executar.

## Registro na daily

Todo processamento (manual ou agendado) grava um bloco novo na daily processada:

```markdown
### Auto-organização
- <resumo do item> → <destino/resultado>
```

Itens resolvidos por palpite automático (modo agendado) levam a marca `(auto)` no fim da linha, sinalizando que merecem uma segunda olhada.

## Reconciliação de Atividades (o fim implica os passos anteriores)

Rafael pode trabalhar direto pelas **Atividades**: escrever a frase padrão à mão (`✅ SGV-XXXX - Aprovada em homologação`) sem passar por pendência nenhuma. O botão reconcilia os cards com o que a daily de hoje declara — pra cada linha `✅ 🔁 🔴 ⚪ 📤 🗑️` com SGV cujo card não reflete o estado, ele aplica: aprovação em homologação/hotfix conclui o card (status, `data_fim`, move pra `Concluídas/`), aprovação em DEV move pra `HML/`, `🔴` reabre, `🗑️` descarta pro `99 Arquivo/`, `⚪`/`📤` registram no Histórico.

**O fim implica os passos anteriores**: registrar direto o estágio final (card ainda em DEV, atividade diz "aprovada em homologação") não trava nada — o card avança até o estado declarado e o Histórico registra `(etapas anteriores concluídas implicitamente)`. O mesmo vale na anotação de pendência: `(aprovada em homologação)` com card em DEV fast-forwarda a esteira. Idempotente: estado já refletido não é reaplicado (dedupe por data no Histórico).

## Pendência do próximo passo (demanda refinada)

**Invariante da fila viva**: *todo card em aberto (`02 Demandas/` fora de `Concluídas/`) tem um item ativo em "A fazer hoje"* — em qualquer estágio: a refinar, refinada, cadastrada no Notion, em validação, reaberta, aguardando dev. Vale pra bug, melhoria, funcionalidade, POC — tudo.

Na prática:
- Pendência que nasce durante o dia (refinamento, próximo passo, cadastro) entra em **A fazer hoje**. "Pendente para amanhã" é só o estacionamento do fim do dia; o carry-over leva adiante o que não foi concluído.
- O botão 🔄 Atualizar **garante o invariante sozinho**: varre os cards abertos e, pra cada um sem item ativo na fila, move a pendência correspondente do "Pendente para amanhã" pra cima — ou cria o próximo passo padrão (`MEL-NNNN - Cadastrar melhoria no Notion` pra card sem SGV; `SGV-XXXX - Acompanhar (<título>)` pros demais).
- A demanda só sai da fila quando o card sai da esteira (Concluídas ou 99 Arquivo). Quando isso acontece por outro caminho (ex.: aprovação registrada em outra pendência ou direto em Atividades), a pendência de acompanhamento é dada como **concluída pelo organizador**, com a marca do desfecho (ex.: `→ aprovada em homologação (card concluído)`) — não fica órfã aberta.

## Pendência até o cadastro externo

Criar o card/checkbox no vault não fecha o ciclo — Bug e Melhoria ainda precisam ser registrados na ferramenta externa (Notion ou equivalente, resultado esperado já documentado em [[SKILL_BUGS.md|SKILL_BUGS.md]]). Por isso, todo item roteado como Bug ou Melhoria também gera uma linha em **A fazer hoje** da daily do dia (ou de "Pendente para amanhã" da daily processada, quando a rodada é das 7h sobre a daily de ontem — o carry-over traz pra hoje), ex.:

```markdown
- [ ] Cadastrar bug "Trava ao anexar PDF grande" no Notion
- [ ] Refinar e cadastrar melhoria "Padronizar nome do anexo"
```

Essa linha usa o mecanismo já documentado em [[../../01 Daily/README|01 Daily/README]] ("Regra de conclusão de pendência"): carrega de um dia pro outro até Rafael marcar como feita, e aí vira uma linha em Atividades com o resultado, usando a frase padrão já definida (ex.: `SGV-XXXX - Bug cadastrado`).

## Resultado Esperado

Daily organizada (todo registro cru classificado ou marcado com seu desfecho), cards criados pros bugs estruturáveis, backlog do vault alimentado, pendências de cadastro externo criadas, e o bloco `### Auto-organização` registrando o que aconteceu.
