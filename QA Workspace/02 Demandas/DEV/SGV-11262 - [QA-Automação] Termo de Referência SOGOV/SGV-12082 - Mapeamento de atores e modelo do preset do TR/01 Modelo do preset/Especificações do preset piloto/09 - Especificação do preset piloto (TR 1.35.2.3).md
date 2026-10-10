---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.35.2.3"
status: aprovado
---
# 09 - Especificação do preset piloto (item 1.35.2.3)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Mapa geral:** [[../00 - Mapa geral]] · **Recorte-fonte:** [[../Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]], [[06 - Especificação do preset piloto (TR 1.33)|06]], [[07 - Especificação do preset piloto (TR 1.34)|07]], [[08 - Especificação do preset piloto (TR 1.35.2.2.1)|08]]

> [!info] Escopo desta fatia (09/10/2026)
> Oitava fatia da especificação do preset: liga **só o item 1.35.2.3** do recorte 07 — "Retificação do documento de abertura de processo administrativo, com histórico e justificativa legal" — ao que o seed Playwright atual já prepara. Revisão (1.35.2.4), edição em pré-elaboração (1.35.2.5), prazos (1.35.2.6/1.35.2.7), encerramento (1.35.3), associação automática (1.35.4) e histórico geral (1.35.5) ficam **fora desta fatia** — citados só onde necessário como dependência ou dúvida de fronteira. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Ação de teste (cria em tempo de execução):** mutation chamada por um CT especificamente para validar o cenário — não é algo que o baseline deixa pronto de antemão.
- **Consulta (não prepara estado):** função que só lê dados já existentes.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Retificação do documento de abertura (TR 1.35.2.3)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.35.2.3 | Retificar o documento de abertura de um processo administrativo | Ação de teste | `retifyDocument(api, documentObjectId, input, justification, attachments)` → mutation `retifyDocumentObject`. Confirmado exercitado sobre o **mesmo documento de abertura** gerado por `generateDocument`/`makeDocument` (não um despacho nem documento associado) — CTs A18-C02 e A25-C01 chamam `retifyDocument(doc.documentId, ...)` logo após criar `doc` | `playwright/src/api/services/documents.ts` (`retifyDocument`); `playwright/tests/api/processing/rectify-document.spec.ts` (A25-C01); `playwright/tests/api/processing/history-document.spec.ts` (A18-C02) | Confirmado |
| 1.35.2.3 | Categoria do documento retificável (TR diz "processo administrativo") | — | **Achado**: o mecanismo foi exercitado em dois contextos de categoria diferentes — A18-C02 usa `documentContext(seed)` sem override, cujo padrão é `seed.modules.PA.deploymentId` (Processo administrativo, batendo com o texto do TR); A25-C01 usa `seed.modules.DO.deploymentId` (Documento oficial) explicitamente. **Isso não contradiz o TR** (que descreve o caso de processo administrativo), mas sugere que, no código, a mutation não é exclusiva de PA — não concluo que o TR pretenda isso também para outras categorias, só registro o que o código exercita | `factories/documents.ts` (`documentContext`, default `seed.modules.PA.deploymentId`); `rectify-document.spec.ts` (override para `seed.modules.DO`) | Confirmado (mecanismo exercitado em PA e em DO); A confirmar (se o TR restringe isso só a PA) |
| 1.35.2.3 | Justificativa legal | Ação de teste (só valor padrão exercitado) | **Separando existência de adequação**: `retifyDocument` tem parâmetro `justification` (string) e **o campo é enviado à mutation** — isso está confirmado. A18-C02 e A25-C01 **omitem esse argumento**, exercitando só o valor padrão genérico `'Retificando documento'`. Isso confirma que o campo existe e é transmitido — **não confirma** que esse valor atenda ao requisito de "justificativa legal" do TR (que sugere um conteúdo jurídico/motivado, não um texto genérico de teste). Fica em aberto: se o valor usado nos CTs seria aceito como justificativa legal adequada, se o campo é customizável/obrigatório na prática, e se há alguma validação de conteúdo | `documents.ts` (`retifyDocument`, parâmetro `justification`) | Confirmado (campo existe e é enviado); A confirmar (adequação legal do valor; customização, obrigatoriedade e validação) |
| — | Anexos na retificação | — | `retifyDocument` tem parâmetro `attachments` (array), mas **nenhum CT encontrado o preenche** — ambos os testes citados usam o padrão `[]`. Não presumo que anexos funcionem ou sejam obrigatórios nesse fluxo, só registro que o campo existe e não foi exercitado com conteúdo | `documents.ts` (`retifyDocument`, parâmetro `attachments`) | Confirmado (campo existe); A confirmar (uso com conteúdo real) |
| 1.35.2.3 | Histórico da retificação | Consulta (não prepara estado) | `getDocumentForAgent` retorna `isRectified: boolean` e um array `values[]` versionado, com `versionInfo.type`. Enum confirmado com 2 valores: `'initial'` (versão de criação, A18-C01) e `'retification'` (versão após retificar, A18-C02/A25-C01); A25-C01 também confirma `isRectified: true`. **O que isso confirma**: existe versionamento do conteúdo, com a versão retificada identificada como tal. **O que isso não confirma**: a completude do histórico exigido pelo TR — por exemplo, se o registro inclui a justificativa legal usada, autoria/data da retificação, ou todos os eventos relevantes (isso são exemplos do que poderia compor "histórico", não uma lista exaustiva nem algo que os CTs verificam) | `documents.ts` (`getDocumentForAgent`, campo `isRectified`); `history-document.spec.ts` (A18-C01/C02) | Confirmado (versionamento do conteúdo identificado como retificação); A confirmar (completude do histórico exigido pelo TR) |

