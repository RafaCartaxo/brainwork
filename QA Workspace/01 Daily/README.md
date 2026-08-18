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
Quando um bug for reaberto (voltou a falhar depois de já ter sido considerado resolvido/aprovado em algum ambiente), além de registrar em **Atividades** do dia, adicionar um item na fila (A fazer hoje) pra lembrar de revalidar mais tarde, com o SGV linkado pro card (ex.: `"[[card|SGV-9237]] - Revalidar (reaberta novamente em homologação)"`).

## Regra de conclusão de pendência
Toda vez que um item de **A fazer hoje** (retestar, revalidar, gravar evidência, etc.) for marcado como feito, o resultado entra automaticamente como uma linha em **Atividades** (no ambiente correspondente: DEV/HML/POCs) — não basta só marcar o checkbox. Isso fecha o ciclo com a Regra de reabertura acima: reabriu → vira pendência; pendência resolvida → vira atividade com o resultado.

**O checkbox marcado é gatilho de automação**: anote o resultado curto entre parênteses ao marcar — ex.: `- [x] SGV-9499 - Retestar (aprovada em homologação)`, `- [x] MEL-0001 - Cadastrar melhoria no Notion (SGV-10012)` — e o auto-organizador ([[../../Sistema/Skills/SKILL_INBOX|SKILL_INBOX]], seção "Continuação de pendências concluídas") completa o resto do processo definido: linha em Atividades com a frase padrão, card atualizado/movido/renomeado, Histórico. **Inclua o ambiente no parêntese** quando a ação envolve validação — sem ele o organizador precisa perguntar. Marcou sem anotar o resultado? No modo manual ele pergunta; no agendado ele sinaliza `⏳ aguardando resultado` e não mexe em nada. Colou material bruto no parêntese (passo a passo, contexto extenso)? O organizador extrai pro card e resume o checkbox pra forma curta padrão (regra "Anotação longa vira resumo" na SKILL_INBOX).

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

> [!important] Como saber se é `✅` ou `🔁`: **ler o Histórico do card**
> As duas frases descrevem "passou" — o que as separa é a **história**, não o resultado de hoje. A regra de decisão:
>
> 1. Abrir o card e olhar a lista `- Histórico:` em Informações adicionais.
> 2. Existe alguma entrada `🔴 Reaberta em <ambiente>` **antes** de hoje? → use **`🔁 Retestada e aprovada`**.
> 3. Não existe? É a primeira validação → use **`✅ Aprovada`**.
>
> Não dá pra decidir pela memória de quem escreve, nem pela pasta onde o card está: card em `HML/` pode nunca ter sido reaberto, e card reaberto volta pra `DEV/`. **A fonte é o Histórico.**
>
> Registrado em 30/07: uma sessão de IA simulada sem contexto acertou as duas copies mas **não tinha como saber qual usar** — a tabela descrevia os dois casos e não dizia como identificar em qual você está.
| Falhou / voltou a falhar | `🔴 SGV-XXXX - Reaberta em <ambiente>` (usar "reaberta novamente" só da 2ª reabertura em diante) |
| Não foi possível reproduzir | `⚪ SGV-XXXX - Retestado, não reproduzido` |
| Não reproduzido, **com desdobramento pendente** de dev/produto | `⚪ SGV-XXXX - Retestado, não reproduzido (aguardando decisão do dev: <o que se espera>)` |
| Sem mudança desde o último dia | `⏳ SGV-XXXX - Sem novidades, aguardando retorno de dev` |
| Investiguei/analisei sem validar (não é aprovação nem reprovação) | `🔎 SGV-XXXX - Análise em <ambiente> (<resultado curto>)`; análise de código/causa raiz sem ambiente específico: `🔎 SGV-XXXX - Análise (<resultado curto>)` |

