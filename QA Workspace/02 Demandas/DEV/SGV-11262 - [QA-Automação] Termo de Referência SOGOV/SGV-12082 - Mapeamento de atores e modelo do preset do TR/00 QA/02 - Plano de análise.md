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

Percorrer o TR completo (itens 1.1–1.43) e produzir, de forma rastreável, o modelo de atores/entidades/configurações/estados/relações/dependências do SOGOV — registrado na [[../01 Modelo do preset/01 - Matriz de atores e relações|matriz]] e sintetizado no [[../01 Modelo do preset/00 - Mapa geral|mapa geral]].

---

## Riscos e escopo

- **Risco principal:** tratar inferência como fato, ou presumir blocos temáticos/atores antes de ler o TR.
- **Fora do escopo desta rodada:** casos de teste (CTs), sincronização com a Qase, automação e implementação de seed/preset.

---

## Estratégia de análise

1. Confirmar fonte e escopo — PDF do TR completo (itens 1.1–1.43).
2. Percorrer o TR progressivamente, por blocos temáticos definidos durante a própria leitura (não antecipados aqui).
3. Lançar cada elemento e relação identificado na matriz, com a referência do item do TR e o estado de conhecimento.
4. Sintetizar o mapa geral (Mermaid) a partir do que já estiver registrado na matriz — nunca o contrário.
5. Revisar cobertura (todo item do TR mapeado, não aplicável com justificativa, ou pendente) e consistência entre matriz e mapa.

### Critérios de classificação

- **Confirmado:** presente explicitamente no texto do TR. Fonte correlata (documento externo) pode ser registrada como contexto identificado, mas não transforma, por si só, algo em Confirmado.
- **Inferido:** interpretação provável a partir do TR, ainda pendente de validação.
- **A confirmar:** evidência ausente ou ambígua.
- **Não aplicável:** item do TR considerado — a análise continua passando por ele —, mas sem elemento relevante para este modelo; registrar a justificativa. Não significa excluído da leitura nem ignorado.
- **Ambiguidade:** registrada explicitamente como pendência de revisão, nunca resolvida por suposição.

---

## Itens de verificação

| Item | Tipo | Fonte | Situação |
|---|---|---|---|
| <placeholder — bloco temático a definir durante a leitura> | Mapeamento documental | PDF do TR completo | A confirmar |

> Replique a linha para cada bloco temático conforme for definido durante a leitura do TR. Não antecipar nomes/quantidade de blocos nesta etapa.

---

## Entrada e saída

**Entrada:** PDF do TR completo (itens 1.1–1.43), em [[../Fontes/Requisitos Sogov.pdf|Fontes/Requisitos Sogov.pdf]].

**Saída:** matriz de atores e relações com rastreabilidade ao TR; mapa geral (Mermaid) como síntese; registro de cobertura, lacunas e ambiguidades para revisão.
