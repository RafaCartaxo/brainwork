---
tags:
  - qa
  - casos-de-teste
---
# Casos de Teste — Fluxos do QA Workspace

- **Task:** Validar os fluxos do vault QA Workspace (sistema de trabalho do QA, não o produto Sogov)
- **Projeto:** QA Workspace (Obsidian)
- **Branch:** n/a (vault sem git)
- **Data de criação:** 2026-07-14
- **Referência:** [[Sistema/Contexto/FLUXOS|FLUXOS]] (passo a passo), [[QA Workspace/01 Daily/README|01 Daily/README]] (frases padrão e MEL), [[Sistema/Skills/SKILL_INBOX|SKILL_INBOX]] (auto-organizador)

| Fluxo | CTs |
|---|---|
| 1. Começar o dia (Dashboard) | CT-001 a CT-006 |
| 2. Registrar na daily | CT-007 a CT-008 |
| 3. Esteira do bug | CT-009 a CT-013 |
| 4. Melhoria (MEL) | CT-014 a CT-018 |
| 5. Evidência | CT-019 a CT-020 |
| 6. Auto-organizador (IA) | CT-021 a CT-027 |
| 7. Fechar o dia | CT-028 |
| 8. Botão 🔄 Atualizar + fila viva | CT-029 a CT-037 |
| 9. Refinar demanda já cadastrada | CT-038 |
| 10. Ciclo por estágios + reconciliação | CT-039 a CT-041 |

---

**Fluxo 1 — Começar o dia (Dashboard)**

## CT-001 Abrir o vault abre a Dashboard automaticamente em modo leitura

Dado que o Obsidian está fechado

Quando o usuário abre o vault BrainWork

Então a Dashboard ("Central de Operações QA") é exibida automaticamente como nota ativa
E a nota está em modo leitura (sem cursor de edição; ícone de modo no canto mostra leitura)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-002 Voltar pra Dashboard de qualquer nota com Ctrl+H

Dado que o usuário está com qualquer outra nota aberta (ex.: uma daily)

Quando pressiona `Ctrl+H`

Então a Dashboard é aberta como nota ativa, sem precisar navegar pelo explorador de arquivos

Execução Passou?

- [x] <span style="color:#2ecc71">Sim</span> ✅ 2026-07-14
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-003 Botão da daily de hoje abre a nota do dia

Dado que a daily de hoje já existe em `01 Daily/`

Quando o usuário clica no botão "✏️ Escrever na daily de hoje" na seção **Hoje** da Dashboard

Então a daily do dia atual é aberta

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-004 Aviso quando a daily de hoje ainda não existe

Dado que a daily de hoje ainda não foi criada

Quando o usuário abre a Dashboard

Então a seção **Hoje** exibe o aviso de que a daily não existe, com a instrução de criação (`Ctrl+P` → "Open today's daily note")
E nenhuma nota nova é criada só por abrir a Dashboard

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-005 KPIs contam bugs por status, incluindo descartados

Dado que existem cards de bug com status aberto, em validação, resolvido e descartado

Quando o usuário abre a Dashboard

Então a faixa de KPIs exibe um card por status (abertos, em validação, resolvidos, descartados, total) com as contagens batendo com os cards reais em `02 Demandas/` e `99 Arquivo/`
E nenhuma daily ou nota que não seja bug entra na contagem

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-006 KPI zerado aparece esmaecido

Dado que um dos status não tem nenhum bug (contagem 0)

Quando o usuário olha a faixa de KPIs

Então o card zerado aparece com opacidade reduzida em relação aos cards com valor

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 2 — Registrar na daily**

## CT-007 Pendências abertas da daily mais recente aparecem na Dashboard

Dado que a daily mais recente tem itens não marcados em "A fazer hoje" ou "Pendente para amanhã"

Quando o usuário abre a Dashboard

