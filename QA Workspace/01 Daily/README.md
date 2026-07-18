---
tags:
  - qa
  - diario
---
# 01 Daily

Registro diário de atividades de teste.

As notas ficam organizadas em subpastas por ano-mês (ex.: `2026-07/`), e o arquivo usa só dia-mês (ex.: `13-07.md`) — o ano já fica implícito pela pasta. Esse formato é numérico de propósito: este Obsidian não tem o locale em português carregado, então nomes de mês por extenso (`Julho`) não são gerados automaticamente pelo plugin — só em inglês (`July`). Usar `YYYY-MM`/`DD-MM` evita esse problema, ordena corretamente por data e deixa os nós mais curtos e legíveis no Graph View.

> [!tip] Dica
> Use `obsidian daily` para criar notas diárias e links para as demandas trabalhadas no dia.
> Ao virar o mês, o plugin Daily Notes já cria a subpasta do novo mês automaticamente (ex.: `2026-08/`).

## Regra de links
Nas seções **Atividades**, **Bugs encontrados**, **Melhorias propostas** e **Anotações**: se o SGV mencionado já tem um card em `02 Demandas/`, referencie como wikilink (ex.: `[[9971 - Bug Assinatura Servidor Não Aprovado|SGV-9971]]`), não como texto puro. Se não existe card pra aquele SGV, mantenha como texto puro (`SGV-9635`) — não force link pra algo que não existe.

O mesmo vale pra **melhorias (MEL)**: a partir do momento em que a melhoria tem card (etapa Refinada em diante), todo `MEL-NNNN` mencionado vira wikilink pro card (ex.: `[[MEL-0001 - Organizar Eventos Retificação Campos Repetidos|MEL-0001]]`) — inclusive no próprio checkbox de "Melhorias propostas", que nasce em texto puro (proposta ainda sem card) e ganha o link no refinamento. Melhoria descartada com card arquivado linka pro card em `99 Arquivo/`.

**Vale pra todo lugar onde a numeração aparece** — inclusive **Pendências de ontem**, **A fazer hoje** e **Pendente para amanhã**: se o card existe, a citação é link (da Dashboard, que renderiza a fila, vira acesso de um clique). Sem card, texto puro, como sempre. O botão 🔄 Atualizar linkifica sozinho as linhas de fila que estiverem em texto puro.

## Regra de reabertura
Quando um bug for reaberto (voltou a falhar depois de já ter sido considerado resolvido/aprovado em algum ambiente), além de registrar em **Atividades** do dia, adicionar um item na fila (A fazer hoje) pra lembrar de revalidar mais tarde, com o SGV linkado pro card (ex.: "[[card|SGV-9237]] - Revalidar (reaberta novamente em homologação)").

## Regra de conclusão de pendência
Toda vez que um item de **A fazer hoje** (retestar, revalidar, gravar evidência, etc.) for marcado como feito, o resultado entra automaticamente como uma linha em **Atividades** (no ambiente correspondente: DEV/HML/POCs) — não basta só marcar o checkbox. Isso fecha o ciclo com a Regra de reabertura acima: reabriu → vira pendência; pendência resolvida → vira atividade com o resultado.

**O checkbox marcado é gatilho de automação**: anote o resultado curto entre parênteses ao marcar — ex.: `- [x] SGV-9499 - Retestar (aprovada em homologação)`, `- [x] MEL-0001 - Cadastrar melhoria no Notion (SGV-10012)` — e o auto-organizador ([[../Sistema/Skills/SKILL_INBOX|SKILL_INBOX]], seção "Continuação de pendências concluídas") completa o resto do processo definido: linha em Atividades com a frase padrão, card atualizado/movido/renomeado, Histórico. **Inclua o ambiente no parêntese** quando a ação envolve validação — sem ele o organizador precisa perguntar. Marcou sem anotar o resultado? No modo manual ele pergunta; no agendado ele sinaliza `⏳ aguardando resultado` e não mexe em nada. Colou material bruto no parêntese (passo a passo, contexto extenso)? O organizador extrai pro card e resume o checkbox pra forma curta padrão (regra "Anotação longa vira resumo" na SKILL_INBOX).

## Regra de padronização de resultados em Atividades
Usar sempre a mesma frase pro mesmo tipo de resultado — não variar a redação dia a dia pra descrever a mesma coisa (ex.: "Validação concluída e aprovada" e "Bug cadastrado e aprovado" são a mesma situação de "Aprovada", só com palavras diferentes).

Toda linha começa com o **emoji de status** — numa lista de Atividades, a coluna de emojis vira leitura instantânea do dia (verde = passou, vermelho = voltou), sem precisar ler as frases. Este catálogo é a **copy oficial**: usando a frase exata da situação, qualquer pessoa (ou IA) sabe exatamente o que aconteceu e onde agir, sem interpretar.

