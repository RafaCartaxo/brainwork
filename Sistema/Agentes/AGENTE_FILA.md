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

| Gatilho | Quando dispara |
|---|---|
| **🔄 Atualizar** | Junto com o script `qa-atualiza.py`, ao clicar o botão na Dashboard |
| **Sessão interativa** | "organiza a fila" |

## O que faz

### 1. Agrupa por natureza

Cada item da fila é classificado pelo verbo de ação:

| Grupo | Padrão de reconhecimento |
|---|---|
| 🎯 **Validação** | "Validar", "Retestar", "Revalidar", "Testar", "Verificar se reproduz" |
| 🔎 **Refinamento** | "Refinar", "Revisar cenários", "Analisar", "Investigar" |
| 📤 **Cadastro** | "Cadastrar no Notion", "Atualizar no Notion", "Levar análise", "Registrar" |
| 👁️ **Acompanhamento** | "Acompanhar", "Verificar task", "Confirmar critérios", itens sem verbo de ação claro |
| 📋 **Triagem** | "Triagem", "Bater os cards", "Reexportar" |

### 2. Sinaliza idade

Todo item que veio do carry-over (carregado das "Pendências de ontem") ganha o marcador de idade:

| Dias arrastado | Marca |
|---|---|
| 1-2 dias | (sem marca — normal) |
| 3-4 dias | `🕐 Nd` |
| 5-6 dias | `🕐 Nd ⚠️` |
| 7+ dias | `🕐 Nd 🚨` + alerta no Auto-organização |

A idade é calculada a partir da primeira aparição do item em qualquer daily (não da daily de hoje).

### 3. Sinaliza bloqueio

Se o texto do item indica bloqueio, adiciona o motivo:

| Padrão | Marca |
|---|---|
| "aguardando dev", "MR em revisão", "quando o dev entregar" | `⏳ aguardando dev` |
| "aguardando responsável", "aguardando retorno", "aguardando decisão" | `⏳ aguardando externo` |
| "bloqueada", "impedimento" | `⏳ bloqueado` |
| Sem indicação de bloqueio | (sem marca) — assume-se que depende de você |

### 4. Move concluídos do dia

Itens marcados `[x]` hoje (concluídos nesta daily) vão pra subseção `### ✅ Concluídos hoje` no fim da lista, com separador visual. Itens marcados em dias anteriores não reaparecem — o carry-over já os removeu.

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
- [ ] Triagem SP15 - Bater os 53 cards
- [ ] Triagem SP15 - Reexportar a view completa
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
- [ ] [[Triagem SP15]] - Bater os cards
- [ ] Triagem SP15 - Reexportar view

### ⚠️ Parado (sem ação há 6+ dias)
- [ ] Detalhar captura despacho sigiloso 🕐 6d ⚠️

### ✅ Concluídos hoje
- [x] [[SGV-9750]] - Revisar cenários (ok)
- [x] [[SGV-5273]] - Validar em HML (aprovada)
- [x] [[SGV-3413]] - Verificar se reproduz (descartado)
```

## Relação com outros agentes

- **AGENTE_ORGANIZADOR**: Fornece o carry-over e a fila viva que este agente lê e reorganiza
- **AGENTE_STATUS_REUNIAO**: Itens em "Foco de hoje" refletem a fila organizada

## Copy padronizada

O agente nunca altera o texto dos itens — só agrupa, adiciona marcadores (🕐, ⏳, ⚠️) e move concluídos. O texto original da pendência é preservado integralmente.
