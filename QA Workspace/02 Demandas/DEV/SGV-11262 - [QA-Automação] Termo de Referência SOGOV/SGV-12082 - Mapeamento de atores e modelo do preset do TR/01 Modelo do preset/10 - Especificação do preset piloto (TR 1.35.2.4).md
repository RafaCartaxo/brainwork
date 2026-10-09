---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.35.2.4"
status: aprovado
---
# 10 - Especificação do preset piloto (item 1.35.2.4)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recorte-fonte:** [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]], [[06 - Especificação do preset piloto (TR 1.33)|06]], [[07 - Especificação do preset piloto (TR 1.34)|07]], [[08 - Especificação do preset piloto (TR 1.35.2.2.1)|08]], [[09 - Especificação do preset piloto (TR 1.35.2.3)|09]]

> [!info] Escopo desta fatia (09/10/2026)
> Nona fatia da especificação do preset: liga **só o item 1.35.2.4** do recorte 07 — "Solicitação de revisão de documentos/comunicações oficiais ainda em estado pré-elaboração (antes da emissão oficial)" — ao que o seed Playwright atual já prepara. Edição em pré-elaboração (1.35.2.5), retificação (1.35.2.3), prazos (1.35.2.6/1.35.2.7), encerramento (1.35.3), associação automática (1.35.4) e histórico geral (1.35.5) ficam **fora desta fatia** — citados só onde necessário como fronteira. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Ação de teste (cria em tempo de execução):** mutation chamada por um CT especificamente para validar o cenário — não é algo que o baseline deixa pronto de antemão.
- **Consulta (não prepara estado):** função que só lê dados já existentes.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Solicitação de revisão (TR 1.35.2.4)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.35.2.4 | Solicitar revisão de um documento | Ação de teste | **Comportamento observado nesta cobertura, não uma regra geral do produto**: no CT/factory analisados, a revisão é configurada *no payload da criação* do documento — `makeDocument(ctx, { withReviews: true, reviewsConfig })`, passada para `generateDocument`. `reviewsConfig` inclui `createdById`, `reviewers: [{publicAgentId, publicAgentSectorId}]` e `comment` (default `'Revise via API'`). CT A27-C01 confirma: ao criar o documento com `withReviews: true`, surge um evento `REVIEW` no documento, com `review.id` e `review.reviewers[]`. **Não foi investigado** se existe também um fluxo de solicitação de revisão *posterior* à criação (sobre um documento já existente, sem revisão) — esta cobertura não prova nem descarta isso | `playwright/src/data/factories/documents.ts` (`makeDocument`, campos `withReviews`/`reviewsConfig`); `playwright/src/api/services/documents.ts` (`generateDocument`); `playwright/tests/api/processing/review-document.spec.ts` (A27-C01) | Confirmado (configuração na criação); A confirmar (solicitação de revisão posterior à criação) |
| 1.35.2.4 | Revisor(es) designado(s) | Ação de teste | `reviewers` é uma lista (`[{publicAgentId, publicAgentSectorId}]`) — o shape aceita mais de um revisor, mas o CT citado só exercita **um** revisor (`ctx.reviewer ?? ctx.agent`, por padrão `seed.agents.agentSupport`) | `factories/documents.ts` (`makeDocument`); `review-document.spec.ts` (A27-C01, usa `actors.agentApi('agentSupport')`) | Confirmado (um revisor); A confirmar (mais de um revisor simultâneo) |
| 1.35.2.4 | Aprovação da revisão | Ação de teste | `approveReview(api, reviewId, reviewerId)` — chamado pelo revisor (ator diferente de quem criou o documento). **O que o CT A27-C01 verifica exatamente**: lê o evento `REVIEW` inicial (guarda `reviewId`/`reviewerId`), chama `approveReview`, depois consulta novamente o evento `REVIEW` mais recente e confirma `reviewers[0].status === 'REVIEWED'`. **O que o CT não verifica**: não compara o `id` do evento/da revisão antes e depois, nem conta quantos eventos `REVIEW` existem — o comentário no próprio código afirma que é "o mesmo evento", mas essa afirmação não é comprovada pela asserção em si. Por isso, fica **A confirmar** se a aprovação atualiza o mesmo evento/revisão ou gera um novo | `documents.ts` (`approveReview`); `review-document.spec.ts` (A27-C01, `expect.poll` até `status === 'REVIEWED'`, sem comparar IDs) | Confirmado (status muda para `'REVIEWED'`); A confirmar (se é o mesmo evento/revisão ou um novo) |
| — | Rejeição da revisão | — | **Não encontrei** nenhuma função de rejeição de revisão (`rejectReview` ou equivalente) no código lido — só `approveReview` existe. Não presumo que a rejeição não exista no produto, só não a encontrei no repositório | `documents.ts` (busca por `Review`/`review` não encontrou função de rejeição) | A confirmar |
| — | Status inicial do revisor (antes de aprovar) | — | O CT citado só verifica o status **depois** de aprovar (`'REVIEWED'`); não vi, no código lido, a grafia exata do status inicial/pendente (ex.: algo como `'PENDING'`) | `documents.ts`, interface do campo `review` | A confirmar |
| — | Justificativa do revisor (`justification`) | — | O shape de retorno do documento declara `reviewers: [{..., justification: string \| null}]`, mas `approveReview` **não recebe** parâmetro de justificativa — nenhum CT encontrado preenche esse campo. Pode estar ligado a um fluxo de rejeição não encontrado | `documents.ts`, interface do campo `review` (`justification`) | A confirmar |
| 1.35.2.4 | Restrição a documentos "ainda em pré-elaboração" (antes da emissão oficial) | — | **Não verificado nesta rodada**: o CT A27-C01 não checa nenhum estado de emissão/elaboração do documento antes ou depois de configurar a revisão — não confirma nem contradiz que o mecanismo seja exclusivo de documentos em pré-elaboração | — | A confirmar |

