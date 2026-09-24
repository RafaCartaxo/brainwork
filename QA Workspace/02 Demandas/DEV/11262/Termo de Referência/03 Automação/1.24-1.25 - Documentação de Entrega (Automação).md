---
tags:
  - qa
  - automacao
  - entrega
tipo: referencia
revisado: 2026-09-02
---
# 1.24-1.25 — Documentação de Entrega (Automação)

> [!info] Sobre esta nota
> Documento de **revisão** pro Rafael conferir o grupo de testes de automação do TR 1.24-1.25 (Cypress, repo `sogov-automation-test`). Cobre os 36 CTs com código (de 38 no escopo): o que cada cenário faz, quais asserts ele executa, e o status atual. É complementar ao [[1.24-1.25 - Handoff de execução|Handoff de execução]] (que é a camada de estado/orquestração pra IA continuar o trabalho) — aqui o foco é só "o que o código faz", pra revisão humana.

## Como a suíte é construída

- **Agentes isolados por CPF gerado na hora** — `cy.createIsolatedTestAgent(token, instanceId, sectorId, namePrefix, scenarioTag)` (comando único, `user.api.commands.js`). Usado sempre que um cenário bloqueia a conta ou muda seu `workStatus` — nunca no `AGENT_CPF` global, que é reusado por 127 testes já existentes via `cy.session`. Nome amarrado ao CPF (`"Lockout {cpf}"` / `"Lifecycle {cpf}"`) pra evitar reaproveitar um agente antigo pelo nome com um CPF novo nunca registrado.
- **`cy.session` pros atores globais** (`loginAgent`/`loginCitizen`/`loginAdministrator`) — cacheia sessão entre specs (`cacheAcrossSpecs: true`), reduz tempo de execução.
- **`loginAgentExpectFailure`/`loginCitizenExpectFailure`** — primitiva de login CRU, **sem** `cy.session`. Usada sempre que o teste precisa: esperar falha (bloqueio, credencial errada); repetir login pro mesmo usuário mais de uma vez no mesmo teste (senão o cache mascararia o comportamento real sendo testado); ou obter 2 tokens independentes pro mesmo usuário (CT-038). Sempre inclui `cy.clearCookies()` no início — fix de um vazamento real de cookie entre testes (ver "Achados" no Handoff de execução).
- **`changePublicAgentWorkStatus`** — mutation e enum (`IN_ACTIVITY`/`LICENSE`/`VACATION`/`SUSPEND`) descobertos via captura de HAR real, não por introspection (desabilitada em HML). "Inativo" e "Suspenso" mapeiam pro mesmo enum `SUSPEND`.
- **GraphQL cru via `cy.apiRequest`** — todo command API monta manualmente `{operationName, variables, query}` e chama `cy.apiRequest('POST', urlApi, body, header)`.
- **Factories** (`user.factory.js`) — `makePublicAgent`, `makeFinishAgentRegistry`, `makeEditPublicAgentInput`, `makeChangeWorkStatusInput`, todas com padrão de `overrides`.

**Legenda de status:** ✅ confirmado passando · ⚠️ achado real de produto (não é bug do teste) · ❓ falha sem causa raiz identificada · ❌ sem código ainda / falhando por motivo não relacionado ao teste em si.

---

## Suíte 1 — Tipos de acesso (`login.api.cy.js`) — ✅ 9/9

Reaproveita os atores globais do setup (`AGENT_CPF`, `CITIZEN_CNPJ`) — nenhum destes casos bloqueia ou muda status de conta.

| CT | O que faz | Asserts | Status |
|---|---|---|---|
| **CT-001** | `loginAgent` com CPF+senha corretos do servidor global. | Token presente (`resp.body.id` existe). | ✅ |
| **CT-002** | `loginCitizen` usando o CPF do servidor global como identificador de cidadão PF (suposição documentada: não existe cidadão PF puro no setup — criar um dinamicamente falhava na confirmação de cadastro). | Token presente. | ✅ |
| **CT-003** | `loginCitizen` com CNPJ (RAW, sem pontuação — descoberta: diferente do CPF, o CNPJ só é aceito sem formatação) + senha da empresa. | Token presente. | ✅ |
| **CT-004** | `loginAgentExpectFailure` com CNPJ+senha **reais de uma empresa cidadã**, contra o login de **servidor** — testa segregação de contexto, não só formato inválido. | Status não é 200/201. | ✅ |
| **CT-005** | `loginCitizen` com CPF do servidor global (redundante de propósito com CT-002, documentado no Qase). | Token presente — reafirma que CPF nunca cai em contexto Empresa. | ✅ |
| **CT-006** | `loginAgentExpectFailure` com CPF de dígito verificador inválido. | Status não é 200/201. | ✅ |
| **CT-007** | `loginCitizenExpectFailure` com CNPJ de dígito verificador inválido. | Status não é 200/201. | ✅ |
| **CT-008** | `createAutoRegistrationForCitizen` tentando recriar cadastro da empresa já existente (mesmo CNPJ). | Status não é 200/201 (recusado). | ✅ |
| **CT-009** | `loginCitizen` do servidor com o próprio CPF (mesmo mecanismo do CT-002) — confirmado com Rafael em 31/08 que é coexistência esperada, não gap. | Token presente. | ✅ |

