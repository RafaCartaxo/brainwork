---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: Rafael
pontos: ""
---

# Plano de teste — SGV-11083

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
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
| [[03 - Casos de teste#^ct-001\|CT-001]] a [[03 - Casos de teste#^ct-033\|CT-033]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** funcionalidade implementada em DEV (backlog no Notion — ainda não iniciada).
**Saída:** 33 CTs executados, C21 desbloqueado pela definição do Produto.
