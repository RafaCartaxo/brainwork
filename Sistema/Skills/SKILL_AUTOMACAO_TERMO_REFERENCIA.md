---
tags:
  - qa
  - skill
---
# Skill: Automação de Termo de Referência

Levar um **Termo de Referência sem CTs nem card ainda** até um conjunto de testes automatizados validados de verdade contra o ambiente de teste — cobrindo o degrau anterior ao de [[SKILL_INICIAR_AUTOMACAO]] (que já parte de um card validado manualmente): gerar os casos, investigar a API real quando não é conhecida, planejar a massa, codar, VALIDAR rodando (não só escrever), triar cada falha (bug meu × achado real × instabilidade do ambiente) e preparar a subida.

Repo: `~/Documentos/Sogov/sogov-automation-test` (GitLab `qa_sogov/sogov-automation-test`), pacote Playwright em `playwright/`. Fonte de verdade de comandos, execução e regras de escrita: `playwright/README.md` e `playwright/ENVIRONMENTS.md`; no vault, [[00 - Índice da automação Playwright]] e [[01 - Primeiros passos]]. Esta skill não duplica isso.

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Pedido explícito | "automatiza o TR X.YY", "vamos automatizar esse Termo de Referência" |
| Termo de Referência sem CTs ainda | material novo (PDF/descrição) sem casos de teste escritos nem card criado |
| Nova onda de um TR em andamento | "próxima onda de cenários do TR" (ver seção 2) |

## 1. Ponto de partida — gerar os CTs e o card

Diferente de [[SKILL_INICIAR_AUTOMACAO]] (que exige card **já validado manualmente**), aqui normalmente não existe nem CTs nem card ainda:

1. Gerar os casos de teste a partir do Termo ([[SKILL_CASOS_DE_TESTE]] — formato Dado/Quando/Então), organizados em suítes por área/requisito.
2. **Criar/linkar o card (SGV) o quanto antes** — não esperar até o fim da automação pra vincular (aconteceu na automação do TR 1.24-1.25: só foi criado depois de tudo codado, atrasando a rastreabilidade).
3. Confirmar o gate de validação manual (mesmo fluxo de [[SKILL_INICIAR_AUTOMACAO]]) antes de codar qualquer suíte.

## 2. Ciclo por ondas de ~20 CTs

Um TR grande não se automatiza de uma vez. Divide-se em **ondas de ~20 CTs** (o tamanho cresce com o tempo), cada uma entregue de ponta a ponta:

1. **Cada onda tem o seu `01 Automação/01 - Análise`** (template em `Sistema/Templates/Pacote/01 Automação/`), com contexto, decisões técnicas, escopo, fora de escopo, riscos, pendências e a seção **Massa desta entrega**.
2. **A massa herda das ondas anteriores:** a Análise nova linka as anteriores e registra **só o que acrescenta** (atores, módulos, A&S, instâncias, e-mail, exclusivos e seus donos, versão do baseline). Não repetir linhas.
3. **Massa versionada, não pessoal:** ator/módulo/instância que um teste versionado precisa entra no `baseline.ts` (rastreio no código por comentário `// SGV-XXXX · CT-0xx: motivo`; **um incremento de `SEED_SCHEMA_VERSION` por entrega**); quem altera cadastro tem dono em `ownership.ts` e spec `@shared-state`. `massa/<nome>.json` é só iteração local, fora do git.
4. **Mapa CT → teste existente antes de codar:** muitos CTs de um TR já têm cobertura (spec com ID `A##`/`E##`). Registrar na Análise e só escrever o que falta; CT sem nada no código, que depende de job de BI, que dispara e-mail real a cada execução ou cujo comportamento ainda não foi confirmado manualmente vai para **Fora de escopo** com o motivo.
5. **Gate "pronto para planejar"** da Análise fechado → `02 - Plano de automação` → código → `03 - Validação automação`. A onda só fecha com os CTs com resultado atual (ou justificativa) e a massa registrada.

## 3. Fase de investigação técnica (quando a API não é conhecida)

Quando o comportamento a testar depende de uma mutation/query/enum que não está documentada e a **introspection do GraphQL está desabilitada no ambiente** (comum — não insistir tentando de novo):

