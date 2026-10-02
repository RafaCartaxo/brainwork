---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: ""
framework: ""
status: planejado
pontos: ""
---

# Automação — <ID>

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Plano de teste:** [[../00 QA/02 - Plano de teste]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Validação:** [[../00 QA/04 - Validação dev]]
> **Preparação Qase:** [[../00 QA/05 - Preparação Qase]]
> **Automação:** [[00 - Automação]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Esta nota é o **hub de configuração** da automação — infraestrutura, pendências cross-cutting, checklist antes de subir. **Não guarda placar por CT** (isso é [[02 - Validação automação|02 - Validação automação]], sempre atual) nem narrativa de achado/correção (isso é [[03 - Handoff de execução|03 - Handoff de execução]], histórico). Guardar os dois aqui de novo é como esta pasta ficou confusa da primeira vez — não repetir.

Processo completo (investigação técnica → codar → validar → triar achado real × bug × instabilidade → documentação viva → subir): [[../../../Skills/SKILL_AUTOMACAO_TERMO_REFERENCIA|SKILL_AUTOMACAO_TERMO_REFERENCIA]]. Antes de qualquer commit/MR, aplicar o crivo de [[../../../Skills/SKILL_REVISAO_CODIGO_AUTOMACAO|SKILL_REVISAO_CODIGO_AUTOMACAO]] (duplicação entre arquivos, reaproveitamento de dado de teste, comentários, impacto em código pré-existente).

> [!info]- Documentos desta pasta
> Esta nota (`00`) e [[02 - Validação automação|02 - Validação automação]] são as únicas obrigatórias sempre que `Automação/` existir — uma configura, a outra registra o placar atual por CT. Quando a automação for grande o bastante pra precisar de plano de arquitetura, log de execução entre rodadas ou revisão cenário a cenário em separado, crie:
> - [[01 - Plano de automação|01 - Plano de automação]] — arquitetura, convenções, faseamento.
> - [[03 - Handoff de execução|03 - Handoff de execução]] — estado/orquestração pra outra sessão continuar, log cronológico por rodada.
> - [[04 - Documentação de entrega|04 - Documentação de entrega]] — revisão cenário a cenário do que cada CT de código faz, pra revisão humana.

---

## Configuração

- **Repo:** `<nome do repo>`
- **Branch/MR:** `<branch de trabalho>`
- **Framework:** `<cypress | playwright | outro>` — registrar aqui a ferramenta usada nesta rodada; o restante da nota não deve depender de sintaxe/nome de comando específico de uma ferramenta, pra sobreviver a uma troca de framework sem precisar reescrever tudo.
- **Ambiente de validação:** `<dev | hml | prod>`

---

## Status

Placar completo, por CT: [[02 - Validação automação|02 - Validação automação]].

---

## Pendências

> Só pendências **cross-cutting** (afetam mais de um CT ou a automação como um todo) — pendência de um CT específico fica na Observação da tabela de [[02 - Validação automação|02 - Validação automação]], com link pro detalhe no Handoff.

- Nenhuma pendência registrada ainda.

---

## Checklist antes de subir

- [ ] Crivo de [[../../../Skills/SKILL_REVISAO_CODIGO_AUTOMACAO|SKILL_REVISAO_CODIGO_AUTOMACAO]] aplicado (duplicação, reaproveitamento de dado, comentários, impacto em código pré-existente).
- [ ] Achados reais confirmados/triados — nenhum "conserto" de asserção sem essa triagem.
- [ ] CTs com achado em disputa ou sem causa raiz identificada ficam de fora do commit (ou entram com `.skip()`/equivalente + comentário linkando o achado).
- [ ] [[02 - Validação automação|02 - Validação automação]] refletida em `../00 QA/03 - Casos de teste` (campo `Automação` de cada CT).
- [ ] Status desta nota atualizado.