## Fronteiras com itens vizinhos (fora desta fatia)

- **"Revisão de anexo"** (`playwright/tests/api/processing/review-attachment.spec.ts`, A26) é um mecanismo **diferente**: o próprio comentário no código diz que "a revisão de anexo é, na prática, a **substituição** do anexo por um novo" (`approveAttachmentWithSubstitution`/`disapproveAttachmentWithSubstitution`) — não é a mesma coisa que a revisão de documento (A27) tratada nesta fatia, e não foi analisada aqui.
- **Prazo de revisão**: um comentário no código (`documents.ts`, perto da linha 385) lista "review" como um dos 4 tipos de prazo (`document`/`review`/`signature`/`custom`) — mencionado só para registrar a existência, sem analisar prazos nesta fatia (ficam para fatia futura, conforme 1.35.2.6/1.35.2.7).

## O que falta para este recorte virar preset executável (resumo)

- **Rejeição de revisão** — não encontrada no código lido; não presumo ausência no produto.
- **Status inicial do revisor e grafia exata do enum** — só o valor pós-aprovação (`'REVIEWED'`) foi confirmado.
- **Campo `justification` do revisor** — existe no shape de leitura, não exercitado por nenhum CT encontrado.
- **Múltiplos revisores simultâneos** — o shape aceita lista, só um revisor foi exercitado no CT.
- **Restrição a documentos em pré-elaboração** — não verificada; não presumo que o mecanismo dependa ou não desse estado.
- **Nenhuma revisão integra o baseline persistente** — o CT citado (A27-C01) cria seu próprio documento com revisão configurada em tempo de execução.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só o item 1.35.2.4 foi usado nesta fatia.
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/data/factories/documents.ts` (`makeDocument`, campos `withReviews`/`reviewsConfig`), `playwright/src/api/services/documents.ts` (`generateDocument`, `approveReview`, interface do campo `review`), `playwright/tests/api/processing/review-document.spec.ts` (A27-C01), `playwright/tests/api/processing/review-attachment.spec.ts` (A26, citado só como fronteira). Lido nesta sessão, só leitura — nenhum comando executado.