1. **Perguntar se já existe uma captura salva** (ex.: pasta `~/Downloads/` — foi onde a mudança de status do TR 1.24-1.25 estava, uma captura de API + Recorder do Chrome DevTools + o PDF do Termo) antes de pedir uma nova ao responsável.
2. Se o código do produto estiver no disco (`~/Documentos/Sogov/Sogov-application`), ler a mutation e o enum direto dele; lembrar que o checkout pode estar atrás do ambiente — confirmar o valor com uma chamada real antes de codar.
3. Se não existir, pedir uma captura real (DevTools Network, salvar como HAR, ou o request/response colado) — nunca inventar o shape de uma mutation.
4. Cruzar a ordem dos passos de UI (se houver Recorder) com a ordem das chamadas de API capturadas na mesma sessão pra confirmar mapeamentos não óbvios (ex.: um rótulo de tela que mapeia pra um enum de nome diferente).
5. Registrar o achado na documentação técnica do repo (`playwright/README.md`, `planning/`) ou, se for conhecimento de produto, numa nota de `04 Conhecimento/` — é onde a próxima sessão vai procurar.

## 4. Infraestrutura reaproveitável

Nunca duplicar helper/serviço: procurar antes em `src/api/services/*`, `src/ui/internal/*`, `src/fixtures/index.ts` e nos specs do domínio. Preparo de massa dentro do teste é **por API**; só a ação avaliada passa pela UI. Usar o ator padrão do worker (`actors.agent()`), e **atores exclusivos e dedicados por cenário** quando o teste altera cadastro — nunca bloquear, inativar ou mudar status do ator compartilhado (quebra os outros specs; o `parallel-safety.spec.ts` reprova uso fora do dono).

Gotchas confirmados: nome de servidor de teste tem limite de tamanho no backend (`exceed-max-length`) — manter curto; nome de módulo recusa a partir de ~30 caracteres; CPF/e-mail de usuário são únicos no ambiente inteiro (bloqueio de login é da pessoa, em todas as instâncias).

## 5. Escrever e VALIDAR de verdade

Escrever os testes seguindo `playwright/README.md` (seção de regras de escrita). **Rodar contra o ambiente suíte por suíte antes de considerar pronto** — não basta compilar. Vários bugs reais desta automação só apareceram rodando:
- Sessão vazando entre testes (aqui, cada ator abre o próprio contexto — nunca logout/login na mesma página) mascarando falsos-positivos.
- Campo de busca (`getPublicAgents` por nome) não encontrando um registro recém-criado, mesmo com o registro já usável pra login.
- Helper com `return` faltando, nunca detectado porque nenhum teste anterior exercitava aquele caminho.

## 6. Triagem de cada falha (o núcleo do fluxo)

Toda falha ao rodar contra o ambiente é **uma de três coisas** — não presumir qual sem investigar:

1. **Bug no teste** — corrigir (ex.: assert no campo errado, dado de teste mal montado).
2. **Achado real de produto** — o teste está certo, o sistema diverge do que o Termo pede. **Nunca forçar o assert a passar** só pra ficar verde. Atualizar o resultado e a observação do CT em [[../Templates/Pacote/01 Automação/03 - Validação automação]] e reportar pro responsável do produto/backend. No código, o caso é marcado `[BUG DE PRODUTO]` com `test.fail()` imediatamente antes da asserção do bug, com comentário explicando a divergência.
3. **Instabilidade do ambiente** — ver seção 7.

Se um achado real for **contestado por observação manual** (aconteceu no TR 1.24-1.25: o teste automatizado mostrou um bypass de bloqueio de conta, mas o responsável testou manualmente e viu o bloqueio funcionar) — não confiar cegamente em nenhum dos dois lados. Reabrir com um **experimento controlado** (ex.: variar o tempo entre passos, comparar dado bruto da API antes de mudar qualquer asserção).

## 7. Lidar com instabilidade do ambiente

O ambiente de teste apresenta com alguma frequência: `503`, `ETIMEDOUT`, timeout de GraphQL. Antes de insistir:

