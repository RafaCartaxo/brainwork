---
tags:
  - qa
  - contexto
---
# Fluxos — passo a passo

Guia prático de execução: a ordem certa de fazer cada coisa. Cada fluxo aponta pro documento canônico com a regra completa — este índice não duplica regra, só encadeia e linka. Validação destes fluxos: [[../Specs/2026-07-14-cts-fluxos-vault|CTs dos fluxos do vault]].

> [!warning] Sessão de IA? Leia [[REGRAS_IA]] antes
> Estes fluxos dizem **o que** fazer; o [[REGRAS_IA]] diz **como se comportar** ao fazer — resolver a data pelo relógio, commitar arquivo por arquivo, o que é do script e o que é do agente, propor antes de alterar doc de processo, e não presumir SGV nem ambiente.

## Mapa de atuação — aconteceu X, uso qual fluxo?

Roteamento de um olhar: acha a situação na coluna da esquerda e segue. A **ação imediata** é o primeiro passo concreto — o resto está no fluxo linkado.

| Aconteceu isso | Fluxo | Ação imediata |
|---|---|---|
| Começando o dia | 1 | Abrir a Dashboard → **✏️ daily de hoje** (não existe? 🔄 Atualizar cria) → revisar Pendências de ontem |
| Fiz/testei/vi/pensei algo e quero registrar | 2 | Escrever na seção certa da daily (na dúvida: `## Anotações`, cru — o organizador roteia) |
| Suspeitei de bug (ainda não confirmei) | 3a·0 | `❓ Suspeita de bug registrada: <título>` em Atividades + "Investigar suspeita" em A fazer hoje |
| Confirmei bug novo (reproduzível) | 3a | Gravar evidência ([[../../QA Workspace/Evidências/README\|guia]]) → card via [[../Skills/SKILL_BUGS\|SKILL_BUGS]] |
| Um **CT de uma Melhoria reprovou em DEV** | 3i | É **Defeito**, não Bug: card com `pai: "<SGV da task>"` → a pai volta a `🔴 Reaberta em DEV` |
| Vou validar demanda em DEV / HML / hotfix | 3b / 3c / 3d | Executar os CTs do card, gravar evidência, frase padrão na daily |
| Bug investigado não reproduz / cenário não existe | 3e | [[../Contexto/PADROES_QA#Descarte de bug/suspeita (99 Arquivo)\|Regra de descarte]] → `🗑️` na daily |
| Chegou task só de API | 3f | Definir critérios no card; validação pula DEV, direto em homologação |
| Validação reprovou **e** abriu bug novo (SGV próprio) | 3g | Marcar a pendência com `(reprovada em <ambiente>, bug SGV-YYYY aberto)` — o organizador completa o resto |
| Tive ideia de melhoria do produto | 4 | Checkbox `**MEL-NNNN · Título**` em Melhorias propostas (próximo número: Dashboard) → [[../Skills/SKILL_MELHORIA\|SKILL_MELHORIA]] |
| Gravei um vídeo de validação | 5 | [[../../QA Workspace/Evidências/README\|Evidências/README]] — renomear e mover **no mesmo dia** |
| Chegou demanda já cadastrada pra refinar | 6 | Conduzir a mesa → [[../Skills/SKILL_REFINAMENTO\|SKILL_REFINAMENTO]] (material → `05 Refinar/` → Destilado → gate de doc → CTs → card) |
| Fechando o dia | 7 | Anotar resultado curto nos checkboxes feitos → Pendente para amanhã → 🔄 Atualizar |
| Exportei documentação do projeto | 8 | Limpar → classificar → template Conhecimento.md → `04 Conhecimento/` |
| Quero estudar/pesquisar algo (fonte externa) | — | Nota por tópico (template Estudo.md) → [[../../QA Workspace/06 Estudos/README\|06 Estudos]]; gradua pra `04 Conhecimento` quando vira regra estável |
| Exportei view de sprint do Notion | 9 | Agrupar por status, cruzar com vault, divergências → `Planejamento/SP<N>` → [[../Skills/SKILL_TRIAGEM_SPRINT\|SKILL_TRIAGEM_SPRINT]] |
| Exportei .md do Notion (não sei o tipo) | — | Pedir "processa o material novo" — o [[../Agentes/AGENTE_PROCESSAR_EXPORT\|agente]] classifica e roteia |
| Tenho um MR do GitLab pra revisar o escopo | — | Colar o link (+ problema original, se tiver) → [[../Skills/SKILL_REVISAO_ESCOPO_MR\|SKILL_REVISAO_ESCOPO_MR]] |
| Tenho um teste e2e pronto pra subir | — | Revisar padrão + coerência de asserts → [[../Skills/SKILL_REVISAO_AUTOMACAO_E2E\|SKILL_REVISAO_AUTOMACAO_E2E]] |
| Quero conferir um bug/demanda contra a documentação | — | Identificar o módulo → cruzar contra `04 Conhecimento/Módulos/` → [[../Skills/SKILL_VERIFICACAO_DOC\|SKILL_VERIFICACAO_DOC]] |
| Quero iniciar automação de um card | 3h | Conferir gates (card validado + fix no ambiente do Cypress) → repo `sogov-automation-test` → [[../Skills/SKILL_INICIAR_AUTOMACAO\|SKILL_INICIAR_AUTOMACAO]] |
| Quero subir CTs de um card pra Qase | 3j | Filtrar CTs aplicáveis (fora os "Não se aplica") → rascunho "Preparação Qase" → [[../Skills/SKILL_SYNC_QASE\|SKILL_SYNC_QASE]] |
| Documento/card fora do padrão do vault | — | Revisar grafia/estrutura/copy oficial → [[../Skills/SKILL_PADRONIZACAO\|SKILL_PADRONIZACAO]] |
| Quero que a IA organize tudo que ficou cru | — | Pedir "organiza a daily" — cobre parte mecânica + classificação ([[../Agentes/AGENTE_ORGANIZADOR\|AGENTE_ORGANIZADOR]]) |

---

## 1. Começar o dia

> [!important] Antes de tudo: **resolver a data de hoje pelo relógio** (`date +%F`) — o daily é sempre o de hoje. Não reusar data cacheada (a sessão pode ter cruzado a meia-noite). Ver [[../Contexto/PADROES_QA#Regra de data|Regra de data]].

1. Abrir a [[../../QA Workspace/Dashboard/Dashboard|Dashboard]].
2. Conferir **Pendências em aberto** e **Melhorias propostas em aberto**.
3. Clicar em **✏️ Escrever na daily de hoje** (ou `Ctrl+P` → "Daily notes: Open today's daily note").
4. Revisar o callout **Pendências de ontem** (recolhido) e marcar em **A fazer hoje** o que continua valendo.
5. Conferir o bloco **Status — reunião** (regras: [[../../QA Workspace/01 Daily/README#Status — reunião (primeira seção da daily)\|01 Daily/README]]).

A partir daqui, o dia inteiro acontece dentro da daily.

### O que "processa" significa

Quando o Rafael diz **"processa"**, **"processa o dia"** ou **"organiza a daily"**, ele está pedindo os cinco passos abaixo — **não só apertar o botão**. Essa ambiguidade já custou um dia de fila fora do padrão (28/07).

| # | Passo | Executor |
|---|---|---|
| 1 | Rodar o **🔄 Atualizar** (ou `python3 .obsidian/scripts/qa-atualiza.py`) | Script |
| 2 | **Agrupar a fila** nos 7 grupos de [[../../QA Workspace/01 Daily/README#Grupos da fila ("A fazer hoje")\|01 Daily/README]] | [[../Agentes/AGENTE_FILA\|AGENTE_FILA]] — **sessão de IA** |
| 3 | **Regenerar o Status — reunião** por inteiro (derivado de Atividades + fila) | [[../Agentes/AGENTE_STATUS_REUNIAO\|AGENTE_STATUS_REUNIAO]] — **sessão de IA** |
| 4 | **Classificar registro cru**, se houver linha em Anotações/Bugs encontrados sem a marca ` → ` | [[../Agentes/AGENTE_ORGANIZADOR\|AGENTE_ORGANIZADOR]] — **sessão de IA** |
| 5 | **Ler os avisos** do callout `[!organizacao]- Auto-organização` e agir em cada um (ou registrar por que não) | Sessão de IA |

> [!warning] O botão sozinho **não** fecha o processamento
> O `qa-atualiza.py` é Python: cria a daily, faz carry-over, envelhece a fila, recolhe os `[x]`, reconcilia cards, roteia evidência e escreve o log. Ele **não agrupa a fila**, **não gera o Status** e **não faz gate de doc** — isso é julgamento, e julgamento é da camada de IA ([[../Agentes/AGENTE_FILA#Fronteira com o script\|fronteira]]).
>
> Apertar o botão e parar deixa a fila sem grupos e o Status vazio. Foi exatamente o que aconteceu em 28/07 — e a "correção" de então foi pior: mover o agrupamento pra dentro do script.

Os cinco passos são de **uma sessão só**, em sequência — não é rodar o script hoje e agrupar a fila amanhã. Quem para no passo 1 deixa a daily pela metade, e quem retoma depois não tem como saber o que já foi feito.

> [!tip] Abriu o vault com um ou mais dias sem processar?
> **Não tem protocolo especial — o script já trata.** Ele carrega as pendências da **daily mais recente** (não "de ontem" literal) e envelhece pelo **delta real de datas**: fim de semana sem daily vale +3 dias, não +1 (`dias = (hoje - ontem[0]).days`, precedente de 27/07). Basta rodar os cinco passos normalmente.
>
> O que **não** é automático: as Atividades do dia que ficou sem processar continuam sem classificação. Se havia registro cru lá, abrir aquela daily e rodar o passo 4 nela também.

Depois de processar, **conferir**: os 4 callouts da daily íntegros (nenhuma linha sem `>` dentro de um `[!...]`), e rodar o 🔄 **duas vezes** — a segunda não deve mudar nada. Se mudar, algo não é idempotente e vale investigar antes de seguir.

## 2. Registrar algo durante o dia

Regra de bolso: **escreveu? foi na daily. quer ver? foi na Dashboard.**

| O que aconteceu | Onde registrar |
|---|---|
| Fiz/testei algo | `## Atividades` (frase padrão do [[../../QA Workspace/01 Daily/README\|01 Daily/README]]) |
| Planejei/refinei/triei/documentei | `## Atividades` → `### Planejamento` |
| Vi um bug | `## Bugs encontrados` |
| Tive ideia de melhoria | `## Melhorias propostas` (checkbox) |
| Lembrete pra depois | `## Pendente para amanhã` |
| Não sei classificar | `## Anotações`, cru, sem pensar |

O que cair em **Anotações** ou **Bugs encontrados** sem estrutura, o auto-organizador ([[../Agentes/AGENTE_ORGANIZADOR\|AGENTE_ORGANIZADOR]]) roteia. Dois caminhos reais: o 🔄 cobre só a **mecânica** (não classifica nada), e a classificação acontece numa **sessão de IA** ("organiza a daily" / "processa o dia"). O modo agendado das 7h é ⚠️ **previsto, sem cron ativo**.

## 3. Esteira do bug (DEV → HML → Concluída)

O ciclo completo de vida do bug está em [[../../QA Workspace/02 Demandas/README\|02 Demandas/README]] e [[../Contexto/PADROES_QA#Organização de Bugs\|PADROES_QA]]. O skill de criação de card está em [[../Skills/SKILL_BUGS\|SKILL_BUGS]].

### 3a. Da suspeita ao card
1. Identificou possível bug? `❓ Suspeita` em Atividades + "Investigar suspeita" na fila
2. Confirmou? Gravar evidência ([[../../QA Workspace/Evidências/README\|guia]])
3. Criar card em `02 Demandas/DEV/` via [[../Skills/SKILL_BUGS\|SKILL_BUGS]]
4. Daily: `🐛 SGV-XXXX - Bug cadastrado` + entrada em Bugs encontrados
5. Pendência de cadastro no Notion na fila

### 3b–3d. Validar em DEV / HML / Hotfix
Executar CTs → gravar evidência → **gate de doc (abaixo)** → frase padrão na daily. Aprovou? Mover card pra próxima pasta (DEV→HML→Concluídas) — movimentação atômica via [[../Agentes/AGENTE_MIGRACAO_CARDS\|AGENTE_MIGRACAO_CARDS]] (dispara ao marcar o checkbox com o resultado). Reprovou? Reabrir + pendência de revalidação. Regras de movimentação: [[../Contexto/PADROES_QA#Organização de Bugs\|PADROES_QA]].

**Reprovou executando o CT de uma task pai, em DEV?** Aí não é bug — é **Defeito**, e o ciclo é o do fluxo 3i abaixo.

**Gate obrigatório antes de ✅ e de mover o card**: cruzar o comportamento aprovado contra a doc do módulo ([[../Skills/SKILL_VERIFICACAO_DOC\|SKILL_VERIFICACAO_DOC]]) e registrar o veredito. Aprovado contradiz a doc → decisão de Produto + pendência de atualizar; doc **não existe** → pendência de importar (fluxo 8). Rede de segurança: [[../Agentes/AGENTE_VALIDACAO_DOC\|AGENTE_VALIDACAO_DOC]] sinaliza aprovações sem esse registro.

### 3e. Descartar
`status: descartado` → CTs marcados Sim → mover pra `99 Arquivo/` → `🗑️` na daily. Regra completa: [[../Contexto/PADROES_QA#Descarte de bug/suspeita (99 Arquivo)\|PADROES_QA]].

### 3f. Tasks só de API
QA define critérios → dev implementa cenários → QA revisa → teste direto em homologação. Sem esteira DEV. Regras completas: [[../Contexto/PADROES_QA#Tasks de API (fluxo 3f)\|PADROES_QA]].

### 3g. Reprovação com bug novo (SGV próprio)
Duas demandas nascem: a original reaberta + card novo pro bug. Marcar a pendência com `(reprovada em <ambiente>, bug SGV-YYYY aberto)` e o [[../Agentes/AGENTE_ORGANIZADOR\|organizador]] completa o resto.

### 3h. Após aprovar: preparar automação
Fecha a ponte validação → automação. Card aprovado (idealmente em HML) e com CTs prontos → conferir os gates (card validado + fix no ambiente que o Cypress ataca) → [[../Skills/SKILL_INICIAR_AUTOMACAO\|SKILL_INICIAR_AUTOMACAO]] → escrever o teste (guia no repo `sogov-automation-test`) → revisar ([[../Skills/SKILL_REVISAO_AUTOMACAO_E2E\|SKILL_REVISAO_AUTOMACAO_E2E]]) → commit/MR + atualizar Histórico do card. Gates abertos → pendência `⏳` com o motivo, não iniciar.

### 3i. Defeito (filho de task pai)

CT de uma Melhoria/Funcionalidade reprovou **em DEV**? O problema é **Defeito**, não Bug — regra completa em [[../Contexto/PADROES_QA#Defeito × Bug|PADROES_QA → Defeito × Bug]].

1. **Criar o card do defeito** ([[../Skills/SKILL_BUGS|SKILL_BUGS]]) com `pai: "<SGV da task>"` no frontmatter, tag `defeito` e arquivo `<SGV> - Defeito <Título>`
2. **Apontar do CT pro defeito**: o CT do pai que reprovou linka o card do defeito
3. **A task pai volta a `🔴 Reaberta em DEV`** (regra de reabertura) — na daily: `🐛 SGV-XXXX - Defeito cadastrado (da SGV-YYYY)`
4. Dev corrige → **revalidar o CT afetado no card do pai**, não o defeito isolado
5. CT passou → **callout de reconciliação** no CT ([[../Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]]) + defeito fecha em `Concluídas/` com `ambiente: DEV` e o Histórico nomeando a pai
6. **Gate**: sem defeito aberto, a Melhoria pode ser aprovada em DEV e seguir pra `HML/`

> [!warning] Defeito aberto **bloqueia** a aprovação da pai em DEV
> Identificou, resolve. Aprovar entrega cujo próprio CT reprovou é registro falso. Exceção (produto adia o fix) exige decisão explícita registrada no card do pai — o `🔄` avisa quando a aprovação chega com defeito filho ainda aberto.

Na fila, o defeito **não ocupa linha própria** — aparece aninhado sob a linha da pai. E **em homologação não se reteste defeito**: valida-se a Melhoria inteira, e problema encontrado lá é **Bug** (esteira completa, sem `pai:`).

### 3j. Após aprovar: subir CTs pra Qase
Fecha a ponte validação → repositório de casos da Qase, em paralelo à automação (fluxo 3h). CTs prontos (Dado/Quando/Então já escritos no card) → filtrar quais aplicam de fato (fora os marcados "Não se aplica" — não representam cenário real da entrega) → identificar mecânica repetida entre CTs (candidato a shared step) → escrever/atualizar o rascunho "Preparação Qase" em `04 Conhecimento/Tasks/<epic>/<parte>/` → [[../Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]] (mapeia campos, gera `corrections.json`, roda dry-run → lote isolado → `--apply` via `sogov-automation-test/scripts/qase-sync-<contexto>/`) → rascunho vira registro com os ids/hashes da Qase.

## 4. Melhoria: da ideia ao cadastro

Orquestrado pela [[../Skills/SKILL_MELHORIA|SKILL_MELHORIA]] (7 passos: ideia → refinar → plano → CTs → card → Notion → esteira).

1. Checkbox `**MEL-NNNN · Título**` em Melhorias propostas + `💭 MEL-NNNN - Melhoria proposta` em Atividades
2. Refinar escopo + regras de negócio ([[../Skills/SKILL_REFINAMENTO|SKILL_REFINAMENTO]] como sub-passo) → plano de teste ([[../Skills/SKILL_PLANO_DE_TESTE|SKILL_PLANO_DE_TESTE]]) → CTs ([[../Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]])
3. Criar card hub [[../Templates/Demanda.md|Demanda]] em `02 Demandas/DEV/` → `📝 MEL-NNNN - Melhoria refinada (card criado)`
4. Cadastrar no Notion → ganha SGV → renomear arquivo → `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)`
5. **Validar em DEV**: executar os CTs. CT que reprovar vira **Defeito** (fluxo 3i), não Bug — a pai reabre e só é aprovada quando não houver defeito aberto.
6. Aprovada em DEV → `HML/`, onde se valida **a Melhoria como um todo**. Problema encontrado em homologação é **Bug** (esteira completa). Regras completas: [[../../QA Workspace/01 Daily/README#Regra de Melhorias propostas\|01 Daily/README]].

## 5. Evidência

Guia completo em [[../../QA Workspace/Evidências/README\|Evidências/README]].

## 6. Refinar demanda já cadastrada

Conduzido pela [[../Skills/SKILL_REFINAMENTO\|SKILL_REFINAMENTO]]: material bruto em `05 Refinar/` → análise na mesa ([[../Templates/Refinamento.md|Refinamento.md]], regra das 2 pendências) → **gate de doc** → Destilado → **CTs** → card → Notion atualizado → mesa arquivada em `04 Conhecimento/`. Regras completas: [[../../QA Workspace/05 Refinar/README\|05 Refinar/README]].

Encadeamento do fim da mesa: ao fechar o Destilado (resultado esperado + critérios), **gate obrigatório** de cruzar contra a doc do módulo ([[../Skills/SKILL_VERIFICACAO_DOC\|SKILL_VERIFICACAO_DOC]]); depois criar o card ([[../Skills/SKILL_BUGS\|SKILL_BUGS]]) e os casos de teste ([[../Skills/SKILL_CASOS_DE_TESTE\|SKILL_CASOS_DE_TESTE]]) — um CT por critério de aceite.

## 7. Fechar o dia

1. Marcar itens de **A fazer hoje** com resultado entre parênteses — o [[../Agentes/AGENTE_ORGANIZADOR\|organizador]] completa o resto
2. Preencher `## Pendente para amanhã`
3. Conferir se não sobrou vídeo cru na raiz de `Evidências/`
4. Clicar **🔄 Atualizar** na Dashboard

## 8. Importar documentação do projeto

Export .md bruto → limpar ([[../Skills/SKILL_LIMPEZA_EXPORT\|SKILL_LIMPEZA_EXPORT]], modo C) → classificar (módulo? fluxo? referência?) → template [[../Templates/Conhecimento.md\|Conhecimento.md]] → `04 Conhecimento/<subpasta>/`.

| Tipo | Pasta | Exemplo |
|---|---|---|
| Módulo do sistema | `Módulos/` | Assinaturas, Workflow, Mesa de trabalho |
| Fluxo ponta a ponta | `Fluxos/` | Ciclo de vida do documento |
| Doc externa (repo, lei, manual) | `Referências/` | Docs do repositório, leis, normativas |

Regra de ouro: **importar ≠ copiar tudo**. Trazer só o que ajuda a testar (regras, restrições, perfis, estados). O resto vira link na seção Referências. Na daily: `📚 <Doc> - Documentação importada/atualizada (<escopo curto>)` em Atividades → Planejamento. Regras completas: [[../../QA Workspace/04 Conhecimento/README\|04 Conhecimento/README]].

## 9. Triagem de sprint

Export da view de sprint do Notion (dezenas de cards num arquivo) → [[../Skills/SKILL_TRIAGEM_SPRINT\|SKILL_TRIAGEM_SPRINT]]. Pipeline: agrupar por status → cruzar com cards existentes no vault → identificar divergências Notion × vault → criar página em `Planejamento/SP<N>.md`. Na daily: `📋 Planejamento <sprint> - <n>/<total> cards batidos` em Planejamento.

O agente [[../Agentes/AGENTE_PROCESSAR_EXPORT\|AGENTE_PROCESSAR_EXPORT]] automatiza a classificação e o roteamento — você dropa o .md e ele decide o caminho.
