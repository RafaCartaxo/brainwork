---
tags: [qa, conhecimento, automacao]
tipo: referencia
revisado: 2026-10-16
---
# Migração Cypress → Playwright

Histórico, decisões e contexto de transição. Comandos, execução e regras de escrita: `sogov-automation-test/playwright/README.md` — ver [[00 - Índice da automação Playwright]].

> [!info] Por que esta nota existe
> A suíte Playwright entrou na `main` do `sogov-automation-test` em setembro/2026, escrita por **Waldemar Coimbra**, sem passar por nenhum registro do vault. Até 01/10/2026 **todo** documento de automação daqui — [[1.24-1.25 - Plano de Automação|Plano de Automação]], as skills, o [[FLUXOS]] — dizia "Cypress". Esta nota registra a transição.

## O estado em uma frase

**Playwright é o padrão e, desde 15/10/2026, o único. O Cypress foi removido do `main`.**

> [!success] Decisão do Rafael, 01/10/2026
> A migração está sendo finalizada. O Cypress **vai ser descartado — mas não agora**. **Teste novo só se escreve em Playwright.**
>
> A suíte Cypress continua existindo e rodando até o descarte: serve para ler o que já existe e como referência de regra de negócio. Não é lugar de escrever caso novo.

> [!success] Atualização 15/10/2026 — o descarte aconteceu
> O commit `0d6ba89` ("Remoção do código cypress"), consolidado no merge `b1a9759`, tirou o Cypress do `main`: `cypress/` ficou com **0 arquivos** (eram 233), e o `package.json` e o `.gitlab-ci.yml` da raiz foram apagados junto. O texto acima é o registro da decisão de 01/10; o estado atual é este. Para consultar regra de negócio do código Cypress antigo, só pelo histórico do git ou por branch arquivada.

Estado até 14/10/2026 (registro histórico) e a partir de 15/10/2026:

| | Cypress (raiz) — até 14/10 | Cypress — a partir de 15/10 | Playwright (`playwright/`) |
|---|---|---|---|
| Specs | ~127 testes legados | **removido** (`cypress/` com 0 arquivos) | **131 arquivos / 398 testes** (medido em 01/10) |
| Entrada | `cypress.config.js` | — | `playwright/playwright.config.ts` |
| Roda no CI | ✅ sim (`.gitlab-ci.yml`) | — | ❌ **não** (e hoje não há CI nenhum) |
| Estado | legado, a descartar | **descartado** | **padrão** — todo caso novo vem pra cá |

## Como a migração entrou

Três commits de migração, mergeados na `main` pela MR da branch `migracao-playwright` (commit de merge `1d78bf9`):

- `a8bc9c5` (20/09) — `feat: add Playwright migration suite`, o commit-raiz
- `87ceee1` (23/09) — merge da `main` e espelhamento dos casos novos
- `e7fd5f5` (24/09) — execução paralela com até 4 workers

A branch **não existe mais** no GitLab. Quem tiver clone antigo vê `origin/migracao-playwright` num ref congelado — é ilusão, resolve com `git fetch --prune`.

> [!tip] Feita com Claude Code
> Os commits trazem `Co-Authored-By: Claude`. O registro do processo está em `playwright/planning/` (15 documentos) — vale como leitura de contexto, não como regra viva.

> [!success] Ambiente validado na máquina do Rafael em 01/10/2026
> `npm run test:infra` → **50/50** (hoje são 55). `npm run test:seed` → **passou em 1.4 min**, instância `E2E Automatic Test` id **45 reutilizada** (a idempotência funciona — não recriou nada). Manifesto: 3 setores (GP, SCTA, DIR), 29 agentes, 5 cidadãos. `npm run test:list` → **398 testes em 131 arquivos**.
>
> O seed emite avisos de *"vínculos duplicados ignorados"* nos módulos PA e CO — resíduo de dados no homolog, não erro: ele escolhe o vínculo mais antigo e segue.

## Equivalências Cypress → Playwright

O `playwright/README.md` (seções 3 e 4) cobre fixtures, atores, paralelismo e regras de escrita, mas foi escrito do zero, sem pensar em quem vem do Cypress. O que segue é só a tradução de conceitos, o contexto de transição que o README não tem. Para o funcionamento, ver o README.

