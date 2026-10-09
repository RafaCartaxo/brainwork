---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.35.2.2.1"
status: em levantamento
---
# 08 - Especificação do preset piloto (item 1.35.2.2.1)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recorte-fonte:** [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]], [[06 - Especificação do preset piloto (TR 1.33)|06]], [[07 - Especificação do preset piloto (TR 1.34)|07]]

> [!info] Escopo desta fatia (09/10/2026)
> Sétima fatia da especificação do preset: liga **só o item 1.35.2.2.1 (Despacho durante a tramitação) e seus subitens numerados (1.35.2.2.1.1–1.35.2.2.1.6)** do recorte 07 ao que o seed Playwright atual já prepara. Os demais itens de 1.35 (histórico, estados gerais, prazos amplos, encerramento, documentos associados automaticamente) ficam de fora desta fatia. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Ação de teste (cria em tempo de execução):** mutation/CT que gera o despacho especificamente para validar o cenário — não é algo que o baseline deixa pronto de antemão.
- **Consulta (não prepara estado):** função que só lê dados já existentes.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Despacho na tramitação — atributos (TR 1.35.2.2.1.1–1.35.2.2.1.6)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.35.2.2.1.1 | Despacho — campo de livre preenchimento, com anexos e definição de destinatários (inclusive setores em cópia) | Ação de teste | `makeDispatch({sector, author, recipient?, recipientSector?}, overrides)`: `description` (texto livre), `attachments: []`, `involvedInDispatch: [{inCopy, publicAgentId, publicAgentSectorId}]` (destinatários, com `inCopy` para "em cópia") + `values.destinations`. CT A14-C01 confirma a criação básica | `playwright/src/data/factories/documents.ts` (`makeDispatch`); `playwright/src/api/services/documents.ts` (`generateDispatch`); `playwright/tests/api/processing/dispatch.spec.ts` (A14-C01) | Confirmado |
| 1.35.2.2.1.3 | Despacho sigiloso ou não | Ação de teste | `withConfidentiality` (booleano) + `values['privacity-dispatch']`. CT A14-C01 confirma sem sigilo; CT A14-C02 confirma com sigilo (`withConfidentiality: true`, verificado via evento do documento) | `documents.ts`/`factories/documents.ts`; `dispatch.spec.ts` (A14-C01/C02) | Confirmado |
| 1.35.2.2.1.4 | Despacho pode indicar prazo aos destinatários (respeita prazo oficial/do documento pré-existente) | Ação de teste | `makeDeadlineForDispatch({sector, recipient}, overrides)`: `deadlineDays`, `initialDate`, `finalDate`, `recipient`. CT A14-C03 cria despacho com `deadlinesConfig: [deadline]`. **Não verifiquei nesta rodada** se o código impede ultrapassar um prazo oficial/do documento pré-existente — só confirmei que o prazo do despacho existe como dado | `factories/documents.ts` (`makeDeadlineForDispatch`); `dispatch.spec.ts` (A14-C03) | Confirmado (dado de prazo existe); A confirmar (regra de não ultrapassar prazo pré-existente) |
| 1.35.2.2.1.2.a | Despacho pode apensar outro documento à tramitação | Ação de teste | CT A14-C04 cria despacho com `documentsAssociated: [outroDocumentoId]` e confirma, no evento do documento, `documentsAssociate[].isAssociated`. **Achado relevante, sem resolver a dúvida já registrada no recorte 07**: o campo e o evento usam a palavra "associado" (`documentsAssociated`/`isAssociated`), não "apensado" — isso é consistente com o mecanismo descrito no TR (vínculo via despacho), mas não decido aqui se essa é a mesma estrutura de dados do "documento associado automaticamente" (1.35.4) — a dúvida do recorte 07 sobre os dois mecanismos **permanece como está**, sem alteração | `documents.ts`/`factories/documents.ts`; `dispatch.spec.ts` (A14-C04) | Confirmado (mecanismo do despacho existe); A confirmar (identidade com 1.35.4 — dúvida do recorte 07 preservada) |
| 1.35.2.2.1.5 | Assinar/solicitar assinaturas em despacho específico e anexos | — | Encontrei helpers de UI (`clickOnDispatchSignaturesButton`, `citizenIssueAndSign`) em `playwright/src/ui/dispatch.ts` — confirmam que o fluxo de solicitar/assinar despacho existe e é automatizado, mas são interações de tela, não um dado de preset isolado. Não aprofundei o payload de API por trás dessas ações nesta rodada | `playwright/src/ui/dispatch.ts` | Confirmado (mecanismo existe, via UI); A confirmar (payload de API/dado de preset) |
| 1.35.2.2.1.6 | Possibilidade de imprimir despacho emitido, incluindo anexos e assinaturas | Ação de teste (gera/baixa o PDF) + Consulta (`CreatedDispatch` só traz URLs) | **Confirmado que existe geração e download de PDF do despacho**: CT A22-C04 (`print.spec.ts`) cria documento+despacho, consulta `getDispatchPrintInfo(dispatchId)`, solicita download do tipo `CUSTOM_VERSION_DISPATCH` via `requestDownload`, espera o status `DONE` e confirma uma URL `.pdf` baixável. Separadamente, o retorno de `generateDispatch` (`CreatedDispatch`) já traz `originalDispatchUrl` e, por anexo, `printUrl` — são evidências distintas, nenhuma delas prova sozinha o conteúdo do PDF. **O que isso não confirma**: que o PDF gerado de fato *inclua* anexos e assinaturas, como o TR pede — nem o CT A22-C04 nem o CT A14 (criação do despacho) verificam o conteúdo do arquivo baixado, só que o download é bem-sucedido (URL `.pdf`, sem checar o que há dentro) | `playwright/src/api/services/print.ts` (`getDispatchPrintInfo`); `playwright/tests/api/processing/print.spec.ts` (A22-C04); `documents.ts`, interface `CreatedDispatch` (`originalDispatchUrl`, `printUrl`) | Confirmado (geração/download de PDF existe); A confirmar (inclusão de anexos e assinaturas no conteúdo do PDF) |

