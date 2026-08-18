---
tags:
  - qa
  - skill
---
# Skill: Melhoria (da ideia ao cadastro)

Orquestra o ciclo completo de uma melhoria de produto — da ideia anotada na daily até o cadastro no Notion e entrada na esteira de validação. É o fio condutor do [[../Contexto/FLUXOS#4. Melhoria: da ideia ao cadastro|fluxo 4]]. Não duplica as regras que já existem: aponta pra elas e encadeia na ordem certa.

## Contexto (pra qualquer IA/pessoa sem o setup na cabeça)

- **Onde nasce**: `## Melhorias propostas` da daily, como checkbox `MEL-NNNN · Título`
- **Template do card**: [[../Templates/Demanda.md|Demanda]] (hub — diferente de bug que usa Bug Report autocontido)
- **Destino do card**: `QA Workspace/02 Demandas/DEV/`, arquivo `MEL-NNNN - <título>` (renomeado com SGV após cadastro)
- **Regras completas de MEL**: [[../../QA Workspace/01 Daily/README#Regra de Melhorias propostas|01 Daily/README]] (formato do checkbox, numeração, ciclo de vida)
- **Copy oficial**: catálogo de frases em [[../../QA Workspace/01 Daily/README|01 Daily/README]] — seções Melhoria e Planejamento

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Ideia anotada na daily | "registra essa melhoria", "cria MEL pra ideia X" |
| Refinar melhoria existente | "refina a MEL-0001", "vamos destilar a MEL-0001" |
| Cadastrar no Notion | "cadastra a MEL-0001 no Notion" |
| Levantar plano de teste | "plano de teste da MEL-0001" |

## Melhoria × Bug (por que skill separado)

| Aspecto | Bug | Melhoria |
|---|---|---|
| Natureza | Comportamento errado que existe | Sistema funciona, pode funcionar melhor |
| Template | [[../Templates/Bug Report.md|Bug Report]] (nota única, autocontida) | [[../Templates/Demanda.md|Demanda]] (hub — agrega plano, CTs, evidências, bugs) |
| Refinamento | Análise de causa raiz | Definição de escopo + regras de negócio |
| Skill | [[SKILL_BUGS]] | SKILL_MELHORIA (este arquivo) |

## Passo a passo

### 1. Registrar a ideia

Checkbox em `## Melhorias propostas` da daily do dia:

```markdown
- [ ] **MEL-NNNN · <Título curto e acionável>** — <contexto em 1 frase>. (origem: [[card|SGV-XXXX]])
```

- **Número**: sequencial global (MEL-0001, MEL-0002...). Nunca reaproveitado — mesmo descartada mantém o número. Próximo número: [[../../QA Workspace/Dashboard/Dashboard|Dashboard]].
- **Origem**: opcional, quando a ideia nasceu de um card específico.
- **Daily**: `💭 MEL-NNNN - Melhoria proposta` em Atividades.

### 2. Refinar (escopo + regras de negócio)

Conduzir usando [[SKILL_REFINAMENTO]] como sub-passo. O foco muda:

- **O que analisar**: escopo, regras de negócio afetadas, impacto em outros fluxos, dependências
- **O que definir**: o que entra e o que fica fora do escopo, prioridade
- **Gate de doc**: cruzar regras contra [[../../QA Workspace/04 Conhecimento/README|04 Conhecimento]] via [[SKILL_VERIFICACAO_DOC]]
- **Material importado**: se veio export do Notion, usar [[SKILL_LIMPEZA_EXPORT]] modo A (envelopar no Refinamento.md em `05 Refinar/`). Se já tem informações suficientes, pular a mesa.

**Se descartada no refinamento**: marcar checkbox, `🗑️ MEL-NNNN - Melhoria descartada (<motivo>)` na daily. Fim do ciclo.

Daily: `🔎 MEL-NNNN - Análise (<resultado curto>)` em Planejamento a cada rodada.

### 3. Criar plano de teste

Usar [[SKILL_PLANO_DE_TESTE]] — definir escopo, tipos de teste, dependências, critérios de aceite. O plano **mora dentro do card hub**, não em arquivo separado.

### 4. Criar casos de teste

Usar [[SKILL_CASOS_DE_TESTE]] — um CT por critério de aceite (checklist de completude na própria skill). Os CTs moram na seção `## Casos de teste` do card hub.

### 5. Criar o card hub

Criar em `02 Demandas/DEV/` usando [[../Templates/Demanda.md|Demanda]]:

| Campo | Valor |
|---|---|
| **Arquivo** | `MEL-NNNN - <título>.md` (sem SGV ainda) |
| **Frontmatter** | `task: ""`, `mel: "NNNN"`, `status: dev`, `data_inicio: hoje` |
| **Conteúdo** | Resumo, Regras de negócio, Pontos de atenção, Casos de teste, Evidências, Histórico |
| **Link reverso** | Transformar `MEL-NNNN` no checkbox da daily original em wikilink pro card ([[../../QA Workspace/01 Daily/README#Regra de links|Regra de links]]) |

Daily: `📝 MEL-NNNN - Melhoria refinada (card criado)` em Planejamento.

### 6. Cadastrar no Notion

- Cadastrar como task no Notion → ganha número SGV
- Preencher `task` e Link no card
- Renomear arquivo: `MEL-NNNN - <título>.md` → `<SGV> - <título>.md`
- Atualizar wikilinks no vault ([[../Agentes/AGENTE_MIGRACAO_CARDS|AGENTE_MIGRACAO_CARDS]])
- Marcar checkbox na daily original como `[x]`

Daily: `💡 SGV-XXXX - Melhoria cadastrada (MEL-NNNN)` em Atividades.

### 7. Esteira de validação

A partir do cadastro, segue o ciclo de qualquer demanda ([[../Contexto/FLUXOS#3b–3d. Validar em DEV / HML / Hotfix|fluxos 3b–3d]]), com **gate de doc a cada aprovação** ([[SKILL_VERIFICACAO_DOC]]) e, depois de aprovada, automação ([[../Contexto/FLUXOS#3h. Após aprovar: preparar automação|fluxo 3h]] → [[SKILL_INICIAR_AUTOMACAO]]).

Frases com tipo explícito: `✅ SGV-XXXX - Melhoria aprovada em <ambiente>`, `🔁 SGV-XXXX - Melhoria retestada e aprovada em <ambiente>`, `🔴 SGV-XXXX - Melhoria reaberta em <ambiente>`.

#### 7a. Em DEV: CT que reprova vira **Defeito**

O que fazer quando um CT reprova é a parte que faltava aqui — e é o que separa DEV de HML.

1. **Executar os CTs** do card hub em DEV, gravando evidência
2. **CT reprovou → nasce um Defeito** (não um Bug): card com `pai: "<SGV desta Melhoria>"`, tag `defeito`, arquivo `<SGV> - Defeito <Título>`. Fluxo: [[../Contexto/FLUXOS#3i. Defeito (filho de task pai)|FLUXOS → 3i]] · criação: [[SKILL_BUGS]]
3. **A Melhoria volta a `🔴 Melhoria reaberta em DEV`** — na daily: `🐛 SGV-XXXX - Defeito cadastrado (da SGV-YYYY)`
4. Dev corrige → **revalidar o CT afetado neste card**, não o defeito isolado. CT passa de `Não` pra `Sim` com **callout de reconciliação** ([[SKILL_CASOS_DE_TESTE]])
5. Defeito fecha em `Concluídas/` com `ambiente: DEV`, Histórico nomeando esta Melhoria

> [!warning] Gate: não aprovar em DEV com defeito aberto
> Identificou, resolve. Aprovar entrega cujo próprio CT reprovou é registro falso. Exceção (produto adia o fix) exige decisão explícita registrada **neste card**, dizendo quem decidiu e por quê — o `🔄` avisa quando a aprovação chega com defeito filho ainda aberto.

Na fila, os defeitos aparecem **aninhados sob a linha desta Melhoria**, não como itens soltos.

#### 7b. Em HML: valida-se a entrega inteira

Aprovada em DEV, o card vai pra `HML/`. Aqui **não se reteste defeito** — cada um já foi validado pelo CT que o encontrou. O que se valida é **a Melhoria como um todo**.

**Problema encontrado em homologação é Bug**, não Defeito: nasce sem `pai:`, com tag `bug`, e segue a esteira completa com vida própria ([[../Contexto/FLUXOS#3g. Reprovação com bug novo (SGV próprio)|fluxo 3g]]).

**Precedente**: SGV-3234 (Refatoração de Etiquetas), 17/08 — 29 CTs em DEV, 5 defeitos encontrados e corrigidos, os 5 fechados sem passar por HML. Foi o caso que originou esta regra.

## Handoff

| De | Para | Quando |
|---|---|---|
| Passo 1 (ideia) → | Passo 2 (refinamento) | Checkbox criado na daily |
| Passo 2 (refinamento) → | Passo 3 (plano) | Escopo definido, regras mapeadas |
| Passo 3–4 (plano + CTs) → | Passo 5 (card) | Plano e CTs prontos pra embarcar no hub |
| Passo 5 (card) → | Passo 6 (Notion) | Card hub criado em `02 Demandas/DEV/` |
| Passo 6 (Notion) → | Passo 7 (esteira) | Ganhou SGV, arquivo renomeado, checkbox marcado |
| Passo 7a (CT reprovou em DEV) → | [[SKILL_BUGS]] (modo Defeito) | Card de defeito com `pai:` preenchido |
| Passo 7a (sem defeito aberto) → | Passo 7b (HML) | Todos os CTs em `Sim`, gate de doc registrado |
| Passo 7 (aprovada HML) → | [[SKILL_INICIAR_AUTOMACAO]] | Card validado, CTs executados, fix no ambiente do Cypress |

## Resultado Esperado

Melhoria registrada, refinada com escopo claro, card hub com plano e CTs, cadastrada no Notion com SGV, e entrando na esteira de validação — com rastro completo na daily e na fila em cada etapa, sem lacuna entre a ideia e o teste.
