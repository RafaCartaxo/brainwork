---
tags: [qa, conhecimento]
tipo: indice
---
# Índice — Sanidade automatizada do SOGOV (Termo de Referência)

> [!info]- Navegação
> **Índice geral da SGV-11262:** [[../0 - SGV-11262 - Índice|Índice da SGV-11262]]
> **Roadmap da iniciativa:** [[../../Roadmap - Modelo de atores e preset do TR|Roadmap — Modelo de atores e preset do TR]]
> **Hub no Notion:** [Sanidade automatizada do SOGOV — Termo de Referência](https://app.notion.com/p/3fa72f8c899080a1a1d6f421cc6d4426) — organizado em 15/10/2026: 3 subpáginas de conteúdo (Transcrição, Modelo-alvo, Matriz), 1 subpágina placeholder (Cenários de sanidade, sem cenários publicados) e uma database "Demandas relacionadas" com a SGV-12200
> **Demanda ativa que consome esta referência (Onda 1):** [[../../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/00 README|SGV-12200 — Levantamento da Onda 1 de cenários de sanidade]]
> **Frente de origem (encerrada, produziu os três documentos abaixo):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README|SGV-12082 — Mapeamento de atores e modelo do preset do TR]]

## Objetivo desta pasta

Reunir, num só lugar e independente de qual demanda está consumindo-a no momento, a **referência permanente** do Termo de Referência do SOGOV e do modelo de dados derivado dela — para que qualquer onda futura de cenários de sanidade (não só a Onda 1 da SGV-12200) tenha um ponto de partida estável. Esta pasta não decide nem aprova cenários; ela só organiza a referência que os cenários usam.

## Os três documentos canônicos

| # | Documento | Papel |
|---|---|---|
| 1 | [Termo de Referência SOGOV — Transcrição integral](<01 - Termo de Referência SOGOV - Transcrição integral.md>) | Transcrição fiel do PDF (itens 1.1–1.43), estruturada por ID, com página do PDF indicada. Texto navegável — **não substitui** o PDF original, que continua a fonte normativa. |
| 2 | [Modelo-alvo de atores, dados e estados](<02 - Modelo-alvo de atores, dados e estados.md>) | Análise derivada do TR e do produto: entidades, atributos, relações e status Confirmado/Inferido/A confirmar. Não decide canal de fornecimento. |
| 3 | [Matriz de fornecimento dos dados](<03 - Matriz de fornecimento dos dados.md>) | Análise derivada do Modelo-alvo: canal candidato de fornecimento (`.env`, seed persistente ou cenário) para cada dado/estado. Hipóteses candidatas, não decisões de arquitetura. |

Os três documentos são publicáveis como estão (sem frontmatter, sem metadados de processo) e usam citação portátil ao TR no formato `TR §ID — PDF p. N — transcrição §ID` — ver [[../../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/02 - Guia de organização e publicação no Notion|Guia de organização e publicação no Notion]] para o método completo e a auditoria de fidelidade.

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

Os três documentos foram produzidos a partir dos artefatos aprovados da **SGV-12082** (demanda encerrada em seu escopo — Fases 1–4, passos 1–10 do Roadmap): o Modelo-alvo e a Matriz de fornecimento têm origem nos documentos `04 - Modelo-alvo dos dados do preset` e `05 - Matriz de fornecimento dos dados` dessa demanda ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04]] · [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05]]), auditados e adaptados para publicação. Os 11 recortes temáticos e as 17 fatias de evidência técnica da SGV-12082 permanecem na pasta de origem, não duplicados aqui — são consulta secundária, nunca substituto desta referência.

## Notion

O hub no Notion (link acima) já está organizado: subpáginas para os três documentos canônicos, uma subpágina placeholder para "Cenários de sanidade" (sem cenários publicados — a Onda 1 segue proposta pendente de aprovação) e uma database "Demandas relacionadas" com uma linha para a SGV-12200 (URL da task em branco, nenhuma task Notion dedicada foi localizada). Auditoria de fidelidade de conteúdo (headings, tabelas, diagramas Mermaid) feita em 15/10/2026 — ver o guia de publicação linkado acima para o método.
