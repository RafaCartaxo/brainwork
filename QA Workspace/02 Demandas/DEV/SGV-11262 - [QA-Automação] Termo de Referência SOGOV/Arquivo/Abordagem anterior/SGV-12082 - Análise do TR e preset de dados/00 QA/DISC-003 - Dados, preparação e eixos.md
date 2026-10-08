---
tags: [qa, automacao, dados, matriz]
task: SGV-12082
pai: SGV-11262
tipo: matriz-detalhe
parte_de: "[[Matriz - Análise do preset provável]]"
---

# DISC-003 — Dados, preparação e diferenças por eixo

> [!info]- Navegação
> **Índice/resumo:** [[Matriz - Análise do preset provável]] · **DISC-001 (arquitetura):** [[../01 Automação/01 - Plano de automação#DISC-001 — Auditoria do projeto, reconciliada com o código (07/10/2026)|Plano de automação]] · **DISC-002:** [[DISC-002 - Cobertura do TR e rastreabilidade dos CTs]] · **DISC-004:** [[DISC-004 - Alternativas e recomendação]] · **Fluxo do preset:** [[Fluxo - Preset de dados]]

> [!info] Nota de extração (08/10/2026)
> Conteúdo movido sem alteração técnica do antigo corpo da Matriz pra esta nota própria, pra reduzir o tamanho do índice. Nenhuma evidência ou achado foi reescrito — só reorganizado. A seção "Dois eixos..." abaixo é a decisão de planejamento que fundamenta toda a análise de dados/eixos que segue. Ver [[Matriz - Análise do preset provável]] pro propósito/legenda.

## Dois eixos que não podem virar um termo só

> [!important] Decisão de planejamento (Codex + Claude, 07/10/2026)
> **"Ambiente" é genérico demais e não entra mais sozinho nesta matriz.** Dois eixos diferentes, com evidência de naturezas diferentes:
> - **Ambiente de implantação** — dev/hml/prod: backend e URLs diferentes (`PW_BASE_URL`/`PW_GRAPHQL_URL`/`PW_AUTH_URL`). Hoje só há **um** configurado e usado de fato.
> - **Cliente/instância/tenant** — ex.: a instância do baseline do seed, ou a instância 225 criada em 07/10/2026. Mesmo backend, tenant diferente (`x-tenant`/`instanceId`).
>
> Reuso entre um e outro são afirmações **separadas**. Nesta rodada, registrar como **Confirmado** só o que foi observado rodando (há uma configuração de backend atual, usada pelos 13 CTs); capacidade de reproduzir em outro ambiente de implantação ou noutra instância/tenant fica **Inferida** até teste explícito — não executar nada pra "confirmar" isso agora.

## DISC-003 — Dados, preparação e diferenças por eixo (07/10/2026)

> [!info] Escopo e método
> Cruzei os 3 mecanismos do DISC-002 (Playwright atual, Cypress no branch `bdf5e9a`, sem código) contra seed/fixtures, configuração disponível, seleção de cliente/instância, credenciais, preparação/reset e dependência externa (Gmail). Lido: `playwright/config/env.ts`, `.env.example`; `cypress/support/e2e.js` (709 linhas, só os trechos de resolução de instância/setores/módulos); nomes de chave (não valores) de `cypress.env.json`, `cypress.env.set.json`, `cypress.env.set.dev.json`. **Nenhum segredo foi copiado** — só nomes de variável, por regra desta matriz. Nenhum teste rodado, nenhuma config alterada.

### Mapa do que é reutilizável hoje

| Dado/estado candidato | CTs que justificam | Preparação existente (Confirmado) | Reuso entre ambientes/instâncias | Evidência/pendência |
|---|---|---|---|---|
| Instância-alvo | Todos os 38 | **Os dois frameworks usam o mesmo nome fixo** `"E2E Automatic Test"` — Playwright via `BASELINE.instance.name` + `getInstanceOrCreate`; Cypress via `instanceName` hardcoded em `cypress/support/e2e.js:78` + mesma função. **Confirmado: mesmo nome nos dois códigos. Não confirmado: identidade real do alvo** — se os dois `.env`/`cypress.env*.json` apontam pro mesmo backend/registro, ou só coincidem no nome, não foi verificado (exigiria comparar valores de configuração, fora do escopo desta leitura) | **Nenhum dos dois frameworks tem parâmetro de `clienteId`/instância alternativa hoje** — achado chave, não presumido: procurei explicitamente por isso e não existe em nenhum dos dois | A confirmar: identidade real do alvo entre os dois configs; e o que aconteceria se os dois rodassem ao mesmo tempo contra o mesmo backend (concorrência entre frameworks, não só entre workers) |
| Setores/módulos/serviços/workflows | CT-020–036 (via setup) + resto do seed (fora do escopo do TR) | Ambos os frameworks usam `getXOrCreate` idempotente, por nome — Playwright em `src/api/services/*.ts`, Cypress nos commands equivalentes (`organizational.api.command.js`, etc., tocados no mesmo commit `bdf5e9a`) | Mesmo padrão nos dois frameworks (reconciliação por identidade natural, não por ID fixo) | — |
| Atores de servidor (CT-001-012/038, Suítes 3/4) | Playwright: pool por worker (CPF/senha de `env.agentPass`). Cypress: `createIsolatedTestAgent` por cenário (CPF/senha geradas ou fixas por código) | **Playwright não cria agente isolado por cenário** — só reusa o pool padrão do worker (não se aplica a bloqueio/status). **Cypress cria um agente dedicado por CT/cenário** (`createIsolatedTestAgent`) e, na Suíte 4, usa CPF **fixo** (reaproveitado entre rodadas) em vez de gerado | A confirmar — Playwright nunca implementou o equivalente de "agente isolado" porque os 13 CTs atuais não precisam | Se a Suíte 4 for portada, decidir se o padrão "CPF fixo reaproveitado" do Cypress é reaproveitado ou se vira sempre-novo (como o resto do Playwright prefere) |
| Estados de conta (bloqueio, licença, férias, inativo/suspenso) | CT-013-015,018-019 (bloqueio) e CT-020-036 (status) | **Confirmado, só no Cypress**: `cy.changePublicAgentWorkStatus` + `WORK_STATUS` enum (mutation real, capturada por request/response). **Não existe no Playwright** — `src/api/services/users.ts` não tem essa mutation portada | Mutation é a mesma API em ambos os casos (GraphQL do backend, não muda por framework) — só falta portar o client-side | Portar `changePublicAgentWorkStatus`/`WORK_STATUS` pro Playwright é a peça técnica que destrava qualquer preset pra Suíte 4 |
| Credenciais (senha por papel) | Todos | **Mesmo padrão nos dois**: senha única por papel via variável de ambiente — Playwright: `PW_AGENT_PASSWORD`/`PW_CITIZEN_PASSWORD`; Cypress: `AGENT_PASSWORD`/`CITIZEN_PASSWORD` (chave sem prefixo) | Mesmo padrão, nomenclatura de variável diferente | A confirmar se os valores são os mesmos entre os dois `.env` — não comparei valores (são segredo) |
| Dependência externa — Gmail (confirmação de cadastro/notificação) | CT-008 (signup), CT-026 (e-mail de fim de Licença), criação de cidadão/servidor em geral | **Mesmo padrão nos dois**: polling IMAP — Playwright: `PW_GMAIL_USER`/`PW_GMAIL_APP_PASSWORD`; Cypress: `GMAIL_USER`/`GMAIL_APP_PASSWORD` + `cy.task('waitForGmailMessage'/'deleteGmailMessage')` | Mesmo papel, implementação separada por framework | A confirmar se é a mesma caixa de e-mail nos dois `.env` (não comparei valores) |
| Preparação/reset — mecanismo de manifesto | — | **Mesmo padrão nos dois, implementações diferentes**: Playwright grava manifesto por execução em `.runtime/<runId>/seed-manifest.json` (schema versionado, `SEED_SCHEMA_VERSION=12`). Cypress regrava **um único arquivo fixo** `cypress.env.set.json` toda vez que `cypress/support/e2e.js` roda (`cy.writeFile`, limpa e reescreve) | Playwright isola por run (`runId`); Cypress sobrescreve sempre o mesmo arquivo — rodar Cypress e Playwright em paralelo contra o mesmo ambiente não tem proteção cruzada conhecida | A confirmar: nunca testado rodar os dois frameworks ao mesmo tempo |

### Diferenças e lacunas por eixo

> **Ambiente de implantação** (dev/hml/prod, backend/URLs) vs. **cliente/instância/tenant** (ex.: instância 225) — eixos sempre separados, por decisão já registrada no Plano.

- **Ambiente de implantação**: só **um** configurado de fato hoje (o que `PW_BASE_URL`/`PW_GRAPHQL_URL`/`PW_AUTH_URL` e o `cypress.env*.json` ativo apontam). Não há evidência, nesta análise, de execução confirmada contra um segundo ambiente de implantação. Playwright e Cypress usam **nomes de variável diferentes** pro mesmo papel (prefixo `PW_` vs. sem prefixo) — isso por si só não é um problema, mas significa que apontar os dois frameworks pro mesmo ambiente novo exige configurar duas vezes.
- **Cliente/instância/tenant**: ambos os frameworks resolvem **sempre pelo mesmo nome de instância fixo** — não existe hoje nenhum parâmetro (env var, CLI, config) que troque qual instância é usada. **A identidade real do alvo entre os dois configs não foi verificada** (não comparei valores). A instância 225 (criada em 07/10) não é selecionada por nenhum dos dois ainda.
- **Lacuna mais concreta pro preset**: a mutation de status (`changePublicAgentWorkStatus`) e o padrão de agente isolado por cenário existem **só no Cypress**. Enquanto não forem portados, qualquer preset de "estado de conta" pra Playwright teria que reimplementar essa mutation do zero (ela já está confirmada/testada, só não portada).

### Pressupostos para sanidade reproduzível

- Pressupõe que a instância-alvo **já existe e está provisionada** (nenhum dos dois frameworks testa criação de instância nova em execução normal — regra D4, documentada em `planning/13-REVISAO-E-ONDAS-DREAM.md`).
- Pressupõe que rodar **um** framework por vez contra um ambiente — não há evidência (nem teste) de comportamento com os dois simultâneos.
- Pressupõe que `enable_system_commands`/mutações de estado tocam uma instância compartilhada — qualquer preset de estado de conta precisa de isolamento por ator (como o Cypress já faz com agente isolado), não do agente global.

### Perguntas que ainda precisam de evidência

- Os valores reais de `.env` do Playwright e `cypress.env*.json` do Cypress apontam pro **mesmo** ambiente/instância hoje, ou são ambientes diferentes por coincidência de nome igual ("E2E Automatic Test" pode existir em mais de um backend)? Não comparei valores (são segredo) — só os nomes das chaves.
- O `changePublicAgentWorkStatus` realmente ainda funciona contra o ambiente atual (API pode ter mudado desde 01/10/2026, quando foi confirmado)? Não testado nesta rodada.
- Rodar Cypress e Playwright ao mesmo tempo contra a mesma instância já aconteceu alguma vez, e com que resultado? Sem evidência encontrada.
