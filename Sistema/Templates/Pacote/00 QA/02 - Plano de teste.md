---
demanda: "[[Sistema/Templates/Pacote/00 QA/Melhoria/01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — <ID>

> [!info]- Navegação QA
> **README do card:** [[Sistema/Templates/Pacote/00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[Sistema/Templates/Pacote/00 QA/Melhoria/01 - Demanda]]
> **Plano de teste:** [[Sistema/Templates/Pacote/00 QA/02 - Plano de teste]]
> **Casos de teste:** [[Sistema/Templates/Pacote/00 QA/03 - Casos de teste]]
> **Validação:** [[Sistema/Templates/Pacote/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[Sistema/Templates/Pacote/00 QA/05 - Preparação Qase]]
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — só quando houver cobertura automatizada)*

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

---

## Riscos e escopo

- **Risco principal:**
- **Fora do escopo desta rodada:**

---

## Estratégia de teste

- **Unitário:** regras e serviços isolados.
- **API/repositório:** contrato, validações e persistência.
- **UI/E2E:** comportamento do usuário e integração entre campos/telas.
- **Regressão:** fluxos existentes afetados pela mudança.

Defina apenas as camadas aplicáveis; não crie testes por obrigação quando não houver risco naquela camada.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[Sistema/Templates/Pacote/00 QA/03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI/API | Manual | [[Sistema/Templates/Pacote/00 QA/04 - Validação dev\|Registrar resultado]] |

> Replique a linha para cada CT do pacote.

---

## Entrada e saída

**Entrada:**
**Saída:**
