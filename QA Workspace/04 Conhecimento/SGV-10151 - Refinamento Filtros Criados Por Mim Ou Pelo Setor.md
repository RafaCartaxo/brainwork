---
tags:
  - qa
  - refinamento
task: "10151"
status: refinado
data_inicio: 2026-08-10
responsavel: Rafael
modulo: mesa-de-trabalho
---
# Refinamento: Filtros "Criados por mim" / "Criados pelo setor"

> [!info]- Mesa de trabalho — [[Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada|fluxo 6]]
> Análise e suposição vivem aqui — o card em `02 Demandas/` nasce do **Destilado**, limpo. Ao concluir: análise → Notion (`📤`), card criado (`📝`), este arquivo → `04 Conhecimento/` (`status: refinado`).
>
> **Arquivado** — card destilado em [[QA Workspace/02 Demandas/DEV/10151 - Melhoria Filtros Criados Por Mim Ou Pelo Setor|SGV-10151]].

## O problema (task no Notion)

**Descrição** — Escopo da entrega: "Adiciona os filtros 'Criados por mim' ou 'Criados pelo setor' na barra de filtros e a funcionalidade na api." Notas de Design: "Criados por mim" ou "Criados pelo setor" depende da aba selecionada. É a **[PARTE 4]** da melhoria maior *[MELHORIA-CX] Melhoria no Layout da mesa de trabalho* (item pai, sem card próprio no vault).

**Saída esperada** — Botão de filtro rápido na barra de ferramentas da mesa, cujo rótulo e comportamento mudam conforme a aba ativa: "Criados por mim" filtra por `createdById` em "Meus documentos"; "Criados pelo setor" filtra por `createdBySectorId` em "Documentos do setor".

**Saída atual** — Funcionalidade inexistente até esta entrega.

**Entrega do dev** (B. Luan, 29/07/2026 — [MR !666](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/666), status Notion "Em ambiente teste/Dev") —

> Descrição das Alterações: Adiciona filtro de origem de criação na mesa de trabalho (`onlyCreatedByMeOrSector`) — na aba "Meus documentos" filtra por `createdById` e na aba "Documentos do setor" filtra por `createdBySectorId`, com tratamento para documentos migrados sem criador. Implementa a cláusula SQL `buildCreatedByClause` no backend, propagando o parâmetro por todas as queries da mesa (lista, painel, contagem de lista, contagem kanban). Extrai a lógica de toggle com debounce do botão de favoritos para o hook reutilizável `useDebouncedToggleFilter` e refatora o botão de favoritos para usá-lo. Cria o hook `useCreatedByFilter` com lógica de negócio: rótulo muda conforme aba ativa ("Criados por mim" / "Criados pelo setor") e botão é desabilitado quando não há setor para filtrar. Adiciona o botão de filtro "Criados por" na barra de ferramentas da mesa (arquivos list/desktop), ao lado do botão de favoritos, usando o ícone `PaperPlaneIcon` com variante preenchida/contornada. Refatora sistema de estilos da FilterToolbar — renomeia `FavoriteButton` para `ToggleFilterButton` genérico e adiciona `ToggleFilterLabel` com ghost span para evitar deslocamento de layout ao alternar bold. Adiciona ao `PaperPlaneIcon` suporte a variante filled com path SVG distinto. Corrige o cálculo de `effectiveSector` no `WorkBoardPage` usando a função extraída `resolveActiveTab` e reseta `onlyCreatedByMeOrSector` ao trocar de aba. Adiciona 3 chaves de tradução (`created-by-me`, `created-by-sector`, `created-by-disabled`). Adiciona 5 testes de integração no backend: filtro por criador pessoal, filtro por setor, documento sem criador, consistência entre contadores de lista e painel, e isolamento de tenant.
>
> Objetivo: Permitir que agentes públicos filtrem rapidamente a mesa de trabalho por documentos criados por eles mesmos ou pelo setor selecionado, sem precisar abrir o filtro avançado.
>
> Tela impactada: `/mesa-de-trabalho` (lista e painel). Endpoints impactados: `documentObjectsForWorkboard`, `documentObjectsCountForWorkboard`, `documentObjectsByAllStatus`, `documentObjectsCountByAllStatus`.

