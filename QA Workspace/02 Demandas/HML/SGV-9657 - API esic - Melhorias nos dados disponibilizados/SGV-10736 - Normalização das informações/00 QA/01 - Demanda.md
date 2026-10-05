---
prioridade: media
origem: repo
pontos_alocados: ""
---

# SGV-10736 — Normalizar os campos retornados pela API e-SIC

**Ticket de origem:** SGV-10736 no Notion ("[DEV][PARTE 1] Normalização das informações"), item filho de SGV-9657 ("[Melhoria-dev] API esic - Melhorias nos dados que são disponibilizados na API...").

> [!info]- Navegação QA/DEV
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Problema / contexto

Clientes do SoGov usam os dados das solicitações e-SIC (relatórios como o da ATRICOM) e precisavam de informações ausentes ou ambíguas no retorno da API: não dava para diferenciar solicitantes de nomes iguais (sem ID), faltava tipo/data de nascimento/gênero do solicitante pessoa física, e a data de abertura/vencimento não vinha calculada de forma consistente quando não havia prazo configurado.

## Objetivo

A API retorna o JSON de solicitações e de estatísticas normalizado, com os campos novos descritos abaixo, permitindo identificar solicitantes de forma única e calcular prazo de atendimento de forma consistente.

### Entrega desta capacidade

Apenas a **Parte 1** (SGV-10736): mudanças de contrato da API (campos novos no retorno). Não inclui nenhuma tela — a Parte 2 (SGV-10735, feature de integrações) está impedida e fora de escopo nesta rodada.

> [!important] Esta é uma task **só de API** (fluxo 3f)
> Sem interface visual pra validar. A validação depende de chamadas diretas (Postman/curl/swagger) direto em homologação, sem esteira DEV — ver [[../../../../../Sistema/Contexto/PADROES_QA#Tasks de API (fluxo 3f)|PADROES_QA#Tasks de API (fluxo 3f)]].

---

## Decisões de produto

- Dados do solicitante (ID, tipo PF/PJ, data de nascimento, gênero) só existem quando o solicitante tiver o cadastro correspondente preenchido — sem exigir recadastro retroativo.
- A data limite (`orderDateDeadline`) é calculada e retornada mesmo quando a solicitação não tem prazo configurado, sinalizando isso explicitamente em vez de omitir o campo.
- Nomenclatura de campos no retorno segue padrão em inglês.
- Mensagens de erro da API vêm em português, com status code HTTP coerente com a mensagem retornada.

---

## Escopo

- Endpoint de **listagem de solicitações**: ID do solicitante, tipo (pessoa física/jurídica), data de nascimento e gênero (quando cadastrados), data de abertura (`orderDate`), data limite calculada (`orderDateDeadline`, com `date`/`days`/`type`).
- Endpoint de **estatísticas**: ID do solicitante no ranking (`rankingRequesters[].id`) e detalhamento de prazo (`deadline.timely`/`delayed`/`undefined`).
- Padronização de mensagens de erro (português) e coerência entre status code e mensagem.

---

## Fora de escopo

- Qualquer tela ou fluxo de UI (Parte 2 — SGV-10735, impedida, sem pacote próprio).
- Alterações em módulos além de solicitações/estatísticas do e-SIC.
- Contagem de solicitações respondidas (`totalAnswered`) e status "Respondido" — o sistema não tem esse conceito de status; `orderStatus` reflete o andamento interno do documento (tramitação), não o fato de já ter sido respondido ao cidadão.

---

## Critérios de aceite

- C1. A listagem de solicitações retorna o ID do solicitante, diferenciando solicitantes de mesmo nome. ^c1
- C2. A listagem de solicitações retorna o tipo do solicitante (pessoa física ou jurídica) corretamente para cada um. ^c2
- C3. Para solicitante pessoa física com cadastro completo, a listagem retorna data de nascimento e gênero; quando o cadastro não tiver esses dados, a API não quebra e os campos vêm ausentes/nulos. ^c3
- C4. A listagem retorna `orderDate` (data de abertura) para toda solicitação. ^c4
- C5. A listagem retorna `orderDateDeadline` com `date`, `days` e `type` calculados, mesmo quando a solicitação não tem prazo configurado. ^c5
- C6. `orderStatus` distingue corretamente os status Recebido, Em Andamento e Encerrado. ^c6
- C7. `rankingRequesters` retorna o ID de cada solicitante, diferenciando solicitantes de mesmo nome, com o nome correto (pessoa física, razão social de pessoa jurídica, ou identificação de anônimo). ^c7
- C8. O endpoint de estatísticas retorna o detalhamento de prazo (`timely`/`delayed`/`undefined`) com totais consistentes com os dados da listagem. ^c8
- C9. Em cenário de erro, a API retorna a mensagem (`message`) em português. ^c9
- C10. O status code HTTP da resposta de erro é coerente com a mensagem retornada. ^c10

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.
