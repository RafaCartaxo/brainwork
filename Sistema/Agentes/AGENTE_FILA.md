---
tags:
  - qa
  - agente
---
# Agente: Organizador da Fila

Reorganiza a seção "A fazer hoje" da daily: agrupa por natureza, sinaliza idade e bloqueios, remove ruído.

## Por que existe

A lista "A fazer hoje" acumula itens sem distinção de natureza, urgência ou idade. Com 10-14 itens num dia típico, é impossível bater o olho e saber o que precisa de ação imediata. Este agente organiza a fila pra virar leitura instantânea.

## Gatilhos

| Gatilho | Executor | O que acontece |
|---|---|---|
| **🔄 Atualizar** (Dashboard) | Script (`qa-atualiza.py`) | **Prepara, não agrupa**: calcula idade (`🕐`/`⚠️`/`🚨`), recolhe os `[x]` em ✅ Concluídos hoje e mantém a fila viva. Os grupos por natureza **não são tocados** — o docstring de `coleta_concluidos()` diz isso explicitamente |
| **Sessão de IA** | Este agente | O agrupamento por natureza nos 7 grupos. **Só acontece aqui** — "organiza a fila", "processa o dia" ou qualquer pedido de organização da daily |
> [!warning] O botão 🔄 **não** dispara este agente — e confundir isso já custou caro
> O 🔄 executa `.obsidian/scripts/qa-atualiza.py`, que é **Python**: ele não invoca agente de IA. Só prepara a parte mecânica.
>
> Até 30/07 esta tabela listava o botão como gatilho do agente. Uma sessão de IA leu isso, entendeu que apertar o botão fazia o trabalho todo — e em 28/07 outra sessão foi além: **moveu o agrupamento pra dentro do script** (`reorganiza_afazer`) pra fazer a promessa virar verdade. A fila quebrou. **A doc não descreveu o bug; ela o causou.**
>
> Por isso a tabela agora tem coluna **Executor**: gatilho sem executor é promessa.


## O que faz

### 1. Agrupa por natureza

