---
prioridade: media
origem: repo
pontos_alocados: ""
---

# SGV-10736 — Normalizar os campos retornados pela API e-SIC

**Ticket de origem:** SGV-10736 no Notion ("[DEV][PARTE 1] Normalização das informações"), item filho de SGV-9657 ("[Melhoria-dev] API esic - Melhorias nos dados que são disponibilizados na API...").

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** validar os CTs em homologação (Postman/curl) — sem esteira DEV, fluxo 3f.

---

## Problema / contexto

Clientes do SoGov usam os dados das solicitações e-SIC (relatórios como o da ATRICOM) e precisam de informações hoje ausentes ou ambíguas no retorno da API: não dá para diferenciar solicitantes de nomes iguais (sem ID), falta tipo/data de nascimento/gênero do solicitante pessoa física, e a data de abertura/vencimento não vem calculada de forma consistente, mesmo quando não há prazo configurado.

## Objetivo

A API retorna o JSON de solicitações e de estatísticas já normalizado, com os campos novos descritos abaixo, permitindo identificar solicitantes de forma única e calcular prazo de atendimento de forma consistente.

### Entrega desta capacidade

Apenas a **Parte 1** (SGV-10736): mudanças de contrato da API (campos novos no retorno). Não inclui nenhuma tela — a Parte 2 (SGV-10735, feature de integrações) está impedida e fora de escopo nesta rodada.

> [!important] Esta é uma task **só de API** (fluxo 3f)
> Sem interface visual pra validar. A validação depende de chamadas diretas (Postman/curl/swagger) direto em homologação, sem esteira DEV — ver [[../../../../../Sistema/Contexto/PADROES_QA#Tasks de API (fluxo 3f)|PADROES_QA#Tasks de API (fluxo 3f)]].

---

## Decisões de produto

- Dados do solicitante (ID, tipo PF/PJ, data de nascimento, gênero) só existem quando o solicitante tiver o cadastro correspondente preenchido — sem exigir recadastro retroativo.
- A data limite (`orderDateDeadline`) deve ser calculada e retornada mesmo quando a solicitação não tiver prazo configurado, sinalizando isso explicitamente em vez de omitir o campo.
- Novo status de solicitação "Respondido" (`totalAnswered`) passa a existir separado de "Em Andamento" (`totalInProgress`), tanto na listagem (`orderStatus`) quanto nas estatísticas.

---

## Escopo

- Endpoint de **listagem de solicitações**: incluir `requester.id`, `requester.type` (Pessoa Física/Jurídica), `PessoaFisica.dataNascimento`, `PessoaFisica.genero`, `orderDate`, `orderDateDeadline` (`date`/`days`/`type`), e o novo valor de `orderStatus` "Respondido".
- Endpoint de **estatísticas**: incluir `status.totalAnswered`, `rankingRequesters[].id`, e o detalhamento de prazo (`deadline.timely`/`delayed`/`undefined`).
- Ajustes de estrutura do JSON necessários para suportar os campos acima (ver `Retornos esperados (novos)` — `novo-documentos.json` e `novo-estatistica.json`).

---

## Fora de escopo

- Qualquer tela ou fluxo de UI (Parte 2 — SGV-10735, impedida, sem pacote próprio).
- Alterações em módulos além de solicitações/estatísticas do e-SIC.

---

## Critérios de aceite

- C1. A listagem de solicitações retorna `requester.id`, diferenciando solicitantes de mesmo nome. ^c1
- C2. A listagem de solicitações retorna `requester.type` (Pessoa Física/Jurídica) corretamente para cada solicitante. ^c2
- C3. Para solicitante Pessoa Física com cadastro completo, a listagem retorna `dataNascimento` e `genero`; quando o cadastro não tiver esses dados, a API não quebra e os campos vêm ausentes/nulos. ^c3
- C4. A listagem retorna `orderDate` (data de abertura) para toda solicitação. ^c4
- C5. A listagem retorna `orderDateDeadline` com `date`, `days` e `type` calculados, mesmo quando a solicitação não tiver prazo configurado (tipo "Dias úteis/Dias corridos" refletindo a regra aplicada). ^c5
- C6. `orderStatus` distingue corretamente "Respondido" de "Em Andamento" e dos demais status existentes (Recebido, Encerrado). ^c6
- C7. O endpoint de estatísticas retorna `totalAnswered` com a contagem correta de solicitações respondidas. ^c7
- C8. `rankingRequesters` retorna o `id` de cada solicitante, diferenciando solicitantes de mesmo nome no ranking. ^c8
- C9. O endpoint de estatísticas retorna o detalhamento de prazo (`timely`/`delayed`/`undefined`) com totais consistentes com os dados da listagem. ^c9

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido. *(sem estimativa em pontos registrada no Notion para esta parte — confirmar com o time antes de preencher)*

---

## Pendências de decisão

- `pontos_alocados` em aberto (ver checklist acima).
- **Nomenclatura de campos diverge do documento `Retornos esperados (novos)`** (achado em 05/10/2026, validação real em homologação): o retorno usa `requester.type: "PF"/"PJ"` (não "Pessoa Física"/"Pessoa Jurídica"), `data.individualPerson`/`data.legalPerson` (não `PessoaFisica`/`PessoaJuridica`), `individualPerson.birthDate`/`gender`/`fullName` (não `dataNascimento`/`genero`/`NomeCompleto`), `legalPerson.companyName` (não `RazaoSocial`), `"Sem sigilo"` com case diferente de `"Sem Sigilo"`. Rafael decide se isso é o contrato final (e os CTs/esta Demanda são atualizados pra bater) ou se é desvio (vira Bug). Enquanto não decidido, `04 - Validação dev` trata CT-001/002/003/005/011/014 como aprovados com ressalva, não fechados.
