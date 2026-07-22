---
tags:
  - qa
  - skill
---
# Skill: Revisão de Automação E2E

Revisar uma feature de teste e2e do repositório de automação (Cypress) ANTES de subir — conferir
se o código segue os padrões do repo, se as asserções ("expects") são coerentes, e se
comentários/docs batem com o código. Não é code review profundo nem validação de bug — é o crivo
de qualidade do próprio teste automatizado.

Repo: `~/Documentos/Sogov/sogov-automation-test` (GitLab `qa_sogov/sogov-automation-test`).
Complementa [[SKILL_REVISAO_ESCOPO_MR]] (que checa se o fix do MR bate com o problema); aqui o
foco é o **código do teste em si**.

## Gatilhos
| Gatilho | Exemplo |
|---|---|
| Pedido de revisão de teste e2e | "revisa a automação e2e de <feature>", "confere se o teste tá no padrão" |
| Antes de commit/MR de teste novo | "esse e2e tá pronto pra subir?" |

## 1. Mapear os arquivos da feature
Uma feature e2e costuma ter (nem sempre todos):
- Command: `cypress/support/commands/e2e/<dominio>.e2e.command.js`
- Spec: `cypress/testes/e2e/entities/<entidade>/<nome>.cy.js`
- Import do command em `cypress/support/e2e.js`
- Docs: `docs/commands/e2e/<dominio>.e2e.md` e `docs/business-rules/e2e/<dominio>-flow.md`

## 2. Convenções do repo (o padrão a exigir)
Comparar contra 2-3 irmãos (ex.: `processing/sign.document.cy.js`,
`organizational/sector.e2e.cy.js` e os commands correspondentes):
- **Spec**: `describe("Entidade - Ação")`; `beforeEach` lê env
  (`INSTANCE_ID`/`AGENT_CPF`/`AGENT_PASSWORD`) e faz `loginAgent`; título `"[SUCESSO] Como
  <persona>, desejo <ação>"`; passos com `cy.log("AÇÃO N: ...")` / `PRECONDIÇÃO` / `RESULTADO`;
  imports relativos; dados de teste dinâmicos (`faker`) ou valores fixos.
- **Command**: comandos não-triviais têm comentário antes do `Cypress.Commands.add` (os óbvios
  podem não ter); arquivos maiores costumam usar divisórias `// ---`; comandos best-effort
  recursivos com `attemptsLeft`; `scrollAndClick`/`scrollAndGet`; `cy.log("[CMD] ...")` quando
  ajudar o diagnóstico. Nada disso é obrigatório em todo comando — é o estilo dominante, não regra
  rígida (não reprovar um comando só por não ter comentário/divisória).
- **Asserts**: baseados em toast/estado visível — `cy.contains('[data-testid="flashMessage-snackbar"]',
  <texto>).should('be.visible')` com timeout generoso (10-30s).
- **Docs**: quando existem, ficam em dois lugares — `docs/commands/e2e/` (assinatura + descrição +
  exemplo) e `docs/business-rules/e2e/` (fluxo + gotchas + resultado esperado). Nem toda feature
  tem os dois (algumas só têm o de commands) — a ausência de um deles não é, por si, defeito.

## 3. Checklist de auditoria
- [ ] **Padrão**: spec/command/docs batem com a seção 2?
- [ ] **Coerência dos expects**: cada asserção valida algo real e no lugar certo? Existe um assert
      FINAL que garante o fluxo inteiro, sem caminho de falso-positivo (se um passo falhar em
      silêncio, o assert final tem que quebrar)? O texto/regex do toast confere com o que o front
      realmente mostra?
- [ ] **Comentário × código**: nenhum comentário contradiz o código. Grep de termos que ficam
      stale após iterações: `grep -nE "Suposição|TODO|cy\.document\(|<termos antigos do fluxo>" <arquivos>`
- [ ] **Docs × código**: seletores, passos e ordem de asserts nos .md batem com o código atual.
- [ ] **Risco de flake**: `cy.wait(<fixo>)`; seletores frágeis (classe MUI com sufixo `css-*`
      dinâmico — preferir testid ou classe estável, ex.: `.casca-dialog`); dependência de
      ordem/estado não garantido.
- [ ] **Código morto**: command definido e não usado deve estar sinalizado (`// NÃO USADA hoje ...`).

## 4. Rodar pra confirmar verde
```bash
cd ~/Documentos/Sogov/sogov-automation-test
npx cypress run --spec <caminho-do-spec>
```
Esperado: `1 passing` / `All specs passed!`. O env de runtime (`INSTANCE_ID`/`AGENT_CPF`/
`AGENT_PASSWORD`) vem do setup; sem ele localmente, o veredito de comportamento sai pelo CI no
push. Rodar 2x pra descartar flake.

## 5. Saída — relatório rankeado
- **Veredito**: "no padrão?" e "expects coerentes?" (sim/não + porquê).
- **Achados** por gravidade: 🔴 crítico (contradição/bug) · 🟡 médio · ⚪ leve/opcional ·
  ✅ positivos confirmados. Cada um com `arquivo:linha` + sugestão.
- **Decisão**: "pode subir" ou "ajustar X antes".

## Exemplos reais

| Feature | Achados | Decisão |
|---|---|---|
| `matters-services/matter-service.cy.js` (Criar Serviço) — 21/07/2026 | Criava "Assunto", mas o fluxo real capturado é "Serviço" (`type=SERVICES`); módulo chutado (`Alvarás` → `Precondition DO API`); a tela Casca era detectada por um testid inexistente → trocado pela classe estável `.casca-dialog` (senão o loop clicava no "Avançar" já coberto pelo modal → 60s de timeout); assert final na ordem errada (tem que vir DEPOIS de "Ajustar proporção", que dispara o `updateMatterService` `status:READY`); vários comentários desatualizados. | Ajustar antes de subir → depois **verde 2x seguidas** |

## Resultado Esperado
Crivo rápido e consistente de qualidade do teste e2e antes do commit/MR — mesmo veredito e
formato toda vez, independente de quem (ou qual IA) revisa. A revisão em si não altera nada;
correções só depois de aprovadas.
