---
tags: [qa, automacao, dados, matriz]
task: SGV-12082
pai: SGV-11262
tipo: matriz-analise
status: em levantamento
---
# Matriz — análise do preset provável para o TR

> [!info] Propósito
> Esta matriz vai da regra/caso aos dados e ao mecanismo atual de preparação. Ela deve orientar a recomendação do preset inicial; não é um catálogo geral do SOGOV nem uma especificação aprovada de seed.
>
> **Fonte funcional:** [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste|38 CTs da SGV-11971]] · **Demanda:** [[01 - Demanda]] · **Plano:** [[02 - Plano de teste]] · **Roadmap:** [[../../Roadmap - Automação TR|Automação TR]]

## Como preencher

- Use uma linha por CT quando as pré-condições ou dados diferirem; agrupe apenas quando ator, estado e preparação forem iguais.
- Para cada afirmação, registre a fonte (caso, arquivo, configuração ou execução existente).
- Use **Confirmado**, **Inferido** ou **A confirmar**. Não transforme lacuna em fato.
- Não copiar valores secretos. Registre apenas nomes de variáveis/chaves e onde a configuração deve ser verificada.

## Legenda de estado do conhecimento

| Estado | Significado |
|---|---|
| Confirmado | Visível diretamente no CT/código/documento ou em execução já registrada |
| Inferido | Interpretação provável que ainda precisa de validação |
| A confirmar | Evidência ausente, ambiente inacessível ou comportamento não verificado |

## Dois eixos que não podem virar um termo só

> [!important] Decisão de planejamento (Codex + Claude, 07/10/2026)
> **"Ambiente" é genérico demais e não entra mais sozinho nesta matriz.** Dois eixos diferentes, com evidência de naturezas diferentes:
> - **Ambiente de implantação** — dev/hml/prod: backend e URLs diferentes (`PW_BASE_URL`/`PW_GRAPHQL_URL`/`PW_AUTH_URL`). Hoje só há **um** configurado e usado de fato.
> - **Cliente/instância/tenant** — ex.: a instância do baseline do seed, ou a instância 225 criada em 07/10/2026. Mesmo backend, tenant diferente (`x-tenant`/`instanceId`).
>
> Reuso entre um e outro são afirmações **separadas**. Nesta rodada, registrar como **Confirmado** só o que foi observado rodando (há uma configuração de backend atual, usada pelos 13 CTs); capacidade de reproduzir em outro ambiente de implantação ou noutra instância/tenant fica **Inferida** até teste explícito — não executar nada pra "confirmar" isso agora.

## Matriz de cobertura do TR completo

Esta visão cobre os requisitos do PDF (1.1–1.43). As linhas agrupam requisitos correlatos para orientar a investigação; subitens específicos devem ser desmembrados quando tiverem cobertura, dados ou evidências diferentes. **Os 38 CTs atuais cobrem os itens 1.24–1.25 apenas.**

