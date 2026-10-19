---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — SGV-12272

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Confirmar que os 20 CTs (a redigir em `03 - Casos de teste.md`) cobrem fielmente os 20 cenários aprovados na Proposta da Onda 1 (SGV-12200), com rastreabilidade direta ao TR preservada em cada CT.

---

## Riscos e escopo

- **Risco principal:** perder rastreabilidade ao TR, ou introduzir requisito não sustentado pela Proposta/Modelo-alvo/Matriz, ao converter cenário em CT.
- **Fora do escopo desta rodada:** automação, execução, arquitetura seed/.env, Onda 2.

---

## Estratégia de teste

- **Funcional/manual:** os 20 CTs nascem como casos manuais (Gherkin) — sem automação nesta demanda.
- **Regressão:** não aplicável — cenários novos, sem baseline automatizado anterior.

Camadas de API/E2E ficam para quando a automação for planejada (fora de escopo desta demanda).

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-009\|CT-009]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-010\|CT-010]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-011\|CT-011]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-012\|CT-012]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-013\|CT-013]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-014\|CT-014]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-015\|CT-015]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |

> Lotes 1, 2 e 3 (CT-001 a CT-015) listados acima. Replique uma linha por CT a cada novo lote — CT-016 a CT-020 seguem pendentes.

---

## Entrada e saída

**Entrada:** os 20 cenários aprovados na Proposta da Onda 1 (SGV-12200).
**Saída:** 20 CTs validados, prontos para sincronização na Qase.