## Despacho de etapa (1.30.2) × Despacho na tramitação (1.35.2.2.1) — comparação de código

> O recorte 05 (piloto 1.30–1.31) já registrava este despacho de etapa como "Preparação específica de cenário (não a população padrão)"; o recorte 07 já registrava a dúvida "mesmo termo, atributos compatíveis, mas o TR não declara identidade formal" e o contexto de produto (módulo Despachos) como "parcialmente esclarecido — mesma família/modelo funcional; identidade estrutural não confirmada".

- **O que esta fatia verificou:** o despacho de etapa (`makeWorkflowInput`, array `dispatches` por `step`) só **configura** que uma etapa exige N despachos (com ou sem assinatura, com ou sem exigência de anexo) — é uma configuração do workflow, não uma chamada à mutation de criação de despacho. Não encontrei, no código lido, nenhum teste que **emita de fato** o despacho exigido por uma etapa e observe se isso aciona `generateDispatch`/`createDispatch` (a mesma mutation usada pelo despacho geral de tramitação, 1.35.2.2.1) — busquei por testes que combinem `workflow`/`Workflow` com `generateDispatch`/`createDispatch` e não encontrei nenhum.
- **Conclusão desta fatia:** **não encontrei evidência de código que declare ou resolva a identidade** entre os dois despachos. A dúvida registrada nos recortes 05 e 07 **permanece exatamente como estava** — esta fatia não a resolve nem a transforma em fato, só confirma que não há (ainda) um teste automatizado que ligue os dois.

## O que falta para este recorte virar preset executável (resumo)

- **Regra de prazo do despacho não ultrapassar prazo oficial/do documento (1.35.2.2.1.4)** — não verificada nesta rodada.
- **Payload de API da assinatura de despacho (1.35.2.2.1.5)** — só confirmei via helpers de UI; não aprofundei o lado de dados/API.
- **Conteúdo do PDF de despacho impresso (1.35.2.2.1.6)** — confirmado que o download do PDF existe e funciona (CT A22-C04); não confirmado que o PDF inclua de fato anexos e assinaturas, como o TR descreve.
- **Identidade entre despacho de etapa (1.30.2) e despacho de tramitação (1.35.2.2.1)** — segue sem evidência de código; nenhum teste liga workflow a `generateDispatch`.
- **Relação com a dúvida apensado × associado automaticamente (recorte 07)** — o despacho usa `documentsAssociated`/`isAssociated` internamente; isso não resolve a dúvida já registrada, só é um dado novo a considerar se/quando ela for revisitada.
- **Nenhum despacho integra o baseline persistente** — todos os CTs citados (A14-C01–C04) criam seus próprios documentos/despachos em tempo de execução.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só a parte referente a 1.35.2.2.1 foi usada nesta fatia.
- Piloto anterior (referência, não repetida como requisito aqui): [[04 - Especificação do preset piloto (TR 1.30–1.31)]] (despacho de etapa).
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/data/factories/documents.ts` (`makeDispatch`, `makeDeadlineForDispatch`, `makeExternalDispatch`, `makeDisassociateDispatch`), `playwright/src/api/services/documents.ts` (`generateDispatch`, `generateExternalDispatch`, interface `CreatedDispatch`), `playwright/src/api/services/print.ts` (`getDispatchPrintInfo`), `playwright/src/api/services/workflow.ts` (confirmado: só `getWorkflowOrCreate`, nenhuma função de emissão de despacho de etapa), `playwright/src/ui/dispatch.ts`, `playwright/tests/api/processing/dispatch.spec.ts` (A14-C01–C04), `playwright/tests/api/processing/print.spec.ts` (A22-C04). Lido nesta sessão, só leitura — nenhum comando executado.
