---
tags: [qa]
task: "11083"
pai: ""
tipo: "funcionalidade"
status: analise
ambiente: dev
prioridade: media
etapa_atual: "QA · Casos de teste"
modulo: servicos-pj
responsavel: Rafael
aguardando: ""
cadastrado_por: ""
data_inicio: 2026-09-02
data_fim: ""
pontos: ""
---
# SGV-11083 — Departamentos para cidadão Pessoa Jurídica

> [!info]- Navegação QA/DEV
> **Demanda:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/01 - Demanda]]
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/04 - Validação dev]]
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Preparada |
| Plano de teste | ⏳ |
| Casos de teste | ✅ Preparados (CT-001 a CT-033) |
| Validação | ✅ 33/33 CTs aprovados — aprovação geral da task em DEV (02/10/2026), execução individual não registrada neste vault |
| Preparação Qase | ⏳ |
| Automação | ⏳ |

**Próximo passo:** preparar os 33 CTs pra envio na Qase. 1 ponto em aberto (CT-021, contagem da coluna "Participantes") segue aguardando definição do Produto, sem bloquear a aprovação geral.

> [!info]- Origem
> **Parte 1** da epic [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]], irmã da [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/01 - Demanda|SGV-11184 (Parte 2)]]. SGV-11083 no Notion ("[Parte 1] Departamentos: Criação, edição, exclusão, suspensão e gerenciamento de membros"). Refinado a partir de 3 documentos do Notion (requisito técnico completo, doc de produto consolidado, resumo em formato de QA).

Pacote para `SGV-11083`:

```text
SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---
