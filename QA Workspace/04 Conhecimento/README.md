---
tags:
  - qa
  - conhecimento
---
# 04 Conhecimento

Base de conhecimento sobre o Sogov — comportamentos do sistema, regras de negócio aprendidas nas validações, referências técnicas.

## Análises de refinamento (primeiro tipo estruturado)

Quando um refinamento do [[../05 Refinar/README|05 Refinar]] é concluído ([[../Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada (Notion → vault)|fluxo 6]]), o arquivo de mesa de trabalho ([[../Sistema/Templates/Refinamento.md|Refinamento.md]]) é **arquivado aqui** — com a análise completa (causa raiz, evidências, hipóteses descartadas, decisões dos pontos a definir) que **não entra no card**:

- Nome do arquivo: `<SGV> - Refinamento <título curto>.md` (mesmo título curto do card, prefixado por "Refinamento")
- `status: refinado` no frontmatter (era `em_refinamento` na fila)
- O card correspondente em `02 Demandas/` referencia este arquivo em **Observações** (wikilink), e este arquivo linka o card — rastro nos dois sentidos

A fonte de verdade externa da análise continua sendo a task no Notion (`📤`); a cópia daqui é o acervo local pesquisável — vale pra investigar bug parecido depois, sem depender de buscar no Notion.

## Outros tipos

Ainda sem estrutura definida: até ganharem template próprio, o auto-organizador não roteia nada mais pra cá ([[../Sistema/Skills/SKILL_INBOX|SKILL_INBOX]]); aprendizados pontuais ficam registrados na daily ou no card da demanda.
