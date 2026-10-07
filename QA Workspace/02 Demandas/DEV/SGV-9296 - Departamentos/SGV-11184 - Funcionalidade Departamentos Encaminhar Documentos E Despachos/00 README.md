---
tags: [qa]
task: "11184"
pai: ""
tipo: "funcionalidade"
status: analise
ambiente: dev
prioridade: media
etapa_atual: "QA · Validação"
modulo: servicos-pj
responsavel: Rafael
aguardando: ""
cadastrado_por: ""
data_inicio: 2026-09-03
data_fim: ""
pontos: ""
---
# SGV-11184 — Departamentos: encaminhar documentos e despachos

> [!info]- Navegação QA/DEV
> **Demanda:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/01 - Demanda]]
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/04 - Validação dev]]
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/05 - Preparação Qase]]
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
| Casos de teste | ✅ Preparados (CT-001 a CT-022, com variantes a/b/c — 28 no total) |
| Validação | 🟡 Aprovado com ressalvas — 20/21 CTs aplicáveis aprovados (6 via aprovação geral da task em DEV, 02/10/2026), 1 reprovado (CT-012a, defeito SGV-11338 aberto); 7 marcados Não se aplica (nível "participantes" fora desta entrega) |
| Preparação Qase | 📤 Enviado (21 casos aplicáveis + 2 shared steps na suite SGV/220, 04/09/2026) |
| Automação | ⏳ |

**Próximo passo:** DEV corrigir o defeito SGV-11338 (truncamento de destinatário com nome extenso); CT-012a é o único CT real ainda pendente.

> [!info]- Origem
> **Parte 2** da epic [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]], irmã da [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/01 - Demanda|SGV-11083 (Parte 1)]]. SGV-11184 no Notion ("[Parte 2] Departamentos: Encaminhar documentos/despachos para o departamento"). Refinado a partir do requisito técnico do Notion.

Pacote para `SGV-11184`:

```text
SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
├── 05 - Preparação Qase.md
└── Defeitos/
    └── SGV-11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo.md
```

---
