---
tags:
  - qa
  - skill
---
# Skill: Refinamento (conduzir a mesa)

Dona do estágio de **refinamento**: pega material bruto (export do Notion, texto colado, análise de dev) e conduz a mesa de trabalho em `05 Refinar/` até virar um **card destilado** no padrão do vault. É o passo entre a limpeza do export e a escrita do card — e o ponto onde a especificação fica pronta pra validação e, depois, pra automação.

Consolida e aponta pra: [[../../QA Workspace/05 Refinar/README|05 Refinar/README]] (regras completas), [[../Contexto/FLUXOS#6. Refinar demanda já cadastrada|FLUXOS fluxo 6]] e o template [[../Templates/Refinamento.md|Refinamento.md]]. Não duplica essas regras — orquestra os passos e os handoffs.

## Contexto (pra qualquer IA/pessoa sem o setup na cabeça)

- **Mesa de refinamento:** `QA Workspace/05 Refinar/` — arquivos `<SGV> - <título>.md` envelopados no template `Refinamento.md`.
- **Destino do card:** `QA Workspace/02 Demandas/<ambiente>/`.
- **Arquivo é a fonte de verdade:** conversa não registrada na mesa não existe. Nada se atualiza sozinho — o Destilado anda quando se trabalha.

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Material que precisa virar card, mas falta informação | "refina a SGV-XXXX", "atualiza o destilado da SGV-XXXX" |
| Saída do [[SKILL_LIMPEZA_EXPORT]] modo A (ou do [[../Agentes/AGENTE_PROCESSAR_EXPORT|AGENTE_PROCESSAR_EXPORT]]) | material roteado pra `05 Refinar/` |

**Quando PULAR a mesa:** se o material já vem completo (descrição, passos, critérios, ambiente) → não refina; usa [[SKILL_LIMPEZA_EXPORT]] modo B pra criar card direto. A mesa é pra quando falta informação, não é checkpoint obrigatório.

## Passo a passo

1. **Envelopar in-place** o material no template `Refinamento.md` (sem criar arquivo paralelo): O problema → Análise → Pontos a definir → Destilado → Histórico. Só conteúdo, texto verbatim; metadado de card fica fora; **lacuna que importa pro QA vira item em "Pontos a definir"**, não lista passiva.
2. **Refinar** em quantas rodadas precisar (causa raiz, evidências, hipóteses descartadas, dúvidas pra dev/produto). Cada rodada rende `🔎 SGV-XXXX - Análise (<resultado curto>)` na daily. **Regra de ouro:** nada é inventado — cada informação é **extraída**, **inferida** (sempre listada explicitamente pra validação) ou **perguntada**. Na dúvida, pergunta.
3. **Fila viva (2 pendências):** material parado na mesa **sempre** tem um item `SGV-XXXX - Refinar (material em 05 Refinar/)` em A fazer hoje. Ao destilar o card, essa pendência fecha e nascem as próximas (validar em DEV / cadastrar no Notion) — a fila nunca fica sem o próximo passo do item.
4. **Gate de doc antes de destilar:** ao fechar resultado esperado + critérios, **cruzar contra a doc do módulo** ([[SKILL_VERIFICACAO_DOC]]) — gate obrigatório. Confirma o critério ou expõe divergência; se a doc não existe, abrir pendência de importar (fluxo 8).
5. **Destilar → card:** criar o card em `02 Demandas/<ambiente>/` a partir da seção Destilado ([[SKILL_BUGS]] pra bug; [[../Templates/Demanda.md|Demanda.md]] pra melhoria/funcionalidade) — só o problema, sem análise/suposição (no máximo uma linha em Observações apontando pra análise). Daily: `📝 SGV-XXXX - <Tipo> refinado(a)` (copy oficial) + **regra de links** (toda menção ao SGV vira wikilink pro card).
6. **CTs:** escrever os casos de teste ([[SKILL_CASOS_DE_TESTE]]) — **um CT por critério de aceite** (checklist de completude na própria skill).
7. **Fechar o ciclo:** análise/critérios levados pra task no Notion (`📤`) e a mesa **arquivada em** `04 Conhecimento/` (`status: refinado`, renomeada `<SGV> - Refinamento <título>.md`), com link cruzado card ↔ refinamento.

## Handoff (pra onde vai depois)

Card destilado + CTs → **validação** (fluxo 3b–3d, com o gate de doc) → aprovado → **automação** ([[../Contexto/FLUXOS#3h. Após aprovar: preparar automação|fluxo 3h]] → [[SKILL_INICIAR_AUTOMACAO]]).

## Resultado Esperado

Card limpo em `02 Demandas/`, com critérios cruzados contra a doc e CTs cobrindo cada critério, mesa arquivada em `04 Conhecimento/`, e a fila sempre com o próximo passo do item — pronto pra validar sem lacuna nem suposição não sinalizada.
