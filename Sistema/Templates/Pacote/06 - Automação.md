---
demanda: "[[01 - Demanda]]"
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
repo: ""
framework: ""
status: planejado
pontos: ""
---

# Automação — <ID>

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Esta nota registra o **estado da cobertura automatizada** dos CTs de `03 - Casos de teste` — não duplica o cenário (fica em 03) nem o resultado da validação manual (fica em 04), só o que é específico de automação: infraestrutura, achados encontrados rodando, e pendências. O campo `Automação` de cada CT em `03` (manual/automatizado) é a fonte de verdade de *o que* está automatizado; aqui fica o *como* e o *estado atual*.

Processo completo (investigação técnica → codar → validar → triar achado real × bug × instabilidade → documentação viva → subir): [[../../Skills/SKILL_AUTOMACAO_TERMO_REFERENCIA|SKILL_AUTOMACAO_TERMO_REFERENCIA]]. Antes de qualquer commit/MR, aplicar o crivo de [[../../Skills/SKILL_REVISAO_CODIGO_AUTOMACAO|SKILL_REVISAO_CODIGO_AUTOMACAO]] (duplicação entre arquivos, reaproveitamento de dado de teste, comentários, impacto em código pré-existente).

---

## Configuração

- **Repo:** `<nome do repo>`
- **Branch/MR:** `<branch de trabalho>`
- **Framework:** `<cypress | playwright | outro>` — registrar aqui a ferramenta usada nesta rodada; o restante da nota não deve depender de sintaxe/nome de comando específico de uma ferramenta, pra sobreviver a uma troca de framework sem precisar reescrever tudo.
- **Ambiente de validação:** `<dev | hml | prod>`

---

## Cobertura por CT

| CT | Status | Observação |
|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | ⏳ | |

> Legenda: ✅ confirmado passando · ⚠️ achado real de produto (ver seção abaixo) · ❓ falha sem causa raiz identificada · ❌ sem código ainda · ⏳ planejado.

---

## Achados reais de produto

> Achado de produto encontrado *pela* automação não é bug do teste — não "consertar" a asserção pra fazer passar. Quando confirmado (não é instabilidade de ambiente nem suposição incorreta do teste), vira **Defeito** (não Bug solto): `pai: "<ID desta demanda>"`, pacote em `<pai>/Defeitos/` — mesma regra de [[../Bug/01 - Bug|01 - Bug]] (seção "Defeito, não Bug?").

- Nenhum achado registrado ainda.

---

## Pendências

- Nenhuma pendência registrada ainda.

---

## Checklist antes de subir

- [ ] Crivo de [[../../Skills/SKILL_REVISAO_CODIGO_AUTOMACAO|SKILL_REVISAO_CODIGO_AUTOMACAO]] aplicado (duplicação, reaproveitamento de dado, comentários, impacto em código pré-existente).
- [ ] Achados reais confirmados/triados — nenhum "conserto" de asserção sem essa triagem.
- [ ] CTs com achado em disputa ou sem causa raiz identificada ficam de fora do commit (ou entram com `.skip()`/equivalente + comentário linkando o achado).
- [ ] Cobertura por CT (tabela acima) refletida em `03 - Casos de teste` (campo `Automação` de cada CT).
- [ ] Status desta nota atualizado.
