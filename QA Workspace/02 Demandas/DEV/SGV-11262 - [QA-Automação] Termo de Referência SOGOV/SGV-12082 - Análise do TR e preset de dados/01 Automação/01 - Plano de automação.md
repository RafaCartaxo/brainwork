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

1. **"Ambiente" deixou de ser um termo único** — separado em **ambiente de implantação** (dev/hml/prod, backend/URLs) e **cliente/instância/tenant** (ex.: instância 225). Ver [[../00 QA/Matriz - Análise do preset provável#Dois eixos que não podem virar um termo só|seção da Matriz]].
2. A tabela "O que os 13 CTs consomem" do [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] foi reaproveitada como base, não refeita do zero.
3. Só o observado em execução real conta como **Confirmado**; reuso entre ambientes/instâncias é **Inferido** até teste explícito — nenhum teste foi rodado nesta rodada.
4. **Prioridade reordenada, não reduzida**: os 13 CTs Playwright (único recorte com execução verde real) entram primeiro, de rastreabilidade profunda. CT-013–037 (Suítes 3/4) continuam no critério de saída C2 — ficam pendentes por sequenciamento, não removidos.

**Entregue nesta rodada:** grafo CT→pré-condição→dados/configuração→mutação→lacuna dos 13 CTs Playwright, na [[../00 QA/Matriz - Análise do preset provável#Grafo confirmado — os 13 CTs Playwright (CT-001–012, CT-038)|Matriz]]. Zero divergência da tabela equivalente do Mapa do seed. **Evidência não é uniforme** (corrigido após revisão do Codex): CT-001–012 reconciliados contra o commit `16c41e4`; CT-038 é untracked no worktree, evidência é a execução manual confirmada contra o estado atual (não commitado), não contra `16c41e4`.

> [!info] Pausa de 07/10 (concluída) — Codex/Rafael revisaram, encontraram 2 inconsistências (contagem 24→25, evidência do commit não cobrindo CT-038), corrigidas, e autorizaram prosseguir pro recorte completo abaixo.

## DISC-002 concluído — síntese dos 38 CTs (07/10/2026)

**38/38 rastreados** na [[../00 QA/Matriz - Análise do preset provável#CT-013 a CT-037 (exceto CT-038) — decomposto em 07/10/2026|Matriz]]. Três categorias de evidência, nenhuma delas "pronta pra proteger pipeline hoje":

| Categoria | CTs | Onde está o código | O que falta |
|---|---|---|---|
| Playwright, commit atual | CT-001–012 | `16c41e4` (HEAD do worktree `sogov-automation-playwright`) | Nada — já roda no `api` project |
| Playwright, não commitado | CT-038 | Worktree, untracked | Decidir branch e commitar |
| Cypress, branch local não mesclado | CT-013,014,015,018,019,020–036 (22 CTs) | Commit `bdf5e9a`, branch `tr-1.24-1.25-suites-3-4-5`, checked out no worktree **`sogov-automation-test`** | Portar pra Playwright (alvo atual) — o Cypress não roda em nenhuma CI porque não está na `main` |
| Sem código em nenhum framework | CT-016, CT-017, CT-037 | — | Captura de API/endpoint (desbloqueio e auditoria) — bloqueio de produto, não de teste |

**Achado mais relevante pro preset** (dos 22 CTs em `bdf5e9a`): a Suíte 4 inteira já usa exatamente o padrão de "agente de teste isolado + mutação de status via `changePublicAgentWorkStatus`" que a seção de Preset deste mesmo Plano (ver "Estratégia por suíte" acima) já tinha identificado como necessário — só que em Cypress, não Playwright. Portar esse código (não reinventar a lógica) é provavelmente o caminho mais barato pra Suíte 4.

**Achados de produto já documentados no código** (achados reais, não bugs de teste — preservados pra DISC-004 não redescobrir): CT-015 (conta bloqueada aceita login com senha correta — contradiz o Termo), CT-033 (mecanismo de revogação de token não confirmado), CT-022/CT-028 (busca por nome às vezes não encontra agente recém-criado), CT-034/CT-036 (atraso de propagação não explicado entre mudança de status e efeito).

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
