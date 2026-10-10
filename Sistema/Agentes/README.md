---
tags:
  - sistema
  - agente
---
# Agentes

Agentes são comportamentos autônomos do vault — eles executam ações sem intervenção humana, seguindo regras pré-definidas.

Diferente de [[../Skills/README|Skills]] (que são instruções de referência para você ou a IA seguir quando solicitado), agentes **disparam sozinhos** em resposta a gatilhos específicos.

## Agentes ativos

| Agente | Gatilho | O que faz |
|---|---|---|
| [[AGENTE_PROCESSAR_EXPORT]] | "processa o material novo" / "processa o export SGV-XXXX" | Pipeline completo: classifica .md bruto do Notion (task? triagem? doc?) → limpa → roteia pro destino (mesa/card/conhecimento/triagem) |
| [[AGENTE_FILA]] | **Sessão de IA** (skill `organiza-daily`): "organiza a fila" / "processa o dia" (o 🔄 só prepara idade e concluídos) | Reorganiza "A fazer hoje": agrupa por natureza (🎯🔎📤👁️📋), sinaliza idade (🕐) e bloqueio (⏳), move concluídos, alerta zumbis +7d |
| [[AGENTE_ORGANIZADOR]] | **Script** no 🔄 (só a parte mecânica) · **Sessão de IA** via skill `organiza-daily` (`~/.claude/skills/organiza-daily/`) em "organiza a daily" / "processa o dia" (classificação completa). Modo 7h: ⚠️ previsto, **sem cron ativo** (existe um skill agendado pronto, `qa-inbox-auto-organizacao`, mas não está registrado em nenhum cron) | Classifica registros crus, completa ciclos de pendências, reconcilia Atividades com cards. **Não mantém mais a fila viva automaticamente** (retirado 06/10/2026 — ver abaixo) |
| [[AGENTE_MIGRACAO_CARDS]] | Conclusão de pendência / "move o card" (IA) / verificação diária | Move cards entre pastas da esteira atualizando wikilinks, frontmatter e Histórico atomicamente |
| [[AGENTE_STATUS_REUNIAO]] | Skill `status-reuniao` (`~/.claude/skills/status-reuniao/`) — chamado pelo `organiza-daily` ou direto: "status da reunião" / `/status-reuniao` | Lê Atividades + fila da daily e gera o bloco Status — reunião (Fiz/Foco/Travas) |
| [[AGENTE_VALIDACAO_DOC]] | **Sessão de IA**: "organiza a daily" / "processa o dia" (o 🔄 não faz gate de doc) | Rede de segurança do gate de doc: sinaliza cards aprovados sem cruzamento contra a doc do módulo (levanta pendência ⏳) |

## Gatilhos compartilhados

> [!important] Decisão final sobre a fila automática (06/10/2026)
> Em 24/09/2026 Rafael zerou a fila automática (131 itens acumulados) e pausou o ponto pra decidir depois. Em 06/10/2026 o diagnóstico fechou: a reconciliação de Atividades (o que foi feito vira estado do card) sempre funcionou bem — o problema era só a injeção incondicional de `SGV-XXXX - Acompanhar (<título>)` pra **todo** card aberto com dono, todo dia, sem distinguir se havia ação nova. Essa injeção foi **removida do `qa-atualiza.py`** (`sincroniza_demandas_ativas`, ramo "card normal"). O que continua igual: aninhamento de defeito sob a pai, idade (`🕐`/`⚠️`/`🚨`), coleta de `[x]`, reconciliação de Atividades, `resolve_pendencias_obsoletas`. O que mudou: visibilidade passiva de card aberto sem ação pendente agora é a seção **"Seus cards abertos"** da [[../../QA Workspace/Dashboard/Dashboard|Dashboard]], não mais uma linha na fila do dia — "A fazer hoje" volta a ser só o que tem ação pendente de verdade, escrito manualmente ou por sessão de IA (nunca por varredura). Isso afeta [[AGENTE_FILA]], [[AGENTE_ORGANIZADOR]], [[AGENTE_STATUS_REUNIAO]] e [[AGENTE_VALIDACAO_DOC]] — a descrição operacional de cada um abaixo continua valendo pro que o agente faz quando chamado.
>
> **Status — reunião** também ganhou gatilho real nesta correção: os skills `status-reuniao` e `organiza-daily` do Claude Code (`~/.claude/skills/`) implementam [[AGENTE_STATUS_REUNIAO]] e [[AGENTE_ORGANIZADOR]] de verdade — antes, o "comando `/status-reuniao`" era só uma promessa em markdown que nenhuma ferramenta executava.

> [!warning] O botão 🔄 **não dispara agente nenhum** — corrigido em 30/07
> Esta tabela dizia que o 🔄 disparava cinco agentes. **É impossível**: o botão executa `.obsidian/scripts/qa-atualiza.py`, que é Python e não invoca IA.
>
> Uma sessão de IA simulada sem contexto leu exatamente esta linha e afirmou que o botão fazia o trabalho todo. E foi essa promessa que levou uma sessão, em 28/07, a **mover o agrupamento da fila pra dentro do script** pra fazer a doc virar verdade — quebrando a fila. **A doc causou o bug.**

| Pedido | O que o **script** faz | O que só a **IA** faz |
|---|---|---|
| **🔄 Atualizar** (ou rodar o `.py`) | Cria a daily, carry-over, envelhece a fila, recolhe `[x]`, reconcilia cards, roteia evidência, aninha defeito sob pai existente, grava o log | — |
| **"processa o dia"** / **"organiza a daily"** (skill `organiza-daily`) | O mesmo do 🔄 (é o passo 1) | Agrupar a fila ([[AGENTE_FILA]]) · regenerar o Status ([[AGENTE_STATUS_REUNIAO]], skill `status-reuniao`) · classificar registro cru ([[AGENTE_ORGANIZADOR]]) · gate de doc ([[AGENTE_VALIDACAO_DOC]]) · agir nos avisos do log |
| **"processa o material novo"** | — | [[AGENTE_PROCESSAR_EXPORT]] |
| **"move o card"** | Move sozinho quando a daily declara o desfecho | [[AGENTE_MIGRACAO_CARDS]] nos casos que exigem julgamento |

Sequência completa dos cinco passos: [[../Contexto/FLUXOS#O que "processa" significa|FLUXOS → O que "processa" significa]].

## Como funciona um agente

1. **Gatilho** dispara o agente (botão, comando de IA, horário)
2. **Fonte** é a daily **de hoje** — data resolvida pelo relógio do ambiente no momento de escrever (`date +%F`), nunca reusada de antes na sessão (ver [[../Contexto/PADROES_QA#Regra de data|Regra de data]]) — ou a daily especificada
3. **Regras** definem o que fazer com cada tipo de registro
4. **Resultado** é registrado no bloco recolhido `[!organizacao]- Auto-organização` da daily

## Criar um novo agente

1. Criar arquivo `AGENTE_NOME.md` nesta pasta
2. Especificar: gatilho, fonte, regras, resultado esperado
3. Referenciar em [[../Contexto/FLUXOS|FLUXOS]] se for parte de um fluxo