## Suíte 2 — Validação de credenciais (`credentials.api.cy.js`) — ✅ 3/3

| CT | O que faz | Asserts | Status |
|---|---|---|---|
| **CT-010** | `loginAgentExpectFailure` com CPF correto + senha errada. | Status não é 200/201. | ✅ |
| **CT-011** | `loginAgentExpectFailure` com CPF gerado na hora (nunca registrado). | Status não é 200/201. | ✅ |
| **CT-012** | `loginAgentExpectFailure` com todos os campos em branco. | Status não é 200/201. Nota: Plano de Automação classifica isso como comportamento primariamente de UI — codado como API por ora, sem E2E dedicado. | ✅ |

## Suíte 3 — Bloqueio por tentativas (`lockout.api.cy.js`) — 4/5

Setup cria 5 agentes isolados (`cy.createIsolatedTestAgent(..., "Lockout", tag)`). CT-016 (desbloqueio por e-mail) e CT-017 (desbloqueio manual) não estão aqui — sem código ainda.

| CT | O que faz | Asserts | Status |
|---|---|---|---|
| **CT-013** | 4 tentativas erradas seguidas + uma 5ª, no `agentBlocked`. | Status não 200/201 na 5ª **E** a mensagem de erro é exatamente `system.messages.account-blocked` (sinal explícito de bloqueio, não só "senha errada" genérica — confirma que o contador realmente chegou a 5). | ✅ |
| **CT-014** | 4 tentativas erradas no `agentFourAttempts`, depois 1 com senha **correta**. | Login com senha correta funciona (200/201) — confirma que 4 erradas não bloqueiam. | ✅ |
| **CT-015** ⚠️ | Reaproveita o `agentBlocked` (já bloqueado no CT-013), tenta login **imediatamente depois com a senha correta**. | Esperado: continuar recusando. **Real: autentica normalmente (200)** — acredita-se ser achado de produto, mas Rafael testou manualmente (tela + API) e o bloqueio funcionou. Hipótese de timing/condição de corrida ainda não confirmada — experimento controlado tentado 3x, sem sucesso por instabilidade de ambiente. | ⚠️ **em disputa** |
| **CT-018** | 3 erradas → 1 correta (deve passar, só 3 não bloqueiam) → 3 erradas de novo → 1 correta de novo (deve passar, contador reiniciou após o sucesso). | Ambas tentativas corretas retornam 200/201. | ✅ |
| **CT-019** | `agentUserA` leva 5 tentativas erradas (bloqueia); `agentUserB` tenta login normal em paralelo. | Mensagem de A é `account-blocked`; B autentica normalmente (200/201) — bloqueio de um não afeta o outro. | ✅ |

## Suíte 4 — Ciclo de vida da identidade (`identity-lifecycle.api.cy.js`) — 8/17

Setup cria 5 agentes isolados (`cy.createIsolatedTestAgent(..., "Lifecycle", tag)`), muda `workStatus` via `changePublicAgentWorkStatus`. Ordem dos testes segue dependência de estado do agente, não a ordem numérica dos CTs.

