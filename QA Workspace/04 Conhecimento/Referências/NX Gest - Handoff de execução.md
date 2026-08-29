---
tags:
  - qa
  - conhecimento
tipo: referencia
revisado: 2026-08-28
---
# NX Gest - Handoff de execução

> [!info] Sobre esta nota
> Documento de transição para **outra sessão de IA executar** os planos do repo pessoal `RafaCartaxo/nxgest` — **não é sistema Sogov**.
> Esta nota é a **camada de orquestração**: ordem, setup, colisões entre planos e regras transversais. Os passos de cada plano vivem nas notas de plano — **não estão duplicados aqui de propósito**, para não criar duas fontes que divergem.

> [!important] Para a IA executora — leia isto primeiro
> 1. Cada plano tem sua nota com **checklist de execução e vetos permanentes**. Essas notas são a fonte de verdade dos passos.
> 2. Este handoff manda na **ordem** e nas **regras transversais**. Onde houver conflito entre este documento e a nota de um plano, **este documento perde** — a nota do plano é mais específica; sinalize a divergência em vez de escolher em silêncio.
> 3. **Estado atualizado em 28/08:** o **3º modelo de contrato (`alternada`) foi executado** — virou o **PLAN-085 do repo**, implementado e **em produção** (27/08). O repo está **clonado** em `~/Documentos/Desenvolvimento/nxgestao` e `gh` está disponível. Os demais planos seguem pendentes.
> 4. Quando um passo depender de decisão que não está escrita: **pare e pergunte**. A lista de decisões pendentes está no fim.

## Fonte de verdade por plano

| Plano | Nota (passos + vetos) | Natureza | Toca código? |
|---|---|---|---|
| Identidade / posicionamento | [[NX Gest - Reposicionamento de identidade (PLAN-086)]] | docs + 3 strings | mínimo (2 arquivos) |
| Insights / gráficos | [[NX Gest - Insights e gráficos (PLAN-080)]] | correção do plano + fases | Fase 0.5 = doc-only |
| Navegação escalável | [[NX Gest - Navegação escalável (PLAN-081)]] | refactor + overflow | sim, frontend |
| ~~3º modelo de contrato~~ | [[NX Gest - Contrato periodicidade alternada (PLAN-085)]] — **executado** | domínio + UI + 2 BRs | ✅ feito (PLAN-085, em prod) |

## Setup (uma vez, antes de qualquer plano)

1. **Repo clonado em `~/Documentos/Desenvolvimento/nxgestao`** (28/08) — o passo de clonar já está feito; confirmar `git status` limpo antes de trabalhar (há favicons pendentes de outra sessão, fora destes planos).
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
> As saídas registradas nas notas foram medidas em **21/08/2026** num clone descartável. O `docs:audit` compara doc contra código — qualquer commit no repo desde então move a linha de partida. **Meça de novo antes de começar** e use a sua medição como referência, não a das notas. Se algum gate já vier sujo, isso é dívida pré-existente: registre e siga, não tente consertar dentro destes planos. (Referência de 28/08: testes **172**, smoke CI **278**.)

## Ordem de execução

Sequencial, **um plano por branch**, nunca em paralelo (ver Colisões abaixo). **Atualizado em 28/08** — o item 3 (3º modelo de contrato) já foi executado.

| # | O quê | Por que nessa posição | Tamanho | Estado |
|---|---|---|---|---|
| ~~**1**~~ | ~~PLAN-080 — apenas a Fase 0.5~~ | O `PLAN-080` no repo hoje **instrui a fazer o que foi decidido não fazer** (expandir `dependsOn`, construir gráfico sobre `snapshots_atraso`). É doc-only, independente, e para o repo de desinformar. | ~30 min | ✅ **feito (28/08)** — organização |
| **1** | **Identidade** (→ PLAN-086) | Docs + strings + ADR-007. **Revisado 28/08:** a copy preventiva do e-mail de convite foi entregue no PLAN-087. | médio | ✅ **executado como PLAN-086 (28/08)** |
| ~~**3**~~ | ~~**3º modelo de contrato**~~ | ~~Único que entrega valor direto ao usuário~~ | — | ✅ **executado como PLAN-085 (27/08, em prod)** |
| **2** | **Erros do link de convite** (→ PLAN-087) | Corrige incidente de produção que travou duas pessoas. Código + BR + UC/CT + copy preventiva do e-mail. | médio | ✅ **executado como PLAN-087 (28/08)** |
| **3** | **PLAN-081 — Fase 1 e 2** | Refactor de higiene (`nav.ts`) + aba "Mais". Sem valor visível ao usuário na Fase 1. Não bloqueia nada. | médio | ⏳ pendente |

