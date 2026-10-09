---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.30–1.31"
status: aprovado
---
# 04 - Especificação do preset piloto (itens 1.30–1.31)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recorte-fonte:** [[Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)|05 - Fluxos de trabalho e modelos de documentos]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02 (TR 1.24–1.27)]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03 (TR 1.28–1.29)]]

> [!info] Escopo desta fatia (09/10/2026)
> Terceira fatia da especificação do preset: liga o recorte 05 (Fluxo de trabalho, Etapa, Despacho, Modelo simples, Documento automatizado) ao que o seed Playwright atual já prepara. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 05, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Preparação específica de cenário:** dado/estado que só alguns cenários precisam — não integra a população padrão; pode ser preparado uma única vez no ambiente persistente, sem presumir execução por teste.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Fluxo de trabalho, Etapa e Despacho (TR 1.30)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.30 | Fluxo de trabalho — status (ativo/inativo/rascunho) | Baseline | O seed cria workflows com `status: 'ACTIVE'` apenas — não encontrei `INACTIVE`/rascunho no código lido. Não presumo ausência desses outros valores, só não os vi | `playwright/src/data/factories/seed.ts`, funções `makeWorkflowInput`/`makeMultiStepDispatchWorkflowInput` (`status: 'ACTIVE'`) | Confirmado (ACTIVE); A confirmar (demais valores) |
| 1.30, 1.30.1 | 3 configurações de Fluxo de trabalho no baseline | Baseline | `BASELINE.modules.workflow` (3 etapas, etapa 02 exige despacho+assinatura), `workflowAttachment` (idêntico, mas exige também o anexo como local de assinatura), `workflowFiveSteps` (5 etapas, todas só com despacho obrigatório, sem assinatura — base do cenário de retificação) | `baseline.ts` (nomes dos módulos); `provision.ts` L.315-360 (criação dos 3 workflows); `seed.ts`, funções `makeWorkflowInput`/`makeMultiStepDispatchWorkflowInput` | Confirmado |
| 1.30.1 | Etapa — nome, setor responsável, regras de tramitação (setores que podem visualizar/participar/retroceder-avançar; setores que podem encerrar) | Baseline | Cada `step` do workflow tem `name`, `position`, `sectorResponsibleId`, e as listas `canParticipate`, `canMoveForwardOrBackward`, `canClose` (por setor) — mapeiam diretamente nas regras de tramitação do TR | `seed.ts`, função `makeWorkflowInput` (objeto `base` dos steps) | Confirmado |
| 1.30.2 | Despacho na etapa — customizado, com assinatura obrigatória opcional, bloqueante ao avanço | Baseline (no workflow `workflow`) + preparação específica de cenário (variante com anexo) | Cada `dispatches` de uma etapa tem `name`, `canEmitDispatch`, `count`, `onlyResponsibleEmit`, `signatures: {isSequential, signers}`. O local do despacho (`dispatchLocations`) é `['DISPATCH']` por padrão; incluir `DISPATCH_ATTACHMENT` faz o backend **exigir** anexo pra emitir — usado no módulo `workflowAttachment` | `seed.ts`, função `makeWorkflowInput` (comentário explícito sobre `dispatchLocations`) | Confirmado |
| 1.30.3 | Regras de transição (avanço só após ações obrigatórias; retrocesso de 1 etapa com justificativa; checklist exibido) | — | Não verificado nesta rodada — são regras de comportamento de tela/fluxo, não necessariamente dados do seed; não encontrei isso nos arquivos de preparação lidos. Não presumo ausência | — | A confirmar |

## Modelo simples e Documento automatizado (TR 1.31)