> [!success] Verificação contra o PDF de origem (07/10/2026)
> **Fonte:** `Downloads/SGV-12082/Requisitos Sogov.pdf` (20 páginas, itens 1.1 a 1.43 — é mais completo que o PDF usado em 31/08/2026 pra conferir o ciclo 1.24-1.25, que ia só até o item 1.26). Lido por inteiro e conferido item a item contra a tabela abaixo: os intervalos descritos em cada linha (1.1–1.23, 1.26 a 1.43) batem com o conteúdo real do PDF — nenhuma linha precisou ser corrigida na descrição de escopo.
>
> **Confirmado, palavra por palavra**: os itens 1.24, 1.25 (incluindo 1.25.1 a 1.25.3.4), 1.27.10.1 e 1.27.11.2/1.27.11.4 batem exatamente com o texto citado em C1–C16 do [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/01 - Demanda|01 - Demanda da SGV-11971]] — a checagem de 31/08 se confirma também nesta versão mais completa do documento.
>
> **✅ Discrepância resolvida — níveis de permissão (CT-020), confirmado pelo Rafael em 07/10/2026:** o item **1.27.2** do PDF lista os nomes de rascunho (`Administrador`, `Administrador setorial`, `Assistente administrativo`, `Auxiliar administrativo`, `Visualizador`), mas o produto real usa **`Administrador`, `Administrador setorial`, `Especialista`, `Usuário básico`, `Somente leitura`** — os 2 níveis administrativos de topo mantiveram o nome do Termo; os 3 operacionais de baixo foram renomeados no produto (Assistente administrativo → Especialista, Auxiliar administrativo → Usuário básico, Visualizador → Somente leitura). São **5 níveis**, não 3 — a decisão anterior da SGV-11971 ("Especialista/Usuário básico/Somente leitura, confirmado em 4 fontes") capturou só os 3 operacionais, sem registrar os 2 administrativos de topo. Vale atualizar o `01 - Demanda` da SGV-11971 (CT-020) pra refletir os 5 nomes completos.

| Itens do TR | Área/requisito | Automação/evidência atual a localizar | Massa/preset a investigar | Situação |
|---|---|---|---|---|
| 1.1–1.23 | Infraestrutura, hospedagem, disponibilidade, banco de dados, rede, e-mail, segredos, segurança, armazenamento, filas, criptografia e monitoramento | Requisitos predominantemente técnicos/operacionais; confirmar se há testes no projeto e qual evidência os valida | Não presumir preset de dados; mapear dependências ambientais e evidência exigida | A confirmar |
| 1.24–1.25 | Autenticação e ciclo de vida da identidade funcional | 38 CTs existentes na SGV-11971; 13 localizados em Playwright (CT-001–012, CT-038); estado dos demais deve ser reconciliado | Seed global, fixtures/pools e credenciais do ambiente; detalhes no mapa atual do seed | Parcialmente conhecido; portabilidade entre ambientes não demonstrada |
| 1.26 | Organograma, setores/subsetores, suspensão, hierarquia e permissões de setor | Localizar cobertura existente; não assumir que os CTs de 1.24–1.25 cobrem este requisito | Seed declara setores/subsetores; dependência por teste e estado de execução a mapear | A confirmar |
| 1.27 | Cadastro de servidores, 5 níveis (nomes do produto, confirmado pelo Rafael: Administrador, Administrador setorial, Especialista, Usuário básico, Somente leitura — item 1.27.2 do PDF tinha nomes de rascunho pros 3 operacionais, ver achado acima), permissões extras, convites, listagem e ciclo de vida | Localizar testes e separar atores/papéis necessários pelos 5 níveis reais | Seed declara muitos servidores e perfis; relação com testes/TR a mapear | Requisito e nomenclatura confirmados; automação/massa por nível segue a confirmar |
| 1.28 | Gerenciamento de serviços/assuntos e campos configuráveis | Localizar testes que criam ou consomem serviços/assuntos | Seed declara serviços; dependências, configuração por ambiente e reuso a mapear | A confirmar |
| 1.29 | Categorias de documentos e módulos, formulários e zoneamento | Localizar suítes e dados dependentes por categoria | Seed declara módulos; determinar subconjunto realmente consumido | A confirmar |
| 1.30 | Fluxos de trabalho e etapas | Localizar testes e estados de workflow exigidos | Seed declara três workflows; mapear correspondência, estabilidade e reset | A confirmar |
| 1.31 | Modelos simples e automatizados de documentos | Localizar testes, modelos e documentos próprios do teste | Mapa atual aponta que o seed não fornece massa-base de documentos para os CTs de autenticação; demais suítes a investigar | A confirmar |
| 1.32 | Cadastro de contatos externos e notificação por e-mail | Localizar testes, identidade externa e requisitos de caixa de e-mail | Seed declara cidadãos; mapear contatos, e-mail e limitações de ambiente | A confirmar |
| 1.33 | Mesa de trabalho, filas, visões, alertas e busca | Localizar testes e massa de documentos/atribuições | Mapear dependências de setores, documentos, estados, datas e usuários | A confirmar |
| 1.34 | Etiquetas e aplicação/compartilhamento por setor | Localizar testes e relações com documentos/setores | A verificar no seed e nos dados criados pelos testes | A confirmar |
| 1.35 | Tramitação, histórico e estados de documentos/processos | Localizar testes, transições, prazos e limpeza | Mapear documentos, workflows, setores e atores; verificar isolamento e reset | A confirmar |
| 1.36–1.37 | Central de atendimento e acompanhamento por usuários externos | Localizar fluxos externos e identidades PF/PJ | Seed declara cidadãos; mapear cadastro, solicitações e massa entre ambientes | A confirmar |
| 1.38 | Divulgação/publicação de documentos (jornal/transparência) | Localizar testes, permissões, estado de publicação e documentos | A verificar no seed e nos dados próprios de cada teste | A confirmar |
| 1.39 | Exportação e impressão de documentos/processos | Localizar formatos, tamanho e dados documentais exigidos | Mapear documentos/árvore processual e dependências de armazenamento | A confirmar |
| 1.40 | Assinaturas eletrônicas/digitais e solicitações | Localizar atores, tipos, ordem e estado de assinatura | Seed lista perfis relacionados a assinatura; confirmar consumo, configuração e dependências externas | A confirmar |
| 1.41 | Chaves de acesso e criação delegada | Localizar permissões, limites, documentos e ciclo de vida da chave | Seed declara módulo accessKey e servidor dedicado; confirmar cobertura e massa exigida | A confirmar |
| 1.42 | Personalização e identidade visual do órgão | Localizar testes e dados de configuração do cliente | Provável configuração da instância; validar se automatizável e se pertence ao preset | A confirmar |
| 1.43 | Estatísticas de uso, setores, documentos, servidores e recursos | Localizar testes e massa agregada necessária aos cálculos | Mapear volume, variedade e consistência dos dados; avaliar se seed é apropriado | A confirmar |

