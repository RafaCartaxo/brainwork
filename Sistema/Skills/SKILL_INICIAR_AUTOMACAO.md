---
tags:
  - qa
  - skill
---
# Skill: Iniciar Automação de Card

Levar um card de QA **já validado** (card + casos de teste escritos) até o **início da escrita dos testes automatizados** — decidindo *se* é hora, *onde* escrever, *o que* já existe pra reaproveitar e *qual massa de dados* a entrega precisa. Esta skill cobre a **decisão e a preparação**; os comandos e as regras de escrita vivem na documentação do próprio repositório (ver "Onde a automação mora").

É o passo **anterior** à [[SKILL_REVISAO_AUTOMACAO_E2E]] (que revisa e2e já escrito) e à [[SKILL_REVISAO_CODIGO_AUTOMACAO]]: aqui vai-se do card pro teste; lá, revisa-se o teste pronto.

## Contexto (leia antes — necessário pra qualquer IA/pessoa que não conhece o setup)

- **Vault QA (Obsidian)** — onde vivem cards, CTs, planos e skills:
  - Card: `QA Workspace/02 Demandas/<ambiente>/` (ambiente = `DEV`, `HML`, `Concluídas`...).
  - Casos de teste: `00 QA/03 - Casos de teste` do pacote, formato Dado/Quando/Então ([[SKILL_CASOS_DE_TESTE]]).
  - Pacote de automação do card: `01 Automação/` — `00 - Automação` (hub), `01 - Análise`, `02 - Plano de automação`, `03 - Validação automação` (modelo em `Sistema/Templates/Pacote/01 Automação/`).
  - Conhecimento de módulo: `QA Workspace/04 Conhecimento/Módulos/`.
- **Repositório de automação** — `sogov-automation-test`, em `~/Documentos/Sogov/sogov-automation-test`; o pacote Playwright está em `playwright/`. É **aqui** que a automação de QA é escrita. O Cypress foi removido do `main` em 15/10/2026; teste novo é só Playwright.
  - **NÃO** usar o pacote `packages/e2e` dentro do `Sogov-application` (monorepo). Decisão do time: automação de QA nova não vai lá.
  - **Fonte de verdade de *como* rodar e escrever:** `playwright/README.md` (comandos, como uma execução funciona, regras de escrita, seed, lista de testes) e `playwright/ENVIRONMENTS.md` (massa por QA). Em divergência, vale o código. O vault **não duplica** isso: [[00 - Índice da automação Playwright]] só aponta e guarda histórico, achados e registros de execução.
  - Setup do zero: [[01 - Primeiros passos]]. O ambiente-alvo vem do `playwright/.env` (`PW_BASE_URL`, `PW_GRAPHQL_URL`...); hoje é o homolog. Rodar sempre pelos scripts `npm run test:*` (passam pelo launcher `scripts/run.mjs`), nunca `playwright test` direto.

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Pedido explícito | "iniciar automação da SGV-XXXX", "vamos automatizar o card X" |
| Após validação de um card | card aprovado e o time quer cobertura automatizada de regressão |

## Pré-requisitos (GATES — não pule)

Automação vem **depois** da validação manual, **nunca antes**. Confirmar os dois gates antes de escrever qualquer teste:

1. **Card validado manualmente** — os CTs do card já foram executados e os critérios de aceite confirmados. Se o card está sem execução → **pare**: valide manualmente primeiro. Automatizar comportamento não confirmado arrisca cristalizar um assert errado num teste.
2. **Fix disponível no ambiente que a suíte ataca** — o repo roda contra o ambiente do `playwright/.env`. Se a correção do card ainda está só em DEV, um teste do comportamento corrigido **falha** contra esse ambiente. Confirme que o fix chegou no ambiente-alvo antes de escrever asserts do comportamento novo.

Gate aberto → registrar bloqueio na fila da daily como pendência `⏳` com o motivo, e **não começar**.

## Passo a passo

1. **Extrair o insumo do card** (no vault): descrição, resultado esperado, critérios de aceite e os CTs (Dado/Quando/Então), mais o mapeamento em `04 Conhecimento/` e a doc do módulo. Os CTs são o roteiro do que automatizar.
2. **Escrever a Análise** em `01 Automação/01 - Análise` (template em `Sistema/Templates/Pacote/01 Automação/`). É o passo que costuma travar, e vem **antes do plano**:
   - **O que já existe:** procurar no repo, por CT, spec com ID (`A##`/`E##`), serviço em `src/api/services/*`, helper em `src/ui/internal/*` e fixture em `src/fixtures/index.ts`. Registrar o mapa CT → teste existente; **não duplicar**.
   - **Camada:** API (mais rápida, menos frágil) quando o comportamento é verificável por API; E2E quando é interação de tela.
   - **Massa desta entrega:** quais atores, módulos, A&S e instâncias cada CT usa; o que é reuso do `baseline.ts` e o que é entrada nova; se o CT **altera** cadastro (então ator exclusivo, dono em `ownership.ts`, spec `@shared-state`); se dispara **e-mail real** e quantos. Preencher a tabela da Análise. Ator/módulo de teste versionado vai no `baseline.ts` (com comentário `// SGV-XXXX · CT-0xx: motivo`); `massa/<nome>.json` é só iteração local.
   - **Fora de escopo:** CT que fica manual e por quê (depende de job de BI, manda e-mail real a cada execução, comportamento não confirmado, nada no código).
   - **Pendências de decisão** pro Rafael/time; enquanto houver, a Análise fica `status: analise`. Fechado o gate da Análise, segue-se ao plano.
3. **Plano de automação** em `02 - Plano de automação`: matriz curta por suíte (camada, preparação/limpeza específica, reuso, dependência). Os dados e o estado inicial **apontam para a tabela de massa da Análise**, sem duplicá-la. A próxima ação geral fica no hub `00`.
4. **Escrever o(s) teste(s)** seguindo `playwright/README.md` (seção de regras de escrita) e o modelo de um spec do mesmo domínio. Reaproveitar antes de criar. Preparo de massa dentro do teste é por API; só a ação avaliada passa pela UI.
5. **Rodar** contra o ambiente-alvo só o seu caso (`node scripts/run.mjs --project=api --grep "<ID>"`) e confirmar verde — incluindo regressão dos fluxos que o fix tocou. Nunca rodar `npm run test` (suíte inteira satura o gerador de PDF; ver [[00 - Índice da automação Playwright]]). Antes de entregar: `npm run verify`.
6. **Entregar pra revisão** via [[SKILL_REVISAO_AUTOMACAO_E2E]] / [[SKILL_REVISAO_CODIGO_AUTOMACAO]] antes do commit/MR.
7. **Registrar na daily** (`## Atividades → ### Planejamento`, copies do [[../../QA Workspace/01 Daily/README|01 Daily/README]]) o início/andamento, com wikilink pro card. Manter `00 - Automação` com status/próxima ação, `01 - Análise` com decisões e massa, `02 - Plano de automação` com a estratégia e `03 - Validação automação` com o resultado atual por CT. Sincronizar a cobertura no campo **Automação** dos CTs.

## Resultado Esperado

Decisão consciente de **quando** automatizar (gates cumpridos), **onde** (`sogov-automation-test/playwright`), **o quê** (CTs mapeados por camada, reaproveitando o que existe) e **com qual massa** (registrada, com dono e risco de e-mail) — com os gaps levantados **antes** da escrita e o teste entregue pra revisão. Nunca automação antes de validação manual; nunca teste escrito contra ambiente onde o fix ainda não está; nunca massa nova sem registro na Análise.
