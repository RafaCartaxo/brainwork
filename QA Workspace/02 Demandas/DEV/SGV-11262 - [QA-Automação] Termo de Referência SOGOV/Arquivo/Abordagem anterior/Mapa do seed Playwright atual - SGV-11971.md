---
tags:
  - qa
  - automacao
  - seed
  - conhecimento
tipo: mapa-tecnico
demanda: SGV-11971
revisado: 2026-10-07
---
# Mapa do seed Playwright atual — SGV-11971

> [!info] Escopo deste mapa
> Registra o que o código atual prepara e o que os 13 CTs Playwright da SGV-11971 consomem. Não propõe arquitetura nova, não altera o seed e não afirma que a configuração já funcione em qualquer cliente/instância.

## Resumo

O repositório já tem um mecanismo reutilizável de preparação: `BASELINE` + projeto Playwright `seed` + `provisionBaseline` + manifesto por execução + fixtures de atores. A preparação é idempotente em uma instância fixa e gera/reconcilia uma massa ampla para a suíte do repositório.

Os CTs atuais de autenticação consomem uma fração pequena dessa massa: **instância, servidor de um pool por worker, cidadão PJ de um pool por worker e credenciais configuradas no ambiente**. Não usam módulos, assuntos/serviços, workflows ou documentos diretamente.

## O que os 13 CTs consomem

| CTs | Dados e operação | Preparação necessária |
|---|---|---|
| CT-001 | Login válido de servidor (`A02-C01`) | Instância do manifesto + servidor do pool do worker + senha de servidor |
| CT-002 | Login de cidadão PF usando o CPF do mesmo servidor (`A02-C02`) | Instância + servidor do pool + senha de servidor; não há cidadão PF puro no baseline atual |
| CT-003 | Login de cidadão PJ (`A02-C03`) | Instância + cidadão PJ do pool + senha de cidadão |
| CT-004 | Tentativa de login de servidor usando o CNPJ do cidadão PJ (`A02-C04`) | Instância + CNPJ do cidadão do pool + senha de cidadão |
| CT-005, CT-009 | CPF do servidor autenticado pela rota de cidadão (`A02-C05`, `A02-C09`) | Instância + servidor do pool + senha de servidor; os dois cenários usam a mesma identidade PF emprestada |
| CT-006, CT-007 | CPF/CNPJ inválidos (`A02-C06`, `A02-C07`) | Instância + endpoint/credencial correspondente; identificadores inválidos são fornecidos pelo teste |
| CT-008 | Tentar cadastrar de novo CNPJ já existente (`A02-C08`) | Instância + CNPJ do cidadão PJ do pool; o teste espera rejeição e não pretende criar outra conta |
| CT-010 | Servidor com senha incorreta (`A01-C01`) | Instância + servidor do pool + senha deliberadamente incorreta |
| CT-011 | CPF inexistente (`A01-C02`) | Instância + identificador gerado pelo teste + senha de servidor |
| CT-012 | Credenciais vazias (`A01-C03`) | Instância + endpoint de autenticação; atualmente é uma chamada API, não uma verificação da prevenção de envio na interface |
| CT-038 | Abrir duas sessões API simultâneas do mesmo servidor e consultar `getPublicAgents` nas duas (`A55-C01`) | Instância + servidor do pool + credenciais de servidor; duas sessões novas no mesmo teste |

O fixture `seed` troca os atores padrão do manifesto pelos atores do slot do worker (`parallelIndex`). Assim, `seed.agents.agent` e `seed.citizens.citizen` nos specs apontam para identidades dos pools por worker, não necessariamente para as identidades de nome-base `Servidor Público 01` e `Cidadão 01`.

Para o cidadão PJ, isso significa que os CTs não usam diretamente a identidade-base `Cidadão 01`: a chave `citizen` passa a apontar para um dos quatro registros `Cidadao Pool E2E W1–W4`. O pool é selecionado pelo worker. O pool de CNPJs alfanuméricos é separado e não é usado por estes CTs.

### Leitura correta dos resultados verdes

- Os CTs não alteram estado de conta: não bloqueiam, desbloqueiam, mudam status nem cadastram um usuário novo como resultado esperado.
- As rejeições negativas confirmam uma resposta de erro HTTP ou resposta sem ID de sessão; o matcher não distingue toda causa de negócio possível. Para CT-008, por exemplo, uma rejeição genérica não prova sozinha que o motivo foi duplicidade.
- CT-002/005/009 reutilizam a identidade do servidor na face de cidadão. O baseline atual não fornece uma identidade de pessoa física cidadã independente.
- CT-012 verifica rejeição pela API com campos vazios. Se o requisito exigir que a interface impeça o envio, isso requer cobertura de UI além do teste atual.
- O run de 06/10/2026 registrado no vault não teve falhas nos 13 testes `@auth`; esta nota não representa uma nova execução.