**Não executar:** a Fase 2 do PLAN-081 original (sidebar colapsável) — foi cortada do escopo. E nenhuma fase do PLAN-080 além da 0.5 sem decisão do dono.

## Colisões entre planos (o motivo de ser sequencial)

Estes arquivos são tocados por **mais de um** plano. Executar em branches paralelas gera conflito em todos eles (**atualizado 28/08**: o 3º modelo já executou e não toca mais):

| Arquivo | Planos que tocam |
|---|---|
| `docs/skills/SKILL-009-documentation-sync.md` §3 | Identidade **e** 3º modelo (já adicionou sua linha no PLAN-085) |
| `docs/plans/README.md` | Identidade, convite, (3º modelo já registrado como PLAN-085) |
| `docs/UPDATES.md` · `docs/STATUS.md` | **todos** |
| `docs/product/01-DOMAIN.md` | Identidade (opcional) **e** 3º modelo (periodicidade — já feita no PLAN-085) |
| `src/shared/email/templates.ts` | Identidade (`marca` + `convite.seguro`) |

## Atribuição de números — regra dura

> [!warning] Não pré-reservar número
> Os rótulos das notas de identidade e convite ainda são **provisórios**. **No repo o último plano é o PLAN-085** (alternada, executado) e o BR mais alto é o **BR-108** (verificado em 28/08).

- **PLAN:** cada plano recebe o **próximo número livre no momento em que o arquivo é criado**, na ordem em que efetivamente entrar. Estado real em 28/08: **alternada = PLAN-085** (executado) · **convite = PLAN-087** (executado); **identidade → PLAN-086** (pendente) — **mas confira o último número no repo antes**, porque outro plano pode ter nascido nesse meio-tempo.
- **BR:** mesma regra, sequencial a partir do próximo livre. O 3º modelo usou **BR-107 e BR-108**; o convite usou **BR-109**. O de identidade não precisa de BR.
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
- **`gh` disponível** (28/08) — push/PR podem ser feitos via CLI. Usar commits convencionais do repo.
- **Após qualquer mudança de código, aplicar a matriz de propagação** da `SKILL-009` e rodar `npm run docs:audit`. É regra do próprio repo (`AGENTS.md`).

## Decisões pendentes — pare e pergunte

Nenhuma destas está resolvida. **Não escolher em silêncio.**

- [x] **Onde clonar / branch** — resolvido: repo em `~/Documentos/Desenvolvimento/nxgestao`; commits diretos em `main` (não via PR) é o padrão atual do dono.
- [x] **A Fase 0.5 do PLAN-080** — resolvido: aplicada isolada em 28/08 (organização), como recomendado.
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

- As notas de plano: [[NX Gest - Reposicionamento de identidade (PLAN-086)]] · [[NX Gest - Insights e gráficos (PLAN-080)]] · [[NX Gest - Navegação escalável (PLAN-081)]] · [[NX Gest - Contrato periodicidade alternada (PLAN-085)]]
- Contrato universal do repo para agentes: `AGENTS.md` na raiz
- Governança de doc do repo: `docs/skills/SKILL-009-documentation-sync.md` · `docs/CONTRIBUTING.md`
- Convenções deste vault: [[../../../Sistema/Contexto/REGRAS_IA|REGRAS_IA]] · [[../README|04 Conhecimento]] regra 2
