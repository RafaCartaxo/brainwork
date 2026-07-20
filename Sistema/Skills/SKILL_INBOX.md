---
tags:
  - qa
  - skill
---
# Skill: Auto-organização da Daily

> [!info] Agente autônomo
> A lógica de classificação, roteamento e continuação de pendências é executada pelo [[../Agentes/AGENTE_ORGANIZADOR|Agente Organizador]] — este skill descreve como invocá-lo e o que esperar.

## Como usar

### Gatilhos disponíveis

| O que fazer | Como | O que cobre |
|---|---|---|
| Parte mecânica (rápido, offline) | Clicar **🔄 Atualizar** na [[../../QA Workspace/Dashboard/Dashboard\|Dashboard]] | Carry-over, conclusão de pendências anotadas, reconciliação de Atividades, fila viva |
| Tudo (classificação de registros crus + mecânica) | Pedir numa sessão: "organiza a daily" | Tudo acima + classificar Anotações e Bugs encontrados sem card |
| Automático | Agendado às 7h (via cron, opcional) | Tudo, com palpite automático |

### O que acontece

1. O organizador lê a daily mais recente
2. Roteia registros crus (Anotações, Bugs encontrados) pros destinos corretos
3. Completa ciclos de pendências marcadas com resultado anotado entre parênteses
4. Reconcilia Atividades escritas à mão com os cards correspondentes
5. Garante que todo card aberto tem item ativo na fila (invariante da fila viva)
6. Registra tudo no bloco recolhido `[!organizacao]- Auto-organização` da daily

### Marca de processado

Linhas processadas ganham ` → <resultado>` no final. O organizador nunca reprocessa linha que já tem essa marca.

### Copy padronizada

Tudo que o organizador escreve segue as frases oficiais do [[../../QA Workspace/01 Daily/README\|01 Daily/README]] — nunca inventa redação própria.

## Regras completas

A especificação detalhada (tabela de continuação de pendências, roteamento, reconciliação, invariante da fila viva) está em [[../Agentes/AGENTE_ORGANIZADOR|AGENTE_ORGANIZADOR]]. Design completo em [[../Specs/2026-07-14-inbox-auto-organizacao-design.md|Spec]].
