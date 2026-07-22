---
tags:
  - qa
  - skill
---
# Skill: Verificação contra Documentação

Cruzar o comportamento de um bug/demanda (o que foi relatado, o resultado esperado, ou o que foi aprovado na validação) contra a documentação de módulo em [[../../QA Workspace/04 Conhecimento/README|04 Conhecimento]] — para confirmar o critério de aceite, ou expor uma divergência entre o sistema e a doc. Mesma filosofia do [[SKILL_REVISAO_ESCOPO_MR]]: **registrar a divergência, não julgar quem está certo** — QA sinaliza, Produto decide.

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Pedido explícito | "verifica a SGV-XXXX contra a doc", "bate esse bug com a documentação", "isso está na doc?" |
| Dentro do refinamento (fluxo 6) | ao preencher o **resultado esperado**/critérios da mesa `05 Refinar/`, confirmar contra a doc do módulo antes de destilar o card |
| Ao criar card de bug ([[SKILL_BUGS]]) | ao definir **Resultado Esperado** e **Critérios de aceite**, checar se a doc respalda |
| Ao validar/aprovar em HML (fluxo 3c) | quando o comportamento aprovado contradiz a doc → a doc provavelmente está desatualizada |

## Gate obrigatório — antes de ✅ aprovar e antes de destilar o card

Rodar esta verificação **não é opcional** nestes dois momentos:
- **Ao destilar o card no refinamento** (fechar resultado esperado + critérios): cruzar contra a doc do módulo antes de fechar o Destilado.
- **Antes de marcar `✅ aprovado`** numa validação (DEV/HML): cruzar o comportamento aprovado contra a doc **no momento da aprovação**, não em retrospectiva. Não marque ✅ nem mova o card pra próxima pasta antes de rodar a verificação e registrar o veredito.

**Se a doc do módulo não existe:** não pule em silêncio. Registrar a lacuna e **abrir pendência "Importar doc de \<Módulo\> (fluxo 8)"** na fila da daily — ausência de doc é gap a preencher, não "ok, segue".

Rede de segurança do gate: [[AGENTE_VALIDACAO_DOC]] varre, na organização da daily, cards aprovados sem esse registro e levanta pendência.

## 1. Achar a doc do módulo

1. Identificar o **módulo** — do campo `módulo` do card/mesa, ou do título/descrição do bug (ex.: "Novo rastreio de documentos" → módulo **Rastrear Documento**).
2. Localizar em `04 Conhecimento/Módulos/<Módulo>.md`. Fluxos ponta a ponta ficam em `04 Conhecimento/Fluxos/`.
3. **Doc não existe** → não inventa. Registrar a lacuna (ver seção 4, caso *silêncio*) e sugerir importar a doc via [[../Contexto/FLUXOS#8. Importar documentação do projeto|Fluxo 8]]. Seguir sem bloquear.

## 2. Isolar as duas afirmações a comparar

- **Do bug/demanda**: qual é o comportamento em questão? Extrair o **Resultado Esperado** (ou o resultado esperado *inferido* do MR/análise, se ainda a validar), não o sintoma cru.
- **Da doc**: achar a regra correspondente. Buscar por termos do comportamento (nome da ação, do botão, do estado). Citar **o trecho e a linha** — não parafrasear de memória.

## 3. Cruzar — três resultados possíveis

| Resultado | O que significa | Ação |
|---|---|---|
| ✅ **Confirma** | A doc respalda o resultado esperado | Reforça o critério de aceite. Registrar que a doc respalda (com link + linha) — dá confiança pra validação |
| ⚠️ **Diverge** | A doc diz o **contrário** do que o bug/validação afirma | Registrar a divergência com `[!warning]`, **sem deduzir quem está certo**. Se a validação **já aprovou** o comportamento oposto ao da doc → a doc está provavelmente **desatualizada** → decisão de Produto + pendência de atualizar a doc (seção 5) |
| ❓ **Silêncio/lacuna** | A doc **não cobre** o cenário | Registrar como **Dúvida em aberto** na doc do módulo + possível gap de documentação. Não é bloqueio |

Regra de ouro (herdada do [[SKILL_REVISAO_ESCOPO_MR]]): **não deduzir se está certo ou errado, só registrar a divergência.** QA não decide entre "a doc está errada" e "o bug está errado" — expõe o conflito pra Produto/Dev resolverem.

## 4. Onde registrar cada resultado

- **Divergência viva** → callout `[!warning]` na mesa de refinamento (`05 Refinar/`, enquanto estiver lá) **e/ou** nas **Observações** do card; e na doc do módulo, na seção `## Comportamentos observados em teste (QA)`, com **data e ambiente** (é exatamente o que o cabeçalho `[!info] Origem` da doc pede: "ao detectar divergência com o sistema em teste, atualizar aqui").
- **Lacuna/silêncio** → item na seção `## Dúvidas em aberto` da doc do módulo.
- **Confirmação** → nada obrigatório na doc; opcionalmente adicionar o SGV validado em `## Cards relacionados` da doc (rastreabilidade bug↔módulo).
- **Na daily** (`## Atividades → ### Planejamento`): `🔎 SGV-XXXX - Verificado contra doc [[<Módulo>]] — <resultado curto>` (ex.: "doc respalda", "diverge — doc desatualizada, decisão de produto").

## 5. Divergência com decisão de Produto (não editar a regra sozinho)

Quando a divergência é **decisão de negócio** (a doc pode estar certa e o bug errado, ou vice-versa):

- **NÃO** reescrever a regra da doc por conta própria. Só **registrar** o conflito (`[!warning]` + "Comportamentos observados em teste" com data).
- Abrir a decisão como **pendência/dúvida** pra confirmar com Dev/Produto (na daily e/ou nas Anotações via `[IA]`).
- **Só depois de confirmada** a decisão: atualizar a regra na doc **e** registrar a mudança em `## Comportamentos observados em teste (QA)` (com data e o que mudou). Aí a divergência vira histórico resolvido.

## Exemplo real (2026-07-21 — SGV-9464)

- **Módulo**: [[../../QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]].
- **Bug/validação**: "Novo rastreio" deve **reiniciar os filtros** (`statusFilter`, `importedDocuments`) — aprovado em HML.
- **Doc (linha 54)**: diz que "Novo rastreio" reabre o modal *mantendo os resultados anteriores visíveis ao fundo* e **não menciona reiniciar filtros** — tratava manter o estado como comportamento especificado.
- **Resultado**: ⚠️ **Diverge**. Como a validação aprovou "reiniciar filtros", a doc está provavelmente **desatualizada** (fonte de 25/03 vs. bug/MR de julho). Registrado como decisão de Produto em aberto — doc **não** editada até confirmar. Assim que confirmar: atualizar a linha do "Novo rastreio" + registrar em "Comportamentos observados em teste".

## Resultado Esperado

Um veredito rápido por demanda — **doc respalda**, **doc diverge** (→ decisão de Produto) ou **doc silencia** (→ dúvida em aberto) — com o trecho exato da doc citado e o registro no lugar certo (mesa/card/doc/daily). Nunca "verifiquei" sem citar a linha da doc, e nunca reescrever regra de negócio da doc sem decisão confirmada.