**`<ambiente>`** assume: `DEV`, `homologação`, `hotfix` (ambiente de homologação com a versão de produção + a hotfix — ver [[Sistema/Contexto/PADROES_QA.md#Organização de Bugs\|PADROES_QA]]) ou `produção`.

**Validação de bug** (o card mora na pasta do ambiente em `02 Demandas/`):

| Situação | Copy |
|---|---|
| Comecei a testar/validar | `🚀 SGV-XXXX - Início de validação` |
| Passou no teste (1ª validação, sem reabertura anterior) | `✅ SGV-XXXX - Aprovada em <ambiente>` |
| Passou no reteste, depois de já ter sido reaberto antes | `🔁 SGV-XXXX - Retestada e aprovada em <ambiente>` |
| Falhou / voltou a falhar | `🔴 SGV-XXXX - Reaberta em <ambiente>` (usar "reaberta novamente" só da 2ª reabertura em diante) |
| Não foi possível reproduzir | `⚪ SGV-XXXX - Retestado, não reproduzido` |
| Sem mudança desde o último dia | `⏳ SGV-XXXX - Sem novidades, aguardando retorno de dev` |
| Investiguei/analisei sem validar (não é aprovação nem reprovação) | `🔎 SGV-XXXX - Análise em <ambiente> (<resultado curto>)`; análise de código/causa raiz sem ambiente específico: `🔎 SGV-XXXX - Análise (<resultado curto>)` |

**Ciclo do bug** (espelho do ciclo da melhoria — trilha: `❓ → 🐛 → 📤/esteira` ou `❓ → 🗑️`):

| Situação | Copy |
|---|---|
| Identifiquei um possível bug (suspeita, a investigar) | `❓ Suspeita de bug registrada: <título curto>` — registrar também em **Bugs encontrados** como suspeita, e a pendência "Investigar suspeita: <título>" entra em **A fazer hoje** |
| Suspeita confirmada, card criado (sem SGV ainda) | `🐛 Bug confirmado (card criado): [[card]]` — card nasce pela [[Sistema/Skills/SKILL_BUGS\|SKILL_BUGS]]; pendência de cadastro no Notion entra na fila |
| Bug novo encontrado e cadastrado (já com SGV) | `🐛 SGV-XXXX - Bug cadastrado` (e linkar também em **Bugs encontrados**) |
| Suspeita investigada e descartada sem card | `🗑️ Suspeita descartada: <título> (não é bug: <motivo curto>)` |
| Bug/suspeita com card, investigada e descartada (não ocorre) | `🗑️ Bug/SGV XXXX - Descartado (não reproduz: <motivo curto>)` (ver [[Sistema/Contexto/PADROES_QA.md#Descarte de bug/suspeita (99 Arquivo)\|regra de descarte]]) |

**Melhoria** (antes do cadastro é `MEL-NNNN`; depois, a frase leva a palavra "Melhoria" pra diferenciar da esteira de bug só lendo a daily):

| Situação | Copy |
|---|---|
| Ideia nasceu (checkbox criado em Melhorias propostas) | `💭 MEL-NNNN - Melhoria proposta` |
| Melhoria refinada (card criado, aguardando cadastro externo) | `📝 MEL-NNNN - Melhoria refinada (card criado)` |
| Demanda já cadastrada (Notion) refinada internamente | `📝 SGV-XXXX - <Tipo> refinado(a) (critérios de aceite prontos)` — ex.: `Bug refinado`, `Melhoria refinada`, `Funcionalidade refinada` |
| Análise/critérios levados pra task externa (Notion atualizado) | `📤 SGV-XXXX - <Tipo> atualizado(a) no Notion (análise/critérios registrados na task)` |
| Melhoria refinada e cadastrada (ganhou SGV) | `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)` |
| Melhoria descartada no refinamento | `🗑️ MEL-NNNN - Melhoria descartada (<motivo curto>)` |
| Melhoria passou na validação | `✅ SGV-XXXX - Melhoria aprovada em <ambiente>` |
| Melhoria passou no reteste após reabertura | `🔁 SGV-XXXX - Melhoria retestada e aprovada em <ambiente>` |
| Melhoria falhou na validação | `🔴 SGV-XXXX - Melhoria reaberta em <ambiente>` |

**Planejamento** (subseção própria em Atividades — triagem, refinamento, estudo/importação de documentação, definição de critérios; trabalho que prepara os testes, sem ser execução em ambiente):

| Situação | Copy |
|---|---|
| Rodada de análise numa mesa de refinamento | `🔎 SGV-XXXX - Análise (Nª — <status simples>)` — ex.: `(1ª — travada: aguardando decisão do responsável sobre a regra)`, `(1ª — problema entendido, rascunho do card pronto)` |
| Demanda refinada (card criado) | `📝 SGV-XXXX - <Tipo> refinado(a) (critérios de aceite prontos)` |
| Análise/critérios levados pro Notion | `📤 SGV-XXXX - <Tipo> atualizado(a) no Notion (análise/critérios registrados na task)` |
| Batida de triagem de sprint | `📋 Triagem <sprint> - <n>/<total> cards batidos (<resultado curto>)` |
| Documentação importada/atualizada em 04 Conhecimento | `📚 <Doc> - Documentação importada/atualizada (<escopo curto do que entrou>)` |

As linhas `🔎`/`📝`/`📤` moram **em Planejamento** (não em DEV — refinamento não é validação em ambiente). Nada muda nas frases em si — só o endereço.

**O parêntese é em linguagem simples**: descreve o que aconteceu e o que falta, pra qualquer pessoa entender sem conhecer o processo — nada de jargão do fluxo (destilado, mesa, rodada). Os termos técnicos vivem na mesa de refinamento e no callout de Detalhes, onde o contexto os explica.

## Status — reunião (primeira seção da daily)

Bloco de standup no topo, pra ler direto na reunião da daily. Três linhas fixas: **Fiz** · **Foco de hoje** · **Travas**.

- **Cabe numa fala de 30 segundos**: cada bloco (**Fiz**/**Foco de hoje**/**Travas**) é uma pequena lista — um item por linha, máximo 3 por bloco, em linguagem simples. Não é inventário — é o que o time precisa ouvir. Detalhe mora em Atividades/fila, nunca aqui.
- **Mesmo padrão das Atividades, agrupado**: emoji(s) de status + numeração na frente, depois a frase (`📝📤 SGV-XXXX - ...`). Se o mesmo item passou por vários estágios no dia, os emojis se **agrupam numa linha só** (📝📤 = refinado e levado pro Notion) em vez de virar linhas separadas. Em "Travas", `⏳` na frente. **Tudo linkado** (regra de links: card; sem card, a mesa de refinamento).
- **Regenerado, não acumulado**: o bloco é *derivado* do que já está registrado na daily (Atividades + fila + travas) — reescreve-se por inteiro a cada atualização, não recebe item em cima de item. Pedir numa sessão ("gera meu status da reunião") ou escrever à mão, desde que tudo que ele diga exista registrado embaixo.
- **Sempre visível**: o callout não é recolhível de propósito — é a primeira coisa da nota.
- Trava sem dono/ação não entra: "Travas" lista só o que de fato bloqueia algo teu, com quem/o que se espera.

**Regra do detalhe recolhível** (vale pra qualquer seção de Atividades): a linha da atividade fica **curta** — emoji + link + copy padrão + status curto entre parênteses. Detalhamento longo (contexto, achados, custo do trabalho) desce pra um callout **fechado** logo abaixo, indentado na própria linha:

```
- 🔎 SGV-XXXX - Análise (rodada 1 — bloqueada no responsável)
	> [!note]- Detalhes
	> Texto longo aqui, quantas linhas precisar.
```

Bater o olho na lista mostra só emoji+status; expandir mostra o resto. Parêntese longo demais é sinal de que o conteúdo pertence ao callout.

**Regras transversais**:
- **Cada estágio vivido no dia é uma atividade**: proposta, refinamento, atualização no Notion, cadastro, validação — cada etapa que acontecer hoje ganha a própria linha em Atividades no momento em que acontece (inclusive quando o trabalho é feito numa sessão com IA — ela registra a linha de cada estágio que executar). A daily mostra o caminho: `💭 → 📝 → 📤 → 💡 → 🚀/✅...`.
- **A fazer hoje é o ledger completo do dia**: todo estágio executado aparece nele também como item **marcado**, com o que foi feito entre parênteses (`- [x] SGV-XXXX - Refinar (card criado, critérios prontos)`) — mesmo que a tarefa nunca tenha sido enfileirada antes; registra-se já concluída, com a marca ` → registrado`. O botão 🔄 Atualizar faz esse backfill sozinho a partir das linhas de Atividades. No fim do dia, a fila mostra tudo: o que foi feito (marcado) e o que carrega pra amanhã (aberto).
- **A frase é a fonte da verdade**: dá pra registrar qualquer estágio direto em Atividades, à mão, mesmo pulando os anteriores — o botão 🔄 Atualizar sincroniza os cards com o que a daily declara e infere as etapas puladas ([[../Sistema/Skills/SKILL_INBOX|SKILL_INBOX]], "Reconciliação de Atividades").
- **Tipo na frase**: bug é o tipo padrão e não leva prefixo (`✅ SGV-XXXX - Aprovada em ...`); qualquer outro tipo leva o nome na frase (`✅ SGV-XXXX - Melhoria aprovada em ...`, `Funcionalidade aprovada`, `POC aprovada`). Exceção: a frase de **refinamento** (`📝`) é sempre tipada, inclusive pra bug — "Refinada" sozinho não diz o quê.
- Complemento entre parênteses com contexto curto é sempre opcional, em qualquer frase (ex.: `✅ SGV-6375 - Aprovada em homologação (data ausente no evento de despacho corrigida)`).
- **A daily é sempre "o que EU fiz hoje"** — a frase é sua mesmo quando o card foi cadastrado por outra pessoa, e cadastrar sem testar não gera frase de validação. Autoria mora no card: campo `cadastrado_por` no frontmatter (preencher só se tiver a informação; vazio se não) e o Histórico registra quem validou cada etapa quando se sabe.
- O item do **Histórico** do card usa a mesma frase, prefixada pela data: `- 2026-07-14 - 🔁 Retestada e aprovada em homologação`. Uma linguagem só, na daily e no card.

## Regra de Melhorias propostas
Qualquer QA pode registrar aqui uma ideia de melhoria de produto notada durante a validação (não é bug — o sistema funciona, mas dá pra funcionar melhor). Sempre como checkbox (`- [ ]`), não texto puro — diferente das Pendências, aqui **não se recopia** de um dia pro outro: a [[../Dashboard/Dashboard|Dashboard]] tem uma seção ("Melhorias propostas em aberto") que junta automaticamente todos os checkboxes não marcados de todas as dailies, então dá pra acompanhar sem duplicar nada manualmente.

**Formato do checkbox** — ID sequencial + título curto na frente, detalhe depois (a Dashboard lista essas linhas fora de contexto, então o começo da linha precisa se explicar sozinho):

```markdown
- [ ] **MEL-NNNN · <Título curto e acionável>** — <contexto em 1 frase>. (origem: [[card|SGV-XXXX]])
```

Ex.: `- [ ] **MEL-0001 · Padronizar descrição dos eventos de campos repetidos** — revisar outros pontos que vazam identificador técnico pra UI. (origem: [[...|SGV-8805]])`. A parte de origem é opcional quando a ideia não nasceu de um card.

**Numeração**: sequencial global (`MEL-0001`, `MEL-0002`, ...), nunca por dia e nunca reaproveitada — mesmo melhoria descartada mantém o número pra sempre. O próximo número livre aparece na [[../Dashboard/Dashboard|Dashboard]], na seção de melhorias. Enquanto não é cadastrada, o `MEL-NNNN` é a referência dela em qualquer lugar (daily, conversa, anotação).

**Ciclo de vida do MEL**:
1. **Proposta** — nasce como checkbox aberto com `MEL-NNNN`.
2. **Refinada** — o card já nasce no refinamento, com [[../Sistema/Templates/Demanda.md|Demanda.md]] em `02 Demandas/DEV/`, arquivo nomeado `MEL-NNNN - <título>` (sem SGV ainda: `task` vazio, `mel: "NNNN"` preenchido). É nele que moram regras de negócio, escopo e CTs. No checkbox da daily original: **transformar o `MEL-NNNN` em wikilink pro card** (Regra de links acima) e, se o refinamento mudar o escopo, atualizar também o texto — a Dashboard exibe essa linha, ela precisa dizer a coisa certa e dar acesso de um clique. O checkbox continua aberto.
3. **Cadastrada** — quando cadastrada na ferramenta externa (ganha SGV): preencher `task` e o Link no card, renomear o arquivo pra `<SGV> - <título>`, marcar o checkbox na daily original, e registrar em Atividades: `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)`.
4. **Descartada** — marcar o checkbox e registrar em Atividades: `🗑️ MEL-NNNN - Melhoria descartada (<motivo curto>)`. Se já existia card de refinamento, mover pra `99 Arquivo/`.
5. Depois de cadastrada, segue a esteira normal de demanda (DEV → HML → Concluída) com as frases padrão de melhoria.

Quando a melhoria passar por refinamento (discussão, priorização) e virar uma demanda **Melhoria** de verdade (usando [[../Sistema/Templates/Demanda.md|Demanda.md]] — ver [[../Sistema/Contexto/COMO_EU_TRABALHO.md#Tipos de Demandas|tipos de demanda]]) ou for descartada, marcar o checkbox como feito (`- [x]`) **na nota original do dia** — ela some da lista da Dashboard sozinha, sem precisar editar em outro lugar.

Não confundir com o backlog de ferramenta do vault (esse fica só no [[../00 Inbox/README|00 Inbox]]) — aqui é melhoria do produto/sistema sendo testado.
