---
tags:
  - qa
  - skill
---
# Skill: Triagem de Sprint

Processar export de view de sprint do Notion — dezenas de cards num arquivo só — agrupando por status, cruzando com o vault e identificando divergências.

## Pipeline

### 1. Agrupar cards por status do Notion

O export de view do Notion traz cada card com seu status atual. Agrupar nas categorias padrão:

| Status no Notion | Significado |
|---|---|
| Homologação | Em validação em HML |
| Teste DEV | Em validação em DEV |
| Testando HML | Validação em andamento em HML |
| Revisar MR | Dev entregou, aguardando revisão de QA |
| Em dev | Ainda em desenvolvimento |
| Impedimento | Bloqueado por dependência |
| Não reproduzido | Bug não confirmado |
| Backlog | Aguardando priorização |
| Produção/Concluído | Já entregue |

### 2. Cruzar com o vault

Pra cada card com SGV reconhecido:
- Buscar se já existe card correspondente em `02 Demandas/`
- Se existe → **wikilink** pro card no vault
- Se não existe → anotar como "sem card no vault"

### 3. Identificar divergências Notion × vault

Comparar o status no Notion com o status real do card no vault:

| Divergência comum | Exemplo |
|---|---|
| Notion "Backlog", vault "em validação em HML" | Card avançou no vault mas não atualizaram o Notion |
| Notion "Homologação", vault "DEV" | Card foi movido pra DEV mas Notion ficou pra trás |
| Notion "Concluído", vault "HML" | Card concluído no Notion mas ainda não validado |

Divergências viram item em `## Anotações` da daily pra alinhar com o time.

### 4. Criar página de planejamento

Criar uma **página única** `Planejamento/SP<N>.md` — como a daily note, mas no escopo da sprint. Organizada por estágio QA na ordem do fluxo real:

```markdown
# Planejamento SP<N>

> [!info] Sprint D/M → D/M | Progresso: X/Y batidos
> A revisar: X/Y · Ação imediata: X/Y · Em validação: X/Y · Aguardando deploy: X/Y · Aguardando dev: X/Y · Acompanhamento: X/Y

## A revisar (n)            ← decidir antes de agir
### Revisar MR
### Refinar / definir critérios
### Alertas

## Ação imediata (n)         ← testar AGORA
### 🔴 Homologação
### 🟡 DEV

## Em validação (n)          ← testes em andamento
### DEV
### HML

## Aguardando deploy (n)     ← aprovado, esperando subir
### ⏳ Subir pra HML
### ⏳ Release

## Aguardando dev (n)        ← bloqueado por terceiros
### Em desenvolvimento
### Impedimento / CX

## Acompanhamento (n)        ← concluídos, sem ação
### Concluído / Produção
### Não reproduzido / Descartado
### Duplicados
### Outro QA aprovou
### Órfãos do export
### Backlog

## Decisões recentes
## Registro
```

A ordem segue o pipeline QA real: primeiro decide, depois testa, depois acompanha. "Não reproduzido" vai pra Acompanhamento — bug que não reproduz mais é concluído (provavelmente corrigido por outra feature), não gera pendência.

### 5. Pendências e daily

- Pendência na fila: `📋 Triagem <sprint> - <n>/<total> cards batidos`
- Cada card sem análise ganha pendência própria
- Cards com divergência ganham pendência de alinhamento
- Na daily: linha em `### Planejamento` com detalhes recolhidos

## Copy na daily

```
📋 [[Planejamento/SP15|Planejamento SP15]] - 44/82 cards batidos
  (Ação imediata: 14 · Em validação: 5 · Aguardando deploy: 5 · A revisar: 18 · Aguardando terceiros: 12 · Acompanhamento: 32)
```

## Resultado Esperado

Página de planejamento criada como página única por sprint, cards cruzados com o vault, divergências identificadas e anotadas, pendências de acompanhamento na fila. O callout do topo agrega o progresso geral. Exemplo: [[../../QA Workspace/Planejamento/SP15|Planejamento SP15]].
