---
tags:
  - qa
  - conhecimento
  - automacao
tipo: referencia
revisado: 2026-10-01
---
# Automação Playwright

> [!info] Por que esta nota existe
> A suíte Playwright entrou na `main` do `sogov-automation-test` em setembro/2026, escrita por **Waldemar Coimbra**, sem passar por nenhum registro do vault. Até 01/10/2026 **todo** documento de automação daqui — [[1.24-1.25 - Plano de Automação|Plano de Automação]], as skills, o [[FLUXOS]] — dizia "Cypress". Esta nota fecha esse buraco: é o que você lê antes de voltar a escrever teste.

## O estado em uma frase

O repositório tem **duas suítes convivendo**: o Cypress histórico na raiz e o Playwright em `playwright/`, pacote NPM independente. O Playwright é a suíte nova e maior; **o CI ainda roda só Cypress**.

| | Cypress (raiz) | Playwright (`playwright/`) |
|---|---|---|
| Specs | ~127 testes legados | **130 specs / 503 testes** |
| Entrada | `cypress.config.js` | `playwright/playwright.config.ts` |
| Roda no CI | ✅ sim (`.gitlab-ci.yml`) | ❌ **não** |
| Estado | mantido | ativo, recebendo casos novos |

## Como a migração entrou

Três commits de migração, mergeados na `main` pela MR da branch `migracao-playwright` (commit de merge `1d78bf9`):

- `a8bc9c5` (20/09) — `feat: add Playwright migration suite`, o commit-raiz
- `87ceee1` (23/09) — merge da `main` e espelhamento dos casos novos
- `e7fd5f5` (24/09) — execução paralela com até 4 workers

A branch **não existe mais** no GitLab. Quem tiver clone antigo vê `origin/migracao-playwright` num ref congelado — é ilusão, resolve com `git fetch --prune`.

> [!tip] Feita com Claude Code
> Os commits trazem `Co-Authored-By: Claude`. O registro do processo está em `playwright/planning/` (15 documentos) — vale como leitura de contexto, não como regra viva.

## Arquitetura — o que muda em relação ao Cypress

### Fixtures no lugar de commands

Nenhum spec importa `test` do `@playwright/test`. **Todos** importam de `src/fixtures/index.ts`, que entrega quatro coisas no `async ({ ... })`:

| Fixture | Escopo | O que é |
|---|---|---|
| `env` | worker | config validada (URLs, timeouts, `runId`) |
| `seed` | worker | manifesto da massa, já amarrado ao worker |
| `actors` | teste | sessões autenticadas (ver abaixo) |
| `cleanup` | teste | `ScenarioScope` para restaurações LIFO |

Mais dois automáticos: `diagnostics` (anexa log GraphQL em falha) e `pace` (3 s entre testes, herdado do Cypress, porque o homolog é compartilhado).

### Autenticação por ator — não existe `cy.loginAgent`

Sem `storageState`, sem login global. Cada ator abre o próprio `BrowserContext`:

```ts
const agent   = await actors.agent();      // servidor, com page
const citizen = await actors.citizenApi(); // cidadão, só API, sem browser
const admin   = await actors.admin();      // admin SOGOV
```

A sessão traz `page`, `request`, `api` (cliente GraphQL), `token`, `instanceId`. Fecha sozinha no teardown.

> [!warning] Regra que substitui o `cy.goToFresh`
> Vários atores no mesmo teste = **vários contexts**. Nunca fazer logout/login na mesma página. Isso resolve de origem o problema de estado React/Apollo herdado que o `goToFresh` contornava no Cypress.

Teste de API usa `actors.agentApi()`; teste E2E usa `actors.agent()` e pega o `page` dali.

### Massa de dados: seed idempotente

`src/data/seed/` reconcilia tudo por API antes da suíte rodar. É o projeto `seed`, do qual `api`, `e2e-chromium` e `version` dependem — roda sozinho, não precisa ser chamado.

O preparo de massa dentro do teste é **sempre por API**; só a ação avaliada passa pela UI:

```ts
await generateDocument(agent.api, makeDocument(documentContext(seed)));
```

### Paralelismo com posse declarada

Até 4 workers. Cada worker recebe um servidor/cidadão próprio do pool.

> [!important] Antes de escrever teste que altera cadastro
> Teste que muda setor, e-mail, nome ou mesa de um servidor precisa de um **servidor exclusivo**: declarar em `src/data/seed/baseline.ts`, registrar o dono em `src/data/seed/ownership.ts`, marcar o arquivo com `@shared-state` e rodar o seed. Nunca alterar servidor que outro arquivo lê.
>
> Asserção sobre listagem compartilhada (mesa, mural, contadores) **filtra pelo protocolo do próprio caso**.
>
> Isso é verificado automaticamente por `tests/infrastructure/parallel-safety.spec.ts` — violação reprova sem nem rodar o teste.

### Camada de UI: funções, não Page Objects

