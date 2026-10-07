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

**Sequenciamento decidido em 07/10/2026 (Codex + Rafael):** priorizar rastreabilidade profunda dos **13 CTs já em Playwright** (único recorte com execução real/verde registrada) antes de decompor os 24 restantes das Suítes 3/4. Isso reordena o trabalho — **não remove** CT-013–037 do critério de saída do DISC-002.

### Grafo confirmado — os 13 CTs Playwright (CT-001–012, CT-038)

Reconciliado contra o código no commit `16c41e4` (mesmo commit do DISC-001) e contra a tabela equivalente do [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] — sem divergência entre os dois.

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

### CT-013 a CT-037 (exceto CT-038) — ainda não decompostos nesta rodada

Pendentes por decisão de sequenciamento, não por esquecimento — continuam no critério de saída C2 da demanda. Ver placar histórico em [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/01 Automação/02 - Validação automação|02 - Validação automação (Arquivo)]] pro estado conhecido de cada um.

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
