---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.35.5"
status: aprovado
---
# 15 - Especificação do preset piloto (item 1.35.5)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Mapa geral:** [[../00 - Mapa geral]] · **Recorte-fonte:** [[../Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]], [[06 - Especificação do preset piloto (TR 1.33)|06]], [[07 - Especificação do preset piloto (TR 1.34)|07]], [[08 - Especificação do preset piloto (TR 1.35.2.2.1)|08]], [[09 - Especificação do preset piloto (TR 1.35.2.3)|09]], [[10 - Especificação do preset piloto (TR 1.35.2.4)|10]], [[11 - Especificação do preset piloto (TR 1.35.2.5)|11]], [[12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12]], [[13 - Especificação do preset piloto (TR 1.35.3)|13]], [[14 - Especificação do preset piloto (TR 1.35.4)|14]]

> [!info] Escopo desta fatia (09/10/2026)
> Décima quarta e última fatia do recorte 07: liga **só o item 1.35.5** — "Possibilidade de visualizar histórico do documento/processo quando houver retificações ou edições" — ao que o seed Playwright atual já prepara. **Não cobre de novo** o conteúdo já mapeado nas fatias 09 (retificação, 1.35.2.3) e 11 (edição, 1.35.2.5) — essas permanecem como estão, citadas aqui só como fronteira; o que esta fatia acrescenta é a visão agregada do **histórico** em si (o array `values[]` como um todo, e a possibilidade de **visualizar** esse histórico pela tela) e suas lacunas próprias. **Linha do tempo geral da tramitação (1.35.1)** é um mecanismo **diferente e mais amplo** (todo evento do documento, não só retificação/edição) — citado só como fronteira, não analisado aqui. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**; nenhuma nota aprovada foi revisitada. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Ação de teste (cria em tempo de execução):** mutation chamada por um CT especificamente para validar o cenário — não é algo que o baseline deixa pronto de antemão.
- **Consulta (não prepara estado):** função que só lê dados já existentes.
- **Comportamento de tela observado, não dado de preset:** confirma que um elemento de UI existe/aparece, sem ser algo que o seed prepare.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Histórico do documento/processo (TR 1.35.5)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.35.5 | Histórico como array de versões (`values[]`) com `versionInfo.type` | Ação de teste | **Confirmado por asserção real** nos dois únicos valores exercitados: `'initial'` (versão de criação, A18-C01) e `'retification'` (versão após retificar, A18-C02/A25-C01) — já registrado em detalhe nas fatias 09 e 11, não repetido aqui. O que esta linha acrescenta: olhando os 2 testes de `history-document.spec.ts` como conjunto, **confirma-se que é o mesmo mecanismo** (mesma leitura `getDocumentForAgent(...).values`) usado para "ver que o documento foi criado" e "ver que o documento foi retificado" — não são dois históricos separados | `playwright/tests/api/processing/history-document.spec.ts` (A18-C01/C02) | Confirmado |
| 1.35.5 | Histórico cobre também **edições** (não só retificações) | — | **Não confirmado por asserção**: como já registrado na fatia 11, o valor `'edit'` de `versionInfo.type` aparece só num comentário de código (`edit-document.spec.ts`), nunca verificado via `expect(...).toBe('edit')`. Resultado desta fatia: o texto do TR 1.35.5 ("quando houver retificações **ou edições**") cobre dois casos, mas só o caso de retificação tem cobertura real — o de edição não | `edit-document.spec.ts` (comentário, sem asserção); `history-document.spec.ts` (nenhum teste de edição) | A confirmar (mesma lacuna já registrada na fatia 11, reafirmada aqui pela ótica do histórico) |
| — | Histórico acumulado com **múltiplas** retificações/edições | — | **Não encontrado**: o único teste de retificação (A25-C01) confirma `values.length >= 2` após **uma** retificação (`'initial'` + `'retification'`). Nenhum teste lido retifica ou edita um documento **mais de uma vez** para confirmar que o array continua crescendo (3, 4+ versões) de forma consistente | `rectify-document.spec.ts` (A25-C01, `values.length >= 2`, uma única retificação) | A confirmar |
| — | Metadados por versão (autor, data/hora da retificação ou edição) | — | **Não confirmado**: a interface usada nos testes (`VersionedValue`) só declara `versionInfo?: { type?: string }` — nenhuma asserção lida verifica autor ou data/hora **por versão individual** do array `values[]`. (A linha do tempo geral, 1.35.1, tem seu próprio registro de autor/data/hora por **ação**, mas é um mecanismo diferente — ver fronteira abaixo; não presumo que ela preencha essa lacuna do histórico de versões) | `history-document.spec.ts`, `rectify-document.spec.ts` (interface `VersionedValue` local a cada arquivo, só com `type`) | A confirmar |
| 1.35.5 | Botão/opção "histórico" visível na tela do documento | Comportamento de tela observado, não dado de preset | **Confirmado só a presença do botão**: `E18-C04` (`workflow/document.spec.ts`) verifica que a toolbar de um documento (encerrado "para mim", com fluxo iniciado) exibe uma opção que casa com `/hist[óo]rico/i`. **Não encontrei nenhum teste que clique nessa opção** nem que verifique o conteúdo da tela/drawer de histórico que ela abre — não há helper de UI dedicado (`ui/internal/`) para abrir ou ler essa tela, diferente do que existe para prazos (`ui/internal/deadlines.ts`) ou etiquetas (`ui/internal/labels.ts`, que inclui histórico de **etiqueta**, um recurso diferente — ver fronteira) | `playwright/tests/e2e/workflow/document.spec.ts` (E18-C04, verificação de presença na toolbar, via `toolbarOption`) | Confirmado (botão existe na toolbar); A confirmar (conteúdo da tela que ele abre) |
| — | Visibilidade condicional do botão "quando houver retificações ou edições" | — | **Não teria como concluir a partir da cobertura encontrada**: o único teste que verifica a presença do botão "histórico" (E18-C04) o faz num documento de fluxo de trabalho encerrado, **sem nenhuma retificação ou edição confirmada** nesse cenário — o botão aparece mesmo assim. Isso **sugere** que o botão não é condicional ao histórico ter conteúdo relevante, mas o teste não foi desenhado para checar essa condição especificamente, então não considero isso uma confirmação | `playwright/tests/e2e/workflow/document.spec.ts` (E18-C04) | A confirmar |

