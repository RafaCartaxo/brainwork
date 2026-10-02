---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
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

> Esta nota é o **hub de configuração** — infraestrutura, pendências cross-cutting, checklist. **Não guarda placar por CT** (isso é [[02 - Validação automação|02 - Validação automação]], sempre atual) nem narrativa de achado/correção (isso é [[03 - Handoff de execução|03 - Handoff de execução]], histórico) — guardar os dois aqui de novo é como esta pasta ficou confusa da primeira vez.

> [!info]- Documentos detalhados desta automação
> - [[01 - Plano de automação|01 - Plano de automação]] — arquitetura, convenção de pastas/specs, faseamento.
> - [[02 - Validação automação|02 - Validação automação]] — placar atual por CT (framework, resultado, rótulo do teste).
> - [[03 - Handoff de execução|03 - Handoff de execução]] — estado/orquestração entre rodadas, log cronológico.
> - [[04 - Documentação de entrega|04 - Documentação de entrega]] — revisão cenário a cenário do que cada CT de código faz.

---

## Configuração

- **Repo:** `sogov-automation-test`
- **Branch/MR:** Suítes 1/2 mergeadas no `origin/main` (commit `6c9188c`, 09/09/2026). Suítes 3/4/5 commitadas só localmente (`bdf5e9a`, branch `tr-1.24-1.25-suites-3-4-5`, 01/10/2026) — não sobem em Cypress, serão portadas.
- **Framework:** Cypress — alvo migrou pra Playwright (01/10/2026); código a portar.
- **Ambiente de validação:** HML

---

## Status

Placar completo, por CT (resultado, framework, rótulo do teste): [[02 - Validação automação|02 - Validação automação]] — **25/38 aprovados, 13 no framework atual (Playwright)**. 4 achados reais em disputa/confirmação, 6 falhas sem causa raiz, 3 CTs sem código — detalhe de cada um na Observação da tabela e no [[03 - Handoff de execução|Handoff]].

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
- [ ] [[02 - Validação automação|02 - Validação automação]] refletida em `../00 QA/03 - Casos de teste` (campo `Automação` de cada CT).
- [ ] Status desta nota atualizado.