## Fronteiras com itens vizinhos (fora desta fatia)

- **Retificação de despacho** (`playwright/tests/e2e/processing/rectify-dispatch.spec.ts`) é um mecanismo **diferente**, sobre despacho, não sobre o documento de abertura — não faz parte de 1.35.2.3 e não foi analisado nesta fatia, só identificado para não ser confundido com o que está aqui.
- **Histórico geral do documento/processo** (1.35.5) tem seu próprio teste dedicado (`history-document.spec.ts`), que também cobre a versão `'initial'` sem retificação alguma — citado aqui só porque o mesmo arquivo cobre o caso de retificação (A18-C02); o restante do escopo de 1.35.5 não foi analisado.
- **Revisão de documento em pré-elaboração** (1.35.2.4) e **edição de documento em pré-elaboração** (1.35.2.5) não foram verificadas nesta fatia — podem ou não compartilhar mecanismo com a retificação; não presumo nada sobre isso aqui.

## O que falta para este recorte virar preset executável (resumo)

- **Adequação da justificativa legal (1.35.2.3)** — o campo existe e é enviado, mas os CTs só exercitam um valor padrão genérico (`'Retificando documento'`); não confirmado se isso atenderia ao requisito de justificativa legal do TR, nem se o campo é customizável/obrigatório/validado na prática.
- **Completude do histórico de retificação (1.35.2.3)** — confirmado o versionamento do conteúdo (versão identificada como retificação); não confirmado se o histórico completo exigido pelo TR inclui justificativa legal registrada, autoria/data, ou todos os eventos.
- **Anexos na retificação** — campo existe, não exercitado com conteúdo em nenhum CT encontrado.
- **Restrição por categoria de documento** — o TR descreve o caso de "processo administrativo"; o código exercita o mecanismo tanto em PA quanto em Documento oficial — não presumo que isso generalize a toda categoria, só registro a evidência encontrada.
- **Nenhuma retificação integra o baseline persistente** — os dois CTs citados (A18-C02, A25-C01) criam seu próprio documento e retificam em tempo de execução.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[../Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só o item 1.35.2.3 foi usado nesta fatia.
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/api/services/documents.ts` (`retifyDocument`, `getDocumentForAgent`), `playwright/src/data/factories/documents.ts` (`documentContext`, `makeDocument`), `playwright/tests/api/processing/rectify-document.spec.ts` (A25-C01), `playwright/tests/api/processing/history-document.spec.ts` (A18-C01/C02). Lido nesta sessão, só leitura — nenhum comando executado.
