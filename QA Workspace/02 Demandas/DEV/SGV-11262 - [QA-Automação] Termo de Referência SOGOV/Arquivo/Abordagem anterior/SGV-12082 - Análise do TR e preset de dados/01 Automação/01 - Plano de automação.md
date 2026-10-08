---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: "sogov-automation-playwright"
status: planejado
---

# Plano de automação — SGV-12082

> [!info]- Navegação QA
> **README:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos de análise:** [[../00 QA/03 - Casos de teste]]
> **Matriz:** [[../00 QA/Matriz - Análise do preset provável]]
> **Fluxo do preset:** [[../00 QA/Fluxo - Preset de dados]]
> **Automação:** [[00 - Automação]]
> **Validação:** [[02 - Validação automação]]

> [!settings]- Controle do plano
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Plano de investigação técnica que segue a estrutura do template. A implementação só será planejada em entrega posterior, depois da decisão baseada em evidências.

## Objetivo e escopo

- **Objetivo:** entender como o projeto prepara e consome massa, avaliar reaproveitamento entre ambientes e recomendar o preset provável que atende aos requisitos do TR validáveis por automação/dados, relacionando evidências para os demais.
- **CTs incluídos:** verificações DISC-001–DISC-004; elas analisam o PDF completo e a automação existente. CT-001–CT-038 são casos existentes apenas dos requisitos 1.24–1.25, sem criar novos CTs funcionais.
- **Fora do escopo:** editar/executar o seed, alterar dados/instâncias e portar os CTs restantes.

## Estratégia por suíte

| Suíte / CTs | Camada | Dados e estado inicial | Reuso / mudança necessária | Dependência ou gate |
|---|---|---|---|---|
| DISC-001 — arquitetura | Repositório/documentação | Configuração Playwright, setup, provisionamento, manifesto e fixtures | Descrever capacidades existentes; não alterar código | Acesso de leitura ao repositório e definição do commit analisado |
| DISC-002 — cobertura do TR e dos 38 CTs existentes | Requisitos + casos/testes | Requisitos do PDF; atores, entidades, estados e operações dos CTs 1.24–1.25 | Classificar cobertura/evidência do TR e cruzar os casos existentes com código; agrupar só com justificativa | PDF integral e fonte dos 38 CTs; validar estado atual de cada suíte |
| DISC-003 — dados/ambientes | Configuração + dados | Endpoints, credenciais (nomes, sem valores), disponibilidade e isolamento | Distinguir parametrização existente de portabilidade comprovada | Configuração segura/documentação ou evidência registrada por ambiente |
| DISC-004 — recomendação | Síntese da matriz | Conjunto mínimo de dados/estados e restrições | Comparar opções sem presumir refatoração do seed | DISC-001–003 revisados |

## Pronto para codar quando

- [ ] Os requisitos do TR estão classificados; os testes/dados existentes e as lacunas de cobertura estão rastreados, incluindo análise detalhada dos 38 CTs de 1.24–1.25.
- [ ] Os ambientes relevantes e as lacunas de evidência estão identificados.
- [ ] O preset provável tem escopo mínimo, dependências, isolamento e forma de validação descritos.
- [ ] Refatorar seed, parametrizar configuração ou manter mecanismo atual foram comparados com evidências.

## Pronto para validar quando

- [ ] Mapa, matriz, recomendação e sequência de entregas candidatas estão revisados.
- [ ] Cada recomendação aponta para CTs e fontes verificáveis.
- [ ] Nenhum resultado documental é apresentado como execução em ambiente.

---

## Decisão de sequenciamento (Codex + Claude, alinhado com o Rafael, 07/10/2026)

Depois do DISC-001, o Codex (planejador) e o Claude (execução) alinharam uma reordenação do DISC-002, com 4 ressalvas acordadas:

