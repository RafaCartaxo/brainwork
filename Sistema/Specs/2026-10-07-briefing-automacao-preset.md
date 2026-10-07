---
tags:
  - qa
  - automacao
  - spec
data: 2026-10-07
---
# Briefing — Automação SOGOV: estado atual, convenções e ponto de dor

> Documento gerado pra servir de contexto numa sessão de desenho de processo (Codex). Cobre: como a task de automação chega hoje, como os arquivos estão organizados (vault + repo), convenções de código, e o caso concreto que motivou a pergunta — aplicar um conceito de "Preset" na TR 1.24-1.25.

## Objetivo de quem está lendo isto

Rafael é responsável por evoluir a automação do Termo de Referência (TR) do SOGOV. Quer adotar um padrão pra que a automação "nasça junto" com a demanda, do mesmo jeito que o pacote de QA manual já nasce hoje (template fixo, preenchível). O padrão atual de automação existe mas ficou com texto demais, longe do estilo enxuto do resto do vault — é isso que precisa ser redesenhado.

## 1. Dois mundos — vault e repo

- **Vault Obsidian** (`/home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork`) — documentação viva do trabalho de QA: demandas, casos de teste, validação, automação. Cada demanda vira um "pacote" de arquivos.
- **Repo de automação** (`sogov-automation-test`, worktree de leitura em `sogov-automation-playwright`) — o código de automação de verdade. Playwright é o padrão atual (`playwright/`); Cypress é legado em fim de vida (segue rodando, não recebe teste novo).

## 2. Como a task de automação chega hoje (intake)

No vault, cada demanda vira:
```
02 Demandas/<ambiente>/<SGV> - <título>/
├── 00 QA/         manual: 01-Demanda → 02-Plano de teste → 03-Casos de teste → 04-Validação dev → 05-Preparação Qase
└── 01 Automação/  opcional — só nasce se alguém decidir automatizar; sem gatilho automático
```

No repo, intake de automação hoje é 100% manual: ler os CTs do vault → escrever um briefing → disparar um subagente (`.claude/agents/criar-teste-{e2e,api}.md`, no repo) → o spec sai em `tests/{api,e2e}/<domínio>/*.spec.ts`. **Esses subagentes são do Cypress legado — não existe equivalente ensinando Playwright ainda.**

## 3. Organização de arquivos

| Onde | O quê |
|---|---|
| `Sistema/Templates/Pacote/00 QA/*` (vault) | templates manuais — curtos, tabela + checklist |
| `Sistema/Templates/Pacote/01 Automação/*` (vault) | templates de automação (ver seção 6) |
| `playwright/tests/{api,e2e}/<domínio>/*.spec.ts` (repo) | specs — 1 arquivo por suíte, 1 `describe`, 1 `test` por CT |
| `playwright/src/api/services/*.ts` (repo) | operação de API por entidade, padrão `getXOrCreate` |
| `playwright/src/data/factories/*.ts` (repo) | monta payload de mutation |
| `playwright/src/data/seed/*.ts` (repo) | baseline fixo + `provisionBaseline` (idempotente) |
| `playwright/src/ui/<domínio>.ts` + `internal/` (repo) | ações de tela, com `test.step` automático |
| `playwright/src/fixtures/index.ts` (repo) | `actors`, `seed`, `env`, `cleanup` |
| `playwright/planning/*.md` (repo) | 15 docs de arquitetura/decisão (regra D4, inventários de ID, paridade Cypress→Playwright) |

## 4. Convenções de escrita de teste (repo)

- **ID no título**: `A<NN>` (API) ou `E<NN>` (E2E) + `-C<NN>`/`-S<NN>`. Numeração **sequencial por arquivo de origem do Cypress legado** — não tem relação com o `CT-NNN` do vault. Esse descasamento de numeração é um gap real de rastreabilidade entre vault e repo.
- Próximo ID livre é consultado em `playwright/planning/11-INVENTARIO-API.md` (registro central — nunca "chutar" um número).
- Classificação obrigatória no título: `[SUCESSO]` · `[FALHA]` · `[REGRESSÃO]`.
- Comentário de origem logo após os imports (de onde veio o caso, por que diverge se divergir).
- Toda `expect` leva mensagem descritiva no segundo argumento.
- Tags: `['@api'|'@e2e', '@<domínio>']` no describe; `@smoke` no test, nunca no describe; `@shared-state` quando o arquivo muta estado compartilhado.
- Bug de produto conhecido: `test.fail()` imediatamente antes da asserção, nunca no topo do teste.
- Skip sempre com `annotation` tipada explicando o motivo (ex.: `d4`, `pendencia-de-produto`).

