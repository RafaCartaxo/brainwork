---
tags:
  - qa
  - contexto
---
# Fluxos — passo a passo

Guia prático de execução: a ordem certa de fazer cada coisa. Cada fluxo aponta pro documento canônico com a regra completa — este índice não duplica regra, só encadeia e linka. Validação destes fluxos: [[../Specs/2026-07-14-cts-fluxos-vault|CTs dos fluxos do vault]].

## Mapa de atuação — aconteceu X, uso qual fluxo?

Roteamento de um olhar: acha a situação na coluna da esquerda e segue. A **ação imediata** é o primeiro passo concreto — o resto está no fluxo linkado.

| Aconteceu isso | Fluxo | Ação imediata |
|---|---|---|
| Começando o dia | 1 | Abrir a Dashboard → **✏️ daily de hoje** (não existe? 🔄 Atualizar cria) → revisar Pendências de ontem |
| Fiz/testei/vi/pensei algo e quero registrar | 2 | Escrever na seção certa da daily (na dúvida: `## Anotações`, cru — o organizador roteia) |
| Suspeitei de bug (ainda não confirmei) | 3a·0 | `❓ Suspeita de bug registrada: <título>` em Atividades + "Investigar suspeita" em A fazer hoje |
| Confirmei bug novo (reproduzível) | 3a | Gravar evidência ([[../../QA Workspace/Evidências/README\|guia]]) → card via [[../Skills/SKILL_BUGS\|SKILL_BUGS]] |
| Vou validar demanda em DEV / HML / hotfix | 3b / 3c / 3d | Executar os CTs do card, gravar evidência, frase padrão na daily |
| Bug investigado não reproduz / cenário não existe | 3e | [[../Contexto/PADROES_QA#Descarte de bug/suspeita (99 Arquivo)\|Regra de descarte]] → `🗑️` na daily |
| Chegou task só de API | 3f | Definir critérios no card; validação pula DEV, direto em homologação |
| Validação reprovou **e** abriu bug novo (SGV próprio) | 3g | Marcar a pendência com `(reprovada em <ambiente>, bug SGV-YYYY aberto)` — o organizador completa o resto |
| Tive ideia de melhoria do produto | 4 | Checkbox `**MEL-NNNN · Título**` em Melhorias propostas (próximo número: Dashboard) |
| Gravei um vídeo de validação | 5 | [[../../QA Workspace/Evidências/README\|Evidências/README]] — renomear e mover **no mesmo dia** |
| Chegou demanda já cadastrada pra refinar | 6 | Conduzir a mesa → [[../Skills/SKILL_REFINAMENTO\|SKILL_REFINAMENTO]] (material → `05 Refinar/` → Destilado → gate de doc → CTs → card) |
| Fechando o dia | 7 | Anotar resultado curto nos checkboxes feitos → Pendente para amanhã → 🔄 Atualizar |
| Exportei documentação do projeto | 8 | Limpar → classificar → template Conhecimento.md → `04 Conhecimento/` |
| Quero estudar/pesquisar algo (fonte externa) | — | Nota por tópico (template Estudo.md) → [[../../QA Workspace/06 Estudos/README\|06 Estudos]]; gradua pra `04 Conhecimento` quando vira regra estável |
| Exportei view de sprint do Notion | 9 | Agrupar por status, cruzar com vault, divergências → `05 Refinar/Triagem - <sprint>` |
| Exportei .md do Notion (não sei o tipo) | — | Pedir "processa o material novo" — o [[../Agentes/AGENTE_PROCESSAR_EXPORT\|agente]] classifica e roteia |
| Tenho um MR do GitLab pra revisar o escopo | — | Colar o link (+ problema original, se tiver) → [[../Skills/SKILL_REVISAO_ESCOPO_MR\|SKILL_REVISAO_ESCOPO_MR]] |
| Tenho um teste e2e pronto pra subir | — | Revisar padrão + coerência de asserts → [[../Skills/SKILL_REVISAO_AUTOMACAO_E2E\|SKILL_REVISAO_AUTOMACAO_E2E]] |
| Quero conferir um bug/demanda contra a documentação | — | Identificar o módulo → cruzar contra `04 Conhecimento/Módulos/` → [[../Skills/SKILL_VERIFICACAO_DOC\|SKILL_VERIFICACAO_DOC]] |
| Quero iniciar automação de um card | 3h | Conferir gates (card validado + fix no ambiente do Cypress) → repo `sogov-automation-test` → [[../Skills/SKILL_INICIAR_AUTOMACAO\|SKILL_INICIAR_AUTOMACAO]] |
| Documento/card fora do padrão do vault | — | Revisar grafia/estrutura/copy oficial → [[../Skills/SKILL_PADRONIZACAO\|SKILL_PADRONIZACAO]] |
| Quero que a IA organize tudo que ficou cru | — | Pedir "organiza a daily" — cobre parte mecânica + classificação ([[../Agentes/AGENTE_ORGANIZADOR\|AGENTE_ORGANIZADOR]]) |

---

## 1. Começar o dia

1. Abrir a [[../../QA Workspace/Dashboard/Dashboard|Dashboard]].
2. Conferir **Pendências em aberto** e **Melhorias propostas em aberto**.
3. Clicar em **✏️ Escrever na daily de hoje** (ou `Ctrl+P` → "Daily notes: Open today's daily note").
4. Revisar o callout **Pendências de ontem** (recolhido) e marcar em **A fazer hoje** o que continua valendo.
5. Conferir o bloco **Status — reunião** (regras: [[../../QA Workspace/01 Daily/README#Status — reunião (primeira seção da daily)\|01 Daily/README]]).

A partir daqui, o dia inteiro acontece dentro da daily.

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

O que cair em **Anotações** ou **Bugs encontrados** sem estrutura, o auto-organizador ([[../Agentes/AGENTE_ORGANIZADOR\|AGENTE_ORGANIZADOR]]) roteia. Três gatilhos: 🔄 Atualizar (mecânica), "organiza a daily" (IA, tudo) e 7h (agendado).

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

**Gate obrigatório antes de ✅ e de mover o card**: cruzar o comportamento aprovado contra a doc do módulo ([[../Skills/SKILL_VERIFICACAO_DOC\|SKILL_VERIFICACAO_DOC]]) e registrar o veredito. Aprovado contradiz a doc → decisão de Produto + pendência de atualizar; doc **não existe** → pendência de importar (fluxo 8). Rede de segurança: [[../Agentes/AGENTE_VALIDACAO_DOC\|AGENTE_VALIDACAO_DOC]] sinaliza aprovações sem esse registro.

### 3e. Descartar
`status: descartado` → CTs marcados Sim → mover pra `99 Arquivo/` → `🗑️` na daily. Regra completa: [[../Contexto/PADROES_QA#Descarte de bug/suspeita (99 Arquivo)\|PADROES_QA]].

### 3f. Tasks só de API
QA define critérios → dev implementa cenários → QA revisa → teste direto em homologação. Sem esteira DEV. Regras completas: [[../Contexto/PADROES_QA#Tasks de API (fluxo 3f)\|PADROES_QA]].

### 3g. Reprovação com bug novo (SGV próprio)
Duas demandas nascem: a original reaberta + card novo pro bug. Marcar a pendência com `(reprovada em <ambiente>, bug SGV-YYYY aberto)` e o [[../Agentes/AGENTE_ORGANIZADOR\|organizador]] completa o resto.

### 3h. Após aprovar: preparar automação
Fecha a ponte validação → automação. Card aprovado (idealmente em HML) e com CTs prontos → conferir os gates (card validado + fix no ambiente que o Cypress ataca) → [[../Skills/SKILL_INICIAR_AUTOMACAO\|SKILL_INICIAR_AUTOMACAO]] → escrever o teste (guia no repo `sogov-automation-test`) → revisar ([[../Skills/SKILL_REVISAO_AUTOMACAO_E2E\|SKILL_REVISAO_AUTOMACAO_E2E]]) → commit/MR + atualizar Histórico do card. Gates abertos → pendência `⏳` com o motivo, não iniciar.

## 4. Melhoria: da ideia ao cadastro

1. Checkbox `**MEL-NNNN · Título**` em Melhorias propostas + `💭 MEL-NNNN - Melhoria proposta` em Atividades
2. Refinar → card [[../Templates/Demanda.md|Demanda]] em `02 Demandas/DEV/`
3. Cadastrar no Notion → ganha SGV → renomear arquivo → `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)`
4. Segue esteira normal. Regras completas: [[../../QA Workspace/01 Daily/README#Regra de Melhorias propostas\|01 Daily/README]].

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

Export da view de sprint do Notion (dezenas de cards num arquivo) → [[../Skills/SKILL_TRIAGEM_SPRINT\|SKILL_TRIAGEM_SPRINT]]. Pipeline: agrupar por status → cruzar com cards existentes no vault → identificar divergências Notion × vault → criar documento em `05 Refinar/Triagem - <sprint>`. Na daily: `📋 Triagem <sprint> - <n>/<total> cards batidos` em Planejamento.

O agente [[../Agentes/AGENTE_PROCESSAR_EXPORT\|AGENTE_PROCESSAR_EXPORT]] automatiza a classificação e o roteamento — você dropa o .md e ele decide o caminho.