Então a seção **Pendências em aberto** lista esses itens, indicando de qual daily vieram, com a data no formato dd/MM/yyyy

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-008 Daily de data futura não é tratada como diário mais recente

Dado que existe uma daily criada com data de amanhã (pré-criada)

Quando o usuário abre a Dashboard hoje

Então a seção "Diário mais recente" mostra a daily de hoje (ou a última até hoje), nunca a de amanhã

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 3 — Esteira do bug**

## CT-009 Aprovação em DEV move o card pra HML sem perder dados

Dado que um card de bug em `02 Demandas/DEV/` foi aprovado na validação de DEV

Quando o usuário move o arquivo pra `02 Demandas/HML/`, atualiza o campo ambiente pra HML e adiciona o item no Histórico

Então o card passa a aparecer no grupo HML da tabela "Bugs por Ambiente" da Dashboard
E todos os links pro card (daily, outros cards) continuam funcionando após a movimentação

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-010 Aprovação em HML conclui o card e atualiza os KPIs

Dado que um card de bug em `02 Demandas/HML/` foi aprovado em homologação

Quando o usuário muda o status pra resolvido, preenche a data de fim, move pra `02 Demandas/Concluídas/` e registra `✅/🔁 SGV-XXXX - ... aprovada em homologação` na daily

Então o KPI "resolvidos" da Dashboard aumenta em 1 e o "em validação"/"abertos" diminui de acordo
E o card aparece no grupo de resolvidos da tabela de bugs

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-011 Reabertura gera pendência de revalidação

Dado que um bug considerado resolvido voltou a falhar

Quando o usuário marca a pendência de reteste com `(reprovada)` e clica em 🔄 Atualizar — ou registra manualmente `🔴 SGV-XXXX - Reaberta em <ambiente>` em Atividades

Então uma pendência de revalidação ("Revalidar SGV-XXXX...") entra na fila (A fazer hoje / carry-over)
E ela aparece na Dashboard (Pendências em aberto) até ser concluída, quando vira linha de resultado em Atividades

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-012 Descarte de suspeita vai pro 99 Arquivo e conta no KPI

Dado que uma suspeita de bug foi investigada e confirmada como não ocorrendo

Quando o usuário aplica a regra de descarte (status descartado, CTs marcados como Sim, motivo em Observações, arquivo movido pra `99 Arquivo/`, frase `🗑️ ... Descartado (não reproduz: ...)` na daily)

Então o KPI "descartados" da Dashboard aumenta em 1
E o card não aparece mais entre os bugs ativos de `02 Demandas/`

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-013 Coluna de emojis das Atividades conta a história do dia

Dado que a daily tem várias linhas de Atividades registradas com as frases padrão

Quando o usuário olha a seção Atividades em modo leitura

Então toda linha começa com o emoji de status correspondente à situação (✅ 🔁 🔴 🐛 🚀 ⏳ ⚪ 🗑️ 💡)
E dá pra entender o desfecho de cada item só pela coluna de emojis, sem ler as frases

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 4 — Melhoria (MEL)**

## CT-014 Dashboard exibe o próximo número MEL livre

Dado que a maior numeração existente no vault é MEL-0001 (em qualquer daily ou card Demanda)

Quando o usuário abre a seção "Melhorias propostas em aberto" da Dashboard

Então a linha "Próximo número livre" exibe MEL-0002

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-015 Melhoria proposta aparece na Dashboard com o título se explicando sozinho

Dado que uma melhoria foi registrada na daily no formato `- [ ] **MEL-NNNN · Título curto** — contexto. (origem: [[...|SGV-XXXX]])`

Quando o usuário abre a Dashboard

Então a melhoria aparece em "Melhorias propostas em aberto" com o MEL e o título legíveis no começo da linha

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-016 Marcar o checkbox na daily original remove a melhoria da Dashboard

Dado que uma melhoria listada na Dashboard foi cadastrada ou descartada