## 5. Pontos principais de arquitetura/código

- Toda função de API recebe `instanceId` explícito (`GraphQLClient.withTenant(instanceId)`, em `src/api/graphql-client.ts`) — a arquitetura já é pronta pra multi-cliente, mas hoje só uma instância fixa roda de verdade (`BASELINE.instance` em `src/data/seed/baseline.ts`).
- O padrão `getXOrCreate` idempotente (`getInstanceOrCreate`, `getSectorOrCreate`, `getModuleOrCreate`, `getMatterServiceOrCreate`, `getPublicAgentOrCreate`, `getCitizenOrCreate` — todos em `src/api/services/*.ts`) **é**, na prática, o conceito de "Preset" que já existe no repo — só que hoje aplicado só ao baseline fixo do seed, nunca a um cliente variável.
- **Regra D4** (documentada em `planning/13-REVISAO-E-ONDAS-DREAM.md:242`): nunca criar instância/usuário novo em execução normal de teste — não existe API de exclusão de instância no backend, então criar à vontade vira lixo permanente no ambiente compartilhado. `tests/api/instance/in-deployment.spec.ts` já tem o código pra criar instância, mas está `test.skip` por essa razão.
- Sharding/paralelismo multi-ambiente é bloqueado explicitamente em `scripts/run.mjs` ("concorrência no tenant único") — a arquitetura assume **um backend, uma instância, uma execução por vez**.
- `changePublicAgentWorkStatus(publicAgentId, input: Status)` — muda o status do servidor (Ativo/Licença/Férias/Inativo-Suspenso). **Mutation e enum já confirmados via captura real de API** (`WORK_STATUS = IN_ACTIVITY | LICENSE | VACATION | SUSPEND`), implementados como command Cypress, **nunca portados pro Playwright** (`src/api/services/users.ts` hoje só tem `getPublicAgentOrCreate`/`editPublicAgent`).

## 6. O template de automação que já existe no vault (os 5 arquivos)

`Sistema/Templates/Pacote/01 Automação/`:

1. `00 - Automação.md` — hub, status geral, link pros outros 4
2. `01 - Plano de automação.md` — arquitetura/estratégia de porte **← este é o que virou texto demais, log de investigação acumulado**
3. `02 - Validação automação.md` — placar por CT (frontmatter `ct_resultados` + tabela + widget Meta Bind) **← este já é enxuto, bom modelo pro resto**
4. `03 - Handoff de execução.md` — log cronológico do processo
5. `04 - Documentação de entrega.md` — detalhe de code review

O ponto de dor: `01 - Plano de automação.md` cresceu como narrativa de investigação (decisões, achados, histórico), bem mais denso que o padrão tabela+checkbox do `00 QA/`. O `02 - Validação automação.md` é o contra-exemplo bom — nasceu justamente pra resolver esse mesmo problema de densidade, só que pro placar de resultado, não pro plano.

## 7. Processo/tooling com lacuna

- Não existe subagente Claude Code pra criar teste Playwright — só os antigos `.claude/agents/criar-teste-{e2e,api}.md`, que ensinam Cypress.
- CI roda só Cypress (`.gitlab-ci.yml`) — a suíte Playwright não protege merge nenhum ainda.
- O worktree `sogov-automation-playwright` está em HEAD destacado (sem branch) — decisão de branch pendente antes de qualquer commit novo nele.

## 8. Caso concreto que motivou a investigação — TR 1.24-1.25 (SGV-11971, vault)

38 CTs de autenticação/ciclo de vida, 5 suítes. Hoje portadas pra Playwright: Suítes 1, 2 e CT-038 (Suíte 5) — nenhuma delas precisa de "Preset" (usam só o servidor/cidadão padrão do baseline, sem estado especial).

