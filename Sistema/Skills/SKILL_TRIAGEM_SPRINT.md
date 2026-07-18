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

### 4. Criar documento de triagem

Arquivo em `05 Refinar/Triagem - <sprint>.md` com:

```markdown
# Triagem - SP<N>

> [!info] Export do Notion em YYYY-MM-DD — <n>/<total> cards

## Por status

### Homologação (<n>)
- [[card|SGV-XXXX]] — <título>
- SGV-YYYY — <título> (sem card no vault)

### Teste DEV (<n>)
...
```

### 5. Pendências e daily

- Pendência na fila: `📋 Triagem <sprint> - <n>/<total> cards batidos`
- Cada card sem análise ganha pendência própria
- Cards com divergência ganham pendência de alinhamento
- Na daily: linha em `### Planejamento` com detalhes recolhidos

## Copy na daily

```
📋 [[05 Refinar/Triagem - SP15|Triagem SP15]] - 12/53 cards batidos
  (6 com critérios, 4 já refinados no vault, 1 refinado hoje, 1 em construção)
```

## Resultado Esperado

Documento de triagem criado, cards cruzados com o vault, divergências identificadas e anotadas, pendências de acompanhamento na fila.
