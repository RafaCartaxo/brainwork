---
tags: [qa]
task: "SGV-12200"
tipo: "guia-publicacao"
status: pronto-para-publicacao
---
# Guia de organização e publicação no Notion

> [!info]- Navegação
> **README do card (SGV-12200):** [[00 README|Abrir README do card]]
> **Proposta da Onda 1 (inalterada por este trabalho):** [[01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]]
> **Índice da sanidade automatizada do TR (ponto de entrada dos documentos canônicos, em 04 Conhecimento):** [[QA Workspace/04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/00 - Índice da sanidade automatizada do TR|00 - Índice]]
> **Transcrição canônica:** [[QA Workspace/04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/01 - Termo de Referência SOGOV - Transcrição integral|01 - Termo de Referência SOGOV - Transcrição integral]]
> **Modelo-alvo canônico:** [[QA Workspace/04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/02 - Modelo-alvo de atores, dados e estados|02 - Modelo-alvo de atores, dados e estados]]
> **Matriz de fornecimento canônica:** [[QA Workspace/04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/03 - Matriz de fornecimento dos dados|03 - Matriz de fornecimento dos dados]]
> **Fonte normativa (PDF canônico, permanece na SGV-12082 dentro da SGV-11262, encerrada, não duplicado):** [[Termo de Referência SOGOV.pdf]]
> **Artefatos de origem auditados (SGV-12082, encerrada, não editados):** [[04 - Modelo-alvo dos dados do preset]] · [[05 - Matriz de fornecimento dos dados]]

> [!important] Publicado no Notion em 15/10/2026
> Este guia é **interno** (QA/vault) e documenta como os três documentos canônicos (agora em `04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/`) foram produzidos, revisados, auditados e publicados no hub do Notion. Ele próprio **não é publicável** — pode citar o vault, datas, decisões e metodologia à vontade. Os três documentos canônicos (transcrição, modelo-alvo e matriz de fornecimento) é que são publicáveis — nenhum deles contém o que está neste guia.
>
> **Estado atual:** o hub já está organizado — ver §2 para a estrutura final e §3 para o método/auditoria de publicação.

## 1. Mapa de conteúdo

| Camada | Papel | Onde vive | Observação |
|---|---|---|---|
| PDF original do TR | Fonte normativa única (canônica) | `SGV-12082/Fontes/Termo de Referência SOGOV.pdf` (SGV-12082, encerrada, não reaberta) | **Não duplicado** — a transcrição aponta para ele, nunca o substitui. |
| Transcrição integral canônica | Texto navegável, pronto para publicação | `04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/01 - ...md` | Estruturada por IDs originais 1.1–1.43 (mais 1.27.10/1.27.11 como headings próprios), com página do PDF indicada; sem frontmatter, sem metadados de processo. |
| Modelo-alvo canônico | Análise derivada — entidades, atributos, relações e status Confirmado/Inferido/A confirmar | `04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/02 - ...md` | Auditado contra o artefato de origem 04 da SGV-12082; toda referência ao TR usa citação portátil (§4). |
| Matriz de fornecimento canônica | Análise derivada — canal candidato de fornecimento por dado/estado | `04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/03 - ...md` | Auditada contra o artefato de origem 05 da SGV-12082; mesma convenção de citação do TR. |
| Recortes temáticos, mapa geral, matriz de atores (vault) | Leitura/análise interna de QA | `SGV-12082/01 Modelo do preset/` | Não publicados; usados só como checagem secundária de cobertura — nunca substituto da fonte. |
| Artefatos de origem 04/05 (SGV-12082, encerrada) | Fonte de auditoria dos documentos canônicos | `SGV-12082/01 Modelo do preset/` | Não editados por este trabalho. |

Esta referência passou por dois locais no vault: de `SGV-12200/00 QA/Conteúdo para Notion/` para `SGV-11262/Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/` (15/10/2026), e dali para `04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/` (16/10/2026) — reflete que a referência permanente do TR não é específica da Onda 1 nem da própria SGV-11262, servindo a qualquer onda futura de cenários mesmo após o encerramento da iniciativa que a produziu. Ver [[QA Workspace/04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/00 - Índice da sanidade automatizada do TR|00 - Índice]] para a cadeia completa TR → Modelo-alvo → Matriz → ondas de cenários.

## 2. Estrutura no Notion

> [!note] Histórico — publicação original em 15/10/2026
> O hub (criado por Rafael, título já correto: "Sanidade automatizada do SOGOV - Termo de Referência") foi publicado como página solta (sem página-avó), com as 4 subpáginas abaixo e a database "Demandas relacionadas" como **filha direta do hub**.

**Estado atual (reorganizado em 16/10/2026, a pedido de Rafael):**

