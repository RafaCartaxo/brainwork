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
| *(a preencher ao redigir os 20 CTs em [[03 - Casos de teste]])* | | | | |

> Replique uma linha por CT quando os 20 forem redigidos — nenhum CT foi criado ainda nesta preparação.

---

## Entrada e saída

**Entrada:** os 20 cenários aprovados na Proposta da Onda 1 (SGV-12200).
**Saída:** 20 CTs validados, prontos para sincronização na Qase.
