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

Criar uma **pasta** `05 Refinar/Triagem - <sprint>/` com a estrutura abaixo, organizada por estágio QA (não por status do Notion):

```markdown
Triagem - SP<N>/
├── README.md                   ← visão geral, progresso, decisões recentes
├── 01-acao-imediata.md         ← cards testáveis agora (Homologação + Teste dev)
├── 02-em-validacao.md          ← cards com QA ativa (CTs em execução)
├── 03-aguardando-deploy.md     ← aprovado, aguardando fix subir de ambiente
├── 04-a-revisar.md             ← Revisar MR, sem critérios, investigar descarte
├── 05-aguardando-terceiros.md  ← Em dev, impedimento, CX, aguardando sprint
└── 06-acompanhamento.md        ← Produção, outro QA aprovou, decididos, órfãos
```

Cada arquivo contém apenas os cards daquele estágio, com checkboxes, wikilinks e sublinhas (prioridade/dev/origem) preservados. O README agrega o progresso geral e as decisões recentes.

**Por que estágio QA, não status Notion**: um card "Disponível para homologação", um "Pronto pra teste em dev" e um "Aprovado no Dev" têm a mesma ação pendente de QA (validar). Separar por estágio QA responde "o que eu preciso fazer agora" em vez de "onde está no backlog do dev".

### 5. Pendências e daily

- Pendência na fila: `📋 Triagem <sprint> - <n>/<total> cards batidos`
- Cada card sem análise ganha pendência própria
- Cards com divergência ganham pendência de alinhamento
- Na daily: linha em `### Planejamento` com detalhes recolhidos

## Copy na daily

```
📋 [[05 Refinar/Triagem - SP15/README|Triagem SP15]] - 44/82 cards batidos
  (01 Ação imediata: 8/20 · 03 Aguardando deploy: 5/5 · 04 A revisar: 6/18 · 06 Acompanhamento: 27/32)
```

## Resultado Esperado

Documento de triagem criado como pasta com 6 arquivos por estágio QA, cards cruzados com o vault, divergências identificadas e anotadas, pendências de acompanhamento na fila. O README da pasta agrega o progresso geral.
