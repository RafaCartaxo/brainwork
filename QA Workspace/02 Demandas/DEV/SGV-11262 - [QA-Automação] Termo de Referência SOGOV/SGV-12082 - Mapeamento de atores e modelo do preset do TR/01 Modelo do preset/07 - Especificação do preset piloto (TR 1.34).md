---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.34"
status: em levantamento
---
# 07 - Especificação do preset piloto (item 1.34)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recorte-fonte:** [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]], [[06 - Especificação do preset piloto (TR 1.33)|06]]

> [!info] Escopo desta fatia (09/10/2026)
> Sexta fatia da especificação do preset: liga **só o item 1.34 (Etiquetas)** do recorte 07 ao que o seed Playwright atual já prepara. Tramitação/despacho (1.35), também do mesmo recorte, fica para fatia futura separada. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega (`provision.ts`).
- **Ação de teste (cria e remove em tempo de execução):** CRUD exercitado só dentro de um teste específico, com limpeza no fim — não fica pronto de antemão.
- **Consulta (não prepara estado):** função que só lê dados já existentes.
- **Dependência observada (não confirmado que o seed prepare):** algo que um teste pressupõe já existir no ambiente-alvo, sem que o próprio repositório o crie.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Etiqueta — criação, edição, subetiqueta e compartilhamento (TR 1.34)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.34, 1.34.2 | Etiqueta — nome, cor, criação | Ação de teste (cria e remove) | `createTag`/`makeTagInput` (`name`, `backgroundColor`, `textColor`). CT A40-C01 cria e confirma os 3 campos; `cleanup.defer` exclui a etiqueta ao fim do teste — **não é dado persistente do baseline**, `provision.ts` não referencia nenhuma função de etiqueta | `playwright/src/api/services/tags.ts` (`createTag`); `playwright/src/data/factories/tags.ts` (`makeTagInput`); `playwright/tests/api/processing/label-management.spec.ts` (A40-C01) | Confirmado |
| 1.34.1.a | Etiqueta pessoal (uso individual, visível só na mesa do próprio servidor) | Ação de teste | `makeTagInput` tem `sharedType: 'NO_SHARE'` por padrão; A40-C01 confirma `isShared: false` no resultado. **O que isso confirma**: a etiqueta não está compartilhada (`NO_SHARE`/`isShared: false`). **O que isso não confirma**: que ela seja visível só na mesa pessoal do servidor que a criou — essa parte específica do TR (visibilidade restrita) não foi verificada pelos CTs citados, é a leitura mais direta do nome "não compartilhada", não um teste de visibilidade | `tags.ts`; `factories/tags.ts`; A40-C01 (`tag.isShared` = `false`) | Confirmado (não compartilhada); Inferido/A confirmar (visibilidade restrita à mesa pessoal) |
| 1.34.1.b, 1.34.2.1 | Etiqueta compartilhada entre setores | Ação de teste | CT A40-C05 cria etiqueta com `sharedType: 'MY_SECTORS'` + `sectorsIds` (2 setores do baseline, GP/SCTA) e confirma `isShared: true` e os setores em `OrganizationalComponents`. **Não verifiquei** a parte de UI "aparece em seção própria, visível a todos do setor" (1.34.2.1) — é afirmação de tela, não de dado | `tags.ts`; `factories/tags.ts`; `label-management.spec.ts` (A40-C05) | Confirmado (dado); A confirmar (comportamento de tela) |
| 1.34.1.2 | Etiqueta padrão "Urgente", fixa, não excluível | **Dependência observada** — não confirmado que o seed prepare | `provision.ts` **não cria** nenhuma etiqueta (busca por `createTag`/`makeTagInput` no arquivo não encontrou nenhuma ocorrência). O CT A19 (`label-document.spec.ts`) **assume** que a etiqueta de id fixo `1` já existe no ambiente-alvo com o nome `'Urgente'` (`const LABEL_ID = 1`) — isso é uma dependência do ambiente, não algo que este repositório prepara | `playwright/tests/api/processing/label-document.spec.ts` (`LABEL_ID = 1`, comentário "Urgente") | Confirmado (dependência existe no teste); Inferido (que seja de fato a etiqueta padrão do TR 1.34.1.2, por nome/comportamento bater) |
| 1.34.2.2 | Subetiqueta ligada a etiqueta principal | Ação de teste | `makeSubTagInput(name, fatherTagId)` — **confirmado pelo payload**: o input não envia `sharedType` próprio. **Não confirmado pelos CTs**: que isso resulte, de fato, em herdar o compartilhamento da etiqueta-pai — essa explicação ("herda o compartilhamento") é um **comentário no código**, não um comportamento verificado por nenhum dos CTs citados (eles conferem `isSub`, `fatherTagId`, `fatherTag.name` e a relação pai↔filho em `childTags`, não o efeito do compartilhamento herdado). CTs A40-C02/C04/C07/C09/C10 cobrem criação, edição, exclusão e histórico de subetiqueta | `factories/tags.ts` (`makeSubTagInput`, comentário "herda o compartilhamento da etiqueta-pai"); `label-management.spec.ts` (A40-C02 e seguintes) | Confirmado (estrutura pai/filho); A confirmar (herança de compartilhamento na prática) |
| 1.34.2.3 | Edição de nome/cor/setores de qualquer etiqueta | Ação de teste | `updateTag(api, id, input)` — CT A40-C03 (etiqueta) e A40-C04 (subetiqueta, com `sharedType: null` — "subetiqueta não tem compartilhamento próprio", confirmado no comentário do código) | `tags.ts` (`updateTag`); `label-management.spec.ts` (A40-C03/C04) | Confirmado |
| — | Histórico de alterações da etiqueta/subetiqueta | Ação de teste (gera o histórico) + Consulta (recupera o histórico) | Os CTs A40-C08/C09/C10 primeiro **criam/editam** a etiqueta ou subetiqueta (ação de teste — é isso que gera os registros) e só depois chamam `getTagHistory` para **ler** o que foi gerado (consulta, não prepara nada por si só). Granularidade confirmada: criação = `NEW`; edição = `UPDATE` (campo `name`); para subetiqueta, campos próprios (`subTagCreated`, `subTagName`, `subTagDeleted`) registrados tanto na sub quanto, parcialmente, na etiqueta-pai | `tags.ts` (`getTagHistory`); `label-management.spec.ts` (A40-C08/C09/C10) | Confirmado |
| 1.34.2.4 | Alterações de etiqueta se aplicam automaticamente às etiquetas já aplicadas em documentos | — | Não verifiquei nesta rodada — os CTs de edição (A40-C03/C04) testam a etiqueta em si, não o efeito em documentos que já a têm aplicada | — | A confirmar |
| 1.34.2.5 | Etiqueta excluída permanece nos documentos onde já estava, mas não pode ser adicionada a novos | — | Não verifiquei nesta rodada — os CTs de exclusão (A40-C06/C07) confirmam que a etiqueta some de `tagsByPublicAgent`, não o estado dela em documentos onde já estava aplicada | — | A confirmar |
| 1.34.1.3 | Etiquetas usáveis como filtro na mesa de trabalho | — | O piloto 1.33 já registrou que `getWorkboardDocuments` aceita `filter: { tags: [] }` — não aprofundei aqui se esse filtro usa `tagId` de forma equivalente ao que esta fatia descreve; sem nova verificação | Ver [[06 - Especificação do preset piloto (TR 1.33)|piloto 1.33]] | A confirmar (sem verificação nova) |

