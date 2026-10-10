---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.35.2.5"
status: aprovado
---
# 11 - Especificação do preset piloto (item 1.35.2.5)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Mapa geral:** [[../00 - Mapa geral]] · **Recorte-fonte:** [[../Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]], [[06 - Especificação do preset piloto (TR 1.33)|06]], [[07 - Especificação do preset piloto (TR 1.34)|07]], [[08 - Especificação do preset piloto (TR 1.35.2.2.1)|08]], [[09 - Especificação do preset piloto (TR 1.35.2.3)|09]], [[10 - Especificação do preset piloto (TR 1.35.2.4)|10]]

> [!info] Escopo desta fatia (09/10/2026)
> Décima fatia da especificação do preset: liga **só o item 1.35.2.5** do recorte 07 — "Edição do documento de abertura (documento/comunicação oficial) ainda em estado pré-elaboração, com histórico de cada edição" — ao que o seed Playwright atual já prepara. Solicitação de revisão (1.35.2.4, já mapeada na fatia anterior), retificação (1.35.2.3), prazos (1.35.2.6/1.35.2.7), encerramento, associação automática e histórico geral ficam **fora desta fatia** — citados só onde necessário como fronteira. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Ação de teste (cria em tempo de execução):** mutation chamada por um CT especificamente para validar o cenário — não é algo que o baseline deixa pronto de antemão.
- **Consulta (não prepara estado):** função que só lê dados já existentes.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Edição do documento de abertura (TR 1.35.2.5)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.35.2.5 | Editar o documento/comunicação oficial de abertura | Ação de teste | `editDocument(api, documentObjectId, input, sectorId)` → mutation `editDocumentObject`. CT A17-C01 confirma: lê a última versão em `values[]`, monta um novo valor (`{...latest, 'shortText-1_P': 'Teste Editado'}`) e chama `editDocument`; a leitura seguinte mostra o campo atualizado na versão mais recente | `playwright/src/api/services/documents.ts` (`editDocument`); `playwright/tests/api/processing/edit-document.spec.ts` (A17-C01) | Confirmado |
| 1.35.2.5 | **Achado relevante — estado "pré-elaboração" não confirmado nesta cobertura**: o TR descreve a edição para documentos "ainda em pré-elaboração" | — | O **único** CT encontrado que chama `editDocument` (A17-C01) cria o documento com `mode: 'SEND'`, **não** `mode: 'DRAFT'` — e não verifica `documentStatus` em nenhum momento. Separadamente, confirmei que outros CTs (`create-document.spec.ts`, `issue-draft-timeline-event.spec.ts`) usam `mode: 'DRAFT'` e verificam `documentStatus: 'DRAFT'` — relevante porque é o estado que mais se aproxima do termo "pré-elaboração" do TR. **Não verifiquei nesta fatia** o enum completo de `documentStatus` no backend nem os demais valores possíveis. **Isso não confirma nem descarta** que `editDocument` funcione ou seja restrito a documentos em `DRAFT` — só registro que a única cobertura encontrada não exercita esse estado específico | `playwright/src/data/factories/documents.ts` (`mode: 'SEND'` em `edit-document.spec.ts`; `mode: 'DRAFT'` em `create-document.spec.ts`, `issue-draft-timeline-event.spec.ts`, `delete-document.spec.ts`) | A confirmar |
| 1.35.2.5 | Edição é mecanismo **distinto** da retificação (1.35.2.3)? | — | **Confirmado que são mutations diferentes**: `editDocumentObject` (edição) e `retifyDocumentObject` (retificação, [[09 - Especificação do preset piloto (TR 1.35.2.3)|piloto 1.35.2.3]]) são duas funções/mutations próprias e distintas no código, e **confirmado que o CT de edição lê o mesmo array `values[]`** usado pelo histórico versionado. **O que não está confirmado por asserção**: o comentário em `edit-document.spec.ts` sugere uma sequência compartilhada de versionamento ("HISTÓRICO de versões (**initial**, **edit**, **retification**, ...)"), mas nenhum teste afirma que uma edição realmente produz uma entrada com `versionInfo.type: 'edit'` — o comportamento/valor `'edit'` em si não foi exercitado. Não presumo mais identidade nem mais diferença do que isso | `documents.ts` (`editDocument`, `retifyDocument` — nomes de mutation distintos); `edit-document.spec.ts` (leitura de `values[]`; comentário sobre a sequência de versionamento, sem asserção do valor `'edit'`) | Confirmado (mutations distintas; CT de edição lê o mesmo array `values[]`); A confirmar (se a edição gera entrada com `versionInfo.type: 'edit'` em execução) |
| 1.35.2.5 | Histórico de cada edição | — | O comentário em `edit-document.spec.ts` cita `'edit'` como um dos valores de `versionInfo.type` no histórico — mas **nenhum teste encontrado afirma isso via asserção** (`expect(...versionInfo.type).toBe('edit')` não existe no código lido). Os únicos valores de `versionInfo.type` **confirmados por asserção real** são `'initial'` e `'retification'` ([[09 - Especificação do preset piloto (TR 1.35.2.3)|piloto 1.35.2.3]]). A existência de um terceiro valor `'edit'` fica como observação de comentário, não como fato confirmado | `edit-document.spec.ts` (comentário, sem asserção); `history-document.spec.ts`/`rectify-document.spec.ts` (únicas asserções reais de `versionInfo.type`) | A confirmar (existência em execução e grafia do valor `'edit'`) |