> **Importante sobre "Baseline × cenário" nesta seção:** confirmei em `provision.ts` que nenhuma das funções de Modelo simples/Documento automatizado é chamada ali — `makeDocumentModel`/`createDocumentModel` e `makeAutomatedDocumentModel`/`generateAutomatedDocumentModel` só são usadas em tempo de execução, dentro de specs de teste individuais (`playwright/tests/api/models/simple-model.spec.ts`, `automated-model.spec.ts`, `model-group.spec.ts`, `revoke-automated.spec.ts`; `playwright/tests/e2e/models/models.spec.ts`, `automated-document.spec.ts`). **Não integram o baseline persistente** — cada teste cria o seu próprio modelo quando precisa, não há um modelo pré-existente reutilizável no seed atual.

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.31.1.1 | Modelo simples — nome, herança de dados (sim/não), vínculo com Categoria/Serviço/Assunto **obrigatório independente da herança**, corpo, exclusividade (próprio/compartilhado) | Preparação específica de cenário — criada em tempo de execução pelo próprio teste (`simple-model.spec.ts`), não por `provision.ts` | `makeDocumentModel`: `inheritanceType: 'WITHOUT_INHERITANCE'` e `sharedType: 'NO_SHARE'` são, segundo a documentação do projeto (`docs/business-rules/api/simple-document-model.md`), os **únicos valores confirmados por captura real** desses dois enums — outros valores (incluindo o de "com herança") não foram explorados/capturados. `sharedType: 'NO_SHARE'` significa **"Não desejo compartilhar"** (mesmo enum `SharedType` documentado em `label-management.e2e.md`); com `sectorsIds: []`. **Não é "exclusividade por setor"** — é o valor de "não compartilhado"; não confirmei se existe uma opção equivalente a "próprio do servidor" | `playwright/src/api/services/models.ts`, função `makeDocumentModel`; `docs/business-rules/api/simple-document-model.md` | Confirmado (valores vistos); A confirmar (demais valores do enum; opção "próprio do servidor") |
| 1.31.1.2 | Histórico de alterações do modelo (criação/edição/duplicação) | — | Não verificado nesta rodada | — | A confirmar |
| 1.31.2, 1.31.2.1.1–2 | Documento automatizado — nome, vínculo com Categoria/Serviço/Assunto | Preparação específica de cenário — criado em tempo de execução pelo próprio teste (`automated-model.spec.ts`), não por `provision.ts` | `makeAutomatedDocumentModel`: `name`, `moduleMatterServiceId` (vínculo, singular — diferente do `moduleMatterServiceIds` plural do Modelo simples) | `models.ts`, função `makeAutomatedDocumentModel`/`generateAutomatedDocumentModel` | Confirmado |
| 1.31.2.1.3 | Estilização de cabeçalho e rodapé | Preparação específica de cenário | `headerImage`/`headerImagePosition`/`headerImageSize`/`headerText` e os mesmos 4 campos para `footer` | `models.ts`, função `makeAutomatedDocumentModel` | Confirmado |
| 1.31.2.1.3.1 | Conteúdo do escopo do modelo, incluindo herança de dados | Preparação específica de cenário | `contentText` montado com campos de atalho (@mentions) vindos de `getAllAutomatedDocumentMentionFields`/`inheritanceItems` — é o mecanismo de herança de dados do documento automatizado | `models.ts`, funções `getAllAutomatedDocumentMentionFields`, `makeAutomatedDocumentModel` | Confirmado |
| 1.31.2.1.3.2 | Validade pré-definida, contada a partir da emissão | Preparação específica de cenário | `validityType: 'STANDARD'`, `validityUnit: 'YEARS'`, `validityValue: 1` estão presentes no payload, **mas `hasValidity: false`** — a validade **não está ativada** nessa configuração padrão da fábrica. Os campos existem e batem com o formato do requisito, mas a fábrica atual não exercita a validade como ativa; não encontrei nenhum teste que sobrescreva `hasValidity` para `true` | `models.ts`, função `makeAutomatedDocumentModel` (`hasValidity: false`, linha confirmada por busca direta) | Confirmado (campos existem; validade desativada por padrão) |
| 1.31.3 | Edição/exclusão de modelos (ambos os tipos) com permissão, com histórico | — | Não verificado nesta rodada | — | A confirmar |
| — | **Achado fora do TR deste recorte**: "Grupo de Modelos" (`makeModelGroup`/`createModelGroup`) agrupa Documentos Automatizados já existentes | — | Entidade de produto sem correspondência no texto do recorte 05 — não presumo que seja exigência do TR; registro só como achado de código, para referência futura | `models.ts`, funções `makeModelGroup`/`createModelGroup` | Achado de produto (fora do TR) |

## O que falta para este recorte virar preset executável (resumo)

- **Status de Fluxo de trabalho** (inativo/rascunho) — só `ACTIVE` foi visto no código; os demais valores do enum do TR não foram localizados nem descartados.
- **Modelo simples e Documento automatizado** — o baseline atual não contém modelos reutilizáveis; os testes os criam em tempo de execução (`simple-model.spec.ts`, `automated-model.spec.ts` e afins), não `provision.ts`. A forma de preparar modelos persistentes para a sanidade fica em aberto.
- **Enum completo de `inheritanceType`/`sharedType`** (Modelo simples) — a documentação do projeto confirma que só os valores "sem herança" (`WITHOUT_INHERITANCE`) e "não compartilhado" (`NO_SHARE`) foram capturados por evidência real; os demais valores desses enums (incluindo "com herança" e a opção "próprio do servidor") seguem sem captura.
- **Validade do Documento automatizado** (1.31.2.1.3.2) — os campos de validade existem na fábrica, mas `hasValidity: false` por padrão: a validade não está ativa na configuração atual, apesar de bater com o formato do requisito do TR.
- **Regras de transição de etapa, histórico de modelos, edição/exclusão com permissão** (1.30.3, 1.31.1.2, 1.31.3) — nenhum dos três foi verificado nesta rodada; não são dados de seed óbvios, podem ser comportamento de tela.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)]].
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/data/seed/baseline.ts`, `playwright/src/data/seed/provision.ts`, `playwright/src/data/factories/seed.ts`, `playwright/src/api/services/models.ts`, `playwright/tests/api/models/simple-model.spec.ts` e `automated-model.spec.ts` (confirmação de que são chamados em tempo de execução, não por `provision.ts`). Lido nesta sessão, só leitura — nenhum comando executado.
- Documentação técnica do repositório: `docs/business-rules/api/simple-document-model.md` (valores confirmados por captura real de `inheritanceType`/`sharedType`); `docs/commands/api/label-management.e2e.md` (significado de `sharedType: NO_SHARE`).