1. **"Ambiente" deixou de ser um termo único** — separado em **ambiente de implantação** (dev/hml/prod, backend/URLs) e **cliente/instância/tenant** (ex.: instância 225). Ver [[../00 QA/DISC-003 - Dados, preparação e eixos#Dois eixos que não podem virar um termo só|seção do DISC-003]].
2. A tabela "O que os 13 CTs consomem" do [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] foi reaproveitada como base, não refeita do zero.
3. Só o observado em execução real conta como **Confirmado**; reuso entre ambientes/instâncias é **Inferido** até teste explícito — nenhum teste foi rodado nesta rodada.
4. **Prioridade reordenada, não reduzida**: os 13 CTs Playwright (execução atual, já reconciliada nesta análise contra o commit `16c41e4`) entram primeiro, de rastreabilidade profunda — **correção de 07/10/2026**: não é mais o único recorte com "execução verde" alegada, já que o DISC-002 encontrou relatos históricos de execução verde em Cypress pra mais 22 CTs (não revalidados, branch não mesclado). CT-013–037 (Suítes 3/4) continuam no critério de saída C2 — ficam pendentes por sequenciamento, não removidos.

**Entregue nesta rodada:** grafo CT→pré-condição→dados/configuração→mutação→lacuna dos 13 CTs Playwright, no [[../00 QA/DISC-002 - Cobertura do TR e rastreabilidade dos CTs#Grafo confirmado — os 13 CTs Playwright (CT-001–012, CT-038)|DISC-002]]. Zero divergência da tabela equivalente do Mapa do seed. **Evidência não é uniforme** (corrigido após revisão do Codex): CT-001–012 reconciliados contra o commit `16c41e4`; CT-038 é untracked no worktree, evidência é a execução manual confirmada contra o estado atual (não commitado), não contra `16c41e4`.

> [!info] Pausa de 07/10 (concluída) — Codex/Rafael revisaram, encontraram 2 inconsistências (contagem 24→25, evidência do commit não cobrindo CT-038), corrigidas, e autorizaram prosseguir pro recorte completo abaixo.

## DISC-002 concluído — síntese dos 38 CTs (07/10/2026)

**38/38 rastreados** no [[../00 QA/DISC-002 - Cobertura do TR e rastreabilidade dos CTs#CT-013 a CT-037 (exceto CT-038) — decomposto em 07/10/2026|DISC-002]]. Três categorias de evidência, nenhuma delas "pronta pra proteger pipeline hoje":

| Categoria | CTs | Onde está o código | O que falta |
|---|---|---|---|
| Playwright, commit atual | CT-001–012 | `16c41e4` (HEAD do worktree `sogov-automation-playwright`) | Nada — já roda no `api` project |
| Playwright, não commitado | CT-038 | Worktree, untracked | Decidir branch e commitar |
| Cypress, branch local não mesclado | CT-013,014,015,018,019,020–036 (22 CTs) | Commit `bdf5e9a`, branch `tr-1.24-1.25-suites-3-4-5`, checked out no worktree **`sogov-automation-test`** | Portar pra Playwright (alvo atual). Sobre CI: branch **não mesclado**; `.gitlab-ci.yml` roda o job `e2e-tests` automaticamente só em push pra `main` (`$CI_COMMIT_BRANCH == "main"`), mas as `rules` também permitem `$CI_PIPELINE_SOURCE == "trigger"` (API) ou `"web"` (disparo manual pela interface) em **qualquer branch** — não verifiquei nesta análise se algum pipeline chegou a rodar nesta branch especificamente, só que a configuração permite |
| Sem código em nenhum framework | CT-016, CT-017, CT-037 | — | Captura de API/endpoint (desbloqueio e auditoria) — bloqueio de produto, não de teste |

**Achado mais relevante pro preset** (dos 22 CTs em `bdf5e9a`): a Suíte 4 inteira já usa exatamente o padrão de "agente de teste isolado + mutação de status via `changePublicAgentWorkStatus`" que a seção de Preset deste mesmo Plano (ver "Estratégia por suíte" acima) já tinha identificado como necessário — só que em Cypress, não Playwright. Portar esse código (não reinventar a lógica) é provavelmente o caminho mais barato pra Suíte 4.

**Achados de produto já documentados no código** (achados reais, não bugs de teste — preservados pra DISC-004 não redescobrir): CT-015 (conta bloqueada aceita login com senha correta — contradiz o Termo), CT-033 (mecanismo de revogação de token não confirmado), CT-022/CT-028 (busca por nome às vezes não encontra agente recém-criado), CT-034/CT-036 (atraso de propagação não explicado entre mudança de status e efeito).

## DISC-003 — síntese (07/10/2026)

Detalhe completo (mapa de reutilização, tabela por dado/estado, eixos, pressupostos e perguntas em aberto) vive no [[../00 QA/DISC-003 - Dados, preparação e eixos#DISC-003 — Dados, preparação e diferenças por eixo (07/10/2026)|DISC-003]]. Resumo:

- **Achado principal**: Playwright e Cypress usam **o mesmo nome fixo de instância** (`"E2E Automatic Test"`) — confirmado lendo `cypress/support/e2e.js:78` (`instanceName` hardcoded) contra `src/data/seed/baseline.ts`. **Correção de precisão (07/10/2026)**: isso é "mesmo nome", não "mesma instância confirmada" — a identidade real do alvo (se os dois `.env`/`cypress.env*.json` apontam pro mesmo backend/registro, ou só coincidem no nome) **não foi verificada**, porque isso exigiria comparar valores de configuração, não só código. **Nenhum dos dois frameworks tem hoje um parâmetro de `clienteId`/instância alternativa** — não é uma lacuna só do Playwright, é dos dois.
- A mutation de mudança de estado de conta (`changePublicAgentWorkStatus`) e o padrão de agente isolado por cenário (`createIsolatedTestAgent`) só existem no lado Cypress — é a peça que, portada, destrava qualquer preset de estado pra Playwright.
- Cypress reescreve um **único arquivo fixo** de manifesto (`cypress.env.set.json`) a cada run; Playwright isola por `runId`. Rodar os dois frameworks ao mesmo tempo contra o mesmo ambiente não tem proteção cruzada conhecida — não testado.
- Credenciais e dependência de Gmail seguem o mesmo padrão conceitual nos dois frameworks, só com nomes de variável diferentes (`PW_*` vs. sem prefixo) — não comparei valores (segredo), só nomes de chave.

Nenhum teste foi rodado, nenhuma configuração foi alterada nesta verificação.

## DISC-004 — Síntese e recomendação (07/10/2026)

Detalhe completo (comparação de alternativas, entregas sequenciadas com CTs/dependências/aceite/risco) vive no [[../00 QA/DISC-004 - Alternativas e recomendação#DISC-004 — Comparação de alternativas e recomendação (07/10/2026)|DISC-004]]. Resumo:

> [!info] Natureza desta seção
> Só recomendação documental — nenhuma implementação, execução ou pasta/demanda criada. O Rafael decide se aprova, ajusta ou rejeita.

- **Recomendação:** portar pro Playwright os mecanismos de estado que já existem confirmados em Cypress (`changePublicAgentWorkStatus`, `createIsolatedTestAgent`), mantendo a instância fixa atual — **não** começar pela seleção de cliente/instância (isso é a última etapa do Roadmap, não a primeira, e nenhum CT de estado existe ainda pra validar essa seleção contra).
- **6 entregas candidatas, sequenciadas** (nenhuma aberta como pasta ainda — correção de contagem de 07/10/2026, eram listadas como 5 antes de separar a entrega de flakiness): (1) portar bloqueio limpo — CT-013/014/018/019; (2) resolver com produto o achado do CT-015 antes de portá-lo; (3) portar ciclo de vida **sem nenhuma lacuna conhecida** — CT-020/021/023/024/026/027/031/035 (8 CTs); (4) portar com **gate de timeout explícito pra instabilidade de teste** (hipótese de flakiness a validar na execução, não disputa de produto — se o teto for excedido de forma consistente, vira achado, não é mascarado) — CT-022/028 (busca por nome instável) e CT-036 (atraso de propagação); (5) resolver achados de **produto** antes de portar — CT-025/033 (mesma pergunta: ação após mudança de status com token antigo), CT-032/034 (dependem da mesma sequência de agente do CT-033) e a discrepância de fonte do CT-029/030; (6) trilha **separada e não bloqueante** — desenhar seleção segura da instância 225. **CT-016/017/037 (sem código) não entram nessa contagem** — ficam à parte, sem porte previsto.
- **Correção de 07/10/2026 (revisão do Codex, duas rodadas)**: a Entrega 3 original rotulava CT-022/025/028/036 como "sem achado em disputa", mas o próprio código (e minhas notas na Matriz) já documentavam instabilidade/achado pra esses 4 — movidos pra uma Entrega 4 própria (os 2 de flakiness, com gate de timeout explícito) e pra Entrega 5 (CT-025, que compartilha a pergunta de produto do CT-033). Regra agora explícita: nenhum CT com achado conhecido fica implícito num grupo "limpo".
- **Fora de escopo, sem porte previsto:** CT-016, CT-017, CT-037 — bloqueio de produto/backend (endpoint/mutation nunca confirmados), não lacuna de automação.
- **Achado de discrepância não resolvido, registrado para o Rafael decidir:** o código real de CT-029/030 não mostra nenhum achado (espelham CT-023/024, "limpos"), mas o placar histórico da SGV-11971 lista os dois junto com CT-015/033 como "falha/achado" — as duas fontes divergem e não escolhi uma sozinho.

Quando este DISC-004 for revisado e aprovado, as entregas futuras nascem do template de demanda (pacote `00 QA/` + `01 Automação/`), uma de cada vez — regra já combinada, não alterada aqui.

---

## DISC-001 — Auditoria do projeto, reconciliada com o código (07/10/2026)

> [!success] Commit analisado
> `16c41e4` (HEAD do worktree `sogov-automation-playwright`, detached — sem branch). Único item não commitado no repo: `playwright/tests/api/auth/audit-sessions.spec.ts` (untracked, CT-038/A55-C01, já confirmado passando).

**Fluxo confirmado, ponta a ponta** (configuração/comandos → setup e seed → provisionamento/manifesto → fixtures/pools → specs):

1. **`playwright.config.ts`** — 5 projects: `infrastructure` (sem dependência), `seed` (`tests/setup/seed.setup.ts`), `e2e-chromium`/`version`/`api` (todos `dependencies: ['seed']`).
2. **`config/env.ts`** (não `src/config/env.ts` — correção de um erro de caminho que eu tinha anotado antes) — parseia só variáveis `PW_*` (URLs, credenciais, `PW_RUN_ID`, `PW_WORKERS`). Nenhum parâmetro de cliente/instância.
3. **`tests/setup/seed.setup.ts`** — entry point do project `seed`: abre sessão admin, chama `provisionBaseline`, grava o manifesto.
4. **`src/data/seed/baseline.ts`** (`BASELINE`) — contei linha a linha contra o código: **15 módulos** (14 no objeto `modules` + 1 em `subsectors.module`), **12 serviços**, **29 servidores nomeados**, **5 cidadãos nomeados**, pools de 4 (servidor/cidadão PJ/cidadão alfanumérico). Bate exatamente com o [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] — **nenhuma divergência encontrada**.
5. **`src/data/seed/provision.ts`** (`provisionBaseline`) — orquestra na ordem: instância → setores (GP/SCTA/DIR) → módulos → serviços → árvore de subsetores (+ módulo dedicado) → servidores → cidadãos → workflows. Idempotente por identidade natural (nome/CPF/CNPJ), revalida pela API a cada execução.
6. **`src/data/seed/manifest.ts`** — `SEED_SCHEMA_VERSION = 12` (confirmado no código), grava `.runtime/<runId>/seed-manifest.json`.
7. **`src/data/seed/pool.ts`** (`bindWorkerActors`) — troca os atores padrão (`agents.agent`, `citizens.citizen`, `citizens.alphanumeric`) pelo slot do worker (`parallelIndex`).
8. **`src/fixtures/index.ts`** — `env`/`seed`/`actors`/`cleanup`/`diagnostics`/`pace`; `actors.*` resolvem `instanceId = seed.instance.id` internamente, nunca de variável de ambiente.
9. **Specs de autenticação** (`tests/api/auth/{login,credentials,audit-sessions}.spec.ts`) — sem mudança desde a última leitura; continuam usando só `seed.agents.agent`/`seed.citizens.citizen` (pool), sem módulo/serviço/documento.

**Achado lateral, fora do escopo de DISC-001 mas relevante pra DISC-002/matriz (corrigido após revisão do Codex):** os servidores `seqBasic`/`seqSpecialist`/`seqSectorAdmin`/`seqAdmin` em `baseline.ts` usam `accessLevel` 2/3/4/5 respectivamente — mapeiam **4 dos 5 níveis**: Usuário básico=2, Especialista=3, Administrador setorial=4, Administrador=5. Busquei no código (`grep accessLevel` em `baseline.ts` e `factories/seed.ts`) e **não há nenhum agente com `accessLevel: 1`**, nem nome "Visualizador"/"Somente leitura" em lugar nenhum do seed. Ou seja: **o 5º nível (Somente leitura) não tem representante no baseline hoje** — confirmado, não presumido. Isso é uma lacuna real pro preset, não só um "falta achar": se algum CT de 1.25.3.x precisar de um servidor Somente leitura, essa identidade precisa ser criada, não já existe pronta.

**Conclusão do DISC-001:** o mapa técnico existente (`Mapa do seed Playwright atual - SGV-11971.md`) está correto e atualizado contra o commit `16c41e4` — não precisou de correção, só desta reconciliação registrada.

---

**Execução direta:** nesta entrega, “pronto para validar” significa revisão da análise e rastreabilidade; não significa código ou execução funcional.