## Detalhamento dos 38 CTs de 1.24–1.25

A tabela acima não substitui o mapeamento caso a caso. Para cada CT-001–CT-038, cruzar cenário/pré-condição com código Playwright/Cypress ou execução manual, identificando ator, identificador, status inicial, preparação, mutação/limpeza, credenciais/configuração e evidência. O estado prévio dos CTs deve ser revalidado; não inferir resultado atual a partir do placar histórico.

**Sequenciamento decidido em 07/10/2026 (Codex + Rafael):** priorizar rastreabilidade profunda dos **13 CTs já em Playwright** (único recorte com execução **Playwright atual, reconciliada nesta análise**) antes de decompor os **25 restantes** das Suítes 3/4 (CT-013 a CT-037 — 037-013+1 = 25, não 24; correção de 07/10/2026 após revisão do Codex). **Correção de redação** (07/10/2026, após o DISC-002 encontrar os 22 CTs em Cypress no commit `bdf5e9a`): "único recorte com execução real" não é mais preciso — existem relatos históricos de execução verde em Cypress pra 22 desses 25, só que não revalidados nesta rodada e num branch não mesclado. A frase original falava só do estado conhecido até aquele ponto da investigação (antes do DISC-002 ler o código das Suítes 3/4). Isso reordena o trabalho — **não remove** CT-013–037 do critério de saída do DISC-002.

### Grafo confirmado — os 13 CTs Playwright (CT-001–012, CT-038)