## Associação de etiqueta a documento (TR 1.34, via recorte 07/elemento "Documento")

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| — | Atribuir/desatribuir etiqueta a um documento | Ação de teste | `updateDocumentLabel(api, documentObjectId, tagId, sectorId)` — alterna: 1ª chamada com um `tagId` atribui, 2ª com o mesmo `tagId` desatribui. CTs A19-C01/C02 confirmam os dois sentidos, usando a etiqueta "Urgente" de id fixo (ver linha acima — dependência observada, não preparada por este repositório) | `playwright/src/api/services/documents.ts` (`updateDocumentLabel`); `playwright/tests/api/processing/label-document.spec.ts` (A19-C01/C02) | Confirmado |

## O que falta para este recorte virar preset executável (resumo)

- **Etiqueta "Urgente" (1.34.1.2)** — é uma dependência observada do ambiente-alvo (id fixo `1`), não algo que `provision.ts` prepara; se um cenário precisar dela num ambiente novo, isso precisaria ser resolvido primeiro (criar ou confirmar que já existe).
- **Efeito de edição/exclusão sobre documentos já etiquetados (1.34.2.4/1.34.2.5)** — não verificado nesta rodada.
- **Filtro de etiqueta na mesa (1.34.1.3)** — existe um parâmetro `filter.tags` na consulta da mesa (piloto 1.33), mas não aprofundei a equivalência nesta fatia.
- **Nenhuma etiqueta integra o baseline persistente** — toda a cobertura confirmada (CRUD, subetiqueta, compartilhamento, histórico) vem de CTs que criam e removem seus próprios dados em tempo de execução.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só a parte referente a 1.34 foi usada nesta fatia.
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/api/services/tags.ts`, `playwright/src/data/factories/tags.ts`, `playwright/src/api/services/documents.ts` (`updateDocumentLabel`), `playwright/src/data/seed/provision.ts` (confirmado: nenhuma referência a funções de etiqueta), `playwright/tests/api/processing/label-management.spec.ts`, `playwright/tests/api/processing/label-document.spec.ts`. Lido nesta sessão, só leitura — nenhum comando executado.
