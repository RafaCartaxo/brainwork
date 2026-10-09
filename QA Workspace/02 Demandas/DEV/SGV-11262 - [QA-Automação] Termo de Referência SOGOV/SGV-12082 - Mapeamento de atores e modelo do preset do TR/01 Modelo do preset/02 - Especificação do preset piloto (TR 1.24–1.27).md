---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.24–1.27"
status: aprovado
---
# 02 - Especificação do preset piloto (itens 1.24–1.27)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recortes-fonte:** [[Seções do TR/02 - Autenticação e ciclo de vida da identidade (1.24–1.25)|02 - Autenticação]], [[Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)|03 - Estrutura organizacional]]

> [!info] Escopo deste piloto (09/10/2026)
> Primeira ligação entre o modelo conceitual do TR (recortes 02/03) e o que a automação já prepara/consome de fato. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** É especificação: para cada ator/dado/estado dos recortes 02/03, registra se já existe no seed Playwright atual, onde, e o que falta. Os 11 recortes, a matriz e o mapa geral **não foram alterados** — este arquivo só referencia o que eles já registraram. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal) e `bdf5e9a` (branch `tr-1.24-1.25-suites-3-4-5`, não mesclada — usada só como evidência de produto já capturada, não como fonte do TR). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Por isso, esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico (ex.: se a lacuna de "estados funcionais" seria resolvida portando a mutation do Cypress, criando um seed próprio, ou outro caminho — isso é decisão de quem for implementar, não desta especificação).

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega, pronto para qualquer cenário (não muda por teste).
- **Preparação específica de cenário:** dado/estado que só alguns cenários precisam — não faz parte da população padrão do baseline. Isso descreve a necessidade lógica do dado, não que o seed será executado ou mutado a cada teste: pode ser preparado uma única vez no ambiente persistente (ver "Restrição de ambiente" acima); a forma e o momento do provisionamento não são decididos nesta nota.
- **Cobertura atual do seed:** o que o código do repositório confirma hoje — não o que seria desejável.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Autenticação e identidade (TR 1.24–1.25)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.24.1 | Servidor Público — CPF + senha | Baseline | Vários servidores nomeados em `BASELINE.agents` (CPF próprio) + pool de 4 por worker (`BASELINE.pools.agent`); senha via `PW_AGENT_PASSWORD` | `playwright/src/data/seed/baseline.ts`; CT A02-C01 (`login.spec.ts`) | Confirmado |
| 1.24.2 | Cidadão (Pessoa Física) — CPF + senha | Baseline | **Lacuna**: não existe cidadão PF próprio no baseline; os CTs A02-C02/C05/C09 reaproveitam o CPF do servidor como login de cidadão | `login.spec.ts` (comentário explícito: "o baseline não tem um cidadão Pessoa Física puro") | Confirmado (lacuna, não suposição) |
| 1.24.3 | Empresa/entidade (Pessoa Jurídica) — CNPJ + senha | Baseline | `BASELINE.citizens` (citizen/engineer/architect/manager/alphanumeric) + pools `citizen`/`alphanumeric` (4 cada); senha via `PW_CITIZEN_PASSWORD` | `baseline.ts`; CT A02-C03 | Confirmado |
| 1.25.1 | Bloqueio por 5 tentativas malsucedidas | Preparação específica de cenário (precisa de um agente isolado, não o pool padrão) | **Não portado para Playwright.** Existe só em Cypress, branch não mesclado (`createIsolatedTestAgent` + contagem de tentativas) | DISC-004 (arquivado), Entrega candidata 1 (CT-013/014/018/019); confirmado por `git grep` nesta sessão: mecanismo presente só em `tr-1.24-1.25-suites-3-4-5` | Confirmado (gap) |
| 1.25.3.1–4 | 4 estados funcionais: Ativo/Licença/Férias/Inativo | Preparação específica de cenário (estado necessário em cenários específicos; não integra a população padrão) | **Não existe no Playwright `main`** (nenhum campo de status em `BASELINE.agents`). Existe em Cypress (branch não mesclado): mutation `changePublicAgentWorkStatus`, enum `WORK_STATUS` com 4 valores | Ver seção "Status funcional e presença" abaixo | Confirmado (gap) |