Quando o usuário marca o checkbox dela como feito na daily em que nasceu

Então ela some da seção "Melhorias propostas em aberto" da Dashboard sem nenhuma outra edição

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-017 Melhoria cadastrada vira card Demanda mantendo o rastro do MEL

Dado que uma melhoria MEL-NNNN foi refinada e cadastrada na ferramenta externa com número SGV

Quando o usuário cria o card com o template Demanda preenchendo o campo `mel` com o número, marca o checkbox original e registra `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)` em Atividades

Então o card aparece na seção Demandas da Dashboard
E o "Próximo número livre" da Dashboard não regride nem repete o número usado

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-018 Número de melhoria descartada nunca é reaproveitado

Dado que uma melhoria MEL-NNNN foi descartada no refinamento (checkbox marcado + `🗑️ MEL-NNNN - Melhoria descartada (...)` em Atividades)

Quando uma nova melhoria é proposta depois

Então ela recebe um número maior que o da descartada — o número da descartada permanece dela pra sempre

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 5 — Evidência**

## CT-019 Vídeo de evidência embedado toca dentro do card

Dado que um vídeo foi gravado, renomeado pro padrão `<SGV> - <descrição>.mp4` e movido pra subpasta do ambiente em `Evidências/`

Quando o usuário adiciona o embed `![[arquivo.mp4]]` na seção Evidências do card e abre o card em modo leitura

Então o player do vídeo aparece dentro da nota e reproduz ao clicar

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-020 Link 📁 do card abre a pasta do ambiente no gerenciador de arquivos

Dado que um card de bug tem o link 📁 no título da seção Evidências

Quando o usuário clica no 📁

Então o gerenciador de arquivos abre direto na pasta do ambiente correspondente (Desenvolvimento/Homologação/etc.)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 6 — Auto-organizador**

## CT-021 Bug estruturável em Anotações vira card completo com rastro

Dado que a daily tem uma linha crua em Anotações descrevendo um comportamento errado com passos claros

Quando o auto-organizador roda (manual ou agendado)

Então um card novo é criado em `02 Demandas/DEV/` no template de Bug Report com os dados da anotação
E a linha original ganha o sufixo ` → card criado: [[card]]`
E o bloco `### Auto-organização` da daily lista o item e o destino
E uma pendência de cadastro externo ("Cadastrar ... no Notion") entra na fila (A fazer hoje da daily do dia, ou Pendente para amanhã da daily processada na rodada das 7h — o carry-over traz)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-022 Item ambíguo no modo agendado recebe a marca (auto)

Dado que a daily tem uma anotação ambígua (não é claramente bug, melhoria ou lembrete)

Quando a execução agendada das 7h processa a daily (sem ninguém pra perguntar)

Então o item é roteado pro destino mais provável
E a linha correspondente no bloco `### Auto-organização` termina com `(auto)`

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-023 Modo manual pergunta antes de decidir item ambíguo

Dado que a daily tem uma anotação ambígua

Quando o usuário pede "organiza a daily" numa sessão interativa

Então o organizador pergunta o tipo/destino do item antes de mover qualquer coisa, em vez de decidir sozinho

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-024 Linha já processada não é reprocessada

Dado que uma linha de Anotações já tem a marca de processado (sufixo ` → ...`)

Quando o auto-organizador roda de novo (qualquer modo)

Então a linha é ignorada — nenhum card duplicado, nenhuma pendência repetida, nenhuma nova entrada no bloco de registro pra ela

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-025 Melhoria roteada pelo organizador recebe o próximo MEL e a copy padrão

Dado que a daily tem uma anotação crua que é claramente uma ideia de melhoria do produto

Quando o auto-organizador processa a daily

Então um checkbox novo entra em "Melhorias propostas" no formato `**MEL-NNNN · Título** — contexto. (origem: ...)`, usando o próximo número livre do vault
E a linha original ganha ` → movido pra Melhorias propostas`

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-026 Captura legada do Inbox é roteada e o arquivo some

