---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.33"
status: em levantamento
---
# 06 - Especificação do preset piloto (item 1.33)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recorte-fonte:** [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]]

> [!info] Escopo desta fatia (09/10/2026)
> Quinta fatia da especificação do preset: liga **só o item 1.33 (Mesa de trabalho)** do recorte 07 ao que o seed Playwright atual já prepara. O recorte-fonte 07 reúne 1.33–1.35 (Mesa, Etiquetas, Tramitação); por decisão do Codex, etiquetas (1.34) e tramitação/despacho (1.35) ficam para fatias futuras separadas, para não ampliar demais esta entrega. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega — aqui, especialmente, o que `provision.ts` inicializa para todo agente novo.
- **Preparação específica de cenário:** dado/estado que só alguns cenários precisam, ou comportamento exercitado só em tempo de teste (ex.: alternar o modo de visualização para testar os dois).
- **Comportamento de tela (não é dado de preset):** interações de UI que não correspondem a um dado/estado persistido — registradas só para não serem confundidas com preset.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Mesa de trabalho — preferências, status e navegação (TR 1.33)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.33.3.1, 1.33.3.2 | Visualização da mesa: Kanban (padrão) ou Lista | **Baseline** — `provision.ts` inicializa isso para todo agente novo | `changeWorkboardViewMode(api, viewMode)` — valores confirmados no código: `'panel'` (Kanban) e `'list'`. `provision.ts` chama `initializeWorkboardPreferences`, que define o modo `'panel'` pra cada agente **recém-criado** — comentário no código explica que um agente novo tem `preferences` vazio e a mutation falharia (`something-went-wrong`) sem essa inicialização prévia. É uma preferência real, persistida por agente (não comportamento efêmero de tela) | `playwright/src/data/seed/provision.ts`, função `initializeWorkboardPreferences`; `playwright/src/api/services/documents.ts`, função `changeWorkboardViewMode`; `playwright/tests/api/workboard/panel.spec.ts` (testa os dois modos) | Confirmado |
| 1.33.3.6, 1.35.2.1 | Status de Documento/Processo e da Mesa (5 valores: Em aberto, Em elaboração, Em tramitação, Pausado, Encerrado) | Baseline (consulta) | **Confirmação direta e precisa**: a consulta `getWorkboardDocuments` (`documentObjectsByAllStatus`) usa o parâmetro `includeDocumentContents: { OPEN, DRAFT, PROCESSING, PAUSED, CLOSED }` — 5 chaves que batem 1:1 com os 5 valores do enum do TR (Em aberto=OPEN, Em elaboração=DRAFT, Em tramitação=PROCESSING, Pausado=PAUSED, Encerrado=CLOSED). Por padrão, a consulta **não inclui** `CLOSED` (detalhe operacional da query, não do enum em si) | `playwright/src/api/services/documents.ts`, função `getWorkboardDocuments` | Confirmado |
| 1.33.3.7 | Reabertura de documentos encerrados | Preparação específica de cenário | `reopenDocumentInSector` (`reopenDocumentObjectInSector`) existe como função dedicada | `documents.ts`, função `reopenDocumentInSector` | Confirmado |
| 1.33.1 | Usuário alterna entre setores | Baseline (mecanismo) + preparação específica de cenário (mesas alheias) | `changeLastSectorAccessed` muda o setor ativo da sessão (já usado em `initializeWorkboardPreferences` e em cenários de permissão por setor — ver piloto 1.28–1.29, teste E64). `othersWorkboard` (mesas alheias: acesso à mesa de outro setor, com `canDownload`) é configurado em identidades específicas do baseline (ex.: `agentThird`) — é uma preparação já presente para servidores dedicados a isso, não para todo agente | `playwright/src/api/services/organizational.ts`, função `changeLastSectorAccessed`; `baseline.ts` (`agentThird.othersWorkboard`); `users.ts` (campo `othersWorkboard`) | Confirmado |
| 1.33.3, 1.33.3.3, 1.33.3.4 | Mesa com alertas de prazo/novas demandas/pendências, independente do setor ativo | Baseline (consulta) | `getWorkboardDocuments` aceita parâmetros de filtro/alerta: `deadline`, `deadlineFromDashboard`, `newDocuments`, `signaturePendencies`, `reviewPendencies`, `mentionPendencies` — nomes batem com os conceitos do TR (prazo, novas demandas, pendência de assinatura/revisão), mas são **toggles de consulta**, não necessariamente "alertas" no sentido de notificação ativa — não presumo equivalência total com o conceito de "alerta" do TR, só que os dados/filtros subjacentes existem | `documents.ts`, função `getWorkboardDocuments` (objeto `defaults`) | Confirmado (existência dos filtros); Inferido (equivalência com "alerta") |
| 1.33.3.5 | Filtragem por prazos vencidos/próximos | Baseline (consulta) | Parâmetro `deadline` (booleano) na mesma consulta | `documents.ts`, função `getWorkboardDocuments` | Confirmado |
| 1.33.4 | Filtros/busca/ordenação (11 critérios: palavra-chave, pessoas, CPF, CNPJ, alfabética, assinatura pendente, revisão pendente, status, módulo, assunto/serviço, período) | Baseline (consulta) | Confirmei nos parâmetros da mesma consulta: `term` (palavra-chave), `orderBy` (`'MOST_RECENT_UPDATED'` — ordenação, mas não confirmei se há a opção alfabética específica do TR), `signaturePendencies`, `reviewPendencies`, `sector`, `deadline`. **Não confirmei neste nível de leitura** os parâmetros de pessoas/CPF/CNPJ/módulo/assunto-serviço especificamente para esta consulta — podem existir dentro do objeto `filter`, que não explorei por completo nesta rodada | `documents.ts`, função `getWorkboardDocuments` | Confirmado (parte dos critérios); A confirmar (restante) |
| 1.33.5, 1.33.5.1–3 | Nos documentos da mesa: setor responsável, data/hora última atividade, notificações de novas interações | — | `WorkboardItem` (tipo de retorno) só declara `id`, `documentCode`, `trackerCode` explicitamente, com `[field: string]: unknown` para o resto — não cheguei ao shape completo da query GraphQL (`Q.documentObjectsByAllStatus`) para confirmar se esses 3 campos específicos vêm na resposta | `documents.ts`, interface `WorkboardItem` | A confirmar |
| 1.33.6 | Ferramenta de rastreio/busca ampla por toda a organização (não só a mesa em visualização) | Baseline (consulta) | `trackDocumentObjects` — comentário no código confirma que é a tela "Rastrear documentos", com parâmetro `includeOtherSectors` (bate com "não só na mesa em visualização") e `searchContent` (expande a busca pro conteúdo/despachos, não só campos indexados) | `documents.ts`, função `trackDocumentObjects` | Confirmado |
| 1.33.2, 1.33.2.1 | Resumo inicial (tela de boas-vindas): contagem de Em aberto, Em tramitação, Concluído, Assinaturas pendentes, Demandas vencendo/vencidas | — | Não encontrei uma consulta dedicada de "resumo"/"dashboard" de boas-vindas nos arquivos lidos (`documents.ts`, `organizational.ts`, `users.ts`). É possível que a mesma `getWorkboardDocuments`/`documentObjectsByAllStatus` sirva de base para esses números (já que agrupa por status), mas não confirmei isso — não presumo | — | A confirmar |