**Quem precisa de Preset**: Suíte 3 (bloqueio/desbloqueio, CT-013 a CT-019) e Suíte 4 (ciclo de vida, CT-020 a CT-036) — ambas exigem um servidor **num estado específico** (bloqueado por tentativas, ou `workStatus` em Licença/Férias/Suspenso) antes do teste rodar, isolado do agente global do baseline (que não pode ser mexido sem quebrar os outros 127+ testes que dependem dele). Isso já tinha sido identificado pelo próprio Rafael em 31/08/2026 (`01 - Plano de automação.md`, vault): *"Usuários de teste isolados por cenário (bloqueio, Licença, Férias, Inativo, Suspenso) via `getPublicAgentOrCreate` com nome fixo por cenário — nunca reusar o agente global do setup."*

O que falta tecnicamente: portar `changePublicAgentWorkStatus` pro Playwright (seção 5). O que **não** é resolvido por um Preset (são gaps de investigação de produto, não de infraestrutura de teste): a mutation de desbloqueio manual (CT-017) nunca foi capturada; o mecanismo de aplicação em tempo real do status (CT-025/CT-033 — revogação de token? polling?) segue sem confirmação.

## 9. O que está em aberto pra desenhar agora

- Um padrão de template de automação no vault que "nasça junto" com a demanda, no mesmo estilo enxuto do `00 QA/` (tabela/checkbox, não narrativa).
- Decidir se o escopo do "Preset" agora é estreito (preparar servidor/cidadão num estado específico, pra destravar Suítes 3/4 da TR 1.24-1.25) ou genérico (módulos/assuntos/serviços/documentos, qualquer cliente novo por `clienteId` — que hoje não existe como conceito no repo, nem variável de ambiente nem parametrização).
- Se for o escopo genérico, ficam em aberto: como o `clienteId` seria passado numa execução, e se o Preset precisa criar instância nova (esbarra na regra D4) ou só operar sobre instância já existente.

## 10. Revisão da estrutura atual e proposta

### Diagnóstico

A pasta atual tem informação suficiente para uma automação grande como a SGV-11971, mas os cinco arquivos não formam uma sequência simples de trabalho. Eles foram numerados como se fossem etapas, embora três sejam registros opcionais e de naturezas diferentes.

| Arquivo atual | Problema observado |
|---|---|
| `00 - Automação.md` | Mistura configuração, resumo, pendências gerais e checklist de saída. É um bom hub, mas o texto explica demais o que cada outro arquivo não deve conter. |
| `01 - Plano de automação.md` | Tem os campos certos para arquitetura, mas não define limite de tamanho nem destino para achados. Vira caderno de investigação e histórico. |
| `02 - Validação automação.md` | É o melhor modelo: estado atual por CT numa tabela, sem histórico. Deve continuar sendo a fonte única do resultado por CT. |
| `03 - Handoff de execução.md` | Junta estado de continuidade, decisões pendentes, regras e log cronológico. Handoff é uma necessidade eventual, não uma etapa obrigatória. |
| `04 - Documentação de entrega.md` | A revisão por cenário pode ajudar num porte grande, mas repete contexto e status e não é necessária em toda entrega. |

Há duplicação concreta na SGV-11971: resumo e pendências aparecem no hub, o plano contém histórico de investigação, o handoff repete decisões e progresso, e a documentação de entrega volta a descrever cobertura e situação. A navegação repetida em cada nota também ocupa espaço sem ajudar a decidir onde registrar uma informação.

### Estrutura recomendada

Manter a pasta `01 Automação/`, mas reduzi-la a três notas-base e uma nota opcional. A numeração representa ordem de leitura, não uma fila de etapas.

```text
01 Automação/
├── 00 - Automação.md          hub curto: contexto, estado e próximo passo
├── 01 - Plano de automação.md plano curto, necessário quando houver decisão técnica
├── 02 - Validação automação.md placar atual por CT; fonte única dos resultados
└── 03 - Histórico e handoff.md opcional: decisões, achados e contexto para retomar
```

`04 - Documentação de entrega.md` deixa de ser um arquivo padrão. Para automações grandes que realmente precisem de revisão detalhada, a tabela por CT pode ser uma seção opcional do plano ou um apêndice da nota de histórico. A entrega de código continua apontada pelo repo, branch/MR e revisão correspondente; não precisa de uma segunda narrativa de code review no vault.