**Design & Referências** — Figma: https://www.figma.com/design/57GnUc1cTERzuMCdea2eQa/Mesa-de-Trabalho---Handoff?node-id=957-2978

---

## Análise

- **Causa raiz**: n/a — funcionalidade nova, não bug.
- **Evidências**: inspeção no Figma (Claude em Chrome), node 957-2978 e frames vizinhos.
  - **Rafael estava certo: são 3 estados, não 4.** As anatomias `957-2958` ("Favoritos"), `957-2968` (rotulada "Favoritos" na camada, mas o título dentro do frame é **"Criados por mim"** — a camada ficou com nome desatualizado) e `957-2978` ("Criados pelo setor") mostram, cada uma, **Default → Hover → Active**. Nenhuma das três desenha um 4º estado desabilitado — nem a de Favoritos, que é o componente de onde este toggle foi extraído (o dev cita reuso do hook de favoritos).
  - **É o mesmo componente, rótulo muda por aba** — confirmado nas duas anatomias: nota de design idêntica nas duas ("Ao ficar ativo, a mesa passa a exibir apenas os documentos criados [pelo usuário / pelo setor selecionado]. Ao ser clicado novamente (desativado), a visualização retorna ao estado padrão."), só troca o sujeito. Bate com o hook único `useCreatedByFilter` do dev.
  - **Ícone confirmado**: `PaperPlaneIcon` contornado (Default/Hover) e preenchido com borda azul (Active) — igual ao `⭐`/estrela do Favoritos, mesma linguagem visual.
  - **Posição confirmada** no frame "Anatomia - Alterações gerais na Mesa de Trabalho" → `tela-mesa-de-trabalho`: na barra de filtros, a ordem é `Pesquisa | Tipo de documento | Etiquetas | Pendências | ☆ Favoritos | ✈ Criados pelo setor | ⇅ | 🔽 (filtro avançado)` — o botão fica **imediatamente depois de Favoritos**, como o dev descreveu, e na mesma barra da busca, como a doc do módulo descreve. As duas descrições não divergem, só olham a barra de ângulos diferentes.
- **Hipóteses descartadas**: nenhuma — não havia hipótese de bug aqui, só a leitura de "quantos estados existem".

---

## Pontos a definir