## Estrutura organizacional e níveis (TR 1.26–1.27)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.26 | Setor/Subsetor, hierarquia reparentável | Baseline | `BASELINE.sectors` (GP, SCTA, DIR) + `BASELINE.subsectors` (1 setor pai + 5 filhos, módulo dedicado) | `baseline.ts`; `provision.ts` (criação idempotente por nome) | Confirmado |
| 1.27 | Servidor vinculado a Setor, com nível/cargo **por vínculo** (N:N) | Baseline (1 setor) + preparação específica de cenário (2º setor) | No baseline, cada agente de `BASELINE.agents` aponta para 1 setor só. **O vínculo N:N é exercitado em cenário**: a identidade `reviewTwoSectors` nasce com 1 setor (DIR) e o teste E64 adiciona um segundo (SCTA) via `editPublicAgent`, antes do login do servidor de teste — não é "não exercitado" | `baseline.ts` (`reviewTwoSectors: {..., sector: 'DIR', ...}`); `playwright/tests/e2e/public-agents/review-attachment-button-by-sector.spec.ts`, função `configureAgent` (`components.push(...)` quando `key === 'reviewTwoSectors'`) | Confirmado |
| 1.27.2.1–5 / níveis canônicos | 5 níveis: Administrador, Administrador Setorial, Especialista, Usuário básico, Somente leitura (nomes canônicos confirmados por Rafael — ver recorte 03, "Mapeamento confirmado") | Baseline | Campo numérico `accessLevel` (2–5) em `BASELINE.agents`, propagado para `organizationHierarchyId` na API. Identidades nomeadas confirmam a escala: `seqBasic` (2), `seqSpecialist` (3), `seqSectorAdmin` (4), `seqAdmin` (5). **Nível 1 ("Somente leitura") não tem identidade própria no baseline atual** | `baseline.ts` L.126-129; `provision.ts` L.435-448 | Confirmado (4 dos 5 níveis têm identidade; nível 1 é lacuna) |
| 1.27.4.4 / 1.27.5.4 / 1.27.6 | Permissão de visualizar/criar Assuntos e Serviços, por nível | — | **Contexto de produto confirmado por Rafael** (recorte 03, "Permissões confirmadas — Assuntos e Serviços", 08/10/2026): os 5 níveis visualizam; só Administrador e Administrador Setorial criam. **Essa regra ainda não foi verificada no código/seed nesta rodada** — não procurei a mutation/endpoint correspondente no repositório | [[Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)#Permissões confirmadas — Assuntos e Serviços (contexto de produto, Rafael, 08/10/2026)|recorte 03]] | Confirmado (produto); A confirmar (código) |
| 1.27.3–1.27.7.4 | Escopo de permissão por nível (4 áreas: organograma/servidores/contatos externos/assuntos-serviços) | — | Não verificado nesta rodada — fora do escopo deste piloto (autenticação + organização/níveis); checagem de regras de permissão por área fica para quando um cenário de sanidade precisar dela | — | A confirmar |
| 1.27.10.1 / 1.27.11.2 | Status de atividade (listagem × editável) e presença online/offline | Preparação específica de cenário | Ver seção "Status funcional e presença" abaixo | — | Confirmado (gap) |

## Status funcional e presença — evidência nova (09/10/2026)

O recorte 03 já registrava, como dúvida do TR, que a relação entre o enum de listagem (1.27.10.1, 5 valores) e o enum editável (1.27.11.2, 4 valores) **não é especificada pelo texto**, e tratava "Inativo = Suspenso" como convenção de trabalho confirmada por Rafael para a tela atual — não como equivalência literal do TR.

Nesta rodada, encontrei evidência de **produto** (não do TR) que fortalece essa convenção, numa branch não mesclada do repositório Playwright/Cypress (`tr-1.24-1.25-suites-3-4-5`, arquivo `docs/business-rules/api/identity-lifecycle.md`): uma mutation GraphQL real (`changePublicAgentWorkStatus`) foi capturada por request/response (DevTools/HAR) em 31/08/2026. O enum do backend (`WORK_STATUS`) tem exatamente 4 valores:

| Rótulo na tela | Valor do enum (backend, capturado) |
|---|---|
| Em atividade | `IN_ACTIVITY` |
| De licença | `LICENSE` |
| De férias | `VACATION` |
| **Inativo** | **`SUSPEND`** |

**Não existe um valor `INACTIVE` separado** — o rótulo "Inativo" da tela e o conceito de "Suspenso" mapeiam para o mesmo valor de enum `SUSPEND`. Isso é evidência de produto (captura real de API), **não é texto do TR** e não reescreve a dúvida registrada no recorte 03 — mas é uma camada de evidência mais forte do que a confirmação verbal já registrada, porque vem de uma captura de comportamento real do backend, não de leitura de tela.

**O que isso NÃO resolve:** o enum de 5 valores da listagem (1.27.10.1: Ativo/Inativo-offline/Suspenso/Licença/Férias) continua sem relação declarada com este `WORK_STATUS` de 4 valores — "Inativo" em 1.27.10.1 significa presença offline (eixo diferente), não o mesmo "Inativo"/`SUSPEND` do formulário de edição. Essa parte da dúvida do recorte 03 permanece aberta.

Este mecanismo (`changePublicAgentWorkStatus`/`WORK_STATUS`) **não foi encontrado na `main`** — confirmado por busca direta no código (`git grep` não encontrou o nome em nenhum arquivo de `main`) — e **está presente na branch Cypress não mesclada** (`tr-1.24-1.25-suites-3-4-5`). Não presumo aqui que portar essa mutation seja o único caminho ou um pré-requisito — registro só o estado atual confirmado nesta sessão (consistente com o que DISC-003/004, arquivado, já havia achado); a escolha de mecanismo fica para quem implementar.

## O que falta para este recorte virar preset executável (resumo)

- **Cidadão Pessoa Física próprio** (1.24.2) — hoje reaproveita o CPF do servidor; se um cenário de sanidade precisar de um cidadão PF independente, falta criá-lo no baseline.
- **Bloqueio por tentativas** (1.25.1) e **estados funcionais** (1.25.3.1–4, 1.27.10.1, 1.27.11.2) — mecanismos já confirmados e testados em Cypress (branch não mesclada); não encontrados na `main` do Playwright. Não presumo aqui qual mecanismo resolveria isso — só registro que não existe hoje no Playwright.
- **Identidade de nível "Somente leitura"** (nível 1) — os outros 4 níveis canônicos já têm identidade nomeada no baseline (via `accessLevel`); falta uma para o nível 1.
- **Permissão de Assuntos e Serviços por nível** (visualizar/criar) — confirmada como contexto de produto por Rafael; ainda não verificada no código/seed.
- **Vínculo servidor↔múltiplos setores** — já exercitado em cenário (teste E64, `reviewTwoSectors`), não no baseline estático.

## Fontes/evidências

- Recortes do TR (fonte do modelo conceitual, não alterados nesta rodada): [[Seções do TR/02 - Autenticação e ciclo de vida da identidade (1.24–1.25)]], [[Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)]].
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/data/seed/baseline.ts`, `playwright/src/data/seed/pool.ts`, `playwright/src/data/seed/provision.ts`, `playwright/tests/api/auth/login.spec.ts`, `playwright/tests/e2e/public-agents/review-attachment-button-by-sector.spec.ts`. Lido nesta sessão, só leitura — nenhum comando executado.
- Código do repositório (branch `tr-1.24-1.25-suites-3-4-5`, commit `bdf5e9a`, **não mesclada**): `docs/business-rules/api/identity-lifecycle.md` — consultado só como evidência de produto já capturada (mutation/enum), não como decisão de arquitetura nem como fonte do TR.
- Material arquivado (referência secundária, não fonte primária desta rodada): [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Roadmap - Automação TR]], [[../../Arquivo/Abordagem anterior/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]], [[../../Arquivo/Abordagem anterior/SGV-12082 - Análise do TR e preset de dados/00 QA/DISC-003 - Dados, preparação e eixos|DISC-003]], [[../../Arquivo/Abordagem anterior/SGV-12082 - Análise do TR e preset de dados/00 QA/DISC-004 - Alternativas e recomendação|DISC-004]].