### Quando criar cada nota

| Nota | Regra de uso | Fonte única para |
|---|---|---|
| `00 - Automação` | Sempre que a pasta existir. | Identificação do repo/framework, estado geral e próxima ação. |
| `01 - Plano de automação` | Se houver escolha de camada, preparação especial de dados, dependência técnica ou mais de uma suíte/fase. Em automação direta, registrar no hub que não houve plano separado. | Escopo automatizado e decisões de construção ainda válidas. |
| `02 - Validação automação` | Sempre que houver ao menos um CT automatizado. | Resultado atual de cada CT no framework atual, arquivo/spec, ambiente e observação curta. |
| `03 - Histórico e handoff` | Só quando outra sessão/pessoa precisar continuar ou quando decisões e achados exigirem histórico. | Linha do tempo curta, decisões tomadas, pendências com responsável/próxima ação e instruções de retomada. |

Não manter `03` como diário obrigatório: registrar apenas mudanças que expliquem o estado atual ou evitem repetir investigação. O resultado atual permanece em `02`.

### Conteúdo mínimo que o template precisa pedir

O conjunto deve permitir que uma pessoa entenda **o que será automatizado, onde está o código, como preparar/rodar com segurança e o que está passando agora**, sem ler um relato longo.

- **Hub (`00`)**: ID/link da demanda e CTs de origem; repo e framework; link de branch/MR quando houver; ambiente; estado geral; próxima ação objetiva; links para plano/validação/histórico existentes.
- **Plano (`01`)**: objetivo e CTs incluídos/excluídos; estratégia por suíte/camada; código e dados existentes a reaproveitar; dados/estado especial necessário e como será preparado/limpo; riscos de estado compartilhado; dependências ou lacunas que bloqueiam implementação; etapas/gates e critério de pronto. Cada linha deve ser decisão ou ação verificável, não narrativa de investigação.
- **Validação (`02`)**: uma linha por CT automatizado ou explicitamente fora/bloqueado; ID de CT ligado à origem; caminho do teste e rótulo; framework; resultado; observação curta/link ao histórico; ambiente e data/build da execução. O resumo e a tabela precisam usar estados compatíveis, sem contagens escritas manualmente em duas notas.
- **Histórico (`03`)**: data/rodada, o que mudou, decisão/achado e efeito no próximo passo. Instrução de retomada deve começar pelo estado atual e próxima ação, não recontar o projeto.

O template atual cobre repo, framework, ambiente, placar, arquitetura, fases e pendências. Precisa tornar explícitos a **origem e o escopo dos CTs**, o **preparo e limpeza de dados**, os **riscos de estado compartilhado**, os **comandos/condições de execução**, e **quem faz o próximo passo**. Esses campos cabem numa tabela/checklist curta; não exigem seções narrativas separadas.

### Aplicação ao preset

Para este pacote, “preset” deve ser tratado inicialmente como **preparo repetível de dados/estado para testes** (por exemplo, servidor de teste isolado bloqueado ou com `workStatus` específico), e não como um mecanismo genérico de provisionamento de qualquer cliente/instância. Isso corresponde à necessidade comprovada das Suítes 3 e 4 e evita sugerir que a regra D4 de criação de instâncias foi resolvida.

No plano, o preset entra como uma linha de preparação: estado desejado → mecanismo confirmado → identidade isolada → limpeza/limites → CTs consumidores. Até `changePublicAgentWorkStatus` e as regras de bloqueio estarem implementadas e validadas no Playwright, registrá-lo como dependência/pendência, sem prometer que os CTs já podem rodar.

### Migração e alcance

Esta proposta é para os templates e novos pacotes. A SGV-11971 contém histórico técnico útil e não deve ser reescrita só para caber no modelo curto; quando houver migração, preservar os detalhes como material de referência e atualizar apenas hub/placar para apontarem às fontes corretas. Antes de aplicar a estrutura aos templates, revisar também o mapa de pastas no `00 QA/00 README.md` e a descrição em `PADROES_QA.md`, que hoje ainda descrevem os cinco nomes antigos.