1. **Checar com `curl` direto** se é queda geral do ambiente ou só a chamada específica falhando (`curl -s -o /dev/null -w "status=%{http_code}\n" <endpoint>`).
2. **Verificar processos órfãos de browser/Playwright** — `ps aux | grep -i "chrom\|playwright"`. Um `kill` que só matou o processo pai pode deixar filhos Chromium rodando por horas, consumindo memória e causando timeout em runs seguintes. Limpar antes de rodar de novo. Lembrar: duas execuções simultâneas no mesmo ambiente/pasta não são suportadas.
3. **Não rodar a suíte inteira de uma vez** (satura o gerador de PDF do backend e gera falhas que não são bugs reais): ir por domínio, em lotes de 15–20 min.
4. **Critério de parada**: 2 falhas seguidas pela mesma causa de instabilidade → parar de insistir, marcar os CTs afetados como bloqueados em [[../Templates/Pacote/01 Automação/03 - Validação automação]] e registrar em [[../Templates/Pacote/01 Automação/00 - Automação]] a causa e próxima ação. Não consumir mais tentativas no mesmo dia.

## 8. Documentação viva

Manter os quatro registros do pacote de automação coerentes, sem criar um diário por rodada:

- [[../Templates/Pacote/01 Automação/00 - Automação|00 - Automação]]: status geral, próxima ação, bloqueios gerais e link de entrega.
- [[../Templates/Pacote/01 Automação/01 - Análise|01 - Análise]]: contexto, decisões, escopo da onda, riscos e **massa desta entrega**; atualizar quando a decisão mudar, nunca como log de investigação.
- [[../Templates/Pacote/01 Automação/02 - Plano de automação|02 - Plano de automação]]: estratégia por suíte e decisões de construção antes de codar; revisar somente quando o plano mudar.
- [[../Templates/Pacote/01 Automação/03 - Validação automação|03 - Validação automação]]: resultado mais recente por CT; sobrescrever o estado anterior a cada execução.

Achado técnico duradouro vai para a documentação técnica correspondente no repositório; bug de produto segue o fluxo de bug; andamento e próxima ação ficam no registro de trabalho do dia. Criar um handoff separado somente quando uma continuidade complexa não puder ser entendida com esses registros e os links para as fontes.

## 9. Antes de subir (commit/MR)

1. Aplicar [[SKILL_REVISAO_AUTOMACAO_E2E]] e [[SKILL_REVISAO_CODIGO_AUTOMACAO]] antes do commit; rodar `npm run verify` (typecheck, lint, knip, independência, infra, audit). Pra testes de API, o equivalente da checklist de e2e é: padrão de serviços/GraphQL batendo com os vizinhos, reuso confirmado (nada duplicado), asserts coerentes (status **e** campo de dado relevante), doc atualizada só por acréscimo.
2. **Decidir o que entra no MR e o que fica de fora**: CTs 100% verdes entram sem controvérsia; CTs com causa raiz desconhecida ficam de fora (um vermelho sem explicação no MR gera ruído); CTs que são achados reais confirmados mas ainda sem decisão do responsável — subir como `[BUG DE PRODUTO]` com `test.fail()` ou com skip e `annotation` tipada linkando o achado, preservando o código sem quebrar a execução.
3. **Mudou o `baseline.ts`?** Confirmar o comentário de rastreio `// SGV-XXXX · CT-0xx`, o dono em `ownership.ts`, o incremento de `SEED_SCHEMA_VERSION` (um por entrega) e a linha na tabela de massa da Análise.
4. Granularidade de commit: por suíte costuma ser mais fácil de revisar do que um commit único gigante.
5. Confirmar que nada da working tree que **não é seu** (mudanças de outra sessão/trabalho paralelo) entrou no stage — `git status` e revisar cada arquivo modificado antes de `git add`.

## Resultado Esperado

Um Termo de Referência sem nenhum caso de teste automatizado vira, de forma repetível e rastreável, uma sequência de **ondas de ~20 CTs**, cada uma com: CTs gerados e linkados a um card, API real investigada (nunca inventada), **Análise com massa registrada (com dono e risco de e-mail), herdando as ondas anteriores**, testes escritos E validados contra o ambiente real, cada falha corretamente classificada (bug meu / achado real / instabilidade), e um pacote pronto pra revisão e subida — sem surpresa de "por que isso tá vermelho" nem de "de onde veio esse dado" pro time que for revisar depois.
