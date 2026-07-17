---
tags:
  - qa
  - refinar
---
# 05 Refinar

**Mesa de trabalho do refinamento** — exports `.md` do Notion, texto colado de outra ferramenta, qualquer material que precise virar card no padrão do vault ([[../Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada (Notion → vault)|fluxo 6]]). Não é só fila de passagem: é aqui que a análise acontece, em quantas rodadas precisar, **antes** do card existir — pro card nascer limpo, só com o problema.

## Como usar

1. **Jogar o arquivo aqui**, do jeito que veio — export cru do Notion, com lixo de site e tudo, sem arrumar nada. Sempre com o número no nome (`<SGV> - <qualquer coisa>.md` ou só `<SGV>.md`).
2. **Estruturar a mesa**: numa sessão com IA, **o próprio arquivo exportado é envelopado in-place** no template [[../Sistema/Templates/Refinamento.md|Refinamento.md]] — sem criar arquivo paralelo, tudo numa visualização só: **O problema** (conteúdo da task em parágrafos com lead-in em negrito: Descrição com autoria, Saída esperada, Saída atual, Entrega do dev com link do MR) → Análise → Pontos a definir → Destilado → Histórico. Regra do envelope: **só conteúdo, texto preservado verbatim** — metadado de card fica de fora (sprint, revisores, datas, progresso, lista de campos vazios; quem precisar abre a task no Notion), artefato de export se remove, e **lacuna que importa pro QA vira item em Pontos a definir** (ex.: task sem passo a passo/evidência), não lista passiva. Nada se infere.
3. **Refinar no próprio arquivo** (quantas rodadas precisar): causa raiz, evidências, hipóteses descartadas, dúvidas pra dev/produto. Cada rodada rende `🔎 SGV-XXXX - Análise (<resultado curto>)` na daily. O card ainda não existe nesse estágio.
   **Como a mesa evolui — nada muda sozinho**: o Destilado não se atualiza automaticamente; ele anda quando se trabalha, por dois caminhos equivalentes: **(a)** Rafael preenche Análise/Pontos a definir direto no Obsidian e pede numa sessão ("atualiza o destilado da SGV-XXXX") — a IA escreve o Destilado a partir do que está na mesa; **(b)** o trabalho acontece no chat e a IA escreve na mesa (Análise + Destilado juntos, rodada a rodada). Nos dois casos **o arquivo é a fonte de verdade** — conversa não registrada na mesa não existe.
4. **Regra de ouro do refinamento**: nada é inventado. Cada informação nasce **extraída** do material, **inferida** como comportamento mais lógico (sempre listada explicitamente pra validação) ou **perguntada** quando ambígua — na dúvida, pergunta, não assume.
5. **Destilar quando estiver no ponto**: o card nasce em `02 Demandas/<ambiente>/` a partir da seção **Destilado** — só o problema (Descrição objetiva, reprodução, resultado esperado, critérios, CTs), **sem análise nem suposição**; no card, no máximo uma linha em Observações referenciando a análise. Na daily: `📝 SGV-XXXX - <Tipo> refinado(a) (critérios de aceite prontos)` — **copy oficial do catálogo** ([[../01 Daily/README|01 Daily/README]]) — e, com o card criado, **aplicar a regra de links**: toda menção ao SGV na daily (Atividades, fila, anotações) vira wikilink pro card.
6. **Fechar o ciclo**: análise/critérios levados pra task no Notion (`📤`) e o arquivo de refinamento **arquivado em [[../04 Conhecimento/README|04 Conhecimento/]]** (`status: refinado`, renomeado `<SGV> - Refinamento <título curto>.md`) — acervo local da análise, com link cruzado entre card e refinamento.

Arquivo parado aqui é pendência: todo material nesta pasta deve ter um item correspondente em **A fazer hoje** da daily (`SGV-XXXX - Refinar (material em 05 Refinar/)`), pra fila não virar cemitério.
