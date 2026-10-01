---
tags:
  - qa
  - spec
  - automacao
tipo: referencia
revisado: 2026-10-01
status: proposta
---
# Proposta — adequar as skills de automação ao Playwright

> [!info] Isto é proposta, não edição
> [[REGRAS_IA#Doc de processo: propor antes de aplicar]] manda que mudança em Skill vá como plano primeiro, porque são os arquivos que outras sessões vão obedecer. **Nenhuma skill foi alterada.** Este documento descreve o que precisa mudar e pede a decisão.

## O problema

O repo migrou para Playwright em setembro ([[Automação Playwright]]). As 4 skills de automação do vault descrevem Cypress — não só no nome da ferramenta, mas na **mecânica**: `cy.session`, `cy.request`, `cypress.env.json`, caminhos `cypress/testes/...`, `Cypress.Commands.add`.

Uma sessão que siga essas skills hoje escreve teste no framework que não recebe mais casos novos.

| Skill | Linhas | Citações de Cypress | Gravidade |
|---|---|---|---|
| [[SKILL_INICIAR_AUTOMACAO]] | 54 | 4 | 🟡 média — gates continuam válidos, só a mecânica muda |
| [[SKILL_AUTOMACAO_TERMO_REFERENCIA]] | 80 | 3 | 🟢 baixa — é sobre processo, quase independe de ferramenta |
| [[SKILL_REVISAO_CODIGO_AUTOMACAO]] | 141 | 15 | 🔴 alta — crivo inteiro montado sobre commands |
| [[SKILL_REVISAO_AUTOMACAO_E2E]] | 91 | 13 | 🔴 alta — caminhos e seletores de arquivo são Cypress |

## A decisão que não é minha

Antes de mexer em qualquer skill, uma pergunta de fundo precisa de resposta:

> **O Cypress continua recebendo teste novo, ou virou legado?**

Hoje o repo é híbrido de verdade: o Cypress está inteiro, **o CI roda só Cypress**, e o Playwright, apesar de maior (130 specs / 503 testes), não tem pipeline. Isso não é estado de migração concluída — é convivência.

| Se a resposta for | Então as skills |
|---|---|
| **Playwright é o padrão, Cypress é legado** | São **reescritas**. Mais simples, menos manutenção. |
| **Os dois convivem** | Ganham **seção por framework**, ou viram duas famílias (`..._PW`). Mais trabalho, mas honesto com a realidade. |
| **Ainda não se sabe** | Mexer só no mínimo: um aviso no topo de cada uma apontando para [[Automação Playwright]], e nada mais. |

Essa pergunta provavelmente é do time, não só do Rafael — quem mantém o CI decide junto.

## O que muda em cada skill

### SKILL_INICIAR_AUTOMACAO 🟡

O que **continua valendo** (é o coração da skill): os dois gates — card validado manualmente com CTs executados, e fix presente no ambiente que a suíte ataca.

O que muda:

| Hoje | Vira |
|---|---|
| `cypress.env.json` define o ambiente | `playwright/.env` (`PW_BASE_URL`, `PW_GRAPHQL_URL`) |
| `npm run open` / `npm run chrome` | `npm run test:e2e` / `test:api` — sempre via `scripts/run.mjs` |
| dados de teste em `cypress.env.set.json` | seed idempotente, `npm run test:seed` |
| "guia de como escrever mora em `.claude/agents/criar-teste-e2e.md`" | ⚠️ **esse agente ainda ensina Cypress** — enquanto não for atualizado, apontar para `playwright/README.md` |

### SKILL_AUTOMACAO_TERMO_REFERENCIA 🟢

Quase toda sobre processo (fases, triagem de falha em 3 categorias, critério de parada por instabilidade) — **sobrevive inteira**. Três ajustes pontuais:

- "agentes isolados por cenário, nunca o global cacheado via `cy.session`" → o equivalente em Playwright é mais forte e já é obrigatório: pool por worker + posse exclusiva declarada em `ownership.ts`.
- "cookie vazando entre testes (`cy.request` manda o cookie jar atual)" → **não existe mais**: cada ator tem `BrowserContext` próprio. Vira nota histórica.
- "processos órfãos de Cypress/Chrome" → vale igual para Playwright, só trocar o `grep`.

### SKILL_REVISAO_CODIGO_AUTOMACAO 🔴

O crivo é bom, mas está montado sobre uma arquitetura que mudou. Equivalências:

| Crivo atual (Cypress) | Equivalente em Playwright |
|---|---|
| duplicação de command entre specs | duplicação de helper em `src/ui/` ou `src/api/services/` |
| `grep "Cypress.Commands.add('<nome>'"` antes de criar | `grep` em `src/ui/internal/` e `src/api/services/` |
| `ls cypress/testes/{api,e2e}/entities/<dominio>/*.cy.js` | `ls playwright/tests/{api,e2e}/<dominio>/*.spec.ts` |
| CPF fixo × gerado | continua idêntico — mas agora o baseline do seed é a fonte |
| convenção de comentário (nunca citar pessoa, nunca narrar debug) | **continua idêntica** — e ganha item novo: comentário `// <ID> — origem:` é obrigatório |

**Itens novos**, que o crivo atual não tem como cobrir porque não existiam:

- [ ] `@shared-state` presente quando o arquivo muta cadastro compartilhado?
- [ ] ator exclusivo registrado em `ownership.ts`?
- [ ] toda `expect` com mensagem descritiva no segundo argumento?
- [ ] ID `A<NN>`/`E<NN>-C<NN>` no título e ainda livre em `10-PARIDADE-P90.md`?
- [ ] `test.fail()` imediatamente antes da asserção do bug, nunca no topo?
- [ ] `npm run verify` passa?

> Boa parte disso o ESLint já cobra sozinho (`no-wait-for-timeout`, `no-element-handle`, `prefer-web-first-assertions`, `missing-playwright-await`). A skill pode **encolher** delegando ao lint e focando no que é julgamento humano.

### SKILL_REVISAO_AUTOMACAO_E2E 🔴

Caminhos e gotchas são todos de Cypress. O que **sobrevive intacto** é o conhecimento de domínio da tela SOGOV — e isso é o mais valioso:

- toast `[data-testid="flashMessage-snackbar"]` — mesmo seletor, há helper pronto (`expectSnackbar`)
- gotchas de MUI (classes `css-*`, menu que renderiza item vazio por um frame) — continuam reais; o Playwright tem `clickWhenStable` para isso
- rota por persona (`/cliente/` servidor × `/cidadao/` cidadão) — **a regra mais violada**, continua valendo, agora via `clientPath()` / `citizenPath()`

## Ordem sugerida

1. **Responder a pergunta de fundo** (Cypress legado ou convivência?) — trava as outras.
2. Enquanto não houver resposta: aviso no topo das 4 skills apontando para [[Automação Playwright]]. Custo baixo, evita que uma sessão escreva Cypress por engano.
3. `SKILL_REVISAO_CODIGO_AUTOMACAO` primeiro entre as reescritas — é a de maior gravidade e a que mais encolhe ao delegar para o ESLint.
4. `SKILL_REVISAO_AUTOMACAO_E2E` depois, preservando o conhecimento de tela.
5. As duas 🟡🟢 por último — mudança pequena.

## Fora deste documento

As skills e agentes **do repositório** (`.claude/skills/criar-teste-{api,e2e}/`, `.claude/agents/criar-teste-{api,e2e}.md`) têm o mesmo problema, em grau pior: ensinam `cy.loginAgent`, `cy.apiRequest`, `cy.goToFresh` em detalhe. São arquivos do repo, não do vault — mudá-los é trabalho no `sogov-automation-test` e precisa de decisão separada.

## Referências

- [[Automação Playwright]] — arquitetura e convenção nova
- [[REGRAS_IA]] — a regra que torna isto proposta e não edição
- `playwright/README.md` · `playwright/planning/01-ARQUITETURA.md` · `playwright/eslint.config.mjs`
