---
tags:
  - qa
  - agente
---
# Agente: Migração de Cards

Garantir que a movimentação de cards entre pastas da esteira (`DEV` → `HML` → `Concluídas` → `99 Arquivo`) seja atômica e consistente: atualizar o arquivo, os wikilinks e o Histórico numa operação só.

## Por que existe

Mover um card manualmente ou fora do Obsidian (script, IA, terminal) quebra wikilinks silenciosamente — o Obsidian só reescreve links sozinho quando a movimentação é feita **dentro** dele. Este agente cobre o gap.

## Gatilhos

| Gatilho | Quando dispara |
|---|---|
| **Conclusão de pendência** | O [[AGENTE_ORGANIZADOR]] detecta que um checkbox `[x]` implica movimentação de card (ex.: aprovada em HML → concluída) |
| **Sessão interativa** | Rafael pede "move o card SGV-XXXX pra HML" |
| **Verificação programada** | Varredura diária detecta cards com `ambiente`/`status` inconsistente com a pasta onde estão |

## O que faz

### 1. Movimentação atômica
Para cada card a ser migrado:
1. **Lê** o estado atual (pasta, frontmatter, wikilinks que apontam pra ele)
2. **Move** o arquivo fisicamente pra pasta de destino
3. **Atualiza** o frontmatter (`ambiente` e `status` conforme a esteira)
4. **Atualiza** todos os wikilinks no vault que apontavam pro caminho antigo → novo caminho
5. **Registra** no Histórico do card: `- YYYY-MM-DD - <frase padrão com emoji>`
6. **Registra** na daily: linha em Atividades com a frase padrão

### 2. Esteira padrão

| De | Para | Quando | Status | Ambiente |
|---|---|---|---|---|
| `DEV/` | `HML/` | Aprovada em DEV | mantém | `HML` |
| `HML/` | `Concluídas/` | Aprovada em homologação | `resolvido` | preenche `data_fim` |
| `Hotfix/` | `Concluídas/` | Aprovada em hotfix | `resolvido` | preenche `data_fim` |
| Qualquer | `99 Arquivo/` | Descartada | `descartado` | — |

### 3. Reabertura
Se um card em `Concluídas/` for reaberto:
- `status: aberto` (ou `em_validacao`)
- Move de volta pra `DEV/` ou `HML/` conforme contexto
- Nova pendência de revalidação na fila

### 4. Detecção de inconsistência
Varre `02 Demandas/` periodicamente e sinaliza:
- Card em `HML/` com `ambiente: DEV` → inconsistente
- Card em `Concluídas/` com `status: aberto` → inconsistente
- Card em `DEV/` com `status: resolvido` → inconsistente

Registra na daily no callout `[!organizacao]- Auto-organização` com `⚠️ card em pasta inconsistente: [[card]]`.

## Relação com outros agentes

- **AGENTE_ORGANIZADOR**: Dispara este agente quando um checkbox `[x]` implica movimentação (ex.: "Retestar SGV-XXXX (aprovada em homologação)")
- **AGENTE_STATUS_REUNIAO**: Cards migrados hoje aparecem no Fiz do Status — reunião

## Copy padronizada

Segue o catálogo de frases do [[../../../QA Workspace/01 Daily/README|01 Daily/README]] — mesmo padrão de qualquer validação.
