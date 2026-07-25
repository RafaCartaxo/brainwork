---
tags:
  - qa
  - triagem
sprint: SP15
status: em_andamento
data: 2026-07-17
responsavel: Rafael
---
# Triagem SP15 — Engenharia (BUG'S)

> [!info] Sprint 14/07 → 28/07, em andamento (29,33%)
> Fontes: view `[SP15 - 2026] Engenharia (BUG'S)` do Notion (17/07, reconciliada 22/07) + view `Release: 23/07/2026 12.35.36.2` (24/07, 41 itens — cruza com outros QAs).
> Progresso: **44/82** batidos.
> Arquivo original completo em [[../Triagem - SP15|Triagem - SP15]] (legado, referência).

## Por estágio QA

| # | Estágio | O que entra | Batidos |
|---|---------|------------|---------|
| 01 | [[01-acao-imediata|Ação imediata]] | Testável agora: Homologação, Teste dev (com fix deployado) | 8/20 |
| 02 | [[02-em-validacao|Em validação]] | Cards com QA ativa (CTs em execução em DEV ou HML) | — |
| 03 | [[03-aguardando-deploy|Aguardando deploy]] | Aprovado em DEV (aguardando HML) ou HML (aguardando release) | — |
| 04 | [[04-a-revisar|A revisar]] | Revisar MR, sem critérios, investigar descarte, refinar | 6/18 |
| 05 | [[05-aguardando-terceiros|Aguardando terceiros]] | Em dev, impedimento, CX, aguardando sprint/priorização | 1/12 |
| 06 | [[06-acompanhamento|Acompanhamento]] | Produção, outro QA aprovou, decididos, órfãos do export | 27/32 |

> [!tip] Como usar
> Cada arquivo é focado — abra o estágio relevante pro que você precisa fazer agora. Os checkboxes e wikilinks foram preservados do arquivo original. O progresso geral é atualizado aqui no README (ou peça "atualiza o progresso da triagem SP15").

## Decisões e alertas recentes

- **24/07 — SGV-4873**: ⚠️ NÃO TESTAR. Notion "Disponível para homologação" mas `fix/4873` NÃO mergeado; mesa de refinamento bloqueada (conflito com regra de retificação).
- **24/07 — SGV-8977**: 🚨 Notion "Reaberto". Coincide com risco do card (timeout 10s não comprovado). Confirmar com Rafael/time.
- **23/07 — 9633/3820/8574**: Consolidadas na 9633 (master). 3820 e 8574 duplicadas.
- **22/07 — Export ainda incompleto**: 53/75 cards. "Load more" do Notion corta. Rolar até o fim antes do próximo export.

## Registro da triagem

- 2026-07-17 — Lista criada (53/60 cards)
- 2026-07-17 — Primeira batida (10/53)
- 2026-07-22 — Reconciliação com novo export (53 cards, 11 novos, 20 mudanças)
- 2026-07-23 — Consolidação 9633/3820/8574
- 2026-07-24 — Reconciliação com view Release (41 itens, +17 novos)
- 2026-07-24 — Batidas do dia (7935, 6083, 5360, 6348, 10246, 5269)
- 2026-07-25 — Reorganizado em 6 arquivos por estágio QA (visão de [[../../Sistema/Contexto/FLUXOS|esteiras]])
