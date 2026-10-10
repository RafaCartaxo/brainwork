---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.28–1.29"
status: aprovado
---
# 03 - Especificação do preset piloto (itens 1.28–1.29)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Mapa geral:** [[../00 - Mapa geral]] · **Recorte-fonte:** [[../Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)|04 - Serviços, assuntos e categorias de documentos]] · **Piloto anterior:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02 - Especificação do preset piloto (TR 1.24–1.27)]]

> [!info] Escopo desta fatia (09/10/2026)
> Segunda fatia da especificação do preset: liga o recorte 04 (módulos, assuntos, serviços e categorias de documento) ao que o seed Playwright atual já prepara. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 04, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Preparação específica de cenário:** dado/estado que só alguns cenários precisam — não integra a população padrão; pode ser preparado uma única vez no ambiente persistente, sem presumir execução por teste.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Serviços, Assuntos e campos personalizados (TR 1.28)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.28, 1.28.1 | Serviço/Assunto — cadastro com nome, categoria de documento vinculada, sigilo, prazo etc. | Baseline | `BASELINE.services` (12 serviços nomeados, ligados a um módulo cada) + `makeService` (fábrica dos campos: setor, módulo, `categoryId`, prazo oficial, extensão de prazo) | `playwright/src/data/seed/baseline.ts`; `playwright/src/data/factories/seed.ts` função `makeService` | Confirmado |
| 1.28 / 1.27.8.2.o | Categoria/Subcategoria de Assuntos e Serviços (lacuna (n) do mapa — relação inferida pelo nome, não descrita pelo TR) | — | `makeService` tem um campo `categoryId` no payload, hoje sempre `null` em todos os serviços do baseline — **o campo existe na API, mas nenhum serviço do seed o usa**; não há entidade "Categoria de Assuntos e Serviços" separada representada no seed | `seed.ts`, função `makeService` (`categoryId: null`) | Confirmado (campo existe, não exercitado); lacuna (n) do TR permanece sem relação com isso — são conceitos distintos, não presumo equivalência |
| 1.28.1.2.1 | Tipos de campo personalizado (enum: texto, número, e-mail, mapa, arquivo, seleção de pessoas/setores etc.) | Preparação específica de cenário (cada módulo ativa só os tipos que seus casos usam) | Cobertura parcial confirmada: `file` (módulo DO), `bigText` (módulos CO/ASS/accessKey), campos `informativeText-*` nomeados (SGV-8383). **Não verifiquei neste recorte** os demais tipos do enum do TR (mapa, link, data/hora, escolha única/múltipla, seleção de referência Pessoas/Setores) — não presumo ausência, só não busquei | `baseline.ts`; `seed.ts`, função `makeModuleProperties` | Confirmado (parcial); A confirmar (restante do enum) |

## Categorias de documento (TR 1.29)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.29.1 | Categoria de documento (base, 3 valores): Documento oficial, Comunicação oficial, Processo administrativo | Baseline | **Confirmação direta no código**: as fábricas atuais do seed configuram exatamente os 3 valores do TR para `documentType` — `'official_document'` (módulo DO), `'official_communication'` (módulo CO), `'administrative_process'` (módulo PA e default da fábrica `makeModule`). A query GraphQL (`module.ts`) confirma que o campo existe e é lido; **não confirma** que o schema do backend aceite só esses 3 valores — isso não foi verificado | `seed.ts`, funções `makeModule`/`makeModuleDO`/`makeModuleCO`; `module.ts` (campo `documentType` na query GraphQL) | Confirmado (uso no seed); A confirmar (limite do schema) |
| 1.29.2–1.29.9 | Categorias específicas (8 valores: Memorando, Circular, Ofício, Processo administrativo genérico, Solicitação externa, Ouvidoria, e-SIC, Ato oficial) | — | **Não verificado nesta rodada.** Os módulos do baseline (PA/DO/CO/PU/ASS + variantes de workflow) não têm, no código que li, um sub-enum que nomeie essas 8 categorias especificamente — pode existir em outro nível (regras do módulo, tipo de serviço) não lido aqui. Não presumo ausência, só não encontrei | `baseline.ts`, `seed.ts` (módulos lidos nesta rodada) | A confirmar |
| 1.29.10 | Processo urbanístico / Zoneamento — categoria-base não declarada pelo TR (ver recorte 04, dúvida e "Contexto de produto") | Preparação específica de cenário | **Confirmação de código, mais forte que a documentação de produto já citada no recorte 04**: o módulo `PU` é criado via `makeModule({ name: b.modules.PU, userId, isUrbanisticProcess: true })` — **sem sobrescrever `documentType`**, que permanece no valor-padrão `'administrative_process'` da fábrica. Ou seja, **no seed atual**, "processo urbanístico" é configurado como um módulo do tipo `administrative_process` com a flag `isUrbanisticProcess: true` ligada. Isso não prova que o schema do backend não tenha ou não aceite um `documentType` próprio pra zoneamento — só que o seed, hoje, não usa um. Confirma, por um caminho independente (código, não documentação do Notion), a mesma conclusão já registrada no recorte 04: é opção/variação de configuração dentro de Processo Administrativo, **não presumo que isso faça parte do preset padrão de todo órgão** — é um módulo específico (`Precondition PU API`) que só existe porque os CTs que o usam precisam dele | `provision.ts` (criação do módulo `PU`); `seed.ts`, função `makeModule` (default `isUrbanisticProcess: false`); `module.ts` (campo `isUrbanisticProcess` na query GraphQL) | Confirmado (configuração do seed); A confirmar (limite do schema) |
| 1.29.10.4 | Zona, Categoria de uso (entidades de zoneamento) | — | Não localizado no código consultado nesta rodada — a leitura cobriu módulos/serviços/categorias de documento, não entidades de zoneamento especificamente; não presumo ausência | — | A confirmar |

## O que falta para este recorte virar preset executável (resumo)

- **Categoria/Subcategoria de Assuntos e Serviços** (1.27.8.2.o, lacuna (n) do mapa) — o campo `categoryId` existe na API mas nenhum serviço do baseline o usa; não há exemplo no seed para comparar com a relação inferida do TR.
- **8 categorias específicas de documento** (1.29.2–1.29.9) — não confirmei se/como o seed as distingue; fica como ponto a verificar antes de qualquer cenário que dependa de uma categoria específica.
- **Zona / Categoria de uso** (1.29.10.4) — não localizadas no código lido; se um cenário de sanidade precisar de zoneamento, essa parte do seed (se existir) ainda não foi conferida.
- **Processo urbanístico** (1.29.10) — já tem módulo próprio no seed (`PU`), mas é tratado como módulo específico de cenário (preparação, não baseline geral); confirmado **na configuração do seed** como variação de Processo Administrativo — não concluo isso sobre o produto em geral nem sobre o schema do backend, e não presumo que faça parte do preset padrão de todo órgão.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[../Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)]].
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/data/seed/baseline.ts`, `playwright/src/data/seed/provision.ts`, `playwright/src/data/factories/seed.ts`, `playwright/src/api/services/module.ts`. Lido nesta sessão, só leitura — nenhum comando executado.
- Documentação de produto já citada no recorte 04 (não repetida aqui como requisito do TR): [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]].
