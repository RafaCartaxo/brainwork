---
tags:
  - qa
  - conhecimento
  - automacao
tipo: referencia
revisado: 2026-07-22
---
# SGV-9610 — Plano de Automação

> [!info] O que é esta nota
> Plano de referência pra automatizar a SGV-9610 ("Associar Documento — Abertura Multi-Setor"), pra ficar fácil de retomar quando a implementação começar. Fluxo geral: [[Sistema/Skills/SKILL_INICIAR_AUTOMACAO|SKILL_INICIAR_AUTOMACAO]]. Material relacionado: [[SGV-9610 - Refinamento Associar Documento Abertura Multi-Setor|mapeamento/refinamento]], card [[../02 Demandas/DEV/9610 - Bug Associar Documento Abertura Multi-Setor|SGV-9610 (DEV)]], doc [[Módulos/Associar e Desassociar]].

## Contexto

Ao começar a validar a 9610 em DEV, levantou-se a dúvida: *pra iniciar a automação, já tem tudo pronto?* Investigação (vault + repo `sogov-automation-test` + `packages/e2e`) concluiu: **documentalmente pronto, procedimentalmente prematuro** — por dois gates de ambiente. Este plano registra o estado e a sequência.

**Decisões:**
- Automação mora no **`sogov-automation-test`** (standalone). **NÃO** usar `packages/e2e` do sogov-application.
- Toda documentação (este plano + a skill) fica no Obsidian. O guia de *escrever* teste continua no repo (`.claude/agents/criar-teste-e2e.md`); a skill do vault aponta pra ele.

## Estado atual (assessment)

**Especificação — pronta:**
- Refinamento `status: refinado` (17/07): [[SGV-9610 - Refinamento Associar Documento Abertura Multi-Setor]].
- Card [[../02 Demandas/DEV/9610 - Bug Associar Documento Abertura Multi-Setor|9610 (DEV)]]: 6 CTs em Gherkin (CT-B01…B06), 5 critérios, ambiente DEV, ligado ao MR !537. **Status `aberto` — zero execução manual.**
- Doc de módulo [[Módulos/Associar e Desassociar]] cobre o comportamento multi-setor.

**Terreno de automação (`sogov-automation-test`) — pronto:**
- Padrões claros (factories, commands API/E2E, helpers; guia interno `.claude/agents/criar-teste-e2e.md`). Env preenchido, aponta pra **HML**, roda hoje (`npm run open` / `npm run chrome`).
- Já existe `cypress/testes/api/entities/processing/associate.document.api.cy.js` — mas só **single-setor** (associar na abertura / via despacho). O caso **multi-setor** da 9610 **não** está coberto → 9610 = estender esse spec (sem duplicar).

## Dois gates (por que não agora)

1. **Card não validado em DEV** — nenhum CT executado. Automatizar antes de confirmar arrisca cristalizar um assert errado.
2. **Fix (MR !537) está em DEV, não em HML** — o Cypress do standalone roda contra **HML**, onde o bug ainda está vivo; um teste do comportamento corrigido **falharia hoje**.

## Roadmap (gated; só quando os gates abrirem)

**Gate 1 — validar 6 CTs manualmente em DEV:** executar CT-B01…B06, marcar Passou/Não + critérios, gravar evidência, mover card DEV→HML quando aprovado.
**Gate 2 — MR !537 em HML:** confirmar que o fix chegou no ambiente que o Cypress ataca.

Quando abrirem, na ordem:
1. **Camada API** — estender `cypress/testes/api/entities/processing/associate.document.api.cy.js` com os casos **multi-setor** (CT-B01 acesso por setor não-atuante, CT-B04 sem-acesso fica fora, CT-B03 paridade abertura×despacho). Reusar `support/test-data/factories/document.processing.factory.js` (`makeDocument({ documentsAssociated })`) e `support/commands/api/document.processing.api.commands.js`. Precisa de persona multi-setor + 2º `SECTOR_ID` no env.
2. **Camada E2E** — novo spec em `cypress/testes/e2e/entities/processing/` pro **drawer de associação na abertura** (feature 22/10/2025). Selectors por `data-testid`; gotchas MUI em `.claude/agents/criar-teste-e2e.md`.
3. **Regressão de assinatura** — o MR !537 toca `SignatureToolbarItem.tsx`; rodar `cypress/testes/e2e/entities/processing/sign.document.cy.js` (CT-B06).
4. **Revisão + MR** — passar pela [[Sistema/Skills/SKILL_REVISAO_AUTOMACAO_E2E|SKILL_REVISAO_AUTOMACAO_E2E]] antes do push.

**Arquivos-chave a reaproveitar:** `associate.document.api.cy.js`, `document.processing.factory.js`, `support/commands/api/`, `.claude/agents/criar-teste-e2e.md`.

## Gaps conhecidos do cenário multi-setor (levantar/prover antes de escrever)
- **Persona multi-setor** + **2º setor** provisionados no env do repo (`cypress.env.set.json`) — o happy path atual é single-setor.
- Confirmar cobertura/commands pro fluxo do **drawer de abertura** na camada E2E (a associação hoje é coberta por API, não UI).