## Fronteiras com itens vizinhos (fora desta fatia)

- **Linha do tempo geral da tramitação** (1.35.1, já mapeada no recorte 07 como "Mapeado", sem fatia própria de preset ainda) é um mecanismo **diferente e mais amplo**: `getDocumentEvents`/`DocumentEvent` registra **todo** tipo de evento (`DISPATCH`, `REVIEW`, `ASSOCIATE_DOCUMENT`, `SECTOR_ENDED`, `ENDED`, `RESUME`, `SIGNATURE`, etc. — já citados em várias fatias anteriores), com autor/setor/data por evento. **Não presumo** que essa linha do tempo seja a mesma coisa que o "histórico" de 1.35.5 (que o próprio texto do TR restringe a retificações/edições) — são dois conceitos/mecanismos de código distintos (`values[]`/`versionInfo` vs. `getDocumentEvents`), não analisados juntos aqui.
- **Retificação** (1.35.2.3, já mapeada na fatia 09) e **Edição** (1.35.2.5, já mapeada na fatia 11) têm seus próprios achados detalhados sobre os mecanismos que **produzem** o histórico — não repetidos aqui; esta fatia olha só o histórico resultante como recurso de visualização.
- **Histórico de etiqueta/subetiqueta** (`getTagHistory`, `label-management.spec.ts`, E46-C07–C09) é um recurso **de outra entidade** (Etiqueta, não Documento/Processo) — mecanismo de UI e API totalmente separado (tem inclusive um drawer "Histórico" próprio, de fato aberto e verificado nos testes citados, ao contrário do histórico de documento). Citado só para contraste: mostra que o padrão do projeto, quando testa um "histórico" a fundo, abre a tela e verifica o conteúdo — o que não acontece para o histórico de documento.

## O que falta para este recorte virar preset executável (resumo)

- **Conteúdo real da tela/drawer de "histórico" do documento** — nunca verificado; só a presença do botão na toolbar foi confirmada (E18-C04).
- **Cobertura de edições no histórico** — mesma lacuna já registrada na fatia 11: valor `'edit'` em `versionInfo.type` só existe em comentário, nunca confirmado por asserção.
- **Histórico acumulado (3+ versões)** — não testado; só uma retificação isolada foi exercitada.
- **Metadados por versão (autor, data/hora)** — não confirmados; `versionInfo` só tem o campo `type` nos testes lidos.
- **Visibilidade condicional do botão "histórico"** — não é possível concluir se é sempre visível ou condicionada a haver retificação/edição.
- **Nenhum histórico específico integra o baseline persistente** — os CTs citados (A18, A25) criam seu próprio documento e o retificam/consultam em tempo de execução.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[../Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só o item 1.35.5 foi usado nesta fatia.
- Piloto anterior (referência, não repetida como requisito aqui): [[09 - Especificação do preset piloto (TR 1.35.2.3)]] (retificação); [[11 - Especificação do preset piloto (TR 1.35.2.5)]] (edição, inclusive a lacuna do valor `'edit'`).
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/api/services/documents.ts` (`getDocumentForAgent`, campo `values`, `isRectified`; `getDocumentEvents`, citado só como fronteira), `playwright/tests/api/processing/history-document.spec.ts` (A18-C01/C02), `playwright/tests/api/processing/rectify-document.spec.ts` (A25-C01), `playwright/tests/e2e/workflow/document.spec.ts` (E18-C04, verificação de presença do botão "histórico" na toolbar), `playwright/src/ui/internal/labels.ts` e `playwright/tests/e2e/processing/label-management.spec.ts` (E46-C07–C09, histórico de etiqueta, citado só como contraste/fronteira). Lido nesta sessão, só leitura — nenhum comando executado.
