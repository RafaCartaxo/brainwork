---
tags:
  - qa
  - skill
---
# Skill: Automação de Termo de Referência

Levar um **Termo de Referência sem CTs nem card ainda** até um conjunto de testes automatizados validados de verdade contra HML — cobrindo o degrau anterior ao de [[SKILL_INICIAR_AUTOMACAO]] (que já parte de um card validado manualmente): gerar os casos, investigar a API real quando não é conhecida, codar, VALIDAR rodando (não só escrever), triar cada falha (bug meu × achado real × instabilidade do ambiente) e preparar a subida.

Repo: `~/Documentos/Sogov/sogov-automation-test` (GitLab `qa_sogov/sogov-automation-test`).

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Pedido explícito | "automatiza o TR X.YY", "vamos automatizar esse Termo de Referência" |
| Termo de Referência sem CTs ainda | material novo (PDF/descrição) sem casos de teste escritos nem card criado |

## 1. Ponto de partida — gerar os CTs e o card

Diferente de [[SKILL_INICIAR_AUTOMACAO]] (que exige card **já validado manualmente**), aqui normalmente não existe nem CTs nem card ainda:

1. Gerar os casos de teste a partir do Termo ([[SKILL_CASOS_DE_TESTE]] — formato Dado/Quando/Então), organizados em suítes por área/requisito.
2. **Criar/linkar o card (SGV) o quanto antes** — não esperar até o fim da automação pra vincular (aconteceu na automação do TR 1.24-1.25: só foi criado depois de tudo codado, atrasando a rastreabilidade).
3. Confirmar a Fase 0 (gate de validação manual, mesmo fluxo de [[SKILL_INICIAR_AUTOMACAO]]) antes de codar qualquer suíte.

## 2. Fase 1 — investigação técnica (quando a API não é conhecida)

Quando o comportamento a testar depende de uma mutation/query/enum que não está documentada e a **introspection do GraphQL está desabilitada em HML** (comum neste ambiente — não insistir tentando de novo):

1. **Perguntar se já existe uma captura salva** (ex.: pasta `~/Downloads/` — foi onde a mudança de status do TR 1.24-1.25 estava, uma captura de API + Recorder do Chrome DevTools + o PDF do Termo) antes de pedir uma nova ao responsável.
2. Se não existir, pedir uma captura real (DevTools Network, salvar como HAR, ou o request/response colado) — nunca inventar o shape de uma mutation.
3. Cruzar a ordem dos passos de UI (se houver Recorder) com a ordem das chamadas de API capturadas na mesma sessão pra confirmar mapeamentos não óbvios (ex.: um rótulo de tela que mapeia pra um enum de nome diferente).
4. Registrar o achado numa doc de `docs/business-rules/api/` do repo de automação — é o que os subagentes de teste (`criar-teste-api`/`criar-teste-e2e`) encontram automaticamente depois.

## 3. Fase 2 — infraestrutura reaproveitável

Mesmas convenções de [[SKILL_INICIAR_AUTOMACAO]]: nunca duplicar command (`grep` antes de criar), reaproveitar padrão `getXOrCreate`, **agentes de teste isolados e dedicados por cenário** — nunca o agente/cidadão global do setup (cacheado via `cy.session` e reusado por todos os testes existentes; bloqueá-lo ou mudar seu status quebra a suíte inteira).

Gotcha confirmado: nome de agente de teste isolado tem limite de tamanho no backend (`exceed-max-length`) — manter curto (ex.: `Lifecycle {cpf}`), nunca embutir texto descritivo longo.

## 4. Fase 3 — escrever e VALIDAR de verdade

Escrever os testes seguindo o guia do repo (`.claude/agents/criar-teste-{e2e,api}.md`). **Rodar contra HML suíte por suíte antes de considerar pronto** — não basta compilar/passar no parser de sintaxe. Vários bugs reais desta automação só apareceram rodando:
- Cookie de sessão vazando entre testes (`cy.request` sempre envia o cookie jar atual, independente do body) — mascarava falsos-positivos.
- Campo de busca (`getPublicAgents` por nome) não encontrando um registro recém-criado, mesmo com o registro já usável pra login.
- Um `return` faltando num command já existente no repo, nunca detectado porque nenhum teste anterior exercitava aquele caminho.

