---
tags: [qa]
task: "SGV-12082"
pai: SGV-11971
tipo: "melhoria"
status: analise
ambiente: dev
prioridade: media
etapa_atual: "QA · Análise da demanda"
modulo: Automação
responsavel: ""
aguardando: "Mapear os requisitos do PDF e relacionar a cobertura existente"
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
> **Roadmap:** [[../../../Roadmap - Automação TR|Roadmap da iniciativa]]
> **Ciclo de origem:** [[../../Arquivo/00 QA/00 README|SGV-11971 — TR 1.24–1.25]]
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
| Validação | ⏳ Aguardando análise e evidências |
| Matriz do preset | 🟡 Estrutura criada; levantamento pendente |
| Automação | 📋 Análise do projeto e dos dados; sem alteração de código nesta entrega |

**Próximo passo:** classificar os requisitos 1.1–1.43 do [[Fontes/Requisitos Sogov.pdf|TR completo]] e relacionar cobertura, tipo de evidência e dados necessários; mapear em detalhe os 38 CTs existentes de 1.24–1.25 na [[Matriz - Análise do preset provável]].

> [!warning] Escopo em análise
> A Entrega 01 sobre a instância 225 fica preservada como histórico do piloto. A SGV-12082 investiga o estado real antes de decidir se o seed precisa ser refatorado, configurado ou apenas melhor documentado. Nenhuma execução do seed é autorizada por esta entrega.

> [!tip]- Esforço e capacidade
> ```dataviewjs
> const raizDoPacote = dv.current().file.folder.split("/").slice(0, -1).join("/");
> const paginas = dv.pages('"' + raizDoPacote + '"').where(p => typeof p.pontos === "number");
> dv.table(["Artefato", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> ```

O PDF fonte foi preservado em [[Fontes/Requisitos Sogov.pdf|Fontes/Requisitos Sogov.pdf]]. Os 38 CTs da SGV-11971 cobrem apenas autenticação/ciclo de vida (1.24–1.25), não o TR completo.

Esta entrega segue o pacote de melhoria dos templates: `00 QA/` reúne demanda, plano, casos e validação; `01 Automação/` registra a leitura técnica, sem criar uma implementação antes da análise.
