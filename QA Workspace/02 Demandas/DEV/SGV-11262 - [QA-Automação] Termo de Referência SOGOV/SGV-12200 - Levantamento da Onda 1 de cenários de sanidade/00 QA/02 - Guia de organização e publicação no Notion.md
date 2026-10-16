---
tags: [qa]
task: "SGV-12200"
pai: "SGV-11262"
tipo: "guia-publicacao"
status: pronto-para-publicacao
---
# Guia de organização e publicação no Notion

> [!info]- Navegação
> **README do card (SGV-12200):** [[00 README|Abrir README do card]]
> **Proposta da Onda 1 (inalterada por este trabalho):** [[01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]]
> **Índice da sanidade automatizada do TR (ponto de entrada dos documentos canônicos):** [[../../Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/00 - Índice da sanidade automatizada do TR|00 - Índice]]
> **Transcrição canônica:** [[../../Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/01 - Termo de Referência SOGOV - Transcrição integral|01 - Termo de Referência SOGOV - Transcrição integral]]
> **Modelo-alvo canônico:** [[../../Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/02 - Modelo-alvo de atores, dados e estados|02 - Modelo-alvo de atores, dados e estados]]
> **Matriz de fornecimento canônica:** [[../../Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/03 - Matriz de fornecimento dos dados|03 - Matriz de fornecimento dos dados]]
> **Fonte normativa (PDF canônico, permanece na SGV-12082, encerrada, não duplicado):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]
> **Artefatos de origem auditados (SGV-12082, encerrada, não editados):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]] · [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]]

> [!important] Publicado no Notion em 15/10/2026
> Este guia é **interno** (QA/vault) e documenta como os três documentos canônicos (agora em `Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/`) foram produzidos, revisados, auditados e publicados no hub do Notion. Ele próprio **não é publicável** — pode citar o vault, datas, decisões e metodologia à vontade. Os três documentos canônicos (transcrição, modelo-alvo e matriz de fornecimento) é que são publicáveis — nenhum deles contém o que está neste guia.
>
> **Estado atual:** o hub já está organizado — ver §2 para a estrutura final e §3 para o método/auditoria de publicação.

## 1. Mapa de conteúdo

| Camada | Papel | Onde vive | Observação |
|---|---|---|---|
| PDF original do TR | Fonte normativa única (canônica) | `SGV-12082/Fontes/Termo de Referência SOGOV.pdf` (SGV-12082, encerrada, não reaberta) | **Não duplicado** — a transcrição aponta para ele, nunca o substitui. |
| Transcrição integral canônica | Texto navegável, pronto para publicação | `Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/01 - ...md` | Estruturada por IDs originais 1.1–1.43 (mais 1.27.10/1.27.11 como headings próprios), com página do PDF indicada; sem frontmatter, sem metadados de processo. |
| Modelo-alvo canônico | Análise derivada — entidades, atributos, relações e status Confirmado/Inferido/A confirmar | `Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/02 - ...md` | Auditado contra o artefato de origem 04 da SGV-12082; toda referência ao TR usa citação portátil (§4). |
| Matriz de fornecimento canônica | Análise derivada — canal candidato de fornecimento por dado/estado | `Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/03 - ...md` | Auditada contra o artefato de origem 05 da SGV-12082; mesma convenção de citação do TR. |
| Recortes temáticos, mapa geral, matriz de atores (vault) | Leitura/análise interna de QA | `SGV-12082/01 Modelo do preset/` | Não publicados; usados só como checagem secundária de cobertura — nunca substituto da fonte. |
| Artefatos de origem 04/05 (SGV-12082, encerrada) | Fonte de auditoria dos documentos canônicos | `SGV-12082/01 Modelo do preset/` | Não editados por este trabalho. |

Esta mudança de local (de `SGV-12200/00 QA/Conteúdo para Notion/` para `Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/`) reflete que a referência permanente do TR não é específica da Onda 1 — ela serve a qualquer onda futura de cenários. Ver [[../../Conhecimento/Sanidade automatizada do SOGOV - Termo de Referência/00 - Índice da sanidade automatizada do TR|00 - Índice]] para a cadeia completa TR → Modelo-alvo → Matriz → ondas de cenários.

## 2. Estrutura no Notion (publicada em 15/10/2026)

O hub (criado por Rafael, título já correto: "Sanidade automatizada do SOGOV - Termo de Referência") foi organizado assim:

1. **Página-pai/hub** — [link](https://app.notion.com/p/3fa72f8c899080a1a1d6f421cc6d4426) — intro curta + cadeia TR→Modelo-alvo→Matriz→ondas + lista dos 4 itens abaixo.
2. **Subpágina — Termo de Referência SOGOV — Transcrição integral** — conteúdo integral da transcrição canônica, 45 headings (1.1–1.43, com 1.27.10/1.27.11 próprios), preservado.
3. **Subpágina — Modelo-alvo de atores, dados e estados** — conteúdo integral do documento canônico 02: 10 tabelas, 6 diagramas Mermaid, seções 1–11.
4. **Subpágina — Matriz de fornecimento dos dados** — conteúdo integral do documento canônico 03: 5 tabelas (fatias C1–C2 a C6), seções 1–7.
5. **Subpágina — Cenários de sanidade** — placeholder: nenhum cenário publicado; a Onda 1 continua proposta pendente de aprovação no vault (ver [[01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]]).
6. **Database "Demandas relacionadas"** (Título/ID/Papel/Estado/URL da task) — uma linha para a SGV-12200, URL da task em branco (nenhuma task Notion dedicada foi localizada; não inventada).

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
