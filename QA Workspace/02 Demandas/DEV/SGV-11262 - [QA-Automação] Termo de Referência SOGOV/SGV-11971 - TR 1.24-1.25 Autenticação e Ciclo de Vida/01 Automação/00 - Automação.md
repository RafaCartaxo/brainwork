---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
validacao_origem: "[[../00 QA/04 - Validação dev]]"
repo: "sogov-automation-test"
framework: "cypress — a portar pra playwright"
status: executado
pontos: ""
---

# Automação — SGV-11971 (TR 1.24-1.25)

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Plano de teste:** [[../00 QA/02 - Plano de teste]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Validação:** [[../00 QA/04 - Validação dev]]
> **Preparação Qase:** [[../00 QA/05 - Preparação Qase]]
> **Automação:** [[00 - Automação]]

> [!warning] Escrito pra Cypress — o alvo mudou pra Playwright em 01/10/2026
> O repo `sogov-automation-test` migrou pra Playwright em setembro/2026 (merge `1d78bf9`) enquanto esta automação estava parada. O código terá de ser portado. Estado atual e convenção nova em [[QA Workspace/04 Conhecimento/Referências/Automação Playwright|Automação Playwright]].

> Esta nota registra o **estado da cobertura automatizada** dos 38 CTs de [[../00 QA/03 - Casos de teste|03 - Casos de teste]] (+ 3 extras fora de escopo) — não duplica o cenário (fica em `03`) nem o resultado da validação manual (fica em `04`). O campo `Automação` de cada CT em `03` é a fonte de verdade de *o que* está automatizado; aqui fica o *como* e o *estado atual*.

> [!info]- Documentos detalhados desta automação
> - [[01 - Plano de automação|01 - Plano de automação]] — arquitetura, convenção de pastas/specs, faseamento.
> - [[02 - Handoff de execução|02 - Handoff de execução]] — estado/orquestração entre rodadas, log cronológico.
> - [[03 - Documentação de entrega|03 - Documentação de entrega]] — revisão cenário a cenário do que cada CT de código faz.

---

## Configuração

- **Repo:** `sogov-automation-test`
- **Branch/MR:** Suítes 1/2 mergeadas no `origin/main` (commit `6c9188c`, 09/09/2026). Suítes 3/4/5 commitadas só localmente (`bdf5e9a`, branch `tr-1.24-1.25-suites-3-4-5`, 01/10/2026) — não sobem em Cypress, serão portadas.
- **Framework:** Cypress — alvo migrou pra Playwright (01/10/2026); código a portar.
- **Ambiente de validação:** HML

---

## Cobertura por CT

| CT | Status | Observação |
|---|---|---|
| [[../00 QA/03 - Casos de teste#^ct-001\|CT-001]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-002\|CT-002]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-003\|CT-003]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-004\|CT-004]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-005\|CT-005]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-006\|CT-006]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-007\|CT-007]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-008\|CT-008]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-009\|CT-009]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/login.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-010\|CT-010]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/credentials.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-011\|CT-011]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/credentials.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-012\|CT-012]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (run de 01/10/2026, `api/auth/credentials.spec.ts`). |
| [[../00 QA/03 - Casos de teste#^ct-013\|CT-013]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-014\|CT-014]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-015\|CT-015]] | ⚠️ | Achado real em disputa: via automação, após o bloqueio na 5ª tentativa (log retorna `account-blocked`), a tentativa seguinte com a senha correta autentica. Validação manual do Rafael (tela e API) não reproduziu. Hipótese de corrida/timing não confirmada — 3 experimentos falharam por instabilidade do ambiente. |
| [[../00 QA/03 - Casos de teste#^ct-016\|CT-016]] | ❌ | Sem código — aguarda captura de API do desbloqueio por link de e-mail. |
| [[../00 QA/03 - Casos de teste#^ct-017\|CT-017]] | ❌ | Sem código — aguarda captura de API do desbloqueio manual por servidor. |
| [[../00 QA/03 - Casos de teste#^ct-018\|CT-018]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-019\|CT-019]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-020\|CT-020]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-021\|CT-021]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-022\|CT-022]] | ❓ | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |
| [[../00 QA/03 - Casos de teste#^ct-023\|CT-023]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-024\|CT-024]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-025\|CT-025]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-026\|CT-026]] | ❓ | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |
| [[../00 QA/03 - Casos de teste#^ct-027\|CT-027]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-028\|CT-028]] | ❓ | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |
| [[../00 QA/03 - Casos de teste#^ct-029\|CT-029]] | ⚠️ | Achado real: em Férias a escrita não é bloqueada, diferente de Licença (CT-023), que bloqueia corretamente. Divergência entre os dois estados de quarentena — confirmar com produto se é intencional. |
| [[../00 QA/03 - Casos de teste#^ct-030\|CT-030]] | ⚠️ | Achado real: em Férias a leitura não é bloqueada, diferente de Licença (CT-024). Mesma divergência do CT-029. |
| [[../00 QA/03 - Casos de teste#^ct-031\|CT-031]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-032\|CT-032]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). |
| [[../00 QA/03 - Casos de teste#^ct-033\|CT-033]] | ⚠️ | Achado real: sessão obtida antes da mudança para Inativo segue acessando o próprio perfil depois da mudança — a sessão antiga não é revogada nem revalidada. |
| [[../00 QA/03 - Casos de teste#^ct-034\|CT-034]] | ❓ | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |
| [[../00 QA/03 - Casos de teste#^ct-035\|CT-035]] | ❓ | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |
| [[../00 QA/03 - Casos de teste#^ct-036\|CT-036]] | ❓ | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |
| [[../00 QA/03 - Casos de teste#^ct-037\|CT-037]] | ❌ | Sem código — aguarda captura do endpoint de auditoria. |
| [[../00 QA/03 - Casos de teste#^ct-038\|CT-038]] | ✅ | Confirmado contra HML pela suíte automatizada (31/08/2026). **Portado e confirmado passando em Playwright** (02/10/2026, `api/auth/audit-sessions.spec.ts`, rótulo `A55-C01`) — rodado contra HML real, verde em 4.6s. Arquivo criado, ainda **não commitado** (worktree em HEAD destacado, branch a definir). |
| [[../00 QA/03 - Casos de teste#^ct-e01\|CT-E01]] | ⏳ | Fora do escopo do Termo de Referência — não executado. |
| [[../00 QA/03 - Casos de teste#^ct-e02\|CT-E02]] | ⏳ | Fora do escopo do Termo de Referência — não executado. |
| [[../00 QA/03 - Casos de teste#^ct-e03\|CT-E03]] | ⏳ | Fora do escopo do Termo de Referência — não executado. |

> Legenda: ✅ confirmado passando · ⚠️ achado real de produto (ver seção abaixo) · ❓ falha sem causa raiz identificada · ❌ sem código ainda · ⏳ fora do escopo do Termo.

---

## Achados reais de produto

> Achado de produto encontrado *pela* automação não é bug do teste — não "consertar" a asserção pra fazer passar. Quando confirmado, vira **Defeito** — decisão de 02/10/2026: por ora os 4 abaixo seguem como achado de conformidade, sem SGV próprio (ver `../00 QA/00 README` → Próximo passo).

- **CT-015** — em disputa: via automação, após o bloqueio na 5ª tentativa (log retorna `account-blocked`), a tentativa seguinte com a senha correta autentica. Validação manual do Rafael (tela e API) não reproduziu. Hipótese de corrida/timing não confirmada — 3 experimentos falharam por instabilidade do ambiente.
- **CT-029 / CT-030** — em Férias, escrita e leitura não são bloqueadas, diferente de Licença (CT-023/CT-024), que bloqueia corretamente. Divergência entre os dois estados de quarentena — confirmar com produto se é intencional.
- **CT-033** — sessão obtida antes da mudança para Inativo segue acessando o próprio perfil depois da mudança — a sessão antiga não é revogada nem revalidada.

---

## Pendências

1. **CT-015** — repetir o experimento de timing (script pronto) assim que o ambiente HML estabilizar.
2. **6 CTs sem causa raiz** (CT-022/026/028/034/035/036) — mesma janela de investigação do item 1.
3. **CT-029/030/033** — confirmação rápida com produto/backend se a divergência Licença × Férias é intencional.
4. **CT-016/017/037** — aguardam captura de API nova (desbloqueio manual e endpoint de auditoria).
5. **Porte Cypress → Playwright** de toda a suíte, antes de qualquer MR novo — Suítes 1, 2 (12 CTs, já estava feito, achado em 02/10) e CT-038 (13º, portado em 02/10) prontos; restam 25 CTs (Suíte 3 inteira, Suíte 4 inteira, CT-037).
6. **Commitar `audit-sessions.spec.ts`** — escrito e testado (verde), mas o worktree `sogov-automation-playwright` está em HEAD destacado; Rafael decide a branch antes de commitar.

---

## Checklist antes de subir

- [ ] Crivo de [[Sistema/Skills/SKILL_REVISAO_CODIGO_AUTOMACAO|SKILL_REVISAO_CODIGO_AUTOMACAO]] aplicado.
- [ ] 4 achados reais confirmados/triados com produto/backend.
- [ ] 6 falhas sem causa raiz investigadas.
- [ ] Suíte portada pra Playwright.
- [ ] Cobertura por CT (tabela acima) refletida em `../00 QA/03 - Casos de teste` (campo `Automação` de cada CT).
- [ ] Status desta nota atualizado.