| No Cypress | No Playwright |
|---|---|
| Commands customizados (`cy.loginAgent`, `cy.apiRequest`) | Fixtures. Nenhum spec importa `test` de `@playwright/test`: todos importam de `src/fixtures/index.ts` (`env`, `seed`, `actors`, `cleanup`) |
| `cy.session` / login global cacheado | Sem `storageState` nem login global. Cada ator abre o próprio `BrowserContext` (`actors.agent()`, `actors.citizenApi()`, `actors.admin()`) |
| `cy.goToFresh` (contornava estado React/Apollo herdado) | Vários atores no mesmo teste = **vários contexts**; nunca logout/login na mesma página. Isso resolve de origem o problema que o `goToFresh` contornava |
| `cy.wait` | `waitForGraphQL(page, operationName, opts)` (arma a espera **antes** da ação), `clickWhenStable(locator)` (modal/gaveta MUI animando) e `clickUntilGraphQL(page, target, operationName)` (reclica só se nenhuma requisição saiu) |
| Commands de UI | Funções, não Page Objects: `src/ui/<domínio>.ts` reexporta `src/ui/internal/<domínio>.ts` embrulhado em `test.step` automático (por isso `test.step` explícito é raro nos specs) |
| Pausa entre testes (homolog compartilhado) | Fixture automática `pace` (3 s), herdada do Cypress |
| Dados de teste em `cypress.env.set.json` | Seed idempotente (`src/data/seed/`), roda sozinho antes de `api`, `e2e-chromium` e `version`. Preparo de massa dentro do teste é sempre por API; só a ação avaliada passa pela UI |

## O que a migração NÃO cobriu

> [!warning] Três lacunas abertas em 01/10/2026
> 1. **O CI continuava 100% Cypress** — `.gitlab-ci.yml` usava `image: cypress/included:16.0.0`. Nenhum pipeline rodava Playwright; a suíte Playwright não protegia merge nenhum — a inconsistência mais séria, e não se resolve do lado do vault.
>    **Atualização 15/10/2026 — agora é pior:** o `.gitlab-ci.yml` foi apagado junto com o Cypress (`0d6ba89`). Não existe **nenhum** pipeline no `main` — nem Cypress, nem Playwright. Nada roda automaticamente em merge.
> 2. **As skills e agentes `.claude/` do repo ensinavam Cypress** linha a linha (`cy.loginAgent`, `cy.apiRequest`, `cy.goToFresh`). Proposta de correção: [[2026-10-01-skills-automacao-playwright]].
>    **Atualização 15/10/2026:** a proposta **não foi implementada** (segue `status: proposta`, em `Sistema/Specs/`). O `0d6ba89` **apagou** os 4 arquivos (`.claude/skills/criar-teste-{api,e2e}/SKILL.md` e `.claude/agents/criar-teste-{api,e2e}.md`) **sem substituto**: o `main` não tem skill nem agente de criação de teste, só sobrou `.claudeignore`. As 4 skills do **vault** (`SKILL_*`) que a proposta cobre seguem descrevendo Cypress.
> 3. ~~**O TR 1.24-1.25 não existe no lado Playwright** — zero ocorrências de `CT-0` em `playwright/`.~~ **Corrigido em 02/10/2026** — essa conclusão estava errada: só buscou pelo rótulo literal `CT-0`, sem comparar o conteúdo. `tests/api/auth/login.spec.ts` e `credentials.spec.ts` **são** o porte de CT-001 a CT-012 (Suítes 1 e 2) — títulos idênticos aos do `03 - Casos de teste`, só com rótulo diferente (`A02-C01`...`A02-C09`, `A01-C01`...`A01-C03`). Confirmado verde num run real de 01/10/2026 (`playwright/test-results/results.xml`, 398 testes). Restam as Suítes 3, 4 e 5 (26 CTs) a portar. Ver [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/01 Automação/01 - Plano de automação|Plano de Automação]].


## Apêndice — de onde vinham as variáveis do `.env`

As variáveis `PW_*` derivavam do `cypress.env.json` do lado Cypress — arquivo que **não existe mais** no repo desde 15/10/2026. O `playwright/README.md` lista as variáveis, mas não de onde vinham os valores; este mapeamento só existe aqui. Não há outra fonte documentada para os valores atuais.

| Variável | Vem de (Cypress) |
|---|---|
| `PW_BASE_URL` | `GUI_BASE_URL` |
| `PW_GRAPHQL_URL` | `API_URL` |
| `PW_AUTH_URL` | `API_URL_AUTH` |
| `PW_ADMIN_USERNAME` / `PW_ADMIN_PASSWORD` | `ADMINISTRATOR_*` |
| `PW_AGENT_PASSWORD` / `PW_CITIZEN_PASSWORD` | fixas no produto: `Teste123!` |
| `PW_GMAIL_USER` / `PW_GMAIL_APP_PASSWORD` | `GMAIL_*` |
| `PW_SEED_NAMESPACE` | qualquer string — obrigatória, mas sem uso no código (vestígio de design) |
