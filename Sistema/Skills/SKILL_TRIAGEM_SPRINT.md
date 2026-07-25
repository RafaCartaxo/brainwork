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

Criar uma **página única** `Planejamento/SP<N>.md` — como a daily note, mas no escopo da sprint. Status em ordem cronológica do pipeline QA:

```markdown
# Planejamento SP<N>

> [!info] Sprint D/M → D/M | Progresso: X/Y batidos

## Backlog (n)
## Em desenvolvimento (n)
## Refinamento (n)
## Revisar MR (n)
## Pronto pra teste em dev (n)     ← dev finalizou, aguardando deploy DEV
## Em teste (n)                    ← fix no ambiente, QA testando
## Aguardando deploy HML (n)       ← aprovado DEV, fix não subiu
## Pronto pra homologação (n)      ← Notion "disponível", aguardando deploy HML
## Aguardando release (n)          ← aprovado HML, release
## Impedimento / CX (n)
## Em produção / Concluído (n)
## Não reproduzido / Descartado (n)
## Duplicados (n)
## Outro QA aprovou (n)
## 👻 Órfãos do export (n)
```

Cada card em 1 linha: `- [ ] **SGV-XXXX** — título curto · prioridade · dev · squad`. Notas e alertas em sub-bullet.

**Regras**:
- "Pronto pra teste em dev" ≠ está em DEV — dev finalizou, aguardando deploy
- "Pronto pra homologação" ≠ está em HML — Notion disponível, aguardando deploy
- Só "Em teste" = fix no ambiente, testando
- "Não reproduzido" nasce `[x]` — bug não reproduz mais = concluído
- Duplicados nascem `[x]`
- Apenas Órfãos do export usa callout colapsável (`> [!note]-`)

### 5. Pendências e daily

- Pendência na fila: `📋 Triagem <sprint> - <n>/<total> cards batidos`
- Cada card sem análise ganha pendência própria
- Cards com divergência ganham pendência de alinhamento
- Na daily: linha em `### Planejamento` com detalhes recolhidos

## Copy na daily

```
📋 [[../../QA Workspace/Planejamento/SP15|Planejamento SP15]] - 50/82 cards batidos
  (Ação imediata: 8/14 · Em validação: 2/3 · Aguardando deploy: 5/5 · A revisar: 6/9 · Aguardando dev: 0/5 · Acompanhamento: 29/46)
```

## Resultado Esperado

Página de planejamento criada como página única por sprint, com seções colapsáveis na ordem do fluxo QA. Cards cruzados com o vault, divergências identificadas, pendências na fila. Exemplo: [[../../QA Workspace/Planejamento/SP15|Planejamento SP15]].