> [!warning] Evidência não é uniforme entre os 13 — corrigido após revisão do Codex (07/10/2026)
> **CT-001–012** (`login.spec.ts`, `credentials.spec.ts`) estão commitados em `origin/main` — reconciliados contra o commit `16c41e4` (mesmo commit do DISC-001).
> **CT-038** (`audit-sessions.spec.ts`) é diferente: o arquivo está **untracked no worktree**, não faz parte do commit `16c41e4` nem de nenhum commit. A evidência dele é a execução manual confirmada contra o estado atual (não commitado) do worktree — não "contra o commit 16c41e4". Mantido nos 13/38 porque o teste existe e passa, mas a rastreabilidade de código dele é mais frágil (pode ser perdido se o worktree for descartado antes de commitar).
>
> Contra a tabela equivalente do [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] — sem divergência, para os 13.

**Pré-condições e dependências comuns aos 13** (Confirmado, não repetido linha a linha):
- Projeto `seed` do Playwright já rodou (`dependencies: ['seed']` no `playwright.config.ts`) e gravou `seed-manifest.json`.
- Fixture `seed` troca os atores padrão (`agents.agent`, `citizens.citizen`) pelo slot do worker (`pool.ts`/`parallelIndex`) — identidade real variável por worker, nunca `Servidor Publico 01`/`Cidadão 01` fixos.
- `instanceId` sempre vem de `seed.instance.id` (resolvido pelo seed), nunca de env var — não existe parametrização de cliente/instância hoje.
- **Cliente/instância:** a do baseline reconciliado pelo seed — Confirmado. **Ambiente de implantação:** o backend atual de `PW_BASE_URL`/`PW_GRAPHQL_URL`/`PW_AUTH_URL` — Confirmado. Reuso em outro ambiente de implantação ou outra instância/tenant (ex. 225) — Inferido, sem teste.
- Nenhum dos 13 muda estado de conta (bloqueio, status, cadastro novo) como resultado esperado — todos são leitura/validação de credencial.