| CT | O que faz | Asserts | Status |
|---|---|---|---|
| **CT-020** | Define status Ativo, login, `userInstanceInfo` com o próprio token. | Login 200/201; leitura do próprio perfil funciona. | ✅ |
| **CT-033** ⚠️ | Login **antes** da mudança (token "antigo"), muda status pra Inativo, tenta ler o perfil com o token antigo. | Esperado: acesso negado com token antigo. **Real: acesso continua funcionando** — sessão antiga não é revogada/checada. | ⚠️ **achado real** |
| **CT-032** | Login com credenciais corretas no agente já Inativo (desde CT-033). | Status não é 200/201. | ✅ |
| **CT-034** ❓ | Reverte status pra Ativo, espera 3s, tenta login. | Esperado: login volta a funcionar (200/201). **Real: continua recusando (400)** mesmo após a espera — causa raiz não diagnosticada. | ❓ |
| **CT-035** ❓ | Muda `agentSuspenso` pro enum `SUSPEND` (mesmo enum de Inativo — não há valor técnico separado pra "Suspenso"), espera 3s, login. | Esperado: negado, igual Inativo. **Real: autentica (200)** — mesma causa raiz não diagnosticada do grupo abaixo. | ❓ |
| **CT-025** | Login antes da mudança (token "antigo"), muda status pra Licença, tenta **editar** o próprio perfil com o token antigo. | Edição não deve funcionar com o token antigo — bloqueada. | ✅ |
| **CT-021** | Login no `agentLicenca` (já em Licença desde CT-025). | Login funciona (200/201) — diferente de Inativo. | ✅ |
| **CT-022** ❓ | Busca o agente via `getPublicAgents` por nome (`Lifecycle {cpf}`). | Esperado: item encontrado com `workStatus === LICENSE`. **Real: item vem `undefined`** — busca por nome não encontra o agente isolado recém-criado. | ❓ |
| **CT-023** | Login, tenta editar o próprio perfil. | Edição bloqueada. | ✅ |
| **CT-024** | Login, tenta ler o próprio perfil (`userInstanceInfo`). | Leitura bloqueada. | ✅ |
| **CT-026** ❓ | Define `statusEnd` no passado (Licença já expirada), espera e-mail de aviso de mudança de status (Termo 1.27.11.4), login, busca por nome. | E-mail chega (✅ confirmado); login funciona (✅); `workStatus` deveria voltar sozinho pra Ativo. **Real: falha na 3ª parte** — mesma causa raiz do CT-022. | ❓ |
| **CT-027** | Define status Férias, login. | Login funciona (200/201) — diferente de Inativo. | ✅ |
| **CT-028** ❓ | Busca por nome (`Lifecycle {cpf}`). | Esperado: `workStatus === VACATION`. **Real: item `undefined`** — mesma causa raiz do grupo. | ❓ |
| **CT-029** ⚠️ | Login, tenta editar o próprio perfil. | Esperado: edição bloqueada em Férias. **Real: edição funciona** — achado real (Férias não bloqueia escrita, diferente de Licença/CT-023). | ⚠️ **achado real** |
| **CT-030** ⚠️ | Login, tenta ler o próprio perfil. | Esperado: leitura bloqueada em Férias. **Real: leitura funciona** — mesmo padrão do CT-029. | ⚠️ **achado real** |
| **CT-031** | Define `statusEnd` no passado (Férias expirada), login, busca por nome. | Login funciona **e** `workStatus` volta pra Ativo sozinho. | ✅ (nota: mesma forma de checagem do CT-026, mas aqui passa — pista útil pra investigar a causa raiz do grupo ❓) |
| **CT-036** ❓ | `agentTransitions` passa por Licença → Inativo → Ativo, checando `workStatus` via busca por nome a cada etapa; testa login negado no meio (Inativo) e permitido no fim (Ativo). | `workStatus` esperado em cada etapa + login negado/permitido nos pontos certos. **Real: falha já na 1ª checagem** — mesma causa raiz do grupo. | ❓ |

## Suíte 5 — Transversais e auditoria (`audit-sessions.api.cy.js`) — ✅ 1/1

CT-037 (log de auditoria) não está aqui — sem código ainda.

| CT | O que faz | Asserts | Status |
|---|---|---|---|
| **CT-038** | 2 logins crus (`loginAgentExpectFailure` como primitiva sem cache) pro **mesmo** `AGENT_CPF` — gera 2 tokens independentes pro mesmo usuário. | Ambos logins retornam 200/201; depois, **ambos** os tokens continuam válidos (`getPublicAgents` com cada um retorna 200/201) — nenhuma sessão derruba a outra. | ✅ |

## E2E smoke — `login.e2e.cy.js` — ❌ 0/1

A regra de negócio (aceitar/rejeitar CPF/CNPJ, contexto) já está coberta via API acima — este spec cobre só o que é exclusivo da tela real (rota, campo único, botão).

| CT | O que faz | Asserts | Status |
|---|---|---|---|
| **CT-002/CT-003 (smoke UI)** | `cy.goTo('/login/cidadao/{instanceId}')`, `cy.loginCitizenUI(formatCNPJ(citizenCnpj), citizenPassword)` — preenche campo único (CPF/CNPJ) + senha, clica Entrar. | `cy.location('pathname')` não deve mais incluir `/login/cidadao` (sinal indireto de sucesso — não há `data-testid` confirmado da tela pós-login). **Real: timeout de 15s, continua em `/login/cidadao/45`** — não investigado a fundo contra homolog ainda (erro diferente do observado contra dev, que era um `SyntaxError` de asset). | ❌ |

## Sem código ainda (fora das tabelas acima)

- **CT-016** — desbloqueio de conta por link de e-mail.
- **CT-017** — desbloqueio manual por outro servidor.
- **CT-037** — log de auditoria de tentativas de login.

Os três dependem de uma captura de API (HAR) dedicada, que ainda não foi feita — a captura já obtida só cobre a mudança de `workStatus`.

## Pendências e achados — fonte única

A lista de achados reais, prioridades e o que entra no próximo MR já estão documentados em [[1.24-1.25 - Handoff de execução|Handoff de execução]] (seção "Achados reais" e atualização de 02/09) — não duplicado aqui.