`src/ui/<domínio>.ts` reexporta `src/ui/internal/<domínio>.ts` embrulhado em `test.step` automático. Por isso `test.step` explícito é raro nos specs — o passo aparece no relatório sozinho.

Domínios disponíveis: `access-keys`, `common`, `contact-groups`, `deadlines`, `dispatch`, `document`, `imported-documents`, `labels`, `matters-services`, `models`, `mural`, `organizational`, `profile`, `public-agents`, `signature`, `tracking`, `workboard`, `workflow`.

Helpers de sincronização que substituem os `cy.wait` do Cypress:

- `waitForGraphQL(page, operationName, opts)` — arma a espera **antes** da ação
- `clickWhenStable(locator)` — para modal/gaveta MUI que entra animando
- `clickUntilGraphQL(page, target, operationName)` — reclica só se nenhuma requisição saiu

## Convenção de escrita

```ts
import { test, expect } from '../../../src/fixtures/index.js';  // sempre .js

// E26 — origem: cypress/testes/e2e/.../arquivo.e2e.cy.js (SGV-8173)
// Por que diverge da origem, se divergir.

test.describe('Downloads - Versão compactada', { tag: ['@e2e', '@downloads'] }, () => {
  test('E26-C01 [REGRESSÃO] O download produz um ZIP íntegro', { tag: '@smoke' }, async ({ actors, seed }) => {
    expect(valor, 'mensagem descritiva obrigatória').toBeGreaterThan(0);
  });
});
```

Regras que o lint cobra:

1. **ID no título**: `A<NN>` (API) ou `E<NN>` (E2E) + `-C<NN>`. É o que o relatório usa para agrupar.
2. **Classificação**: `[SUCESSO]` · `[FALHA]` · `[REGRESSÃO]`.
3. **Comentário de origem obrigatório** logo após os imports.
4. **Toda `expect` leva mensagem** no segundo argumento.
5. **Tags**: `['@api'|'@e2e', '@<domínio>']` no describe; `@smoke` no `test`, não no describe.
6. `@shared-state` no describe quando o arquivo muta estado compartilhado.
7. **Bug de produto**: `test.fail()` imediatamente antes da asserção do bug, nunca no topo.
8. **Skip** sempre com `annotation` tipada explicando o motivo.

Proibido pelo ESLint: `waitForTimeout`, `elementHandle`, asserção que não seja web-first, `expect` sem `await`.

## Como rodar

Sempre via `scripts/run.mjs` (gera o `PW_RUN_ID`), **nunca** `playwright test` direto.

```bash
cd playwright
npm ci && npx playwright install chromium
cp .env.example .env    # apontar para o homolog
npm run test:seed       # obrigatório antes da primeira rodada
npm run test:api
npm run test:e2e
npm run verify          # typecheck + lint + knip + independência + infra + audit
node scripts/run.mjs --project=api --grep "A12"   # um caso só
```

## O que a migração NÃO cobriu

> [!warning] Três lacunas abertas em 01/10/2026
> 1. **O CI continua 100% Cypress** — `.gitlab-ci.yml` usa `image: cypress/included:16.0.0`. Nenhum pipeline roda Playwright.
> 2. **As skills e agentes `.claude/` do repo ensinam Cypress** linha a linha (`cy.loginAgent`, `cy.apiRequest`, `cy.goToFresh`). Quem pedir "cria um teste" hoje é empurrado para o framework antigo.
> 3. **O TR 1.24-1.25 não existe no lado Playwright** — zero ocorrências de `CT-0` em `playwright/`. Há `tests/api/auth/{login,credentials}.spec.ts`, mas sem relação com a numeração CT-001…CT-038. Ver [[1.24-1.25 - Plano de Automação]].

## Antes de escrever o primeiro spec

Ler, nesta ordem:

1. `playwright/README.md` — paralelismo e posse de atores
2. `playwright/src/fixtures/index.ts` — o que está disponível no teste
3. `playwright/src/ui/internal/common.ts` — `clientPath`, `citizenPath`, `byTestId`, `waitForGraphQL`
4. `playwright/src/data/factories/documents.ts` — como montar massa
5. Um spec do mesmo domínio, como molde
6. `playwright/eslint.config.mjs` — o que o lint recusa
7. `playwright/planning/10-PARIDADE-P90.md` — qual ID ainda está livre

## Referências

- Repo: `~/Documentos/Sogov/sogov-automation-test` (branch de trabalho) · worktree de leitura em `~/Documentos/Sogov/sogov-automation-playwright`
- `playwright/planning/01-ARQUITETURA.md` — decisões de arquitetura
- `playwright/planning/10-PARIDADE-P90.md` — rastreabilidade Cypress → Playwright
- `PLAYWRIGHT_LESSONS.md` (raiz) — lições do porte
- [[Ambientes e Links de Trabalho]] · [[Docs do repositório Sogov]]