> [!important] Os grupos são definidos no `01 Daily/README`, não aqui
> A tabela oficial dos 7 grupos vive em [[../../QA Workspace/01 Daily/README#Grupos da fila ("A fazer hoje")|01 Daily/README → Grupos da fila]], junto do catálogo de copies. Este agente **executa** o agrupamento; ele não é a fonte da verdade do vocabulário.
> Motivo: até 28/07 os grupos existiam só aqui, a prática das dailies usava outros nomes (`📋 Triagem` vs `📋 Planejamento`, `🚨 Parado (7+)` vs `⚠️ Parado (6+)`) e nada cruzava os dois — uma sessão de IA seguiu este doc à risca e produziu uma fila fora do padrão. Ao mexer em grupo, mexer **no README**.

Resumo operacional (detalhe e casos de borda no README): 🎯 Validação · 🔎 Refinamento · 📤 Cadastro · 👁️ Acompanhamento · 📋 Triagem · 🚨 Parado (7+ dias) · ✅ Concluídos hoje.

Classificar pelo **verbo da ação** — o texto antes do primeiro `(`, `—` ou `;` — nunca pela linha toda. E `🚨`/`✅` valem por **estado** (idade / `[x]`), ganhando do verbo.

### 2. Sinaliza idade

> [!important] Isto é do script, não do agente (desde 28/07)
> O incremento de idade e os limiares abaixo são executados por `envelhece_fila()` no `.obsidian/scripts/qa-atualiza.py`, no momento do carry-over. **O agente não recalcula idade** — só lê o que já está marcado. Ver "Fronteira com o script" no fim deste documento.

| Dias arrastado | Marca |
|---|---|
| 1-2 dias | (sem marca — normal) |
| 3-4 dias | `🕐 Nd` |
| 5-6 dias | `🕐 Nd ⚠️` |
| 7+ dias | `🕐 Nd 🚨` + alerta no Auto-organização |

A idade é calculada a partir da primeira aparição do item em qualquer daily (não da daily de hoje). O incremento usa o **intervalo real entre as duas dailies**, não +1 fixo: sexta → segunda vale +3 dias (precedente de 27/07).

### 3. Sinaliza bloqueio

Se o texto do item indica bloqueio, adiciona o motivo:

| Padrão | Marca |
|---|---|
| "aguardando dev", "MR em revisão", "quando o dev entregar" | `⏳ aguardando dev` |
| "aguardando deploy", "aguardando release", "fix não subiu" | `⏳ aguardando deploy` |
| "aguardando responsável", "aguardando retorno", "aguardando decisão" | `⏳ aguardando externo` |
| "bloqueada", "impedimento" | `⏳ bloqueado` |
| Sem indicação de bloqueio | (sem marca) — assume-se que depende de você |

### 4. Move concluídos do dia

> [!important] Isto é do script, não do agente (desde 28/07)
> Quem move os `[x]` pro fim, sob o header `✅ Concluídos hoje`, é `coleta_concluidos()` no `qa-atualiza.py`. É operação mecânica e idempotente; o agente não precisa refazer.

Itens marcados `[x]` hoje (concluídos nesta daily) vão pra subseção `✅ Concluídos hoje` no fim da lista, com separador visual. Itens marcados em dias anteriores não reaparecem — o carry-over já os removeu.

### 5. Alerta zumbis

Item com +7 dias de arrasto → registra no Auto-organização:
```
⚠️ item parado há Nd: "<título>" — revisar ou descartar
```

### 6. Auto-resolve órfãos

Card em `Concluídas/` ou `99 Arquivo/` que ainda tem pendência de "Acompanhar" → pendência fechada automaticamente com `→ card concluído/descartado`.

## Exemplo (dia 20/07/2026)

Antes (14 itens, plano):

```
- [ ] SGV-9610 - Validar em DEV
- [ ] Planejamento SP15 - Bater os 53 cards
- [ ] Planejamento SP15 - Reexportar a view completa
- [ ] SGV-4873 - Refinar
- [ ] SGV-9963 - Revisar cenários de teste
- [ ] MEL-0001 - Cadastrar melhoria no Notion
- [ ] Detalhar passo a passo da captura...
- [ ] SGV-9971 - Acompanhar
- [ ] SGV-9977 - Acompanhar
- [ ] SGV-8977 - Atualizar no Notion
- [ ] SGV-9036 - Confirmar critérios
- [x] SGV-9750 - Revisar cenários de teste
- [x] SGV-5273 - Validar em HML
- [x] SGV-3413 - Verificar se reproduz
```

Depois (agrupado, com idade e bloqueio):

```
### 🎯 Validação
- [ ] [[SGV-9610]] - Validar em DEV (pronto pra teste)

### 🔎 Refinamento
- [ ] SGV-4873 - Refinar 🕐 3d ⏳ aguardando responsável
- [ ] [[SGV-9963]] - Revisar cenários 🕐 5d ⏳ aguardando dev

### 📤 Cadastro
- [ ] [[MEL-0001]] - Cadastrar no Notion 🕐 5d ⚠️
- [ ] [[SGV-8977]] - Atualizar no Notion

### 👁️ Acompanhamento
- [ ] [[SGV-9971]] - Acompanhar
- [ ] [[SGV-9977]] - Acompanhar
- [ ] SGV-9036 - Confirmar critérios no Notion

### 📋 Triagem
- [ ] [[Planejamento/SP15|Triagem SP15]] - Bater os cards
- [ ] Triagem SP15 - Reexportar view

### 🚨 Parado (7+ dias)
- [ ] Detalhar captura despacho sigiloso 🕐 7d 🚨

### ✅ Concluídos hoje
- [x] [[SGV-9750]] - Revisar cenários (ok)
- [x] [[SGV-5273]] - Validar em HML (aprovada)
- [x] [[SGV-3413]] - Verificar se reproduz (descartado)
```

## Fronteira com o script (definida em 28/07)

Em 28/07 uma sessão de IA moveu o agrupamento por natureza pra dentro do `qa-atualiza.py` (função `reorganiza_afazer`). Deu ruim: a fila passou a ser reescrita em todo 🔄 por keywords, com os efeitos colaterais registrados na daily de [[QA Workspace/01 Daily/2026-07/28-07|28/07]] (item caindo no grupo errado, `🚨 Parado` e `✅ Concluídos hoje` sumindo). A função foi **revertida** e a divisão de trabalho ficou assim:

| Responsabilidade | Dono | Por quê |
|---|---|---|
| Agrupar por natureza (🎯 🔎 📤 👁️ 📋) | **Este agente (IA)** | É julgamento: depende de ler a intenção do item, não dá pra decidir por keyword — "Reexportar a view do Notion" não é Cadastro |
| Idade `🕐`/`⚠️`/`🚨` | **`qa-atualiza.py`** (`envelhece_fila`) | Aritmética de data; determinístico e roda sempre, sem depender da IA lembrar |
| Mover `[x]` pra `✅ Concluídos hoje` | **`qa-atualiza.py`** (`coleta_concluidos`) | Mecânico e idempotente |
| Ledger (Atividades → `[x]` na fila) | **`qa-atualiza.py`** (`ledger_do_dia`) | Já era do script |

Regra prática: **se dá pra decidir com uma conta ou um regex seguro, é do script; se precisa entender o que o item quer dizer, é do agente.** Ao mexer no `.py`, conferir se a mudança não invade a coluna do agente — e vice-versa.

## Relação com outros agentes

- **AGENTE_ORGANIZADOR**: Fornece o carry-over e a fila viva que este agente lê e reorganiza
- **AGENTE_STATUS_REUNIAO**: Itens em "Foco de hoje" refletem a fila organizada

## Copy padronizada

O agente nunca altera o texto dos itens — só agrupa, adiciona marcadores (🕐, ⏳, ⚠️) e move concluídos. O texto original da pendência é preservado integralmente.