| CT | Rótulo/arquivo | Pré-condição específica | Dados/configuração consumidos | Mutação/limpeza | Lacuna ou observação |
|---|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | `A02-C01` / `tests/api/auth/login.spec.ts` | Servidor do pool existe e está ativo | CPF do servidor (`seed.agents.agent.cpf`), `env.agentPass` | Nenhuma | — |
| [[03 - Casos de teste#^ct-002\|CT-002]] | `A02-C02` / `login.spec.ts` | Mesma identidade de CT-001, testada no login de cidadão | CPF do servidor (emprestado), `env.agentPass` | Nenhuma | Baseline **não tem cidadão PF puro** — usa o CPF do próprio servidor. Lacuna de massa, não de teste |
| [[03 - Casos de teste#^ct-003\|CT-003]] | `A02-C03` / `login.spec.ts` | Cidadão PJ do pool existe | CNPJ do cidadão (`seed.citizens.citizen.cnpj`), `env.citizenPass` | Nenhuma | Username PJ só é aceito em formato RAW (só dígitos) — achado da origem Cypress, preservado no Playwright |
| [[03 - Casos de teste#^ct-004\|CT-004]] | `A02-C04` / `login.spec.ts` | Cidadão PJ do pool existe | CNPJ do cidadão, `env.citizenPass`, login tipo `public-agent` | Nenhuma (espera rejeição) | Prova segregação de contexto servidor×cidadão |
| [[03 - Casos de teste#^ct-005\|CT-005]] | `A02-C05` / `login.spec.ts` | Igual a CT-002 | Igual a CT-002 | Nenhuma | Redundante com CT-002 por design — mesmo mecanismo, reafirma CPF nunca vira contexto Empresa |
| [[03 - Casos de teste#^ct-006\|CT-006]] | `A02-C06` / `login.spec.ts` | Nenhuma (identificador gerado no teste) | CPF inválido fixo (`'12345678900'`), `env.agentPass` | Nenhuma (espera rejeição) | Identificador não vem do seed — é um literal no spec |
| [[03 - Casos de teste#^ct-007\|CT-007]] | `A02-C07` / `login.spec.ts` | Nenhuma | CNPJ inválido fixo (`'12345678000100'`), `env.citizenPass` | Nenhuma (espera rejeição) | Idem CT-006, literal no spec |
| [[03 - Casos de teste#^ct-008\|CT-008]] | `A02-C08` / `login.spec.ts` | Cidadão PJ do pool existe | CNPJ do cidadão já existente, via `makeCitizenPJAutoRegistration` | Nenhuma (espera rejeição do `signup`) | Testa duplicidade, não cria conta nova |
| [[03 - Casos de teste#^ct-009\|CT-009]] | `A02-C09` / `login.spec.ts` | Igual a CT-002/005 | Igual a CT-002/005 | Nenhuma | Mesma identidade emprestada — 3º caso com o mesmo mecanismo (CT-002, CT-005, CT-009) |
| [[03 - Casos de teste#^ct-010\|CT-010]] | `A01-C01` / `tests/api/auth/credentials.spec.ts` | Servidor do pool existe | CPF do servidor, senha deliberadamente errada (literal no spec) | Nenhuma (espera rejeição) | — |
| [[03 - Casos de teste#^ct-011\|CT-011]] | `A01-C02` / `credentials.spec.ts` | Nenhuma | CPF gerado (`generateCPF()`, inexistente), `env.agentPass` | Nenhuma (espera rejeição) | Identificador não vem do seed |
| [[03 - Casos de teste#^ct-012\|CT-012]] | `A01-C03` / `credentials.spec.ts` | Nenhuma | Campos vazios (`''`) | Nenhuma (espera rejeição) | É chamada de API pura — não verifica se a **UI** impede o envio com campo vazio. Se o requisito exigir isso, falta cobertura de tela |
| [[03 - Casos de teste#^ct-038\|CT-038]] | `A55-C01` / `tests/api/auth/audit-sessions.spec.ts` | Servidor do pool existe | Credenciais do servidor, 2 sessões API abertas no mesmo teste | Nenhuma (2 sessões ficam abertas até o teste encerrar, sem revogação explícita) | Spec ainda **não commitado** no repo (worktree em HEAD destacado) |

> Agrupamento aplicado só onde ator, estado e preparação são idênticos (CT-002/005/009) — mantidos em linhas separadas porque cada um tem critério de aceite próprio (C2–C5), só a coluna de pré-condição aponta a equivalência.

### CT-013 a CT-037 (exceto CT-038) — decomposto em 07/10/2026

> [!warning] Achado que muda a leitura do placar histórico — corrigindo o rótulo "cypress (legado)"
> O placar arquivado (`02 - Validação automação` do Arquivo) marca a maioria destes CTs como `cypress (legado)` com a nota genérica "código legado". Fui conferir o código real antes de propagar isso e **o rótulo esconde um detalhe que muda a avaliação**: o código **não está no commit atual** (`16c41e4`, HEAD do worktree `sogov-automation-playwright`, onde todo o resto desta investigação foi reconciliado). Ele existe no commit **`bdf5e9a`**, branch **`tr-1.24-1.25-suites-3-4-5`**, que hoje está **checked out no worktree irmão** `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-test` — não foi enviado ao remoto ("NÃO vai para o remoto: o alvo do port passou a ser Playwright", mensagem do commit). Ou seja: é código real, legível, mas num branch não mesclado — mais frágil que "legado" sugere. **Sobre rodar em CI, com precisão** (`.gitlab-ci.yml` do `sogov-automation-test`): o job `e2e-tests` dispara automaticamente só em push pra `main`, mas as `rules` também aceitam `$CI_PIPELINE_SOURCE == "trigger"` (API) ou `"web"` (disparo manual pela interface) em **qualquer branch** — não é tecnicamente impossível rodar esta branch em CI, só não roda **automaticamente**. Não verifiquei se algum pipeline manual/API já rodou contra ela.
>
> **Confirmei lendo os 2 arquivos de teste reais** (`git show bdf5e9a:cypress/testes/api/entities/auth/{lockout,identity-lifecycle}.api.cy.js`) — não presumi a partir do placar. Resultado: **22 dos 25 CTs têm teste Cypress real e completo** (CT-013,014,015,018,019 — Suíte 3; CT-020 a CT-036 inteira — Suíte 4). **3 não têm código em lugar nenhum**: CT-016, CT-017 (desbloqueio — mutation nunca capturada) e CT-037 (auditoria — endpoint nunca confirmado).
>
> **Execução:** os comentários do próprio código afirmam "confirmado rodando contra HML" em vários pontos (e o commit diz "13 CTs verdes"), mas isso é uma **alegação do código antigo, não uma execução validada nesta rodada** — não rodei nada (fora do escopo desta entrega). Estado: **Confirmado** que o código existe e é coerente com o requisito; **Inferido** que passaria se rodado hoje (ambiente pode ter mudado desde 01/10/2026).

**Pré-condições e dependências comuns aos 22 com código** (Confirmado, não repetido linha a linha):
- Cada cenário usa um **servidor de teste isolado** (`createIsolatedTestAgent`), nunca o agente global — mudar status/bloquear o agente global quebraria os ~127 testes que o reusam.
- Login sempre via `loginAgentExpectFailure` (primitiva sem `cy.session`) — mesmo nos casos de sucesso esperado, porque `cy.session` cachearia por CPF e mascararia uma segunda tentativa real no mesmo teste.
- Mutação de status usa `changePublicAgentWorkStatus` (confirmada via captura de API, não introspection — GraphQL introspection está desabilitada em HML) + enum `WORK_STATUS` (`IN_ACTIVITY`/`LICENSE`/`VACATION`/`SUSPEND` — Inativo e Suspenso são o mesmo `SUSPEND`).
- **Cliente/instância:** `Cypress.env("INSTANCE_ID")` — mesma instância de todo o resto da suíte Cypress, não parametrizada por teste. **Ambiente de implantação:** o que `cypress.env.json`/CI apontarem — não lido nesta rodada (fora do escopo, só leitura de teste).

#### Suíte 3 — Bloqueio por tentativas (CT-013 a CT-019)

| CT | Pré-condição específica | Dados/configuração | Mutação/limpeza | Lacuna ou observação |
|---|---|---|---|---|
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-013\|CT-013]] | Agente isolado novo, senha correta conhecida | 4 tentativas erradas + 1ª que bloqueia (`attemptFailedLogins`, N=4 + 1) | Conta fica bloqueada ao fim do teste (não revertida) | Assinatura exata do erro na 5ª tentativa: `system.messages.account-blocked` |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-014\|CT-014]] | Agente isolado novo (diferente do CT-013) | 4 tentativas erradas, depois 1 correta | Nenhuma mutação de status — só confirma que não bloqueou | — |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-015\|CT-015]] | **Reaproveita a conta já bloqueada pelo CT-013** — depende de CT-013 ter rodado antes no mesmo arquivo | Mesma conta do CT-013, senha correta desta vez | Nenhuma | **Achado real em disputa, já documentado no código**: rodando contra HML, login com senha CORRETA numa conta bloqueada autenticou normalmente (200) — contradiz a regra esperada. O comentário do teste é explícito: "não é bug do teste — é uma discrepância real entre o Termo e o comportamento do backend" |
| CT-016 | — | — | — | **Sem código.** Desbloqueio por link de e-mail — mutation nunca capturada (dependia de HAR que não chegou) |
| CT-017 | — | — | — | **Sem código.** Desbloqueio manual por outro servidor — mesma causa de CT-016 |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-018\|CT-018]] | Agente isolado novo | 3 tentativas erradas → 1 correta → mais 3 erradas → 1 correta | Nenhuma (prova reset do contador, duas vezes) | — |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-019\|CT-019]] | 2 agentes isolados novos (A e B) | A leva ao bloqueio (4+1 erradas); B tenta com senha certa | Conta A fica bloqueada; conta B intacta | Prova isolamento entre contas — mesma assinatura de erro do CT-013 |

#### Suíte 4 — Ciclo de vida da identidade (CT-020 a CT-036)

5 agentes fixos (CPF fixo, reaproveitados entre rodadas — diferente da Suíte 3): `agentAtivoInativo` (CT-020/032/033/034), `agentLicenca` (CT-021/022/023/024/025/026), `agentFerias` (CT-027/028/029/030/031), `agentSuspenso` (CT-035), `agentTransitions` (CT-036).

| CT | Pré-condição específica | Dados/configuração | Mutação/limpeza | Lacuna ou observação |
|---|---|---|---|---|
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-020\|CT-020]] | `agentAtivoInativo` setado pra `IN_ACTIVITY` | Login + leitura do próprio perfil (`userInstanceInfo`) | `setWorkStatus(IN_ACTIVITY)` | Testa acesso "irrestrito" só por consulta de perfil — não varre todos os 5 níveis de permissão (achado relevante pro gap de nível "Somente leitura" já registrado) |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-033\|CT-033]] | Mesmo agente, token obtido **antes** da mudança | Token antigo + `setWorkStatus(SUSPEND)` no meio do teste | Agente fica Inativo (setup do CT-032) | **Achado real documentado no código**: mecanismo de revogação (polling vs. invalidação de token) não confirmado — teste só observa o efeito esperado, "se falhar não é bug do teste" |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-032\|CT-032]] | Depende do CT-033 já ter deixado o agente Inativo | Login com credenciais corretas | Nenhuma | Ordem de execução importa — não é independente dos outros `it()` do arquivo |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-034\|CT-034]] | Mesmo agente, reversão pra Ativo | `setWorkStatus(IN_ACTIVITY)`, espera 3s, login | Devolve o agente a Ativo | **Achado sem causa raiz**: login continuou recusando por alguns segundos após a reversão — atraso de propagação não explicado |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-035\|CT-035]] | Agente fixo próprio (`agentSuspenso`) | `setWorkStatus(SUSPEND)` → login → reverte pra `IN_ACTIVITY` no fim | Reversão obrigatória no mesmo teste (agente é reaproveitado entre rodadas) | Confirma que "Suspenso" usa o mesmo enum técnico de "Inativo" — não existe valor separado |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-025\|CT-025]] | `agentLicenca`, token obtido antes da mudança | `setWorkStatus(LICENSE)` + tentativa de edição com token antigo | Agente fica em Licença (setup pros CT-021/022/023/024) | Mesmo padrão de achado do CT-033 (ação de escrita com token antigo) |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-021\|CT-021]] | Depende do CT-025 (agente já em Licença) | Login com credenciais corretas | Nenhuma | Confirma login permitido em Licença (diferente de Inativo) |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-022\|CT-022]] | Depende do CT-025 | Consulta `workStatus` via `getPublicAgents` por nome | Nenhuma | **Achado sem causa raiz, documentado no código**: a busca por nome às vezes não encontra o agente recém-criado, mesmo existindo (login funciona nos testes vizinhos) — instabilidade de busca, não de dado |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-023\|CT-023]] | Depende do CT-025 | Tentativa de `editPublicAgent` com token próprio | Nenhuma | Confirma bloqueio de escrita em Licença |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-024\|CT-024]] | Depende do CT-025 | `userInstanceInfo` (leitura do próprio perfil) | Nenhuma | Confirma zero visibilidade em Licença — decisão de produto de 18/08 (sem leitura mínima) |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-026\|CT-026]] | `agentLicenca`, `statusEnd` no passado | `setWorkStatus` com `statusStart`/`statusEnd` retroativos | Verifica e-mail de notificação (`waitForGmailMessage`) + reversão automática | Único CT da suíte que depende de caixa de e-mail real; confirma o requisito 1.27.11.4 de notificação |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-027\|CT-027]] | `agentFerias` | `setWorkStatus(VACATION)` + login | Agente fica em Férias (setup pros CT-028/029/030) | Espelha CT-021 pra Férias |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-028\|CT-028]] | Depende do CT-027 | `workStatus` via `getPublicAgents` | Nenhuma | Espelha CT-022 |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-029\|CT-029]] | Depende do CT-027 | `editPublicAgent` com token próprio | Nenhuma | Espelha CT-023 |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-030\|CT-030]] | Depende do CT-027 | `userInstanceInfo` | Nenhuma | Espelha CT-024 |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-031\|CT-031]] | `agentFerias`, `statusEnd` no passado (15 dias) | `setWorkStatus` retroativo | Reversão automática esperada | Espelha CT-026, sem a parte de e-mail |
| [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste#^ct-036\|CT-036]] | `agentTransitions`, agente dedicado só pra este CT | 3 mutações de status em sequência (Licença→Inativo→Ativo), checando login a cada etapa | Termina em Ativo | Único CT que testa transição múltipla no mesmo teste; mesma nota de atraso de propagação do CT-034 |

#### CT-037 (Suíte 5, restante)

| CT | Situação |
|---|---|
| CT-037 | **Sem código em nenhum framework.** Log de auditoria de tentativas de login — endpoint nunca confirmado (mesma limitação de CT-016/017: sem captura real de API, não dá pra codar sem inventar endpoint) |

> Fonte de todo este bloco: `git show bdf5e9a:cypress/testes/api/entities/auth/{lockout,identity-lifecycle}.api.cy.js`, lido por inteiro em 07/10/2026. Nenhum teste foi executado; nenhum arquivo foi alterado.

## Catálogo mínimo candidato

Preencher somente após cruzar os CTs com código e fontes de dados. Manter cada entrada ligada aos CTs que a exigem.

| Dado/estado candidato | CTs que justificam | Preparação existente | Reuso entre ambientes | Ação candidata | Evidência/pendência |
|---|---|---|---|---|---|
| Instância-alvo e configuração de endpoint | CTs que executam contra a instância | Perfil fixo no baseline; URLs fornecidas pelo ambiente | Não demonstrado para seleção de instância diferente | Avaliar parametrização segura com validação explícita do alvo | Confirmar ambientes e proteção contra criação acidental |
| Atores de servidor/cidadão e credenciais de teste | CTs de autenticação/estado | Pools por worker e credenciais ambientais no baseline Playwright | Reuso de atores no mesmo backend existe; entre ambientes a confirmar | Documentar pré-condições, ownership e reset por ambiente | Validar estado real e política de credenciais de teste |
| Estados de conta (bloqueio, licença, férias, inativo/suspenso) | CTs de 1.24–1.25 correspondentes após mapeamento individual | A verificar por CT | A confirmar | Determinar se são provisionados, alterados em teste ou preparados por API | Registrar operação inversa/limpeza e isolamento |
| Módulo/serviço/permissões | Requisitos e testes que comprovarem dependência | Seed declara catálogo mais amplo; consumo de cada CT a verificar | A confirmar | Incluir apenas dependências rastreadas | Cruzar passos/precondições e código dos testes |

## Decisões ao concluir

- **O que entra no preset:** apenas massa/estados necessários a requisitos que serão validados por automação; requisitos de infraestrutura ou operação devem apontar para evidência adequada.
- **Forma recomendada do preset:** a preencher com comparação fundamentada (perfil/configuração, seed reconciliador, preparação específica por suíte ou combinação).
- **Escopo mínimo inicial:** CTs, atores, entidades e estados que a matriz comprovar necessários.
- **Diferenças por ambiente:** endpoint, credenciais, disponibilidade de entidades, permissões e limpeza.
- **Riscos de isolamento e concorrência:** a preencher.
- **Primeiras entregas sugeridas:** a preencher com escopo pequeno, dependências e aceite próprio.
