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

- **Unitário:** não aplicável — não há código/regra isolada sendo desenvolvida nesta demanda; os 20 cenários cobrem funcionalidade já existente no sistema.
- **API/repositório:** não aplicável nesta rodada — os 20 CTs nascem como casos manuais; a camada de API fica para quando a automação for planejada (fora de escopo desta demanda).
- **UI/E2E:** os 20 CTs nascem como casos manuais (Gherkin), cobrindo o comportamento observável pelo usuário na interface — sem automação nesta demanda.
- **Regressão:** não aplicável — cenários novos, sem baseline automatizado anterior.

Defina apenas as camadas aplicáveis; não crie testes por obrigação quando não houver risco naquela camada.

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
| [[03 - Casos de teste#^ct-016\|CT-016]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-017\|CT-017]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-018\|CT-018]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-019\|CT-019]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-020\|CT-020]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |

> Matriz completa: os 20 CTs (CT-001 a CT-020) estão listados acima, cada um rastreável ao seu cenário de origem em `03 - Casos de teste.md`.

---

## Entrada e saída

**Entrada:** os 20 cenários aprovados na Proposta da Onda 1 (SGV-12200).
**Saída:** 20 CTs validados, prontos para sincronização na Qase.
