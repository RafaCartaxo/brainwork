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

Criar uma **página única** `Planejamento/SP<N>.md` — como a daily note, mas no escopo da sprint. Seções colapsáveis — só a "Ação imediata" fica expandida por padrão.

```markdown
# Planejamento SP<N>

> [!info] Sprint D/M → D/M | ⚡X/Y ⚙️X/Y 🚦X/Y ⏳X/Y 📋X/Y ✅X/Y
> Fontes: Notion D/M...

---

> [!note]- 📋 A revisar (n) · X batidos
> Cards que precisam de decisão antes de entrar em validação.
>
> ### Revisar MR (n)
> - [ ] **SGV-XXXX** — título curto · prioridade · dev · squad
> ### Refinar / definir critérios (n)
> - [x] **SGV-XXXX** — título curto · prioridade · dev · squad
> ### Alertas (n)
> - [x] **SGV-XXXX** — título curto · prioridade · dev · squad

## ⚡ Ação imediata (n) · X batidos
### 🔴 Homologação (n)
- [ ] **SGV-XXXX** — título curto · prioridade · dev · squad
### 🟡 DEV (n)
- [ ] **SGV-XXXX** — título curto · prioridade · dev · squad

> [!note]- ⚙️ Em validação (n) · X batidos
> ### DEV / HML
> ...

> [!note]- 🚦 Aguardando deploy (n) · X batidos
> ### ⏳ Subir pra HML / ⏳ Release
> ...

> [!note]- ⏳ Aguardando dev (n) · X batidos
> ### Em desenvolvimento / Impedimento / CX
> ...

> [!note]- ✅ Acompanhamento (n) · X batidos
> ### Concluído / Produção (n)
> > [!note]- 🗑️ Não reproduzido / Descartado (n)
> > [!note]- 👥 Outro QA aprovou (n)
> > [!note]- 👻 Órfãos do export (n)
> ### Duplicados (n) · Concluídos com card (n) · Backlog (n)

## Decisões recentes
## Registro
```

**Princípios aplicados** (UX do nexus-platform):
- Carga cognitiva baixa: 5 de 6 seções colapsadas, ~30 linhas visíveis ao abrir
- Informação crítica sempre visível: progresso + Ação imediata expandidos
- Progressão natural: ordem do pipeline QA (decidir → agir → validar → deploy → aguardar → acompanhar)
- Cards compactados: 1 linha por card (prioridade + dev + squad inline)
- Sub-seções do Acompanhamento colapsadas (menor relevância, maior volume)

**Regras de classificação**:
- "Não reproduzido" → Acompanhamento (bug não reproduz = concluído, sem pendência)
- "Decididos/duplicados" → Acompanhamento (já decididos, sem ação)
- Apenas "Em desenvolvimento" e "Impedimento/CX" → Aguardando dev

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
