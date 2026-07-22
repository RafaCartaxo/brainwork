---
tags:
  - qa
  - skill
---
# Skill: Iniciar Automação de Card

Levar um card de QA **já validado** (card + casos de teste escritos) até o **início da escrita dos testes automatizados** — decidindo *se* é hora, *onde* escrever e *o que* já existe pra reaproveitar. Esta skill cobre a **decisão e a preparação**; a escrita mecânica do teste segue o guia que vive dentro do próprio repositório de automação (ver "Onde a automação mora").

É o passo **anterior** à [[SKILL_REVISAO_AUTOMACAO_E2E]] (que revisa e2e já escrito): aqui vai-se do card pro teste; lá, revisa-se o teste pronto.

## Contexto (leia antes — necessário pra qualquer IA/pessoa que não conhece o setup)

- **Vault QA (Obsidian)** — onde vivem cards, CTs, refinamentos, planos e skills:
  - Card: `QA Workspace/02 Demandas/<ambiente>/` (ambiente = `DEV`, `HML`, `Concluídas`...).
  - Casos de teste: dentro do card, seção "Casos de Teste Básicos" (CT-B01…), formato Dado/Quando/Então ([[SKILL_CASOS_DE_TESTE]]).
  - Mapeamento/refinamento e planos: `QA Workspace/04 Conhecimento/`.
- **Repositório de automação** — `sogov-automation-test` (Cypress, standalone), em `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-test`. É **aqui** que a automação de QA é escrita.
  - **NÃO** usar o pacote `packages/e2e` dentro do `Sogov-application` (monorepo). Decisão do time: automação de QA nova não vai lá.
  - O repo tem um **guia próprio de escrita de teste** em `.claude/agents/criar-teste-e2e.md` (convenções obrigatórias, estrutura, gotchas de MUI, personas, navegação). Esse guia é a **fonte de verdade de *como* escrever o teste**. Esta skill do vault **não duplica** isso — só aponta pra ele. Reaproveitar factories/commands/specs existentes do mesmo domínio antes de criar do zero.
  - O repo roda contra um **ambiente específico** definido em `cypress.env.json` (atualmente **HML**). Scripts: `npm run open` (UI) / `npm run chrome` (headless).

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Pedido explícito | "iniciar automação da SGV-XXXX", "vamos automatizar o card X" |
| Após validação de um card | card aprovado e o time quer cobertura automatizada de regressão |

## Pré-requisitos (GATES — não pule)

Automação vem **depois** da validação manual, **nunca antes**. Confirmar os dois gates antes de escrever qualquer teste:

1. **Card validado manualmente** — os CTs do card já foram executados (marcados Passou/Não) e os critérios de aceite confirmados. Se o card está `aberto` / sem execução → **pare**: valide manualmente primeiro. Automatizar comportamento não confirmado arrisca cristalizar um assert errado num teste.
2. **Fix disponível no ambiente que o Cypress ataca** — o repo roda contra um ambiente fixo (ver `cypress.env.json`, hoje HML). Se a correção do card ainda está só em DEV, um teste do comportamento corrigido **falha** contra esse ambiente. Confirme que o fix chegou no ambiente-alvo antes de escrever asserts do comportamento novo.

Gate aberto → registrar bloqueio na fila da daily como pendência `⏳` com o motivo, e **não começar**.

## Passo a passo

1. **Extrair o insumo do card** (no vault): descrição, resultado esperado, critérios de aceite e os CTs (Dado/Quando/Então). Ler também o mapeamento/refinamento em `04 Conhecimento/` e a doc de módulo relacionada em `04 Conhecimento/Módulos/`. Os CTs são o roteiro do que automatizar.
2. **Levantar gaps do cenário ANTES de escrever** (é o passo que costuma travar):
   - **Dados de teste**: o cenário exige personas/setores/documentos/permissões que já existem no env do repo (`cypress.env.set.json`) ou falta provisionar? Falta = pré-trabalho de setup.
   - **Cobertura/commands**: já existe command/fluxo no repo pro que o cenário precisa, ou terá de ser criado?
   - **Camada**: dá pra cobrir por **API** (mais rápido, menos frágil) ou exige **E2E de UI**? Preferir começar por API quando o comportamento é verificável por API; E2E quando é interação de tela.
   - **Registrar os gaps** (na daily e/ou no plano do card em `04 Conhecimento/`) — eles viram as primeiras tarefas da automação.
3. **Escrever o(s) teste(s)** seguindo o guia do repo `.claude/agents/criar-teste-e2e.md` (convenções, estrutura, selectors, personas). Reaproveitar antes de criar.
4. **Rodar localmente** contra o ambiente-alvo e confirmar verde — incluindo regressão dos fluxos que o fix tocou.
5. **Entregar pra revisão** via [[SKILL_REVISAO_AUTOMACAO_E2E]] antes do commit/MR.
6. **Registrar na daily** (`## Atividades → ### Planejamento`, copies do [[../../QA Workspace/01 Daily/README|01 Daily/README]]) o início/andamento, com wikilink pro card; atualizar o Histórico do card quando a cobertura automatizada existir.

## Resultado Esperado

Decisão consciente de **quando** automatizar (gates cumpridos), **onde** (repo standalone `sogov-automation-test`) e **o quê** (CTs do card mapeados por camada), com os gaps de setup levantados **antes** da escrita — e o teste entregue pra revisão. Nunca automação antes de validação manual; nunca teste escrito contra ambiente onde o fix ainda não está.