## 5. Triagem de cada falha (o núcleo do fluxo)

Toda falha ao rodar contra HML é **uma de três coisas** — não presumir qual sem investigar:

1. **Bug no teste** — corrigir (ex.: assert no campo errado, dado de teste mal montado).
2. **Achado real de produto** — o teste está certo, o sistema diverge do que o Termo pede. **Nunca forçar o assert a passar** só pra ficar verde. Documentar (handoff + comentário no código) e reportar pro responsável do produto/backend.
3. **Instabilidade do ambiente** — ver seção 6.

Se um achado real for **contestado por observação manual** (aconteceu no TR 1.24-1.25: o teste automatizado mostrou um bypass de bloqueio de conta, mas o responsável testou manualmente e viu o bloqueio funcionar) — não confiar cegamente em nenhum dos dois lados. Reabrir com um **experimento controlado** (ex.: variar o tempo entre passos, comparar dado bruto da API antes de mudar qualquer asserção).

## 6. Lidar com instabilidade do ambiente

HML deste projeto apresenta com alguma frequência: `503`, `ETIMEDOUT`, timeout de 120s em chamadas GraphQL dentro de `before()`. Antes de insistir:

1. **Checar com `curl` direto** se é queda geral do ambiente ou só a chamada específica falhando (`curl -s -o /dev/null -w "status=%{http_code}\n" <endpoint>`).
2. **Verificar processos órfãos do Cypress/Chrome acumulados** — `ps aux | grep -i cypress`. Um `kill` anterior que só matou o processo pai pode deixar filhos Chrome rodando por horas, consumindo memória e causando timeout em runs seguintes. Limpar (`pkill -9 -f "run-<PID>"` ou padrão equivalente) antes de rodar de novo.
3. **Critério de parada**: 2 falhas seguidas pela mesma causa de instabilidade → parar de insistir, registrar no handoff como pendência, não consumir mais tentativas no mesmo dia.

## 7. Documentação viva

Manter uma nota de handoff (ou equivalente) **atualizada a cada rodada** — status por suíte, achados, correções feitas, pendências. É o que permite retomar sem perder contexto depois de uma reorganização de vault, troca de sessão, ou intervalo de dias. Não deixar o estado "só na cabeça" da sessão atual.

## 8. Antes de subir (commit/MR)

1. Aplicar [[SKILL_REVISAO_AUTOMACAO_E2E]] antes do commit — a checklist original é focada em E2E (seletor de tela, toast); pra testes de API, o equivalente é: padrão de commands/GraphQL cru batendo com os vizinhos, reuso confirmado (nada duplicado), asserts coerentes (status **e** campo de dado relevante), doc atualizada só por acréscimo.
2. **Decidir o que entra no MR e o que fica de fora**: CTs 100% verdes entram sem controvérsia; CTs com causa raiz desconhecida ficam de fora (um vermelho sem explicação no MR gera ruído); CTs que são achados reais confirmados mas ainda sem decisão do responsável — considerar subir com `.skip()` + comentário linkando o achado, preservando o código sem quebrar o CI.
3. Granularidade de commit: por suíte costuma ser mais fácil de revisar do que um commit único gigante.
4. Confirmar que nada da working tree que **não é seu** (mudanças de outra sessão/trabalho paralelo) entrou no stage — `git status` e revisar cada arquivo modificado antes de `git add`.

## Resultado Esperado

Um Termo de Referência sem nenhum caso de teste automatizado vira, de forma repetível e rastreável: CTs gerados e linkados a um card, API real investigada (nunca inventada), testes escritos E validados contra o ambiente real, cada falha corretamente classificada (bug meu / achado real / instabilidade), e um pacote pronto pra revisão e subida — sem surpresa de "por que isso tá vermelho" pro time que for revisar depois.