```
Sogov
├── Backlog
│   └── Demandas relacionadas (database — Título/ID/Papel/Estado/URL da task; 1 linha: SGV-12200, URL da task em branco)
└── Sanidade automatizada do SOGOV - Termo de Referência (hub) — [link](https://app.notion.com/p/3fa72f8c899080a1a1d6f421cc6d4426)
    ├── Termo de Referência SOGOV — Transcrição integral — conteúdo integral da transcrição canônica, 45 headings (1.1–1.43, com 1.27.10/1.27.11 próprios)
    ├── Modelo-alvo de atores, dados e estados — conteúdo integral do documento canônico 02: 10 tabelas, 6 diagramas Mermaid, seções 1–11
    ├── Matriz de fornecimento dos dados — conteúdo integral do documento canônico 03: 5 tabelas (fatias C1–C2 a C6), seções 1–7
    └── Cenários de sanidade — placeholder: nenhum cenário publicado; a Onda 1 continua proposta pendente de aprovação no vault (ver [[01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]])
```

O hub e as 4 subpáginas preservaram seus IDs originais na reorganização (`notion-move-pages`, não recriação). A database também preservou ID, schema e a linha da SGV-12200 ao ser movida para dentro de Backlog. No corpo do hub, a referência à database foi trocada de embed estrutural (`<database>`, que ficou órfão quando ela mudou de pai) para `<mention-page>`, que sobrevive a reorganizações futuras de pai sem quebrar.

Observação técnica: a ferramenta de escrita do Notion (`insert_content`, usada para anexar conteúdo a uma página já existente) corrompeu quebras de linha/tabs em duas tentativas iniciais (Transcrição e Modelo-alvo); detectado por auditoria de conteúdo pós-escrita e corrigido reescrevendo essas páginas por completo (`replace_content`), que não apresentou o mesmo problema. Conteúdo final auditado e sem resíduos de corrupção nas 4 subpáginas.

## 3. Método e auditoria (resumo)

- **Transcrição:** produzida por leitura visual das 20 páginas do PDF (não por extração de texto, que fragmenta palavras por problema de ligadura tipográfica), com checagem secundária contra os 250 IDs numerados do TR — 250/250 confirmados, nenhum faltante ou extra, consistente com a revisão documental já registrada na SGV-12082. Nenhum trecho ficou ilegível. Auditoria independente (Codex) corrigiu a ordem de 1.27.10/1.27.11 (antes de 1.28, headings próprios) e a página de uma linha específica sob 1.27.6.1 (atribuída à p. 4) — ambos já corrigidos na versão atual.
- **Modelo-alvo e Matriz de fornecimento:** auditados linha a linha contra os artefatos de origem 04/05 da SGV-12082 — cobertura de entidades 100% (26 entidades/11 seções no Modelo-alvo; 36 linhas/5 fatias na Matriz), nenhuma adicionada ou removida; os 6 diagramas Mermaid do Modelo-alvo preservam a estrutura original (0 referências de nó ausentes); distinções Confirmado/Inferido/A confirmar preservadas onde a fonte já as fazia. Duas rodadas de correção de paginação (Servidor status funcional × online/offline; item 1.35.1) já aplicadas e revalidadas.
- **Citações ao TR:** 44 no Modelo-alvo + 45 na Matriz de fornecimento = **89 citações portáteis**, cada uma validada automaticamente contra a tabela de página/heading da transcrição — 0 erros na validação mais recente.
- **Metadados de processo:** confirmada a ausência de frontmatter, wikilinks, caminhos de vault, e menções a Rafael/Codex/aprovação/Roadmap/passo do Roadmap/commit nos três arquivos publicáveis.

## 4. Citações portáteis ao TR (Modelo-alvo e Matriz de fornecimento)

Toda referência a um item do TR, nos documentos canônicos "Modelo-alvo de atores, dados e estados" e "Matriz de fornecimento dos dados", segue o formato:

```
TR §ID — PDF p. N — transcrição §ID
```

- **`TR §ID`** — o identificador original do item/subitem, exatamente como consta no PDF.
- **`PDF p. N`** — a(s) página(s) do PDF original onde esse ID aparece (incluindo faixa, quando o item atravessa página, ex. `14–15`).
- **`transcrição §ID`** — o heading da transcrição integral sob o qual o item vive (um dos 45 headings de `01 - Termo de Referência...md`; subitens mais profundos apontam para o heading do item de primeiro nível que os contém).

Citações com mais de um ID listam todos os IDs e a faixa de páginas correspondente (ex.: `TR §1.28–1.29 — PDF p. 7–9 — transcrição §1.28/§1.29`).

**Nenhuma URL ou âncora de Notion foi inventada** — o formato é independente de plataforma, funciona como citação antes de a página existir e continua funcionando depois, ao lado do link real.