> [!warning] "Não reproduzido" não é descarte
> `⚪` é **resultado de teste**; `🗑️` é **decisão de encerramento**. Enquanto o desdobramento depende de alguém (dev vai ver se sobe o fix, produto vai decidir a regra), o item fica em limbo e **nada é arquivado**: card não vai pra `99 Arquivo/`, a numeração não é dada como resolvida, a entrada da Triagem fica **sem marcar**, e entra pendência de acompanhamento na fila (`⏳ aguardando dev`). Só quando a decisão chega é que se usa `🗑️` e a [[Sistema/Contexto/PADROES_QA.md#Descarte de bug/suspeita (99 Arquivo)\|regra de descarte]].
> Registrar também **por que** um ambiente não foi testado, quando for decisão: comportamento de instância específica não se reproduz em DEV, e sem essa nota alguém lê como cobertura faltando depois (precedente: SGV-6136, 28/07).

**Ciclo do bug** (espelho do ciclo da melhoria — trilha: `❓ → 🐛 → 📤/esteira` ou `❓ → 🗑️`):

| Situação | Copy |
|---|---|
| Identifiquei um possível bug (suspeita, a investigar) | `❓ Suspeita de bug registrada: <título curto>` — registrar também em **Bugs encontrados** como suspeita, e a pendência "Investigar suspeita: <título>" entra em **A fazer hoje** |
| Suspeita confirmada, card criado (sem SGV ainda) | `🐛 Bug confirmado (card criado): [[card]]` — card nasce pela [[Sistema/Skills/SKILL_BUGS\|SKILL_BUGS]]; pendência de cadastro no Notion entra na fila |
| Bug novo encontrado e cadastrado (já com SGV) | `🐛 SGV-XXXX - Bug cadastrado` (e linkar também em **Bugs encontrados**) |
| Suspeita investigada e descartada sem card | `🗑️ Suspeita descartada: <título> (não é bug: <motivo curto>)` |
| Bug/suspeita com card, investigada e descartada (não ocorre) | `🗑️ Bug/SGV XXXX - Descartado (não reproduz: <motivo curto>)` (ver [[Sistema/Contexto/PADROES_QA.md#Descarte de bug/suspeita (99 Arquivo)\|regra de descarte]]) |

**Ciclo do defeito** (problema que saiu da execução de um CT de uma task pai, em DEV — regra completa em [[Sistema/Contexto/PADROES_QA#Defeito × Bug\|PADROES_QA → Defeito × Bug]]):

| Situação | Copy |
|---|---|
| Defeito encontrado na execução de um CT | `🐛 SGV-XXXX - Defeito cadastrado (da [[card pai\|SGV-YYYY]])` — registrar também em **Bugs encontrados** |
| Defeito corrigido e o CT do pai passou no reteste | `✅ SGV-XXXX - Defeito corrigido e retestado em DEV` |
| Defeito reprovou no reteste | `🔴 SGV-XXXX - Defeito reaberto em DEV` |
| Defeito investigado e descartado (não procede) | `🗑️ SGV-XXXX - Defeito descartado (<motivo curto>)` |

> [!important] O defeito é sempre nomeado com a pai
> A frase de cadastro cita a task pai porque é ela que dá sentido ao defeito — sem isso, um `🐛 SGV-10831 - Defeito cadastrado` solto na daily não diz de que entrega ele saiu. O mesmo vale pro Histórico do card ([[Sistema/Contexto/PADROES_QA#Defeito × Bug\|PADROES_QA]]).
>
> Note que **não existe** copy de "Defeito aprovado em homologação": defeito não vai pra HML. Se você precisou dessa frase, ou não era defeito (era Bug), ou a esteira foi seguida errado.

**Tasks de API** (fluxo 3f — sem esteira DEV, validação direto em homologação; regras completas em [[Sistema/Contexto/PADROES_QA#Tasks de API (fluxo 3f)\|PADROES_QA]]):

| Situação | Copy |
|---|---|
| Revisão de cenários/contratos | `🔎 SGV-XXXX - Revisão de cenários (API) (<resultado>)` |
| Aprovada em homologação | `✅ SGV-XXXX - API aprovada em homologação` |
| Reprovada em homologação | `🔴 SGV-XXXX - API reaberta em homologação` |

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
| Batida de planejamento de sprint | `📋 Planejamento <sprint> - <n>/<total> cards batidos (<resultado curto>)` |
| Documentação importada/atualizada em 04 Conhecimento | `📚 <Doc> - Documentação importada/atualizada (<escopo curto do que entrou>)` |
| Trabalho no próprio vault/ferramenta (script, README, template, agente, skill) | `🔧 <alvo> - <o que mudou>` — ex.: `🔧 qa-atualiza.py - Radical 'analis' adicionado ao agrupamento 🔎` |

As linhas `🔎`/`📝`/`📤` moram **em Planejamento** (não em DEV — refinamento não é validação em ambiente). Nada muda nas frases em si — só o endereço.

`🔧` é reservado pra mudança no **próprio vault/processo** (script, doc, template, agente, skill) — nunca em cards do sistema testado, que usam `📚` (documentação de conhecimento) ou as copies de validação/refinamento acima. Decidido em 18/08, resolvendo uma das 5 propostas em aberto desde 31/07 — antes não havia copy oficial e o trabalho de ferramenta saía com emoji fora do catálogo (`🤖`).

**O parêntese é em linguagem simples**: descreve o que aconteceu e o que falta, pra qualquer pessoa entender sem conhecer o processo — nada de jargão do fluxo (destilado, mesa, rodada). Os termos técnicos vivem na mesa de refinamento e no callout de Detalhes, onde o contexto os explica.

## Grupos da fila ("A fazer hoje")

**Este é o vocabulário oficial** — o [[../../Sistema/Agentes/AGENTE_FILA|AGENTE_FILA]] executa o agrupamento, mas a lista de grupos mora aqui, junto do catálogo de copies. (Antes ela existia só no doc do agente, e a prática das dailies divergiu sem ninguém notar — foi o que deu errado em 28/07.)

| Grupo | Entra aqui |
|---|---|
| 🎯 **Validação** | "Validar", "Retestar", "Revalidar", "Testar", "Verificar se reproduz" |
| 🔎 **Refinamento** | "Refinar", "Revisar cenários", "Analisar", "Investigar" |
| 📤 **Cadastro** | "Cadastrar no Notion", "Atualizar no Notion", "Levar análise", "Criar card" |
| 👁️ **Acompanhamento** | "Acompanhar", "Confirmar critérios", e todo item sem verbo de ação claro |
| 📋 **Triagem** | "Triagem", "Bater os cards", "Reexportar" |
| 🚨 **Parado (7+ dias)** | Qualquer item que cruzou 7 dias de fila |
| ✅ **Concluídos hoje** | Itens já marcados `[x]` |

Duas regras que evitam item no grupo errado:

- **Classificar pelo verbo da ação**, não pela linha toda — o verbo é o texto antes do primeiro `(`, `—` ou `;`. Sem isso, "Triagem SP15 - Reexportar a view do **Notion**" cai em 📤 Cadastro pela palavra "Notion".
- **`🚨` e `✅` valem por estado** (idade / `[x]`) e **ganham** do agrupamento por verbo: item de validação parado há 8 dias vai pra 🚨, não pra 🎯.

Quem preenche o quê: **idade** (`🕐`/`⚠️`/`🚨`) e a **coleta dos `[x]`** em ✅ são do `qa-atualiza.py`; o agrupamento por natureza é do agente. Detalhe em [[../../Sistema/Agentes/AGENTE_FILA|AGENTE_FILA]] → "Fronteira com o script".

### Defeito não entra em grupo — entra embaixo da pai

Item de **defeito** ([[../../Sistema/Contexto/PADROES_QA#Defeito × Bug|PADROES_QA → Defeito × Bug]]) **não é classificado por verbo** e não ocupa linha de topo: ele aparece **aninhado sob a linha da task pai**, e é a pai que entra em 🎯 Validação.

```
> 🎯 **Validação**
> - [ ] [[card|SGV-3234]] - Validar em DEV a refatoração de etiquetas (28/29 CTs) 🕐 5d ⚠️
>     - [ ] ↳ [[card|SGV-10831]] - Defeito (aguardando fix)
>     - [ ] ↳ [[card|SGV-10842]] - Defeito (aguardando fix)
```

Motivo: os defeitos são **um trabalho só** com a entrega que os gerou. A 3234 sozinha ocupava **6 linhas** da fila (1 pai + 5 defeitos) para uma única validação — numa fila que passa de 100 itens, isso é ruído que esconde o resto.

O aninhamento é feito pelo **script** (`sincroniza_demandas_ativas`, lendo o campo `pai:` do frontmatter), não pelo agente — é decisão determinística, não julgamento. **Bug continua item independente**, no grupo do seu verbo.

## Pendência ↔ copy de Atividades

A fila fala em **verbo de ação** ("Validar em HML") e as Atividades falam em **resultado** ("Aprovada em homologação"). São vocabulários diferentes de propósito, e esta tabela liga os dois — é o que evita inventar frase ao fechar uma pendência, e é a mesma tabela que o `LEDGER` do `qa-atualiza.py` implementa.

| Pendência na fila | Resultado anotado | Copy que vai pra Atividades |
|---|---|---|
| `Validar em <ambiente>` | `(aprovada)` | `✅ SGV-XXXX - Aprovada em <ambiente>` |
| `Revalidar` / `Retestar` (já tinha reaberto) | `(aprovada)` | `🔁 SGV-XXXX - Retestada e aprovada em <ambiente>` |
| `Validar` / `Revalidar` | `(reprovada)` | `🔴 SGV-XXXX - Reaberta em <ambiente>` + pendência de revalidação |
| `Validar` / `Revalidar` | `(não reproduzido)` | `⚪ SGV-XXXX - Retestado, não reproduzido` |
| `Refinar` | `(card criado, critérios prontos)` | `📝 SGV-XXXX - <Tipo> refinado(a) (critérios de aceite prontos)` |
| `Atualizar no Notion` / `Levar análise` | `(feito)` | `📤 SGV-XXXX - <Tipo> atualizado(a) no Notion (...)` |
| `Cadastrar melhoria MEL-NNNN no Notion` | `(SGV-XXXX)` | `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)` |
| `Cadastrar bug no Notion` | `(SGV-XXXX)` | `🐛 SGV-XXXX - Bug cadastrado` |
| `Criar card` (bug confirmado sem SGV) | — | `🐛 Bug confirmado (card criado): [[card]]` |
| `Corrigir defeito` / `Retestar CT-NNN` | `(corrigido)` | `✅ SGV-XXXX - Defeito corrigido e retestado em DEV` |
| `Corrigir defeito` / `Retestar CT-NNN` | `(reprovado)` | `🔴 SGV-XXXX - Defeito reaberto em DEV` |
| `Investigar suspeita: <título>` | `(descartada: <motivo>)` | `🗑️ Suspeita descartada: <título> (não é bug: <motivo>)` |
| `Revisar cenários` | `(<resultado>)` | `🔎 SGV-XXXX - Análise (...)` ou `🔎 ... Revisão de cenários (API) (...)` |
| `Triagem` / `Bater os cards` | `(<resultado curto>)` | `📋 Planejamento <sprint> - <n>/<total> cards batidos (...)` |

Tipo na frase segue a regra transversal: bug não leva prefixo, os outros tipos sim (`Melhoria aprovada`, `Funcionalidade aprovada`, `Defeito corrigido`) — exceto refinamento (`📝`), que é sempre tipado.

## Status — reunião (primeira seção da daily)

Lista do que foi feito no dia, no topo da daily, pra rastreabilidade — não um roteiro de fala pra reunião (Rafael já sabe o que falar). Três blocos fixos: **Fiz** · **Foco de hoje** · **Travas**.

- **Lista rastreável, sem limite de itens**: cada bloco (**Fiz**/**Foco de hoje**/**Travas**) é uma lista — um item por linha, em linguagem simples, sem cortar pra caber num tamanho fixo. Detalhe mais extenso mora em Atividades/fila, nunca aqui.
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
- **A frase é a fonte da verdade**: dá pra registrar qualquer estágio direto em Atividades, à mão, mesmo pulando os anteriores — o botão 🔄 Atualizar sincroniza os cards com o que a daily declara e infere as etapas puladas ([[../../Sistema/Skills/SKILL_INBOX|SKILL_INBOX]], "Reconciliação de Atividades").
- **Tipo na frase**: bug é o tipo padrão e não leva prefixo (`✅ SGV-XXXX - Aprovada em ...`); qualquer outro tipo leva o nome na frase (`✅ SGV-XXXX - Melhoria aprovada em ...`, `Funcionalidade aprovada`, `POC aprovada`, `Defeito corrigido e retestado em DEV`). Exceção: a frase de **refinamento** (`📝`) é sempre tipada, inclusive pra bug — "Refinada" sozinho não diz o quê.
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
2. **Refinada** — o card já nasce no refinamento, com [[../../Sistema/Templates/Demanda.md|Demanda.md]] em `02 Demandas/DEV/`, arquivo nomeado `MEL-NNNN - <título>` (sem SGV ainda: `task` vazio, `mel: "NNNN"` preenchido). É nele que moram regras de negócio, escopo e CTs. No checkbox da daily original: **transformar o `MEL-NNNN` em wikilink pro card** (Regra de links acima) e, se o refinamento mudar o escopo, atualizar também o texto — a Dashboard exibe essa linha, ela precisa dizer a coisa certa e dar acesso de um clique. O checkbox continua aberto.
3. **Cadastrada** — quando cadastrada na ferramenta externa (ganha SGV): preencher `task` e o Link no card, renomear o arquivo pra `<SGV> - <título>`, marcar o checkbox na daily original, e registrar em Atividades: `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)`.
4. **Descartada** — marcar o checkbox e registrar em Atividades: `🗑️ MEL-NNNN - Melhoria descartada (<motivo curto>)`. Se já existia card de refinamento, mover pra `99 Arquivo/`.
5. Depois de cadastrada, segue a esteira normal de demanda (DEV → HML → Concluída) com as frases padrão de melhoria.

Quando a melhoria passar por refinamento (discussão, priorização) e virar uma demanda **Melhoria** de verdade (usando [[../../Sistema/Templates/Demanda.md|Demanda.md]] — ver [[../../Sistema/Contexto/COMO_EU_TRABALHO.md#Tipos de Demandas|tipos de demanda]]) ou for descartada, marcar o checkbox como feito (`- [x]`) **na nota original do dia** — ela some da lista da Dashboard sozinha, sem precisar editar em outro lugar.

Não confundir com o backlog de ferramenta do vault (esse fica só no [[../00 Inbox/README|00 Inbox]]) — aqui é melhoria do produto/sistema sendo testado.