## Inventário atual do seed

`tests/setup/seed.setup.ts` executa `provisionBaseline` antes do projeto `api`. A preparação obtém ou cria uma instância pelo perfil de identidade definido em código, configura os recursos por API, revalida recursos importantes e grava IDs/resultados num manifesto em `.runtime/<runId>/seed-manifest.json`. O setup usa autenticação administrativa e, quando necessário, a caixa de e-mail configurada.

| Recurso | Capacidade atual observada no código | Usado diretamente pelos 13 CTs? |
|---|---|---|
| Instância | Um perfil fixo em `BASELINE.instance`; o ID efetivo é descoberto e gravado no manifesto | **Sim, todos** |
| Setores | 3 setores principais; setor pai e 5 subsetores dedicados | Não |
| Módulos | 14 módulos nomeados no mapa e 1 módulo dedicado à árvore de subsetores; regras/propriedades aplicadas e verificadas em alguns casos | Não |
| Assuntos/serviços | 12 serviços nomeados, incluindo variações de prazo, abertura externa, interação do cidadão e opções de módulo | Não |
| Workflows | 3 configurações, incluindo workflow com anexo obrigatório e workflow de 5 etapas | Não |
| Servidores | 29 identidades nomeadas em `BASELINE.agents`; além delas, pool de 4 servidores isolados por worker | **Pool de 4** |
| Cidadãos | 5 identidades nomeadas: `citizen`, `engineer`, `architect`, `manager`, `alphanumeric`; pool de 4 cidadãos PJ e pool de 4 CNPJs alfanuméricos | **Pool PJ de 4** |
| Documentos | O seed não cria uma massa-base de documentos para estes CTs de autenticação | Não |

Os 13 CTs são de autenticação API e não precisam de qualquer módulo, serviço ou documento. Esses recursos são preparados porque o mesmo seed é dependência global dos demais projetos/suítes Playwright. Oportunidade de seed mínimo por projeto é uma hipótese de otimização, não uma necessidade demonstrada pelos CTs atuais.

### Catálogo que o seed já declara

Este é o catálogo existente no código, não uma proposta de ampliar o baseline. Os nomes entre parênteses são as chaves lógicas disponíveis no manifesto/configuração.

- **Módulos (15):** PA, DO, CO, PU e ASS; `mesasAlheias`; `workflow`, `workflowAttachment`, `workflowFiveSteps`; `proceduralColumns`; `confidentialDispatchOff`; `informativeTextKept` e `informativeTextHidden`; `accessKey`; e o módulo próprio `subsectors.module`.
- **Serviços (12):** PA, CO, DO; `officialPA` e `officialPADeadline` (7 dias úteis); `citizenOpeningOnly`; `workflow`, `workflowAttachment`, `workflowFiveSteps`; `proceduralColumns`; `confidentialDispatchOff`; `openExternalDisabled`.
- **Servidores nomeados (29):** perfis padrão e administrativos; perfis especialistas e de subsetores; identidades dedicadas a cenários de troca de e-mail, mudança de setor, assinatura sequencial, mesas alheias, sigilo, chave de acesso e revisão. O `agentThird` permanece na preparação por dependência da suíte legada; a fixture Playwright o marca como aposentado para novos usos.
- **Pools por worker:** 4 servidores, 4 cidadãos PJ e 4 cidadãos PJ com CNPJ alfanumérico. O número máximo de workers fica limitado ao tamanho desses pools.
- **Cidadãos nomeados (5):** `citizen`, `engineer`, `architect`, `manager` e `alphanumeric`.
- **Workflows (3):** padrão, com anexo do despacho exigido e com cinco etapas.
- **Documentos:** não há um conjunto de documentos provisionado como parte do baseline descrito aqui; os testes de documentos produzem ou criam seus próprios cenários.

Os CTs de autenticação usam apenas o cidadão PJ da chave `citizen` (reapontada ao pool por worker); não usam os perfis `engineer`, `architect`, `manager`, `alphanumeric`, nenhum módulo, nenhum serviço nem os workflows.

## Reprodutibilidade e limites de configuração

### Alvo do primeiro piloto

Decisão da iniciativa em 07/10/2026: começar numa **instância de teste dedicada e estável**, criada ou reconciliada pelo seed. A seleção de uma instância de cliente existente fica para uma etapa futura.

> [!important] Instância dedicada criada para teste — ainda não selecionada pelo seed
> Em 07/10/2026 foi criada a instância **ID 225 — “Termo De Referência - Sogov”**. O seed atual, porém, não seleciona por ID: `provisionBaseline` chama `getInstanceOrCreate` com o nome fixo de `BASELINE.instance`; a busca é pelo nome exato, sem distinção entre maiúsculas/minúsculas. Se não encontrar esse nome, a função cria outro cliente e inicia a implantação. Como o nome configurado hoje é diferente, **não executar o seed antes de ajustar sua seleção para a instância 225**. Também confirmar que a configuração de ambiente do run aponta para o mesmo backend onde a instância 225 foi criada.