- [x] ~~Ver no Figma os estados visuais do botão~~ → **Resolvido**: são 3 (Default/Hover/Active), confirmado nas 3 anatomias do padrão. Não existe estado desabilitado desenhado em nenhuma — nem na de Favoritos.
- [ ] **Sem lastro visual pro estado desabilitado.** Nem a doc de [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho#2. Filtros rápidos dinâmicos e inteligentes (Filter Buttons)|Mesa de trabalho]] nem o Figma definem "quando não há setor para filtrar" nem como o botão deve aparecer nesse estado (chave `created-by-disabled` é só do dev). Não é gate de doc no sentido de divergência — é ausência dos dois lados. Fica pendência pro card: **confirmar com o dev o cenário exato do gatilho** (nunca ficou claro em que situação "Documentos do setor" existe sem setor pra filtrar, já que a aba sempre carrega com um setor ativo pelo switch) antes de considerar o critério fechado.
- [ ] Comportamento com documento migrado sem criador (`createdById`/`createdBySectorId` nulos) — o dev cita tratamento explícito; precisa de um cenário próprio na validação, sem mockup de referência (é dado, não é UI).
- [ ] Reset do filtro ao trocar de aba — comportamento citado pelo dev (`reseta onlyCreatedByMeOrSector ao trocar de aba`), sem contrapartida no Figma (é estado de aplicação, não é visual) — vira CT mesmo assim, verificável em caixa preta.

---

## Destilado (rascunho do card)

> [!abstract] Só o problema — o que vai pro card, quase copy-paste: Descrição objetiva, passo a passo, resultado esperado, critérios de aceite, CTs. Nada de análise ou suposição.

### Descrição

Adiciona à barra de filtros da mesa de trabalho um botão de filtro rápido por origem de criação, ao lado do botão "Favoritos". O rótulo e o comportamento mudam conforme a aba ativa: **"Criados por mim"** em "Meus documentos" (filtra por `createdById`); **"Criados pelo setor"** em "Documentos do setor" (filtra por `createdBySectorId`). Parte 4 da melhoria de layout da mesa.

### Resultado Esperado

Botão com 3 estados visuais (Default/Hover/Active, ícone `PaperPlaneIcon` contornado/preenchido — mesma anatomia do botão Favoritos), rótulo trocando por aba, filtrando a listagem (lista e painel) e as contagens sem quebrar em documentos migrados sem criador.

### Critérios de aceite

*Agrupados na mesma ordem dos casos de teste.*

**A. Rótulo e filtro por aba**

- [ ] **CA1** — Na aba "Meus documentos", o botão exibe o rótulo "Criados por mim"; ativo, a listagem (lista e painel) mostra só documentos criados pelo usuário logado
- [ ] **CA2** — Na aba "Documentos do setor", o botão exibe o rótulo "Criados pelo setor"; ativo, a listagem mostra só documentos criados pelo setor ativo no switch

**B. Anatomia e posição do botão**

- [ ] **CA3** — O botão segue os 3 estados da anatomia vigente (Default contornado, Hover contornado destacado, Active preenchido com rótulo em negrito), ícone `PaperPlaneIcon` — mesma linguagem do botão Favoritos, ao lado do qual fica na barra

**C. Toggle e troca de aba**

- [ ] **CA4** — Clicar no botão ativo desativa o filtro; a listagem volta ao estado padrão (sem filtro de criador)
- [ ] **CA5** — Trocar de aba (Meus documentos ↔ Documentos do setor) reseta o filtro de criador pra desativado, mesmo se estava ativo antes da troca

**D. Dados e consistência**

- [ ] **CA6** — Documento migrado sem criador identificado não quebra a listagem nem aparece indevidamente com o filtro ativo (nem por `createdById` nem por `createdBySectorId`)
- [ ] **CA7** — Com o filtro ativo, a contagem exibida no modo Painel (por coluna) é consistente com a contagem do modo Lista

**E. Estado desabilitado** *(pendência aberta — ver Pontos a definir)*

- [ ] **CA8** — Quando não há setor disponível pra filtrar, o botão "Criados pelo setor" aparece com tratamento visual de desabilitado, sem interação — **cenário exato do gatilho a confirmar com o dev antes de executar**; não há mockup Figma nem regra de doc pra esse estado

> [!info]- Critérios fora desta rodada (registro)
> - Nenhum — refinamento cobre 100% do escopo declarado pelo dev. O CA8 fica **aberto** (não descartado): falta só o cenário de gatilho, não a existência do critério.

### Casos de Teste Básicos

Ver card — CTs escritos direto em `02 Demandas/DEV/` (fluxo pula a nota avulsa por já ter destilado completo nesta rodada).

---

## Histórico do refinamento

- 2026-08-10 - Material recebido (export do Notion, `sgv-10151.md`)
- 2026-08-10 - Análise no Figma (Claude em Chrome, node 957-2978 e anatomias vizinhas): confirmados os 3 estados do toggle (Default/Hover/Active), nenhuma anatomia do padrão desenha estado desabilitado, posição do botão na barra confirmada. Destilado fechado com 8 critérios; CA8 (desabilitado sem setor) fica pendente de confirmar o gatilho com o dev.
