---
tags: [qa]
task: "SGV-12200"
pai: "SGV-11262"
tipo: "staging-notion"
status: rascunho
---
# README de staging — Preparação de conteúdo para o Notion

> [!info]- Navegação
> **README do card (SGV-12200):** [[../00 README|Abrir README do card]]
> **Proposta da Onda 1 (inalterada por este trabalho):** [[../01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]]
> **Transcrição publicável:** [[01 - Termo de Referência SOGOV (transcrição integral 1.1-1.43)|01 - Termo de Referência SOGOV (transcrição integral)]]
> **Modelo-alvo publicável:** [[02 - Modelo-alvo dos dados (Notion)|02 - Modelo-alvo dos dados (Notion)]]
> **Matriz de fornecimento publicável:** [[03 - Matriz de fornecimento dos dados (Notion)|03 - Matriz de fornecimento dos dados (Notion)]]
> **Fonte normativa (PDF original, SGV-12082, encerrada):** [[../../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]
> **Artefatos de origem auditados (SGV-12082, encerrada, não editados):** [[../../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]] · [[../../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]]

> [!important] Rascunho de preparação — nada foi criado, publicado ou transferido no Notion
> Este README é **interno** (QA/vault) e documenta como os três arquivos ao lado foram produzidos e como devem, no futuro, alimentar páginas no Notion. Ele próprio **não é publicável** — pode citar o vault, datas, decisões e metodologia à vontade. Quem é publicável são os três arquivos `01 - Termo de Referência SOGOV (transcrição integral 1.1-1.43).md`, `02 - Modelo-alvo dos dados (Notion).md` e `03 - Matriz de fornecimento dos dados (Notion).md` — nenhum deles contém o que está neste README.

## 1. Mapa de importação

| Camada | Papel | Onde vive hoje | Observação |
|---|---|---|---|
| PDF original do TR | Fonte normativa única | `SGV-12082/Fontes/Termo de Referência SOGOV.pdf` (SGV-12082, encerrada, não reaberta) | Nunca é substituído pela transcrição — a transcrição aponta para ele, não o contrário. |
| Transcrição integral (`01 - Termo de Referência...md`) | Texto navegável, publicável no Notion | Esta pasta (`Notion staging/`) | Estruturada por IDs originais 1.1–1.43 (mais 1.27.10/1.27.11), com página do PDF indicada; sem frontmatter, sem metadados de processo. |
| Modelo-alvo publicável (`02 - Modelo-alvo dos dados (Notion).md`) | Análise derivada — entidades, atributos, relações e status Confirmado/Inferido/A confirmar | Esta pasta (`Notion staging/`) | Auditado contra o artefato de origem 04 da SGV-12082 (ver §6/§7); toda referência ao TR usa citação portátil (§6). |
| Matriz de fornecimento publicável (`03 - Matriz de fornecimento dos dados (Notion).md`) | Análise derivada — canal candidato de fornecimento por dado/estado | Esta pasta (`Notion staging/`) | Auditada contra o artefato de origem 05 da SGV-12082 (ver §6/§7); mesma convenção de citação do TR. |
| Recortes temáticos (`Seções do TR/`, 11 notas) | Leitura/análise interna de QA | `SGV-12082/01 Modelo do preset/Seções do TR/` | Usados só como checagem secundária de cobertura — nunca como substituto da fonte nem replicados neste pacote. |
| Mapa geral / Matriz de atores | Síntese visual interna de QA | `SGV-12082/01 Modelo do preset/` | Não fazem parte deste pacote de preparação — ficam só no vault. |
| Artefatos de origem 04/05 (SGV-12082, encerrada) | Fonte de auditoria das cópias publicáveis | `SGV-12082/01 Modelo do preset/` | Não editados por este trabalho — ver §7 para o diff de fidelidade. |

## 2. Estrutura recomendada no Notion (ainda não criada)

1. **Página-pai do TR** (índice/entrada) — é só isso que falta Alice reservar; a preparação de conteúdo abaixo não depende da criação da página para continuar.
2. **Transcrição integral**, importada a partir de `01 - Termo de Referência SOGOV (transcrição integral 1.1-1.43).md`, preservando os headings por ID (1.1 a 1.43, mais 1.27.10 e 1.27.11 — ver §4 do histórico de auditoria abaixo).
3. **Modelo-alvo dos dados** (`02 - Modelo-alvo dos dados (Notion).md`), como subpágina ou seção ligada à página-pai — análise funcional derivada, com citação portátil para cada item do TR que usa.
4. **Matriz de fornecimento dos dados** (`03 - Matriz de fornecimento dos dados (Notion).md`), como subpágina irmã do Modelo-alvo.
5. **Pendência futura:** para cada recorte temático, mapa geral e matriz de atores do vault (não publicados neste pacote), mapear qual(is) item(ns)/âncora(s) da transcrição ele referencia, e registrar esse vínculo como link direto no Notion. Essa tabela de vínculos **não foi preenchida nesta rodada**.
6. Links de Notion propriamente ditos (URLs de página/bloco) ficam em branco até a página-pai existir — não há nada para preencher ainda; nenhuma URL ou âncora de Notion foi inventada em nenhum dos três arquivos publicáveis.

## 3. Método de transcrição e revisão visual

- **Base estrutural:** extração `pdftotext -layout` do PDF, usada só para esqueleto de ordem/numeração (242–250 IDs) — nunca como texto final, pois fragmenta palavras por problema de ligadura tipográfica ("ti"/"fi" cortados do meio das palavras, ex.: "cer_cado" em vez de "certificado").
- **Transcrição real:** cada uma das 20 páginas do PDF foi lida visualmente (renderização de página, não extração de texto) e transcrita a partir do que foi lido na renderização.
- **Checagem secundária:** a lista de 250 IDs numerados extraída da extração bruta foi usada como checklist de cobertura, cruzada contra a transcrição final — 250/250 IDs confirmados presentes, nenhum faltante, nenhum extra. Esse mesmo total (250 referências numeradas) já havia sido obtido independentemente pela revisão documental da SGV-12082 ([[../../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/04 - Revisão da análise|04 - Revisão da análise]]), o que serve de confirmação cruzada adicional.
- **Nenhum trecho ficou ilegível** nas 20 páginas — não houve necessidade de marcar nenhuma passagem para conferência pendente.

## 4. Ordem e páginas — achados da auditoria do Codex (corrigidos)

- **Sequência 1.27.9 → 1.27.10 → 1.27.11 → 1.28:** a transcrição inicialmente havia colocado 1.28 antes de 1.27.10/1.27.11, com uma nota editorial explicando a inversão. O Codex confirmou visualmente (páginas 6–7) que a ordem literal do PDF é 1.27.9 → 1.27.10 → 1.27.11 → 1.28, e a transcrição foi corrigida: 1.27.10 e 1.27.11 agora são headings estáveis próprios (como os demais itens numerados), na posição correta, sem nenhuma nota editorial no texto publicável.
- **Linha "i. visualizar todo o organograma do órgão;" sob 1.27.6.1:** a transcrição inicial tratava essa linha como uma duplicata de renderização entre as páginas 3 e 4, e a "resolvia" mantendo-a uma única vez por comparação com o padrão de itens idênticos em 1.27.5.1/1.27.7.1. O Codex renderizou as páginas 3–4 e confirmou visualmente que a linha aparece **uma única vez no PDF**, no topo da página 4, imediatamente após o corte de página no fim da página 3 (onde fica só o cabeçalho "1.27.6.1.No organograma:"). A transcrição foi corrigida para refletir isso: a linha é atribuída à página 4, sem qualquer alegação de duplicidade ou de normalização por comparação com outros itens.

## 5. Pendências

- Conversa com Alice (reserva de página no Notion): continua **não realizada** — pendência operacional da SGV-12200, inalterada por este trabalho. Alice só precisa **criar/reservar a página-pai**; isso não bloqueia a preparação de conteúdo, que já está pronta nos três arquivos publicáveis desta pasta.
- Criação/publicação de qualquer página ou bloco no Notion: **não feita** — sem conector de escrita disponível nesta sessão, e dependente de decisão humana.
- Mapeamento item a item de cada recorte/mapa geral/matriz de atores do vault para uma âncora da transcrição (§2, item 5): **não feito nesta rodada** — fica como próximo passo, antes ou durante a criação real da página. Isso é diferente do Modelo-alvo/Matriz de fornecimento, que **já citam** cada item do TR que usam (§6).
- Granularidade de heading da transcrição: heading próprio para os 43 itens de primeiro nível (1.1–1.43) e, por exigência de ordem literal do PDF, também para 1.27.10 e 1.27.11. Subitens mais profundos (ex.: 1.29.10.4, 1.40.2.1) preservam sua numeração completa no texto, mas não têm heading Markdown individual — a citação portátil (§6) sempre aponta para o heading do item de primeiro nível que contém o subitem citado.

## 6. Citações portáteis ao TR (Modelo-alvo e Matriz de fornecimento)

Toda referência a um item do TR, nos dois documentos publicáveis `02 - Modelo-alvo dos dados (Notion).md` e `03 - Matriz de fornecimento dos dados (Notion).md`, segue o formato:

```
TR §ID — PDF p. N — transcrição §ID
```

- **`TR §ID`** — o identificador original do item ou subitem (ex.: `1.29.10.4`), preservado exatamente como consta no PDF.
- **`PDF p. N`** — a página do PDF original onde esse ID aparece (confirmada pela revisão visual página a página da transcrição).
- **`transcrição §ID`** — o heading da transcrição integral sob o qual esse item/subitem vive (sempre um dos 45 headings do arquivo `01 - Termo de Referência...md`; subitens mais profundos apontam para o heading do item de primeiro nível que os contém).

Quando uma linha cita mais de um ID (ex.: uma entidade cujo requisito atravessa `1.28` e `1.29`), a citação lista os dois IDs e a faixa de páginas correspondente (ex.: `TR §1.28–1.29 — PDF p. 7–9 — transcrição §1.28/§1.29`).

**Nenhuma URL ou âncora de Notion foi inventada** — o formato é deliberadamente independente de plataforma, para funcionar como citação mesmo antes de a página existir, e continuar funcionando depois, como texto ao lado do link real.

## 7. Auditoria de fidelidade (Modelo-alvo e Matriz de fornecimento)

- **Cobertura de entidades:** contagem de linhas por seção comparada entre os artefatos de origem (04/05 da SGV-12082) e as cópias publicáveis — **100% de correspondência** (26 entidades em 11 seções do Modelo-alvo; 36 linhas em 5 fatias da Matriz de fornecimento), nenhuma adicionada, nenhuma removida.
- **Diagramas Mermaid:** os 6 diagramas do Modelo-alvo foram copiados sem alteração de estrutura (nós/arestas); validação estrutural automática confirma 0 referências de nó ausentes nos 6 blocos.
- **Citações ao TR:** 42 citações portáteis no Modelo-alvo e 45 na Matriz de fornecimento, cada uma validada automaticamente contra a tabela de página/heading gerada a partir da transcrição — **0 erros** (nenhum ID citado fora do intervalo de página ou heading esperado).
- **Metadados de processo:** confirmada a ausência de frontmatter, wikilinks, caminhos de vault, menções a Rafael/Codex/aprovação/Roadmap/passo do Roadmap/commit nos dois arquivos publicáveis.
- **Distinções Confirmado/Inferido/A confirmar:** preservadas em todas as linhas onde a fonte original já fazia essa distinção (bloqueios, lacunas de nomenclatura, vínculos não confirmados, inferências da automação).
