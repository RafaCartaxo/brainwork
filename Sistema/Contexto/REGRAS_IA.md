---
tags:
  - qa
  - contexto
  - ia
---
# Regras para sessões de IA

Como uma sessão de IA deve operar **neste vault**. Cada regra nasceu de um erro real — o precedente está citado junto, porque regra sem história é parágrafo que ninguém lê.

Não substitui os docs de processo: [[PADROES_QA]] tem os padrões, [[FLUXOS]] a ordem de execução, [[../../QA Workspace/01 Daily/README|01 Daily/README]] o catálogo de copies. Isto aqui é sobre **conduta**.

> [!tip] Por que este arquivo existe
> Aprendizado que fica só na memória privada de uma sessão não impede a próxima de repetir o erro — e as sessões não compartilham memória entre si. Regra sobre o vault mora **no vault**.

## Data

Ver [[PADROES_QA#Regra de data]] — resolver `date +%F` do ambiente no momento de escrever, nunca reusar data da sessão.

**Precedente**: 2026-07-24, trabalho do dia 24 gravado no daily de 23 por data cacheada.

## Git e commits

> [!important] Commitar cada arquivo assim que ele fica pronto
> O vault tem **auto-commit + push a cada ~10 min** pelo Obsidian Git, com mensagem genérica `vault backup: <timestamp>` (ver [[Plugins Instalados#Versionamento (git + Obsidian Git)]]). Quem demora pra commitar perde a mensagem descritiva: o backup varre o trabalho em andamento e sobe com a mensagem dele.
>
> - Commit **por arquivo pronto**, não ao fim do lote — trabalho multi-arquivo estoura a janela de 10 min facilmente.
> - Fixar a identidade: `git -c user.name="Rafael Cartaxo" -c user.email="rafael.borges@sogo.com.br"`. O autor dos commits automáticos varia conforme o disparo.
> - **Nunca reescrever/amend commit já pushed** — nem pra "melhorar a mensagem".
> - Se `git status` está limpo mas a mudança está no disco, **o auto-backup já commitou**: conferir `git log -3 -- <arquivo>` antes de concluir que nada mudou.

**Precedente**: 2026-07-28, duas rodadas de trabalho (correção do script; e um lote de 4 docs de processo, ~15 min) foram engolidas pelo backup e ficaram sem mensagem descritiva.

## Fronteira com o script

O `qa-atualiza.py` e a camada de IA têm territórios definidos em [[../Agentes/AGENTE_FILA#Fronteira com o script]]. Resumo: **se dá pra decidir com uma conta ou um regex seguro, é do script; se precisa entender o que o item quer dizer, é do agente.**

> [!warning] Mexer no script é permitido — mover julgamento pra dentro dele não
> O erro do precedente não foi editar o `.py`. Foi transferir uma decisão que exige interpretação (agrupar item da fila por natureza) pra uma classificação por keyword, e ainda divergindo do vocabulário documentado.

**Precedente**: 2026-07-28 (manhã), uma sessão adicionou `reorganiza_afazer()` ao script; a fila passou a ser reescrita em todo 🔄, item caiu em grupo errado por keyword ("Reexportar a view do **Notion**" → 📤 Cadastro) e os grupos `🚨 Parado` e `✅ Concluídos hoje` desapareceram. Revertido no mesmo dia.

## Doc de processo: propor antes de aplicar

Mudança em [[../../QA Workspace/01 Daily/README|01 Daily/README]], [[FLUXOS]], [[PADROES_QA]], Skills, Agentes ou no `qa-atualiza.py` vai como **plano primeiro**, não como edição direta. São os arquivos que outras sessões vão obedecer.

**Precedentes**: 2026-07-17 (card da SGV-9610 criado seguindo "o espírito" do fluxo em vez da letra) e 2026-07-28 (script alterado sem proposta, revertido).

## Quando o doc e a prática divergem

A **prática das dailies ganha** — mas a reconciliação é explícita: corrigir o doc, avisar nas Anotações e registrar o motivo. Nunca escolher um dos dois em silêncio, nem "seguir o doc" sabendo que a prática é outra.

**Precedente**: 2026-07-28, o `AGENTE_FILA` documentava `📋 Planejamento` e `⚠️ Parado (6+ dias)` enquanto as dailies de 24 e 27/07 usavam `📋 Triagem` e `🚨 Parado (7+ dias)`; o doc ainda se contradizia (limiar 7d 🚨 vs grupo 6+ ⚠️). Uma sessão seguiu o doc à risca e produziu daily fora do padrão.

## Não presumir identidade nem ambiente

**SGV e ambiente decidem** nome do card, pasta de destino, subpasta da evidência e a copy da daily. Perguntar custa uma linha; presumir custa uma cascata de correções.

- Sem o número: **pedir o SGV** em vez de criar card sem prefixo (ver [[../Skills/SKILL_BUGS#Nome do arquivo do card]]).
- Sem o ambiente: **perguntar** — "testei e aprovei" não diz se foi DEV ou homologação, e isso muda o destino do card.

**Precedentes**: 2026-07-24, ambiente da SGV-5269 presumido como HML e o card nasceu com ressalva de suposição. 2026-07-28, card criado sem SGV (SGV-10404) exigiu renomear card, `task`, evidência, link `evidencia://`, copy da daily e 11 wikilinks.

## Sinal de parada

> [!important] Se a saída precisar dessas frases, pare e pergunte
> - *"primeiro card/caso do vault nessa situação"* → você está inaugurando formato inexistente
> - *"assumi X, corrija se precisar"* → você está transferindo pro Rafael a conferência de um chute
>
> Ambas são sinal de decisão que não é sua. Anotar a ressalva **não** substitui perguntar.

**Precedente**: 2026-07-28, a ressalva "primeiro card do vault nessa situação" foi escrita e o trabalho seguiu — o rename veio depois.

## Abrir o template, não só a skill

A **skill** dá a estrutura (quais seções); o **template** dá o formato do conteúdo. Ler só a skill leva a acertar as seções e errar o formato.

**Precedente**: 2026-07-28, "Passo a passo para reproduzir" escrito em lista numerada quando o padrão é BDD `Dado que / E / Quando / Então` — que estava visível tanto na [[../Skills/SKILL_BUGS|SKILL_BUGS]] quanto no [[../Templates/Bug Report|Bug Report]].

## Nunca falhar em silêncio

Situação que a automação não sabe tratar vira **aviso visível + item na fila**, nunca `continue` mudo nem "deu tudo certo". Vale pro script e pro registro na daily: melhor um aviso a mais que trabalho perdido sem ninguém notar.

**Precedentes** (todos no `qa-atualiza.py`): 2026-07-24, o `LEDGER` não reconhecia os emojis 🔎/📋 e ignorava linhas de Atividades caladamente. 2026-07-28, um guard comparava keywords de *pendência* contra copy de *Atividades* e desativou o ledger quase inteiro; e o `reconcilia_atividades` fazia `continue` sem aviso quando o card não existia, com o script imprimindo "nada a fazer — tudo em dia".

## Editar a daily por seção, nunca por `replace` global

A daily repete texto entre seções **por desenho**: a mesma frase aparece no **Status — reunião** (que é derivado), em **Atividades**, na fila e no log do `[!organizacao]`. Então `texto.replace("- ✅ SGV-1234 ...", ...)` casa na **primeira** ocorrência, que quase nunca é a que se quer — e o conteúdo cai na seção errada **sem erro nenhum**.

Antes de editar: localizar os limites da seção (`## X` até o próximo `## `, ou `### X` até o próximo `###`/`##`) e trabalhar **dentro deles**. Depois de editar: conferir que nenhum callout foi rompido — linha sem `>` dentro de um `[!abstract]`/`[!info]`/`[!note]`/`[!organizacao]` significa que o bloco quebrou ali.

O **Status — reunião** tem regra própria: é *derivado* do que está registrado embaixo e se **reescreve por inteiro** ([[../../QA Workspace/01 Daily/README#Status — reunião (primeira seção da daily)|01 Daily/README]]). Remendar linha a linha nele acumula duplicata; o certo é regenerar.

**Precedente**: 2026-07-30. Ao longo do dia eu editei a daily dezenas de vezes com âncora curta. O resultado: o callout do Status partido ao meio, três blocos de Atividades despejados dentro dele, uma atividade (SGV-5783) que **nunca chegou a ser registrada** — existia só no log do script — e duplicatas de 10437 e da suspeita descartada. Nada disso deu erro; só ficou ilegível, e foi o Rafael que viu. Diagnóstico e conserto na daily do dia.

## Anotações = canal IA → Rafael

Aviso, dúvida não bloqueante ou coisa pra ele validar depois vai em `## Anotações` da daily do dia: linha autocontida, com SGV/link quando houver, **sem** a marca ` → ` (essa é de quem processa). Recado em chat se perde quando a sessão fecha.

Pendência de verdade não é anotação — vai pra fila (**A fazer hoje**).

**Origem**: pedido do Rafael em 2026-07-17 (não é regra nascida de erro, como as outras acima) — ele já tem o hábito de processar as Anotações, e é onde o recado sobrevive ao fim da sessão.
