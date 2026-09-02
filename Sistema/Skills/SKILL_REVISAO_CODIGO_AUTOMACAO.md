---
tags:
  - qa
  - skill
---
# Skill: Revisão de Código de Automação (grupo/suíte)

Revisar um **grupo de testes** de automação (uma suíte, um domínio inteiro, ou tudo que vai
entrar num MR) — API **e** E2E — antes de subir. Foco em duplicação de lógica entre arquivos,
reuso de comandos já existentes, organização de specs, e impacto de qualquer correção em código
**pré-existente** compartilhado por outras suítes. Não substitui as skills irmãs, complementa:

- [[SKILL_REVISAO_AUTOMACAO_E2E]] — crivo fino de **1 feature E2E** específica (padrão de
  seletores, asserts de toast, docs). Usar essa depois desta, arquivo por arquivo.
- [[SKILL_REVISAO_ESCOPO_MR]] — confere se o fix de um **MR do GitLab** bate com o problema
  relatado (critérios de aceite). Não olha duplicação/qualidade de código em si.

Repo: `~/Documentos/Sogov/sogov-automation-test`.

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Revisão de um grupo/suíte antes de subir | "confere duplicação nessa suíte", "faz um code review desse grupo de testes" |
| Passo dentro de outro fluxo | Parte de [[SKILL_AUTOMACAO_TERMO_REFERENCIA]], antes do passo "subir" |

## 1. Mapear o grupo em revisão

Listar todos os specs e commands tocados pelo grupo (não só o arquivo mais recente — todo o
domínio/suíte em questão):

```bash
ls cypress/testes/api/entities/<dominio>/*.cy.js cypress/testes/e2e/entities/<dominio>/*.cy.js
```

## 2. Checklist principal

- [ ] **Duplicação de lógica entre arquivos** — helpers/funções locais repetidos quase iguais
      entre 2+ specs do mesmo domínio. Sinal: uma `const minhaFuncao = (...) => {...}` de 15+
      linhas que aparece em mais de um arquivo com só um parâmetro (nome/prefixo) mudando.
      Extrair pra um command único, parametrizado. *Exemplo real: `createIsolatedTestAgent`
      duplicado entre `lockout.api.cy.js` e `identity-lifecycle.api.cy.js` — virou
      `cy.createIsolatedTestAgent(token, instanceId, sectorId, namePrefix, scenarioTag)` em
      `user.api.commands.js`.*
- [ ] **Reuso de comandos existentes** — todo command novo faz, de fato, algo que não existe
      ainda? `grep -rn "Cypress.Commands.add('<nome-parecido>'" cypress/support/commands/` antes
      de aceitar um comando novo.
- [ ] **Organização de specs** — pasta `api/` vs `e2e/` bate com o padrão já estabelecido no
      domínio (`entities/<dominio>/`); nome de arquivo segue a convenção
      (`<nome>.api.cy.js` / `<nome>.e2e.cy.js`).
- [ ] **Impacto em código pré-existente** — toda correção que mexe num command/helper que **já
      existia antes desta feature** precisa apontar quem mais usa ele:
      ```bash
      grep -rn "<nomeDoComando>" cypress/testes cypress/support | grep -v <arquivo-que-você-mexeu>
      ```
      Se houver outros consumidores, confirmar que o comportamento novo não muda contrato
      (assinatura, shape do retorno, quando lança erro) — só corrige o bug, não muda o que os
      outros já esperavam. *Exemplo real: `finishAgentRegistry` (faltava `return`) é usado por
      `getPublicAgentOrCreate`, chamado em 6 pontos do setup global e por 4 suítes de
      `public-agent/` — fix confirmado seguro (só corrige uma race condition, não muda retorno).*
- [ ] **Coerência de asserts** (generalizado do crivo E2E pra API também) — cada assert valida o
      sinal certo? Prefira mensagem de erro específica (`resp.body?.error?.exception?.message`)
      a só "status não é 200/201" quando o backend expõe algo mais preciso.
- [ ] **Docs × código** — `docs/commands/**` e `docs/business-rules/**` batem com o código atual
      (mesmo crivo do [[SKILL_REVISAO_AUTOMACAO_E2E]] — commands novos ou corrigidos têm entrada
      de doc correspondente, acréscimo nunca reescrita).