Após o ajuste, os specs de autenticação consumirão o ID retornado no manifesto, então não precisam fixar `225` em cada teste nem na URL. O que precisa ser explícito é o alvo do seed e a proteção contra criação acidental de outro cliente.

O escopo, os critérios de segurança e a validação desta primeira entrega estão em [[SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/01 Automação/00 - Automação|Entrega 01 — Baseline na instância 225]].

**O que já é reproduzível:**

- O seed procura/reconcilia recursos por identidades naturais e revalida o resultado pela API.
- IDs efetivos ficam no manifesto por execução; os specs consomem o manifesto em vez de fixar IDs de instância/usuário.
- Cada worker recebe atores próprios dos pools; o launcher limita workers ao tamanho do pool e o projeto proíbe sharding.
- Credenciais e URLs vêm do ambiente, e as senhas não são definidas em `baseline.ts`.

**Limites atuais para cliente/instância:**

- O perfil da instância — nome, CNPJ e domínio — está fixo em `BASELINE.instance`; o seed obtém/cria esse perfil no backend apontado pelas URLs atuais.
- `config/env.ts` permite selecionar URLs e credenciais do ambiente, mas não expõe um parâmetro de `clientId` ou de instância-alvo existente.
- `PW_SEED_NAMESPACE` é exigido pelo parser, mas não encontrei uso dele na criação/reconciliação da massa nem na impressão digital do manifesto.
- A impressão digital considera URLs e o nome fixo da instância. Não distingue uma seleção explícita de cliente/instância.

Portanto, a capacidade atual é **preparar/reusar uma instância de teste conhecida em um ambiente configurado**. A decisão para o primeiro piloto já está tomada: criar/reconciliar uma instância dedicada por meio do seed. Selecionar qualquer cliente/instância por execução continua sendo uma evolução futura.

### Roteiro de Sanidade 01 — referência de contexto de negócio

O [[../../../../03 Sanidades/Roteiro de Sanidade 01 - Implantação|Roteiro de Sanidade 01]] é uma referência para entender a implantação do SOGOV: estrutura de órgãos e setores, tipos de módulo, configuração de assuntos/serviços e perfis de servidor com permissões diferentes. Ele dá contexto para analisar CTs e escolher atores/estados quando esses conceitos fizerem parte do escopo.

O roteiro **não define o preset do seed nem deve ser reproduzido como pacote de dados**. A primeira entrega foca na instância dedicada e nos atores necessários aos 13 CTs de autenticação. Esses CTs não usam módulos, serviços, documentos nem perfis variados de permissão. Hoje, porém, o projeto `api` depende do seed global, que prepara também recursos usados por outras suítes. Isso é comportamento existente do repositório, não uma necessidade dos 13 CTs; qualquer redução ou separação do seed global precisa ser avaliada como decisão técnica própria. Quando uma próxima fatia exigir regras de módulos ou permissões, consultar o roteiro para entender o negócio e preparar somente o necessário àquela fatia.

O seed atual tem seus próprios nomes e estruturas para setores, servidores e módulos. Não se deve presumir que eles correspondem aos exemplos do roteiro. O roteiro também contém valores de execução manual, placeholders e credenciais de exemplo; esses valores não são massa permanente para automação.

**Alvo atual do código:** os specs consomem o ID do manifesto, não um ID numérico embutido na URL. O seed seleciona a instância pelo perfil fixo em `BASELINE.instance` no backend definido por `PW_BASE_URL`/`PW_GRAPHQL_URL`/`PW_AUTH_URL`. O código contém comentário de que o homolog é compartilhado, mas não foi lida a configuração local do ambiente; portanto, o endereço e o ID efetivamente usados numa execução atual ainda não estão confirmados. A instância dedicada só estará criada quando o perfil de seed for separado do perfil compartilhado e a preparação for executada no ambiente definido.

## Referências de código

- Seed como dependência dos testes API: `playwright/playwright.config.ts` e `playwright/tests/setup/seed.setup.ts`.
- Perfil de dados: `playwright/src/data/seed/baseline.ts`.
- Reconciliação e composição do manifesto: `playwright/src/data/seed/provision.ts` e `playwright/src/data/seed/manifest.ts`.
- Seleção de atores por worker: `playwright/src/data/seed/pool.ts` e `playwright/src/fixtures/index.ts`.
- CTs: `playwright/tests/api/auth/login.spec.ts`, `credentials.spec.ts` e `audit-sessions.spec.ts`.

> [!note] Repositório consultado
> `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`. Esta análise foi somente de leitura; os testes não foram reexecutados contra o ambiente.
