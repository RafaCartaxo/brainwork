---
tags:
  - sistema
  - agentes
---
# Agentes

Agentes são comportamentos autônomos do vault — eles executam ações sem intervenção humana, seguindo regras pré-definidas.

Diferente de [[../Skills|Skills]] (que são instruções de referência para você ou a IA seguir quando solicitado), agentes **disparam sozinhos** em resposta a gatilhos específicos.

## Agentes ativos

| Agente | Gatilho | O que faz |
|---|---|---|
| [[AGENTE_ORGANIZADOR]] | 🔄 Atualizar (Dashboard) / "organiza a daily" (IA) / 7h (agendado) | Classifica registros crus, completa ciclos de pendências, reconcilia Atividades com cards, mantém a fila viva |
| [[AGENTE_MIGRACAO_CARDS]] | Conclusão de pendência / "move o card" (IA) / verificação diária | Move cards entre pastas da esteira atualizando wikilinks, frontmatter e Histórico atomicamente |
| [[AGENTE_STATUS_REUNIAO]] | 🔄 Atualizar / "status da reunião" (IA) / abertura da daily | Lê Atividades + fila da daily e gera o bloco Status — reunião (Fiz/Foco/Travas) |

## Como funciona um agente

1. **Gatilho** dispara o agente (botão, comando de IA, horário)
2. **Fonte** é a daily mais recente (ou a especificada)
3. **Regras** definem o que fazer com cada tipo de registro
4. **Resultado** é registrado no bloco `### Auto-organização` da daily

## Criar um novo agente

1. Criar arquivo `AGENTE_NOME.md` nesta pasta
2. Especificar: gatilho, fonte, regras, resultado esperado
3. Referenciar em [[../Contexto/FLUXOS|FLUXOS]] se for parte de um fluxo
