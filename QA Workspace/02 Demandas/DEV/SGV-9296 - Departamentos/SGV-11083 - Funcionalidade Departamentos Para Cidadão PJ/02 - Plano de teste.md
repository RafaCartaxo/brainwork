---
demanda: "[[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/01 - Demanda]]"
status: planejado
responsavel: Rafael
pontos: ""
---

# Plano de teste — SGV-11083

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/00 README|Abrir README do card]]
> **Demanda/Bug:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/01 - Demanda]]
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/04 - Validação dev]]
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar criação, gerenciamento de participantes, listagem/visualização, exclusão e suspensão de departamentos de Pessoa Jurídica, conforme os critérios C1-C33.

---

## Riscos e escopo

- **Risco principal:** definição pendente do Produto sobre a contagem da coluna "Participantes" (C21) pode exigir reteste depois de fechada.
- **Fora do escopo desta rodada:** edição formal de um departamento já criado (ver Fora de escopo em `01 - Demanda`).

---

## Estratégia de teste

- **UI/E2E:** fluxos de criação, vínculo/desvínculo de participante, exclusão e suspensão.
- **API/repositório:** validações de obrigatoriedade/duplicidade revalidadas pela API, independente da interface.
- **Regressão:** nenhuma prevista — funcionalidade nova, sem fluxo existente afetado.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-001\|CT-001]] a [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-033\|CT-033]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** funcionalidade implementada em DEV (backlog no Notion — ainda não iniciada).
**Saída:** 33 CTs executados, C21 desbloqueado pela definição do Produto.
