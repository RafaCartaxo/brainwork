---
tags:
  - qa
  - conhecimento
tipo: referencia
revisado: 2026-08-25
---
# NX Gest - Handoff de execução

> [!info] Sobre esta nota
> Documento de transição para **outra sessão de IA executar** os planos do repo pessoal `RafaCartaxo/nxgest` — **não é sistema Sogov**.
> Esta nota é a **camada de orquestração**: ordem, setup, colisões entre planos e regras transversais. Os passos de cada plano vivem nas quatro notas de plano — **não estão duplicados aqui de propósito**, para não criar duas fontes que divergem.

> [!important] Para a IA executora — leia isto primeiro
> 1. Cada plano tem sua nota com **checklist de execução e vetos permanentes**. Essas notas são a fonte de verdade dos passos.
> 2. Este handoff manda na **ordem** e nas **regras transversais**. Onde houver conflito entre este documento e a nota de um plano, **este documento perde** — a nota do plano é mais específica; sinalize a divergência em vez de escolher em silêncio.
> 3. **Nada foi executado ainda.** O repo não está clonado. Todos os planos estão em estado de planejamento.
> 4. Quando um passo depender de decisão que não está escrita: **pare e pergunte**. A lista de decisões pendentes está no fim.

## Fonte de verdade por plano

| Plano | Nota (passos + vetos) | Natureza | Toca código? |
|---|---|---|---|
| Identidade / posicionamento | [[NX Gest - Reposicionamento de identidade (PLAN-085)]] | docs + 3 strings | mínimo (2 arquivos) |
| Insights / gráficos | [[NX Gest - Insights e gráficos (PLAN-080)]] | correção do plano + fases | Fase 0.5 = doc-only |
| Navegação escalável | [[NX Gest - Navegação escalável (PLAN-081)]] | refactor + overflow | sim, frontend |
| 3º modelo de contrato | [[NX Gest - Contrato periodicidade alternada (PLAN-087)]] | domínio + UI + 2 BRs | sim, back + front |

## Setup (uma vez, antes de qualquer plano)

1. **Clonar** `https://github.com/RafaCartaxo/nxgest` — o repo **não está** na máquina. Definir o destino com o dono (sugestão: `~/Documentos/Sogov/nxgest`).
2. `nvm use 20` — Node ≥20 é obrigatório (CI e `react-router@7`).
3. `npm install` na raiz (monorepo com workspaces — instala backend e frontend).
4. **Capturar o baseline dos 6 gates** e guardar a saída literal:

```bash
npm run audit:links     # esperado: "0 erro(s)"
npm run docs:audit      # esperado: "Nenhuma divergência encontrada."
npm run audit:modules   # esperado: "manifest coerente"
npm run audit:ui
npm run audit:styles
npm test
```

> [!warning] O baseline das notas está datado
> As saídas registradas nas notas foram medidas em **21/08/2026** num clone descartável. O `docs:audit` compara doc contra código — qualquer commit no repo desde então move a linha de partida. **Meça de novo antes de começar** e use a sua medição como referência, não a das notas. Se algum gate já vier sujo, isso é dívida pré-existente: registre e siga, não tente consertar dentro destes planos.

## Ordem de execução

Sequencial, **um plano por branch**, nunca em paralelo (ver Colisões abaixo).

| # | O quê | Por que nessa posição | Tamanho |
|---|---|---|---|
| **1** | **PLAN-080 — apenas a Fase 0.5** | O `PLAN-080` no repo hoje **instrui a fazer o que foi decidido não fazer** (expandir `dependsOn`, construir gráfico sobre `snapshots_atraso`). É doc-only, independente, e para o repo de desinformar. Maior prevenção pelo menor custo. | ~30 min |
| **2** | **Identidade** (a nota do PLAN-085) | Docs + 3 strings, autocontido. Inclui a copy preventiva do e-mail de convite, que mitiga o incidente real de link inválido. | médio |
| **3** | **3º modelo de contrato** (nota do PLAN-087) | Único que entrega valor direto ao usuário: modelo que os clientes já usam e o sistema não representa. Toca domínio + UI + 2 BRs. | médio |
| **4** | **Erros do link de convite** (o plano de convite descrito na nota do PLAN-085, anexo) | Corrige incidente de produção que travou duas pessoas. Código + BR + UC/CT. | médio |
| **5** | **PLAN-081 — Fase 1 e 2** | Refactor de higiene (`nav.ts`) + aba "Mais". Sem valor visível ao usuário na Fase 1. Não bloqueia nada. | médio |

**Não executar:** a Fase 2 do PLAN-081 original (sidebar colapsável) — foi cortada do escopo. E nenhuma fase do PLAN-080 além da 0.5 sem decisão do dono.

## Colisões entre planos (o motivo de ser sequencial)

Estes arquivos são tocados por **mais de um** plano. Executar em branches paralelas gera conflito em todos eles:

| Arquivo | Planos que tocam |
|---|---|
| `docs/skills/SKILL-009-documentation-sync.md` §3 | Identidade **e** 3º modelo (cada um adiciona uma linha na matriz) |
| `docs/plans/README.md` | Identidade, convite, 3º modelo (cada um registra seu plano) |
| `docs/UPDATES.md` · `docs/STATUS.md` | **todos** |
| `docs/product/01-DOMAIN.md` | Identidade (opcional) **e** 3º modelo (periodicidade) |
| `src/shared/email/templates.ts` | Identidade (`marca` + `convite.seguro`) |

