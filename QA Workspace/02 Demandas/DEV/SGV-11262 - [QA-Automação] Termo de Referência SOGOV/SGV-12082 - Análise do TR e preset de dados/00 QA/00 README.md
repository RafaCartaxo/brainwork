---
tags: [qa]
task: "SGV-12082"
pai: SGV-11262
tipo: "melhoria"
status: validacao
ambiente: dev
prioridade: media
etapa_atual: "QA · Validação"
modulo: Automação
responsavel: ""
aguardando: "Revisão final do Rafael antes de encerrar ou abrir entregas"
cadastrado_por: ""
data_inicio: ""
data_fim: ""
pontos: ""
---
# SGV-12082 — Entender a automação do TR e propor o preset de dados

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Matriz do preset:** [[Matriz - Análise do preset provável]]
> **Roadmap:** [[../../Roadmap - Automação TR|Roadmap da iniciativa]]
> **Ciclo de origem:** [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/00 README|SGV-11971 — TR 1.24–1.25]]
> **Automação:** [[../01 Automação/00 - Automação|Automação]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Escopo de investigação definido |
| Plano de teste | ✅ Critérios de conclusão registrados |
| Casos de teste | ✅ Verificações documentais definidas |
| Validação | ✅ DISC-001–004 concluídos (07/10/2026) — aguardando revisão final do Rafael |
| Matriz do preset | ✅ TR completo classificado; 38/38 CTs rastreados; recomendação registrada |
| Automação | ✅ Mapa do projeto, dados por eixo e recomendação prontos; sem alteração de código nesta entrega |

**Próximo passo:** revisão final do Rafael sobre a recomendação do [[../01 Automação/01 - Plano de automação#DISC-004 — Síntese e recomendação (07/10/2026)\|DISC-004]] — só depois disso encerrar a SGV-12082 ou abrir a primeira entrega pequena.

> [!warning] Escopo em análise — nenhuma execução/implementação feita
> A Entrega 01 sobre a instância 225 fica preservada como histórico do piloto. A SGV-12082 investigou o estado real (projeto, 38 CTs, dados por eixo) e recomendou um caminho — portar os mecanismos de estado já confirmados em Cypress pro Playwright, na instância atual, em 6 entregas pequenas (os 3 CTs sem código ficam fora dessa conta, como candidatos sem porte previsto). Nenhuma execução do seed foi feita; nenhuma pasta/demanda de implementação foi criada.

> [!tip]- Esforço e capacidade
> ```dataviewjs
> const raizDoPacote = dv.current().file.folder.split("/").slice(0, -1).join("/");
> const paginas = dv.pages('"' + raizDoPacote + '"').where(p => typeof p.pontos === "number");
> dv.table(["Artefato", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> ```

O PDF fonte foi preservado em [[Fontes/Requisitos Sogov.pdf|Fontes/Requisitos Sogov.pdf]]. Os 38 CTs da SGV-11971 cobrem apenas autenticação/ciclo de vida (1.24–1.25), não o TR completo.

Esta entrega segue o pacote de melhoria dos templates: `00 QA/` reúne demanda, plano, casos e validação; `01 Automação/` registra a leitura técnica, sem criar uma implementação antes da análise.