## Fronteiras com itens vizinhos (fora desta fatia)

- **Solicitação de revisão** (1.35.2.4) já foi mapeada na fatia anterior ([[10 - Especificação do preset piloto (TR 1.35.2.4)|piloto 10]]) — mecanismo de evento `REVIEW`, não revisitado aqui.
- **Retificação** (1.35.2.3) já foi mapeada ([[09 - Especificação do preset piloto (TR 1.35.2.3)|piloto 09]]) — mecanismo de mutation `retifyDocumentObject`, citado aqui só para a comparação de mutations distintas.
- **Transição DRAFT→OPEN (emissão)** — observada em `issue-draft-timeline-event.spec.ts` (evento `ISSUED`), mas não analisada a fundo aqui; fica como referência para uma fatia futura de prazos/encerramento/emissão, se fizer sentido.

## O que falta para este recorte virar preset executável (resumo)

- **Edição sobre documento em estado `DRAFT` (pré-elaboração)** — não confirmada: a única cobertura de `editDocument` usa `mode: 'SEND'`, não `'DRAFT'`, e não verifica `documentStatus`. É a lacuna mais concreta desta fatia.
- **Valor `'edit'` em `versionInfo.type`** — citado só em comentário, sem asserção real que confirme a existência em execução nem a grafia.
- **Relação completa entre edição, retificação e o histórico compartilhado** — confirmado que são mutations distintas e que o CT de edição lê o mesmo array `values[]`; a sequência de versionamento compartilhada (`initial`/`edit`/`retification`) é sugerida só por comentário, não confirmada por execução — não aprofundado além disso (ex.: se há regras diferentes de quem pode editar vs. retificar).
- **Nenhuma edição integra o baseline persistente** — o único CT citado (A17-C01) cria seu próprio documento e edita em tempo de execução.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[../Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só o item 1.35.2.5 foi usado nesta fatia.
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/api/services/documents.ts` (`editDocument`, `retifyDocument`, `getDocumentForAgent`), `playwright/src/data/factories/documents.ts` (`makeDocument`, campo `mode`), `playwright/tests/api/processing/edit-document.spec.ts` (A17-C01), `playwright/tests/api/processing/create-document.spec.ts`, `playwright/tests/api/processing/issue-draft-timeline-event.spec.ts`, `playwright/tests/api/processing/delete-document.spec.ts` (uso de `mode: 'DRAFT'`, citados só para contraste). Lido nesta sessão, só leitura — nenhum comando executado.
