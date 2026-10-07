---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: "sogov-automation-playwright"
framework: playwright
ambiente: dev
status: planejado
---

# Automação — SGV-12082

> [!info]- Navegação QA
> **README:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos de análise:** [[../00 QA/03 - Casos de teste]]
> **Matriz do preset:** [[../00 QA/Matriz - Análise do preset provável]]
> **Plano:** [[01 - Plano de automação]]
> **Validação:** [[02 - Validação automação]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(bloqueado),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

Esta entrega analisa a automação e a massa atual para recomendar próximos passos. Não inclui alteração nem execução do seed.

## Próxima ação

- Mapear os CTs de origem caso a caso e cruzar com código, fixtures e configuração ambiental, registrando evidências na matriz.

## Repositório e entrega

- **Repositório:** `sogov-automation-playwright` (leitura; confirmar branch/commit da análise).
- **Branch/MR:** não se aplica nesta entrega de investigação.

## Pendências gerais

- Confirmar os ambientes e a configuração disponíveis para inspeção sem revelar valores secretos.
- Reconciliar framework e estado de cada CT que não esteja entre os 13 já identificados em Playwright.

## Checklist de encerramento

- [ ] Mapa do projeto e da execução atual ligados a evidências.
- [ ] A matriz cobre os CTs incluídos na demanda.
- [ ] A recomendação técnica e as lacunas foram revisadas.
- [ ] O placar desta entrega registra as verificações de análise, sem confundi-las com execução funcional.