Dado que existe um arquivo de captura antigo em `00 Inbox/` com status pendente

Quando o auto-organizador roda

Então o conteúdo é roteado pela tabela normal (card, melhoria, pendência ou backlog)
E o arquivo de captura é apagado após o roteio bem-sucedido
E capturas não classificáveis ficam no Inbox com status "aguardando-estrutura", sem serem apagadas

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-027 Execução sem nada cru não altera nenhum arquivo

Dado que a daily não tem linha crua sem marca e não há captura legada pendente

Quando a execução agendada das 7h roda

Então nenhum arquivo do vault é criado ou modificado (nem bloco de registro vazio é adicionado)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 7 — Fechar o dia**

## CT-028 Pendência concluída fecha o ciclo virando atividade

Dado que um item de "A fazer hoje" foi executado

Quando o usuário marca o checkbox como feito e registra a linha de resultado em Atividades com a frase padrão

Então a pendência some da Dashboard
E o resultado fica registrado em Atividades com o emoji de status correspondente
E o item não é recopiado pra daily seguinte

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 8 — Botão 🔄 Atualizar + fila viva (script determinístico, sem IA)**

## CT-029 Botão cria a daily de hoje com o carry-over pronto

Dado que a daily de hoje ainda não existe e a de ontem tem itens não finalizados

Quando o usuário clica em 🔄 Atualizar na Dashboard

Então a daily de hoje é criada com o template padrão
E os itens não finalizados de ontem aparecem em "Pendências de ontem" e "A fazer hoje"

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-030 Carry-over não duplica itens já presentes

Dado que a daily de hoje já contém um item que também está aberto na daily de ontem (mesmo texto ou mesmo SGV/MEL)

Quando o usuário clica em 🔄 Atualizar

Então o item não é carregado de novo — nenhuma duplicata aparece na fila

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-031 Conclusão com (aprovada) avança o card na esteira

Dado que uma pendência de reteste foi marcada `- [x] Retestar SGV-XXXX (aprovada)` e o card está em HML

Quando o usuário clica em 🔄 Atualizar

Então a linha `✅`/`🔁` com a frase padrão entra em Atividades (🔁 se o card já teve reabertura no Histórico)
E o card vai pra Concluídas com status resolvido e data de fim preenchida
E a linha da pendência ganha a marca " → "

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-032 Conclusão de cadastro de MEL transforma o card sem quebrar links

Dado que uma pendência foi marcada `- [x] Cadastrar melhoria MEL-NNNN no Notion (SGV-XXXX)`

Quando o usuário clica em 🔄 Atualizar

Então o card é renomeado pra `<SGV> - <título>` com `task` preenchida
E todos os wikilinks do vault pro card continuam funcionando (inclusive o checkbox da proposta, que é marcado)
E a linha `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)` entra em Atividades

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-033 Conclusão sem anotação de resultado não inventa nada

Dado que uma pendência de continuação foi marcada `[x]` sem resultado entre parênteses

Quando o usuário clica em 🔄 Atualizar

Então nada é alterado pra esse item
E o bloco "### Auto-organização" registra `⏳ aguardando resultado` pra ele

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-034 Fila viva: card aberto sem pendência ganha item na fila

Dado que existe um card em 02 Demandas (fora de Concluídas) sem nenhum item ativo com o SGV/MEL dele em "A fazer hoje"

Quando o usuário clica em 🔄 Atualizar

Então um item entra em "A fazer hoje" ("Acompanhar SGV-XXXX (título)" ou "Cadastrar melhoria MEL-NNNN no Notion" pra card sem SGV)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-035 Fila viva: pendência no "Pendente para amanhã" de hoje sobe pra fila

Dado que a pendência de uma demanda em aberto está em "Pendente para amanhã" da daily de hoje (e não em "A fazer hoje")

