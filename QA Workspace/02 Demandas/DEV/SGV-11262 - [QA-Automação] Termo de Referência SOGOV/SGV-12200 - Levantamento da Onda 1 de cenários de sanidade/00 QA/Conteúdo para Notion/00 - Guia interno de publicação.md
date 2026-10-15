---
tags: [qa]
task: "SGV-12200"
pai: "SGV-11262"
tipo: "guia-publicacao"
status: pronto-para-publicacao
---
# Guia interno de publicação — Conteúdo pronto para o Notion

> [!info]- Navegação
> **README do card (SGV-12200):** [[../00 README|Abrir README do card]]
> **Proposta da Onda 1 (inalterada por este trabalho):** [[../01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]]
> **Transcrição publicável:** [[01 - Termo de Referência SOGOV (transcrição integral 1.1-1.43)|01 - Termo de Referência SOGOV (transcrição integral)]]
> **Modelo-alvo publicável:** [[02 - Modelo-alvo dos dados (Notion)|02 - Modelo-alvo dos dados (Notion)]]
> **Matriz de fornecimento publicável:** [[03 - Matriz de fornecimento dos dados (Notion)|03 - Matriz de fornecimento dos dados (Notion)]]
> **Fonte normativa (PDF canônico, permanece na SGV-12082, encerrada, não duplicado aqui):** [[../../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]
> **Artefatos de origem auditados (SGV-12082, encerrada, não editados):** [[../../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]] · [[../../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]]

> [!important] Conteúdo pronto para publicação — nada foi criado, publicado ou transferido no Notion ainda
> Este guia é **interno** (QA/vault) e documenta como os três arquivos ao lado foram produzidos, revisados e auditados, e como devem alimentar páginas no Notion. Ele próprio **não é publicável** — pode citar o vault, datas, decisões e metodologia à vontade. Quem é publicável são os três arquivos `01 - Termo de Referência SOGOV (transcrição integral 1.1-1.43).md`, `02 - Modelo-alvo dos dados (Notion).md` e `03 - Matriz de fornecimento dos dados (Notion).md` — nenhum deles contém o que está neste guia.
>
> **Única dependência externa restante:** Alice reservar/criar a página-pai no Notion. Depois disso, basta gerar os links reais e inseri-los onde hoje há citação portátil ao TR ou referência textual entre os três arquivos — o conteúdo em si já está pronto e não depende dessa criação para existir.

## 1. Mapa de conteúdo

| Camada | Papel | Onde vive | Observação |
|---|---|---|---|
| PDF original do TR | Fonte normativa única (canônica) | `SGV-12082/Fontes/Termo de Referência SOGOV.pdf` (SGV-12082, encerrada, não reaberta) | **Não duplicado neste pacote** — a transcrição aponta para ele, nunca o substitui. |
| Transcrição integral (`01 - Termo de Referência...md`) | Texto navegável, pronto para publicação | Esta pasta (`Conteúdo para Notion/`) | Estruturada por IDs originais 1.1–1.43 (mais 1.27.10/1.27.11 como headings próprios), com página do PDF indicada; sem frontmatter, sem metadados de processo. |
| Modelo-alvo (`02 - Modelo-alvo dos dados (Notion).md`) | Análise derivada — entidades, atributos, relações e status Confirmado/Inferido/A confirmar | Esta pasta (`Conteúdo para Notion/`) | Auditado contra o artefato de origem 04 da SGV-12082; toda referência ao TR usa citação portátil (§4). |
| Matriz de fornecimento (`03 - Matriz de fornecimento dos dados (Notion).md`) | Análise derivada — canal candidato de fornecimento por dado/estado | Esta pasta (`Conteúdo para Notion/`) | Auditada contra o artefato de origem 05 da SGV-12082; mesma convenção de citação do TR. |
| Recortes temáticos, mapa geral, matriz de atores (vault) | Leitura/análise interna de QA | `SGV-12082/01 Modelo do preset/` | Não publicados neste pacote; usados só como checagem secundária de cobertura — nunca substituto da fonte. |
| Artefatos de origem 04/05 (SGV-12082, encerrada) | Fonte de auditoria das cópias publicáveis | `SGV-12082/01 Modelo do preset/` | Não editados por este trabalho. |

## 2. Estrutura recomendada no Notion (ainda não criada)

1. **Página-pai do TR** (índice/entrada) — é só isso que falta Alice reservar/criar; o conteúdo abaixo não depende dessa criação para estar pronto.
2. **Transcrição integral**, a partir de `01 - Termo de Referência SOGOV (transcrição integral 1.1-1.43).md`, preservando os headings por ID.
3. **Modelo-alvo dos dados** (`02`), como subpágina ou seção ligada à página-pai.
4. **Matriz de fornecimento dos dados** (`03`), como subpágina irmã do Modelo-alvo.
5. **Pendência futura, fora deste pacote:** mapear recortes/mapa geral/matriz de atores do vault para âncoras da transcrição, se algum dia forem publicados também — não necessário para publicar os três arquivos deste pacote.
6. Links de Notion propriamente ditos (URLs de página/bloco) ficam em branco até a página-pai existir — nenhuma URL ou âncora de Notion foi inventada em nenhum dos três arquivos.

## 3. Método e auditoria (resumo)

- **Transcrição:** produzida por leitura visual das 20 páginas do PDF (não por extração de texto, que fragmenta palavras por problema de ligadura tipográfica), com checagem secundária contra os 250 IDs numerados do TR — 250/250 confirmados, nenhum faltante ou extra, consistente com a revisão documental já registrada na SGV-12082. Nenhum trecho ficou ilegível. Auditoria independente (Codex) corrigiu a ordem de 1.27.10/1.27.11 (antes de 1.28, headings próprios) e a página de uma linha específica sob 1.27.6.1 (atribuída à p. 4) — ambos já corrigidos na versão atual.
- **Modelo-alvo e Matriz de fornecimento:** auditados linha a linha contra os artefatos de origem 04/05 da SGV-12082 — cobertura de entidades 100% (26 entidades/11 seções no Modelo-alvo; 36 linhas/5 fatias na Matriz), nenhuma adicionada ou removida; os 6 diagramas Mermaid do Modelo-alvo preservam a estrutura original (0 referências de nó ausentes); distinções Confirmado/Inferido/A confirmar preservadas onde a fonte já as fazia. Duas rodadas de correção de paginação (Servidor status funcional × online/offline; item 1.35.1) já aplicadas e revalidadas.
- **Citações ao TR:** 44 no Modelo-alvo + 45 na Matriz de fornecimento = **89 citações portáteis**, cada uma validada automaticamente contra a tabela de página/heading da transcrição — 0 erros na validação mais recente.
- **Metadados de processo:** confirmada a ausência de frontmatter, wikilinks, caminhos de vault, e menções a Rafael/Codex/aprovação/Roadmap/passo do Roadmap/commit nos três arquivos publicáveis.

## 4. Citações portáteis ao TR (Modelo-alvo e Matriz de fornecimento)

Toda referência a um item do TR, em `02 - Modelo-alvo dos dados (Notion).md` e `03 - Matriz de fornecimento dos dados (Notion).md`, segue o formato:

```
TR §ID — PDF p. N — transcrição §ID
```

- **`TR §ID`** — o identificador original do item/subitem, exatamente como consta no PDF.
- **`PDF p. N`** — a(s) página(s) do PDF original onde esse ID aparece (incluindo faixa, quando o item atravessa página, ex. `14–15`).
- **`transcrição §ID`** — o heading da transcrição integral sob o qual o item vive (um dos 45 headings de `01 - Termo de Referência...md`; subitens mais profundos apontam para o heading do item de primeiro nível que os contém).

Citações com mais de um ID listam todos os IDs e a faixa de páginas correspondente (ex.: `TR §1.28–1.29 — PDF p. 7–9 — transcrição §1.28/§1.29`).

**Nenhuma URL ou âncora de Notion foi inventada** — o formato é independente de plataforma, funciona como citação antes de a página existir e continua funcionando depois, ao lado do link real.