## O que falta para este recorte virar preset executável (resumo)

- **Resumo da tela de boas-vindas (1.33.2/1.33.2.1)** — não localizei uma consulta dedicada; pode reaproveitar `getWorkboardDocuments`, mas isso não foi confirmado.
- **Campos por documento na mesa (1.33.5.1–3)** — setor responsável, última atividade e notificações não foram confirmados no shape de retorno consultado nesta rodada (ficaria pra uma leitura mais profunda do arquivo de queries GraphQL).
- **Critérios de filtro de pessoas/CPF/CNPJ/módulo/assunto-serviço (parte de 1.33.4)** — não confirmados nesta rodada; podem estar dentro do objeto `filter` não totalmente explorado.
- **Diferença baseline × cenário já fica clara**: o modo de visualização (`panel`/`list`) e o setor ativo são inicializados pelo próprio `provision.ts` pra todo agente novo (baseline); mesas alheias (`othersWorkboard`) são configuradas só em identidades dedicadas a esse cenário.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só a parte referente a 1.33 foi usada nesta fatia.
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/data/seed/provision.ts` (`initializeWorkboardPreferences`), `playwright/src/api/services/documents.ts` (`changeWorkboardViewMode`, `getWorkboardDocuments`, `reopenDocumentInSector`, `trackDocumentObjects`), `playwright/src/api/services/organizational.ts` (`changeLastSectorAccessed`), `playwright/src/api/services/users.ts` (campo `othersWorkboard`), `playwright/src/data/seed/baseline.ts`, `playwright/tests/api/workboard/panel.spec.ts`. Lido nesta sessão, só leitura — nenhum comando executado.
