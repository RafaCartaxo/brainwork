---
tags:
  - demanda
  - qa
  - funcionalidade
  - automacao
  - autenticacao
task: "11262"
status: em andamento
prioridade: media
data_inicio: 2026-08-31
responsavel: Rafael
modulo: autenticacao
---
# Demanda: Automação TR 1.24-1.25 — Autenticação e ciclo de vida do usuário

> [!info] Informações
> - **Tipo:** Automação (cobertura de testes) — criado retroativamente, o trabalho já estava em andamento quando o card foi aberto
> - **Status:** Em andamento — 25 de 38 CTs confirmados passando contra HML, 4 achados reais de produto, 6 sem causa raiz identificada, 3 sem código ainda
> - **Responsável QA:** Rafael
> - **Repo:** `sogov-automation-test` (GitLab `qa_sogov/sogov-automation-test`) — nada commitado ainda
> - **Ambiente:** Homologação (`dev.sogov.net`)
> - **Vault:** [[QA Workspace/07 Termo de Referência/1.24-1.25/03 Automação/1.24-1.25 - Handoff de execução|Handoff de execução]] (estado detalhado, atualizado a cada rodada) · [[QA Workspace/07 Termo de Referência/1.24-1.25/03 Automação/1.24-1.25 - Plano de Automação|Plano de Automação]] (arquitetura) · [[QA Workspace/07 Termo de Referência/1.24-1.25/01 Casos de Teste/1.24-1.25 - Casos de Teste|Casos de Teste]] (fonte dos 38 CTs)
> - **Skill do processo:** [[Sistema/Skills/SKILL_AUTOMACAO_TERMO_REFERENCIA|SKILL_AUTOMACAO_TERMO_REFERENCIA]]

---

> [!abstract] Resumo

Os itens **1.24** (tipos de acesso — servidor, cidadão PF, cidadão PJ) e **1.25** (validação de credenciais, bloqueio por tentativas, ciclo de vida da identidade — Ativo/Licença/Férias/Inativo/Suspenso) do Termo de Referência viraram 38 casos de teste, organizados em 5 suítes. Esta demanda cobre a automação desses 38 CTs no repositório Cypress `sogov-automation-test` — investigação técnica da API real (sem documentação/introspection disponível), escrita dos testes, validação contra HML, e triagem de cada resultado.

Não é uma correção de bug nem uma feature de produto — é cobertura de regressão automatizada pra um Termo já implementado.

---

## Suítes e status atual

| Suíte | CTs | Status |
|---|---|---|
| 1. Tipos de acesso | CT-001 a 009 (9) | ✅ Todos confirmados |
| 2. Validação de credenciais | CT-010 a 012 (3) | ✅ Todos confirmados |
| 3. Bloqueio por tentativas | CT-013, 014, 018, 019 (4) | ✅ Confirmados |
| 3. Bloqueio por tentativas | CT-015 | ⚠️ Em disputa — ver Achados |
| 3. Bloqueio por tentativas | CT-016, 017 | ❌ Sem código (falta captura de API) |
| 4. Ciclo de vida da identidade | CT-020, 021, 023, 024, 025, 027, 031, 032 (8) | ✅ Confirmados |
| 4. Ciclo de vida da identidade | CT-029, 030, 033 (3) | ⚠️ Achados reais — ver Achados |
| 4. Ciclo de vida da identidade | CT-022, 026, 028, 034, 035, 036 (6) | ❓ Falha sem causa raiz identificada |
| 5. Transversais e auditoria | CT-038 | ✅ Confirmado |
| 5. Transversais e auditoria | CT-037 | ❌ Sem código (falta captura de API) |

**25 de 38 CTs 100% prontos e verdes contra HML.**

---

## Achados reais de produto (não são bugs da automação)

- **CT-015** — depois de bloquear uma conta por 5 tentativas erradas (confirmado via log: a 5ª já retorna `"account-blocked"`), uma tentativa imediatamente seguinte com a senha correta autentica normalmente. **Em disputa**: o responsável testou manualmente (tela e API direto) e o bloqueio funcionou. Hipótese de condição de corrida/timing levantada, ainda não confirmada — 3 tentativas de experimento controlado falharam por instabilidade do ambiente (zero dado gerado ainda).
- **CT-029 / CT-030** — em Férias, escrita e leitura não ficam bloqueadas, diferente de Licença (CT-023/CT-024), que bloqueia corretamente. Inconsistência real entre os dois estados de quarentena — vale confirmar se é intencional.
- **CT-033** — uma sessão obtida antes da mudança de status para Inativo continua acessando o próprio perfil normalmente depois da mudança — sessão antiga não é revogada/checada.

---

## Correções feitas no código do repositório (impactam código já existente, não só testes novos)

- **Vazamento de cookie de sessão entre testes**: `cy.apiRequest`/`cy.request` sempre envia o cookie jar atual, independente do body da requisição — uma tentativa de login que deveria falhar podia "passar" por causa de um login bem-sucedido anterior no mesmo spec. Corrigido com `cy.clearCookies()` embutido nos commands de login "cru".
- **Bug pré-existente em `finishAgentRegistry`** (`user.api.commands.js`) — faltava um `return` na chamada da API, nunca detectado porque nenhum teste anterior exercitava o caminho de "criar agente do zero" repetidamente.
- Fix de nome de agente de teste isolado (limite de tamanho de campo no backend).

---

## Pendências (ordem de prioridade combinada)

1. **CT-015** — repetir o experimento de timing (script pronto) assim que o ambiente HML estabilizar.
2. **6 CTs da Suíte 4 sem causa raiz** (CT-022/026/028/034/035/036) — mesma janela de investigação do item 1.
3. **CT-029/030/033** — confirmação rápida com produto/backend se a divergência Licença × Férias é intencional.
4. **CT-016/017/037** — aguardam captura de API nova (desbloqueio manual e endpoint de auditoria), depende do responsável capturar via DevTools/HAR.
5. **Subida do código**: sessão de revisão conjunta (diff suíte por suíte) antes de qualquer commit/MR — nada sobe até resolver pelo menos os itens 1-3.

---

## Histórico

- 2026-08-31 - Iniciada a automação das Suítes 1, 2 e 3 (18 CTs) — sem card vinculado ainda
- 2026-08-31 - Captura de API da troca de status localizada (Downloads do responsável) — desbloqueou e permitiu codar a Suíte 4 inteira (17 CTs)
- 2026-08-31 - Suíte 4 validada contra HML: 8/17 confirmados, 3 achados reais, 6 sem causa raiz
- 2026-09-01 - CT-015 questionado pelo responsável (validação manual diverge do achado automatizado) — investigação de timing tentada, inconclusiva por instabilidade do ambiente
- 2026-09-02 - Card **SGV-11262** criado (retroativo), plano de subida definido, skill [[Sistema/Skills/SKILL_AUTOMACAO_TERMO_REFERENCIA|SKILL_AUTOMACAO_TERMO_REFERENCIA]] registrada no vault