## Atribuição de números — regra dura

> [!warning] Não pré-reservar número
> Os rótulos `PLAN-085`, `PLAN-086` e `PLAN-087` usados nos títulos das notas são **provisórios**. No repo o último plano é o **PLAN-084** e o BR mais alto é o **BR-106** (verificado em 25/08).

- **PLAN:** cada plano recebe o **próximo número livre no momento em que o arquivo é criado**, na ordem em que efetivamente entrar. Com a ordem acima, o de identidade vira `PLAN-085`, o de contrato `PLAN-086`, o de convite `PLAN-087` — **mas confira o último número no repo antes**, porque outro plano pode ter nascido nesse meio-tempo.
- **BR:** mesma regra, sequencial a partir do próximo livre. O 3º modelo precisa de **2 BRs**; o de convite precisa de **1**. Quem entrar primeiro leva os números menores.
- **ADR:** o de identidade cria o **ADR-007** (ADR-006 é o último). Não há disputa.
- **Ao criar cada arquivo, anote o número real na nota do vault correspondente** — para o título provisório deixar de enganar.

## Regras transversais (valem em todos os planos)

- **`git diff --name-status` só com `M` e `A`.** Nenhum `R` (rename) nem `D` (delete) — renomear ou mover um `.md` quebra o `audit:links`.
- **BR é imutável.** Regra alterada = BR nova com nota de revogação apontando a antiga. Nunca reescrever BR existente, nunca reutilizar número.
- **Não dividir `docs/product/02-BUSINESS-RULES.md`** por nível, tema ou vertical. Split ⇒ rename ⇒ link quebrado.
- **Não reescrever histórico.** `docs/plans/Lovable-*`, `Stitch-*` e `docs/plans/arquivo/**` estão marcados `✅ Histórico`/`Superseded`. São o rastro que prova a evolução — política do PLAN-084.
- **Não renomear `nxgestao`.** Ocorrências em `/opt/nxgestao`, volumes, rede Docker, staging DuckDNS e `~/.config/nxgestao/` são infraestrutura em produção. Renomear é migração com risco de perda de volume — proibido pelo PLAN-084.
- **Não tocar o Module Manifest** (`src/modules/admin/domain/modules.ts` e o espelho em `frontend/src/shared/modules/modules.ts`) fora do plano de navegação. Validação: `audit:modules` byte-idêntico ao baseline.
- **Rodar os gates ao fim de cada plano** e comparar com o baseline **daquele** plano, não com o das notas.
- **`gh` não está instalado.** Se o dono quiser PR, instalar/autenticar antes ou subir a branch e abrir pelo navegador.
- **Após qualquer mudança de código, aplicar a matriz de propagação** da `SKILL-009` e rodar `npm run docs:audit`. É regra do próprio repo (`AGENTS.md`).

## Decisões pendentes — pare e pergunte

Nenhuma destas está resolvida. **Não escolher em silêncio.**

- [ ] **Onde clonar**, nome da branch (sugestão: uma por plano, ex. `docs/reposicionamento-plataforma`), e se fica commit local para revisão ou vai a PR.
- [ ] **A Fase 0.5 do PLAN-080 entra isolada** (recomendado) ou espera para entrar junto com a execução do plano inteiro?
- [ ] **`PLAN-071` está `⏳ Em execução`** e a l.69-70 documenta cor primária `#0520ae`, mas `templates.ts:63` usa `#3571eb`. Mudança legítima de tema ou doc estagnada? **Não corrigir às cegas** — o plano de identidade só anota uma linha de rastreio.
- [ ] **Contagens estagnadas do `04-ROADMAP` §Estado Atual** (diz 18 telas; `docs:audit` mede 28). Dívida pré-existente, o gate não checa. Registrar no `BACKLOG.md` — **não** corrigir dentro destes planos.
- [ ] **Meta de verdade** (admin define alvo por operador/período) para o gráfico de performance — se o dono quiser, é plano próprio; o de insights entrega "previsto × recebido".

## Verificação final (depois de todos os planos)

```bash
npm run audit:links && npm run docs:audit && npm run audit:modules
npm run audit:ui && npm run audit:styles
npx tsc --noEmit && npm run build && node scripts/check-dist.mjs
npm test
npm run smoke:api      # requer instância isolada — ver "Como executar" na 07
git diff --name-status # somente M e A
```

Leitura corrida do `docs/foundation/00-NORTH-STAR.md` conferindo que os dois níveis (plataforma × vertical) não se contradizem — é o **teste de pronto** do plano de identidade.

## Cards relacionados

- Nenhum. Produto próprio, fora do escopo Sogov.

## Referências

- As quatro notas de plano: [[NX Gest - Reposicionamento de identidade (PLAN-085)]] · [[NX Gest - Insights e gráficos (PLAN-080)]] · [[NX Gest - Navegação escalável (PLAN-081)]] · [[NX Gest - Contrato periodicidade alternada (PLAN-087)]]
- Contrato universal do repo para agentes: `AGENTS.md` na raiz
- Governança de doc do repo: `docs/skills/SKILL-009-documentation-sync.md` · `docs/CONTRIBUTING.md`
- Convenções deste vault: [[../../../Sistema/Contexto/REGRAS_IA|REGRAS_IA]] · [[../README|04 Conhecimento]] regra 2
