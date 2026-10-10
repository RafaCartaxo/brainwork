---
demanda: "[[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/01 - Demanda]]"
status: execucao
responsavel: Rafael
pontos: ""
---

# Plano de teste — SGV-11184

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/00 README|Abrir README do card]]
> **Demanda/Bug:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/01 - Demanda]]
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/04 - Validação dev]]
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar seleção de departamento como destinatário (campo pessoa e despacho), notificações por e-mail e registro de visualização externa, conforme os critérios C1-C22 (com variantes a/b/c).

---

## Riscos e escopo

- **Risco principal:** defeito SGV-11338 (truncamento de destinatário com nome extenso) ainda aberto, bloqueando C12a.
- **Fora do escopo desta rodada:** exibição/seleção de participantes do departamento; seleção de membro individual como destinatário direto; departamento como signatário de assinatura (ver Fora de escopo em `01 - Demanda`).

---

## Estratégia de teste

- **UI/E2E:** busca e seleção de departamento, accordion, notificações, visualização externa.
- **API/repositório:** persistência e revalidação de vínculo, idempotência de notificação, `DocumentInteraction`.
- **Regressão:** nenhuma prevista — funcionalidade nova.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-001\|CT-001]] a [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-022\|CT-022]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** funcionalidade implementada em DEV, validação em andamento desde 03/09/2026.
**Saída:** 21 CTs aplicáveis executados (14 aprovados, 1 reprovado aguardando fix, 6 aguardando execução); 7 CTs fora de escopo real (Não se aplica).
