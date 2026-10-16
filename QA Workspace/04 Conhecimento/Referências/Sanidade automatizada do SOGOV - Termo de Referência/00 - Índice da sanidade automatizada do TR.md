---
tags: [qa, conhecimento]
tipo: indice
---
# Índice — Sanidade automatizada do SOGOV (Termo de Referência)

> [!info]- Navegação
> **Índice geral da SGV-11262:** [Índice da SGV-11262](<../../../02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/Conhecimento/0 - SGV-11262 - Índice.md>)
> **Roadmap da iniciativa:** [Roadmap — Modelo de atores e preset do TR](<../../../02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/Roadmap - Modelo de atores e preset do TR.md>)
> **Hub no Notion:** [Sanidade automatizada do SOGOV — Termo de Referência](https://app.notion.com/p/3fa72f8c899080a1a1d6f421cc6d4426) — publicado em 15/10/2026 com 4 subpáginas (Transcrição, Modelo-alvo, Matriz, e Cenários de sanidade como placeholder sem cenários publicados). Reorganizado em 16/10/2026: hub movido para dentro da página "Sogov" (subpáginas inalteradas); a database "Demandas relacionadas" — histórico: nasceu como filha direta do hub em 15/10/2026 — foi movida para "Sogov > Backlog", com a linha da SGV-12200
> **Demanda ativa que consome esta referência (Onda 1, independente desde 16/10/2026):** [[../../../02 Demandas/DEV/SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/00 README|SGV-12200 — Levantamento da Onda 1 de cenários de sanidade]]
> **Frente de origem (encerrada, produziu os três documentos abaixo):** [SGV-12082 — Mapeamento de atores e modelo do preset do TR](<../../../02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README.md>)

## Objetivo desta pasta

Reunir, num só lugar e independente de qual demanda está consumindo-a no momento, a **referência permanente** do Termo de Referência do SOGOV e do modelo de dados derivado dela — para que qualquer onda futura de cenários de sanidade (não só a Onda 1 da SGV-12200) tenha um ponto de partida estável. Esta pasta não decide nem aprova cenários; ela só organiza a referência que os cenários usam.

## Os três documentos canônicos

| # | Documento | Papel |
|---|---|---|
| 1 | [Termo de Referência SOGOV — Transcrição integral](<01 - Termo de Referência SOGOV - Transcrição integral.md>) | Transcrição fiel do PDF (itens 1.1–1.43), estruturada por ID, com página do PDF indicada. Texto navegável — **não substitui** o PDF original, que continua a fonte normativa. |
| 2 | [Modelo-alvo de atores, dados e estados](<02 - Modelo-alvo de atores, dados e estados.md>) | Análise derivada do TR e do produto: entidades, atributos, relações e status Confirmado/Inferido/A confirmar. Não decide canal de fornecimento. |
| 3 | [Matriz de fornecimento dos dados](<03 - Matriz de fornecimento dos dados.md>) | Análise derivada do Modelo-alvo: canal candidato de fornecimento (`.env`, seed persistente ou cenário) para cada dado/estado. Hipóteses candidatas, não decisões de arquitetura. |

Os três documentos são publicáveis como estão (sem frontmatter, sem metadados de processo) e usam citação portátil ao TR no formato `TR §ID — PDF p. N — transcrição §ID` — ver [[../../../02 Demandas/DEV/SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/02 - Guia de organização e publicação no Notion|Guia de organização e publicação no Notion]] para o método completo e a auditoria de fidelidade.

## Cadeia de referência

```text
PDF do TR (SGV-12082/Fontes/, fonte normativa, encerrada)
    ↓ transcrição fiel, por ID e página
01 - Termo de Referência SOGOV - Transcrição integral
    ↓ análise derivada (TR + produto)
02 - Modelo-alvo de atores, dados e estados
    ↓ canal candidato de fornecimento
03 - Matriz de fornecimento dos dados
    ↓ referência para propor cenários
Ondas de cenários de sanidade (ex.: Onda 1 — SGV-12200)
```

Cada onda de cenários (atual ou futura) consome os três documentos acima como referência, sem precisar duplicá-los nem esperar que uma onda específica termine para outra começar.

## Origem e histórico

Os três documentos foram produzidos a partir dos artefatos aprovados da **SGV-12082** (demanda encerrada em seu escopo — Fases 1–4, passos 1–10 do Roadmap): o Modelo-alvo e a Matriz de fornecimento têm origem nos documentos `04 - Modelo-alvo dos dados do preset` e `05 - Matriz de fornecimento dos dados` dessa demanda ([04](<../../../02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset.md>) · [05](<../../../02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados.md>)), auditados e adaptados para publicação. Os 11 recortes temáticos e as 17 fatias de evidência técnica da SGV-12082 permanecem na pasta de origem, não duplicados aqui — são consulta secundária, nunca substituto desta referência.

## Notion

O hub no Notion (link acima) está organizado com subpáginas para os três documentos canônicos e uma subpágina placeholder para "Cenários de sanidade" (sem cenários publicados — a Onda 1 segue proposta pendente de aprovação). A database "Demandas relacionadas" — histórico: filha direta do hub em 15/10/2026 — vive hoje em "Sogov > Backlog" desde a reorganização de 16/10/2026, com uma linha para a SGV-12200 (URL da task em branco, nenhuma task Notion dedicada foi localizada). Auditoria de fidelidade de conteúdo (headings, tabelas, diagramas Mermaid) feita em 15/10/2026 — ver o guia de publicação linkado acima para o método.