Quando o usuário clica em 🔄 Atualizar

Então o item é movido do "Pendente para amanhã" pro "A fazer hoje", mantendo o texto original

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-036 Botão é idempotente: clicar de novo não duplica nada

Dado que o botão acabou de processar a daily (continuações, carry-over, fila viva)

Quando o usuário clica em 🔄 Atualizar novamente

Então a notificação informa que não havia nada a fazer
E nenhuma linha, card ou pendência é duplicado

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-037 Copy tipada: a frase diz o tipo da demanda

Dado que uma pendência de melhoria foi concluída com `(aprovada)` e uma de bug com `(reprovada)`

Quando o usuário clica em 🔄 Atualizar

Então a linha da melhoria diz `✅ SGV-XXXX - Melhoria aprovada em <ambiente>` (tipo lido do card)
E a linha do bug diz `🔴 SGV-XXXX - Reaberta em <ambiente>` (bug é o padrão, sem prefixo)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 9 — Refinar demanda já cadastrada (Notion → vault)**

## CT-038 Refinamento gera card tipado + pendência do próximo passo na fila

Dado que uma task já cadastrada no Notion (com SGV) foi refinada no vault

Quando o card é criado (template certo, arquivo `<SGV> - <título>`, task preenchida, critérios de aceite)

Então a daily registra `📝 SGV-XXXX - <Tipo> refinado(a) (critérios de aceite prontos)` — nunca "Refinada" sem tipo
E um item com o próximo passo da demanda entra em "A fazer hoje" (se faltar, o botão 🔄 cria/move sozinho)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

**Fluxo 10 — Ciclo por estágios + reconciliação (a frase é a fonte da verdade)**

## CT-039 Cada estágio vivido no dia vira linha própria em Atividades

Dado que uma melhoria nasceu, foi refinada e foi levada pro Notion no mesmo dia (ou em dias diferentes)

Quando as Atividades das dailies envolvidas forem lidas

Então cada estágio aparece como linha própria, no dia em que aconteceu, com a copy tipada: `💭 Melhoria proposta` → `📝 Melhoria refinada (card criado)` → `📤 ... atualizado(a) no Notion` → `💡 Melhoria cadastrada (MEL-NNNN)`
E nenhum estágio executado fica sem registro — a trilha de emojis conta o caminho completo

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-040 Registrar direto o fim do ciclo sincroniza o card e infere os passos anteriores

Dado que um card está em DEV e o usuário escreve à mão em Atividades `✅ SGV-XXXX - Aprovada em homologação` (sem pendência, sem passar pelas etapas intermediárias no vault)

Quando o usuário clica em 🔄 Atualizar

Então o card avança até o estado declarado (status resolvido, data de fim, movido pra Concluídas)
E o Histórico registra a frase com a nota "(etapas anteriores concluídas implicitamente)"
E clicar de novo não duplica nada (estado já refletido não é reaplicado)

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:

---

## CT-041 Ciclo do bug por estágios: suspeita → confirmado ou descartado

Dado que um possível bug foi identificado e registrado como `❓ Suspeita de bug registrada: <título>` (com a pendência "Investigar suspeita: <título>" na fila)

Quando a pendência é marcada com `(descartada: <motivo>)` ou `(confirmada)` e o usuário clica em 🔄 Atualizar

Então no descarte: a linha `🗑️ Suspeita descartada: <título> (não é bug: <motivo>)` entra em Atividades, sem card criado
E na confirmação: a pendência "Criar card do bug: <título> (via SKILL_BUGS)" entra em "A fazer hoje", e a criação do card (sessão/IA) registra `🐛 Bug confirmado (card criado)` seguindo a trilha `❓ → 🐛` na daily

Execução Passou?

- [ ] <span style="color:#2ecc71">Sim</span>
- [ ] <span style="color:#e74c3c">Não</span>

Evidências de Testes:
