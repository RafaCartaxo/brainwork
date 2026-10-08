---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de análise — SGV-12082

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Revisão da análise:** [[04 - Revisão da análise]]
> **Mapa geral:** [[../01 Modelo do preset/00 - Mapa geral]]
> **Matriz de atores e relações:** [[../01 Modelo do preset/01 - Matriz de atores e relações]]

> [!settings]- Controle do plano de análise
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Percorrer o TR completo (itens 1.1–1.43) e produzir, de forma rastreável, o modelo de atores/entidades/configurações/estados/relações/dependências do SOGOV — registrado nas notas temáticas de cada recorte (`01 Modelo do preset/Seções do TR/`, indexadas pela [[../01 Modelo do preset/01 - Matriz de atores e relações|matriz]]) e sintetizado no [[../01 Modelo do preset/00 - Mapa geral|mapa geral]].

---

## Riscos e escopo

- **Risco principal:** tratar inferência como fato, ou presumir blocos temáticos/atores antes de ler o TR.
- **Fora do escopo desta rodada:** casos de teste (CTs), sincronização com a Qase, automação e implementação de seed/preset.

---

## Estratégia de análise

1. Confirmar fonte e escopo — PDF do TR completo (itens 1.1–1.43) — e **confirmar a segmentação em recortes temáticos** (ver [[../01 Modelo do preset/01 - Matriz de atores e relações|índice de recortes na matriz]]) antes de começar a ler.
2. Ler e registrar cobertura por nota temática — cada recorte em `01 Modelo do preset/Seções do TR/` recebe sua própria leitura, com cobertura/classificação dos itens, elementos e relações identificados, dúvidas e fontes.
3. Consolidar atores/elementos/estados/relações **sem duplicação** — a matriz central só indexa os recortes (intervalo de itens/páginas, status, link); elementos e relações vivem exclusivamente na nota temática correspondente.
4. Sintetizar o mapa geral (Mermaid) a partir do que já estiver **confirmado** nas notas temáticas — nunca antecipar conteúdo que elas ainda não tenham.
5. Revisar cobertura (todo item do TR mapeado, não aplicável com justificativa, ou pendente) e consistência entre as notas temáticas e o mapa — só então fechar a análise e considerar entregáveis futuros.

### Critérios de classificação

- **Confirmado:** presente explicitamente no texto do TR. Fonte correlata (documento externo) pode ser registrada como contexto identificado, mas não transforma, por si só, algo em Confirmado.
- **Inferido:** interpretação provável a partir do TR, ainda pendente de validação.
- **A confirmar:** evidência ausente ou ambígua.
- **Não aplicável:** item do TR considerado — a análise continua passando por ele —, mas sem elemento relevante para este modelo; registrar a justificativa. Não significa excluído da leitura nem ignorado.
- **Ambiguidade:** registrada explicitamente como pendência de revisão, nunca resolvida por suposição.

---

## Itens de verificação

Um item por recorte temático — lista completa e os links das notas vivem no [[../01 Modelo do preset/01 - Matriz de atores e relações#Recortes temáticos do TR|índice de recortes da matriz]]; esta tabela não duplica essa lista.

| Item | Tipo | Fonte | Situação |
|---|---|---|---|
| Confirmar/ajustar a segmentação proposta (11 recortes) | Revisão de escopo | PDF do TR completo | ✅ Concluído — aprovado pelo Rafael (08/10/2026) |

---

## Entrada e saída

**Entrada:** PDF do TR completo (itens 1.1–1.43), em [[../Fontes/Requisitos Sogov.pdf|Fontes/Requisitos Sogov.pdf]]; segmentação em recortes temáticos (`01 Modelo do preset/Seções do TR/`).

**Saída:** notas temáticas com cobertura/elementos/relações/dúvidas/fontes por recorte; matriz como índice consolidado, sem duplicar o conteúdo; mapa geral (Mermaid) como síntese; registro de cobertura, lacunas e ambiguidades para revisão.
