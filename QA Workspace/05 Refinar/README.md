---
tags:
  - qa
  - refinar
---
# 05 Refinar

**Mesa de trabalho do refinamento** — exports `.md` do Notion, texto colado de outra ferramenta, qualquer material que precise virar card no padrão do vault ([[../Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada (Notion → vault)|fluxo 6]]). Não é só fila de passagem: é aqui que a análise acontece, em quantas rodadas precisar, **antes** do card existir — pro card nascer limpo, só com o problema.

## Como usar

1. **Jogar o arquivo aqui**, do jeito que veio — bagunçado mesmo, sem arrumar nada. Se souber o número, prefixar no nome (`<SGV> - <qualquer coisa>.md`); se não, tanto faz.
2. **Estruturar a mesa**: numa sessão com IA, o material bruto é envelopado no template [[../Sistema/Templates/Refinamento.md|Refinamento.md]] — o texto original fica intocado na seção "Material original", e o trabalho acontece nas seções Análise / Pontos a definir / Destilado.
3. **Refinar no próprio arquivo** (quantas rodadas precisar): causa raiz, evidências, hipóteses descartadas, dúvidas pra dev/produto. Cada rodada rende `🔎 SGV-XXXX - Análise (<resultado curto>)` na daily. O card ainda não existe nesse estágio.
4. **Regra de ouro do refinamento**: nada é inventado. Cada informação nasce **extraída** do material, **inferida** como comportamento mais lógico (sempre listada explicitamente pra validação) ou **perguntada** quando ambígua — na dúvida, pergunta, não assume.
5. **Destilar quando estiver no ponto**: o card nasce em `02 Demandas/<ambiente>/` a partir da seção **Destilado** — só o problema (Descrição objetiva, reprodução, resultado esperado, critérios, CTs), **sem análise nem suposição**; no card, no máximo uma linha em Observações referenciando a análise. `📝 SGV-XXXX - <Tipo> refinado(a)` na daily.
6. **Fechar o ciclo**: análise/critérios levados pra task no Notion (`📤`) e o arquivo de refinamento **arquivado em [[../04 Conhecimento/README|04 Conhecimento/]]** (`status: refinado`, renomeado `<SGV> - Refinamento <título curto>.md`) — acervo local da análise, com link cruzado entre card e refinamento.

Arquivo parado aqui é pendência: todo material nesta pasta deve ter um item correspondente em **A fazer hoje** da daily (`SGV-XXXX - Refinar (material em 05 Refinar/)`), pra fila não virar cemitério.