- [ ] **Qualidade e convenção dos comentários** — grep por `Rafael|confirmar com|PENDENTE|não
      investigado a fundo|preciso investigar` nos arquivos do grupo. Um comentário de código deve:
      1. Explicar o **PORQUÊ** não-óbvio (uma restrição, um bug real, uma decisão) — nunca repetir
         o que o código já deixa claro pelo nome.
      2. **Nunca citar uma pessoa** (nem "confirmado com Fulano", nem "perguntar pro Fulano") — se é
         regra confirmada, registrar a regra em si; se está em aberto, isso é conteúdo de
         doc/handoff, não de comentário de código.
      3. Ser **fato, não diário de investigação** — descrever o comportamento atual conhecido (o
         quê + evidência mínima), nunca narrar a jornada de debug ("testei isso, não resolveu,
         ainda preciso ver X") — isso pertence à documentação viva (Handoff/Entrega), não ao código.
      4. **Sem plano de próxima sessão embutido** — "próximo passo: investigar Y" vai pro Handoff,
         nunca pro comentário. *Exemplo real: comentários com "PENDENTE — achado não totalmente
         diagnosticado... precisa de uma rodada isolada pra..." em `identity-lifecycle.api.cy.js`
         reescritos como fato direto ("Achado sem causa raiz conhecida: X não encontra Y, testado
         Z, sem efeito"), sem a narrativa de próximos passos.*

## 3. Rodar pra confirmar que nada quebrou

Depois de qualquer extração/refactor (item "Duplicação" acima), rodar o grupo inteiro de novo —
resultado tem que ser **idêntico** ao de antes do refactor (mesmos CTs passando/falhando, mesmos
motivos):

```bash
cd ~/Documentos/Sogov/sogov-automation-test
npx cypress run --browser chrome --spec "<specs do grupo>" --reporter mochawesome \
  --reporter-options reportDir=cypress/reports,overwrite=false,html=false,json=true
```

## 4. Saída — relatório por arquivo/suíte

- ✅ limpo (sem duplicação, reuso correto, organização ok)
- ⚠️ achado de duplicação/reuso — arquivo:linha + sugestão de extração
- 🔴 impacto arriscado em código pré-existente — quem mais usa + o que pode quebrar
- **Decisão**: "pode subir" ou "ajustar X antes" (mesmo formato das skills irmãs)

## Exemplos reais

| Grupo | Achados | Decisão |
|---|---|---|
| TR 1.24-1.25, Suíte 1 (`login.api.cy.js`) — 02/09/2026 | Nenhuma duplicação; só reusa commands pré-existentes + os novos `loginAgentExpectFailure`/`loginCitizenExpectFailure` (usados também por outras 4 suítes, não é duplicação). Organização api/e2e confere com o padrão de `public-agent/`. | Pode subir sem pendência |
| TR 1.24-1.25, Suítes 3/4 (`lockout.api.cy.js` + `identity-lifecycle.api.cy.js`) — 02/09/2026 | `createIsolatedTestAgent` duplicado quase igual nos dois arquivos (só prefixo do nome/e-mail e shape do retorno mudavam). Fix pré-existente em `finishAgentRegistry` confirmado usado por 6 pontos do setup global + 4 suítes de `public-agent/` — seguro (só corrige race condition). | Extraído pra `cy.createIsolatedTestAgent` único; suítes rodadas de novo, resultado idêntico ao anterior (4/5 e 8/17, mesmos motivos) |
| TR 1.24-1.25, todos os specs de `auth/` — 02/09/2026 (revisão de comentários) | 2 comentários citando "Rafael" diretamente (`login.api.cy.js`, `lockout.api.cy.js`); 2 blocos em tom de diário de investigação com plano de próxima sessão embutido (`identity-lifecycle.api.cy.js`, CT-022 e CT-034); `login.e2e.cy.js` usava `formatCNPJ()` (CNPJ formatado) — divergia da regra já confirmada via API no CT-003 (CNPJ deve ser RAW), achado ao revisar o comentário de "suposição" do teste. | Comentários reescritos conforme a convenção acima. `login.e2e.cy.js` corrigido pra CNPJ raw (fix correto, consistente com CT-003) — mas **ainda não confirmado verde**: 3 rodadas seguidas falharam por 3 motivos diferentes de instabilidade de frontend no homolog (erro de asset, timeout de redirect, elemento não encontrado), nunca chegou a expor se o fix resolve o comportamento de fato |

## Resultado Esperado

Crivo de qualidade de código (não de comportamento) aplicado a um grupo inteiro de testes antes
de subir — pega duplicação e reuso que uma revisão arquivo-por-arquivo ([[SKILL_REVISAO_AUTOMACAO_E2E]])
não enxerga, e confirma que correções em código pré-existente são seguras pra quem mais depende
dele. A revisão em si não altera nada além do que for uma extração/dedup explicitamente aprovada;
correções de comportamento ficam fora do escopo desta skill.
