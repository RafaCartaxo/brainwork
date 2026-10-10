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

Esta entrega analisa o projeto de automação e o TR completo (itens 1.1–1.43), identifica cobertura/dados reutilizáveis e recomenda próximos passos. Os 38 CTs atuais da SGV-11971 representam somente os itens 1.24–1.25. Não inclui alteração nem execução do seed.

## Próxima ação

**DISC-001–004 concluídos (07/10/2026).** Aguardando revisão final do Rafael sobre a recomendação do [[01 - Plano de automação#DISC-004 — Síntese e recomendação (07/10/2026)|DISC-004]] antes de encerrar esta entrega ou abrir a primeira das **6 entregas pequenas** recomendadas (os 3 CTs sem código — 016/017/037 — ficam fora dessa conta, sem porte previsto).

## Repositório e entrega

- **Repositório:** `sogov-automation-playwright` (leitura). Commit analisado: `16c41e4` (HEAD, worktree detached). Código das Suítes 3/4 (22 CTs) está no commit `bdf5e9a`, branch `tr-1.24-1.25-suites-3-4-5`, checked out no worktree irmão `sogov-automation-test` — não mesclado.
- **Branch/MR:** não se aplica nesta entrega de investigação — nenhum código foi escrito ou alterado.

## Pendências gerais

- Revisão final do Rafael sobre a recomendação do DISC-004.
- Identidade real do alvo entre `.env` (Playwright) e `cypress.env*.json` (Cypress) não verificada — mesmo nome de instância, backend real não comparado.

## Checklist de encerramento

- [x] Mapa do projeto e da execução atual ligados a evidências (DISC-001).
- [x] A matriz cobre os 38 CTs incluídos na demanda (DISC-002).
- [x] Dados/preparação/eixos mapeados, lacunas registradas (DISC-003).
- [x] A recomendação técnica e as lacunas foram documentadas (DISC-004) — falta só a revisão do Rafael.
- [x] O placar desta entrega registra as verificações de análise, sem confundi-las com execução funcional.
